## A Sum-Order-Preserving Hashing

In this section, we recap the concept of sum-order-preserving hashing, provide a proof of Theorem 1.11, and further discuss the plausibility of Hypothesis 1.12. Recall that a function \(h:X\rightarrow\mathbb{Z}\) (for some integer set _X_) is _sum-order-preserving_ if for all \(x_1,x_2,y_1,y_2\in X\):<tbc>

<tbc>Analogously, we call _h order-preserving_ if for all \(x,y\in X\):

\(x<y\text{implies}h(x)<h(y).\)

### A.1 Quasi-Polynomial Bounds

We will first focus on the proof of Theorem 1.11 (restated next) which claims that for any integer set _X_ with doubling _K_ there exists a large fraction, depending _quasi-polynomially_ on _K_, that can be hashed with a sum-order-preserving hash function.

**Theorem 1.11** (Sum-Order-Preserving Hashing with Quasi-Polynomial Bounds [11, 87])**.** _For every integer set X with doubling_ \(|X+X|\le K|X|\) _there is a subset_ \(Y\subseteq X\) _of size_ \(|Y|\ge|X|/\mathrm{exp}((\mathrm{log}K)^{O(1)})\) _and a sum-order-preserving function_ \(h:Y\rightarrow\{0,\dots,|X|\}\).

