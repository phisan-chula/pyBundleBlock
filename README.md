# pyBundleBlock

pyBundleBlock.py : Perform bundle block adjustment computation using 'lmfit'</br>
        The program benefits modern and convenient  pythonic paramdigm.</br>
        It incoperates Lmfit for least square adjustment computations</br>
        and solve non-linear bundle block problem with Levenberg-</br>
        Marquardt algorithm (LMA). The damped iterative solution can</br>
        result which may be more robust than the traditional Gauss-Markov</br>
        solution.</br>
Author   : P.Santitamnont</br>
           Faculty of Engineering, Chulalongkorn University, Bangkok, Thailand</br>
</br>
History  : 22 Feb 2022  Initial</br>
</br>
</br>
<H1>Example Result</H1>
<H2>Reading YAML "Block_62_63_6TP_TLE2020px.yml" ...</H2>

==================== Input Measurement ====================
     Photo Pnt_Name    jx_px    iy_px     xp_mm    yp_mm
0   P62_15    40401   9840.1  -2376.6   34.2148  77.8308
1   P62_15    40501  13847.1  -2155.5   94.3682  81.1493
2   P62_15    30301   6563.1  -8907.7  -14.9802 -20.2166
3   P62_15    30401  10098.1  -7945.7   38.0876  -5.7753
4   P62_15    20301   7534.0 -13325.9   -0.4052 -86.5450
5   P62_15    20401  10160.2 -13288.9   39.0196 -85.9900
6   P62_15       t1   8494.2 -11029.6   14.0096 -52.0720
7   P62_15       t2  10081.9  -9718.9   37.8443 -32.3954
8   P62_15       t3  11374.6 -10245.2   57.2504 -40.2967
9   P62_15       t4  10324.4  -7793.9   41.4849  -3.4964
10  P62_15       t5   9578.8  -7418.1   30.2919   2.1454
11  P62_15       t6   9351.6  -5323.3   26.8812  33.5936
12  P63_15    40401   3819.3  -2552.0  -56.1696  75.1969
13  P63_15    40501   7940.2  -2354.9    5.6915  78.1541
14  P63_15    30301    458.4  -9075.0 -106.6204 -22.7222
15  P63_15    30401   4110.3  -8135.0  -51.7999  -8.6127
16  P63_15    20301   1358.3 -13529.1  -93.1104 -89.5854
17  P63_15    20401   3902.2 -13518.0  -54.9224 -89.4197
18  P63_15       t1   2403.2 -11223.7  -77.4254 -54.9782
19  P63_15       t2   3927.4  -9920.9  -54.5450 -35.4217
20  P63_15       t3   5176.8 -10462.1  -35.7894 -43.5464
21  P63_15       t4   4328.7  -7984.9  -48.5214  -6.3595
22  P63_15       t5   3600.8  -7601.3  -59.4484  -0.6008
23  P63_15       t6   3130.3  -5503.1  -66.5119  30.8966
==================== Input GCPs ====================
['40401' '40501' '30301' '30401' '20301' '20401']
=================== Used GCPs ====================
['40401' '40501' '30301' '30401' '20301' '20401']
====================================================
============================================================
====== Adjusted Parameters and Precision ======
<table>
<thead>
<tr><th>Parameter  </th><th>Value        </th><th>Precision  </th></tr>
</thead>
<tbody>
<tr><td>P62_15_X   </td><td>3708.724 m   </td><td>+/-0.171 m </td></tr>
<tr><td>P62_15_Y   </td><td>2100.812 m   </td><td>+/-0.133 m </td></tr>
<tr><td>P62_15_Z   </td><td>2258.521 m   </td><td>+/-0.058 m </td></tr>
<tr><td>P62_15_O   </td><td>2.194102 deg </td><td>+/-12 sec  </td></tr>
<tr><td>P62_15_P   </td><td>-0.432875 deg</td><td>+/-17 sec  </td></tr>
<tr><td>P62_15_K   </td><td>-2.216435 deg</td><td>+/-3 sec   </td></tr>
<tr><td>P63_15_X   </td><td>4908.014 m   </td><td>+/-0.137 m </td></tr>
<tr><td>P63_15_Y   </td><td>2089.745 m   </td><td>+/-0.138 m </td></tr>
<tr><td>P63_15_Z   </td><td>2257.388 m   </td><td>+/-0.057 m </td></tr>
<tr><td>P63_15_O   </td><td>2.404430 deg </td><td>+/-11 sec  </td></tr>
<tr><td>P63_15_P   </td><td>-0.310290 deg</td><td>+/-13 sec  </td></tr>
<tr><td>P63_15_K   </td><td>-1.772814 deg</td><td>+/-4 sec   </td></tr>
</tbody>
</table>
====================== Residual ==============================
<table>
<thead>
<tr><th>Photo  </th><th style="text-align: right;">     Point</th><th style="text-align: right;">  vx_mm</th><th style="text-align: right;">  vy_mm</th><th style="text-align: right;">  vx_px</th><th style="text-align: right;">  vy_px</th></tr>
</thead>
<tbody>
<tr><td>P62_15 </td><td style="text-align: right;">20301     </td><td style="text-align: right;"> 0.0001</td><td style="text-align: right;">-0.0005</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0  </td></tr>
<tr><td>P62_15 </td><td style="text-align: right;">20401     </td><td style="text-align: right;"> 0.0003</td><td style="text-align: right;"> 0.0008</td><td style="text-align: right;">    0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>P62_15 </td><td style="text-align: right;">30301     </td><td style="text-align: right;"> 0.0002</td><td style="text-align: right;"> 0.0015</td><td style="text-align: right;">    0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>P62_15 </td><td style="text-align: right;">30401     </td><td style="text-align: right;"> 0.001 </td><td style="text-align: right;">-0.0015</td><td style="text-align: right;">    0.1</td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>P62_15 </td><td style="text-align: right;">40401     </td><td style="text-align: right;">-0.0033</td><td style="text-align: right;"> 0.0017</td><td style="text-align: right;">   -0.2</td><td style="text-align: right;">    0.1</td></tr>
<tr><td>P62_15 </td><td style="text-align: right;">40501     </td><td style="text-align: right;"> 0.0016</td><td style="text-align: right;">-0.002 </td><td style="text-align: right;">    0.1</td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">20301     </td><td style="text-align: right;">-0.0009</td><td style="text-align: right;">-0.0009</td><td style="text-align: right;">   -0.1</td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">20401     </td><td style="text-align: right;">-0.0017</td><td style="text-align: right;">-0.0003</td><td style="text-align: right;">   -0.1</td><td style="text-align: right;">   -0  </td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">30301     </td><td style="text-align: right;"> 0.0039</td><td style="text-align: right;">-0.0005</td><td style="text-align: right;">    0.3</td><td style="text-align: right;">   -0  </td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">30401     </td><td style="text-align: right;"> 0.0023</td><td style="text-align: right;"> 0.0001</td><td style="text-align: right;">    0.2</td><td style="text-align: right;">    0  </td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">40401     </td><td style="text-align: right;">-0.0022</td><td style="text-align: right;"> 0.0046</td><td style="text-align: right;">   -0.1</td><td style="text-align: right;">    0.3</td></tr>
<tr><td>P63_15 </td><td style="text-align: right;">40501     </td><td style="text-align: right;">-0.0012</td><td style="text-align: right;">-0.0031</td><td style="text-align: right;">   -0.1</td><td style="text-align: right;">   -0.2</td></tr>
</tbody>
</table>
====================== program stop =========================
