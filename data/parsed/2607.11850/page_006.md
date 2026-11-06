up to lower-order constant factors. Since _K_<sub>max</sub> is fixed and _D_=O(log_n_), this is asymptotically O(log_n_).

Combining this with the fixed auxiliary buffers described earlier, the total auxiliary space usage of the implementation is

\(\mathcal{O}(1)+\mathcal{O}(logn)=\mathcal{O}(logn),\)

where the O(1) term hides the fixed-size helper arrays and fragment buffers. In practical terms, the dominant auxiliary memory cost is the fixed helper storage, while the recursive bucket-offset vectors contribute only a small additional amount proportional to the recursion depth.

## 4.3 Expected Recursion Depth

In this section, we provide intuition for why NFS Sort can perform well on typical inputs. We first prove a simple theorem that relates the expected recursion depth to the density of the input distribution. The theorem is not intended to characterize every implementation detail of the algorithm; rather, it serves as a guide for understanding why recursive bucket refinement can quickly reduce subproblem sizes. We then apply the result to several concrete input distributions.

We will give a simple bound on the expected recursion depth under a bounded input density model. Suppose the input elements

\(X_1,X_2,\dots,X_n\)

are drawn independently from a probability density function _f_ supported on an interval [_a,b_]. Assume that _f_ is bounded, and define

\(M:=(b-a)\|f\|_\infty.\)

The quantity _M_ measures how far the density may deviate from the uniform density on [_a,b_]. For example, if _f_ is uniform on [_a,b_], then _M_=1.

Assume that each recursive distribution step divides the current value interval into _B_ equal-width buckets, and that recursion stops on a branch once the corresponding bucket contains at most _T_ elements.

Theorem 4.2. _Let_

\(M:=(b-a)\|f\|_\infty.\)

_For the branch containing X_<sub>1</sub>_, let D be the first depth d such that the depth-d bucket containing X_<sub>1</sub> _contains at most T sample points. Then_

\(\mathbb{E}[D]\le max\left\{0,\left\lceil log_B\left(\frac{nM}{T}\right)\right\rceil\right\}+\frac{B}{B-1}.\)

_In particular,_

\(\mathbb{E}[D]=\mathcal{O}(logn).\)

Proof. For each depth \(d\ge 0\), let _I<sub>d</sub>(X_<sub>1</sub>) be the unique depth- _d_ bucket that contains _X_<sub>1</sub>. Since each recursive step divides the current interval into _B_ equal-width buckets, the length of a depth-_d_ bucket is

\(|I_d(X_1)|=\frac{b-a}{B^d}.\)

Then define

\(N_d:=\#\{1\le i\le n:X_i\in I_d(X_1)\},\)

the number of sample points lying in the same depth-_d_ bucket as _X_<sub>1</sub>. The stopping depth is therefore

\(D:=min\{d\ge 0:N_d\le T\}.\)

Equivalently,

\(\{D>d\}=\{N_d>T\}.\)

Using the tail-sum formula for nonnegative integer-valued random variables,

\(\mathbb{E}[D]=\sum_{d\ge 0}Pr(D>d)=\sum_{d\ge 0}Pr(N_d>T).\)

We next bound Pr(_N<sub>d</sub>\>T_). Fix _d_, and condition on the value _X_<sub>1</sub>=_x_. Then _I<sub>d</sub>(X_<sub>1</sub>) becomes the deterministic bucket _I<sub>d</sub>(x_) containing _x_. Its probability mass is

\(p_d(x):=Pr(X_j\in I_d(x))=\int_{I_d(x)}f(u)du.\)

Since \(f(u)\le\|f\|_\infty\) for all _u_, we have

\(p_d(x)\le\|f\|_\infty|I_d(x)|=\|f\|_\infty\frac{b-a}{B^d}=\frac{M}{B^d}.\)

Conditioned on _X_<sub>1</sub>=_x_, the remaining random variables _X_<sub>2</sub>_,...,X<sub>n</sub>_ are independent of _X_<sub>1</sub>, and each falls in _I<sub>d</sub>(x_) with probability _p<sub>d</sub>(x_). Therefore

\(N_d|(X_1=x)=^d1+Bin(n-1,p_d(x)).\)

Hence

\(\mathbb{E}[N_d-1|X_1=x]=(n-1)p_d(x)\le\frac{(n-1)M}{B^d}\le\frac{nM}{B^d}.\)

Taking expectation over _X_<sub>1</sub>, we obtain

\(\mathbb{E}[N_d-1]\le\frac{nM}{B^d}.\)

Since _N<sub>d</sub>_ is integer-valued, the event _N<sub>d</sub>\>T_ implies

\(N_d-1\ge T.\)

By Markov’s inequality,

\(Pr(N_d>T)=Pr(N_d-1\ge T)\le\frac{\mathbb{E}[N_d-1]}{T}\le\frac{nM}{TB^d}.\)

Since probabilities are also at most 1,

\(Pr(D>d)=Pr(N_d>T)\le min\left\{1,\frac{nM}{TB^d}\right\}.\)

Let

\(A:=\frac{nM}{T}.\)

Then

\(\mathbb{E}[D]\le\sum_{d\ge 0}min\left\{1,\frac{A}{B^d}\right\}.\)

Choose

\(d_0:=max\left\{0,\left\lceil log_BA\right\rceil\right\}.\)

By definition of _d_<sub>0</sub>, we have \(A\le B^{d_0}\). Therefore, for every \(d\ge d_0\),

\(\frac{A}{B^d}\le B^{d_0-d}\le 1.\)

Splitting the sum at _d_<sub>0</sub>, we get

\(\mathbb{E}[D]\le\sum_{d=0}^{d_0-1}1+\sum_{d=d_0}^\infty\frac{A}{B^d}.\)

