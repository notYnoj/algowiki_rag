The high-level idea of the proof is that any valid _st_-flow _f<sub>st</sub>_ can be transformed into a succinct _st_-flow \(f'_{st}\) by eliminating all copies of a certain pattern from _f<sub>st</sub>_, while preserving the flow value and meeting the flow constraints. The pattern that will be eliminated is called an _anti-directed closed walk_ (see Figure 3). It is, in our context, a directed graph whose underlying graph forms a _simple_ closed walk, that is where no edge appears twice, and consecutive edges have alternate directions, or in other words, no pair of consecutive edges forms a directed path. Note that an anti-directed closed walk must have an even number of edges.

**Definition 2.6** (anti-directed closed walk)**.** _For any integer_ \(\ell\)_, an_ anti-directed closed walk _is a simple closed walk_ \(C=(u_1,u_2,\dots,u_{2\ell})\) _where for each_ \(i\in[1,\dots,2\ell]\)_, the edges between u_<sub>_i_-1</sub>_,u<sub>i</sub> and between u<sub>i</sub>,u_<sub>_i_+1</sub> _are oriented in one of two ways: either (1) towards u<sub>i</sub>, that is_ \((u_{i-1},u_i),(u_{i+1},u_i)\in E(C)\)_, or (2) away from u<sub>i</sub>, that is_ \((u_i,u_{i-1}),(u_i,u_{i+1})\in E(C)\).

For an anti-directed closed walk _C_ we define _P<sub>out</sub>_ (respectively, _P<sub>in</sub>_) as the set of all node occurrences \(u_i\in C\) whose adjacent edges are oriented in way (1) (respectively, in way (2)). Note that |_P<sub>in</sub>_|=|_P<sub>out</sub>_|, \(P_{in}\cap P_{out}=\emptyset\), and \(P_{in}\cup P_{out}=C\).

The related concept of anti-directed _cycles_ has been studied before in other contexts, such as edge partitioning \[AHR81\] and the existence of anti-directed hamiltonian cycles \[DM15\]. We are now ready to prove Lemma 2.5.

_Proof of Lemma 2.5._ Let _f<sub>st</sub>_ be an _st_-flow in _G_. To modify _f<sub>st</sub>_, we iteratively find an anti-directed closed walk _C_ in _f<sub>st</sub>_ and reroute the flow of _f<sub>st</sub>_ that is shipped through _C_. The rerouting is done in such a way that results in a zero flow through at least one edge of _C_, causing the edge to be removed from _f<sub>st</sub>_. This is achieved while ensuring that the total flow entering each node in _P<sub>in</sub>_ and leaving each node in _P<sub>out</sub>_ remains exactly the same before and after the operation (refer to Figure 3).

More formally, let _e<sub>min</sub>_ be an edge in _C_ such that the flow of _f<sub>st</sub>_ through it _f<sub>st</sub>(e<sub>min</sub>_) is minimal among all edges of _C_, and assume without loss of generality that _e<sub>min</sub>_ is oriented from a node _u<sub>i</sub>_ to its predecessor _u_<sub>_i_-1</sub> in _C_ for some \(i\in[|C|]\) (where indices are calculated modulo |_C_|). For every node occurrence \(u_j\in P_{in}\), we reroute a flow of value _f<sub>st</sub>(e<sub>min</sub>_) that was previously shipped through the edge (_u<sub>j</sub>,u_<sub>_j_-1</sub>) to flow through the edge (_u<sub>j</sub>,u_<sub>_j_+1</sub>) instead. By induction on the number of<tbc>

ui-1
Pin
in
min
Pin
ui
Pout
Pout
ui+1

Figure 3: The figure on the left shows an anti-directed walk of length 8, while the figure on the right illustrates its elimination.

