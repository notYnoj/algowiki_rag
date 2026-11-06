_Proof of Lemma 5.17._ Observe \(s\in S'\) is only possible for an iteration \(t\in T(i,b)\) when level(_s_)=level(_s,b_). Fix some \(\ell=\text{level}(s)=\text{level}(s,b)\). Observe that \(s\in S'\) holds in an iteration where \(t\in T(i,b)\) and level\((s)=\text{level}(s,b)=\ell\) if and only if

\(\emptyset\neq\mathcal{A}(s,b)\cap V_i^{(b)}\subseteq\bigcup_{r=\ell-b+1}^\ell L(s,r)\cap V_i^{(b)}\neq\emptyset.\) (3)

Furthermore, this holds in at most one iteration \(t\in T(i,b)\) where \(\ell=\text{level}(s)=\text{level}(s,b)\). This follows as we remove \(V_i^{(b)}\) from A(_s,b_) after the first iteration that this occurs, thus guaranteeing that A(_s,b_) is disjoint from \(V_i^{(b)}\) until level(_s,b_) is increased.

Thus, as in Lemma 5.5, it suffices to bound the number of \(\ell\) where Equation (3) holds. Since \(V_i^{(b)}\) has hop diameter _d_, \(V_i^{(b)}\) has diameter 2_bd_. Then,

\(V_i^{(b)}\subseteq\bigcup_{r=\ell_0}^{\ell_0+2bd}L(s,r)\)

for some \(\ell_0\). We conclude by bounding the number of distinct values of \(\ell\) by \(\lceil\frac{2bd+1}{b}\rceil\le 3d\).

Next, we may bound the size of _T(i,b_) following identical arguments as Lemma 5.6.

**Lemma 5.18.** _For all_ \(V_i^{(b)}\), \(T(i,b)=\tilde{O}\left(\frac{d\phi n\mathrm{log}B\mathrm{log}n}{\left|N\left(V_i^{(b)}\right)\right|}\right)\).

_Proof of Lemma 5.18._ We repeat the argument for completeness. As before, let \(T_k(i,b)\subseteq T(i,b)\) denote the iterations of the while loop where \(\frac{|S_\mathrm{in}|}{2^{k-1}}\ge|S|\ge\frac{|S_\mathrm{in}|}{2^k}\). Thus, \(T(i,b)=\bigcup_{k=1}^{\mathrm{log}|S_\mathrm{in}|}T_k(i,b)\) as the while loop terminates once |_S_| is empty.

We bound |_T<sub>k</sub>(i,b_)| for \(k\ge 1\). Fix an iteration of the while loop \(t\in T_k(i,b)\) where \(V_i^{(b)}\) is the chosen cluster. Since \(|S|\ge\frac{|S_\mathrm{in}|}{2^k}\) , we have \(\mathrm{score}(i,b)>\frac{|S|\left|N\left(V_i^{(b)}\right)\right|}{2\phi n\mathrm{log}B}\ge\frac{|S_\mathrm{in}|\left|N\left(V_i^{(b)}\right)\right|}{2^{k+1}\phi n\mathrm{log}B}\) . In particular, there are \(\frac{|S_\mathrm{in}|\left|N\left(V_i^{(b)}\right)\right|}{2^{k+1}\phi n\mathrm{log}B}\) distinct sources in _S_ where \(\mathcal{A}(s)\cap V_i^{(b)}\neq\emptyset\): i.e. \(S'(t)\) contains at least \(\frac{|S_\mathrm{in}|\left|N\left(V_i^{(b)}\right)\right|}{2^{k+1}\phi n\mathrm{log}B}\) vertices, where \(S'(t)\) denotes the set \(S'\) chosen in the _t_-th iteration of the while loop. From Lemma 5.17, we know that each source \(s\in S_\mathrm{in}\) is in \(S'\) for at most 3_d_ distinct iterations in _T<sub>k</sub>(i,b_). Combining the above observations,<tbc>

\(3|S|d\ge\sum_{s\in S}|\{t\in T_k(i,b)\text{s.t.}s\in S'(t)\}|=\sum_{t\in T_k(i,b)}|\{s\in S'(t)\}|\ge|T_k(i,b)|\frac{\left|S_\mathrm{in}\right|\left|N\left(V_i^{(b)}\right)\right|}{2^{k+1}\phi n\mathrm{log}B}.\)

<tbc>Rearranging and applying the upper bound \(|S|\le\frac{|S_\mathrm{in}|}{2^{k-1}}\),

\(|T_k(i,b)|\le\frac{2^{k+1}\phi n\mathrm{log}B}{\left|N\left(V_i^{(b)}\right)\right|\left|S_\mathrm{in}\right|}\frac{3|S_\mathrm{in}|d}{2^{k-1}}\le\frac{12d\phi n\mathrm{log}B}{\left|N\left(V_i^{(b)}\right)\right|}.\)

Summing over _k_ and using \(|S_\mathrm{in}|\le n\) we get \(|T(i,b)|=O\left(\frac{d\phi n\mathrm{log}B\mathrm{log}n}{\left|N\left(V_i^{(b)}\right)\right|}\right)\).

Finally, we bound the total running time of all iterations where \(V_i^{(b)}\) is chosen using similar arguments as Theorem 5.1. We break into two cases.

