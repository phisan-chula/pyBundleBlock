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
Example Result</br>
Reading YAML "Block_62_63_6TP_TLE2020px.yml" ...</br>

============================Input Measurement============================
|    | Photo   | Pnt_Name   |   jx_px |    iy_px |     xp_mm |    yp_mm |
|---:|:--------|:-----------|--------:|---------:|----------:|---------:|
|  0 | P62_15  | 40401      |  9840.1 |  -2376.6 |   34.2148 |  77.8308 |
|  1 | P62_15  | 40501      | 13847.1 |  -2155.5 |   94.3682 |  81.1493 |
|  2 | P62_15  | 30301      |  6563.1 |  -8907.7 |  -14.9802 | -20.2166 |
|  3 | P62_15  | 30401      | 10098.1 |  -7945.7 |   38.0876 |  -5.7753 |
|  4 | P62_15  | 20301      |  7534   | -13325.9 |   -0.4052 | -86.545  |
|  5 | P62_15  | 20401      | 10160.2 | -13288.9 |   39.0196 | -85.99   |
|  6 | P62_15  | t1         |  8494.2 | -11029.6 |   14.0096 | -52.072  |
|  7 | P62_15  | t2         | 10081.9 |  -9718.9 |   37.8443 | -32.3954 |
|  8 | P62_15  | t3         | 11374.6 | -10245.2 |   57.2504 | -40.2967 |
|  9 | P62_15  | t4         | 10324.4 |  -7793.9 |   41.4849 |  -3.4964 |
| 10 | P62_15  | t5         |  9578.8 |  -7418.1 |   30.2919 |   2.1454 |
| 11 | P62_15  | t6         |  9351.6 |  -5323.3 |   26.8812 |  33.5936 |
| 12 | P63_15  | 40401      |  3819.3 |  -2552   |  -56.1696 |  75.1969 |
| 13 | P63_15  | 40501      |  7940.2 |  -2354.9 |    5.6915 |  78.1541 |
| 14 | P63_15  | 30301      |   458.4 |  -9075   | -106.62   | -22.7222 |
| 15 | P63_15  | 30401      |  4110.3 |  -8135   |  -51.7999 |  -8.6127 |
| 16 | P63_15  | 20301      |  1358.3 | -13529.1 |  -93.1104 | -89.5854 |
| 17 | P63_15  | 20401      |  3902.2 | -13518   |  -54.9224 | -89.4197 |
| 18 | P63_15  | t1         |  2403.2 | -11223.7 |  -77.4254 | -54.9782 |
| 19 | P63_15  | t2         |  3927.4 |  -9920.9 |  -54.545  | -35.4217 |
| 20 | P63_15  | t3         |  5176.8 | -10462.1 |  -35.7894 | -43.5464 |
| 21 | P63_15  | t4         |  4328.7 |  -7984.9 |  -48.5214 |  -6.3595 |
| 22 | P63_15  | t5         |  3600.8 |  -7601.3 |  -59.4484 |  -0.6008 |
| 23 | P63_15  | t6         |  3130.3 |  -5503.1 |  -66.5119 |  30.8966 |


====== Adjusted Parameters and Precision ======
| Parameter   | Value         | Precision   |
|-------------|---------------|-------------|
| P62_15_X    | 3708.724 m    | +/-0.171 m  |
| P62_15_Y    | 2100.812 m    | +/-0.133 m  |
| P62_15_Z    | 2258.521 m    | +/-0.058 m  |
| P62_15_O    | 2.194102 deg  | +/-12 sec   |
| P62_15_P    | -0.432875 deg | +/-17 sec   |
| P62_15_K    | -2.216435 deg | +/-3 sec    |
| P63_15_X    | 4908.014 m    | +/-0.137 m  |
| P63_15_Y    | 2089.745 m    | +/-0.138 m  |
| P63_15_Z    | 2257.388 m    | +/-0.057 m  |
| P63_15_O    | 2.404430 deg  | +/-11 sec   |
| P63_15_P    | -0.310290 deg | +/-13 sec   |
| P63_15_K    | -1.772814 deg | +/-4 sec    |


====================== Residual ==============================
| Photo   |      Point |   vx_mm |   vy_mm |   vx_px |   vy_px |
|---------|------------|---------|---------|---------|---------|
| P62_15  | 20301      |  0.0001 | -0.0005 |     0   |    -0   |
| P62_15  | 20401      |  0.0003 |  0.0008 |     0   |     0.1 |
| P62_15  | 30301      |  0.0002 |  0.0015 |     0   |     0.1 |
| P62_15  | 30401      |  0.001  | -0.0015 |     0.1 |    -0.1 |
| P62_15  | 40401      | -0.0033 |  0.0017 |    -0.2 |     0.1 |
| P62_15  | 40501      |  0.0016 | -0.002  |     0.1 |    -0.1 |
| P63_15  | 20301      | -0.0009 | -0.0009 |    -0.1 |    -0.1 |
| P63_15  | 20401      | -0.0017 | -0.0003 |    -0.1 |    -0   |
| P63_15  | 30301      |  0.0039 | -0.0005 |     0.3 |    -0   |
| P63_15  | 30401      |  0.0023 |  0.0001 |     0.2 |     0   |
| P63_15  | 40401      | -0.0022 |  0.0046 |    -0.1 |     0.3 |
| P63_15  | 40501      | -0.0012 | -0.0031 |    -0.1 |    -0.2 |


====================== program stop =========================
