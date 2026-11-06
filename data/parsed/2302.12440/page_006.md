## 2.1 Basic Notions

**Notation 5.** We use the following notations throughout this paper.

• For \(k\in\mathbb{Z}_{\ge 0}\), let \[_k_\]:={1_,...,k_}.<tbc>

• For two random variables _X,Y_ , let _I(X;Y_) denote the mutual information between _X_ and _Y_ .<tbc>

• For a distribution _P_=(_p_<sub>1</sub>_,...,p<sub>k</sub>_), define its entropy function as \(h(P):=-\sum_{i\in[k]}p_ilogp_i\). Specially, for \(p\in[0,1]\), define _h(p_):=_h(p,_1-_p_). Define _I(p_):=1-_h(p_).<tbc>

• For \(p\in[0,1]\), let Bern(_p_) denote the Bernoulli random variable, such that for _X_∼Bern(_p_), we have P\[_X_=0\]=1-_p_, P\[_X_=1\]=_p_.<tbc>

• For \(p\in[0,1]\), let BSC_<sub>p</sub>_ be the binary symmetric channel with crossover probability _p_, i.e., on input \(x\in\{0,1\}\), the output BSC_<sub>p</sub>(x_) follows distribution Bern(_p_+(1-2_p)x_).<tbc>

• For two random variables _X,Y_ , define \(X\wedge Y:=min\{X,Y\}\).<tbc>

• Let _x_ be a variable and _f(x_) and _g(x_) be two functions which are defined for all large enough values of _x_. We say _f(x_)=_o<sub>x</sub>(g(x_)) if \(lim_{x\rightarrow\infty} f(x)/g(x)=0\). Specially, if _x=n_, we omit the subscript and write _f(n_)=_o(g(n_)).

We also assume some basic knowledge about information theory, such as chain rule of entropy and mutual information and Fano’s inequality. See e.g. \[PW22\] for an overview.

In Noisy Sorting and Noisy Binary Search, the algorithm is allowed to make noisy comparison queries.

**Definition 6** (Noisy Comparison Query)**.** Fix \(p\in(0,\frac{1}{2})\). Let _x,y_ be two comparable elements (i.e., either \(x\le y\) or \(y\le x\)). We define the noisy comparison query NoisyComparison(_x,y_) as returning BSC_<sub>p</sub>_(1{_x\<y_}), where the randomness is independent for every query.

We will omit the crossover probability _p_ when it is clear from the context throughout the paper.

With these definitions, we are ready to define the problems of study.

**Definition 7** (Noisy Sorting Problem)**.** Let NoisySorting(_n_) be the following problem: Given _n_ comparable elements \((a_i)_{i\in[n]}\), an algorithm is allowed to make query NoisyComparison(_a<sub>i</sub>,a<sub>j</sub>_) for \(i,j\in[n]\). The goal is to output a permutation \((b_i)_{i\in[n]}\) of \((a_i)_{i\in[n]}\) such that \(b_i\le b_{i+1}\) for all \(i\in[n-1]\).

**Definition 8** (Noisy Binary Search Problem)**.** Let NoisyBinarySearch(_n_) be the following problem: Given _n_ elements \((a_i)_{i\in[n]}\) satisfying \(a_i\le a_{i+1}\) for all \(i\in[n-1]\) and an element _x_. An algorithm is allowed to make query NoisyComparison(_s,t_), where {_s,t_}={_a<sub>i</sub>,x_} for some \(i\in[n]\). The goal is to output \(max(\{0\}\cup\{i\in[n]:a_i<x\})\) (i.e., the index of the largest element in \((a_i)_{i\in[n]}\) less than _x_).

**Remark 9.** By our definition of the Noisy Sorting Problem, we can WLOG assume that all elements \((a_i)_{i\in[n]}\) are distinct. In fact, suppose we have an algorithm A which works for the distinct elements case. Then we can modify it such that if it is about to call NoisyComparison(_a<sub>i</sub>,a<sub>j</sub>_), it instead calls NoisyComparison(_a_<sub>max{_i,j_}</sub>_,a_<sub>min{_i,j_}</sub>) (but flip the returning bit if _i\<j_). Call the modified<tbc>

