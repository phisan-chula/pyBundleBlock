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
<table>
<thead>
<tr><th>Parameter  </th><th>Value        </th><th>Precision  </th></tr>
</thead>
<tbody>
<tr><td>p62_15_X   </td><td>3708.694 m   </td><td>+/-0.178 m </td></tr>
<tr><td>p62_15_Y   </td><td>2100.753 m   </td><td>+/-0.131 m </td></tr>
<tr><td>p62_15_Z   </td><td>2258.511 m   </td><td>+/-0.059 m </td></tr>
<tr><td>p62_15_O   </td><td>2.195264 deg </td><td>+/-12 sec  </td></tr>
<tr><td>p62_15_P   </td><td>-0.433633 deg</td><td>+/-18 sec  </td></tr>
<tr><td>p62_15_K   </td><td>-2.216406 deg</td><td>+/-4 sec   </td></tr>
<tr><td>p63_15_X   </td><td>4908.025 m   </td><td>+/-0.142 m </td></tr>
<tr><td>p63_15_Y   </td><td>2089.883 m   </td><td>+/-0.127 m </td></tr>
<tr><td>p63_15_Z   </td><td>2257.377 m   </td><td>+/-0.059 m </td></tr>
<tr><td>p63_15_O   </td><td>2.401673 deg </td><td>+/-10 sec  </td></tr>
<tr><td>p63_15_P   </td><td>-0.309957 deg</td><td>+/-14 sec  </td></tr>
<tr><td>p63_15_K   </td><td>-1.771746 deg</td><td>+/-4 sec   </td></tr>
<tr><td>t1_X       </td><td>3881.968 m.  </td><td>+/-0.037 m.</td></tr>
<tr><td>t1_Y       </td><td>1486.194 m.  </td><td>+/-0.043 m.</td></tr>
<tr><td>t1_Z       </td><td>205.401 m.   </td><td>+/-0.102 m.</td></tr>
<tr><td>t2_X       </td><td>4199.238 m.  </td><td>+/-0.030 m.</td></tr>
<tr><td>t2_Y       </td><td>1737.682 m.  </td><td>+/-0.036 m.</td></tr>
<tr><td>t2_Z       </td><td>244.337 m.   </td><td>+/-0.099 m.</td></tr>
<tr><td>t3_X       </td><td>4442.124 m.  </td><td>+/-0.032 m.</td></tr>
<tr><td>t3_Y       </td><td>1628.696 m.  </td><td>+/-0.039 m.</td></tr>
<tr><td>t3_Z       </td><td>256.329 m.   </td><td>+/-0.102 m.</td></tr>
<tr><td>t4_X       </td><td>4273.925 m.  </td><td>+/-0.030 m.</td></tr>
<tr><td>t4_Y       </td><td>2111.272 m.  </td><td>+/-0.032 m.</td></tr>
<tr><td>t4_Z       </td><td>212.605 m.   </td><td>+/-0.101 m.</td></tr>
<tr><td>t5_X       </td><td>4129.183 m.  </td><td>+/-0.031 m.</td></tr>
<tr><td>t5_Y       </td><td>2192.276 m.  </td><td>+/-0.032 m.</td></tr>
<tr><td>t5_Z       </td><td>208.937 m.   </td><td>+/-0.101 m.</td></tr>
<tr><td>t6_X       </td><td>4083.629 m.  </td><td>+/-0.033 m.</td></tr>
<tr><td>t6_Y       </td><td>2591.675 m.  </td><td>+/-0.040 m.</td></tr>
<tr><td>t6_Z       </td><td>309.609 m.   </td><td>+/-0.098 m.</td></tr>
</tbody>
</table>

====================== Reidual ===============================</br>
<table>
<thead>
<tr><th>Photo  </th><th>Point  </th><th style="text-align: right;">  vx_mm</th><th style="text-align: right;">  vy_mm</th><th style="text-align: right;">  vx_px</th><th style="text-align: right;">  vy_px</th></tr>
</thead>
<tbody>
<tr><td>p62_15 </td><td>20301  </td><td style="text-align: right;"> 0.0002</td><td style="text-align: right;">-0.0004</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0  </td></tr>
<tr><td>p62_15 </td><td>20401  </td><td style="text-align: right;"> 0.0007</td><td style="text-align: right;"> 0.0012</td><td style="text-align: right;">    0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p62_15 </td><td>30301  </td><td style="text-align: right;"> 0.0002</td><td style="text-align: right;"> 0.0031</td><td style="text-align: right;">    0  </td><td style="text-align: right;">    0.2</td></tr>
<tr><td>p62_15 </td><td>30401  </td><td style="text-align: right;"> 0.0019</td><td style="text-align: right;">-0.0006</td><td style="text-align: right;">    0.1</td><td style="text-align: right;">   -0  </td></tr>
<tr><td>p62_15 </td><td>40401  </td><td style="text-align: right;">-0.0035</td><td style="text-align: right;"> 0.0021</td><td style="text-align: right;">   -0.2</td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p62_15 </td><td>40501  </td><td style="text-align: right;"> 0.0006</td><td style="text-align: right;">-0.0017</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p62_15 </td><td>t1     </td><td style="text-align: right;">-0     </td><td style="text-align: right;"> 0.0014</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p62_15 </td><td>t2     </td><td style="text-align: right;"> 0     </td><td style="text-align: right;">-0.0014</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p62_15 </td><td>t3     </td><td style="text-align: right;"> 0     </td><td style="text-align: right;">-0.0011</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p62_15 </td><td>t4     </td><td style="text-align: right;"> 0.0001</td><td style="text-align: right;">-0.0024</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.2</td></tr>
<tr><td>p62_15 </td><td>t5     </td><td style="text-align: right;"> 0     </td><td style="text-align: right;">-0.0015</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p62_15 </td><td>t6     </td><td style="text-align: right;">-0     </td><td style="text-align: right;"> 0.0012</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p63_15 </td><td>20301  </td><td style="text-align: right;">-0.0008</td><td style="text-align: right;">-0.0006</td><td style="text-align: right;">   -0.1</td><td style="text-align: right;">   -0  </td></tr>
<tr><td>p63_15 </td><td>20401  </td><td style="text-align: right;">-0.0026</td><td style="text-align: right;">-0.0004</td><td style="text-align: right;">   -0.2</td><td style="text-align: right;">   -0  </td></tr>
<tr><td>p63_15 </td><td>30301  </td><td style="text-align: right;"> 0.0044</td><td style="text-align: right;">-0.0017</td><td style="text-align: right;">    0.3</td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p63_15 </td><td>30401  </td><td style="text-align: right;"> 0.0021</td><td style="text-align: right;">-0.0025</td><td style="text-align: right;">    0.1</td><td style="text-align: right;">   -0.2</td></tr>
<tr><td>p63_15 </td><td>40401  </td><td style="text-align: right;">-0.003 </td><td style="text-align: right;"> 0.0048</td><td style="text-align: right;">   -0.2</td><td style="text-align: right;">    0.3</td></tr>
<tr><td>p63_15 </td><td>40501  </td><td style="text-align: right;"> 0.0001</td><td style="text-align: right;">-0.0034</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.2</td></tr>
<tr><td>p63_15 </td><td>t1     </td><td style="text-align: right;"> 0     </td><td style="text-align: right;">-0.0014</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
<tr><td>p63_15 </td><td>t2     </td><td style="text-align: right;">-0     </td><td style="text-align: right;"> 0.0014</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p63_15 </td><td>t3     </td><td style="text-align: right;">-0     </td><td style="text-align: right;"> 0.0011</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p63_15 </td><td>t4     </td><td style="text-align: right;">-0.0001</td><td style="text-align: right;"> 0.0024</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.2</td></tr>
<tr><td>p63_15 </td><td>t5     </td><td style="text-align: right;">-0     </td><td style="text-align: right;"> 0.0015</td><td style="text-align: right;">   -0  </td><td style="text-align: right;">    0.1</td></tr>
<tr><td>p63_15 </td><td>t6     </td><td style="text-align: right;"> 0     </td><td style="text-align: right;">-0.0012</td><td style="text-align: right;">    0  </td><td style="text-align: right;">   -0.1</td></tr>
</tbody>
</table>

====================== program stop =========================</br>
