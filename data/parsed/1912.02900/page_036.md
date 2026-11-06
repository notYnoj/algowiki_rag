If we now consider any type-(2b) crossing \((p,p')\), and the instances \(X_s,X_{s^\prime}\) that are responsible for it, with \(s<s'\), then it must be the case that exactly one of the rows \(R_s,R_{s^\prime}\) is a left row, and the other is a right row. Moreover, if \(s'>s+1\), then every row lying between _R<sub>s</sub>_ and \(R_{s^\prime}\) is an empty row.

Let us denote the points in _X_<sub>1</sub> by _p_<sub>1</sub>_,...,p_log_N_, where for each \(1\le i\le logN\), point _p<sub>i</sub>_ lies in column _C_<sub>2_<sup>i</sup>_</sub>. In each subsequent instance _X_<sub>2</sub>_,X_<sub>3</sub>_,..._, the point is shifted by one unit to the right, so that in instance _X<sub>s</sub>_ it lies in column _C_<sub>2_<sup>i</sup>+s_-1</sub>; every column in C must contain exactly one copy of point _p<sub>i</sub>_.

Consider now all copies of the point _p<sub>i</sub>_ that lie in the strip _S_. Let R_<sub>i</sub>_ be the set of rows containing these copies. Then two cases are possible: either (i) R_<sub>i</sub>_ is a contiguous set of rows, and the copies of _p<sub>i</sub>_ appear on R_<sub>i</sub>_ diagonally as an increasing sequence (the _j_th row of R_<sub>i</sub>_ contains a copy of _p<sub>i</sub>_ that lies in the _j_th column of C in the strip _S_); or R_<sub>i</sub>_ consists of two consecutive sets of rows; the first set, that we denote by \(\mathcal{R}'_i\), contains _R_<sub>1</sub>, and the second set, that we denote by \(\mathcal{R}''_i\), contains the last row _R<sub>N</sub>_. The copies of the point _p<sub>i</sub>_ also appear diagonally in \(\mathcal{R}'_i\) and in \(\mathcal{R}''_i\); in \(\mathcal{R}''_i\) the first copy lies on the first column of C in _S_; in \(\mathcal{R}'_i\) the last copy lies on the last column of C in _S_ (see Figure 6).

We show that for each \(1\le i\le logN\), there are at most four type-(2b) crossings of the line _L_ in which a copy of _p<sub>i</sub>_ participates. Indeed, consider any type-(2b) crossing \((p,p')\) in which a copy of _p<sub>i</sub>_ participates. We assume that the row of _p_ lies below the row of \(p'\). Assume first that both _p_ and \(p'\) lie on rows of R_<sub>i</sub>_, and let \(R,R'\) be these two rows, with \(p\in R\), \(p'\in R'\). Recall that, in order for \((p,p')\) to define a crossing, all input points that lie on \(R\cap S\) must lie to the left of _L_, and all point points that lie on \(R'\cap S\) must lie to the right of _L_, or the other way around. It is easy to verify (see Figure 6) that one of two cases must happen: either _R_ contains a copy of _p<sub>i</sub>_ lying closest to _L_ on its left, and \(R'\) contains a copy of _p<sub>i</sub>_ lying closest to _L_ on its right; or _R_ is the last row of \(\mathcal{R}'_i\), and \(R'\) is the first row of \(\mathcal{R}''_i\). Therefore, only two such crossing, with \(R,R'\in\mathcal{R}_i\) are possible.





(a) The consecutive set of rows on which the copies of _p<sub>i</sub>_ appear is denoted by R_<sub>i</sub>_.

(b) The two consecutive sets of rows on which the copies of _p<sub>i</sub>_ appear are \(\mathcal{R}'_i\) (on the bottom) and \(\mathcal{R}''_i\) (on the top).

Figure 6: Two patterns in which copies of _p<sub>i</sub>_ may appear on strip _S_.

