Theorem 2.2 implies that we can remove more than one nilpotent term from an exact decomposition provided they can be made \(O(\varepsilon)\) for the same (symbolic) basis transformations. Despite this, Theorem 2.1 only provides a criterion for removing one term at a time, which is ultimately limited by the fact that, even if we have two terms that correspond to nilpotent products, a set of transformations that makes one \(O(\varepsilon)\) may not necessarily make the other \(O(\varepsilon)\) as well. Hence, we need other tools for identifying when more than one term is removable The following proposition gives an easy necessary condition.

**Proposition 2.3.** _If R_<sup>-1</sup>_U<sub>j</sub>S, S_<sup>-1</sup>_V<sub>j</sub>T, and T_<sup>-1</sup>_W<sub>j</sub>R have entries in_ \(\varepsilon\mathbb{C}[\varepsilon]\) _for all_ \(1\le j\le l\) _and R, S, and T as in Theorem 2.2, then_

\(\mathrm{Trace}(U_{j_1^u}V_{j_1^v}W_{j_1^w}\cdots U_{j_p^u}V_{j_p^v}W_{j_p^w})=0\)

_for all sequences of indices_ \(j_1^u,j_1^v,j_1^w,\dots,j_p^u,j_p^v,j_p^w\le l\) _with_ \(p\ge 1\).

_Proof._ Since trace is basis invariant, all expressions of the form \(\mathrm{Trace}(U_{j_1^u}V_{j_1^v}W_{j_1^w}\dots U_{j_p^u}V_{j_p^v}W_{j_p^w})\) are invariant under De-Groote transformations. By assumption, we have a De-Groote transformation under which the given expression is a polynomial in \(\varepsilon\) with zero constant term. But the original expression does not depend on \(\varepsilon\), so it follows that it must be zero.

Importantly, this necessary condition is also a sufficient one. Moreover, we do not need to check arbitrary products of the _U<sub>j</sub>V<sub>j</sub>W<sub>j</sub>_ (which of course is not possible in practice). This follows from classical results in invariant theory, namely Hilbert’s basis theorem and Hilbert-Mumford, though an effective bound for _p_ is given by Le Bruyn and Procesi \[45, Theorem 1\]. In the literature, this theorem is usually stated in the language of quivers, which we reformulate in our context.<sup>7</sup>

**Theorem 2.4.** _Suppose that_ \(\mathrm{Trace}(U_{j_1^u}V_{j_1^v}W_{j_1^w}\cdots U_{j_p^u}V_{j_p^v}W_{j_p^w})=0\) _for all sequences of indices_ \(j_1^u,j_1^v,j_1^w,\dots\dots,j_p^u,j_p^v,j_p^w\le l\) _with_ \(p\le(m+k+n)^2\)_. Then there exist_ \(R\in\mathbb{C}(\varepsilon)^{m\times m}\), \(S\in\mathbb{C}(\varepsilon)^{k\times k}\)_, and_ \(T\in\mathbb{C}(\varepsilon)^{n\times n}\)_, each invertible over_ \(\mathbb{C}(\varepsilon)\)_, such that R_<sup>-1</sup>_U<sub>j</sub>S, S_<sup>-1</sup>_V<sub>j</sub>T, and T_<sup>-1</sup>_W<sub>j</sub>R have entries in_ \(\varepsilon\mathbb{C}[\varepsilon]\) _for all_ \(1\le j\le l\).

Unfortunately, unlike Theorem 2.1, the proof of this result is not constructive, meaning we cannot use it to find _R_, _S_, and _T_ algorithmically. As a result, it is typically easier to remove one term at a time. Possible generalizations capable of eliminating multiple terms simultaneously are discussed in Section 2.3.

## 2.1.1 \(\langle 2,2,3\rangle\) Example

To see our high-level approach in action, consider an exact \(\langle 2,2,3;11\rangle\) algorithm represented by the tensor decomposition

\(\mathcal{M}_{\langle 2,2,3\rangle}=\left(\begin{array}{ c c }
1 & 1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 1 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
1 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 & -1 \\
0 & 0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 1 \\
0 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
1 & -1 \\
0 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
-1 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 & -1 \\
0 & -1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
1 & 1 \\
0 & 1
\end{array}\right)+\left(\begin{array}{ c c }
1 & -1 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
1 & 0 & 0 \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
-1 & 0 \\
0 & 0 \\
0 & 1
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 & -1 \\
1 & -1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
0 & 0 \\
0 & 1
\end{array}\right)+\left(\begin{array}{ c c }
0 & 0 \\
1 & -1 & -1 \\
0 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 \\
0 & -1 \\
0 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 & 0 \\
0 & -1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
0 & -1 \\
0 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & -1 \\
-1 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
1 & 0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
0 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 & 0 \\
0 & -1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1 \\
0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
0 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 1 & 0 \\
0 & -1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
0 & -1 \\
0 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & -1 \\
-1 & 1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
0 & -1
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
0 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
-1 & -1 \\
0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
0 & 0 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & -1 \\
-1 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 0 \\
-1 & -1 \\
0 & 0
\end{array}\right)+\left(\begin{array}{ c c }
1 & 0 \\
-1 & 0
\end{array}\right)\otimes\left(\begin{array}{ c c }
0 & 0 \\
0 & 0 \\
0 & -1
\end{array}\right)\otimes\left(\begin{array}{ c c }
1 & 1 \\
-1 & -1 \\
1 & 1
\end{array}\right).\text{(2.3)}\)

<sup>7</sup>The relevant quiver for a rank _r_ exact decomposition of \(\mathcal{M}_{\langle m,k,n\rangle}\) is a three-vertex directed cycle with _r_ copies of each arrow. We construct a representation of this quiver by assigning C_<sup>m</sup>,_C_<sup>k</sup>,_C_<sup>n</sup>_ to the vertices and _U<sub>j</sub>,V<sub>j</sub>,W<sub>j</sub>_ to the arrows.

