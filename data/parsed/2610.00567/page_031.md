<tbc>Here the graphs G073, G089,G098-100, G103-104, G109,G111 and G112 are the graphs which are _K_<sub>5</sub> minor or their complements are _K_<sub>5</sub> minor. For graphs G050, G091 and G094, there are (0,2)-decompositions but no automorphism avoiding conditions could be derived for those tree decompositions. All the remaining graphs in  5 are present in one of these graphs an odd number of times. Therefore, our method cannot detect these in \(\widetilde{O}(m^2)\)-time.

### F 7-Vertex Graphs

We used SageMath to exhaustively enumerate connected graphs on seven vertices and identify graphs having an odd number of Hamiltonian paths or Hamiltonian cycles. For a graph _G_, let _p_<sub>7</sub>(_G_) denote the number of undirected Hamiltonian paths and let _c_<sub>7</sub>(_G_) denote the number of undirected Hamiltonian cycles.

For the path enumeration, all permutations of the seven vertices were tested. A permutation was retained when consecutive vertices were adjacent, and a path and its reverse were identified as the same undirected path. Thus, the retained graphs satisfy

\(p_7(G)\equiv 1(\mathrm{mod}2).\)

\begin{tabular}{ccccc}
**Name** & **Adjacency** & **#Aut t.d.** & **Checks** & **#AutRem** \\
G089 & 0111111110011011 & 8 - & - & - \\
G091 & 000110001001011 & 12 045-135-125 & 0\<4, 1\<3 & 3 \\
G092 & 001110001001111 & 12 0345-125 & 0\<4, 4\<3, 1\<2 & 1 \\
G094 & 001110111111010 & 12 - & - & - \\
G095 & 001110111111011 & 12 - & - & - \\
G096 & 010110101011011 & 12 0245-135 & 0\<2, 2\<4, 1\<3 & 1 \\
G098 & 01111001111111 & 12 - & - & - \\
G099 & 01111011111111 & 12 - & - & - \\
G100 & 011111111011001 & 12 - & - & - \\
G101 & 010110111011110 & 16 0245-2345-1345 & 0\<2, 1\<3, 2\<3, 4\<5 & 1 \\
G102 & 01011011101111 & 16 0245-2345-1345 & 0\<2, 1\<3, 2\<3, 4\<5 & 1 \\
G103 & 011111111011111 & 16 - & - & - \\
G104 & 011110001111111 & 24 - & - & - \\
G105 & 00111011111111 & 36 - & - & - \\
G106 & 000110011011110 & 48 0145-1245-2345 & 0\<1, 1\<2, 2\<3, 4\<5 & 1 \\
G107 & 000110011011111 & 48 0145-1245-2345 & 0\<1, 1\<2, 2\<3, 4\<5 & 1 \\
G108 & 011111111011110 & 48 - & - & - \\
G109 & 01111111111111 & 48 - & - & - \\
G110 & 0011101111111000 & 72 - & - & - \\
G111 & 000010001001011 & 120 - & - & - \\
G112 & 1111111111111111 & 720 - & - & - \\
\end{tabular}

5: List of all 6-vertex graphs with no \(\widetilde{O}(m^2)\)-time algorithm for induced subgraph detection.

