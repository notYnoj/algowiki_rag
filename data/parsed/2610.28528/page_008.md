<tbc>differ from the rest of the dataset in solution quality rather than quantity. As discussed in Section IIID, the quantum hardware reached the true optimum on only three of the nine, each time with a single solution at that size, so this family accounts for six of the eight instances in the dataset where the hardware fell short (Section IIF). On three of them (treated separately) classical post-processing discovered strictly larger independent sets.

**Standard instances** (7 - 205 atoms) display the widest variation, from near-unity amplification on small instances to 1727\(\times\) on instance `L12\_seed2763`. The highest-amplification standard instances were `L12\_seed2763` (142 \(\rightarrow\) 245173 solutions), `L14\_seed2867` (55 \(\rightarrow\) 92941 solutions), and `L14\_seed3728` (52 \(\rightarrow\) 52868 solutions). These tend to be larger graphs with many atoms, where unit disk geometry naturally gives rise to large numbers of degenerate optimal configurations. One instance in this family, `L16\_seed4816`, is an exception to the pattern that standard test bed seeds are already optimal: its seven quantum seeds sit at size 63, whereas the certified optimum is 64 with degeneracy 4480, so the 3359 solutions Houdayer discovered from them are all one atom short. Cluster exchange found no size-64 configura<tbc>

<tbc>tion, consistent with the three suboptimal hard instances that likewise failed to improve.

Across all types, amplification correlates only moderately with problem size (Spearman \(\rho=0.55\), \(p=1\times 10^{-4}\), between atom count and amplification factor across all 43 instances), and more weakly with the number of quantum seeds (\(\rho=0.37\), _p_=0.02). Neither is a strong predictor. The exact degeneracy is a far better one (\(\rho=0.86\) between _D_MIS and _A_ over the 35 instances whose seeds reach the optimum).

## C. Initial Diversity and Manifold Exploration

Figure 4 examines the relationship between the diversity of the quantum seed pool and the resulting amplification. We measure diversity as the mean pairwise Hamming distance \(\bar{\Delta}\) between initial quantum solutions. For binary solution vectors the Hamming distance equals the size of the symmetric difference \(|s_i\oplus s_j|\) introduced in Section IIC, so we use the two terms interchangeably and denote the per-pair value \(|\Delta_{ij}|\) and its mean \(\bar{\Delta}\). Error bars come from a delete-one-seed jackknife, because<tbc>

106
105
Final Houdayer solutions Notal
104
103
102
Benchmark Hard Standard No amplification
101
102
103
104
105
106
Initial quantum solutions N quantum

104
Spearman p = 0.85 n = 35
103
Amplification factor A
102
101
Benchmark Hard Standard
100
0
10
20
30
40
50
Mean pairwise Hamming distance A of quantum seeds

FIG. 3. Scatter plot showing the initial quantum solution count _N_quantum versus the final Houdayer solution pool size on a base-10 log-log scale. Points above the diagonal indicate amplification; the three points on the diagonal are instances that showed none. The 40 instances shown exclude the three improvement instances, which are treated separately (Section IIID). Benchmark instances are represented by circles, hard instances by squares, and standard instances by triangles. The highest amplification (`HP1478`) generates 1967339 solution configurations from an initial pool of 165, i.e., a 11923\(\times\) amplification. Most instances show substantial amplification regardless of initial quantum sample size, demonstrating that solution count amplification is not simply proportional to quantum seed quantity.

FIG. 4. Initial solution diversity versus amplification factor. The mean pairwise Hamming distance \(\bar{\Delta}\) (with error bars from a delete-one-seed jackknife, none for pools of two seeds) between the _initial_ quantum solutions versus amplification success. The seed pools are reconstructed from the raw hardware samples through the same repair procedure used by the algorithm (Section IID), so \(\bar{\Delta}\) characterises the pool the hardware actually supplied rather than the amplified manifold. Of the 43 instances, 35 are shown: the three improvement instances are treated separately (Section IIID) and five further instances yield only a single distinct solution at the optimum, so they admit no pair. Benchmark instances are represented by circles, hard instances by squares, and standard instances by triangles. Because \(\bar{\Delta}\) grows with manifold size, much of this association reflects _D_MIS (Section IIIC).

