_Moreover, we have_ \(m_i\le 2c^*(F,k-\frac{1}{2}k_i)\le 2c^*(F,k-1)\).

_Proof._ There are log_m<sub>i</sub>_ inner loop iterations, with _m_ growing exponentially. Thus, lemma 41 immediately implies the bound on comparisons and running time.

We now prove the second statement. If there is only a single run, then _m<sub>i</sub>_=2 and the statement is vacuous. Otherwise, observe that the second-to-last run of WSHForestElim returned `FAIL` for \(m=\frac{1}{2}m_i\). Lemma 41 implies that \(\frac{1}{2}m_i\le c^*(F_i,\frac{1}{2}k_i)\). Let \(R=\tilde{D}'_i\) be the prefix of nodes removed in previous iterations. Recall that _F<sub>i</sub>=F-R_ and _k<sub>i</sub>=k_-|_R_|, so |_R_|=_k-k<sub>i</sub>_. This implies

\(c^*(F_i,\frac{1}{2}k_i)\le c^*(F,|R|+\frac{1}{2}k_i)=c^*(F,k-\frac{1}{2}k_i),\)

as desired.

We are now ready to prove the following, which implies theorem 2:

**Theorem 43.** _There is an algorithm for poset selection using_ O(OPT+OPTlog(_k/_OPT)) _comparisons and_ O(OPT+_k_logOPT) _time, when_ \(\mathrm{OPT}\le\frac{1}{2}k\) _and the input graph is a forest._

_Proof._ Obviously, that algorithm is WSHSparseForestSelect. Let \(m'\) be the value of _m_<sup>∗</sup> just before the second-to-last outer loop iteration, i.e., \(m'=\mathrm{max}_{i\in[t-2]}m_i\). Then \(m'\le\frac{1}{2}\delta k_{t-2}\le k_{t-2}\).

Since iteration decreases _k_ by a factor of \(\beta=(1-\frac{1}{4}\delta)\) and possibly further, we have \(m'\le k_{t-2}\le k\cdot\beta^{t-2}\), and thus \(t-2\le\mathrm{log}_{1/\beta}(k/m')\). Thus, there are \(\mathcal{O}(\mathrm{log}(k/m'))\) iterations in total.

Each iteration but the last two takes \(\mathcal{O}(m')\) comparisons and \(\mathcal{O}(k_i\mathrm{log}m')\) time by lemma 42. From the fact _k<sub>i</sub>_ is exponentially decreasing it follows that these iterations take \(\mathcal{O}(m'\mathrm{log}(k/m'))\) comparisons and \(\mathcal{O}(k\mathrm{log}m')\) time in total. Write _p_=OPT(_F,k_). By lemma 42, we have \(m'\le 2c^*(F,k-1)\le 2p\). Since \(m'\mathrm{log}(k/m')\) is nondecreasing in \(m'\) up to a constant factor, our bounds so far are O(_p_log(_k/p_)) comparisons and O(_k_log_p_) time.

It remains to analyze the last two iterations. In the second-to-last one, we again call WSHSparseForestSelect using O(_p_) comparisons and O(_k_log_p_) time by lemma 42.

In the final one, we call WSHTreeSelect, with running time \(\mathcal{O}(k+c(F_t,k_t-1))\le\mathcal{O}(k+p)\) by lemma 27. Since this is the last iteration, we have \(k<m^*\le\mathcal{O}(p)\). Thus the running time (and thus number of operations) is O(_p_). The theorem follows.

## 7.4 Improved running time for _k_-unbounded trees

Let _F_ be a forest. Recall that _F_ is _k-unbounded_ if every node of depth _k_-1 or less has at least one child. In this section, we shown an improved bound for WSHSparseForestSelect when the input is _k_-bounded, using theorem 10.

On _k_-bounded forests, WSHSparseForestSelect can be shown to take O(OPTloglog_k_) comparisons. To obtain our target bound of O(OPTloglog(OPT_/k_)), a small change is necessary. Maintain a new variable _b_, initially set to 2. After each iteration, compute \(b\leftarrow\mathrm{max}\{b,m\mathrm{log}(k/m)\}\). Replace _m_<sup>∗</sup> with _b_ in the condition \(m^*>\frac{1}{2}\delta k\) (algorithm 3, line 5).<tbc>

