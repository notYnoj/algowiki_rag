### 3 Results and Discussion

PMS8 is implemented in C++ and uses OpenMPI for communication between processors. PMS8 was evaluated on the Hornet cluster in the Booth Engineering Center for Advanced Technology (BECAT) at University of Connecticut. The Hornet cluster consists of 64 nodes, each equipped with 12 Intel Xeon X5650 Westmere cores and 48 GB of RAM. The nodes use Infiniband networking for MPI. In our experiments we employed at most 48 cores on at most 4 nodes.

We generated random (_l,d_) instances according to [11] and as described in the introduction. For every (_l,d_) combination we report the average runtime over 5 random instances. For several challenging instances, in figure 3 we present the speedup obtained by the parallel version over the single core version. For _p_=48 cores the speedup is close to _S_=45 and thus the efficiency is _E=S/p_=94%.

The runtime of PMS8 on instances with _l_ up to 50 and _d_ up to 21 is shown in figure 5. Instances which are expected to have more than 500 motifs simply by random chance (spurious motifs) are excluded. The expected number of spurious motifs was computed as described in appendix C. Instances where _d_ is small relative to _l_ are solved efficiently using a single CPU core. For more challenging instances we report the time taken using 48 cores.

A comparison between PMS8 and qPMS7 [7] on challenging instances is shown in figure 6. Both programs have been executed on the Hornet cluster. qPMS7 is a sequential algorithm. PMS8 was evaluated using up to 48 cores. The speedup of PMS8 single core over qPMS7 is shown in figure 7. The speedup is high for small instances because qPMS7 has to load an ILP table. For larger instances the speedup of PMS8 sharply increases. This is expected because qPMS7 always generates neighborhoods for tuples of 3 _l_-mers, which become very large as _l_ and _d_ grow. On the other hand, PMS8 increases the number of _l_-mers in the tuple with the instance size. With each _l_-mer added to the tuple, the size of the neighborhood reduces exponentially, whereas the number of neighborhoods generated increases by a linear factor. The ILP table precomputation requires solving many ILP formulations. The table then makes qPMS7 less memory efficient than PMS8. The peak memory used by qPMS7 for the challenging instances in figure 6 was 607 MB whereas for PMS8 it was 122 MB. PMS8 is the first algorithm to solve the challenging instances (25,10) and (26,11).

n1
n0
n1
n2
n3
n4
T1
T1
T2
T2
T3
T3
d1
n1+n4-d1
n2+n4-d2
n3+n4-d3
M
M

**Fig.4.** Proof of theorem 1. Case 1 - left figure: There exists \(i,1\le i\le 3\) for which \(n_i\ge d_i\). Without loss of generality we assume _i_=1. Case 2 - right figure: _n<sub>i</sub>\<d<sub>i</sub>_ for all _i_, \(1\le i\le 3\). The top 3 rows represent the input _l_-mers. The last row shows a common neighbor _M_. In any column, identical colors represents matches, different colors represent mismatches.

