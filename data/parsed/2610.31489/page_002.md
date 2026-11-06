succeeds with constant probability. Goldreich, Goldwasser and Ron \[13\] abandoned regularity altogether and, by constructively extending partitions of the graph, obtained the polynomial bound \(S_k(\varepsilon)=\tilde{O}(k^2/\varepsilon^3)\) for \(k\ge 3\) and \(\tilde{O}(1/\varepsilon^2)\) for _k_=2. Alon and Krivelevich \[1\] improved the bound to \(\tilde{O}(k/\varepsilon^2)\) for \(k\ge 3\) and \(\tilde{O}(1/\varepsilon)\) for _k_=2 by growing a tree of colorings of the sample, and they also proved the lower bound \(S_k(\varepsilon)=\Omega(1/\varepsilon)\). Sohler \[22\] then obtained \(\tilde{O}(k^6/\varepsilon)\), by reducing the problem to the satisfiability of a constraint satisfaction problem.

More recently, Blais and Seth \[7, 8\] obtained \(S_k(\varepsilon)=O(\frac{k}{\varepsilon}log^2\frac{1}{\varepsilon})\) by introducing the container method of extremal combinatorics \[18, 6, 21\] into property testing. Kushnir and Shapira \[19\] refined this analysis, removing a factor of \(log(1/\varepsilon)\) and thereby attaining \(O(\frac{k}{\varepsilon}log\frac{1}{\varepsilon})\), which was the previous state of the art, and they also proved a lower bound \(S_k(\varepsilon)=\Omega(logk/\varepsilon)\), conjecturing that \(\Theta(logk/\varepsilon)\) is the truth. In this paper, we prove an upper bound of \(O(\frac{k}{\varepsilon}logk)\) (Theorem 1.1 below).

**Theorem 1.1.** _For every integer_ \(k\ge 2\) _and every_ \(\varepsilon>0\), <sup>1</sup><tbc>

\(S_k(\varepsilon)=O\big(\frac{k}{\varepsilon}logk\big),\)

<tbc>_with an absolute implied constant. More explicitly, choose_<tbc>

\(T:=\left\lceil\frac{4k}{\varepsilon}\right\rceil,\alpha:=\frac{\varepsilon}{4(k+1)},\)

<tbc>_and set_

\(q:=max\left\{4T,\left\lceil\frac{4}{\alpha}log(16k)\right\rceil\right\}.\)

_Then every n-vertex graph that is_ \(\varepsilon\)_-far from being k-colorable has a non-k-colorable induced subgraph on q uniformly sampled vertices with probability at least_ 2/3.

Comparing with the former upper bound of \(O(\frac{k}{\varepsilon}log\frac{1}{\varepsilon})\) of Kushnir and Shapira \[19\], by the conclusion of Lemma 3.2 below, the new bound is no worse than the previous one throughout the nonvacuous parameter range, since \(\varepsilon<1/(2k)\) implies \(logk<log\frac{1}{\varepsilon}\). Moreover, it is a strict improvement whenever \(1/\varepsilon\) is superpolynomial in _k_. Also, if _k_ is fixed, our upper bound matches the existing best lower bound of \(\Omega(\frac{logk}{\varepsilon})\) up to a constant factor, which shows that the sample complexity (treating _k_ as constant) is \(\Theta(\frac{1}{\varepsilon})\).

In general, a container argument compresses a large family of combinatorial objects by recording a relatively small fingerprint and associating it with a container that covers every object having that fingerprint. The counting is based on the fingerprints and the containers they correspond to. In this paper, the proof idea is a combination of containers and palettes. The use of palettes and lists of available colors is classical in graph coloring, see, for example, work on bounded-palette list coloring and palette sparsification \[3, 2, 5, 4\].

Our algorithmic mechanism is different from \[7, 19\]’s. For each original vertex, we use the minimum monochromatic degree over all colors that remain available in its palette. In our process, the deletion triggered by a degree threshold empties the entire palette of an original vertex, rather than removing a single vertex–color copy. After defining a graph consisting of _k_ copies of the original graph, \[7, 19\] introduce a container process that, in fact, applies to any undirected graph. In this paper, we restate the process from the perspective of palettes to make the proof appear more natural.

<sup>1</sup>Our proof also applies when _k_=1. Thus, a formulation valid for all integers \(k\ge 1\) is \(O(klog(k+1)/\varepsilon)\).

