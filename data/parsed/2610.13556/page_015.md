<tbc>The endpoints of a maximum matching form a vertex cover: otherwise an edge with both endpoints uncovered could be added to the matching. This gives the first cover bound. Moreover, a matching of size _q_ in <o>_G_</o> supplies _q_ disjoint nonadjacent pairs in _G_. Giving each pair one color and every remaining vertex its own color gives \(\chi(G)\le n-q\). Thus \(\nu(\overline{G})\le n-\chi(G)\le 2t\) in the second case, and the same endpoint argument gives its cover bound. Finally, \(B_\mathrm{w}(G)\le B(G)\). □

## 5.2. Descriptions of colorings by types.

Let \(U\subseteq V(G)\), with |_U_|=_s_, and suppose that _V(G_)\\_U_ is either an independent set or a clique. For a vertex \(v\notin U\), define its type to be \(\tau(v)=N_G(v)\cap U\). Write \(V_\tau\) for the vertices of type \(\tau\) and \(n_\tau=|V_\tau|\), keeping only nonempty types. There are at most 2_<sup>s</sup>_ types. Any permutation fixing _U_ pointwise and preserving each \(V_\tau\) is an automorphism of _G_; let \(\Gamma\) be the group of these permutations.

For a finite label set _L_, describe a map \(x:V(G)\rightarrow L\) by its restriction to _U_, called its _core map_, and by the vectors

\(\mathbf{x}_\tau=(x_{\tau i})_{i\in L},x_{\tau i}=|V_\tau\cap x^{-1}(i)|.\)

Two maps have the same description if and only if an element of \(\Gamma\) takes one to the other. The next observation is the reason that descriptions can replace individual words in a repair problem.

**Lemma 5.4.** _Let_ A _and_ C _be descriptions of maps_ \(x,y:V(G)\rightarrow L\)_. Define_

\(\delta(\mathcal{A},\mathcal{C})=|\{u\in U:x(u)\neq y(u)\}|+\sum_\tau\left(n_\tau-\sum_{i\in L}\mathrm{min}\{x_{\tau i},y_{\tau i}\}\right).\)

_For every fixed realization x of_ A_, this is the minimum Hamming distance from x to a realization of_ C.

_Proof._ The labels on _U_ are fixed. In \(V_\tau\), at most \(\mathrm{min}\{x_{\tau i},y_{\tau i}\}\) vertices can receive label _i_ in both maps. These upper bounds can be achieved simultaneously: for each _i_, match that many occurrences of _i_ in _y_ to occurrences of _i_ in the fixed map _x_, and then biject the remaining positions arbitrarily. Such bijections can be chosen independently in each type. The displayed formula follows by subtracting the maximum number of agreements from _n_. □

In particular, if a collection of permitted repairs is invariant under \(\Gamma\), the minimum repair distance depends only on the description of the disturbed word. The minimum is computed by minimizing \(\delta\) over the descriptions of permitted repairs.

## 5.3. Graphs with a small vertex cover.

**Proposition 5.5.** _Given a vertex cover U of size s, the values B(G_) _and B_<sub>w</sub>(_G_) _can be computed in time g(s_)(_n_+1)<sup>_O_(1)</sup>_, for a computable function g._

_Proof._ Put _I=V(G_)\\_U_. Since _I_ is independent, \(k=\chi(G)\le s+1\). We first compute _k_. For each _j_=1_,...,s_+1, enumerate the proper maps \(\varphi:U\rightarrow[j]\). Such a map extends to a proper _j_-coloring of _G_ if and only if each nonempty type \(\tau\) has a color outside \(\varphi(\tau)\). Indeed, all vertices of a type can be assigned any one such color. The first successful value of _j_ is _k_.

Direct enumeration of the type counts would give an exponent depending on _s_. Instead, we express the threshold condition by a short formula in Presburger arithmetic: integer linear inequalities and congruences with fixed coefficients, combined by Boolean operations and quantifiers. Effective quantifier elimination converts such a formula into an equivalent quantifier-free one. We use this established result, not its quantitative refinements; see Haase et al. \[11, Corollary 3.2\]. Universal quantifiers can be eliminated by negation.

Include all 2_<sup>s</sup>_ types, including empty ones. Introduce free variables \(\mathbf{N}=(N_\tau)_{\tau\subseteq U}\) for their sizes and a free threshold variable \(\ell\). These variables are not yet assigned their input values.

