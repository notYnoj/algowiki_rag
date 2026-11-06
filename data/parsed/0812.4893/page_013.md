## 6.2 Proof of Theorem 2

Let a positive integer weight _w(e_) for each edge \(e\in E\) be given as input. Assign the preferences of each node _v_ so that whenever _w_({_v,x_})_\>w_({_v,y_}) for two edges \(\{v,x\},\{v,y\}\in E\), _v_ prefers _x_ to _y_. Execute the algorithm in Section 4 for _i_ rounds to obtain the matching _M<sub>i</sub>_. Let \(M^*\subseteq E\) be a maximum-weight matching.

For each red node \(r\in R\), let \(g(r)\subseteq B\) consist of the matches of _r_ in _M<sub>i</sub>_ and in _M_<sup>∗</sup>, if any. In particular, \(|g(r)|\le 2\) for all \(r\in R\), and \(|g^{-1}(b)|\le 2\) for all \(b\in B\).

Let \(\{r,b\}\in M^*\) with \(r\in R\) and \(b\in B\). Exactly one of the following holds at the end of round _i_:

1. The node _r_ has not received a response from _b_. If _r_ is matched with \(b_2\neq b\), _r_ prefers _b_<sub>2</sub> over _b_ and \(w(\{r,b\})\le w(\{r,b_2\})=w_i(b_2)\). Otherwise _r_ is unmatched, _b_ is in _C<sub>i</sub>(r_), and \(w(\{r,b\})\le f_i(r)\).<tbc>

2. The node _r_ has received a response from _b_. Then _b_ is matched with _r_ or with some other red node that _b_ prefers over _r_. Thus \(w(\{r,b\})\le w_i(b)\).

For every \(\{r,b\}\in M^*\) thus<tbc>

\(w(\{r,b\})\le f_i(r)+\sum_{c\in g(r)}w_i(c)\)

<tbc>and hence

\(w(M^*)=\sum_{\{r,b\}\in M^*}w(\{r,b\})\)<br>
\(\le\sum_{r\in R}f_i(r)+\sum_{r\in R}\sum_{c\in g(r)}w_i(c)\)<br>
\(\le\sum_{R\in R}f_i(r)+\sum_{b\in B}2w_i(b)\)<br>
\(=f_i(R)+2w_i(B).\)

From Lemma 6 we conclude that

\(w(M^*)\le(2+\epsilon)w_i(B)=(2+\epsilon)w(M_i)\)

whenever \(i\ge 1+(\Delta-1)/\epsilon\).

We can choose an integer \(i<2+\Delta/\epsilon\). We can compute _M<sub>i</sub>_ in _i_ rounds or \(T=2i<4+2\Delta/\epsilon\) synchronous communication steps.

## 6.3 Proof of Theorem 3

Let us first recall a convenient Chernoff-type upper bound for the tail probability of a binomial random variable _Z_∼Bin(_k,p_), where _k_ is a positive<tbc>

