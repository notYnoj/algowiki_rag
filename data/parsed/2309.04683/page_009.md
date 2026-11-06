and its connections with 2D LWS. Sections 5 and 6 respectively discuss applications of kD LWS and 2D LWS<sup>PT</sup> to various real-world problems.

## 2 Preliminaries

In this section, we state our core problems and relevant problems in fine-grained complexity. We also state our notations for convenience.

For a problem _P_, we say that it is truly sub-quadratic (or sub-cubic) if there exists an algorithm for it with running time \(O(n^{2-\varepsilon})\) (or \(O(n^{3-\varepsilon})\)) for any \(\varepsilon>0\). We say that _P_ and _Q_ are sub-quadratic (sub-cubic) equivalent if _P_ is truly sub-quadratic (sub-cubic) if and only if _Q_ is truly sub-quadratic (sub-cubic).

For a positive integer _n_, we let \[_n_\]={1_,...,n_}. We assume the word-RAM model with word size \(\Theta(logn)\) throughout this paper, and assume that all integer inputs are chosen from \(\{-W,\dots,W,\infty\}\) where _W_ fits in a constant number of words. We usually use _d_ to denote the length of vectors (rank of a tensor) in our problems, _k_ to denote the dimension of our problems, and _n_ to denote the input size. We put these parameters as subscripts of problems. Since we will discuss both rank and slice rank, we make it clear which we are talking about in the discussions. In this paper, "kD LWS has (slice) rank _d_" means the array _w_ has (slice) rank _d_.

For a _k_-dimensional dynamic programming array _T_ with entries _T_\[_i_<sub>1</sub>_,i_<sub>2</sub>_,...,i<sub>k</sub>_\], we let \(I_\ell\) denote the sum of all _i<sub>k</sub>_’s except \(i_\ell\). Let _D<sub>a,b</sub>_ denote the set of all \((i_1,\dots,i_k)\) such that \(a\le i_1+\dots+i_k<b\).

### 2.1 Strong Exponential Time Hypothesis and Min-IP

We state some important problems and definitions in fine-grained complexity that we will refer to later.

**Conjecture 2.1** (Strong Exponential Time Hypothesis (SETH))**.** _For every_ \(\varepsilon>0\)_, there exists a positive integer k such that_ kSAT _requires time_ \(\Omega(2^{(1-\varepsilon)n})\).

SETH is well-known for being a stronger version of \(\mathsf{P}\neq\mathsf{NP}\), i.e. it implies \(\mathsf{P}\neq\mathsf{NP}\).

**Definition 2.2** (OV_<sub>n,d</sub>_)**.** _Given two sets of vectors A_={_a_<sub>1</sub>_,...,a<sub>n</sub>},B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_} _such that_ \(a_i,b_j\in\{0,1\}^d\) _for all i,j, the_ Orthogonal Vectors _problem_ (OV_<sub>n,d</sub>_) _asks to determine whether there exists_ \(1\le i,j\le n\) _such that_ \(\langle a_i,b_j\rangle=0\).

In \[Wil05\], it is shown that assuming SETH, for any positive _c_ there exists \(\varepsilon>0\) such that OV_<sub>n,c</sub>_log_n_ cannot be solved in time \(O(n^{2-\varepsilon})\).

**Definition 2.3** (Min-IP_<sub>n,d</sub>_)**.** _Given two sets of vectors A_={_a_<sub>1</sub>_,...,a<sub>n</sub>},B_={_b_<sub>1</sub>_,...,b<sub>n</sub>_} _such that_ \(a_i,b_j\in\{-W,\dots,W,\infty\}^d\) _for all i,j and a natural number_ \(r\in\mathbb{Z}\)_, the_ Minimal Inner Product (Min-IP_<sub>n,d</sub>_) _asks to determine whether there exists_ \(1\le i,j\le n\) _such that_ \(\langle a_i,b_j\rangle\le r\).

OV_<sub>n,d</sub>_ trivially reduces to Min-IP_<sub>n,d</sub>_, and in fact these two problems are sub-quadratic equivalent \[CW19\]. It is known that this decision version of Min-IP_<sub>n,d</sub>_ is sub-quadratic equivalent to its counting version where it asks to output \(min_{1\le i,j\le n}\langle a_i,b_j\rangle\). We will use the counting version throughout the rest of the paper.

### 2.2 Higher Dimension OV,Min-IP

OV,Min-IP can be naturally generalize to higher dimensions as follows.

**Definition 2.4** (kOV_<sub>n,d</sub>_)**.** _Given k sets of vectors_<tbc>

\(X_1=\{x_{11},\dots,x_{1n}\},\dots,X_k=\{x_{k1},\dots,x_{kn}\}\)

<tbc>_such that_ \(x_{ij}\in\{0,1\}^d\) _for all i,j,_ kOV_<sub>n,d</sub> asks to determine whether there exists_ \(1\le i_1,\dots,i_k\le n\) _such that_<tbc>

\(\langle x_{1,i_1},x_{2,i_2},\dots,x_{k,i_k}\rangle=0.\)

