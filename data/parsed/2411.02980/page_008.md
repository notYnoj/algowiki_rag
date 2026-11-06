<tbc>assignment \(\sigma\) and any \(S\subseteq\Lambda(\sigma)\), we use \(\sigma_S\) to denote \(\otimes_{v\in S}\sigma(v)\). We further write \(\sigma_v=\sigma_{\{v\}}\) for \(v\in V\) .

For any two assignments \(\sigma,\tau\) such that \(\Lambda(\sigma)\cap\Lambda(\tau)=\emptyset\), we define \(\sigma\wedge\tau\in[q]^{\Lambda(\sigma)\cup\Lambda(\tau)}\) as the concatenation of \(\sigma\) and \(\tau\) such that for any \(v\in\Lambda(\sigma)\cup\Lambda(\tau)\),

\((\sigma\wedge\tau)(v)=\left\{\begin{array}{ c c }
\sigma(v) & v\in\Lambda(\sigma), \\
\tau(v) & v\in\Lambda(\tau).
\end{array}\right.\)

We will use \(\varnothing\) to specifically denote an empty assignment, distinguishing from the empty set \(\emptyset\).

## 2.1.2. Notations for events and probability measures.

We begin by specifying some notations for events and probability measures related to the CSP.

**Definition 2.1** (simple notations for events)**.** For simplicity of notation, we will use:

\(\bullet\) a constraint \(c\in\mathcal{C}\) to denote the event that this constraint is satisfied;<tbc>

\(\bullet\) a subset of constraints \(\mathcal{E}\subseteq\mathcal{C}\) to denote the event that all constraints in E are satisfied;<tbc>

\(\bullet\) a partial assignment \(\sigma\) to denote the event that the assignment on \(\Lambda(\sigma)\) is precisely \(\sigma\).

Note that under this definition, the notation \(\sigma\wedge\tau\) as a concatenation of assignments defined previously is consistent with its interpretation as an event, where \(\sigma\wedge\tau\) is considered as the logical "and" of the two events \(\sigma\) and \(\tau\).

We use P to denote the uniform product distribution over the space \[_q_\]_<sup>V</sup>_. We use \(\mu=\mu_\Phi\) to denote the distribution over all satisfying assignments of \(\Phi\) induced by P, i.e.

\(\mu_\Phi\unknown\mathcal{P}\left(\cdot|\mathcal{C}\right).\)

\(\mu_\Phi\) is well-defined only when \(\Phi\) is satisfiable.

When the variable set _V_ and the domain \[_q_\] are clear, we define the following notations for (conditional) distributions for a given set of constraints E defined over _V_ , and some assignment \(\sigma\) defined over \(\Lambda(\sigma)\):

\(\mu_\mathcal{E}\unknown\mathcal{P}(\cdot|\mathcal{E}),\mu_\mathcal{E}^\sigma\unknown\mathcal{P}(\cdot|\mathcal{E}\wedge\sigma).\)

For a probability distribution \(\mu\) and some subset of variables \(\Lambda\subseteq V\) , we use \(\mu_\Lambda\) to denote the marginal distribution induced by \(\mu\) on \(\Lambda\). We use commas to separate multiple subscripts; for example, we use \(\mu_{\mathcal{E},\Lambda}^\sigma\) to denote the marginal distribution induced by \(\mu_\mathcal{E}^\sigma\) on \(\Lambda\).

## 2.1.3. Pinned formula and pinned constraints.

For a subset of variables \(\Lambda\subseteq V\) and a partial assignment \(\sigma\in[q]^\Lambda\) specified on \(\Lambda\), the pinned formula \(\Phi=(V,[q],\mathcal{C})\) under \(\sigma\), denoted by \(\Phi^\sigma=(V^\sigma,[q],\mathcal{C}^\sigma)\), is a new CSP formula such that \(V^\sigma=V\backslash\Lambda(\sigma)\), and the \(\mathcal{C}^\sigma\) is obtained from C by:

(1) replacing each original constraint \(c\in\mathcal{C}\) with the corresponding pinned constraint \(c^\sigma\), where \(\text{vbl}(c^\sigma)=\text{vbl}(c)\backslash\Lambda(\sigma)\) and \(c^\sigma(\tau)=c(\tau\wedge\sigma_{\Lambda(\sigma)\cap\text{vbl}(c)})\) for any \(\tau\in[q]^{\text{vbl}(c^\sigma)}\);<tbc>

(2) removing all the resulting constraints that have already been satisfied.

Whenever a pinning \(\sigma\) is applied to a CSP formula \(\Phi=(V,[q],\mathcal{C})\), we always assume that \(\sigma\) does not violate any constraint in C. Under this assumption, \(\Phi^\sigma\) is always well-defined, and we have \(\mu_{\Phi^\sigma}=\mu_{V\backslash\Lambda(\sigma)}^\sigma\). We use C<sup>∗</sup> to denote the set of all possible constraints obtained from pinning some constraint in C with a non-violating \(\sigma\), including the unpinned constraints in C. Finally, for each (possibly pinned) constraint \(c\in\mathcal{C}^*\), we use _c<sup>O</sup>_ to denote its original unpinned constraint in C.

## 2.1.4. The incidence hypergraph.

We define the underlying _incidence hypergraph_ of CSP formulas as follows.

**Definition 2.2** (incidence (hyper-)graphs for variables and constraints)**.** Given a CSP formula \(\Phi=(V,[q],\mathcal{C})\) , we define two incidence (hyper-)graphs for variables and constraints respectively:

\(\bullet\) We define \(H_\Phi=(V,\mathcal{E})\) to be the hypergraph (with multiple edges allowed), where _V_ is the set of variables in \(\Phi\), and \(\mathcal{E}=\{\text{vbl}(c)|c\in\mathcal{C}\}\).<tbc>

\(\bullet\) Let \(G_\Phi=\text{Lin}(H_\Phi)\) to denote the line graph of \(H_\Phi\), namely, the vertices in \(G_\Phi\) are clauses in \(\Phi\), and two clauses _c_<sub>1</sub>_,c_<sub>2</sub> are adjacent in \(G_\Phi\) if and only if \(\text{vbl}(c_1)\cap\text{vbl}(c_2)\neq\emptyset\).<tbc>

