Variance Bounds: Some Old and Some New

**Abstract**

For functions of independent random variables, various upper and lower variance bounds are revisited in diverse settings. These are then specialized to the Bernoulli, Gaussian, infinitely divisible cases and to Banach space valued random variables. Frameworks and techniques vary from jackknives through semigroups and beyond. Some new applications are presented, in particular, recovering and improving upon all the known estimates on the variance of the length of the longest common subsequences of two random words.

## 1 Introduction and preliminary results

We revisit below various lower and upper bounds on the variance of functions of independent random variables. Throughout and unless otherwise noted, \(X_1,\dots,X_n,X'_1,\dots,X'_n\) are independent random variables such that for all \(k\in\{1,\dots,n\}\), _X<sub>k</sub>_ and \(X'_k\) are identically distributed, while \(S:\mathbb{R}^n\rightarrow\mathbb{R}\) is a Borel function such that \(\mathbb{E}S(X_1,\dots,X_n)^2<+\infty\). Next, and if _S_ is short for _S(X_<sub>1</sub>_,...,X<sub>n</sub>_), for any \(k\in\{1,\dots,n\}\), let \(S^k:=S(X_1,\dots,X_{k-1},X'_k,X_{k+1},\dots,X_n)\) and more generally if \(\alpha\subset\{1,\dots,n\}\), let \(S^\alpha\) be defined as _S(X_<sub>1</sub>_,...,X<sub>n</sub>_) but with _X<sub>k</sub>_ replaced by \(X'_k\) for all \(k\in\alpha\), and so \(S^\emptyset=S\), while \(S^{\{1,\dots,n\}}\) is an independent copy of _S_. With the help of these preliminary notations, we next recall the definitions of various quantities which will play an important role in the sequel.

Following [2], for \(k\in\{1,\dots,n\}\), let

\(B_k:=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}S(S^{i_1,\dots,i_{k-1}}-S^{i_1,\dots,i_k}),\) (1.1)

where S_<sub>n</sub>_ is the symmetric group of degree _n_ and where for _k_=1,\(S^{i_1,\dots,i_{k-1}}=S\). As the following sum is telescopic:

\(\sum_{k=1}^nB_k=\mathbb{E}\frac{1}{n!}\sum_{i\in\mathfrak{S}_n}S(S-S^{i_1,\dots,i_n})=\mathrm{Var}S.\)

One key fact motivating the definition of the _B<sub>k</sub>_’s is that they can be rewritten as:

\(B_k=\mathbb{E}\frac{1}{2n!}\sum_{i\in\mathfrak{S}_n}(S-S^{i_k})(S^{i_1,\dots,i_{k-1}}-S^{i_1,\dots,i_k}).\)

Indeed, if \(\alpha,\beta\subset\{1,\dots,n\}\),

\(\mathbb{E}\left(S^\alpha S^\beta\right)=\mathbb{E}\left(SS^{\alpha\Delta\beta}\right),\) (1.2)

where as usual \(\Delta\) denotes the symmetric difference operator, so

<sup>∗</sup>C.M.A.P. École Polytechnique, Palaiseau, 91120, France & Georgia Institute of Technology, Atlanta, GA, 30332, USA (`clement.deslandes@poytechnique.edu`). <sup>†</sup>School of Mathematics, Georgia Institute of Technology, Atlanta, GA, 30332, USA (`houdre@math.gatech.edu`). <sup>‡</sup>Research supported in part by the awards 524678 and MP-TSM-00002660 from the Simons Foundation. Keywords: Jackknife, Variance Bounds, Poincaré Inequality, Noise Sensitivity, Rademacher Type, Enflo type, Longest Common Subsequences. MSC 2010: 60B20, 60F05.

Clément Deslandes<sup>∗</sup> Christian Houdré<sup>†‡</sup>

October 16, 2024

arXiv:2401.03063v2 [math.PR] 15 Oct 2024

