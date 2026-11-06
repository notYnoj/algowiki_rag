One attempt of the algorithm draws an _s_-sample _S_ of _V(G_) and lets \(\widehat{S}\subseteq V(G)\) be its underlying set. Consider the set system<tbc>

\(\mathcal{F}\unknown_\widehat{S}:=\{N_G(u)\cap\widehat{S}|u\in U\}.\)

<tbc>We have

\(|\mathcal{F}\unknown_\widehat{S}|\le\pi_\mathcal{F}(|\widehat{S}|)\le c|\widehat{S}|^\rho\le cs^\rho\le\frac{|U|}{2}.\)

For each \(\widehat{F}\in\mathcal{F}\unknown_\widehat{S}\), let the _bucket_ \(B(\widehat{F})\) be the set of sets \(F\in\mathcal{F}\) such that \(F\cap\widehat{S}=\widehat{F}\). Thus, the buckets partition F.

Inside every bucket, we arbitrarily choose a maximum set of pairwise disjoint pairs, leaving at most one set unpaired. Let P be the collection of pairs obtained from all the buckets, and let \(\mathcal{P}_\text{good}\subseteq\mathcal{P}\) consist of those pairs {_F_<sub>1</sub>_,F_<sub>2</sub>} such that \(|F_1\triangle F_2|\le k\). If \(|\mathcal{P}_\text{good}|\ge|U|/8\), we output the corresponding pairs of vertices in _U_; otherwise, we discard the attempt and resample _S_.

**Claim 27.** _One attempt takes expected time_ \(\mathcal{O}(n+\sum_{u\in U}deg_G(u))\).

_Proof of claim._ Sampling _S_ takes O(_n_) time. Computing \(\mathcal{F}\unknown_\widehat{S}\) and partitioning F into buckets takes expected time \(\mathcal{O}(n+\sum_{u\in U}deg_G(u))\) by scanning the adjacency lists of the vertices in _U_. Building the candidate pairs takes O(|_U_|) time.

Given a candidate pair {_F_<sub>1</sub>_,F_<sub>2</sub>}, computing \(F_1\triangle F_2\) takes O(|_F_<sub>1</sub>|+|_F_<sub>2</sub>|) time. As the candidate pairs are disjoint, checking all of them takes \(\mathcal{O}(|U|+\sum_{u\in U}deg_G(u))\) time. \(\lrcorner\)

**Claim 28.** _Every attempt succeeds with probability at least_ 1/2.

_Proof of claim._ Let _F_<sub>1</sub>_,F_<sub>2</sub> lie in the same bucket. Then \(F_1\cap S=F_2\cap S\), and hence

\(|F_1\triangle F_2|\le|F_1\triangle f(S,F_1\cap S)|+|F_2\triangle f(S,F_2\cap S)|.\)

Therefore, every pair in P\\P<sub>good</sub> contains a bad element of F. As the candidate pairs are disjoint, the number of such pairs is at most the number of bad elements.

If the buckets are _B_<sub>1</sub>_,...,B<sub>t</sub>_, then \(t=|\mathcal{F}\unknown_\widehat{S}|\le|U|/2\) and<tbc>

\(|\mathcal{P}|=\sum_{j=1}^t\left\lfloor\frac{|B_j|}{2}\right\rfloor\ge\frac{|U|-t}{2}\ge\frac{|U|}{4}.\)

<tbc>With probability at least 1/2, at most |_U|/_8 elements of F are bad, and on that event

\(|\mathcal{P}_\text{good}|\ge|\mathcal{P}|-\frac{|U|}{8}\ge\frac{|U|}{8}.\)

Thus, the attempt succeeds. \(\lrcorner\)

The expected number of attempts is at most two, so Claim 27 proves the claimed expected running time when _U_ contains no pair of twins in _G_.

In the general case, construct a graph \(G'\) by adding, for every \(u\in U\), a new private pendant vertex _x<sub>u</sub>_ adjacent only to _u_. Then the vertices of _U_ have pairwise distinct neighborhoods in \(G'\). We claim that \(G'\) has \((c+2,\rho)\)-polynomial neighborhood complexity. Indeed, fix a nonempty set \(A\subseteq V(G')\), and put \(A_0:=A\cap V(G)\) and _A_<sub>1</sub>:=_A_\\_V(G_). The traces of the old vertices are determined by their traces on _A_<sub>0</sub>, except that at most |_A_<sub>1</sub>| of them can acquire a private pendant<tbc>

