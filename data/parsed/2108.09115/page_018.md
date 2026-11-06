• Cost of using a last pair of windows: \(min_{e(b)=j}\left\{\mathcal{E}(a,b)+\mathrm{ED}(s(a)-1,s(b)-1)\right\}\).

Notice that the runtime of our algorithm is dominated by the number of pairs 1, aka it is \(O(\frac{n^2}{d^2})\). Now, considering all choices of \(\Delta\), we get the required running time.

## 5.4 Close-window graphs and the preprocessing phase

For subset of windows C we define the graph \(G_{\mathcal{C},\tau}\) as follows: The vertex set equals C. The pair \((c,c')\) is connected by an edge if \(\mathrm{ED}(c,c')\le\tau d\). For a substring \(z\in\Sigma^d\), we denote by \(\mathcal{N}^{\mathcal{C},\tau}(z)\) the set of all windows \(c\in\mathcal{C}\) satisfying \(\mathrm{ED}(c,z)\le\tau d\). The windows in \(\mathcal{N}^{\mathcal{C},\tau}(z)\) will also be referred to as the \(\tau\)-neighbors of _c_ in C, and \(|\mathcal{N}^{\mathcal{C},\tau}(z)|\) as its degree in C. When it is clear from the context, we will often omit \(\tau\), and simply use the terms such as neighbors and degree of _c_. We will abuse notation and also use this definition for \(z\notin\mathcal{C}\).

### Preprocessing Phase algorithm.

The preprocessing algorithm crucially uses the algorithm for computing _small edit distance_ with preprocessing from Section 3. In the preprocessing phase, strings _A_ and _B_ are processed separately. Let \(\tau\in\{0,\frac{(1+\epsilon)^i}{d}\}\) for \(i=[0..\mathrm{log}_{(1+\epsilon)}d]\).

### Preprocessing _A_.

For each \(\tau\), the preprocessing algorithm computes the graph \(G_{\mathcal{A},\tau}\). The number of windows of _A_ is \(\frac{n}{d}\). Hence, the preprocessing time over all \(\tau\) is \(O(\frac{n^2}{d^2}d^2)=O(n^2)\).

### Preprocessing _B_.

The preprocessing algorithm computes \(G_{\mathcal{B}^\tau,\tau}\) for each \(\tau\). By the preprocessing algorithm of Section 3, we can process entire _B_ in _O(n_log_n_) time so that the computation of \(\tau d\)- thresholded edit distance between any pair of windows can be run in \(O(\tau^2d^2\mathrm{log}n)\) time.

Note that for a given \(\tau\), the gap between two consecutive windows in _B_ is \(\gamma_\tau=\mathrm{max}(1,\lfloor\epsilon\tau d\rfloor)\). Therefore, when \(\tau=0\), the number of windows is _O(n_<sup>2</sup>), but for every pair of windows, edit distance computation time is _O_(1). For \(\tau>0\), the number of windows is \(O(\frac{n}{\epsilon\tau d})\). Hence, the computation time is \(O(\frac{n^2}{\epsilon^2\tau^2d^2}\tau^2d^2\mathrm{log}n)=O(\frac{n^2}{\epsilon^2})\). Thus, over all \(\tau\), the total preprocessing time for _B_ is \(\tilde{O}_\epsilon(n^2)\).

## 5.5 Query Phase algorithm

The input to the query phase algorithm is the two strings, as well as the close-window graphs computed in the preprocessing phase. The output is an estimate data structure that can answer \(\mathcal{E}:\mathcal{A}\times\mathcal{B}\rightarrow\mathbb{R}^+\) queries in _O_(log(_n_)) time. We implicitly initialize \(\mathcal{E}(a,b)\leftarrow\infty\) for all pairs (_a,b_).

We consider all choices of \(\tau\in\{0,\frac{(1+\epsilon)^i}{d}\}\) for \(i=[0..\mathrm{log}_{(1+\epsilon)}d]\). For \(\tau\) we run the following algorithm that attempts to discover the pairs of windows \(a,b\in\mathcal{A}\times\mathcal{B}^\tau\) of edit distance at most \(\tau\). The estimate algorithm has some false negatives, and it may also have false positives whose true edit distance is up to \(7\tau\). The estimate can be fed into the DP in Section 5.3.

Recall that \(t_\tau:=|\mathcal{B}^\tau|\) denote the number of windows in \(\mathcal{B}^\tau\), and \(t_\tau=\frac{n}{\epsilon\tau d}\).

For each value of \(\tau\), the algorithm below uses \(O(t_\tau^{4/3+o(1)})\) queries to edit distance of pairs of windows of length _O(d_) of the form is \(\mathrm{ED}(a,b)<\tau d\). Using the algorithm from Theorem 3, each query can be answered in \(\tilde{O}(d^2\tau^2)\) time. Hence the total run time is given by<tbc>

\(O\big(t_\tau^{4/3+o(1)}\cdot d^2\tau^2\big)=O(n^{3/2+o(1)}).\)

