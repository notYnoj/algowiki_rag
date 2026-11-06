## 5 LCS Step 2: Nearby Searching

The arguments of this section follow from the work of \[CDG<sup>+</sup>18\]. However, for the sake of completeness, we restate the theorems here. This section is dedicated to presenting a method NonMetricEstimation(_W<sub>A</sub>,W<sub>B</sub>_) to be used for estimating the longest common subsequence. The output of this method is a matrix \(\widehat{M}:[|W_A|]\times[|W_B|]\rightarrow\mathbb{Z}^+\) where \(\widehat{M}[i][j]\) estimates the LCS of windows \(w_i\in W_A\) and \(w_j\in W_B\). We allow for errors in a few elements of \(\widehat{M}\) but we prove at the end of this section that with high probability, the error does not affect the solution significantly.

Our algorithm is pretty simple: We call a pair (_w<sub>i</sub>,w<sub>j</sub>_) of windows _underestimated_ if their LCS is large enough (at least \(\epsilon\lambda\) when normalizing the LCS size) but it is not computed within the desired approximation factor in Step 1.

We are guaranteed by the bounds of Step 1 that the total number of underestimated pairs of windows is sublinear in the number of pairs. Thus, we show their count by \(k^{2-\eta}\). Define \(\mathcal{W}=k^{\eta/2}\mathsf{w}_\mathsf{max}\) and let two windows of the _A_ side or two windows of the _B_ side be _nearby_ if and only if the distance of the starting indices of the windows is bounded by W. Fix \(\epsilon_\mathsf{nbs}\) to be a small error rate. In our algorithm, we sample the windows of the _A_ side with a rate \(p=(10logn)k^{-\eta/2}/\epsilon_\mathsf{nbs}\) and discover all the underestimated pairs whose _A_ side is subsampled via a naive brute-force. We then recompute the LCS of each pair of windows (_w<sub>i</sub>,w<sub>j</sub>_) such that \(w_i\in W_A,w_j\in W_B\) and we detect an underestimated pair \((w_{i^\prime},w_{j^\prime})\) such that _w<sub>i</sub>_ and \(w_{i^\prime}\) are nearby and _w<sub>j</sub>_ and \(w_{j^\prime}\) are also nearby. Finally, starting from the distance matrix provided in Step 1, we update the solution for each pair of windows that we compute their LCS from scratch and output it as matrix \(\widehat{M}\). We prove in Lemma 5.1 that the error of our estimations is bounded with high probability.

**Algorithm 7** Nearby Searching

1: \(p\leftarrow(10logn)k^{-\eta/2}/\epsilon_\mathsf{nbs}\)

2: \(\mathcal{W}\leftarrow k^{\eta/2}\mathsf{w}_\mathsf{max}\)

3: \(\widehat{M}\leftarrow M\)

4: **for** \(w\in W_A\) **do**

5: Skip the following commands with probability 1-_p_

6: **for** \(w'\in W_B\) **do**

7: Compute the LCS of _w_ and \(w'\)

8: **if** \((w,w')\) is underestimated in _M_ **then**

9: **for** any window _w_<sub>1</sub> in _W<sub>A</sub>_ which is nearby to _w_ **do**

10: **for** any window _w_<sub>2</sub> in _W<sub>B</sub>_ which is nearby to \(w'\) **do**

11: Update \(\widehat{M}\) by computing the LCS of _w_<sub>1</sub> and _w_<sub>2</sub> from scratch.

12: **end for**

13: **end for**

14: **end if**

15: **end for**

16: **end for**

17: **return** \(\widehat{M}\)

Let _M_ be the output of Step 1 of our algorithm and \(\widehat{M}\) be the output of Step 2. We refer to the size of the optimal LCS made by matrices _M_ and \(\widehat{M}\) by LCS(_M_) and \(\text{LCS}(M')\) respectively. We moreover, define a matrix \(M'\) which is the same as _M_ except that the LCS values of all the underestimated pairs are corrected in \(M'\). Similarly, we denote by \(\text{LCS}(M')\) the size of the longest common subsequence made by running DP on matrix \(M'\). We prove below that the error between \(\text{LCS}(M')\) and \(\text{LCS}(\widehat{M})\) is bounded.

