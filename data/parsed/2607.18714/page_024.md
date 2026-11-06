The algorithm MODIFIEDFINDCENTERS is straightforward. It invokes FINDCENTERS but restricts it to a maximum of \(\tilde{\mathsf{O}}(1)\) iterations, forcefully terminating the procedure if this limit is exceeded. If FINDCENTERS completes naturally within this threshold, MODIFIEDFINDCENTERS returns the set \(A_\alpha\) produced by that run of FINDCENTERS. Otherwise, it repeats the process. We now formalize and prove the guarantees provided by this modified algorithm.

Let X denote the number of iterations executed by the while loop in FINDCENTERS. By Theorem A.3, \(\mathbb{E}[\mathsf{X}]=\tilde{\mathsf{O}}(1)\). Applying Markov’s inequality, \(\mathrm{Pr}[\mathsf{X}\ge 2\mathbb{E}[\mathsf{X}]]\le 1/2\). We call an execution of FINDCENTERS _successful_ if it terminates within \(2\mathbb{E}[\mathsf{X}]=\tilde{\mathsf{O}}(1)\) iterations. Any single invocation of FINDCENTERS is therefore successful with probability at least 1/2.

MODIFIEDFINDCENTERS repeatedly invokes FINDCENTERS independently. The probability that \(\tilde{\mathsf{O}}(1)\) consecutive runs all fail is at most \((1/2)^{\tilde{\mathsf{O}}(1)}\le\mathsf{n}^{-\mathsf{c}}\) for some constant c_\>_0. Hence, with high probability, there is a successful run of FINDCENTERS within the first \(\tilde{\mathsf{O}}(1)\) iterations of MODIFIEDFINDCENTERS. We now show the guarantees given by MODIFIEDFINDCENTERS.

1. The size of \(A_\alpha\)<tbc>

<tbc>We have shown that within the first \(\tilde{\mathsf{O}}(1)\) iterations of the while loop in MODIFIEDFINDCENTERS, there is a successful run of FINDCENTERS. Consider this successful run of FINDCENTERS. It executes \(\tilde{\mathsf{O}}(1)\) iterations of FINDCENTERS, and in each iteration, at most \(\tilde{\mathsf{O}}\left(\frac{\mathsf{n}}{2^{2\alpha}}\right)\) vertices are added to \(A_\alpha\). Thus, the size of \(A_\alpha\) at termination is at most \(\tilde{\mathsf{O}}(1)\times\tilde{\mathsf{O}}\left(\frac{\mathsf{n}}{2^{2\alpha}}\right)=\tilde{\mathsf{O}}\left(\frac{\mathsf{n}}{2^{2\alpha}}\right)\).<tbc>

2. Size of \(\mathsf{ball}_\alpha(\cdot)\) and \(\mathrm{cluster}_\alpha(\cdot)\)<tbc>

<tbc>Using Theorem A.1, ball size is bounded with high probability. And by Theorem A.3, cluster size is bounded deterministically.<tbc>

3. Running time of MODIFIEDFINDCENTERS<tbc>

<tbc>In MODIFIEDFINDCENTERS, we run FINDCENTERS at most \(\tilde{\mathsf{O}}(1)\) times with a high probability. Also, we allow each invocation of FINDCENTERS to run at most \(\tilde{\mathsf{O}}(1)\) iterations. Using (B3), each iteration of FINDCENTERS takes \(\tilde{\mathsf{O}}(\mathsf{n}^2)\) time. Thus, the running time of MODIFIEDFINDCENTERS is \(\tilde{\mathsf{O}}(\mathsf{n}^2)\) with a high probability.

Thus, all conditions of Theorem 3.5 hold with high probability, completing the proof.

## B Proof of Theorem 3.7

To prove Theorem 3.7, we require that for each \(\mathsf{i}\ge\alpha\), the algorithm samples vertices into A<sub>i</sub> independently. However, since FINDCENTERS performs sampling across multiple iterations, independence within \(A_\alpha\), and hence A<sub>i</sub>, does not follow immediately.

To address this issue, consider the vertices selected in the first iteration of FINDCENTERS that lie in \(A_\alpha\). Denote this set by \(A_\alpha(1)\). FINDCENTERS samples each vertex from V into \(A_\alpha(1)\) independently with probability \(\frac{1}{2^{2\alpha}}\). For \(\mathsf{i}>\alpha\), define \(A_\mathsf{i}(1)\subseteq A_\mathsf{i}\) as the set of vertices obtained by sampling from A<sub>i-1</sub>(1).

Let R be the event that an invocation of FINDCENTERS finishes within the cutoff. Using our arguments in the previous section, \(\mathrm{Pr}[\mathsf{R}]\ge 1/2\). Since MODIFIEDFINDCENTERS returns the first independent invocation satisfying R, its output is distributed as an invocation of FINDCENTERS conditioned on R. Before conditioning, every vertex belongs to A<sub>i</sub>(1) independently with probability 1/2<sup>2i</sup> for every \(\mathsf{i}\ge\alpha\). This follows by induction: it holds for \(\mathsf{i}=\alpha\) by the first iteration of FINDCENTERS, and<tbc>

\(\mathrm{Pr}[\mathsf{v}\in A_{\mathsf{i}+1}(1)]=\mathrm{Pr}[\mathsf{v}\in A_\mathsf{i}(1)]\frac{1}{2^{2\mathsf{i}}}=\frac{1}{2^{2\mathsf{i}}}\frac{1}{2^{2\mathsf{i}}}=\frac{1}{2^{2^{\mathsf{i}+1}}}.\)

