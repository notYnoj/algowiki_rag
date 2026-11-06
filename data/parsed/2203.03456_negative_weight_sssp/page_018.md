Let n be the global variable in Remark 6.3<br>
\(G_0\leftarrow G,E^{rem}\leftarrow\emptyset\)<br>
// Phase 1: mark vertices as light or heavy<br>
\(k\leftarrow cln(n)\) for large enough constant c<br>
\(S\leftarrow\{s_1,\dots,s_k\}\), where each s<sub>i</sub> is a random node in V // possible: s<sub>i</sub>=s<sub>j</sub> for \(i\neq j\)<br>
For each \(s_i\in S\) compute \(\mathrm{Ball}_\mathrm{G}^\mathrm{in}(s_i,D/4)\) and \(\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,D/4)\)<br>
For each \(v\in V\) compute \(\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,D/4)\cap S\) and \(\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,D/4)\cap S\) using Line 5<br>
foreach \(v\in V\) do<br>
   If \(|\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,D/4)\cap S|\le.6k\), mark v in-light // whp \(|\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,D/4)|\le.7|V(G)|\)<br>
   Else if \(|\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,D/4)\cap S|\le.6k\), mark v out-light// whp \(|\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,D/4)|\le.7|V(G)|\)<br>
   Else mark v heavy // w.h.p \(\mathrm{Ball}_\mathrm{G}^\mathrm{in}(v,D/4)>.5|V(G)|\) and \(\mathrm{Ball}_\mathrm{G}^\mathrm{out}(v,D/4)>.5|V(G)|\)<br>
// Phase 2: carve out balls until no light vertices remain<br>
while G contains a node v marked ∗-light for \(*\in\{in,out\}\) do<br>
   Sample R<sub>v</sub>∼Geo(p) for p=min{1,80log<sub>2</sub>(n)/D}.<br>
   Compute \(\mathrm{Ball}_\mathrm{G}^*(v,R_v)\).<br>
   \(E^{boundary}\leftarrow\partial\mathrm{Ball}_\mathrm{G}^*(v,R_v)\) // add boundary edges of ball to E<sup>rem</sup>.<br>
   If R<sub>v</sub>\>D/4 or \(|\mathrm{Ball}_\mathrm{G}^*(v,R_v)|>.7|V(G)|\) then return \(E^{rem}\leftarrow E(G)\) and terminate<br>
// Pr\[terminate\] \(\le 1/n^{20}\)<br>
   \(E^{recurse}\leftarrow\mathrm{LDD}(G[\mathrm{Ball}_\mathrm{G}^*(v,R_v)],D)\) // recurse on ball<br>
  \(E^{rem}\leftarrow E^{rem}\bigcup E^{boundary}\bigcup E^{recurse}\).<br>
  \(G\leftarrow G\backslash\mathrm{Ball}_\mathrm{G}^*(v,R_v)\) // remove ball from G<br>
// Clean Up: check that remaining vertices have small weak diameter in<br>
initial input graph G<sub>0</sub>.<br>
Select an arbitrary vertex v in G.<br>
If \(\mathrm{Ball}_{G_0}^{in}(v,D/2)\unknown\supseteq V(G)\) or \(\mathrm{Ball}_{G_0}^{out}(v,D/2)\unknown\supseteq V(G)\) then return \(E^{rem}\leftarrow E(G)\) and<br>
terminate // Pr\[terminate\] \(\le 1/n^{20}\). If this does not terminate, then all remaining vertices in V(G) have weak diameter \(\le D\)<br>
Return E<sup>rem</sup>

**Algorithm 3:** Algorithm for LDD(G=(V,E),D)

