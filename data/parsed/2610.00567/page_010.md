## 5 Faster Algorithms for Small Patterns

For detecting induced isomorphisms, simply constructing the homomorphism polynomial using Theorem 1 is not sufficient. As described in Section 4, we also have to show existence of decompositions that avoids automorphisms. In this section, we do that for many small pattern graphs. Note that since (_p,q_)- width tree decompositions are tree decompositions \(p+2q\ge w+1\) where _w_ is the treewidth. So for a non-tree, five vertex pattern, the best we can hope for is _p_=1_,q_=1. We show that there are five 5-vertex patterns that have (1,1)-width tree decompositions and can be detected in \(\widetilde{O}(nm)\)-time.

**Theorem 2.** _Given an n-vertex, m-edge host graph H as input, there are_ \(\widetilde{O}(nm)\)_- time algorithms to detect induced subgraphs for the five_ 5_-vertex graphs G05, G09, G12 to G14 in  1 and in Figure 1._

_Proof._ By the method in Section 4, to prove that a 5-vertex pattern _G_ has an \(\widetilde{O}(nm)\)-time algorithm, it is sufficient to provide a (1,1)-decomposition and the automorphism avoiding conditions for that tree decomposition for all 5-vertex patterns \(G'\) that contain _G_ as a subgraph an odd number of times.

1 lists all 5-vertex graphs by specifying their adjacency matrix(in the _Adjacency_ column) as follows: Assume the vertices are labeled 0_,...,_4, then the first bit is for the edge {0,1}, the second for {0,2} and so on until the {3,4} edge. The number of automorphisms is given in the _#Aut_ column. All tree decompositions are path decompositions. So we specify the path of bags in the _t.d._ column. The _Checks_ column specifies conditions that have to be checked failing which we should eliminate the corresponding monomials from the homomorphism polynomial.The - represents that the graph occurs an odd number of times in the _K_<sub>4</sub> minor graph and hence cannot be detected using this method. The ∼ represents that the even number of occurences in the graph cannot be avoided by using any checks from the bags. Finally, the last column _#AutRem_ specifies the number of automorphisms that will remain after these checks are applied.

The \(G_i\times G_j\) entry of  2 specifies the number of _G<sub>i</sub>_-subgraphs in _G<sub>j</sub>_. It contains all 21 connected 5-vertex patterns. The graphs G16 to G21 have a _K_<sub>4</sub>- minor (marked by a <sup>_K_<sub>4</sub></sup> superscript) and therefore cannot have a (1,1)-width tree decomposition. The graphs G07 and G08 have (1,1)-width tree decompositions but there are no checks (marked by <sup>?</sup> superscript) that can be done to make the number of remaining automorphisms odd. Now, for any graph _G_ that is contained in one of G07, G08, G16-21 an odd number of times, we do not have \(\widetilde{O}(nm)\)-time algorithms (marked by <sup>∗</sup> superscript). For the remaining 5 graphs G05, G09, G12-14 (See Figure 1), we can use the (1,1)-width tree decompositions and the checks in  1 to obtain \(\widetilde{O}(nm)\)-time algorithms.

\begin{tabular}{ccccc}
**Name** & **Adjacency** & **#Aut t.d.** & **Checks** & **#AutRem** \\
G01 & 0001001011 & 24 124-024-034 & - & - \\
G02 & 0011001010 & 2 034-142 & 1_\<_2 & 1 \\
\end{tabular}

