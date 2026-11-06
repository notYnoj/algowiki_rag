<tbc>TDM time slot is compressed to \(T_\mathrm{sym}=28\mu\)s. Other parameters are set as _L_<sub>cpp</sub>=12, _c_<sub>1</sub>=9/512, and _c_<sub>2</sub>=1/10000. In the simulation, three high-mobility targets are evaluated, comprising one near-field target and two far-field targets, at extremely high velocities of 60, -50, and 80 m/s, respectively. For the parameters AoD and AoA, the estimation performance is verified by root mean square error (RMSE). While for delay and doppler, it is more appropriate to use normalized mean square error (NMSE) for evaluation. For the parameter vector **h** to be estimated, its NMSE and RMSE are respectively defined as \(\mathbb{E}\left[\frac{\|\mathbf{h}-\hat{\mathbf{h}}\|_2^2}{\|\mathbf{h}\|_2^2}\right]\) and \(\sqrt{\mathbb{E}\left[\|\mathbf{h}-\hat{\mathbf{h}}\|_2^2\right]}\), where \(\hat{\mathbf{h}}\) denotes the corresponding estimated value.

As shown in Fig. 2, the RMSE of our proposed SD- RMO AoA estimation scheme monotonically decreases with the escalation of signal-to-noise ratio (SNR). This asymptotic efficiency stems directly from our polar algebraic manifold formulation. The physical root of this failure lies in the rigid reliance of Multiple Signal Classification (MUSIC) on the planar wavefront assumption, resulting in smeared or entirely missing spatial spectral peaks. Furthermore, while the subspace based method \[12\] partially addresses mixed-field sensing, its performance is fundamentally bottlenecked by the density of the partitioned spatial dictionary.

Figs. 3 and 4 plot the NMSE of delay and Doppler estimation as functions of SNR. To rigorously evaluate our proposed scheme, we benchmark it against three representative baselines: the compressed sensing (CS) method \[15\], the alternating maximum likelihood (AML) algorithm \[16\], and the refined pulse compression (Refined PC) approach \[12\]. In the considered high-mobility scenario,<tbc>

<tbc>the grid-dependent CS method suffers from inevitable basis mismatch and energy leakage, while the Refined PC and AML approaches encounter severe resolution bottlenecks, both leading to prominent error floors at high SNR regimes. In stark contrast, the proposed BR- AEG scheme directly isolates the highly coupled time- frequency parameters by exploiting the intrinsic low-rank tensor structure. Consequently, it achieves a significantly lower NMSE and reduces the high-dimensional optimization to low-dimensional matrix operations, ensuring high performance with bounded complexity.

Fig. 5 depicts the estimation performance of AoD versus SNR. In the scenario considered in this paper, the orthogonal matching pursuit (OMP) \[17\] method experiences severe performance degradation. The fundamental bottleneck lies in its reliance on predefined discrete spatial- temporal dictionaries. Compared with the MUSIC \[18\] method, the algorithm proposed in this paper achieves better performance. This is because the MUSIC process inherently annihilates the intrinsic multidimensional structural gains of the scattered electromagnetic waves.

## V. Conclusion

In this paper, a tensor-based sensing framework tailored for XL-MIMO AFDM systems is developed. The received signals are reformulated as a third-order tensor, and an efficient decomposition approach exploiting the inherent Vandermonde structure is developed to decouple the high- dimensional parameters. To address the near-field effects, we introduce SD-RMO algorithm for AoA estimation, which effectively circumvents the high-dimensional search complexity. For delay-Doppler estimation, BR-AEG algorithm is designed to operate in the continuous domain, fundamentally eliminating grid-mismatch errors in high- mobility scenarios. The remaining target parameter AoD is subsequently extracted in a sequential manner. Simulations confirm that the proposed framework achieves orders-of-magnitude lower delay-Doppler NMSE and eliminates the angular error floors common in existing grid- dependent methods.

## References

101
100
MUSIC
Subspace Based
Proposed SD-RMO
RMSE (AOA)
10-1
10-2
10-3
-10
-5
0
5
10
15
20
SNR (dB)

100
10-2
MUSIC
Compressed Sensing
10-4
AML
Refined PC
Proposed BPR-AEG
10-6
10-8
-10
-5
0
5
10
15
20
SNR (dB)

102
100
MUSIC
Compressed Sensing
10-2
AML
Refined PC
Proposed BPR-AEG
RMSE (Doppler)
10-4
10-6
-10
-5
0
5
10
15
20
SNR (dB)

100
MUSIC
OMP
Proposed Method
RMSE (AOD)
10-1
-10
-5
0
5
10
15
20
SNR (dB)

Fig. 2. RMSE performance of AoA estimation versus SNR

Fig. 3. NMSE performance of delay estimation versus SNR

Fig. 4. NMSE performance of doppler estimation versus SNR

Fig. 5. RMSE performance of AoD estimation versus SNR

