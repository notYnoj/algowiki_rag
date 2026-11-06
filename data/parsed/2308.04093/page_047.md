as desired.

The total time complexity of applying Theorem B.4 at the _k_-th level of the recursion tree is \(O(n+2^k\cdot b_km)\). From \(b_k\ge b_{k-1}/2\), or equivalently \(2^kb_k\ge 2^{k-1}b_{k-1}\), we know 2_<sup>k</sup>b<sub>k</sub>_ is maximized at _k_=log<sub>2</sub>(_r_). Hence, the total time complexity over all log<sub>2</sub>(_r_) levels is at most

\(\sum_{k=1}^{log_2(r)}O(n+2^kb_k\cdot m)\le log_2(r)\cdot O(n+2^{log_2(r)}b_{log_2(r)}\cdot m)\)<br>
\(\le O(nlogr+rmlogrlogm).\)

## B.5 Proof of Lemma 4.10

**Lemma 4.10.** _Given m sets_ \(S_1,S_2,\dots,S_m\in[n]\) _with_ \(|S_i|\le b\)_, there is a deterministic algorithm in O(n_log_m+mb_<sup>3</sup>) _time that computes_ \(k\le log_2(2m)\) _colorings_ \(h_1,h_2,\dots,h_k:[n]\rightarrow[b^2]\)_, such that for every_ \(i\in[m]\) _there exists an h<sub>j</sub> that assigns distinct colors to elements of S<sub>i</sub>._

_Proof._ We iteratively apply the following claim:

**Claim B.5.** _Given m sets_ \(S_1,\dots,S_m\in[n]\) _with_ \(|S_i|\le b\)_, there is a deterministic algorithm in O(n+mb_<sup>3</sup>) _time that computes a coloring_ \(h:[n]\rightarrow[b^2]\)_, such that for at least_ 1/2 _fraction of the_ \(i\in[m]\)_, h assigns distinct colors to elements of S<sub>i</sub>._

To prove Lemma 4.10, we use Claim B.5 to find an coloring _h_, and recurse on the remaining sets _S<sub>i</sub>_ that do not receive distinct colors under _h_. Finally we return all the computed colorings. Since the number of remaining sets gets halved in each iteration, we terminate within log<sub>2</sub>(2_m_) iterations, and the total time complexity is _O(n_log_m+mb_<sup>3</sup>). In the following, it remains to prove Claim B.5.

First note that a uniformly random coloring \(h:[n]\rightarrow[b^2]\) assigns distinct colors to a fixed set _S<sub>i</sub>_ with probability at least \(1-\genfrac(){pt}{2}{|S_i|}{2}\cdot\frac{1}{b^2}\ge 1/2\) by a union bound over all \(\genfrac(){pt}{2}{|S_i|}{2}\) pairs of distinct \(x,y\in S_i\). We now use the standard method of pessimistic estimators to derandomize this random construction. Without loss of generality, assume |_S<sub>i</sub>_|=_b_ for all _i_. We decide the colors \(h(j)\in[b^2]\) sequentially for _j_=1,2_,...,n_. Let \(x_i^{(j)}=|S_i\cap[j]|\) denote the number of already colored elements in _S<sub>i</sub>_. Assuming _S<sub>i</sub>_ has not received repeated colors among its first \(x_i^{(j)}\) elements so far, the probability that coloring the remaining elements causes _S<sub>i</sub>_ to have repeated colors is at most \(p(x_i^{(j)})\) given by \(p(x):=\frac{1}{b^2}\cdot(x\cdot(b-x)+\genfrac(){pt}{2}{b-x}{2})\).

Given the already decided colors _h_(1)_,...,h(j_), define estimator

\(e_i^{(j)}=\left\{\begin{array}{ c c }
1 & S_i\text{has already received repeated colors,} \\
p(x_i^{(j)}) & \text{otherwise.}
\end{array}\right.\)

Then \(\sum_{i=1}^me_i^{(0)}=m\cdot p(0)<m/2\).

Now we verify that \(\mathbf{E}_{h(j+1)\in[b^2]}[e_i^{(j+1)}]\le e_i^{(j)}\). Here it suffices to consider the case where the first \(x=x_i^{(j)}\) elements of _S<sub>i</sub>_ have not received repeated colors, and _j_+1 is the (_x_+1)-st element in _S<sub>i</sub>_ to be colored. Then

\(\mathbf{E}_{h(j+1)\in[b^2]}[e_i^{(j+1)}]-e_i^{(j)}=\big(\frac{x}{b^2}\cdot 1+(1-\frac{x}{b^2})\cdot p(x+1)\big)-p(x)\)<br>
\(=-\frac{x(b+x)(b-x-1)}{2b^4}\)<br>
\(\le 0.\)

