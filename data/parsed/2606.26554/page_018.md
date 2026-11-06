<tbc>\(\hat{L}(s,\text{level}(s))\) untouched until A(_s_) is empty, at which point we increment level(_s_) to a larger value and reset A(_s_). Furthermore, for each value of level(_s_), \(s\in S'\) for at most one iteration where _V<sub>i</sub>_ is chosen, since whenever \(s\in S'\), we remove _V<sub>i</sub>_ from A(_s_). Since A(_s_) does not add elements until level(_s_) is incremented again, \(s\unknown\in S'\) for further iterations where _V<sub>i</sub>_ is chosen. Thus, it suffices to bound the number of distinct level(_s_) for which \(V_i\cap\hat{L}(s,\text{level}(s))\neq\emptyset\).

We conclude by arguing that _V<sub>i</sub>_ can only intersect few _L(s,r_). Since \(\text{diam}(V_i)\le d\), the triangle inequality implies that for any \(u,v\in V_i\),

\(|\text{dist}(s,u)-\text{dist}(s,v)|\le\text{dist}(u,v)\le d.\)

In particular, for all \(s\in S\), \(V_i\subseteq\bigcup_{r=t}^{t+d}L(s,r)\) for some \(t\ge 0\). Thus, we have \(k\le d+1\) as desired.

Next, we bound the size of _T(i_).

**Lemma 5.6.** _For all V<sub>i</sub>,_ \(|T(i)|=O\left(\frac{d\phi n\mathrm{log}n}{|N(V_i)|}\right)\).

_Proof of Lemma 5.6._ Observe that |_S_| is monotonically decreasing from |_S_<sub>in</sub>|. Let \(T_k(i)\subseteq T(i)\) denote the iterations of the while loop where \(\frac{|S_\mathrm{in}|}{2^{k-1}}\ge|S|\ge\frac{|S_\mathrm{in}|}{2^k}\) . Thus, \(T(i)=\bigcup_{k=1}^{\mathrm{log}|S_\mathrm{in}|}T_k(i)\) as the while loop terminates once |_S_| is empty.

We bound |_T<sub>k</sub>(i_)| for \(k\ge 1\). Fix an iteration of the while loop \(t\in T_k(i)\) where _V<sub>i</sub>_ is the chosen cluster. Since \(|S|\ge\frac{|S_\mathrm{in}|}{2^k}\) , we have \(\text{score}(i)>\frac{|S||N(V_i)|}{2\phi n}\ge\frac{|S_\mathrm{in}||N(V_i)|}{2^{k+1}\phi n}\) . In particular, there are \(\frac{|S_\mathrm{in}||N(V_i)|}{2^{k+1}\phi n}\) distinct sources in _S_ where \(\mathcal{A}(s)\cap V_i\neq\emptyset\): i.e. \(S'(t)\) contains at least \(\frac{|S_\mathrm{in}||N(V_i)|}{2^{k+1}\phi n}\) vertices, where \(S'(t)\) denotes the set \(S'\) chosen in the _t_-th iteration of the while loop. From Lemma 5.5, we know that each source \(s\in S_\mathrm{in}\) is in \(S'\) for at most _d_+1 distinct iterations in _T<sub>k</sub>(i_). Combining the above observations,<tbc>

\(|S|(d+1)\ge\sum_{s\in S}|\{t\in T_k(i)\text{s.t.}s\in S'(t)\}|=\sum_{t\in T_k(i)}|\{s\in S'(t)\}|\ge|T_k(i)|\frac{|S_\mathrm{in}||N(V_i)|}{2^{k+1}\phi n}.\)

<tbc>Rearranging and applying the upper bound \(|S|\le\frac{|S_\mathrm{in}|}{2^{k-1}}\) ,

\(|T_k(i)|\le\frac{2^{k+1}\phi n}{|N(V_i)||S_\mathrm{in}|}\frac{|S_\mathrm{in}|(d+1)}{2^{k-1}}\le\frac{8d\phi n}{|N(V_i)|}.\)

Summing over _k_ and using \(|S_\mathrm{in}|\le n\) we get \(|T(i)|=O\left(\frac{d\phi n\mathrm{log}n}{|N(V_i)|}\right)\).

Finally, we are ready to bound the total running time of all iterations where _V<sub>i</sub>_ is the chosen cluster. We break into two cases. Recall that \(S'(t)\) denotes the set \(S'\) chosen in the _t_-th iteration of the while loop.

**Case 1:** \(|N(V_i)|\le\frac{\phi n\mathrm{log}n}{|S_\mathrm{in}|}\) **.** An iteration of the while loop requires time \(O\left(|S'(t)||V_i||N(V_i)|\right)\) (since the running time is dominated by the time taken to relax all edges from \(\mathcal{A}(s)\cap V_i\subseteq V_i\) to \(N(\mathcal{A}(s)\cap V_i)\subseteq N(V_i)\)). Over all iterations in _T(i_), the total time is

\(\sum_{t\in T(i)}O\left(|S'(t)||V_i||N(V_i)|\right)=O\left(|V_i||N(V_i)||S_\mathrm{in}|d\right)=O\left(|S_\mathrm{in}||V_i|\frac{\phi nd\mathrm{log}n}{|S_\mathrm{in}|}\right)=O\left(|V_i|\phi nd\mathrm{log}n\right).\)

In the first equality, we use \(\sum_t|S'(t)|=O\left(|S_\mathrm{in}|d\right)\) by Lemma 5.5. In the second equality, we apply our upper bound on |_N(V<sub>i</sub>_)|.

