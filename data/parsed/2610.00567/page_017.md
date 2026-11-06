### C.1 Graph enumeration and edge encoding

The following function enumerates all connected graphs on _n_ vertices, orders them by automorphism-group size, and assigns a fixed ordering to their possible edges. The edge-bitstring gives a compact representation of each graph with respect to this ordering.

### C.2 Embedding matrix

For graphs _P_ and _H_, the following function counts injective vertex maps from _P_ to _H_ that preserve every edge of _P_. The matrix construction then normalizes this count by the size of the automorphism group of the pattern graph.

from sage.graphs.graph_generators import graphs def connected_graphs(n): G = [H for H in graphs(n) if H.is_connected()] labels = [f"G{i+1:03d}" for i in range(len(G))] aut = [ int(H.automorphism_group().cardinality()) for H in G ] order = sorted( range(len(G)), key=lambda i: aut[i] ) G = [G[i] for i in order] labels = [labels[i] for i in order] aut = [aut[i] for i in order] return G, labels, aut def edge_order(n): return [ (u, v) for u in range(n) for v in range(u + 1, n) ] def edge_bitstring(G): return ’’.join( ’1’ if G.has_edge(u, v) else ’0’ for u, v in edge_order(G.order()) )

from itertools import permutations def embedding_count(P, H): k = P.order() P_vertices = list(P.vertices()) H_vertices = list(H.vertices())

Listing 1.1: Enumeration, ordering, and edge-bitstring encoding of connected _n_-vertex graphs.

Listing 1.2: Construction of the normalized embedding matrix.

