# pyBundleBlock

pyBundle.py : Perform bundle block adjustment computation using 'lmfit'</br>
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
Reading YAML "Block_62_63_6TP_TLE2020.yml" ...</br>
</br>
====== Adjusted Parameters and Precision ======</br>
p62_15_X       3708.694 m.     +/-0.178 m.</br>
p62_15_Y       2100.753 m.     +/-0.131 m.</br>
p62_15_Z       2258.511 m.     +/-0.059 m.</br>
p62_15_O       2.195264 deg.   +/-12 sec</br>
p62_15_P      -0.433633 deg.   +/-18 sec</br>
p62_15_K      -2.216406 deg.   +/-4 sec</br>
p63_15_X       4908.025 m.     +/-0.142 m.</br>
p63_15_Y       2089.883 m.     +/-0.127 m.</br>
p63_15_Z       2257.377 m.     +/-0.059 m.</br>
p63_15_O       2.401673 deg.   +/-10 sec</br>
p63_15_P      -0.309957 deg.   +/-14 sec</br>
p63_15_K      -1.771746 deg.   +/-4 sec</br>
t1_X           3881.968 m.     +/-0.037 m.</br>
t1_Y           1486.194 m.     +/-0.043 m.</br>
t1_Z            205.401 m.     +/-0.102 m.</br>
t2_X           4199.238 m.     +/-0.030 m.</br>
t2_Y           1737.682 m.     +/-0.036 m.</br>
t2_Z            244.337 m.     +/-0.099 m.</br>
t3_X           4442.124 m.     +/-0.032 m.</br>
t3_Y           1628.696 m.     +/-0.039 m.</br>
t3_Z            256.329 m.     +/-0.102 m.</br>
t4_X           4273.925 m.     +/-0.030 m.</br>
t4_Y           2111.272 m.     +/-0.032 m.</br>
t4_Z            212.605 m.     +/-0.101 m.</br>
t5_X           4129.183 m.     +/-0.031 m.</br>
t5_Y           2192.276 m.     +/-0.032 m.</br>
t5_Z            208.937 m.     +/-0.101 m.</br>
t6_X           4083.629 m.     +/-0.033 m.</br>
t6_Y           2591.675 m.     +/-0.040 m.</br>
t6_Z            309.609 m.     +/-0.098 m.</br>
====================== Reidual ===============================
--Photo--------Point-----vx_mm----vy_mm-----vx_px----vy_px---
p62_15       20301       0.0002  -0.0004      0.0     -0.0
p62_15       20401       0.0007   0.0012      0.0      0.1
p62_15       30301       0.0002   0.0031      0.0      0.2
p62_15       30401       0.0019  -0.0006      0.1     -0.0
p62_15       40401      -0.0035   0.0021     -0.2      0.1
p62_15       40501       0.0006  -0.0017      0.0     -0.1
p62_15       t1         -0.0000   0.0014     -0.0      0.1
p62_15       t2          0.0000  -0.0014      0.0     -0.1
p62_15       t3          0.0000  -0.0011      0.0     -0.1
p62_15       t4          0.0001  -0.0024      0.0     -0.2
p62_15       t5          0.0000  -0.0015      0.0     -0.1
p62_15       t6         -0.0000   0.0012     -0.0      0.1
p63_15       20301      -0.0008  -0.0006     -0.1     -0.0
p63_15       20401      -0.0026  -0.0004     -0.2     -0.0
p63_15       30301       0.0044  -0.0017      0.3     -0.1
p63_15       30401       0.0021  -0.0025      0.1     -0.2
p63_15       40401      -0.0030   0.0048     -0.2      0.3
p63_15       40501       0.0001  -0.0034      0.0     -0.2
p63_15       t1          0.0000  -0.0014      0.0     -0.1
p63_15       t2         -0.0000   0.0014     -0.0      0.1
p63_15       t3         -0.0000   0.0011     -0.0      0.1
p63_15       t4         -0.0001   0.0024     -0.0      0.2
p63_15       t5         -0.0000   0.0015     -0.0      0.1
p63_15       t6          0.0000  -0.0012      0.0     -0.1
====================== program stop =========================
