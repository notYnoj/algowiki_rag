There are several key observations about the algorithm. First, we observe that _H_ is an \(\varepsilon\)_-directed_ cut sparsifier of the mixed graph G=(_G,F_). To see this, consider any cut (_S,T_). Then,

\(w_H(S,T)=|E_{G^\prime}(S,T)|+w_F(S,T)\le(1+\varepsilon)\cdot|E_G(S,T)|+w_F(S,T)\)<br>
\(\le(1+\varepsilon)\cdot(|E_G(S,T)|+w_F(S,T))\)<br>
\(=(1+\varepsilon)\cdot w_\mathcal{G}(S,T).\)

A symmetric argument also gives \(w_H(S,T)\ge(1-\varepsilon)\cdot w_\mathcal{G}(S,T)\). Thus, _H_ is indeed an \(\varepsilon\)-directed cut sparsifier of G. As a direct corollary, we have that \(\nu(H)\) approximates \(\nu(\mathcal{G})\) within a \((1\pm\varepsilon)\) factor, following the same reasoning as in Corollary 2.8.

Next, we observe that _K_ consists solely of undirected edges. Hence, the partition computed in Step 6 can be obtained via a recursive procedure: as long as the graph contains a connected component with edge-connectivity at least \(3\varepsilon\cdot\nu(H)\), identify such a component, contract it into a single super-vertex, and recurse on the resulting graph. Upon termination, the remaining super- vertices define the desired partition (_V_<sub>1</sub>_,...,V<sub>z</sub>_). Moreover, since the contracted graph \(K\langle V_1,\dots,V_z\rangle\) is undirected and has edge-connectivity at most \(3\varepsilon\cdot\nu(H)\), we can invoke Lemma 2.5 to conclude that \(|K\langle V_1,\dots,V_z\rangle|\le 3\varepsilon n\cdot\nu(H)\).

We now proceed to show that the baseline algorithm correctly outputs a minimum _s-t_ cut of the mixed graph G=(_G,F_).

**Claim 4.1.** _Algorithm 2 correctly computes a minimum s-t cut of_ G=(_G,F)._

\begin{tabular}{cc}
\multicolumn{2}{c}{**Algorithm 2:** Minimum _s-t_ cut algorithm for mixed graphs.} \\
\multicolumn{2}{c}{**Input:** An _n_-vertex mixed graph G=(_G,F_) with _F_ being given explicitly.} \\
\multicolumn{2}{c}{**Output:** A minimum _s-t_ cut of G.} \\
\multicolumn{2}{c}{**Procedures:**} \\
1. Fix a value of \(\varepsilon\in(0,\frac{1}{5})\). & \\
2. Compute \(G'\) which is a \(\varepsilon\)-cut sparsifier of _G_. & \\
3. Denote \(H=G'\cup F\) and compute \(\nu(H)\). & \\
4. Compute a maximum _s-t_ flow of _H_. Denote such flow graph by F. & \\
5. Obtain \(K=H\backslash(\mathcal{F}\cup F)\). & \\
6. Compute a partition \(V=V_1\cup\dots\cup V_z\) with the following properties. & \\
• Each _K_\[_V<sub>i</sub>_\] has connectivity \(\ge 3\varepsilon\cdot\nu(H)\). & \\
• \(K\langle V_1,\dots,V_z\rangle\) has connectivity \(\le 3\varepsilon\cdot\nu(H)\). & \\
7. Learn all edges of \(G\langle V_1,\dots,V_z\rangle\). & \\
8. Output a minimum _s-t_ cut in \(\mathcal{G}\langle V_1,\dots,V_z\rangle=G\langle V_1,\dots,V_z\rangle\cup F\langle V_1,\dots,V_z\rangle\). & \\
\end{tabular}

Algorithm 2: A baseline algorithm for computing a minimum _s-t_ cut of a mixed graph G=(_G,F_).

