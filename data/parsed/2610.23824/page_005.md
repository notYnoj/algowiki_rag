under the widely believed assumption that \(\text{NP}\unknown\in\text{BPP}\) [AB09]. We note that, although a graph coloring can be obtained by repeatedly choosing a maximum independent set among the uncolored vertices, Rubinstein’s algorithm [Rub16] does not directly imply an online coloring algorithm for random arrivals because the random arrival order on the uncolored vertices is not guaranteed.

**Remark 3.** _Since the approximation side allows randomized algorithms, including random-order processing, we regard this comparison as fair. Moreover, our result achieves O_(log<sup>4</sup>_n_) _colors for 3-colorable graphs; however, no polynomial-time algorithm that colors 3-colorable graphs with O(n_<sup>1/10</sup>) _colors is known at the time of writing._<sup>2</sup>

## 1.5 Overview of the Algorithm

In this subsection, we present an overview of our algorithm and the intuition behind using random arrival order. For simplicity, we consider the case _k=_3 here; the goal is to color a 3-colorable graph _G=(V,E_) online with _O_(log<sup>4</sup>_n_) colors.

First, it suffices to devise an algorithm that colors the last _n/_2 vertices with _O_(log<sup>3</sup>_n_) colors, using information from the first _n/_2 vertices. If this can be done, we can color the entire graph with _O_(log<sup>4</sup>_n_) colors by recursively applying the same algorithm to the first _n/_2 vertices (for example, we color the _n/_4+1_,...,n/_2-th vertices using information from the first _n/_4 vertices), using completely disjoint color sets for different levels of recursion. Here, we denote the set of the first _n/_2 vertices by _S_.

### The Benefit of Random Order.

The benefit of random arrival order is that \(S\subseteq V\) can be assumed to be chosen uniformly at random. Hence, we can assume that the two parts, _G[S_] and _G[V_\\_S_], have similar properties. For example, the sizes of maximum independent sets and the sizes of each color class in a 3-coloring \(\varphi:V\rightarrow\{1,2,3\}\) are very similar.

In particular, for a sufficiently large independent set \(I\subseteq V\) , the parts of _I_ that lie in _S_ and in _V_\\_S_ do not differ much in size, with a statistical error of only \(\pm\widetilde{O}(\sqrt{n})\). Therefore, after the first _n/_2 vertices have arrived, if we "sample" an independent set \(I\subseteq S\) of _G[S_], then it is likely that _I_ can be "extended" to the vertices in _V_\\_S_ to the extent as large as _I_. This mechanism allows us to obtain a large independent set in _G[V_\\_S_] online.

### Hardcore Sampling and Extension.

After receiving all vertices in _S_, we sample an independent set \(I\subseteq S\) from the _hardcore model_ [DK25; Wei06] with parameter \(\lambda\approx\frac{1}{40lnn}\), where _I_ is chosen with probability proportional to \(\lambda^{|I|}\). As implied by the fact that a 3-colorable graph _G[S_] has an independent set of size at least |_S|/_3≈_n/_6, the expected size of _I_ is \(\Theta(\lambda n)=\Theta(\frac{n}{logn})\).

Then, the set of "eligible" vertices for extending the independent set _I_ toward _V_\\_S_ is \(J:=\{v\in V\backslash S:N_I(v)=\emptyset\}\), which is sufficiently large by the discussion above.<sup>3</sup> While _J_ itself may not be an independent set, it can be proven that _G[J_] most probably has maximum degree _O_(log<sup>2</sup>_n_). See<tbc>

<sup>2</sup>Bansal, Huang, and Lee (2026) [BHL26] present an algorithm that colors 3-colorable graphs with _O(n_<sup>0.1954</sup>) colors in polynomial time. Very recently, Song (2026) [Son26] published a preprint claiming to achieve _O(n_<sup>0.1653</sup>) colors. <sup>3</sup>Although we do not directly prove that the "extension" is sufficiently large in the subsequent proof, we believe that this fact helps explain the intuition behind the algorithm.

