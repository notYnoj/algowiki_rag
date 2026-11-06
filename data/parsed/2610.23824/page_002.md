## 1 Introduction

We study the _online coloring_ problem, in which vertices are revealed one by one. When a vertex arrives, we must assign it a color immediately, before the next vertex arrives, so that its color differs from the colors of all its previously revealed neighbors. See Figure 1 for an example. This is one of the most extensively studied problems in online algorithms, alongside the _k_-server problem, paging/caching, and online matching \[Alb03\].

### 1.1 Online Coloring

Online coloring is a classical problem for which natural algorithms are ineffective. The most intuitive strategy is _First-Fit_ \[GL88\], which always chooses the smallest available color. However, First-Fit can use _n/_2 colors even on an _n_-vertex bipartite graph, as shown in Figure 2 (such graphs are called crown graphs<sup>1</sup>). Accordingly, online coloring has been widely studied since the 1980s \[LST89\]. The best-known upper bounds on the competitive ratio are as follows: \(O(\frac{n}{logn})\) for randomized algorithms by Halldórsson (1997) \[Hal97\], and \(O(\frac{n}{loglogn})\) for deterministic algorithms by Kawarabayashi, Yoneda, and Yoneda (2025) \[KYY25\]. In contrast, a lower bound of \(\Omega(\frac{n}{log^2n})\) is known due to Halldórsson and Szegedy (1994) \[HS94\].

Given these strong negative results, online coloring of _k_-colorable graphs for a fixed \(k\ge 2\) has received attention. For bipartite graphs (_k=_2), a deterministic algorithm by Lovász, Saks, and Trotter (1989) \[LST89\] achieves _O_(log_n_) colors. The situation becomes much harder for \(k\ge 3\): even for _k=_3, the best-known results are a randomized \(\widetilde{O}(n^{1/2})\)-color algorithm by Vishwanathan (1992) \[Vis92\] and a deterministic \(\widetilde{O}(n^{2/3})\)-color algorithm by Kierstead (1998) \[Kie98\]. For comparison, the best-known lower bound is \(\Omega(log^{k-1}n)\) colors \[Vis92\], leaving a substantial gap between the upper and lower bounds.

Online coloring is also studied for special graph classes, e.g., trees \[Bea76\], interval graphs \[KT81\], planar graphs \[Ira94\], bounded-treewidth graphs \[AS21\], and graphs of large odd girth \[YY26\]. See \[Kie05\] for a survey on online coloring.

<sup>1</sup>A crown graph on _n_ vertices is a complete bipartite graph _K_<sub>_n/_2_,n/_2</sub> with a perfect matching removed. In particular, we consider the graph _G=_({_u_<sub>1</sub>_,v_<sub>1</sub>_,...,u_<sub>_n/_2</sub>_,v_<sub>_n/_2</sub>}_,E_) where \(E=\{\{u_i,v_j\}:i\neq j\}\), and the vertices arrive in the order _u_<sub>1</sub>_,v_<sub>1</sub>_,...,u_<sub>_n/_2</sub>_,v_<sub>_n/_2</sub>.

Color 1
1
1
1
1
1
1
1
1
1
2
2
3
2
3
1
Unknown Vertices/Edges

**Figure 1:** An example of online graph coloring. The numbers inside the vertices indicate their assigned colors. Vertices and edges drawn with gray dotted lines have not yet been revealed. The player must assign a color immediately when a vertex arrives.

