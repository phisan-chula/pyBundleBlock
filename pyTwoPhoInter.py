#
#
#
PROG_TWOPHOTOINTER='''
pyTwoPhoInter.py : Perform two photos intersection, get two EOPs of two 
                   photos. One compute ground coordinate from measured 
                   photo coordinate on the two photos each.

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
import argparse
from pyBundleBlock import *    # derived from ....

#######################################################################
class TwoPhotoInter(BundleBlock):
    def __init__( self , YAML ):
        ''' read YAML and restructure to dfOBS '''
        with open( YAML, 'r' ) as f:
            self.YAML = yaml.safe_load(f)
        #import pdb; pdb.set_trace()
        if 'EOP' not in  self.YAML.keys():
            raise RuntimeError('***ERROR no "EOP in TwoPhotoIntersection" YAML!!!')
        eops = list() ; pho_coord = list()
        for photo,eop in self.YAML['EOP'].items():
            eops.append( [ str(photo), eop['XYZ'], eop['OPK'] ] )
        self.dfEOP = pd.DataFrame( eops, columns=['Photo_Name', 'XYZ', 'OPK'] )
        for photo,data in self.YAML['Image'].items():
            for pnt,(xp,yp) in data.items():
                pho_coord.append( [ str(photo), str(pnt), xp, yp ] )
        #############################################################
        self.InteriorOrient( pho_coord )
        self.dfMEAS = self.dfPho
        print('==================== Input Measurement ====================')
        print( self.dfPho )
        #############################################################
        for tp,grp in self.dfMEAS.groupby('Pnt_Name'):
            if len(grp)<=1: 
                raise f'***ERROR*** TP "{tp}" measured once on "{grp.iloc[0].Photo}"'

    def DoAdjustment(self):
        self.Params = Parameters()
        for tp,grp in self.dfMEAS.groupby('Pnt_Name'):
            for i in 'XYZ':
                INIT = 10. if i in 'Z' else  1000.
                self.Params.add( f'{tp}_{i}', value=INIT )
        minner = Minimizer( self.ColinFunc2min, self.Params )
        self.RESULT = minner.minimize( method='leastsq')
        self.dfMEAS[['vx_mm','vy_mm']] = self.RESULT.residual.reshape(-1,2)
        self.dfMEAS[['vx_px','vy_px']] = \
                self.dfMEAS[['vx_mm','vy_mm']]/(self.YAML['Project']['ScanRes']/1000) 

    def ColinFunc2min(self, Params):
        def getUnkParams( self, SYMBOL, SUFFIX ):
            par = list()
            for i in SUFFIX: par.append( Params[ f'{SYMBOL}_{i}'].value )
            return par
        residu = list()
        for i,row in  self.dfMEAS.iterrows():
            eop = self.dfEOP[ self.dfEOP.Photo_Name==row.Photo].iloc[0]
            EOP = eop.XYZ + list(np.radians(eop.OPK))
            XYZ_G = getUnkParams( Params, row.Pnt_Name, 'XYZ' )
            xp_,yp_ = self.World2Photo( EOP, XYZ_G )
            residu.extend( [xp_-row.xp_mm, yp_-row.yp_mm ] )  # residual vector
        return residu   # model-data

##############################################################################
if __name__=="__main__":
    parser = argparse.ArgumentParser(description=PROG_TWOPHOTOINTER)
    parser.add_argument('YAML', help='input two-photo intersection file in YAML format' )
    args = parser.parse_args()
    print( PROG_TWOPHOTOINTER )
    print(f'Reading YAML "{args.YAML}" ...\n')
    bb = TwoPhotoInter( args.YAML )
    bb.DoAdjustment()
    #report_fit( bb.RESULT )     # lmfit provide convenient function to blow out 'RESULT'
    ##############################################################################
    print( '====== Adjusted Parameters and Precision ======')
    for tp,grp in bb.dfMEAS.groupby('Pnt_Name'):
        for i in 'XYZ':
            UNK = bb.RESULT.params[ f'{tp}_{i}' ]
            print(  f'{UNK.name:10} {UNK.value:12.3f} m.     +/-{UNK.stderr:.3f} m.' )
    print( '====================== Residual ==============================')
    print( '--Photo--------Point-----vx_mm----vy_mm-----vx_px----vy_px---')
    for i,row in  bb.dfMEAS.sort_values(by=['Photo','Pnt_Name']).iterrows():
        print( f'{row.Photo:12} {row.Pnt_Name:10}'\
               f'{row.vx_mm:8.4f} {row.vy_mm:8.4f} {row.vx_px:8.1f} {row.vy_px:8.1f}' )
    print( '====================== program stop =========================')
    #import pdb; pdb.set_trace()
