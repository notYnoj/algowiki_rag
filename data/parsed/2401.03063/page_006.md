The equality (1.17) could be of use to find the order of Var_S_ as _n_ tends to infinity. For example, if there is a constant _C\>_1 (independent of _n_) such that \(J'_2(n)\le CJ'_1(n)\), then, taking \(k=\lfloor\frac{n}{2C}\rfloor\) will lead to

\(liminf_{n\rightarrow\infty}\frac{\mathrm{Var}S(n)}{J'_1(n)}\ge\frac{1}{4C}.\)

We have proved that the finite sequence \((B_k)_{1\le k\le n}\) is completely monotone and we already knew from \[2\] that it is non-increasing, so it is natural to wonder if one could find further properties of the _B<sub>k</sub>_’s. On the other hand, one may also wonder whether or not \((K_k)_{1\le k\le n}\) does satisfy any further property except, of course, from being non-negative. Both answers appear to be negative:

**Proposition 1.6.** _For any_ \(a_1,\dots,a_n\ge 0\)_, there exists_ \(S:\mathbb{R}^n\rightarrow\mathbb{R}\) _a Borel function such that for all_ \(k\in\{1,\dots,n\}\)_, K<sub>k</sub>=a<sub>k</sub>._

**Corollary 1.7.** _If_ \((b_k)_{1\le k\le n}\) _is completely monotone, then there exists_ \(S:\mathbb{R}^n\rightarrow\mathbb{R}\) _a Borel function such that for all_ \(k\in\{1,\dots,n\}\)_, B<sub>k</sub>=b<sub>k</sub>._

_Proof of the Corollary._ It is easy to see that \((b_k)_{1\le k\le n}\) is completely monotone if and only if for all \(k\in\{1,\dots,n\}\), \(D^{k-1}b_{n-k+1}\ge 0\). From the statement of the proposition, there exists \(S:\mathbb{R}^n\rightarrow\mathbb{R}\) a Borel function such that for all \(k\in\{1,\dots,n\}\), \(K_k=\frac{n!}{(n-k)!}D^{k-1}b_{n-k+1}\), and, recalling (1.9), since there is no choice for the _B<sub>k</sub>_’s knowing the _K<sub>k</sub>_’s, _B<sub>k</sub>=b<sub>k</sub>_.

_Proof of the proposition._ This follows from using the link with the Hoeffding decomposition observed in \[4\]. Consider for example \(A_1,\dots,A_n\ge 0\) and \(S(X_1,\dots,X_n):=A_1\sum_{1\le i_1<n}(X_{i_1}-\mathbb{E}X_{i_1})+A_2\sum_{1\le i_1<i_2\le n}(X_{i_1}-\mathbb{E}X_{i_1})(X_{i_2}-\mathbb{E}X_{i_2})+\cdots+A_n\sum_{1\le i_1<\cdots<i_n\le n}(X_{i_1}-\mathbb{E}X_{i_1})\dots(X_{i_n}-\mathbb{E}X_{i_n})\). Then, from \[4\],

\(K_k=A_k^2k!\sum_{1\le i_1<\cdots<i_k\le n}\mathrm{Var}\left(X_{i_1}-\mathbb{E}X_{i_1}\right)\dots\left(X_{i_n}-\mathbb{E}X_{i_k}\right)\)<br>
\(=A_k^2k!\sum_{1\le i_1<\cdots<i_k\le n}\mathrm{Var}\left(X_{i_1}\right)\dots\mathrm{Var}\left(X_{i_k}\right),\)

so it is possible to adjust the _A<sub>k</sub>_’s to have the _K<sub>k</sub>_’s as wanted.

One could expect the _J<sub>k</sub>_’s to behave like the _K<sub>k</sub>_’s and to also be able to take any values, but this is unfortunately not the case, for example \(2J_2/n=(n-1)(B_1-B_2)\le nB_1=J_1\).

To conclude this section, we connect the _B<sub>k</sub>_’s and the quantities _T<sub>A</sub>_ introduced in \[5\]. For any subset _A_ of {1_,...,n_}, including \(A=\emptyset\), _T<sub>A</sub>_ is defined as<tbc>

\(T_A=\sum_{j\notin A}\Delta_jS(\Delta_jS)^A,\)

<tbc>and then _T_ is defined as<tbc>

\(T=\sum_{A\unknown\{1,\dots,n\}}\frac{T_A}{2(n-|A|)\genfrac(){pt}{2}{n}{|A|}}.\)

<tbc>It is easy to check that for all \(k\in\{1,\dots,n\}\),

\(B_k=\sum_{A:|A|=k-1}\frac{\mathbb{E}(T_A)}{2(n-|A|)\genfrac(){pt}{2}{n}{|A|}},\)

hence \(\mathbb{E}T=\sum_{k=1}^nB_k=\mathrm{Var}S\) (as expected).

**Remark 1.8.**<tbc>

(_i)_ _One might wonder if the above variance results can be transferred to the_ \(\Phi\)_-entropy. Let_ \(\Phi\) _be a convex function of the real variable such that_ \(\mathbb{E}|\Phi(S)|<+\infty\)_, and let the_ \(\Phi\)_-entropy_ \(H_\Phi\) _of S (e.g., see \[3\]) be defined as:_<tbc>

<tbc>\(H_\Phi(S)=\mathbb{E}\Phi(S)-\Phi(\mathbb{E}S).\)<tbc>

