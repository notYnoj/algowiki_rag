Now fix an arbitrary strategy \(\tau'\) for Player 2 in \(G'\). Using the history correspondence, define a strategy \(\tau\) in _G_ by transporting the choices of \(\tau'\) through the inverse local bijections. This is also a legal history-dependent strategy.

Under these strategy pairs, corresponding finite histories have equal probabilities. At player nodes, this follows from the construction of the strategies; at random nodes, it follows from the probability-preserving coupling. Recall that colors determine the labels of the nodes along a play. Thus the two games induce the same distribution on label sequences, and<tbc>

\(\mathrm{Pr}\big(w(\pi'(\sigma',\tau'))\in W\big)=\mathrm{Pr}\big(w(\pi(\sigma,\tau))\in W\big).\)

<tbc>Here \(\pi(\sigma,\tau)\) and \(\pi'(\sigma',\tau')\) denote the resulting infinite plays in _G_ and \(G'\), respectively.

Since this holds for every \(\tau'\), we have<tbc>

\(\mathrm{inf}_{\tau^\prime}\mathrm{Pr}\big(w(\pi'(\sigma',\tau'))\in W\big)\ge\mathrm{inf}_\tau\mathrm{Pr}\big(w(\pi(\sigma,\tau))\in W\big).\)

<tbc>Since \(\sigma\) was arbitrary, it follows that

\(\mathrm{sup}_{\sigma^\prime}\mathrm{inf}_{\tau^\prime}\mathrm{Pr}\big(w(\pi'(\sigma',\tau'))\in W\big)\ge\mathrm{sup}_\sigma\mathrm{inf}_\tau\mathrm{Pr}\big(w(\pi(\sigma,\tau))\in W\big).\)

By symmetry, the values of _G_ and \(G'\) are equal. Since both games are value-determined and have the same threshold _p_, their winners are the same.

_Proof of Theorem A.2._ The first part follows directly from Theorems A.3 and 8.4. For the second part, observe that Theorem A.3 provides an explicit method for constructing a winning strategy on _H_ given a strategy for a prior graph _G<sub>i</sub>_ such that \(G_i\equiv_{1\text{-WL}}H\).

## Generalized Büchi games.

A generalized Büchi game is equipped with a family of sets \(F_1,\dots,F_r\subseteq V\) , and Player 1 wins if every set _F<sub>i</sub>_ is visited infinitely often. Generalized Büchi games can be viewed as a special case of value-determined games. Indeed, if the sets _F_<sub>1</sub>_,...,F<sub>r</sub>_ come with fixed identifiers, we may label every vertex _v_ by the set

\(w(v):=\{i\in[r]|v\in F_i\},\)

and choose the Borel objective that requires every index \(i\in[r]\) to occur infinitely often. Hence, Theorem A.2 immediately applies to this representation.

There is, however, a subtlety in this formulation. Encoding the indices \(i\in[r]\) as part of the vertex labels makes the identities of the Büchi sets part of the input attributes. Consequently, an isomorphism is required to preserve every set _F<sub>i</sub>_ individually. This is stronger than the arguably more natural notion of isomorphism for generalized Büchi games, under which the Büchi sets themselves may be permuted. Namely, one would only require the existence of a graph isomorphism \(\varphi\) and a permutation \(\pi\) of \[_r_\] such that

\(v\in F_i\Longleftrightarrow\varphi(v)\in F'_{\pi(i)}\)

for every \(v\in V\) and \(i\in[r]\).

A natural attempt to model this stronger symmetry is to introduce one unlabeled auxiliary vertex for each Büchi set and encode membership by incidence edges. In such a representation, graph isomorphisms may freely permute the auxiliary vertices, exactly as desired. However, our current 1-WL argument does not immediately extend to this representation: the shadow-play construction preserves local colors and transition behavior, but does not provide a single globally consistent matching between the Büchi sets of the two games. Such a consistent matching appears necessary in order to conclude that visiting every Büchi set infinitely often is preserved.

