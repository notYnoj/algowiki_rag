**Lemma 2.3** (Strassen \[Str87, Proposition 6.2\])**.** _Let U, V_<sub>1</sub>_, V_<sub>2</sub>_, W_<sub>1</sub> _and W_<sub>2</sub> _be vector spaces. Write_ \(T\in U\otimes(V_1\oplus V_2)\otimes(W_1\oplus W_2)\) _as T=T_<sub>1,1</sub>+_T_<sub>1,2</sub>+_T_<sub>2,1</sub>+_T_<sub>2,2</sub> _with_ \(T_{i,j}\in U\otimes V_i\otimes W_j\)_. If T_<sub>2,1</sub>=0_, then_ \(T\unknown_1T_{1,1}\oplus_1T_{2,2}\)_. In block form, with T<sub>i,j</sub> in row i and column j, this reads_

\(\left(\begin{array}{ c c }
T_{1,1} & T_{1,2} \\
0 & T_{2,2}
\end{array}\right)\unknown_1\left(\begin{array}{ c c }
T_{1,1} & 0 \\
0 & T_{2,2}
\end{array}\right).\)

_Proof._ Let \(B(\varepsilon)=\varepsilon I_{V_1}\oplus I_{V_2}\) and \(C(\varepsilon)=I_{W_1}\oplus\varepsilon I_{W_2}\). Then \((I\otimes B(\varepsilon)\otimes C(\varepsilon))T=\varepsilon(T_{1,1}+T_{2,2})+\varepsilon^2T_{1,2}+T_{2,1}\), which is \(\varepsilon(T_{1,1}+T_{2,2})+\varepsilon^2T_{1,2}\) since _T_<sub>2,1</sub>=0.

Figure 3 draws Lemma 2.3 in three dimensions. Strassen applied the general version, for filtrations, to show that every _n_-dimensional algebra with unit degenerates to the null algebra, in which _u<sub>i</sub>u<sub>n</sub>=u<sub>n</sub>u<sub>i</sub>=u<sub>i</sub>_ and _u<sub>i</sub>u<sub>j</sub>_=0 for _i,j\<n_, and that \(\langle\lfloor(h+1)^2/4\rfloor\rangle\unknown D_h\unknown\langle h,h,h\rangle\) for the algebra _D<sub>h</sub>_ of upper triangular \(h\times h\) matrices \[Str87, Section 6\].

Since the decompositions \(V_1\oplus V_2\) and \(W_1\oplus W_2\) are arbitrary, Lemma 2.3 also applies to a tensor with more blocks that has this block form after its block rows and block columns are permuted and grouped. We will use this for three blocks.

**Lemma 2.4.** _Let U, V_<sub>1</sub>_, V_<sub>2</sub>_, V_<sub>3</sub>_, W_<sub>1</sub>_, W_<sub>2</sub> _and W_<sub>3</sub> _be vector spaces. Write_ \(T\in U\otimes(V_1\oplus V_2\oplus V_3)\otimes(W_1\oplus W_2\oplus W_3)\) _as_ \(T=\sum_{i,j=1}^3T_{i,j}\) _with_ \(T_{i,j}\in U\otimes V_i\otimes W_j\)_. If T<sub>i,j</sub>_=0 _for all distinct_ \(i,j\in[3]\) _with_ \(i\neq 2\)_, then_ \(T\unknown_1T_{1,1}\oplus_1T_{2,2}\oplus_1T_{3,3}\)_. In block form, with T<sub>i,j</sub> in row i and column j, this reads_<tbc>

\(\left(\begin{array}{ c c c }
T_{1,1} & 0 & 0 \\
T_{2,1} & T_{2,2} & T_{2,3} \\
0 & 0 & T_{3,3}
\end{array}\right)\unknown_1\left(\begin{array}{ c c c }
T_{1,1} & 0 & 0 \\
0 & T_{2,2} & 0 \\
0 & 0 & T_{3,3}
\end{array}\right).\)

<tbc>_Proof._ Apply Lemma 2.3 to the decompositions \(V_2\oplus(V_1\oplus V_3)\) of the second leg and \(W_2\oplus(W_1\oplus W_3)\) of the third leg; this moves the middle block row and block column to the front and groups the other two. The component of _T_ in \(U\otimes(V_1\oplus V_3)\otimes W_2\) is _T_<sub>1,2</sub>+_T_<sub>3,2</sub>=0. So the lemma gives \(T\unknown_1T_{2,2}\oplus_1(T_{1,1}+T_{1,3}+T_{3,1}+T_{3,3})\), which is \(T_{1,1}\oplus_1T_{2,2}\oplus_1T_{3,3}\) since _T_<sub>1,3</sub>=_T_<sub>3,1</sub>=0.

The following lemma states Lemma 2.3 in the language of bilinear maps and quotients.

**Lemma 2.5** (Strassen \[Str87, Proposition 6.2\])**.** _Let_ \(\mu:U\times V\rightarrow W\) _be a bilinear map, and let_ \(V_1\subseteq V\) _and_ \(W_1\subseteq W\) _be subspaces with_ \(\mu(U\times V_1)\subseteq W_1\)_. Let_ \(\mu_1\) _be the induced map of_ \(\mu\) _on the quotients,_<tbc>

\(\mu_1:U\times(V/V_1)\rightarrow W/W_1,\)

W1
W2
U
V1
T1,1
T1,2
T1,1
V2
T2,2
T
T1,1
T2,2

Figure 3: Lemma 2.3, with the tensors drawn as three-dimensional arrays: the first leg _U_ points into the page, the second leg \(V_1\oplus V_2\) downwards and the third leg \(W_1\oplus W_2\) to the right. The coefficients of _T<sub>i,j</sub>_ lie in the box in block row _i_ and block column _j_, and all other coefficients are zero. The tensor _T_ (left) has no box in block row 2 and block column 1, and degenerates on the second and third legs to the sum _T_<sub>1,1</sub>+_T_<sub>2,2</sub> of its diagonal blocks (right).

