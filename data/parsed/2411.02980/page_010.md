Also, we claim that both conditions in Theorems 1.2 and 1.4 satisfy the desired structural properties.

**Theorem 3.3.** _Both the random k-SAT instance under the condition in Theorem 1.2 and the random hypergraph coloring instance under the condition in Theorem 1.4 satisfy Condition 3.1 with high probability._

Note that the condition in Theorem 1.2 is below the explicit threshold \(\alpha<1.3836\cdot 2^k/k\), as established in \[FS96, Theorem 1.3\]. Similarly, the condition in Theorem 1.4 falls below the explicit threshold \(\alpha<q^{k-1}lnk\), as given in \[DFG15, Theorem 1.1\]. As a result, the instances described in Theorems 1.2 and 1.4 are satisfiable with high probability under respective conditions. Consequently, Theorems 3.2 and 3.3 together imply Theorems 1.2 and 1.4.

The plan goes as follows: For the rest of this section, we formally define the structural properties and verify that Theorem 3.3 holds. Theorem 3.2 will be proved later in Sections 4 and 5.

We now start to introduce the desired structural properties of the CSP formula. Most of the properties and proofs of random CSP formulas were presented in \[GGGY21, HWY23\] using different parameters. Here, we will adapt the proofs to our parameters and show that all properties hold in the uniform hypergraph model as well.

Let H_<sub>k</sub>_ be the set of all _k_-uniform hypergraphs, and \(\mathcal{H}_{\le k}\) be the set of hypergraphs where each hyperedge contains at most _k_ vertices. Now we can describe the following properties for hypergraphs.

**Property 3.4** (bounded maximum degree)**.** _Given a hypergraph H_=(_V,_E)_. The maximum degree_ \(\Delta=\Delta(H)\) _is at most_ \(4k\alpha+6logn\).

**Property 3.5** (edge expansion)**.** _For_ \(\eta,\rho\in(0,1)\)_, we say a hypergraph_ \(H=(V,\mathcal{E})\in\mathcal{H}_{\le k}\) _satisfies_ \((\eta,\rho)\)_-edge expansion if for any_ \(\ell\le\rho|\mathcal{E}|\) _and any_ \(\ell\) _hyperedges_ \(e_1,\dots,e_\ell\in\mathcal{E}\)_, it holds_

\(\left|\bigcup_{i=1}^\ell e_i\right|\ge(1-\eta)k\ell.\)

**Property 3.6** (bounded neighbourhood growth)**.** _For any_ \(e\in\mathcal{E}\) _and any_ \(\ell\ge 1\)_, the number of connected subsets of hyperedges containing e of size_ \(\ell\) _is at most_ \(n^3(p_2\alpha)^\ell\).

Similar to the approaches in \[GGGY21, HWY23\], a crucial component of our algorithm for random instances involves identifying high-degree vertices, as well as those whose marginal distributions may be significantly affected by high-degree ones. We begin with the identifying subroutine.

**Definition 3.7** (high-degree vertices)**.** Given a hypergraph _H_=(_V,_E) with average degree _d_, and a subset of vertices \(V'\subseteq V\) , let \(\mathrm{HD}(V')\unknown\{v\in V'|\mathrm{deg}(v)\ge p_1\alpha\}\) denote the set of _high-degree_ vertices in \(V'\).

Instance:a hypergraph H=(_V,_E) with average degree _d_;<br>
Input:a set of vertices \(V_0\subseteq V\);<br>
Output:a set of bad vertices V<sub>bad</sub>(V<sub>0</sub>) starting from V<sub>0</sub> and a set of bad hyperedges E<sub>bad</sub>(V<sub>0</sub>);<br>
Initialize \(V_\mathrm{bad}(V_0)\leftarrow\mathrm{HD}(V_0)\) and \(\mathcal{E}_\mathrm{bad}(V_0)=\emptyset\);<br>
while \(\exists e\in\mathcal{E}\backslash\mathcal{E}_\mathrm{bad}(V_0)\) _such that_ \(|e\cap V_\mathrm{bad}(V_0)|>\varepsilon_1k\) do<br>
Update<br>
\(V_\mathrm{bad}(V_0)\leftarrow V_\mathrm{bad}(V_0)\cup e\)<br>
and<br>
\(\mathcal{E}_\mathrm{bad}(V_0)\leftarrow\mathcal{E}_\mathrm{bad}(V_0)\cup\{e\}\)<br>
return V<sub>bad</sub>(V<sub>0</sub>)<br>
and<br>
E<sub>bad</sub>(V<sub>0</sub>)

Throughout, we will use the notation V<sub>bad</sub>=V<sub>bad</sub>(V) and E<sub>bad</sub>=E<sub>bad</sub>(V) if the hypergraph _H_=(_V,_E) is clear from the context. The set of _good vertices_ \(V_\mathrm{good}\unknown V\backslash V_\mathrm{bad}\) and the set of _good constraints_ \(\mathcal{E}_\mathrm{good}\unknown\mathcal{E}\backslash\mathcal{E}_\mathrm{bad}\) is defined to be the set of remaining variables/hyperedges.

**Fact 3.8** (bounded-degree for good vertices)**.** _For every good vertex_ \(v\in V_\mathrm{good}\)_, it holds_ \(\mathrm{deg}(v)\le p_1\alpha\).

**Fact 3.9** (bounded fraction of good vertices)**.** _For every good hyperedge_ \(e\in\mathcal{E}_\mathrm{good}\)_, it holds_ \((1-\varepsilon_1)k\le|e\cap V_\mathrm{good}|\le k\).

**Algorithm 1:** IdentifyBad(V<sub>0</sub>) \[HWY23\]

