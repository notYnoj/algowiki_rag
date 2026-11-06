### Initialization: Covered windows

Initially, all windows are uncovered. Intuitively, we say that a window is covered when we have upper bounded the edit distance to its relevant neighbors in \(\mathcal{B}^\tau\).

## A: Intervals

Consider a partition of \[_n_\] into \(t_\tau^{1/3+\epsilon}\) contiguous intervals of length \(n/t_\tau^{1/3+\epsilon}\le t_\tau^{2/3-\epsilon}\cdot d\). For _A_ we define the A_-interval I_<sub>A</sub> corresponding to interval \(I\subset[n]\) as the set of \(\le t_\tau^{2/3-\epsilon}\) windows with indices in _I_. Therefore, for _A_-windows they are either entirely contained in the interval or don’t intersect it. For _B_, we let \(I/\epsilon\) denote a \(1/\epsilon\)-factor expansion of _I_ (i.e. the interval of length \(|I|/\epsilon\) centered at _I_)<sup>2</sup>. We define the \(\mathcal{B}^\tau\)-interval \(I_{\mathcal{B}^\tau}\) to be the set of windows that intersect \(I/\epsilon\). When clear from context we sometimes just call \(I_\mathcal{A},I_{\mathcal{B}^\tau}\) intervals.

## B: Sampling seeds

For each A-interval _I_<sub>A</sub>, if less than log<sup>2</sup>(_n_) windows in _I_<sub>A</sub> remain uncovered, we simply find all of their \(\tau\)-neighbors in \(\mathcal{B}^\tau\) using \(\tilde{O}(t_\tau)\) queries and mark them covered. Otherwise we sample log<sup>2</sup>(_n_) uncovered windows from _I_<sub>A</sub>. For each sampled window _a_, we test whether \(|\mathcal{N}^{\mathcal{B}^\tau,\tau}(a)|\unknown t_\tau^{1/3}\). This is done by sampling \(t_\tau^{2/3}\mathrm{log}^2(n)\) windows \(b\in\mathcal{B}^\tau\) and querying ED(_a,b_) for each. (We account for those queries later, depending on whether _a_ is dense or sparse.)

If more than log<sup>2</sup>(_n)/_2 of the samples belong to \(\mathcal{N}^{\mathcal{B},\tau}(a)\) then _a_ is declared dense, otherwise it is sparse. If the window is dense we process it as described below, after which it is a covered window and no longer a good sample. We then continue to sample (in random order) other uncovered windows from the same _I_<sub>A</sub> until: If the number of sparse windows sampled so far is smaller than log<sup>2</sup>(_n_), we stop sampling whenever we see log<sup>2</sup>(_n_) consecutive covered windows. Otherwise (the number of observed sparse sampled windows is at least log<sup>2</sup>(_n_)), we stop sampling after querying log<sup>2</sup>(_n_) consecutive windows which are all either sparse or covered.

_Remark._ Therefore, if we keep discovering dense windows, we process it as in Step C, the window gets covered, and we keep on sampling more uncovered windows.

## C: Dense windows

Suppose that _a_ is dense; choose (arbitrarily) \(b\in\mathcal{N}^{\mathcal{B}^\tau,\tau}(a)\) among those discovered during Step B while processing _a_. For each windows-pair \(a'\in\mathcal{N}^{\mathcal{A},2\tau}(a)\) and \(b'\in\mathcal{N}^{\mathcal{B}^\tau,4\tau}(b)\), whose estimate has not been computed yet, the algorithm sets \(\mathcal{E}(a',b')\leftarrow 7\tau\). This is done abstractly by pointing each \(a'\) to _a_, \(b'\) to _b_ and marking that \(\mathrm{ED}(a,b)\le\tau\). Observe that the sets \(\mathcal{N}^{\mathcal{A},2\tau}(a),\mathcal{N}^{\mathcal{B}^\tau,4\tau}(b)\) have already been computed during the preprocessing phase. We mark each window in the set \(\mathcal{N}^{\mathcal{A},2\tau}(a)\) as covered.

### Approximation:

Observe that every \(a'\in\mathcal{N}^{\mathcal{A},2\tau}(a)\) is indeed covered in the sense that by triangle inequality, for every \(b''\in\mathcal{N}^{\mathcal{B},\tau}(a')\)

\(\mathrm{ED}(b,b'')\le\mathrm{ED}(b'',a')+\mathrm{ED}(a',a)+\mathrm{ED}(a,b)\le 4\tau,\) (2)

and hence \(\mathcal{N}^{\mathcal{B},\tau}(a')\subseteq\mathcal{N}^{\mathcal{B},4\tau}(b)\). Similarly, by triangle inequality for every \(b'\in\mathcal{N}^{\mathcal{B},4\tau}(b)\) and \(a'\in\mathcal{N}^{\mathcal{B},2\tau}(a)\), we have that

\(\mathrm{ED}(a',b')\le\mathrm{ED}(a',a)+\mathrm{ED}(a,b)+\mathrm{ED}(b,b')\le 7\tau.\) (3)

<sup>2</sup>For example, if _I_=\[20,30\] then its 3-expansion is \[10,40\].

