## B Pseudocodes

In this section we provide pseudocode for our algorithms.

### B.1 New Basic Tools

We start by providing the pseudocodes for the basic tools that are required to design our main algorithm for approximating the LCS of the input strings.

#### B.1.1 Basic Approximation Algorithm

**Algorithm 5** \[Lemma 3\] Basic Approximation Algorithm: Query \((x,y,\beta)\)

**Require:** String _x_ and preprocessed string _y_ of length _n_; parameter \(\beta\ge 1\)

**Ensure:** Computes subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\widetilde{L}>\frac{L}{\beta}-1\) w.h.p.

1: \(x'\leftarrow\) an empty string

2: **if** \(\beta\ge\frac{1}{8clogn}\) **then**

3: \(\widetilde{L}\leftarrow\) compute _LCS(x,y_) using the query phase of Theorem 2

4: **else**

5: \(p\leftarrow\frac{8clogn}{\beta}\)

6: \(q\leftarrow Geo(p)\)

7: **while** \(q\le n\) **do**

8: append _x_\[_q_\] to \(x'\)

9: \(q\leftarrow q+Geo(p)\)

10: \(\widetilde{L}\leftarrow\) compute \(LCS(x',y)\) using the query phase of Theorem 2

11: **return** \(\widetilde{L}\)

The function _Geo(p_) samples a geometric random variable from {1,2,3_,..._} in constant time, see e.g. \[18\].

**Algorithm 6** \[Lemma 4\] Generalised Basic Approximation Algorithm: Query \((x,y,\beta)\)

**Require:** String _x_ and preprocessed string _y_ of length _n_; parameter \(\beta\ge 1\)

**Ensure:** Comutes subsequence \(\widetilde{L}\) of _x,y_ satisfying \(\widetilde{L}\ge\frac{L}{\beta}\) w.h.p.

1: \(\widetilde{L}\leftarrow Query(x,y,\beta)\) of Algorithm 5

2: \(M\leftarrow\) result of Algorithm 8 on (_x,y_)

3: **if** _M\>_0 **then**

4: \(\widetilde{L}\leftarrow max\{\widetilde{L},1\}\)

5: **return** \(\widetilde{L}\)

**Algorithm 7** \[Lemma 5\] Basic Decision Algorithm: Query \((x,y,\ell)\)

**Require:** String _x_ and preprocessed string _y_ of length _n_; parameter \(1\le\ell\le n\)

**Ensure:** Decides whether \(L\ge\ell\) w.h.p.

1: **for** \(\beta=n,n/2,\dots,1\) **do**

2: \(\widetilde{L}\leftarrow Query(x,y,\beta)\) of Algorithm 5

3: **if** \(\widetilde{L}\le\ell/\beta-1\) **then**

4: **return** 0

5: **if** \(\widetilde{L}\ge\ell\) **then**

6: **return** 1

