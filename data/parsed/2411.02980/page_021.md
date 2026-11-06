(_3)_ _Furthermore, it always holds that_<tbc>

<tbc>\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\cdot\frac{|\Omega^{\mathcal{E}\wedge\sigma}|}{|\Omega^{\mathcal{C}\backslash\{c_0\}}|}=p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\cdot\frac{|\Omega^{\mathcal{F}\wedge\tau}|}{|\Omega^\mathcal{C}|},\)<tbc>

<tbc>_and_

\(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X,p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\le q^{-|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot\left(1-\mathrm{e}q^{-(1-\varepsilon_1)k}\right)^{-|\mathrm{vbl}(T)|p_1\alpha}.\)

_Proof._ Items 1 and 2 are derived directly from Definition 5.1 and the well-definedness ensured in Proposition 5.2, both of which are straightforward to verify.

The equation in Item 3 follows from (9). From the same equation (9), we can further derive that \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X=\mu_\mathcal{C}(\mathcal{F}\wedge\tau)\le\mu_\mathcal{C}(\tau)\) and \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y=\mu_{\mathcal{C}\backslash\{c_0\}}(\mathcal{E}\wedge\sigma)\le\mu_{\mathcal{C}\backslash\{c_0\}}(\sigma)\). Together with Lemma 4.11, these imply the final inequalities in Item 3. □

## 5.2. Setting up the linear program.

Next, we construct a linear program that that mimics the marginal probabilities \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^X\) and \(p_{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)}^Y\).

## 5.2.1. _The coupling tree._

To set up the linear program, we first construct a recursion tree for the coupling procedure \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing)\), truncating it when the size of the witness tree _T_ exceeds _M_.

**Definition 5.4** (_M_-truncated coupling tree)**.** The _M-truncated coupling tree_, denoted \(\mathcal{T}=\mathcal{T}_M(\Phi,c_0)\), is a finite rooted tree, where each node in T corresponds to a tuple \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{V}^\mathrm{cp}\). The tree T is constructed inductively as follows:

(1) The root of T corresponds to \((\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset,\varnothing)\), and has depth 0.<tbc>

(2) For _i_=0,1_,..._, consider all nodes \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\) of depth _i_ in the current tree T .<tbc>

(a) If \(\sigma\) violates E or \(\tau\) violates F or \(\mathcal{E}^\sigma=\mathcal{F}^\tau\) or |_V(T_)|=_M_, then \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) is left as a leaf node in T .<tbc>

(b) Otherwise, if \(\mathcal{F}^\tau\nsubseteq\mathcal{E}^\sigma\), then pick the smallest \(c\in\mathcal{F}^\tau\backslash\mathcal{E}^\sigma\) and add \((\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau,T,\varsigma)\) as a child of \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) in T . Furthermore, for each \(\rho\in[q]^{\mathrm{vbl}(c)}\) and \(\pi=\mathtt{False}(c)\), add \((\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\rho)\) as a child of \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) in T .<tbc>

(c) Otherwise, it holds that \(\mathcal{F}^\tau\subseteq\mathcal{E}^\sigma\). Then, pick the smallest \(c\in\mathcal{E}^\sigma\backslash\mathcal{F}^\tau\) and add \((\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau,T,\varsigma)\) as a child of \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) in T . Furthermore, for each \(\pi\in[q]^{\mathrm{vbl}(c)}\) and \(\rho=\mathtt{False}(c)\), add \((\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho,T\oplus c^O,\varsigma\wedge\pi)\) as a child of \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) in T .

Let L denote the set of leaf nodes in T . We further define the following sets of leaf nodes:

\(\bullet\) \(\mathcal{L}_\mathrm{coup}\unknown\{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}|\mathcal{E}^\sigma=\mathcal{F}^\tau\}\) as the set of "coupled" leaf nodes in T ;<tbc>

\(\bullet\) \(\mathcal{L}_\mathrm{run}\unknown\{(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in\mathcal{L}||V(T)|=M\}\) as the set of "truncated" leaf nodes in T ;<tbc>

\(\bullet\) \(\mathcal{L}_\mathrm{valid}\unknown\mathcal{L}_\mathrm{run}\cup\mathcal{L}_\mathrm{coup}\) as the set of "valid" leaf nodes in T ;<tbc>

\(\bullet\) \(\mathcal{L}_\mathrm{invld}\unknown\mathcal{L}\backslash\mathcal{L}_\mathrm{valid}\) as the set of "invalid" leaf nodes in T .

**Proposition 5.5.** _For any satisfiable_ \(\Phi=(V,[q],\mathcal{C})\)_, any_ \(c_0\in\mathcal{C}\) _and_ \(M\ge 1\)_, the M-truncated coupling tree_ \(\mathcal{T}=\mathcal{T}_M(\Phi,c_0)\) _has a depth of at most_ \(M\Delta k+1\) _and a branching number of at most q_<sup>2_k_</sup>_, where_ \(\Delta=\Delta(\Phi)\) _is the maximum degree of_ \(G_\Phi\).

_Proof._ By contradiction, assume there exists a node \((\mathcal{E}',\mathcal{F}',\sigma',\tau',T',\varsigma')\in V(\mathcal{T})\) with depth \(M\Delta k+2\). We track the size of \(\mathcal{E}^\sigma\triangleup\mathcal{F}^\tau\) along the path from the root to \((\mathcal{E}',\mathcal{F}',\sigma',\tau',T',\varsigma')\), denoting this size by _t_. Initially, by Definition 5.6, we have _t_=1. At each intermediate node \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in V(\mathcal{T})\) along the path: we either add some constraint _c_ into E or F, reducing _t_ by 1, or we assign values to \(\sigma\) and \(\tau\) on vbl(_c_), which increases _t_ by at most \(k\Delta-1\) (since at most \(k\Delta\) new elements can be added into \(\mathcal{E}^\sigma\triangleup\mathcal{F}^\tau\), and _c_ is removed from \(\mathcal{E}^\sigma\triangleup\mathcal{F}^\tau\)). In the latter case, the size of _T_ grows by one according to Proposition 4.5. Let _i_ denote the number of times this latter operation is executed.

Since the depth of \((\mathcal{E}',\mathcal{F}',\sigma',\tau',T',\varsigma')\) is \(M\Delta k+2\), the above step is repeated for \(M\Delta k+2\) times. Finally, at the node \((\mathcal{E}',\mathcal{F}',\sigma',\tau',T',\varsigma')\), we still have \(t=|\mathcal{E}^{\prime\sigma^\prime}\triangleup\mathcal{F}^{\prime\tau^\prime}|\ge 0\). Therefore,

\((k\Delta-1)\cdot i+1-(M\Delta k+2-i)\ge 0,\)

This implies that \(|T'|=i>M\), which contradicts the truncation condition in Item 2a of Definition 5.4.

Finally, it is easy to observe that each node in T has at most _q_<sup>2_k_</sup> children. □

