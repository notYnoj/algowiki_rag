1. _x_ is contained in the local view _X<sub>g</sub>_ of the LRCC (there are four such _g_’s),<tbc>

2. _x_ lies in the selected row or column _r<sub>g,i</sub>_ of _X<sub>g</sub>_ (two choices), and<tbc>

3. _x_ participates in the parity check defined by _h<sub>j</sub>_ (at most seven choices).

Therefore each variable participates in at most \(4\cdot 2\cdot 7=56\) tests.

**Reduce the query complexity.** To reduce the query complexity to 3, we apply the standard gadget reduction from EqLIN2 to E3LIN2. For each \(S_{g,i,j}\in\mathcal{S}_1\), denote its indices by _s_<sub>1</sub>_,...,s<sub>q</sub>_. The corresponding local test is the parity constraint<tbc>

\(x_{s_1}+\cdots+x_{s_q}=0.\) (3)

<tbc>Introduce auxiliary variables _y<sub>g,i,j,k</sub>_ for \(2\le k\le q-2\) and replace Equation (3) with the chain

\(\left\{\begin{array}{ c }
x_{s_1}+x_{s_2}+y_{g,i,j,2}=0, \\
y_{g,i,j,2}+x_{s_3}+y_{g,i,j,3}=0, \\
y_{g,i,j,3}+x_{s_4}+y_{g,i,j,4}=0, \\
\cdots \\
y_{g,i,j,q-3}+x_{s_{q-2}}+y_{g,i,j,q-2}=0, \\
y_{g,i,j,q-2}+x_{s_{q-1}}+x_{s_q}=0.
\end{array}\right.\) (4)

An assignment to \((x_s)_{s\in S_{g,i,j}}\) satisfies Equation (3) if and only if we can extend it to the auxiliary variables so that all constraints in Equation (4) are satisfied. This gadget only blows up the number of tests and the block length by a constant factor, so the rate, distance, detection probability, and variable degree remain constant, while the query complexity drops to 3.

Combining with Theorem 1.1, we immediately get the following.

_Proof of Theorem 1.2._ Let \(\tilde{C}_n\) be the LTCs in Lemma 4.4, whose tests are linear equations. By Lemma 2.5, after a fixed permutation of coordinates we may regard each \(\tilde{C}_n\) as systematic; let _f<sub>n</sub>_ be the corresponding encoders. Then by Definition 3.1, the induced CSP instances of \((\tilde{C}_n,f_n)\) are exactly systems of linear equations on F<sub>2</sub>. Because \((\tilde{C}_n,f_n)\) has query complexity 3, these instances reside in E3LIN2, so \(\mathsf{MaxCSP}_{\tilde{C}_n}\) coincides with Max E3LIN2.

The family \((\tilde{C}_n,f_n)\) inherits constant rate, distance, query complexity, detection probability, and variable degree. Therefore Theorem 1.1 implies that there exists \(\varepsilon>0\) such that every \((1-\varepsilon)\)- approximation algorithm for \(\mathsf{MaxCSP}_{\tilde{C}_n}\) has sensitivity at least

\(\frac{n}{2\theta}\left(\delta\left(1-\frac{p}{p-1}\frac{\varepsilon}{r\kappa}\right)-\frac{2\varepsilon}{\kappa}\right)-\frac{1}{2\theta}=\Omega(n),\)

and the expression in parentheses is positive for sufficiently small \(\varepsilon\) (depending only on the code parameters). Hence the constant hidden in the \(\Omega(\cdot)\) notation depends only on the LTC parameters. This establishes the theorem.

## 4.2 Repetition s and Max Cut

Let _t_ be even, \(A\sqcup B=[t]\) a fixed balanced partition with |_A_|=|_B_|=_t/_2, and \(k\ge 1\). Over the alphabet {0,1} consider the _signed t-fold repetition code_<tbc>

\(\mathrm{Rep}^\pm(k,t)=\left\{y\in\{0,1\}^{tk}:\exists x\in\{0,1\}^k\text{s.t.}y_{a,i}=x_i\forall a\in A,y_{b,i}=1-x_i\forall b\in B,\forall i\in[k]\right\}.\)

