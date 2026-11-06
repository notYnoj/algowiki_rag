<tbc>identifier through the function \(\mathrm{id}:V\rightarrow\{1,2,\dots,n^d\}\) for some constant \(d\ge 1\) which is unique to each communication network. Initially, each node only knows its identifier, the size of the id, and potentially some input. The nodes communicate by exchanging messages along the edges of the graph. All nodes execute the same algorithm, which proceeds in synchronous rounds. In each round, every node sends one message to each of its neighbors, receives the messages from its neighbors, and performs some individual computation. After a certain number of rounds, every node outputs, and terminates. For example, let us consider the problem of proper \((\Delta+1)\)-coloring which has been extensively studied in this model. Here, each node of the graph _G_ will initially have \(\Delta\) as input and at the end of a LOCAL coloring algorithm execution, would output the color of the node, which is a number from the palette \([\Delta+1]\).

The LOCAL model assumes a perfect world scenario where the topology of the graph _G_ doesn’t change over time and the communication channels (i.e. the edges) are perfect (i.e. the messages aren’t dropped and they are delivered instantaneously). Each node \(v\in V\) is a computer which is computationally unlimited. Also, there is no limit on the size of the message transmitted by the nodes.

The complexity of a LOCAL algorithm is measured by the number of synchronous rounds.

There is an equivalent definition of LOCAL algorithm based on locality. Before describing the equivalent definition, we define the _t-neighborhood_ of a vertex _v_ in the graph _G_ as follows.

\(\mathrm{For}v\in V(G)\text{and}t\ge 1,N_G^t[v]:=G[\{u\in V(G):\mathrm{dist}_G(u,v)\le t\}].\)

In other words, the _t_-neighborhood of _v_ in _G_ is the graph induced by the vertices of _G_ which are at distance at most _t_ from _v_ (in particular, \(v\in N_G^t[v]\)). A _t-radius view_ of _v_ is the _t_-neighborhood of _v_ along with the id, input, and the initial state of each vertex in the neighborhood.

Any (_t_+1)-round LOCAL algorithm A is equivalent to each vertex computing its output independently provided given access to its _t_-radius view. Each node _v_ implements the _gather algorithm_ where at round 1, node _v_ sends its id, input, and state to each node \(u\in N_G(v)\) and receives id(_u_), the input, and state of _u_. At the second round, it sends the collection of ids, states, and inputs to its neighbors, collects the same from them, and computes 1-radius view of _v_. At each round \(i\ge 3\), node _v_ sends its (_i_-2)-radius view to each node \(u\in N_G(v)\), receives (_i_-2)-radius view of _u_, and trivially computes its (_i_-1)-radius view. Once _v_ computes its _t_-radius view, it "simulates" A offline and compute its output. A comprehensive exposition of this equivalent definition can be found in the lecture notes \[27\].

\begin{tabular}{cccc}
**Model** & **Problem** & **Complexity** & **Source** \\
\multirow{2}{*}{Classical} & _k_-partial (_k_+1)-coloring & _O(n_) time & \[9\] \\
 & _k_-partial _k_-coloring & NP-complete & This paper \\
\multirow{2}{*}{LOCAL} & _k_-partial (_k_+1)-coloring & \(O(\mathrm{log}^2k\cdot\mathrm{log}n)\) rounds & \[9\] \\
 & _k_-partial _k_-coloring & \(\Omega(n)\) rounds (const. _k_) & This paper \\
\end{tabular}

1: Complexity theoretic landscape of _k_-partial coloring with _k_ and _k_+1 colors in the classical and distributed LOCAL models.

