<tbc>this new stable marriage, each woman (resp. man) is better off (resp. worse off) than before eliminating the rotation.

Once an exposed rotation has been identified and eliminated, then one or more rotations may be exposed in the resulting (further reduced) shortlists. This process may be repeated, and once all rotations have been eliminated, we obtain the woman optimal stable marriage. A rotation \(\pi\) is said to be a predecessor of a rotation \(\rho\), denoted by \(\pi<\rho\), if \(\rho\) cannot be exposed in the men shortlists before \(\pi\) is eliminated. This notion of predecessors makes it possible to define what is called the rotation poset \((P,\le)\) where _P_ is the set of all rotations and \(\le\) is the precedence relation that we have just mentioned. A closed set in a poset \((P,\le)\) is a subset _R_ of _P_ such that \(\rho\in R,\pi<\rho\Rightarrow\pi\in R\).

The following theorem is crucial to understand the importance of the rotation poset.

**Theorem 1** _\[Irving and Leather, 1986\] The stable marriages of a given stable marriage instance are in one-to-one correspondence with the closed subsets of the rotation poset._

In this correspondence, each closed subset _R_ represents the stable marriage obtained by eliminating the rotations in _R_ starting from **x**_<sup>m</sup>_.

The rotation poset can be represented as a directed acyclic graph, with the rotations as nodes and an arc from \(\pi\) to \(\rho\) iff \(\pi\) is an immediate predecessor of \(\rho\) (i.e., \(\pi<\rho\) and there is no rotation \(\sigma\) such that \(\pi<\sigma<\rho\)). Note that this graph has at most _n(n_-1)/2 nodes, i.e., there are at most _n(n_-1)/2 rotations \[Irving _et al._, 1987\]. Indeed, there are at most _n_<sup>2</sup>-_n_ pairs that can be involved in rotations (the _n_ pairs of **x**_<sup>w</sup>_ cannot be involved in a rotation). Each pair belong to at most one rotation and there are at least two pairs in each rotation. We will take advantage of the rotation poset in multiple places in the paper. Importantly, note that the rotation poset (actually a subgraph whose transitive closure is the rotation poset) can be generated in _O(n_<sup>2</sup>) \[Gusfield and Irving, 1989\].

**Example 4** _For instance, with the preferences of Example 1, the rotations and their immediate predecessors are given in the following table._

This rotation poset shows that there are (potentially many) other stable marriages than the man-optimal or woman-optimal stable marriages. These other stable marriages are likely to be fairer than **x**_<sup>m</sup>_ and **x**_<sup>w</sup>_ as they are both extreme cases. In order to compute a fair stable

\begin{tabular}{ccc}
Rotation & New pairs & Immediate predecessors \\
\(\rho_1=(4,7),(5,6)\) & (4,6),(5,7) & \\
\(\rho_2=(6,4),(7,5)\) & (6,5),(7,4) & \\
\(\rho_3=(8,8),(9,10),(10,9)\) & (8,10),(9,9),(10,8) & \(\rho_1,\rho_2\) \\
\end{tabular}

P1
P3
P2

Fig. 1: Rotation poset in Example 1.

