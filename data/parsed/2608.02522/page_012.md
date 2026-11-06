(iii) For every \(1\le j\le H\) and any two distinct palettes \(P,Q\in\mathcal{P}_j\) the following holds. If _uv_ is an edge with \(u\in V_P\) and \(v\in V_Q\), then the first coordinate of \(\kappa_j(uv)\) belongs to \(P\triangle Q\). Moreover, if \(c\in[M_j]\) is active on _V<sub>P</sub>_ and missing on _V<sub>Q</sub>_, then, for every fixed \(v\in V_Q\), all vertices \(u\in V_P\) satisfying<tbc>

<tbc>\(\kappa_j(uv)\in\{c\}\times[q]\)<tbc>

<tbc>have the same _L<sub>j,c</sub>_-label.<tbc>

(iv) The coloring \(\kappa_j\) contains no monochromatic member of O<sub>_r_+1</sub>.

In the following, for an edge _uv_ that is colored by \(\kappa_j\), we will refer to the element of \[_M<sub>j</sub>_\] which is the first coordinate of \(\kappa_j(uv)\) as the _primary color_ of _uv_ and to the element of \[_q_\] which is the second coordinate of \(\kappa_j(uv)\) as its _secondary color_.

Having set up the notation and stated the desired invariants, we now proceed to describing the construction of the colorings \(\kappa_j\) and _L<sub>j,c</sub>_. Afterwards, we prove by induction on _j_ that they indeed satisfy all the aforementioned invariants (i)-(iv).

## Construction.

_V_<sub>0</sub> by definition consists of a single vertex, so we define \(\kappa_0\) as the empty map (there are no edges to color). Since _M_<sub>0</sub>=0 by definition, there are no colors at this stage of the process and so the family of vertex-color maps is empty.

Suppose next that \(1\le j\le H\) and that \(\kappa_{j-1}:E(K_{V_{j-1}})\rightarrow[M_{j-1}]\times[q]\), and all maps \(L_{j-1,d}:V_{j-1}\rightarrow[j]\) for all \(d\in[M_{j-1}]\) have already been defined. For every \(P\in\mathcal{P}_j\), since \(|[M_j]\backslash P|=(j-1)t=M_{j-1}\), there exists a bijection from \[_M_<sub>_j_-1</sub>\] to \[_M<sub>j</sub>_\]\\_P_. Pick and fix such a bijection and call it \(\phi_P:[M_{j-1}]\longrightarrow[M_j]\backslash P\).

We now define the vertex-color maps _L<sub>j,c</sub>_ for \(c\in[M_j]\) as follows. Let any \(u\in V_j\) be given and let _V<sub>P</sub>_ with \(P\in\mathcal{P}_j\) be the unique block containing _u_. We then define<tbc>

\(L_{j,c}(u):=\left\{\begin{array}{ c c }
L_{j-1,\phi_P^{-1}(c)}(u), & c\notin P, \\
j+1, & c\in P.
\end{array}\right.\)

<tbc>Next we define \(\kappa_j\). For this, consider any edge \(uu'\) of _K<sub>V<sub>j</sub></sub>_. Suppose first that it is internal to some block, and let \(P\in\mathcal{P}_j\) be unique such that \(u,u'\in V_P\). We now define

\(\kappa_j(uu'):=(\phi_P(d),b)\)

where _d_ and _b_ are unique such that \(\kappa_{j-1}(uu')=(d,b)\).

It remains to define \(\kappa_j\) on edges between distinct blocks.

As some preparation, we first fix an arbitrary linear ordering _\<_ on P_<sub>j</sub>_, and, for every ordered pair _P\<Q_ (arbitrarily) choose and fix distinct colors

\(a_1^{PQ},\dots,a_s^{PQ}\in Q\backslash P,b_1^{PQ},\dots,b_s^{PQ}\in P\backslash Q,\)

which is possible by choice of the collection P_<sub>j</sub>_ (cf. Lemma 3.2).

With these choices in place, we can now complete the definition of \(\kappa_j\): Let \(uu'\in E(K_{V_j})\) be any edge which is _not_ internal to some block, and let \(P,Q\in\mathcal{P}_j\) be the unique distinct palettes such that \(u\in V_P\) and \(u'\in V_Q\). We assume _P\<Q_ without loss of generality<tbc>

