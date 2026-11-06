**Theorem 7.2.** _If the universal variant of the matching problem for the prefix relation can be solved in time_ \(O((|w|m)^{1-\epsilon})\) _for some_ \(\epsilon>0\)_, then SETH fails. This holds even if we operate on an alphabet of constant size._

_Proof._ Let _w_ be an input string and _M_ an \(\varepsilon\)NFA. In time _O_(|_M_|) we can construct an \(\varepsilon\)NFA \(M'\) with \(\mathsf{L}(M')=(\mathsf{L}(M)\cdot\{\#\})\cup\Sigma^*\) for a new symbol #.

If \(w\in\mathsf{L}(M)\), then \(w\#\in\mathsf{L}(M')\), which means that \(\Lambda_{\unknown_\mathsf{pre}}(w\#)\subseteq\mathsf{L}(M')\). If \(\Lambda_{\unknown_\mathsf{pre}}(w\#)\subseteq\mathsf{L}(M')\), then \(w\#\in\mathsf{L}(M')\), which means that \(w\in\mathsf{L}(M)\). Thus, if we could decide whether \(\Lambda_{\unknown_\mathsf{pre}}(w\#)\subseteq\mathsf{L}(M')\) in time \(O((|w\#|\cdot|M'|)^{1-\epsilon})\) for some \(\epsilon>0\), then we would also have decided whether \(w\in\mathsf{L}(M)\) in time \(O((|w|\cdot|M|)^{1-\epsilon})\). This concludes using the results of \[BI16\].

Using a slightly more complicated reduction<sup>5</sup> from the _orthogonal vectors problem_, we can also show that the _O_(|_w_|<sup>2</sup>_m_) upper bound for the universal variant of the matching problem for the infix relation is conditionally optimal under SETH. Recall that, in the _orthogonal vectors problem (OV)_, we are given two sets _U_={_u_<sub>1</sub>_,...,u<sub>n</sub>_}, _V_={_v_<sub>1</sub>_,...,v<sub>n</sub>_} of _d_-dimensional Boolean vectors, with \(d=\omega(logn)\), and want to determine whether there are two orthogonal vectors _u<sub>i</sub>_ and _v<sub>j</sub>_, i.e., whether there exist \(i,j\in[n]\) such that \(u_i\cdot v_j=\sum_{k=1}^du_i[k]\cdot v_j[k]=0\). For convenience, we also use the notation \(u\perp v\) to denote that vectors _u_ and _v_ are orthogonal. The following is well-known:

**Lemma 7.3** (\[Wil05\], see, e.g., \[ABDN18\], Conjecture 1.1)**.** _If there is an algorithm that solves OV in time_ \(O(n^{2-\epsilon}\text{poly}(d))\) _for some_ \(\epsilon>0\)_, then SETH fails._

Using the result above, we can now show:

**Theorem 7.4.** _If we can solve the universal variant of the_ \(\unknown_\text{in}\)_-matching problem on alphabet_ \(\Sigma=\{0,1\}\) _in time_ \(O(|w|^{2-\epsilon}\text{poly}(m))\) _for some_ \(\epsilon>0\)_, then SETH fails._

_Proof._ We reduce from OV. We are given two sets _U_={_u_<sub>1</sub>_,...,u<sub>n</sub>},V_={_v_<sub>1</sub>_,...,v<sub>n</sub>_} of Boolean _d_-dimensional vectors, where \(d=\omega(logn)\), and want to determine whether there exist \(i,j\in[n]\) such that \(u_i\cdot v_j=0\). We will build an NFA _A_ and string \(w\in\Sigma^*\) such that there is an infix of _w_ that is not in L(_A_) if and only if there exist \(i,j\in[n]\) such that \(u_i\cdot v_j=0\). Let \(h:\Sigma^*\rightarrow\Sigma^*\) be the homomorphism defined by _h_(0)=000 and _h_(1)=010, and define _B_=11011 and _E_=11111 as beginning and end markers. We can now construct

\(w=(Bh(u_1))(Bh(u_2))\dots(Bh(u_n))(h(v_1^R)E)(h(v_2^R)E)\dots(h(v_n^R)E),\)

where the parentheses are only used for the convenience of the reader and are not part of the string itself. It is not hard to see that \(u_i\cdot v_j\neq 0\) if and only if there is some \(k\in[d]\) such that _h(u<sub>i</sub>_)\[3_k_-2:3_k_\] and _h(v<sub>j</sub>_)\[3_k_-2:3_k_\] are both equal to _h_(1)=010, namely, _h(u<sub>i</sub>_)\[3_k_-2:3_k_\]=_h(v<sub>j</sub><sup>R</sup>_)\[3(_d-k_+1)-2:3(_d-k_+1)\]=010.

Let us now build the NFA _A_ that rejects exactly the infixes of _w_ that witness \(u_i\cdot v_j=0\) for some \(i,j\in[n]\). We construct _A_ as the union of three NFAs _A<sub>B</sub>_, _A<sub>E</sub>_, and \(A'\). The NFA _A<sub>B</sub>_ accepts all strings that do not start with _B_, and the NFA _A<sub>E</sub>_ accepts all strings that do not end with _E_; it is not hard to achieve |_A<sub>B</sub>_|=|_A<sub>E</sub>_|=_O_(1). Finally, the NFA \(A'\) accepts all strings of the form \(B\Sigma^{3(k-1)}010\Sigma^*010\Sigma^{3(k-1)}E\) for some \(k\in[d]\). By a naive construction of \(A'\), we can achieve \(|A'|=O(d^2)\), which suffices for our purpose. Overall, we thus obtain |_A_|=_O(d_<sup>2</sup>).

Let us give an intuitive explanation of which infixes are accepted by the NFA _A_. Let (_Bh(u<sub>i</sub>_)) (resp., \((h(v_j^R)E)\)) be the block corresponding to _u<sub>i</sub>_ (resp., _v<sub>j</sub>_). Then, intuitively, we use _A<sub>B</sub>_ to match all infixes that do not start at the beginning of some _u<sub>i</sub>_-block. Analogously, we use _A<sub>E</sub>_ to match all infixes that do not end at the end of some _v<sub>j</sub>_-block. This means that _A<sub>B</sub>_ and _A<sub>E</sub>_ accept all ‘ill-formed’ infixes, whereas \(A'\) only has to consider infixes that consist of complete blocks, and accepts the infix starting at the _u<sub>i</sub>_-block and ending at the _v<sub>j</sub>_-block if and only if there is some \(k\in[d]\) witnessing \(h(u_i[k])=h(v_j^R[d-k+1])=h(v_j[k])=010=h(1)\), i.e., \(u_i[k]\cdot v_j[k]=1\).

Let us now show that \(\Lambda_{\unknown_\text{in}}(w)\unknown\subseteq\mathsf{L}(A)\) (i.e., there is an infix \(\unknown_\text{in}w\) such that \(u\notin\mathsf{L}(A)\)) if and only if there exist \(i,j\in[n]\) with \(u_i\cdot v_j=0\). First, assume that _u<sub>i</sub>_ and _v<sub>j</sub>_ are orthogonal<tbc>

<sup>5</sup>We note that this bound was first discussed online, see \[Ama\].

