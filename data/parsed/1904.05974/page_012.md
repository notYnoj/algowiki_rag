A stable matching in _G_<sup>∗</sup> is _B_-perfect and a matching of maximum size in _G_<sup>∗</sup>. Hence, all popular matchings in _G_<sup>∗</sup> match the same set of vertices: this is the set \((A\cup B)\backslash U^*\). Thus _U_<sup>∗</sup> is the set of unpopular vertices in _G_<sup>∗</sup>. We now define a subclass of dominant matchings in _G_<sup>∗</sup>.

**Definition 3** _A popular matching T in_ \(G^*=(A\cup B,E^*)\) _is extra-dominant if T admits a witness_ \(\alpha\) _such that_ \(\alpha_v\in\{\pm 1\}\) _for every popular vertex v and_ \(\alpha_a=-1\) _for all_ \(a\in U_A\backslash U^*\).

We call a witness \(\alpha\) as described in Definition 3 extra-dominant. Note that every extra-dominant matching is also dominant, by the LP-based characterization of dominant matchings (given by Theorem 7). The following lemmas illustrate the relationship between (quasi-)popular matchings in _G_ and extra-dominant matchings in _G_<sup>∗</sup>.

**Lemma 2.** _For any popular matching M in G, the matching M_<sup>∗</sup> _is extra-dominant in G_<sup>∗</sup>.

**Lemma 3.** _For any extra-dominant matching T in G_<sup>∗</sup>, \(T\cap E\) _is a quasi-popular matching in G._

## 3.2 Extended tions of the Dominant and Extra-Dominant Matching Polytopes

We will now show extended formulations of the dominant and extra-dominant matching polytopes of _G_<sup>∗</sup>. For any fractional matching **_x_** in _G_<sup>∗</sup>, define the weight function _c<sub>x</sub>_ on any edge (_a,b_) of _G_<sup>∗</sup> as follows:

\(c_x(a,b)=\left\{\begin{array}{ c c }
1 & \text{if}a\in U^*; \\
\mathfrak{wt}_x(a,b) & \text{otherwise}.
\end{array}\right.\)

See (1) for the definition of wt_<sub>x</sub>(a,b_). Observe that _c<sub>x</sub>_ is an affine function of **_x_**.

Call an edge _e_ in _G_<sup>∗</sup> _dominant_ if there is some dominant matching in _G_<sup>∗</sup> that contains _e_. Let \(E_D^*\) denote the set of dominant edges in _G_<sup>∗</sup>. The set \(E_D^*\) can be determined in linear time, see \[11\]. Consider the polytope F<sub>_G_<sup>∗</sup></sub> in variables **_x_** and \(\alpha\) defined by constraints (7)-(14) given below. Here \(\delta^*(u)\) is the set of edges incident to vertex _u_ in _G_<sup>∗</sup>.

\(\sum_{u\in A\cup B}\alpha_u=0\) (7) \(\sum_{e\in\delta^*(u)}x_e=1\forall u\in(A\cup B)\backslash U^*\) (11) \(\alpha_a+\alpha_b\ge c_x(a,b)\forall(a,b)\in E^*\) (8) \(\alpha_u\ge-1\forall u\in A\cup B\) (9) \(\alpha_a=0\forall a\in U^*\) (10) \(\alpha_a=-1\forall a\in U_A\backslash U^*.\) (14)

**Theorem 8.** _The polytope_ F<sub>_G_<sup>∗</sup></sub> _is an extension of the extra-dominant matching polytope of G_<sup>∗</sup>.

Thus linear programming on F<sub>_G_<sup>∗</sup></sub> gives a min-cost extra-dominant matching in _G_<sup>∗</sup>. Let C<sub>_G_<sup>∗</sup></sub> be the polytope defined by constraints (7)-(13). Theorem 9 will help us prove Theorem 8.

**Theorem 9.** C<sub>_G_<sup>∗</sup></sub> _is an extension of the dominant matching polytope of G_<sup>∗</sup>_. Moreover, the extreme points of_ C<sub>_G_<sup>∗</sup></sub> _are all and only the vectors_ \((I_M,\alpha)\)_, where I<sub>M</sub> is the incidence vector of a dominant matching M in G_<sup>∗</sup> _and_ \(\alpha\) _is a dominant witness of M._

The proof of Theorem 9 uses the extension of the popular fractional matching polytope described in Section 2.1. Recall the integrality of this extension E_<sub>H</sub>_ in a marriage instance _H_ that admits a _perfect_ stable matching \[27, Theorem 2\]. We apply this with _H=G_<sup>∗</sup>\\_U_<sup>∗</sup> and the polytope C<sub>_G_<sup>∗</sup></sub> is realized as a face of an extension of E_<sub>H</sub>_. The proofs of Theorem 8 and Theorem 9 are given in Section 3.4.

