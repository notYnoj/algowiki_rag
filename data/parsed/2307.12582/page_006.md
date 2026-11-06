_Proof Sketch._ We construct an optimal solution **x** through modifying **g**. Specifically, we have **x**=**g**-**x**<sup>-</sup>+**x**<sup>+</sup>, where **x**<sup>-</sup> represents the copies of items in I_<sub>\<b</sub>_ that are deleted from **g**, and **x**<sup>+</sup> represents the copies of items in \(\mathcal{I}_{\unknown b}\) that are added to **g**, while noting that _b_ is the break item. We shall compute two sequences, namely: (i). \(\mathbf{x}^-=\langle x_0^-,\dots,x_{k\cdot U_k}^-\rangle\), where \(x_{t^\prime}^-\) is the minimum total profit of copies in I_<sub>\<b</sub>_ whose total weight is exactly \(t'\); (ii). \(\mathbf{x}^+=\langle x_0^+,\dots,x_{k\cdot U_k}^+\rangle\), where \(x_{t^\prime}^+\) is the maximum total profit of copies in \(\mathcal{I}_{\unknown b}\) whose total weight is exactly \(t'\). The optimal solution can be found easily using these two sequences in _O(kU<sub>k</sub>_) time.

The computation of **_x_**<sup>-</sup> and **_x_**<sup>+</sup> follows the same method as Polak et al. \[26\]: we consider all copies of items whose weight is exactly _w_, and let **_s_**_<sup>w</sup>_ denote the sequence whose \(t'\)-th entry is the maximum total profit of these items when their total weight is exactly \(t'\). After computing all **_s_**_<sup>w</sup>_’s, we iteratively update **_x_**<sup>-</sup> and **_x_**<sup>+</sup> by computing their convolutions with each **_s_**_<sup>w</sup>_. The key point is that we can strategically pick an order of the **_s_**_<sup>w</sup>_’s to perform convolution. In particular, assuming that \(U_1\unknown\dots\unknown U_k\), we have \(\Delta(\mathcal{I}^{W_1\cup\dots\cup W_{k^\prime}})\unknown\sum_{j=1}^{k^\prime} U_j\unknown k'\cdot U_{k^\prime}\) for any \(1\unknown k'\unknown k\). We first convolve **_s_**_<sup>w</sup>_’s in _W_<sub>1</sub>, then _W_<sub>2</sub>, etc. When we compute the convolution with **_s_**_<sup>w</sup>_ where \(w\in W_{k^\prime}\), we can truncate the sequence after the \(k'\cdot U_{k^\prime}\)-th entry, and thus the convolution takes \(O(k'\cdot U_{k^\prime})\) time via SMAWK algorithm \[2\]. It is easy to verify that the total time is \(\widetilde{O}(n+\sum_{j=1}^k|W_j|\cdot j\cdot U_j)=\widetilde{O}(n+k\sum_{j=1}^k|W_j|\cdot U_j)\). \(\square\)

### 2.4 Additive Combinatorics

Additive combinatorics has been a useful tool for Subset Sum. With additive combinatorics tools, Galil and Margalit \[17\] gave a characterization of the regime within which Subset Sum can be solved in linear time. Their result was later improved by Bringmann and Wellnitz \[11\]. Our exchange argument in Section 3 heavily utilizes the dense properties by Bringmann and Wellnitz. We briefly describe these properties in this subsection.

Let _X_ be a multiset of positive integers. We denote the sum of _X_ as \(\Sigma_X\), the maximum element in _X_ as m_<sub>X</sub>_, the maximum multiplicity of elements in _X_ as \(\mu_X\), and the support of _X_ as supp_<sub>X</sub>_. The number of elements in _X_ is denoted by |_X_| (with multiplicities counted). We say _X_ can _hit_ an integer _s_ if some subset of _X_ sums to this integer, i.e., there is a subset \(X'\subseteq X\) that \(\Sigma_{X^\prime}=s\).

Definition 2.1. (Definition 3.1 in \[11\]) _We say that a multiset X is_ \(\delta\)_-dense if it satisfies_ \(|X|^2\unknown\delta\cdot\mu_X\mathfrak{m}_X\).

Definition 2.2. (Definition 3.2 in \[11\]) _Let X be a multiset. We denote by_ \(X(d):=X\cap d\mathbb{Z}\) _the multiset of all numbers in X that are divisible by d. Further, we write X(d_):=_X_\\_X(d_) _to denote the multiset of all numbers in X not divisible by d. We say an integer d\>_1 _is an_ \(\alpha\)_-almost divisor of X if_ \(|\overline{X(d)}|\unknown\alpha\cdot\mu_X\Sigma_X/|X|^2\).

Theorem 2.1. (Theorem 4.2 in \[11\]) _Let X be a multiset of positive integers and set_

\(c_\delta:=1699200\cdot log(2|X|)log^2(2\mu_X),\)<br>
\(c_\alpha:=42480\cdot log(2\mu_X),\)<br>
\(c_\lambda:=169920\cdot log(2\mu_X).\)

_If X is_ \(c_\delta\)_-dense and has no_ \(c_\alpha\)_-almost divisor, then for_ \(\lambda_X:=c_\lambda\mu_X\mathfrak{m}_X\Sigma_X/|X|^2\), _X_ can hit all the integers in range \([\lambda_X,\Sigma_X-\lambda_X]\).

Theorem 2.2. (Theorem 4.1 in \[11\]) _Let X be a multiset of positive integers. Let_ \(\delta,\alpha\) _be functions of n with_ \(\delta\ge 1\) _and_ \(0<\alpha\unknown\delta/16\)_. Given a_ \(\delta\)_-dense set X of size n, there exists an integer_ \(d\ge 1\) _such that_ \(X':=X(d)/d\) _is_ \(\delta\)_-dense and has no_ \(\alpha\)_-almost divisor. Moreover, we have the following additional properties:_

(i) \(d\unknown 4\mu_X\Sigma_X/|X|^2\),<tbc>

(ii) \(|X'|\unknown 0.75|X|\),<tbc>

(iii) \(\Sigma_{X^\prime}\ge 0.75\Sigma_X/d\).

## 3 A General Exchange Argument

In this section, we establish two additive combinatorics results that are crucial to proving our proximity result. Basically we show that given two (multi-)sets _A_ and _B_ of positive integers, if _A_ is dense, and \(\Sigma_B\) is large, there must be some non-empty subset \(A'\) of _A_ and a subset \(B'\) of _B_ such that \(\Sigma_{A^\prime}=\Sigma_{B^\prime}\). We first give a result where multiplicities of integers are not utilized.

