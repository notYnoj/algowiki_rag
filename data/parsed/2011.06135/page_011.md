<tbc>_Proof._ Define functions _f_ and _g_ as<tbc>

\(f(x)=\left\{\begin{array}{ c c }
0 & \text{if}x=0 \\
\frac{2}{3} & \text{if}x=1 \\
g(x)=\left\{\begin{array}{ c c }
\frac{1}{3} & \text{if}x=0 \\
1 & \text{if}x=1
\end{array}\right.\)

<tbc>For a set \(S\subset[d]\), consider its corresponding vector \(\chi_S\in\{0,1\}^d\) where \(\chi_{S,j}=1\) iff \(j\in S\). Let \(F:\{0,1\}^d\rightarrow\{0,1\}^d\) and \(G:\{0,1\}^d\rightarrow\{0,1\}^d\) be defined as

\(F(T)=(f(\chi_{T,1}),\dots,f(\chi_{T,d}))\)<br>
\(G(S)=(g(\chi_{S,1}),\dots,g(\chi_{S,d})).\)

Define \(D(S,T):=\left\|G(S)-F(T)\right\|_\infty\). If \(T\subseteq S\), then \(D(S,T)=\frac{1}{3}\), and _D(S,T_)=1 otherwise. Then, an instance of Bichromatic Subset Query, \(S_1,\dots,S_N\subset[d]\) and \(T_1,\dots,T_N\subset[d]\), can be reduced to a \(\gamma\)-approximate Bichromatic Closest Pair instance with _G(S_<sub>1</sub>)_,...,G(S<sub>N</sub>_) and _F(T_<sub>1</sub>)_,...,F(T<sub>N</sub>_) for \(\gamma<3\). If there exists a pair _G(S<sub>i</sub>),F(T<sub>j</sub>_) with \(D(S_i,T_j)\le 1/3\) , then \(T_j\subseteq S_i\). If no such pair exists, we know that for any \(i,j\in[N]\), \(T_j\unknown\subset S_i\).

Combining Lemma 3.1, Lemma 3.7 and Theorem 2.12, we get the following theorem.

**Theorem 3.8.** _Assuming SETH, for any_ \(\delta>0\)_, C\>_1_, and_ \(\gamma<3\)_, there exists_ \(c=c(\delta,C)\) _such that_ \(\gamma\)_-ANN under the_ \(\ell_\infty\) _norm cannot be solved with N<sup>C</sup> preprocessing and_ \(N^{1-\delta}\) _query time on instances with d=c_log_N._

_Proof._ Suppose there exists some \(\delta>0,C>1\), and \(\gamma<3\) such that there is an algorithm for \(\gamma\)-ANN under the \(\ell_\infty\) norm with _N<sup>C</sup>_ preprocessing time and \(N^{1-\delta}\) query time for all _d=O_(log_N_). Then, by Lemma 3.1, there is a \(N^{2-\delta^\prime}\)-time algorithm for \(\gamma\)-approximate Bichromatic Closest Pair under \(\ell_\infty\) with \(\delta'=\Omega\left(\frac{\delta}{C-1}\right)\) that works for all _d=O_(log_N_). By Lemma 3.7, such an algorithm for Bichromatic Closest Pair implies a \(O(N^{2-\delta^\prime})\)-time algorithm for Bichromatic Subset Query applying to all _d=O_(log_N_). Such an algorithm for Bichromatic Subset Query cannot exist unless SETH is false (Theorem 2.12).

## 3.4 Limitation of OV-based Hardness for ANN

We show that the hard approximation factor of 3 in Theorem 3.8 is, in a certain sense, tight. More precisely, we show that any "natural" reduction from Orthogonal Vectors (which is how most SETH-based hardness results are obtained) to \(\gamma\)-ANN under any metric cannot show hardness for \(\gamma>3\) due to the triangle inequality. This in turn implies that any improvement to Theorem 3.8 in terms of the approximation factor would require novel techniques for proving SETH-based hardness results. This is formalized in Theorem 3.9.

**Theorem 3.9.** _Let d\>_0 _be a positive integer and_ (M_,D_) _be a metric space. Let_ \(F:\{0,1\}^d\rightarrow\mathcal{M}\) _and_ \(G:\{0,1\}^d\rightarrow\mathcal{M}\) _be embeddings such that for any two strings_ \(S,T\in\{0,1\}^d\),

• _If_ \(\mathsf{DISJ}(S,T)=1\)_, then_ \(D(F(S),G(T))\le r\).<tbc>

• _If_ \(\mathsf{DISJ}(S,T)=0\)_, then_ \(D(F(S),G(T))\ge\gamma r\).

_Then, it must be the case that_ \(\gamma\le 3\).

