_Proof._ We will prove the existence via a probabilistic argument. Consider the following random process for constructing an assignment \(A=\left((p_1,q_1),\dots,(p_\ell,q_\ell)\right)\).

1. Assign _p_<sub>1</sub>=1.<tbc>

2. For any \(2\le i\le\ell\), sequentially assign _p<sub>i</sub>_ uniformly at random among {1,2,3}\\{_p_<sub>_i_-1</sub>}<tbc>

3. For each _j_, assign \(q_j\in\{1,2\}\) independently.

We make the following miniclaim: for any (_i,j_) that \(|i-j|\ge 2\), we have (_i,j_) being matched by _A_ with probability at least \(\frac{1}{8}\). To see this, assume WLOG that \(i\ge j+2\). Then, we have

\(\mathrm{Pr}(p_i=p_j)=\mathrm{Pr}(p_{i-1}=p_j)\cdot\mathrm{Pr}(p_i=p_j|p_{i-1}=p_j)+\mathrm{Pr}(p_{i-1}\neq p_j)\cdot\mathrm{Pr}(p_i=p_j|p_{i-1}\neq p_j)\)<br>
\(=\frac{1}{2}\cdot\mathrm{Pr}(p_{i-1}\neq p_j)\)

since Pr(_p<sub>i</sub>=p<sub>j</sub>|p_<sub>_i_-1</sub>=_p<sub>j</sub>_)=0 and \(\mathrm{Pr}(p_i=p_j|p_{i-1}\neq p_j)=\frac{1}{2}\). Moreover, we have

\(\mathrm{Pr}(p_{i-1}\neq p_j)\)<br>
\(=\mathrm{Pr}(p_{i-2}=p_j)\cdot\mathrm{Pr}(p_{i-1}\neq p_j|p_{i-2}=p_j)+\mathrm{Pr}(p_{i-2}\neq p_j)\cdot\mathrm{Pr}(p_{i-1}\neq p_j|p_{i-1}\neq p_j)\)<br>
\(=\mathrm{Pr}(p_{i-2}=p_j)+\frac{1}{2}\cdot\mathrm{Pr}(p_{i-2}\neq p_j)\)<br>
\(=\frac{1}{2}+\frac{1}{2}\cdot\mathrm{Pr}(p_{i-2}=p_j).\)

where the second equality is true via the construction: we have \(\mathrm{Pr}(p_{i-1}\neq p_j|p_{i-2}=p_j)=1\) and \(\mathrm{Pr}(p_{i-1}\neq p_j|p_{i-1}\neq p_j)=\frac{1}{2}\). It is worth noting that these chain of equations subtly relies on the assumption that \(i\ge j+2\). This condition ensures that our random process assigns a value to _p<sub>j</sub>,...,p_<sub>_i_-2</sub>_,p_<sub>_i_-1</sub>, and _p<sub>i</sub>_ in that particular order.

Combining the two equations, we have \(\mathrm{Pr}(p_i=p_j)=\frac{1}{4}+\frac{1}{4}\cdot\mathrm{Pr}(p_{i-2}=p_j)\ge\frac{1}{4}\). Since _q<sub>i</sub>_ and _q<sub>j</sub>_ are assigned uniformly and independently among {1,2}, and independent of _p<sub>i</sub>_ and _p<sub>j</sub>_, we have

\(\mathrm{Pr}(p_i=p_j\wedge q_i\neq q_j)=\mathrm{Pr}(p_i=p_j)\cdot\mathrm{Pr}(q_i\neq q_j)\ge\frac{1}{8}.\)

In other words, (_i,j_) are matched by _A_ with probability at least \(\frac{1}{8}\), thereby proving our miniclaim.

Now consider drawing _t_=24log_n_ independently random assignments from the above process. For any pair \((i,j)\in[\ell]^2\) with \(|i-j|\ge 2\), the probability that (_i,j_) is not matched by any of the _t_ assignments is at most

\(\left(\frac{7}{8}\right)^{24\mathrm{log}n}\le n^{-3}.\)

Applying the union bound over all _O(n_<sup>2</sup>) possible pairs of (_i,j_)’s, w.h.p. every such pairs is matched by at least one among the _t_ assignments. As a consequence, there must be a deterministic choice of those _t_ assignments that the statement remains true, thereby proving our claim.

We are now ready to give an efficient cut-query algorithm for FindLongEdge.

**Lemma 5.8.** FindLongEdge _can be solved deterministically within_ \(O\left(\mathrm{log}\left(n/\delta\right)\right)\) _cut queries to G._

_Proof._ Partition \[0,1\] into \(\ell=\lceil 2/\delta\rceil\) intervals of length \(\delta/2\) (besides the last interval which may be shorter). Denote the _j_<sup>th</sup> interval by \(I_j:=\left[\frac{(j-1)\delta}{2},\frac{j\delta}{2}\right)\). Let A be a set of \(O(\mathrm{log}\ell)\) assignments that follows Claim 5.7 with respect to \(\ell\). Our algorithm proceeds as follows.

