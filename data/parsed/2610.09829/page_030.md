the entries \(\Pi_\mathcal{P}(\beta,h')\), for each descendant \(\beta\) of \(\alpha\) in T , where \(\beta\neq\alpha\) and \(h'\in[k]\). To compute \(\Pi_\mathcal{P}(\alpha,h)\), we would have ideally liked to query entries for descendant of \(\alpha\) that belongs to a (fixed unknown) optimal solution, which we formalize in the next definition (also see Figure 14). However, as the number of nodes in T may not be bounded by a function of _k_, to achieve the running time we desire, the above type of queries will not be possible for us, due to which we will need a slightly more non-trivial notion of "relevant" descendants.

**Definition 5.7.** Let C be a solution for \(\Pi_\mathcal{P}(\alpha,h)\), where \(\alpha\) is a non-leaf node of T and _h\>_1. A node \(\beta\in\mathcal{C}\backslash\{\alpha\}\) is a _solution descendant_ of \(\alpha\) in C if there is no \(\beta'\in\mathcal{C}\backslash\{\alpha,\beta\}\) that lies on the unique path between \(\alpha\) and \(\beta\) in T .

For an illustration of the above definition, see Figure 14. The following observation (which will be useful later) relates \(\Pi_\mathcal{P}(\alpha,h)\) to the entries of the (unknown) solution descendants of \(\alpha\) for some fixed (unknown) optimal solution, and it easily follows from Definition 5.6.

Recall that for a node \(\gamma\) of T , \(\mathcal{T}_\gamma(G)\) is the subtree of T rooted at \(\gamma\).

**Observation 5.1.** _Let_ C _be a solution for_ \(\Pi_\mathcal{P}(\alpha,h)\)_, where_ \(\alpha\) _is a non-leaf node of_ T _and h\>_1_. Furthermore, let_ \(\{\beta_1,\beta_2,\dots,\beta_b\}\) _be the set of solution descendants of_ \(\alpha\) _in_ C_. For each_ \(i\in[b]\)_, let_ \(\mathcal{C}_i=\mathcal{C}\cap V(\mathcal{T}_{\beta_i})\)_, and h<sub>i</sub>_=|C_<sub>i</sub>|. Then the following holds._

1. \(\{\{\alpha\},\mathcal{C}_1,\mathcal{C}_2,\dots,\mathcal{C}_b\}\) _is a partition of_ C.<tbc>

2. _For each_ \(i\in[b]\), \(h_i\ge 1\)_, and_ \(\sum_{i=1}^bh_i=h-1\).<tbc>

_3._ _For any_ \(i\in[b]\)_, replacing_ C_<sub>i</sub> by any optimal solution_ \(\mathcal{C}_i^*\) _for_ \(\Pi_\mathcal{P}(\beta_i,h_i)\) _yields a solution_ \(\mathcal{C}^*=(\mathcal{C}\backslash\mathcal{C}_i)\cup\mathcal{C}_i^*\) _for_ \(\Pi_\mathcal{P}(\alpha,h)\)_, where_ \(w(\mathcal{C}^*\cup\mathcal{P})\ge w(\mathcal{C}\cup\mathcal{P})\).<tbc>

_4._ _For each_ \(i\in[b]\), C_<sub>i</sub> is a solution for_ \(\Pi_\mathcal{P}(\beta_i,h_i)\)_. Moreover, if_ C _is an optimal solution for_ \(\Pi_\mathcal{P}(\alpha,h)\)_, then_ C_<sub>i</sub> is an optimal solution for_ \(\Pi_\mathcal{P}(\beta_i,h_i)\).<tbc>

a
γ5
β1
= 1
81
γ5
γ2
γ3
β2
β3
β4
= =
β5
γ5

Figure 14: The picture illustrates, for a node \(\alpha\) of T , the subtree \(\mathcal{T}_\alpha\), and a solution C for \(\Pi_\mathcal{P}[\alpha,7]\) using red border nodes. The nodes labelled \(\beta_1,\beta_2,\beta_3,\beta_4\), and \(\beta_5\) are solution descendants of \(\alpha\) in C, and the nodes \(\gamma_1,\gamma_2,\gamma_3,\gamma_4\), and \(\gamma_5\) are their representatives, respectively. We also illustrate a maximal degree 2 path below \(\gamma_5\) from \(\gamma_5^\mathsf{s}\) to \(\gamma_5^\mathsf{t}\) (relevant for Section 5.4).

