#### (2) The Output Phase.

Next, we color the remaining _n-m_ vertices. Here, we maintain bins \(J_1,\dots,J_r\subseteq V^*\backslash S\), initially empty, which correspond to _I_<sub>1</sub>_,...,I<sub>r</sub>_, respectively.

When a vertex \(v\in V^*\backslash S\) arrives, we put _v_ into _J<sub>i</sub>_ for the smallest _i_ such that \(N_{I_i}(v)=\emptyset\). Such an _i_ must exist because \(I_r=\emptyset\). Although _J<sub>i</sub>_ is not necessarily an independent set, it can be proven that the maximum degree of _G_<sup>∗</sup>\[_J<sub>i</sub>_\] is \(O((k\mathrm{log}n)/\lambda)\) with high probability in the range of \(i\le\frac{1}{\lambda}\) (Lemma 21). Hence, with the parameter setting

\(\lambda:=\frac{1}{6k\mathrm{ln}(3k)\mathrm{ln}n+2},\)

_G_<sup>∗</sup>\[_J_<sub>1</sub>\]_,...,G_<sup>∗</sup>\[_J<sub>r</sub>_\] all have maximum degrees _O(k_<sup>2</sup>log_k_log<sup>2</sup>_n_) with high probability (Lemma 22). Therefore, we can use the First-Fit algorithm to color each vertex of _G_<sup>∗</sup>\[_J<sub>i</sub>_\]. We use disjoint sets of colors for bins _J_<sub>1</sub>_,...,J<sub>r</sub>_.

#### Overall Algorithm.

The pseudocode for the entire algorithm is presented in Algorithm 1. With high probability, we use _O(k_<sup>2</sup>log_k_log<sup>2</sup>_n_) colors for each _J<sub>i</sub>_, and _r=O(k_log_k_log_n_). Therefore, we use _O(k_<sup>3</sup>log<sup>2</sup>_k_log<sup>3</sup>_n_) colors in expectation for the last _n-m_ vertices (Lemma 23). We analyze the algorithm’s performance in detail in the next section.

**Remark 14.** _The runtime of Algorithm 1 is unbounded for the scenario where m=n is chosen every time. However, if m=n, the only thing that happens is a call to the identical procedure COLORING<sub>k</sub>(n). Therefore, the outcome of Algorithm 1 remains the same if we choose m from the distribution that excludes m=n, i.e., each m_=0_,...,n_-1 _is chosen with probability_ \(\frac{1}{2^n-1}\genfrac(){pt}{2}{n}{m}\)_; this change makes its runtime bounded. Note that r is also bounded; we will prove_ \(r\le n+1\) _in Lemma 15. Nevertheless, this algorithm runs in exponential time, because sampling an independent set from_ \(\mathsf{I}\mathsf{S}_\lambda(G[A_r])\) _takes exponential time._

## 5 Analysis

In this section, we analyze the performance of Algorithm 1.

### 5.1 Number of Levels

First, we analyze the number _r_ of sampled independent sets: we prove that this is surely at most _n_+1 and is _O(k_log_k_log_n_) with high probability.

Random Independent Set
I1
I1
I1
I1
I1
I1
Independent Set
I2
I2
I2
I2
A2
A3
= N4x (I2)
A1
A1

**Figure 6:** An example of the learning phase.

