<tbc>Figure 3 for an illustration. This implies that a large fraction of vertices in _V_\\_S_ can be colored online using First-Fit with only _O_(log<sup>2</sup>_n_) colors.

#### Covering _V_\\_S_ with Multiple Samples.

The issue is that, with a single independent set _I_, only a fraction of the vertices in _V_\\_S_ are colored. We address this issue by _carefully_ sampling a sequence of independent sets _I_<sub>1</sub>_,...,I<sub>r</sub>_ (\(I_r=\emptyset\)), where _r_ is most probably _O_(log_n_). We also maintain "bins" \(J_1,\dots,J_r\subseteq V\backslash S\) for the extension counterpart, initially empty.

For each arrival of \(v\in V\backslash S\), we find the smallest _i_ such that \(N_{I_i}(v)=\emptyset\), and put _v_ into _J<sub>i</sub>_. Then, we can prove that each _G[J<sub>i</sub>_] most probably has maximum degree _O_(log<sup>2</sup>_n_). Hence, by applying First-Fit to each of _G[J_<sub>1</sub>]_,...,G[J<sub>r</sub>_], using a separate set of colors for each bin, we can most probably color the entire _V_\\_S_ with \(r\cdot O(log^2n)=O(log^3n)\) colors.

### 1.6 Organization

Section 2 presents some formal definitions and notation. Section 3 introduces the hardcore model and investigates its properties. Section 4 introduces the main algorithm, and Section 5 analyzes the number of colors used. Section 6 presents an algorithm with a competitive ratio of \(\widetilde{O}(n^{2/3})\). Finally, Section 7 concludes the paper and presents some conjectures.

## 2 Preliminaries

Before moving on to our algorithms, we present the required notation and definitions. First, we formally define online coloring with random arrival order. Then, we define First-Fit, the most straightforward strategy for online coloring.

**Definition 4** (Online Coloring)**.** _In the online coloring problem, an undirected graph G_=(_V,E_) _is initially empty; i.e., there are zero vertices. The vertices of G are given one by one. Immediately after a vertex v arrives (along with all edges incident to previously arrived vertices), we must assign a color_ \(c(v)\in\mathbb{N}\) _that differs from the colors of all adjacent vertices. The goal is to minimize the number of colors used,_ \(|\{c(v):v\in V\}|\).

**Definition 5** (Random-Order Model)**.** _The random-order model of online coloring assumes that a graph G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>)_, where V_<sup>∗</sup>={_v_<sub>1</sub>_,...,v<sub>n</sub>}, is initially fixed and is hidden from the algorithm. We additionally assume that n **is known in advance**. The vertices arrive in the order_ \(v_{\sigma(1)},\dots,v_{\sigma(n)}\)_, where_<tbc>

S
V S
S
V S
I
J
When we take a random independent set I from S...J := {v E V S: NI(v) = 0} is also large and G[J] has degree O(log2 n)

**Figure 3:** Sampling an independent set from _S_ and attempting to extend it into _V_\\_S_.

