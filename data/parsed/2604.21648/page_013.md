<tbc>Lemma 3.11. _Let_ \(V=\left[v_1\cdots v_n\right]\) _be the B-unitary eigenvectors of_ \(\widehat{M}^{-1}B\)_. Consider the following statements:_

_(1)_ \(\mathcal{R}(P)=\mathcal{R}(\left[v_1\cdots v_{n_c}\right])\)_.

_(2)_ \(\mathcal{N}(R^HA)=\mathcal{R}(\left[v_{n_c+1}\cdots v_n\right])\)_.

_(3)_ \(\Pi_A(P,R)\) _is B-orthogonal._

_Any two of the three conditions imply the third statement._

_Proof. (1)_ \(\wedge\) _(2)_ \(\Rightarrow\) _(3):_ Assume that _(1)_ and _(2)_ hold, that is \(P=V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\) for some nonsingular \(Z\in\mathbb{C}^{n_c\times n_c}\) and \(R^HAV\left[\begin{array}{ c }
I_{n_f} \\
0
\end{array}\right]S=0\) for all nonsingular \(S\in\mathbb{C}^{n_c\times n_c}\). It holds

\(\Pi_A(P,R)=P(R^HAP)^{-1}R^HA=V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\left(R^HAV\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]Z\right)^{-1}R^HAVV^{-1}=V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\left(R^HAV\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\right)^{-1}\left[R^HAV\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]0\right]V^{-1}=V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]\left[I_{n_c}0\right]V^{-1}=V\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]V^{-1}.\text{(3.16)}\)

Since _V_ is _B_-unitary, it holds _V<sup>H</sup>BV=I<sub>n</sub>_ and thus _B=V_<sup>-_H_</sup>_V_<sup>-1</sup>. Hence, we get

\(\Pi_A(P,R)^+=B^{-1}\Pi_A(P,R)^HB=VV^HV^{-H}\left[\begin{array}{ c c }
I_{n_c} & 0 \\
0 & 0
\end{array}\right]V^HV^{-H}V^{-1}=\Pi_A(P,R)\)

and \(\Pi_A(P,R)\) is _B_-orthogonal.

_(1)_ \(\wedge\) _(3)_ \(\Rightarrow\) _(2):_ Assume that _(1)_ and _(3)_ are true. By Lemma 3.1 it holds<tbc>

\(\mathcal{N}(R^HA)=\mathcal{N}(P^HB)=\mathcal{N}(\left[I_{n_c}0\right]V^HB).\)

<tbc>Writing any \(x\in\mathbb{C}^n\) as \(x=\sum_{i=1}^n\alpha_iv_i\) with coefficients \(\alpha_i\in\mathbb{C}\), we obtain<tbc>

\(\left[I_{n_c}0\right]V^HBx=\left[I_{n_c}0\right]\sum_{i=1}^n\alpha_iV^HBv_i=\left[I_{n_c}0\right]\sum_{i=1}^n\alpha_ie_i=\left[\begin{array}{ c }
\alpha_1 \\
\vdots \\
\alpha_{n_c} \\
0
\end{array}\right].\)

<tbc>Thus \(x\in\mathcal{N}(\left[I_{n_c}0\right]V^HB)\) if and only if \(\alpha_1=\cdots=\alpha_{n_c}=0\) and hence<tbc>

\(\mathcal{N}(R^HA)=\mathcal{N}(\left[I_{n_c}0\right]V^HB)=\mathcal{R}(\left[v_{n_c+1}\cdots v_n\right]).\)

<tbc>_(2)_ \(\wedge\) _(3)_ \(\Rightarrow\) _(1):_ Assume that _(2)_ and _(3)_ are true. By Lemma 3.1 it holds<tbc>

\(\mathcal{N}(P^HB)=\mathcal{N}(R^HA)=\mathcal{R}(\left[v_{n_c+1}\cdots v_n\right]).\)

<tbc>Since _V_ is nonsingular we can write _P=VS_ for some matrix \(S=\left[\begin{array}{ c }
S_{n_c} \\
\tilde{S}
\end{array}\right]\in\mathbb{C}^{n\times n_c}\) with full rank _n<sub>c</sub>_ where \(S_{n_c}\in\mathbb{C}^{n_c\times n_c}\) and \(\tilde{S}\in\mathbb{C}^{n_f\times n_c}\). Then we get<tbc>

\(0=P^HB\left[v_{n_c+1}\cdots v_n\right]=S^HV^HBV\left[\begin{array}{ c }
0 \\
I_{n_f}
\end{array}\right]=\left[S_{n_c}^H\tilde{S}^H\right]\left[\begin{array}{ c }
0 \\
I_{n_f}
\end{array}\right]=\tilde{S}^H.\)

<tbc>Therefore, _S<sub>n<sub>c</sub></sub>_ must be nonsingular and

\(\mathcal{R}(P)=\mathcal{R}(VS)=\mathcal{R}(V\left[\begin{array}{ c }
I_{n_c} \\
0
\end{array}\right]S_{n_c})=\mathcal{R}(\left[v_1\cdots v_{n_c}\right]).\sqcap\sqcup\)

