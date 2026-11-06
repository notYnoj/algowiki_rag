### A general _j_-th iteration.

Suppose we are given an interval _I_<sub>_j_-1</sub>. The goal is to compute an interval _I<sub>j</sub>_ such that either

1. \(|S\cap I_j|=O(n)\), in which case we proceed to the distance-reporting step; or<tbc>

2. \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\) for some constant \(\rho<1\).

We first compute \(\kappa(I_{j-1})\) using Lemma 11. If \(\kappa(I_{j-1})\le cn\) for a sufficiently large constant _c_, then \(|S\cap I_{j-1}|=O(n)\), and we proceed directly to the distance-reporting step.

Otherwise, we compute a full biclique partition by applying the algorithm for Recurrence (1) with _r=m_. Since every cell of the last cutting has an empty conflict list, the resulting collection \(\Gamma=\{A_\sigma\times B(\sigma):\sigma\in\Xi\}\) forms a full biclique partition of \(S\cap I_{j-1}\). The construction takes _O(mr+n_log_r_) time, which is _O(n_log_m_), and the total biclique size satisfies \(\sum_{A_t\times B_t\in\Gamma}(|A_t|+|B_t|)=O(nlogm)\).

We then construct the expander graphs for the bicliques of \(\Gamma\) and form the weighted distance set _E_ exactly as in Section 5.1. This also takes _O(n_log_m_) time. Next, we partition _E_ into _O_(1) basic intervals and use Lemma 11 to identify the unique interval containing \(\delta^*\). This interval is returned as _I<sub>j</sub>_. By the same analysis as in Section 5.1 (see also \[20, 28\]), there exists a constant \(\rho<1\) such that \(|S\cap I_j|\le\rho|S\cap I_{j-1}|\). Since Lemma 11 is invoked only _O_(1) times, the total running time of the iteration is _O(n_log_m_).

### Distance-reporting.

We are given an interval _I_ containing \(\delta^*\) with \(|S\cap I|=O(n)\). The goal is to finally compute \(\delta^*\).

Assume \(I=(\alpha,\beta]\). We first compute \(K_\alpha\) using Lemma 11. Then \(\delta^*\) is the \((K-K_\alpha)\)-th smallest distance in \(S\cap I\). To enumerate all distances in \(S\cap I\), we again compute a full biclique partition \(\Gamma\) as above. This takes _O(n_log_m_) time. We then explicitly output all distances recorded in \(\Gamma\), which requires \(O(|S\cap I|)=O(n)\) additional time since \(|S\cap I|=O(n)\). Finally, we apply the linear-time selection algorithm to obtain \(\delta^*\) in _O(n_) time. The total running time of the distance-reporting step is therefore _O(n_log_m_).

We conclude that if \(n\ge m^2\), then the distance selection problem can be solved in _O(n_log<sup>2</sup>_m_) time.

### Remark.

One may wonder whether the running time can be improved further to _O(n_log_m_), for example by incorporating approximate counting. The main obstacle is point location. In each iteration, we must locate all _n_ points of _B_ in a hierarchical cutting. In our symmetric case algorithm, we were able to perform these point locations in constant amortized time by using the \(\Gamma\)-framework on sufficiently small subproblems. Here, however, the \(\Gamma\)-framework is no longer applicable. Consequently, each point location costs _O_(log_m_) time, forcing the running time of every iteration to be _O(n_log_m_).

## 6.2 The case _n\<m_<sup>2</sup>

We now consider the case _n\<m_<sup>2</sup>. As before, we follow a prune-and-search framework and maintain an interval _I_ containing \(\delta^*\). Initially, \(I=(0,+\infty)\), and therefore \(|S\cap I|=O(mn)\).

The algorithm consists of three main procedures.

1. Reduce the number of candidate distances from _O(mn_) to _O(m_<sup>2</sup>).<tbc>

2. Reduce the number of candidate distances from _O(m_<sup>2</sup>) to _O(m_<sup>2/3</sup>_n_<sup>2/3</sup>).<tbc>

3. Enumerate the remaining candidate distances and compute \(\delta^*\).

The first and third procedures are relatively straightforward. The main technical challenge lies in the second procedure.

