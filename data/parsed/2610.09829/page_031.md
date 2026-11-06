<tbc>_Proof._ The first statement follows from Definition 5.7, since every cycle in \(\mathcal{C}\backslash\{\alpha\}\) belongs to the subtree of exactly one solution descendant of \(\alpha\). Moreover, the above implies the second statement. The fourth statement is implied by the third one, so we focus on the proof of third item.

As \(\beta_i\in\mathcal{C}_i\cap\mathcal{C}_i^*\), for any cycle \(\delta\in\mathcal{C}^*\backslash\mathcal{C}_i^*\) and \(\delta'\in\mathcal{C}_i^*\), \(E(\delta\cap\delta')\subseteq E(\beta_i\cap\delta')\) (see Lemma 5.2), and thus we can conclude that C<sup>∗</sup> is a solution for \(\Pi_\mathcal{P}(\alpha,h)\). Moreover, \(w(\mathcal{C}^*\cup\mathcal{P})\ge w(\mathcal{C}\cup\mathcal{P})\) follows from \(w(\mathcal{C}_i^*\cup\mathcal{P})\ge w(\mathcal{C}_i\cup\mathcal{P})\).

We will introduce another definition that helps us compute \(\Pi_\mathcal{P}(\alpha,h)\) using at most 2<sup>O(_k_)</sup> queries, and to this end we construct some sets of marked nodes from T as follows. Recall the number of leaves in T is bounded by 4_k_, and thus the number of degree three nodes in T is at most 4_k_. For \(\gamma\in V(\mathcal{T})\), let \(\mathcal{M}_\gamma\) be the nodes from \(\mathcal{T}_\gamma(G)\) containing: i) each leaf, ii) each node of degree at least three, iii) for each maximal path in \(\mathcal{T}_\gamma(G)\) where all nodes are of degree exactly 2, the endpoints of these paths that are closest to \(\gamma\), and iv) all the children of \(\gamma\). We have the following simple observation, which immediately follows from the above definition.

**Observation 5.2.** _For any node_ \(\gamma\) _of_ T _, we have_ \(|\mathcal{M}_\gamma|\le 16k\).

Intuitively, to compute \(\Pi_\mathcal{P}(\alpha,h)\), instead of querying over the solution descendants of \(\alpha\) in a (fixed unknown) optimal solution, we will manage with the "closest" descendants from the set \(\mathcal{M}_\alpha\). We formalize this in the next definition (see Figure 14).

**Definition 5.8.** Let C be a solution for \(\Pi_\mathcal{P}(\alpha,h)\), where \(\alpha\) is a non-leaf node of T and _h\>_1. Consider a solution descendant \(\beta\) of \(\alpha\) in C. The \((\alpha,\mathcal{C})\)_-representative_ (or simply, _representative_, when the context is clear), \(\gamma\) for \(\beta\) is the vertex from \(\mathcal{M}_\alpha\) that is closest to \(\beta\) in the unique path between \(\beta\) and \(\alpha\) in T .

For \(\delta\in V(\mathcal{T})\), a set \(R\subseteq\mathcal{M}_\delta\) (\(\subseteq V(\mathcal{T}_\delta)\)) is \(\delta\)_-lineage-free_ (or, _lineage-free_, if the context is clear) if for distinct \(\gamma,\gamma'\in R\), neither \(\gamma\) is a descendant of \(\gamma'\), nor \(\gamma'\) is a descendant of \(\gamma\), in \(\mathcal{T}_\delta\). Consider a \(\delta\)-lineage-free set _R_ and \(\gamma\in R\). We let \(\Gamma_{\delta,R,\gamma}\) be the set of cycles in \(R\cup\{\delta\}\) (other than \(\gamma\)), that<tbc>

8
Y5
Y4
Y3
Y2
Y1
Y

Figure 15: Illustration of the _relevant-subset_. Here we have a \(\delta\)_-lineage-free_ set \(R=\{\gamma,\gamma_1,\gamma_2,\gamma_3,\gamma_4,\gamma_5\}\). For the cycle \(\gamma\) we have \(\Gamma_{\delta,R,\gamma}=\{\delta,\gamma_1,\gamma_2,\gamma_3\}\)

