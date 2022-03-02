#
PROG='''
pyBundle.py : Perform bundle block adjustment computation using 'lmfit'
              The program benefits modern and convenient  pythonic paramdigm.
              It incoperates Lmfit for least square adjustment computations
              and solve non-linear bundle block problem with Levenberg-
              Marquardt algorithm (LMA). The damped iterative solution can
              result which may be more robust than the traditional Gauss-Markov
              solution.
Author   : P.Santitamnont
           Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand

History  : 22 Feb 2022  Initial
           1  Mar 2022  Observation in pixel via IOP K Matrix'''
#
import pandas as pd
import geopandas as gpd
import yaml
import numpy as np
from lmfit import minimize, Minimizer, Parameters, report_fit
from tabulate import tabulate
import argparse
#######################################################################
def RotationMatrix(OmePhiKap, MODE=None):
    ''' Notation:  Pix4D, Digital Photogrammetry (P.Santitamnont) '''
    (Ome,Phi,Kap) = OmePhiKap
    coso = np.cos(Ome) ; sino = np.sin(Ome)
    cosp = np.cos(Phi) ; sinp = np.sin(Phi)
    cosk = np.cos(Kap) ; sink = np.sin(Kap)
    r11 = cosk*cosp               ; r12 = -sink*cosp              ; r13 = sinp
    r21 = cosk*sino*sinp+sink*coso; r22 = cosk*coso-sink*sino*sinp; r23 = -sino*cosp
    r31 = sink*sino-cosk*coso*sinp; r32 = sink*coso*sinp+cosk*sino; r33 = coso*cosp
    return (r11,r12,r13,r21,r22,r23,r31,r32,r33)
#######################################################################
class BundleBlock:
    def __init__( self , YAML ):
        ''' read YAML and restructure to dfMEAS '''
        with open( YAML, 'r' ) as f:
            self.YAML = yaml.safe_load(f)
        gcps = list() ; pho_coord = list()
        for k,(X,Y,Z) in self.YAML['GCP'].items():
            gcps.append( [ str(k),X,Y,Z ] )
        dfGCP = pd.DataFrame( gcps, columns=['GCP_Name', 'X', 'Y', 'Z' ] )
        for photo,data in self.YAML['Image'].items():
            for pnt,(xp,yp) in data.items():
                pho_coord.append( [ str(photo), str(pnt), xp, yp ] )
        ###########################################################
        self.InteriorOrient( pho_coord )
        print(28*'='+'Input Measurement'+28*'=')
        print( self.dfPho.to_markdown() )
        ###########################################################
        self.dfMEAS = self.dfPho.merge( dfGCP,how='inner', left_on='Pnt_Name', 
                                      right_on='GCP_Name', copy =True )
        print('==================== Input GCPs ====================')
        print( pd.unique(dfGCP.GCP_Name) )
        print('=================== Used GCPs ====================')
        print( pd.unique(self.dfMEAS.GCP_Name) ) 
        print('====================================================')
        onGCP = pd.notna(self.dfMEAS.GCP_Name)
        print(60*'=')
        self.dfGCPs = self.dfMEAS[  onGCP ].copy()
        self.dfTPs  = self.dfMEAS[ ~onGCP ].copy()
        for tp,grp in self.dfTPs.groupby('Pnt_Name'):
            if len(grp)<=1: raise f'***ERROR*** TP "{tp}" measured once on'\
                                  f' "{grp.iloc[0].Photo}"'

    def InteriorOrient(self, pho_coord):
        #import pdb; pdb.set_trace()
        if 'UNIT_IOP' not in self.YAML['Project'].keys():  # already 'mm'
            self.dfPho = pd.DataFrame( pho_coord, 
                         columns=['Photo', 'Pnt_Name', 'xp_mm', 'yp_mm' ] )
            return  # already 'mm'
        self.dfPho = pd.DataFrame( pho_coord,
                         columns=['Photo', 'Pnt_Name', 'jx_px', 'iy_px' ] )
        if self.YAML['Project']['UNIT_IOP']=='mm2px':
            for photo,kmat in self.YAML['IOP'].items():
                self.YAML['IOP'][photo] = np.matrix(kmat).I
        elif self.YAML['Project']['UNIT_IOP']=='px2mm':
            for photo,kmat in self.YAML['IOP'].items():
                self.YAML['IOP'][photo] = np.matrix(kmat)
        else:
            raise f'***ERROR*** unkonwn UNIT_IOP {self.YAML}'
        def PX2MM( row, K_Mats ):
            #import pdb; pdb.set_trace()
            xpyp = K_Mats[row.Photo]*np.matrix( [row.jx_px,row.iy_px,1] ).T
            return pd.Series( [ xpyp[0,0],xpyp[1,0] ]  )
        self.dfPho[['xp_mm','yp_mm']] = self.dfPho.apply( PX2MM, axis=1, 
                                         args=( self.YAML['IOP'],)  )
        self.dfPho[['xp_mm','yp_mm']] = self.dfPho[['xp_mm','yp_mm']].round(4) 

    def DoAdjustment(self):
        self.Params = Parameters()
        for photo,grp in  self.dfGCPs.groupby('Photo'):
            for i in 'XYZOPK':     # Initital XYZ are critical, need 'good' initials
                INIT = 1000. if i in 'XYZ' else  0.
                self.Params.add( f'{photo}_{i}' , value=INIT , vary=True )
        for tp,grp in self.dfTPs.groupby('Pnt_Name'):
            for i in 'XYZ':
                INIT = 10. if i in 'Z' else  1000.
                self.Params.add( f'{tp}_{i}', value=INIT )
        minner = Minimizer( self.ColinFunc2min, self.Params )
        self.RESULT = minner.minimize( method='leastsq')
        self.dfMEAS[['vx_mm','vy_mm']] = self.RESULT.residual.reshape(-1,2)
        self.dfMEAS[['vx_px','vy_px']] =\
                self.dfMEAS[['vx_mm','vy_mm']]/(self.YAML['Project']['ScanRes']/1000) 

    def ColinFunc2min(self, Params):
        def getUnkParams( self, SYMBOL, SUFFIX ):
            par = list()
            for i in SUFFIX: par.append( Params[ f'{SYMBOL}_{i}'].value )
            return par
        residu = list()
        for i,row in  self.dfGCPs.iterrows():
            EOP = getUnkParams( Params, row.Photo, 'XYZOPK' )
            xp_,yp_ = self.World2Photo( EOP, [row.X,row.Y,row.Z] )
            residu.extend( [xp_-row.xp_mm, yp_-row.yp_mm ] )  # residual vector
        for i,row in  self.dfTPs.iterrows():
            EOP    = getUnkParams( Params, row.Photo, 'XYZOPK' )
            XYZ_TP = getUnkParams( Params, row.Pnt_Name, 'XYZ' )
            xp_,yp_ = self.World2Photo( EOP, XYZ_TP ) 
            residu.extend( [xp_-row.xp_mm, yp_-row.yp_mm ] )  # residual vector
        return residu   # model-data

    def World2Photo( self, EOP, XYZ_G ):
        ''' colinearity equation convert XYZ_G meter to photo xp_mm,yp_mm'''
        XG,YG,ZG = XYZ_G   ;  X0,Y0,Z0 = EOP[:3]
        r11,r12,r13,r21,r22,r23,r31,r32,r33 = RotationMatrix( EOP[3:] )
        nom_xp = r11*(XG-X0)+r21*(YG-Y0)+r31*(ZG-Z0)
        nom_yp = r12*(XG-X0)+r22*(YG-Y0)+r32*(ZG-Z0)
        denom  = r13*(XG-X0)+r23*(YG-Y0)+r33*(ZG-Z0)
        #xp = self.x0 - self.FocLen*nom_xp/denom
        #yp = self.y0 - self.FocLen*nom_yp/denom
        f = self.YAML['Project']['FocLen']  # mm
        xp_mm = 0 - f*nom_xp/denom
        yp_mm = 0 - f*nom_yp/denom
        return (xp_mm,yp_mm)

##############################################################################
if __name__=="__main__":
    parser = argparse.ArgumentParser(description=PROG)
    parser.add_argument('YAML', help='input photogrammetric bundle file in YAML format' )
    args = parser.parse_args()
    print( PROG )
    print(f'Reading YAML "{args.YAML}" ...\n')
    bb = BundleBlock( args.YAML )
    bb.DoAdjustment()
    #report_fit( bb.RESULT )     # lmfit provide convenient function to blow out 'RESULT'
    ##############################################################################
    PAR = list()
    print( '====== Adjusted Parameters and Precision ======')
    for photo,grp in bb.dfMEAS.groupby('Photo'):
        for i in 'XYZOPK': 
            UNK = bb.RESULT.params[ f'{photo}_{i}' ]
            if i in 'XYZ':
                PAR.append( [ f'{UNK.name:10}', f'{UNK.value:12.3f} m',
                              f'+/-{UNK.stderr:.3f} m' ] ) 
            else:
                PAR.append( [ f'{UNK.name:10}', f'{np.degrees(UNK.value):12.6f} deg',
                       f'+/-{np.degrees(UNK.stderr)*3600:.0f} sec' ] ) 
    for tp,grp in bb.dfTPs.groupby('Pnt_Name'):
        for i in 'XYZ':
            UNK = bb.RESULT.params[ f'{tp}_{i}' ]
            PAR.append( [ f'{UNK.name:10}', f'{UNK.value:12.3f} m.',
                          f'+/-{UNK.stderr:.3f} m.' ] )
    print( tabulate( PAR, ['Parameter','Value','Precision'], tablefmt='github' ) )
    #import pdb; pdb.set_trace()
    RES = list()
    print( '====================== Residual ==============================')
    for i,row in  bb.dfMEAS.sort_values(by=['Photo','Pnt_Name']).iterrows():
        RES.append( [ f'{row.Photo:12}', f'{row.Pnt_Name:10}', f'{row.vx_mm:+8.4f}',
                      f'{row.vy_mm:+8.4f}', f'{row.vx_px:+8.1f}',f'{row.vy_px:+8.1f}' ] )
    print( tabulate( RES, ['Photo','Point','vx_mm', 'vy_mm', 'vx_px', 'vy_px'], 
                     tablefmt='github' ) )
    print( '====================== program stop =========================')
