_Warmup Proof of Lemma 4.7._ The main idea is to use a specific determinant as a generating function for the set of basis costs, \(\{c(S):S\in\mathcal{F}\}\). For a linear matroid of rank _k_ represented by \(V=\{v_1,\dots,v_n\}\subseteq\mathbb{R}^k\), we use the Cauchy-Binet identity to infer:<tbc>

\(det\left(\sum_{i=1}^nx_iv_iv_i^T\right)=\sum_{S\in\mathcal{F}}\left(\prod_{i\in S}x_i\right)det(V_S)^2,\)

<tbc>where _V<sub>S</sub>_ is the \(k\times k\) matrix with columns indexed by _S_, and \(det(V_S)\neq 0\) if and only if \(S\in\mathcal{F}\). We now define a polynomial _P(x_) by setting _x<sub>i</sub>=x<sup>c<sub>i</sub></sup>_, where _c<sub>i</sub>_’s are the given scalars: i.e.,

\(P(x)=det\left(\sum_{i=1}^nx^{c_i}v_iv_i^T\right)=\sum_{S\in\mathcal{F}}x^{\sum_{i\in S}c_i}det(V_S)^2=\sum_{S\in\mathcal{F}}x^{c(S)}det(V_S)^2.\) (11)

The exponents with non-zero coefficients in _P(x_) are precisely the basis costs \(\{c(S)|S\in\mathcal{F}\}\). The degree of _P(x_) is bounded by _nM_. We can therefore find _P(x_) exactly using polynomial interpolation by evaluating it at _O(nM_) points. This process runs in poly(_n,M_) time. Once the polynomial _P(x_) is known, we can inspect its coefficients to find if any exponent \(c\notin Z\) has a non-zero coefficient.

Furthermore, the associated basis can be found using self-reducibility for matroids. For each element \(j\in U\), we compute the "edge-deletion" polynomial \(P_j(x)=det(\sum_{i\neq j}x^{c_i}v_iv_i^T)\): if _c_ appears as an exponent in _P<sub>j</sub>(x_), a basis with cost _c_ exists without _j_. We delete _j_ and recurse on the smaller problem. On the other hand, if _c_ does not appear in _P<sub>j</sub>(x_), then _j_ must be in every basis _S_ with _c(S_)=_c_. We select _j_ and recurse, searching for a basis with cost _c-c<sub>j</sub>_ in the problem on _U/{j_} (i.e., using an "edge-contraction" polynomial _P<sub>/j</sub>(x_))

When the bound _M_ is large, the poly(_n,M_) time bound is infeasible, as the degree of _P(x_) is too high for efficient interpolation. The full proof, which appears in Section C, avoids this problem by remaindering; i.e., working with the polynomial _P(x_) (mod(_x<sup>p</sup>_-1)) for a suitable prime \(p\in poly(n,\ell,logM)\). This prime is chosen so that the residues modulo _p_ of all values in _Z_ and at least one basis cost \(c\notin Z\) (if such a basis exists) are distinct. This allows for efficient interpolation and reconstruction within the required time bounds. Now we can use Lemma 4.7 to prove Theorem 1.5.

**Theorem 1.5** (Efficient Optimization over Linear Matroids)**.** _Let_ F _be the bases of a rank-k linear matroid_ M=(_U,_I)_, represented by_ \(V\in\mathbb{R}^{k\times n}\) _with entry representation size_ poly(_n). For an unknown integer weight function w_<sup>∗</sup> _satisfying_ \(|w_e^*|\le B\)_, we can sort the bases according to their weight w_<sup>∗</sup>(_S), and hence find the minimum-weight basis_ \(argmin_{S\in\mathcal{F}}w^*(S)\) _in_ poly(_n,B_) _time. The number of comparison queries required is O(nB_log_nB_) _and more generally, O_((_n+C_)log_C), where_ \(C=|\{w^*(S):S\in\mathcal{F}\}|\) _is the number of distinct basis weights._

_Proof._ From Algorithm Section 4.1.1, the stated query complexity follows directly from Theorem 4.2. It remains to bound the total running time required to implement the separation steps.

The maintenance of buckets, affine subspaces, and the corresponding updates can each be carried out in poly(_n,B_) time overall. By Lemma 4.1, the number of separation steps is bounded by _O(nB_). Each separation step invokes the procedures in Lemma 4.6 and Lemma 4.7, which take poly(_n,_log_M_) and \(poly(n,\ell,logM)\) time, respectively. Summing over all separation steps gives a total time of poly(_n,B_), using the facts that \(\ell=O(nB)\) and _M_=2<sup>poly(_n_)</sup>, the latter following from Lemma 4.3.

