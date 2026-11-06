## A Hunt and Szymanski’s LCS Algorithm

In this section we provide a proof sketch of Theorem 2.

**Theorem 2** (Hunt and Szymanski \[27\])**.** _We can preprocess a string y in time_ \(\widetilde{O}(|y|)\)_. Given a string x and a preprocessed string y, we can compute their LCS in time_ \(\widetilde{O}(|x|+M)\).

_Proof._ Since this algorithm is typically stated as running in time \(\widetilde{O}(n+M)\), here for convenience we sketch the algorithm and show how to split it into preprocessing and query phase.

In the preprocessing phase, given string _y_ we compute the set \(\Sigma(y)\) of symbols occuring in _y_, and for each \(\sigma\in\Sigma(y)\) we compute a sorted array \(A_\sigma\) containing the positions at which \(\sigma\) appears in _y_.

In the query phase, we are given a string _x_ and a preprocessed string _y_. The algorithm builds a dynamic programming table _T_ of length |_x_|+1, maintaining the following invariant: After the _i_-th round, _T_\[_k_\] stores the minimum _j_ such that _L(x_\[1_..i_\]_,y_\[1_..j_\])=_k_ (or \(\infty\) if not such _j_ exists).

Initially, corresponding to round _i_=0, the table _T_ is computed by setting _T_\[0\]=0 and \(T[k]=\infty\) for any \(k\in[|x|]\). Then in round _i_ the goal is to match _x_\[_i_\]. Therefore, we iterate over all \(j\in A_{x[i]}\) in decreasing order; note that this enumerates all positions _j_ in _y_ that match _x_\[_i_\]. For each such _j_, we binary search for a value of _k_ with \(T[k-1]<j\le T[k]\), and we set _T_\[_k_\]=_j_. This can be seen to maintain the invariant. In the end, the largest _k_ with \(T[k]\neq\infty\) is equal to _L(x,y_). In pseudocode, this algorithm does the following.

1. Preprocessing: Compute for each symbol \(\sigma\in\Sigma(y)\) an array \(A_\sigma\) listing the positions at which \(\sigma\) appears in _y_, in sorted order.<tbc>

2. Initialization of _T_: \(T[0]\leftarrow 0\), \(T[k]\leftarrow\infty\) for any \(k\in[|x|]\).<tbc>

3. For each _i_ in \[|_x_\]\]: For each _j_ in _A_<sub>_x_\[_i_\]</sub> in decreasing order:<tbc>

4. Find _k_ such that \(T[k-1]<j\le T[k]\), and set _T_\[_k_\]=_j_.<tbc>

5. Return the largest _k_ such that \(T[k]\neq\infty\).

It is easy to see that the preprocessing can be implemented in time _O_(|_y_|log_n_) and the rest of the algorithm runs in time _O_((|_x_|+_M_)log_n_).

