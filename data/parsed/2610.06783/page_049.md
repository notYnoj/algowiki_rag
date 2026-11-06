**Corollary 31.** _Let c\>_10 _and_ \(0<\theta<0.9\)_, let_ \(\rho_c:=9/(c-1)\)_, and let_

\(\gamma:=\frac{\theta ln(1/\rho_c)}{ln4}>0\text{\textit{and}}q:=\frac{\mathrm{H}(\theta)+\theta ln9}{ln4}.\)

_Given as input matrices_ \(X\in\mathbb{Z}^{N\times D}\) _and_ \(Y\in\mathbb{Z}^{D\times N}\) _whose entries are integers of absolute value at most N_<sup>_O_(1)</sup>_, where_ \(2\le D\le N^\varepsilon\) _and_ \(\varepsilon<R_c(\gamma)\)_, with R<sub>c</sub> as in_ (11)_, we can preprocess them deterministically in_ \(O(N^2\mathrm{log}^2D/D^\gamma)\) _time and space, after which any single entry_ (_XY_)\[_I,J_\] _can be computed deterministically in O(D<sup>q</sup>_log_D_) _time. The constants hidden in the_ \(O(\cdot)\) _depend on c,_ \(\theta\)_, and_ \(\varepsilon\).

_Moreover, R<sub>c</sub>_(0) _increases to_ \(\varepsilon^*=\mathrm{ln}4/(5\mathrm{ln}10)=0.1204\dots\) _as c decreases to_ 10.

_Proof._ We repeat the proof of Corollary 26 with \(L:=\lceil cm\rceil\) and \(t:=\lceil\theta m\rceil\). After the padding, the assumption \(D\le N^\varepsilon\) now reads \(N\ge 4^{(m-1)/\varepsilon}\). For the boxes, \(\rho<\rho_c\) gives \(\rho^t\le\rho_c^{\theta m}=D^{-\gamma}\). For the queries, the same calculation with \(x:=(1-\theta)/\theta\) in place of 8, where 9_x\>_1 because \(\theta<0.9\), gives \(\sum_{d\le t}\alpha_d\le(9x)^t(1+1/x)^m=O(D^q)\). For the encodings, the same bound on the binomial coefficient, \(\genfrac(){pt}{2}{n}{k}\ge e^{n\mathrm{H}(k/n)}/(n+1)\), shows that the left-hand side of (10) is \(O(\sqrt{m}\cdot\Lambda^m)\). As \(\varepsilon<R_c(\gamma)\) says that \(\Lambda<4^{1/\varepsilon}\), the inequality (10) thus holds once _m_ exceeds a constant depending on _c_, \(\theta\), and \(\varepsilon\), and for smaller _m_ the corollary again holds trivially.

Finally, a direct calculation shows that for \(\gamma=0\), \(\mathrm{ln}\Lambda\) increases with _c_ and tends to 5ln10 as _c_ decreases to 10, by the identity \(\mathrm{H}(\frac{1}{10})+\frac{9}{10}\mathrm{ln}9=\mathrm{ln}10\). Hence _R<sub>c</sub>_(0) increases to \(\mathrm{ln}4/(5\mathrm{ln}10)=\varepsilon^*\).

## Where \(\varepsilon^*\) comes from.

The identity \(\mathrm{H}(\frac{1}{10})+\frac{9}{10}\mathrm{ln}9=\mathrm{ln}10\) says that \(\genfrac(){pt}{2}{10m}{m}9^{9m}\), the largest term of the binomial expansion of (1+9)<sup>10_m_</sup>, is 10<sup>10_m_</sup> up to polynomial factors. So at _c_=10 a tile has _M_≈10_<sup>L</sup>_ output entries, as many as the recursion has leaves, and the encodings cost \(N\cdot 10^L/\sqrt{M}\approx N\cdot 10^{L/2}\), which is below _N_<sup>2</sup> exactly when \(N\ge 10^{L/2}=D^{1/\varepsilon^*}\).

_Proof of Theorem 24._ Let \(\varepsilon<\varepsilon^*\) and _q\>_0. Choose _c\>_10 with \(R_c(0)>\varepsilon\) (Corollary 31), and then \(\theta\in(0,0.9)\) small enough that \((\mathrm{H}(\theta)+\theta\mathrm{ln}9)/\mathrm{ln}4<q\) and \(R_c(\theta\mathrm{ln}(1/\rho_c)/\mathrm{ln}4)>\varepsilon\). This is possible since, as \(\theta\rightarrow 0\), the first expression tends to 0 and the second to _R<sub>c</sub>_(0). Corollary 31 with these _c_ and \(\theta\) gives the theorem.

_Proof of Theorem 25._ Apply Theorem 24 with \(q:=\kappa/2\), and ask one query for each position of _W_. As \(|W|\le N^2/D^\kappa\), this takes \(O(N^2\mathrm{log}^2D/D^\gamma+|W|D^{\kappa/2}\mathrm{log}D)=O(N^2\mathrm{log}^2D/D^{\gamma^\prime})\) time, where \(\gamma':=\mathrm{min}\{\gamma,\kappa/2\}\).

With Corollary 31 in place of Theorem 24, the same argument gives explicit exponents, which we use for the right half of  2, with the \(\theta\) at which \(\gamma=\kappa-q\). The \(\varepsilon\) of a row of the table is the smallest \(R_c(\gamma)\) over its entries.

**Corollary 32.** _Let c,_ \(\theta\), \(\gamma\)_, q, X, Y , D, and_ \(\varepsilon\) _be as in Corollary 31, and let_ \(\kappa>0\)_. For every set W of at most_ \(N^2/D^\kappa\) _positions of an_ \(N\times N\) _matrix, the entries_ (_XY_)\[_I,J_\], \((I,J)\in W\)_, can be computed deterministically in time_

\(O\big(N^2\mathrm{log}^2D\left(D^{-\gamma}+D^{q-\kappa}\right)\big),\)

_a saving of_ \(D^{\mathrm{min}\{\gamma,\kappa-q\}}\)_, up to logarithmic factors, over the size N_<sup>2</sup> _of the product._

