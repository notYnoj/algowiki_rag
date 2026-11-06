## A Proof of Theorem 3.5

We construct the sample set \(A_\alpha\) using an iterative approach based on the Thorup-Zwick algorithm \[TZ01\]. The construction relies on two primary procedures: FINDCENTERS, which iteratively builds the sample set, and FINDBALLS&CLUSTERS, which computes the corresponding balls and clusters.

In FINDCENTERS, we initialize the active vertex set _W_ to _V_ and the sampled set \(A_\alpha\) to \(\emptyset\). We then proceed in rounds. In each iteration, we sample \(\tilde{O}\left(\frac{n}{2^{2^\alpha}}\right)\) vertices from _W_ and add these to \(A_\alpha\). Specifically, the subroutine SAMPLE(X,s) independently samples each element of X with probability \(min\left\{1,\frac{s}{|X|}\right\}\).

Following the sampling step, we invoke FINDBALLS&CLUSTERS\((A_\alpha,\alpha)\) to update \(\mathrm{ball}_\alpha(v)\) and \(\mathrm{cluster}_\alpha(v)\) for all \(v\in V\). Any vertex _w_ whose cluster size exceeds the threshold of \(4\times 2^{2^\alpha}\) is retained in _W_ for the next iteration. This loop continues until no vertices have excessively large clusters and _W_ becomes empty. This completes the algorithm’s description. We now state its guarantees.

\(\text{\textbf{Algorithm 9:} FINDCENTERS Initialize}A_\alpha\leftarrow\emptyset\text{2}W\leftarrow V\text{\textbf{while}}W\neq\emptyset\text{\textbf{do 4}}A_\alpha\leftarrow A_\alpha\cup\mathrm{SAMPLE}\left(W,\frac{n}{2^{2^\alpha}}\right)\text{\textbf{5} FINDBALLS&CLUSTERS}(A_\alpha,\alpha)\text{\textbf{6}}W\leftarrow\{w\in V||\mathrm{cluster}_\alpha(w)|>4\times 2^{2^\alpha}\}\text{\textbf{7 return}}A_\alpha\text{\textbf{Algorithm 10:} FINDBALLS&CLUSTERS}(A_\mathrm{i},\mathrm{i})\text{\textbf{1 Perform a multi-source BFS from vertices of}}A_\mathrm{i}\text{and update pivot}_\mathrm{i}(s)\text{and est(s,pivot}_\mathrm{i}(s))\text{for each}s\in V\text{\textbf{2 foreach}}s\in V\text{\textbf{do 3 Perform a BFS from}}s\text{up to distance}|\mathrm{s pivot}_\mathrm{i}(s)|-1\text{from}s\text{\textbf{4 foreach}}v\in BFS\text{\textit{Tree of}}s\text{\textbf{do 5}}\mathrm{est}(s,v)\leftarrow\text{level of}v\text{in BFS tree of}s\text{\textbf{6}}\mathrm{ball}_\mathrm{i}(s)\leftarrow\mathrm{ball}_\mathrm{i}(s)\cup\{v\}\text{\textbf{7}}\mathrm{cluster}_\mathrm{i}(v)\leftarrow\mathrm{cluster}_\mathrm{i}(v)\cup\{s\}\)

Observe that in the first iteration of the while loop in FINDCENTERS, the set _W=V_, so SAMPLE independently samples each vertex of _V_ with probability \(\frac{1}{2^{2^\alpha}}\). We now demonstrate that after just this first iteration, \(|\mathrm{ball}_\alpha(v)|\le\tilde{O}(2^{2^\alpha})\) for all \(v\in V\).

To see why, order the vertices of the graph by their distance from _v_, breaking ties arbitrarily. Let _S_ denote the set consisting of the first \(\tilde{O}(2^{2^\alpha})\) vertices in this sorted sequence. The probability that \(A_\alpha\) contains no vertices from _S_ after the first iteration is \(\left(1-\frac{1}{2^{2^\alpha}}\right)^{\tilde{O}(2^{2^\alpha})}\). By appropriately choosing the hidden constant in the \(\tilde{O}\) notation, this probability is at most \(\frac{1}{n^c}\) for some constant c_\>_0.

Consequently, with high probability, at least one vertex in _S_ is sampled into \(A_\alpha\). Because the ball only explores up to the nearest sampled vertex (the pivot), the ball of _v_ will contain at most the vertices in _S_, meaning its size is bounded by \(\tilde{O}(2^{2^\alpha})\). In subsequent iterations of FINDCENTERS, the sampled set \(A_\alpha\) can only grow. As \(A_\alpha\) expands, the size of \(\mathrm{ball}_\alpha(v)\) can only decrease. Thus, we establish the following lemma:

**Lemma A.1.** _After running_ FINDCENTERS_, for each_ \(v\in V\), \(|\mathrm{ball}_\alpha(v)|\le\tilde{O}(2^{2^\alpha})\) _with high probability. This establishes condition (2) of Theorem 3.5 for the ball size._

We now use the above lemma to bound the running time of FINDBALLS&CLUSTERS.

**Lemma A.2.** _The running time of_ FINDBALLS&CLUSTERS\((A_\alpha,\alpha)\) _is_ \(\tilde{O}(n^2)\).

_Proof._ In the first step of FINDBALLS&CLUSTERS\((A_\alpha,\alpha)\), we perform a multi-source BFS from all vertices of \(A_\alpha\). To this end, we add a new source vertex X to the graph and connect it to all vertices of \(A_\alpha\)<tbc>

