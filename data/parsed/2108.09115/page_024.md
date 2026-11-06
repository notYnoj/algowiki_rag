### Approximation

By triangle inequality, every pair of windows in \(\mathcal{N}^{\mathcal{A}_\mathrm{Bad},\tau}(b)\times\mathcal{N}^{\mathcal{B}_\tau,2\tau}(b)\) has edit distance at most \(3\tau\). Notice also that by triangle inequality \(\mathcal{N}^{\mathcal{B}_\tau,\tau}(\mathcal{N}^{\mathcal{A}_\mathrm{Bad},\tau}(b))\subseteq\mathcal{N}^{\mathcal{B}_\tau,2\tau}(b)\), i.e. we have discovered all the \((\mathcal{B}_\tau,\tau)\)-neighbors of all the A<sub>CoveRED</sub>-windows.

### Complexity:

We maintain the bound that at the beginning of the _g_-th iteration, \(|\mathcal{A}_\mathrm{Bad}|=O(t_\tau^{1-(g-1)})=O(t_\tau^{1/2}\mathrm{deg}_g)\). Hence, similarly to Step A, we spend \(\tilde{O}(t_\tau^{1/2})\) queries for estimating the degree of each \(b\in\mathcal{B}_\tau\), for a total of \(\tilde{O}(t_\tau^{3/2})\).

Every time we discover a dense _b_, we query its edit distance to \(\le t+t_\tau\) windows, and decrease by \(\Omega(\mathrm{deg}_g)\) the number of remaining A<sub>Bad</sub>-windows. Recall that we start the _g_-th iteration with at most \(O(t_\tau^{1-(g-1)\epsilon})=O(t_\tau^{1/2}\mathrm{deg}_g)\mathcal{A}_\mathrm{Bad}\)-windows. Hence in total this step requires \(O((t+t_\tau)\cdot t_\tau^{1/2})=O(t_\tau^{3/2})\) queries.

## The sparsification phase: iterating over Step B-_g_

We iteratively apply Step B-\(gO(1/\epsilon)\) times. At the end of the _g_-th iteration, every remaining \(\mathcal{B}_\tau\)- window has at most \(\mathrm{deg}_g=t_\tau^{1/2-(g-1)\epsilon}\) remaining \((\mathcal{A}_\mathrm{Bad},\tau)\)-neighbors. Hence the total number of \(\tau\)-close pairs in \(\mathcal{B}_\tau\times\mathcal{A}_\mathrm{Bad}\) is \(t_\tau^{3/2-(g-1)\epsilon}\). Since every A<sub>Bad</sub> window has \(\Omega(t_\tau^{1/2+\epsilon})(\mathcal{B}_\tau,\tau)\)-neighbors<sup>3</sup>, we have that \(|\mathcal{A}_\mathrm{Bad}|=O(t_\tau^{1-(g)\epsilon})\).

## Step C. Sparse windows

We process the A<sub>Sparse</sub>-windows as in the sparse case in Section 5 (for completeness, we spell out the details below). This algorithm is somewhat simpler than Section 5 since we already determined in advance which windows are sparse and which are dense.

### Intervals (first iteration):

Consider a partition of \[_n_\] into \(t_\tau^{1/2+2\epsilon}\) contiguous intervals of length \(n/t_\tau^{1/2+2\epsilon}\le t_\tau^{1/2-2\epsilon}\cdot d\). For _A_ we define the A_-interval I_<sub>A</sub> corresponding to interval \(I\subset[n]\) as the set of \(\le t_\tau^{1/2-2\epsilon}\) windows with indices in _I_. Therefore, for _A_-windows they are either entirely contained in the interval or don’t intersect it. For _B_, we let \(I/\epsilon\) denote a \(1/\epsilon\)-factor expansion of _I_ (i.e. the interval of length \(|I|/\epsilon\) centered at _I_)<sup>4</sup>. We define the \(\mathcal{B}^\tau\)-interval \(I_{\mathcal{B}^\tau}\) to be the set of windows that intersect \(I/\epsilon\). When clear from context we sometimes just call \(I_\mathcal{A},I_{\mathcal{B}^\tau}\) intervals.

### Sparse subroutine (first iteration):

For each interval _I_<sub>A</sub>, if at most log<sup>2</sup>(_n_) of its windows are sparse, we simply query their entire \((\mathcal{B}^\tau,\tau)\)-neighborhoods. Otherwise, we sample a random set _S(I_<sub>A</sub>) of log<sup>2</sup>(_n_) windows from \(I_\mathcal{A}\cap\mathcal{A}_\mathrm{Sparse}\). For every window in _S(I_<sub>A</sub>), we query its entire \((\mathcal{B}^\tau,\tau)\)-neighborhood using \(t_\tau\) queries. For each interval _I_<sub>A</sub> we record the union of all \(\tilde{O}(t_\tau^{1/2+\epsilon})\) intervals \(\widehat{I_{\mathcal{B}^\tau}}\) that contain any \((\mathcal{B}^\tau,\tau)\)-neighbors of any of the sparse samples \(a\in S(I_\mathcal{A})\). We call these B-windows the _relevant windows_ for the windows in _I_<sub>A</sub>. We henceforth no longer look to match windows from _I_<sub>A</sub> to irrelevant B-windows. Note that in a low-skew mapping, if at least one of the samples is matched, then windows in _I_<sub>A</sub> cannot be mapped to any irrelevant B-windows under that mapping.

<sup>3</sup>Notice that the number of remaining neighbors for \(a\in\mathcal{A}_\mathrm{Bad}\) does not change during the run of the sparsification phase, since once any of _a_’s neighbors is declared _dense_, we move _a_ to A<sub>CoveRED</sub>. <sup>4</sup>For example, if _I_=\[20,30\] then its 3-expansion is \[10,40\].

