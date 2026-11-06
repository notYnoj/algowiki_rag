Alongside every \(a\in\mathcal{A}_i^{(0)}\) (and later sets \(\mathcal{A}_i^{(j)}\)’s), we will store a set \(X\subseteq S\) such that \(\Sigma(X)=a\). This data structure incurs only an additional poly(_n_) overhead in the running time and will allow us to return a collision. Observe that \(|\mathcal{A}_i^{(0)}|=2^{\lfloor n/k\rfloor}\) for every \(i\in[k]\): if \(|\mathcal{A}_i^{(0)}|<2^{\lfloor n/k\rfloor}\), then during construction of the set \(\mathcal{A}_i^{(0)}\) we detected a collision, i.e., two different sets of the same sum, which we return immediately (e.g., by using a data structure described in the previous sentence). Moreover, all sets \(\mathcal{A}_i^{(0)}\) can be computed in \(\mathrm{poly}(n)\cdot W\) time. Let \(p_i^{(0)}:=0\) for every \(i\in[k]\).

This concludes the construction of the sets \(\mathcal{A}_i^{(j)}\) and \(p_i^{(j)}\) for _j_=0 and \(i\in[k]\). We now iterate over _j_=1,2_,...,_log_k_. In the _j_-th step, we compute the set \(\mathcal{B}_{i,p}^{(j)}\). This set \(\mathcal{B}_{i,p}^{(j)}\subseteq\mathcal{A}_{2i-1}^{(j-1)}+\mathcal{A}_{2i}^{(j-1)}\) such that every \(a\in\mathcal{B}_{i,p}^{(j)}\) satisfies the following modular equation<tbc>

\(a\equiv p\cdot W^{j-1}+p_{2i-1}^{(j-1)}+p_{2i}^{(j-1)}(\mathrm{mod}W^j).\)

<tbc>for every \(i\in[k/2^j]\) and \(p\in\{0,\dots,W-1\}\). If at any point we detect a collision (i.e., two equal elements), we immediately return it. Next, for every \(i\in[k/2^j]\), let \(p^\star\in\{0,\dots,W-1\}\) be the index maximizing \(|\mathcal{B}_{i,p^\star}^{(j)}|\), and define:

\(p_i^{(j)}:=p^\star\cdot W^{j-1}+p_{2i-1}^{(j-1)}+p_{2i}^{(j-1)},\)

and let \(\mathcal{A}_i^{(j)}\) be an arbitrary subset of \(\mathcal{B}_{i,p^\star}^{(j)}\) of size at most _W_ (i.e., we truncate \(\mathcal{B}_{i,p^\star}^{(j)}\) if it exceeds size _W_). This completes the algorithm description.

## Running Time.

Note that \(|\mathcal{A}_i^{(j)}|\le W\) for all \(j\in[\mathrm{log}k]\) and \(i\in[k/2^j]\). The computation of each of these sets takes \(\mathrm{poly}(n)\cdot W^2\) time, which implies the desired running time.

Before addressing correctness, observe that throughout the computation, we maintain the following invariant:

**Claim 4.0.1.** _For every_ \(j\in[\mathrm{log}k]\) _and_ \(i\in[k/2^j]\)_, it holds that:_

\(\mathcal{A}_{2i-1}^{(j-1)}+\mathcal{A}_{2i}^{(j-1)}=\mathcal{B}_{i,0}^{(j)}\unknown\mathcal{B}_{i,2}^{(j)}\unknown\dots\unknown\mathcal{B}_{i,W-1}^{(j)}.\) (1)

_Proof:_ Fix \(j\in[\mathrm{log}k]\) and \(i\in[k/2^j]\). For every \(p\neq p'\) the sets \(\mathcal{B}_{i,p}^{(j)}\) and \(\mathcal{B}_{i,p^\prime}^{(j)}\) are disjoint because they contain numbers in different congruence classes modulo _W<sup>j</sup>_. Next, observe that for every \(j\in[\mathrm{log}k]\) and \(i\in[k/2^j]\), it holds that for every \(a\in\mathcal{A}_i^{(j)}\):<tbc>

\(a\equiv p_i^{(j)}(\mathrm{mod}W^j).\)

<tbc>Let \(\mathcal{B}:=\mathcal{A}_{2i-1}^{(j-1)}+\mathcal{A}_{2i}^{(j-1)}\). By definition \(\mathcal{B}\supseteq\mathcal{B}_{i,p}^{(j)}\) for every \(0\le p<W\) , hence it remains to prove the \(\subseteq\) of (1). Observe that for every \(b\in\mathcal{B}\) it holds that:<tbc>

\(b\equiv p_{2i-1}^{(j-1)}+p_{2i}^{(j-1)}(\mathrm{mod}W^{j-1}).\)

<tbc>Therefore, for every \(b\in\mathcal{B}\) there exists \(p\in\{0,\dots,W-1\}\) such that

\(b\equiv p\cdot W^{j-1}+p_{2i-1}^{(j-1)}+p_{2i}^{(j-1)}(\mathrm{mod}W^j),\)

which in particular means that \(b\in\mathcal{B}_{i,p}^{(j)}\).

