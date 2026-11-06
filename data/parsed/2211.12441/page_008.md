We think of coloring the vertices of the permutahedron with their values under \(\Pi\) and make use of the subgraph with the same vertex set but only containing the monochromatic edges, i.e., the edges whose end points have the same value under \(\Pi\). We also consider the the complementary subgraph containing all bichromatic edges.

**Definition 15 (permutahedron graph,** \(G(\cdot)\)**,** \(\overline{G}(\cdot)\)**).** _Let_ \(\Pi\) _be a computational problem in the comparison-query model on a set X of items. The_ permutahedron graph _of_ \(\Pi\)_, denoted_ \(G(\Pi)\)_, has the rankings of X as vertices, and an edge between two rankings_ \(\rho_1\) _and_ \(\rho_2\) _if_ \(\Pi(\rho_1)=\Pi(\rho_2)\) _and there exists an adjacent- rank transposition such that_ \(\rho_2=\tau\rho_1\)_. The_ complementary permutahedron graph _of_ \(\Pi\)_, denoted_ \(\overline{G}(\Pi)\)_, is defined similarly by replacing the condition_ \(\Pi(\rho_1)=\Pi(\rho_2)\) _by its complement,_ \(\Pi(\rho_1)\neq\Pi(\rho_2)\).

Our first technique looks at degrees in the complementary permutahedron graph \(\overline{G}(\Pi)\), and more specifically at the _average degree_ \(deg_{avg}(\overline{G}(\Pi))\doteq\mathbb{E}(deg_{\overline{G}(\Pi)}(\rho))\), where the expectation is with respect to a uniform choice of the ranking \(\rho\). Our second technique looks at the connected components of the permutahedron graph \(G(\Pi)\).

## Connectivity.

Our second technique is reminiscent of a result in algebraic complexity theory, where the number of execution traces of an algorithm for a problem \(\Pi\) in the algebraic comparison- query model is lower bounded in terms of the number of connected components that \(\Pi\) induces in its input space R_<sup>n</sup>_ \[BO83\]. In the comparison-query setting, we obtain the following lower bound.

**Lemma 16 (Connectivity Lemma).** _For any problem_ \(\Pi\) _in the comparison-query model,_ \(\mathrm{D}(\Pi)\) _is at least the number of connected components of_ \(G(\Pi)\).

The Connectivity Lemma allows for a simple and unified exposition of many of the known lower bounds. For counting inversions and inversion parity the argument goes as follows. Every adjacent- rank transposition changes the number of inversions by exactly one (up or down), and therefore changes the output of \(\Pi\), so all _n_! vertices in \(G(\Pi)\) are isolated. This means that any algorithm for \(\Pi\) actually needs to sort and has to make at least log<sub>2</sub>(_n_!) queries. See Section 7 for a proof of the Connectivity Lemma and more applications to classical problems, including the \(\Omega(n)\) lower bound for median finding.

The Connectivity Lemma also enables us to establish strong lower bounds for inversion minimization on special types of trees _T_, namely those of Theorem 8 and the Mann-Whitney instances in Theorem 9, closely related to counting inversions. Both theorems involve an analysis of the size of the connected component of a random ranking \(\rho\) in \(G(\Pi_T)\), and Theorem 8 uses the delicate parity conditions of its statement to keep \(G(\Pi_T)\) as sparse as possible. See Section 8 for more details, including a more general property that guarantees the required sparseness (the partition property from Definition 46) and the resulting lower bound for a generic problem \(\Pi\) that satisfies the property (Lemma 49).

(3,1,2,4)
(4,1,2,3)
(4,2,1,3)
(3,2,1,4)
(4,1,3,2)
(2,1,3,4)
(4,3,1,2)
(2,3,1,4)
(3,1,4,2)
(4,2,3,1)
(2,1,4,3)
(4,3,2,1)
(1,2,3,4)
(3,4,1,2)
(1,3,2,4)
(2,4,1,3)
(3,2,4,1)
(1,2,4,3)
(3,4,2,1)
(1,4,2,3)
(2,3,4,1)
(1,3,4,2)
(2,4,3,1)
(1,4,3,2)

Figure 4: Permutahedron for _n_=4 items

