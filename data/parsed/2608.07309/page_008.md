## Filtering by a random prime.

Let P be the set of primes in {_m_log<sup>2</sup>_n,...,_2_m_log<sup>2</sup>_n_}. We sample \(p\in_R\mathcal{P}\) and keep it fixed throughout the walk. For every fixed choice of _p_, the functions defined below determine a fixed marked subset of _V_(G). When checking a vertex, we use quantum search over residues \(q\in\mathbb{Z}_p\). Once _q_ is fixed, we retain only the left- and right-hand tuple combinations whose partial sums satisfy \(\Sigma_1(\alpha_1)+\Sigma_2(\alpha_2)\equiv q\mathrm{mod}p\) and \(\Sigma_3(\alpha_3)+\Sigma_4(\alpha_4)\equiv-q\mathrm{mod}p\), respectively.

## Data stored at a vertex.

At a vertex _v_=(_S_<sub>2</sub>_,S_<sub>4</sub>), the walk stores, for each \(i\in\{2,4\}\), a dictionary _D<sub>v,i</sub>_ whose bucket indices are residues \(s\in\mathbb{Z}_p\). The bucket indexed by _s_ is

\(D_{v,i}[s]=\{(\Sigma_i(x),x):x\in S_i\text{and}\Sigma_i(x)\equiv s\mathrm{mod}p\}.\)

By Theorem 2.4, those dictionaries can be built in \(\widetilde{O}(m)\) time, and each of coherent lookup, insertion, and deletion costs \(\widetilde{O}(1)\) time. The setup procedure prepares both dictionaries as part of the walk state. If a transition replaces _x_ by \(x'\) in coordinate _i_, its update coherently transforms the vertex data from (_D_<sub>_v,_2</sub>_,D_<sub>_v,_4</sub>) to \((D_{v^\prime,2},D_{v^\prime,4})\) by deleting \((\Sigma_i(x)\mathrm{mod}p,(\Sigma_i(x),x))\) and inserting \((\Sigma_i(x')\mathrm{mod}p,(\Sigma_i(x'),x'))\).

Define the lookup function \(R_{v,i}:\mathbb{Z}_p\rightarrow(\mathbb{Z}\times\mathcal{X}_i)\cup\{\perp\}\), where

\(R_{v,i}(s)=\left\{\begin{array}{ c c }
\mathrm{min}D_{v,i}[s], & D_{v,i}[s]\neq\emptyset, \\
\perp, & D_{v,i}[s]=\emptyset.
\end{array}\right.\)

Here, the minimum is taken lexicographically, first by sum and then by tuple. If _R<sub>v,i</sub>(s_)=(_z,x_), we call (_z,x_) the _canonical representative_ of the bucket indexed by _s_. Later, we show that, with high probability, every entry in the bucket containing a solution has the same sum, so the choice of representative is immaterial.

## Checking a vertex.

Let \(\alpha_1\in\mathcal{X}_1\) and \(\alpha_3\in\mathcal{X}_3\). Fix \(q\in\mathbb{Z}_p\) and define the two target bucket indices by<tbc>

\(s_2^q(\alpha_1)=\left(q-\Sigma_1(\alpha_1)\right)\mathrm{mod}p,s_4^q(\alpha_3)=\left(-q-\Sigma_3(\alpha_3)\right)\mathrm{mod}p.\)

<tbc>Thus, for \(i\in\{2,4\}\), \(s_i^q\) is the bucket index required for the block-_i_ sum. Define _F<sub>v,q</sub>_ and _G<sub>v,q</sub>_ by<tbc>

\(F_{v,q}(\alpha_1)=\left\{\begin{array}{ c c }
\Sigma_1(\alpha_1)+z, & R_{v,2}(s_2^q(\alpha_1))=(z,\alpha_2), \\
\perp, & R_{v,2}(s_2^q(\alpha_1))=\perp,
\end{array}\right.\)

<tbc>and<tbc>

\(G_{v,q}(\alpha_3)=\left\{\begin{array}{ c c }
-\Sigma_3(\alpha_3)-z, & R_{v,4}(s_4^q(\alpha_3))=(z,\alpha_4), \\
\top, & R_{v,4}(s_4^q(\alpha_3))=\perp.
\end{array}\right.\)

<tbc>Here, \(\perp\) and \(\top\) are two distinct symbols outside Z. If \(F_{v,q}(\alpha_1)=G_{v,q}(\alpha_3)\), then the corresponding representatives satisfy \(\Sigma_1(\alpha_1)+\Sigma_2(\alpha_2)=-\Sigma_3(\alpha_3)-\Sigma_4(\alpha_4)\), so the four tuples form a solution. Define the marked set<tbc>

\(\mathcal{M}_p=\{v\in V(\mathcal{G}):\exists q\in\mathbb{Z}_p,\alpha_1\in\mathcal{X}_1,\alpha_3\in\mathcal{X}_3\text{such that}F_{v,q}(\alpha_1)=G_{v,q}(\alpha_3)\}.\)

<tbc>The checking procedure coherently evaluates the predicate \(v\in\mathcal{M}_p\) by quantum search over _q_ and Claw Finding on _F<sub>v,q</sub>_ and _G<sub>v,q</sub>_, and then applies the transformation<tbc>

\(|v\rangle|D_{v,2},D_{v,4}\rangle\longmapsto(-1)^{[v\in\mathcal{M}_p]}|v\rangle|D_{v,2},D_{v,4}\rangle.\)

