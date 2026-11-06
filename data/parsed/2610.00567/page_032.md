For the cycle enumeration, all vertex permutations were similarly tested, with cycles identified under both rotation and reversal. Only connected graphs not already occurring in the _P_<sub>7</sub> collection were considered in the second enumeration. The retained graphs therefore satisfy

\(c_7(G)\equiv 1(mod2),\)

while not belonging to the previously obtained _P_<sub>7</sub> collection.

For each retained graph, the order of its automorphism group was computed using SageMath. When required, the corresponding automorphisms were recorded as vertex maps. To provide a reproducible binary representation of each graph, the \(21=\genfrac(){pt}{2}{7}{2}\) possible edges were placed in the fixed order

\((0,1),(0,2),(0,3),(0,4),(0,5),(0,6),\)<br>
\((1,2),(1,3),(1,4),(1,5),(1,6),\)<br>
\((2,3),(2,4),(2,5),(2,6),\)<br>
\((3,4),(3,5),(3,6),(4,5),(4,6),(5,6).\)

The corresponding 21-bit string contains a 1 exactly when the associated edge is present and a 0 otherwise.

The essential enumeration procedure is given below. The figure generation and file-format conversion used in the computational workflow are omitted from the listing, since they do not affect the graph enumeration itself.

from itertools import permutations<br>
from sage.graphs.graph\_generators import graphs<br>
def hamiltonian\_paths(G):<br>
V = list(G.vertices())<br>
paths = set()<br>
for p in permutations(V):<br>
if all(G.has\_edge(p[i], p[i+1])<br>
for i in range(len(V)-1)):<br>
paths.add(min(p, p[::-1]))<br>
return paths<br>
def hamiltonian\_cycles(G):<br>
V = list(G.vertices())<br>
n = len(V)<br>
cycles = set()<br>
for p in permutations(V):<br>
if not all(G.has\_edge(p[i], p[(i+1) % n])<br>
for i in range(n)):<br>
continue<br>
q = list(p)

Listing 1.6: SageMath code for enumerating _P_<sub>7</sub> and _C_<sub>7</sub> graphs.

