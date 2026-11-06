Observe that since always \(b\ge m^*\), this can only make the algorithm stop earlier. Call the new algorithm WSHSparseForestSelect2.

**Theorem 44.** _There is an algorithm that solves the poset selection problem on k-unbounded forests with_ O(OPTloglog(_k/_OPT)) _comparisons, in time_ O(_k_logOPT)_, when_ \(\mathrm{OPT}\le\frac{1}{4}k\).

_Proof._ We use WSHSparseForestSelect2. For the final two outer loop iterations, the same analysis as in theorem 43 can be used: They take O(OPT) comparisons and O(_k_logOPT) time. From now on, we only consider the first _t_-2 iterations.

Let \(m'=\mathrm{max}_{i\in[t-2]}m_i\), as in theorem 43. The total number of comparisons is \(\mathcal{O}(\sum_{i=1}^{t-2}m_i)\). Define \(b_i=m_i\mathrm{log}\frac{k_i}{m_i}\) for \(i\in[t-2]\), and let \(B=\mathrm{max}_{i\in[t-2]}b_i\). Note that _B_ is precisely the value for _b_ after _t_-2 iterations.

We first argue that _B_ is an asymptotic lower bound for OPT(_F,k_). Let \(i\in[t-2]\) such that _B=b<sub>i</sub>_. Since _F_ is _k_-bounded, we can use theorem 10 with \(k'\leftarrow\lfloor k-\frac{1}{2}k_i\rfloor\). Writing \(s=c^*(F,k-\frac{1}{2}k_i)\), we obtain<tbc>

\(\mathrm{OPT}(F,k)\ge\Omega(s\mathrm{log}\frac{k-k^\prime}{s})=\Omega(s\mathrm{log}(\frac{1}{2}k_i/s)).\)

<tbc>By lemma 42, we have that \(m_i\le 2s\), which implies<tbc>

\(\mathrm{OPT}(F,k)\ge\Omega(m_i\mathrm{log}(\frac{1}{2}k_i/m_i))=\Omega(b_i)=\Omega(B).\)

<tbc>We can now bound each _m<sub>i</sub>_ in terms of _B_. Recall that _k_ falls by a factor of \(\beta=(1-\frac{1}{4}\delta)\) in every iteration, and let \(\gamma=1/\beta\). Then \(k_{i+1}\le k_i/\gamma\) for all _i\<t_-2, so

\(k_i\ge\gamma k_{i+1}\ge\cdots\ge\gamma^{t-2-i}k_{t-2}\ge\gamma^{t-2-i}B.\)

(Recall that \(b\le\frac{1}{2}\delta k\le k\) until the last iteration.)

Thus, we have

\(m_i\le\frac{B}{\mathrm{log}(k_i/m_i)}=\frac{B\mathrm{log}\gamma}{\mathrm{log}_\gamma(k_i/m_i)}\le\frac{B\mathrm{log}\gamma}{t-2-i+\mathrm{log}_\gamma(B/m_i)}\le\frac{B\mathrm{log}\gamma}{t-1-i}.\)

Thus, \(\sum_{i=1}^{t-2}m_i\le\mathcal{O}(B\mathrm{log}\gamma\cdot\mathrm{log}(t-2))\), using the well-known logarithmic bound for the harmonic series. Since we stop before \(B\ge k\) and reduce _k_ by a constant factor every iteration, the number _t_ of iterations is O(log(_k/B_)). Also recall that we proved \(B\le\mathcal{O}(\mathrm{OPT}(F,k))\) above. Thus, we obtain the desired bound \(\mathcal{O}(B\cdot\mathrm{loglog}(k/B))\le\mathcal{O}(\mathrm{OPTloglog}(k/\mathrm{OPT}))\). The running time bound follows as in theorem 43, since WSHSparseForestSelect2 can only be faster than WSHSparseForestSelect.

## 7.5 An O(OPTlogOPT) algorithm

If _F_ is a _k_-unbounded forest with at least two roots, then \(\mathrm{OPT}(F,k)\ge\Omega(\mathrm{log}k)\) by lemma 9. Thus, the number of comparisons for WSHSparseForestSelect2 on _F_ is<tbc>

\(\mathcal{O}(\mathrm{OPTloglog}(k/\mathrm{OPT}))\le\mathcal{O}(\mathrm{OPTlogOPT}).\)

