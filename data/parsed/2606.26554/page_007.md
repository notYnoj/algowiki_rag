<tbc>in Equation (1), their running time is not better than \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}\left(n,n,n|1\right)\right)=\widetilde{\Theta}\left(\mathsf{T}_\mathrm{BMM}\left(n,n,n\right)\right)\). Hence, using fast matrix multiplication for Boolean matrix product (this is the currently best known algorithm for Boolean matrix product), their running time always has an \(n^\omega\) term, even for small values of _s_.

We improve \[GV19\]’s algorithm for small values of _s_, in the important special case of directed acyclic graphs:

**Theorem 1.6.** _There is a deterministic algorithm computing_ MSSP _on unweighted directed acyclic graphs in_ \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}\left(|S_\mathrm{in}|,n,n|n,1\right)\right)\) _time._

Surprisingly, even though the running time expression for Theorem 1.6 is quite different from Equation (2), the _numerical_ values of the exponents in _n_ appear to match for small values of _s_, utilizing the currently best known algorithm for Min-Plus product between two matrices that can have potentially different entry bounds. In fact, if we take the minimum of \[GV19\]’s algorithm and Theorem 1.6, the upper and lower bounds appear to be numerically matching for all values of _s_! Of course, this does not establish a formal lower bound, as there might be better algorithms for such Min-Plus product instances. See Section A for details.

## Shortcut Sets

A set of edges _F_ is a _D_-shortcut-set for graph _G_=(_V,E_) if \(H=\left(V,E\cup F\right)\) has the same transitive closure as _G_ and \(\mathrm{diam}(G\cup F)\le D\). For a directed graph, \(\mathrm{diam}(G)=\mathrm{max}_{\left(u,v\right)\in\mathrm{TC}\left(G\right)}\mathrm{dist}\left(u,v\right)\) is the maximum distance between any two vertices for \(\left(u,v\right)\in\mathrm{TC}\left(G\right)\), where TC(_G_) is the transitive closure of _G_. Shortcut sets have applications in reachability and shortest paths computation in many settings \[KS97, HKN14, HKN15, FN18, LJS19, Fin20, GW20, BGW20\]. Similar to exact hop-sets, a folklore sampling algorithm yields a shortcut set of diameter \(O(\sqrt{n})\) and size \(\widetilde{O}\left(n\right)\). A breakthrough result of Kogan and Parter \[KP22b\] showed that in fact there exist shortcut sets of size \(\widetilde{O}\left(n\right)\) and diameter _O(n_<sup>1/3</sup>), while no linear size shortcut set can achieve diameter _o(n_<sup>1/4</sup>) \[BH23, VXX24\]. As with hop-sets, known algorithms for computing shortcut sets are not optimal, with the current best algorithm computing diameter _D_-shortcut- sets of size \(\widetilde{O}\left(n^2/D^3+n\right)\) in time \(\widetilde{O}\left(mn/D^2\right)=\widetilde{O}\left(n^3/D^2\right)\) whenever \(D=O(\sqrt{n})\) \[KP23a\] (\[KP22a\]’s running time is the same for dense graphs). As an application of Theorem 1.6, we compute shortcut-sets in dense graphs of diameter _D_ and size \(\widetilde{O}\left(n^2/D^3+n\right)\) in time \(\widetilde{O}\left(\mathsf{T}_\mathrm{MPP}\left(n/D^2,n,n|D,1\right)\right)\) (see Theorem 6.6). Our algorithm is faster than \[KP23a\] for all values of \(D=O(\sqrt{n})\), as illustrated in Figure 2. For the important case _D=n_<sup>1/3</sup>, our running time is _O(n_<sup>2.064</sup>).

Comparison of Algorithms for computing Shortcut Sets
This Work Kogan and Parter
2.35
2.30
2.25
2.20
Runtime exponent
2.15
2.10
2.05
2.00
0.0
0.1
0.2 Diameter exponent
0.3
0.4
0.5

Figure 2: Comparison of running times of algorithms for computing shortcut sets in dense graphs with \(m=\Theta(n^2)\) with diameter _D=n<sup>x</sup>_ for \(x\le 0.5\). The algorithm of Kogan and Parter \[KP22b, KP23a\] is the minimum of \(\widetilde{O}\left(n^\omega\right)\) and \(\widetilde{O}\left(n^3/D^2\right)=\widetilde{O}\left(n^{3-2x}\right)\). See Section A for a discussion on known upper bounds on \(\mathsf{T}_\mathrm{MPP}\left(n_1,n_2,n_3|B_1,B_2\right)\).

