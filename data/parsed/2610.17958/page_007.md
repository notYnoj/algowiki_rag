\((\ell,d)\text{-CMM in}\mathcal{O}\left(\genfrac(){pt}{2}{\ell}{d}^2N^2\right)\text{time using}\mathcal{O}(N)\text{space. \sqcap\sqcup\)

This algorithm can be extended to the \(f_{\chi^2}\) support measure by adapting the \(f_{\chi^2}\) version of Algorithm 3.1 (see Corollary A.1). We defer the W\[1\]-hardness for \((\ell,d)\)-CMM, parameterized by _d_, to Appendix B.

**4.1 Parallelization.** The algorithm of Theorem 4.3 is easy to parallelize since the computation can be carried out independently for each _wildcard combination_. As motif pairs are unordered, roughly half of the \(\genfrac(){pt}{2}{\ell}{d}^2\) combinations need to be considered, giving \(\genfrac(){pt}{2}{\ell}{d}\left(\genfrac(){pt}{2}{\ell}{d}+1\right)/2\) independent jobs, each running in O(_N_<sup>2</sup>) time. For \(H\neq H'\), the motifs _X_ and _Y_ are always distinct, so the tie-breaking test \(X\unknown Y\) of Algorithm 3.1 is applied only in the jobs with \(H=H'\). Since each thread processes a disjoint subset of the motif pairs, the global optimum is the maximum of the per-job optima, so aggregation is trivial. We will later see that this is both easy to implement and efficient in practice. Moreover, by using Theorem 4.3, O(_N_) space is used per thread.

**5 Experimental results.** In this section, we compare our exact algorithm against SEQ-SLIDER and M-SLIDER, two variants of SLIDER \[1\], the state-of- the-art (heuristic) method. Each employs a different neighborhood function when sliding over neighboring motifs during steepest ascent. We also empirically evaluate the time and space complexities of our exact algorithm to confirm our theoretical findings. These goals were split into the following research questions:

**RQ1:** How do the scores of SLIDER’s solution set compare to the ones of the optimal solution set?<tbc>

**RQ2:** What is the recall of SLIDER’s solution set relative to the optimal solution set?<tbc>

**RQ3:** How does our algorithm scale as |_V_| (and thus _N_) grows?<tbc>

**RQ4:** How does our algorithm scale as |_E_| grows?<tbc>

**RQ5:** How does our algorithm scale as the number _t_ of threads used increases?

_Remark_ 5.1. We excluded D-MOTIF \[25\] and FindMotif \[15\], as their complexities are prohibitive for our datasets and parameters, and for the same scalability reasons, we excluded their heuristic counterparts, D-STAR and MotifHeuristics. FindMotif and MotifHeuristics also lack publicly available implementations and rely on a different, probabilistic support measure. MotifHeuristics was re-implemented and evaluated in \[1\], where it was shown to be outperformed by SLIDER.

**5.1 Datasets.** We selected 5 networks of different species and with varying sizes among the 10 most queried networks from the STRING database \[24, 26\]<tbc>

<tbc>(version 12). In order to replicate the setup of \[1\] for RQ1 and RQ2 (which concern the _accuracy_ of SLIDER), we also included the two networks used in \[1\]. The characteristics of the networks are summarized in  5.1. These networks were preprocessed as described in Subsection C.1. All networks in  5.1 were used to address RQ1 and RQ2. For RQ3, RQ4, and RQ5, we also generated smaller artificial networks as described in Subsection C.1 to thoroughly investigate different input parameters.

**5.2 Implementations.** We implemented our exact algorithm (Theorem 4.3) in `C++`, which we make available at https://github.com/lucper/cmm. We used `libsais64` (version 2.4.10) to construct the SA and the LCP array \[6\] and implemented the parallel version of Theorem 4.3 (as described in Subsection 4.1) using OpenMP \[5\]. For SLIDER, we used the `Java` implementation provided by the authors \[1\], which is also available in our repository. Since we do not compare the efficiency of the two implementations, using the latter suffices for our purposes.

**5.3 Setup.** All experiments were conducted on two 32-core Intel Xeon Gold 6530 CPUs (2 threads per core, totaling _P_=128 threads across the two CPUs), operating at a base clock frequency of 2.1GHz (up to 4.0GHz), and 512GB RAM. We compiled our implementations with `g++` version `15.2.1` at the `-03` optimization level. Wall-clock times were measured with `std::chrono::steady\_clock`. Peak RAM usage was measured as the maximum resident set size using the `getrusage` function.

**5.4 Metrics for RQ1 and RQ2.**

_Similarity index._ In order to compare solution sets, we introduce a notion of similarity between \((\ell,d)\)-motif pairs. We count the edges in which two \((\ell,d)\)-motif pairs, {_X,Y_} and {_Z,W_}, co-occur such that the \((\ell,d)\)-motifs in each endpoint of the edge match substrings that are at<tbc>

\begin{tabular}{cccc}
Dataset & |_V_| & |_E_| & _N_ \\
E. coli & 4006 & 32,244 & 1,277,734 \\
S. cerevisiae I & 5791 & 104,188 & 2,744,228 \\
D. melanogaster & 10,522 & 118,698 & 6,043,033 \\
A. thaliana & 20,239 & 331,525 & 8,903,236 \\
H. sapiens I & 16,201 & 236,930 & 9,605,435 \\
S. cerevisiae II & 1620 & 9060 & 862,281 \\
H. sapiens II & 10,380 & 69,515 & 5,607,838 \\
\end{tabular}

5.1: Top: Parameters of datasets from the STRING database after preprocessing. Bottom: Parameters of datasets from \[1\] after preprocessing.

