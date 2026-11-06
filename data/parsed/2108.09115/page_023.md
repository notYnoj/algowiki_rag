<tbc>_average_. However, the analysis of the sparse case, crucially relies on _every window_ being sparse. By Markov’s inequality, once we decrease the average degree of the A-window at most \(t^{-\epsilon}\)-fraction of them remain overly-dense. We can thus recurse on all the B-windows and the \(t^{-\epsilon}\)-fraction overly-dense A-windows, again removing the highest-degree B-windows. After \(O(1/\epsilon)\) iterations, all the dense A-windows have been removed.

As in Section 5, we repeat the following steps for every \(\tau\) in a multiplicative-\((1+\epsilon)\)-net.

## Parameters and notation

Following the notation of Section 5.2, we set the base window length to _d=n_<sup>0.2</sup>, and the number of A-windows is _t=n_<sup>0.8</sup>; the number of windows in \(\mathcal{B}_\tau\) is \(t_\tau=O_\epsilon(t/\tau)\). Our algorithm will use \(t_\tau^{3/2+o(1)}\) queries, each in time \(\tilde{O}(d^2\tau^2)\), as well as the DP from Lemma 12. Hence the total running time is given by

\(\tilde{O}\big(t_\tau^{3/2+o(1)}\cdot d^2\tau^2+\frac{n^2}{d^2}\big)=\tilde{O}(n^{1.6+o(1)}).\) (4)

Our sparsification phase (Steps A-2 and B below) works in iterations, where in each iteration we cover the edges of the form (_a,b_) where _b_ is a high degree vertex. In more detail, the algorithm iteratively identifies B-windows with high degree. At the first iteration, the degree threshold is \(\mathrm{deg}_1:=t_\tau^{1/2}\), and it decreases by \(t_\tau^\epsilon\) in each subsequent iteration. I.e. at the _g_-th iteration it is \(\mathrm{deg}_g:=t_\tau^{1/2-(g-1)\epsilon}\).

We maintain a partition of A into three subsets: \(\mathcal{A}=\mathcal{A}_\mathrm{SPARSE}\cup\mathcal{A}_\mathrm{BAD}\cup\mathcal{A}_\mathrm{COVERED}\). Initially, \(|\mathcal{A}_\mathrm{BAD}|\le|\mathcal{A}|=t\le t_\tau\). In each iteration of the sparsification phase, windows from A<sub>BAD</sub> are moved to A<sub>COVERED</sub>. The upper bound on |A<sub>BAD</sub>| decreases by \(t_\tau^\epsilon\)-factor in each iteration.

## Step A: Estimating density of A-windows

For each \(a\in\mathcal{A}\), we sample \(t_\tau^{1/2-\epsilon}\mathrm{log}^2(n)\mathcal{B}_\tau\)-windows _b_ at random and query ED(_b,a_). We place _a_ in A<sub>BAD</sub> if at least \(\frac{1}{2}\mathrm{log}^2(n)\) of the samples are within edit distance \(\tau\). Otherwise, we place it in A<sub>SPARSE</sub> and ignore it until Step C of the algorithm.

## Complexity:

We spend \(\tilde{O}(t_\tau^{1/2})\) queries for each \(a\in\mathcal{A}_\mathrm{BAD}\), hence a total of \(\tilde{O}(t_\tau^{3/2})\).

## Step B-_g_. An iteration of the sparsification phase

In each iteration of the sparsification phase, we enumerate over the \(\mathcal{B}_\tau\)-windows. For each window _b_ that has not already been marked _dense_ in previous iterations, we sample \(\frac{|\mathcal{A}_\mathrm{BAD}|\mathrm{log}^2(n)}{\mathrm{deg}_g}\mathcal{A}_\mathrm{BAD}\)- windows _a_ at random and query ED(_b,a_). We say that _b_ is _dense_ if at least \(\frac{1}{2}\mathrm{log}^2(n)\) of the samples are within edit distance \(\tau\).

If _b_ is dense, we query its entire \(\mathcal{N}^{\mathcal{A}_\mathrm{BAD},\tau}(b),\mathcal{N}^{\mathcal{B}_\tau,2\tau}(b)\) neighborhoods. We (implicitly) add edges with cost \(3\tau\) for every pair in \(\mathcal{N}^{\mathcal{A}_\mathrm{BAD},\tau}(b)\times\mathcal{N}^{\mathcal{B}_\tau,2\tau}(b)\), and move the windows in \(\mathcal{N}^{\mathcal{A}_\mathrm{BAD},\tau}(b)\) to A<sub>COVERED</sub>.

If the number of A<sub>BAD</sub> windows becomes at most \(t_\tau^{1/2}\) at any point, we exhaustively find all their neighbors in \(\mathcal{B}_\tau\) and move them to A<sub>COVERED</sub>.

