<tbc>other side of the inequality note that the center string _C_ should have shape _C=T_<sub>1</sub>$_<sup>N</sup>T_<sub>2</sub>$_<sup>N</sup>..._$_<sup>N</sup>T<sub>k</sub>_ for some strings _T_<sub>1</sub>_,...,T<sub>k</sub>_. Now note that for all _j_<tbc>

\(\sum_{i\in[1,k]}\delta_E(T_j,X_i)\ge\delta_E(X_1,X_2,\dots,X_k).\)

<tbc>Because, the _k_-median edit distance minimizes this sum over all possible strings, and _T<sub>j</sub>_ is simply an instantiation of a string. Now note that<tbc>

\(\sum_{j\in[1,k]}\sum_{i\in[1,k]}\delta_E(T_j,X_i)\ge k\delta_E(X_1,X_2,\dots,X_k),\)

<tbc>which implies

\(\sum_{j\in[1,k]}\delta_E(Y_j,C)\ge k\delta_E(X_1,X_2,\dots,X_k).\)

So, the max over all _j_ of \(\delta_E(Y_j,C)\ge\delta_E(X_1,X_2,\dots,X_k)\). This is the definition of the center edit distance, so we have shown both sides of the inequality.

**Theorem 6.29.** _We are given k strings of length M with a SLP of size m. The k-center-edit-distance problem on these strings requires_ \(\left(M^{k-1}m\right)^{1-o(1)}\) _time if SETH is true._

_Proof._ By Theorem 6.5, given _k_ strings, _X_<sub>1</sub>_,...,X<sub>k</sub>_, of length _N_ which all compress to length _n_, _k_-edit distance requires \(\left(N^{k-1}n\right)^{1-o(1)}\) time if SETH is true.

We use the transformation of \[HBGT20\] and produce strings _Y_<sub>1</sub>_,...,Y<sub>k</sub>_. These strings have length _M=kN_ and an SLP of size _m=kn+k_+lg(_N_). As a result \(M^{k-1}m=O\left(N^{k-1}(n+lg(N))\right)\). Thus, an algorithm that runs in \(\left(M^{k-1}m\right)^{1-\epsilon}\) time for _k_-center edit distance for some constant \(\epsilon>0\) implies a violation of SETH. Thus, _k_-center edit distance requires \(\left(M^{k-1}m\right)^{1-o(1)}\) time.

## 7 Hamming Distance and Beyond

Given _k_ equal-length strings _X_<sub>1</sub>_,...,X<sub>k</sub>_ with \(X_i\in\Sigma_i^N\), we define a string \(X=\otimes_{i=1}^kX_i\in(\unknown_{i=1}^k\Sigma_i)^N\) with _X_\[_j_\]=(_X_<sub>1</sub>\[_j_\]_,...,X<sub>k</sub>_\[_j_\]) for \(j\in[1..N]\). In this section, we show that if each string _X<sub>i</sub>_ can be represented using a straight-line program of size _n<sub>i</sub>_, then _X_ can be represented using a straight-line program of size \(O((\prod_{i=1}^kn_i)^{1/k}N^{1-1/k})\). Next, we apply this construction for computing Hamming distance of two grammar-compressed strings and propose several generalizations for _k=O_(1) grammar-compressed strings.

**Proposition 7.1.** _Given k=O_(1) _straight-line programs_ **G**_<sub>i</sub> of sizes n<sub>i</sub> representing strings X<sub>i</sub> of the same length N\>_0_, a straight-line program_ **G** _of size_ \(O((\prod_{i=1}^kn_i)^{1/k}N^{1-1/k})\) _representing_ \(X=\otimes_{i=1}^kX_i\) _can be constructed in time_ \(O((\prod_{i=1}^kn_i)^{1/k}N^{1-1/k})\).

_Proof._ We proceed based on a threshold \(\tau\in[1..N]\) to be fixed later. For each grammar **G**_<sub>i</sub>_, we first use Lemma 3.7 to derive grammars \(\mathbf{G}_i^+\) and \(\mathbf{G}_i^P\) of size _O(n<sub>i</sub>_).

Next, we consider _relevant tuples_ **F**=(_F_<sub>1</sub>_,...,F<sub>k</sub>_) such that:

• each _F<sub>i</sub>_ is a fragment of exp(_A<sub>i</sub>_) for a symbol _A<sub>i</sub>_ of \(\mathbf{G}_i^+\) satisfying \(|A_i|\le\tau\),<tbc>

• \(|F_1|=\cdots=|F_k|\),<tbc>

• there exists \(i_p\in[1..k]\) such that _F<sub>i<sub>p</sub></sub>_ is a prefix of exp(_A<sub>i<sub>p</sub></sub>_),<tbc>

• there exists \(i_s\in[1..k]\) such that _F<sub>i<sub>s</sub></sub>_ is a suffix of exp(_A<sub>i<sub>s</sub></sub>_).

The number of relevant tuples does not exceed \(\tau^{k-1}\cdot k\cdot\prod_{i=1}^kn_i\), because each **F** is uniquely determined by the choices of symbols _A<sub>i</sub>_, the choice of _i<sub>p</sub>_, and the starting positions of _F<sub>i</sub>_ in exp(_A<sub>i</sub>_) for \(i\neq i_p\). (The common length \(|F_1|=\cdots=|F_k|\) is uniquely determined due to the constraint that at least one _F<sub>i</sub>_ is a suffix of exp(_A<sub>i</sub>)._)

For each relevant tuple **F**, we add to **G** a symbol _A_**<sub>F</sub>** aiming at \(exp(A_\mathbf{F})=\otimes_{i=1}^kF_i\). The symbols _A_**<sub>F</sub>** are ordered consistently with the lexicographic order of tuples (_A_<sub>1</sub>_,...,A<sub>k</sub>_) based on the order of symbols _A<sub>i</sub>_ within each grammar **G**_<sub>i</sub>_.

If each _A<sub>i</sub>_ is a terminal of **G**_<sub>i</sub>_, then _F<sub>i</sub>_=exp(_A<sub>i</sub>_)=_A<sub>i</sub>_ holds for each _i_, and we set _A_**<sub>F</sub>**=(_A_<sub>1</sub>_,...,A<sub>k</sub>_) to be a terminal of **G**. Otherwise, we set _A_**<sub>F</sub>** to be a non-terminal, and we need to specify rhs(_A_**<sub>F</sub>**). For<tbc>

