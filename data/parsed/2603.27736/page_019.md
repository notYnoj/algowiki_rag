Of course, knowing only _A_, _U_, and _V_ it is easy to complete the rank decomposition by constructing _S_ in time _O(nmr_) (for all our applications this running time is strictly subcubic and hence tolerable). The benefit of Definition 3.4 is rather that it is convenient to have access to the "selector" matrix _S_.

In a later key step, it will be crucial that the given rank decomposition satisfies an additional structural property, namely that it is _row-_ or _column-regular_ defined as follows.

**Definition 3.5** (Regular Rank Decomposition)**.** _Let_ (_U,V,S_) _be a rank-r decomposition of some_ \(n\times m\) _matrix, and let_ \(R\ge 1\)_. We call_ (_U,V,S_) _R_-row-regular _if, for all_ \(\ell\in[r]\) _and all_ \(i\in[n]\),

\(|\{j\in[m]:S[i,j]=\ell\}|\le R\cdot\frac{m}{r}.\)

_Analogously, we call_ (_U,V,S_) _R_-column-regular _if, for all_ \(\ell\in[r]\) _and all_ \(j\in[m]\),

\(|\{i\in[n]:S[i,j]=\ell\}|\le R\cdot\frac{n}{r}.\)

The following lemma states that we can transform any rank decomposition into a regular one without loss of generality. Specifically, it states that any matrix _A_ with a given rank-_r_ decomposition can be split into a row-regular part _A_<sub>row</sub>, a column-regular part _A_<sub>col</sub>, and a _small_ part _A_<sub>sm</sub> with strictly smaller rank, _r/_2. Algorithmically we will simply _recurse_ on this small part, which effectively means that we can always treat _A_ as partly row-regular and partly column-regular.

**Lemma 3.6** (Regular Rank Decomposition)**.** _For any matrix_ \(A\in(\mathbb{Z}\cup\{\perp\})^{n\times m}\) _with rank_ \(r(A)\le r\) _there is a partition_ \(A=A_\mathrm{row}\sqcup A_\mathrm{col}\sqcup A_\mathrm{sm}\) _such that_

• _A_<sub>row</sub> _has an O_(log(_nm_))_-row-regular rank-r decomposition,_<tbc>

• _A_<sub>col</sub> _has an O_(log(_nm_))_-column-regular rank-r decomposition, and_<tbc>

• _A_<sub>sm</sub> _has rank_ \(r(A_\mathrm{sm})\le r/2\).

_Moreover, given A and a corresponding rank-r decomposition we can compute the matrices A_<sub>row</sub>_,A_<sub>col</sub>_,A_<sub>sm</sub> _along with their claimed decompositions in deterministic time_ \(\tilde{O}(nmr)\).

The proof of Lemma 3.6 relies on the following covering-type lemma.

**Lemma 3.7** (Conflict-Free Covering)**.** _Let_ \(x_1,\dots,x_n\in[r]\) _and let_ \(C_1,\dots,C_n\subseteq[r]\) _be sets of size at most s such that_ \(x_i\unknown\in C_i\) _for all i. We say that a set_ \(S\subseteq[r]\) covers _item i if_ \(x_i\in S\) _and_ \(C_i\cap S=\emptyset\)_. Then there is a collection_ S _of size_ \(|\mathcal{S}|\le O(s\mathrm{log}n)\) _so that each_ \(i\in[n]\) _is covered by some set_ \(S\in\mathcal{S}\)_. Moreover, there is a deterministic_ \(\tilde{O}(nr)\)_-time algorithm that constructs_ S_, along with a mapping_ \([n]\rightarrow\mathcal{S}\) _indicating for each item i by which set it is covered._

**Proof Sketch.** Here, we only provide a quick proof sketch based on a probabilistic argument; in Appendix B we will then efficiently derandomize this argument based on the method of conditional expectations. The construction of S is simple: Take _O(s_log_n_) independently random sets \(S\subseteq[r]\) with sample rate 1/(2_s_). Each such set _S_ covers any fixed index _i_ with probability at least \(\Omega(1/s)\). Indeed, the probability that \(x_i\in S\) is 1/(2_s_), and independently we avoid all conflicts, \(C_i\cap S=\emptyset\), with probability at least \(1-|C_i|/(2s)\ge 1/2\). Hence, after _O(s_log_n_) repetitions we covered all items with high probability.

**Proof of Lemma 3.6.** Let (_U,V,S_) denote the rank-_r_ decomposition of _A_, and let \(R=\Theta(\mathrm{log}(nm))\) (where we determine the implied constant later). If \(r\le R\) then this rank-_r_ decomposition is trivially _R_-row-regular (and we can simply take _A_<sub>row</sub>=_A_ without modifying the decomposition), so suppose that _r\>R_. For each \(\ell\in[r]\) define the sets

\(I_\ell=\left\{i\in[n]:|\{j\in[m]:S[i,j]=\ell\}|>R\cdot\frac{m}{r}\right\},\)<br>
\(J_\ell=\left\{j\in[m]:|\{i\in[n]:S[i,j]=\ell\}|>R\cdot\frac{n}{r}\right\}.\)

