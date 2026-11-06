<tbc>**Algorithm 1** : \(\text{OutNeighboursCase1}(G,G_S,u,v,w,\delta,\text{out-count}[])\)

**Input**: \(G,G_\pi^-,G_S,\delta\)

1: \(L_1\leftarrow E_{u,v},L_2\leftarrow E_{u,w},L_3\leftarrow E_{v,w}\)

2: \(L_{12}\leftarrow\text{FindExceedingEntryLS}(L_1,L_2)\)

3: \(L_{23}\leftarrow\text{FindExceedingEntryBS}(L_2,L_3)\)

4: **for** \(e=(u,v,t)\in L_1\) **do**

5: **if** \(t(e)\le t(L_{12}[e])\le t(L_{23}[L_{12}[e]]\le t(e)+\delta\) **then**

6: out-count\[_e_\] \(\leftarrow\) out-count\[_e_\]+1

**Algorithm 2** : \(\text{OutNeighboursCase2}(G,G_S,u,v,w,\delta,\text{out-count}[])\)

**Input**: \(G,G_\pi^-,G_S,\delta\)

1: Get the lists \(L_1\leftarrow E_{v,u},L_2\leftarrow E_{v,w},L_3\leftarrow E_{u,w}\)

2: \(L_{13}\leftarrow\text{FindBoundingEntry}(L_1,L_3,\delta)\)

3: \(L_{12}\leftarrow\text{FindExceedingEntryBS}(L_1,L_2)\)

4: **for** \(e=(v,u,t)\in L_1\) **do**

5: **if** \(t(e)\le t(L_{12}[e])\le t(L_{13}[e])\le t(e)+\delta\) **then**

6: out-count\[_e_\] \(\leftarrow\) out-count\[_e_\]+1

**Algorithm 3** : \(\text{OutNeighbours}(G,G_\pi^-,G_S,\delta,\text{out-count}[])\)

**Input**: \(G,G_\pi^-,G_S,\delta\)

1: **for** \((u,v)\in E(G_\pi^-)\) **do**

2: **for** \(w\in N^+(u)\) **do**

3: **if** _w_ is adjacent to _v_ **then**

4: \(\text{OutNeighboursCase1}(G,G_S,u,v,w,\delta,\)

5: OutNeighboursCase2(_G,G<sub>S</sub>,u,v,w,_\(\delta,\)

out-count\[\])

Theorem 3.1. _Consider a temporal edge e_=(_u,v,t_) _with_ \(\pi(u)<\pi(v)\) _and an out-neighbour w of u which is adjacent to v. e forms at least one_ \(\delta\)_-temporal triangle with w if and only if_ \(t(e)\le t(L_{12}[e])\le t(L_{23}[L_{12}[e]])\le t(e)+\delta\).

Proof. If \(t(e)\le t(L_{12}[e])\le t(L_{23}[L_{12}[e]])\le t(e)+\delta\) holds, then the edges _e_ in _L_<sub>1</sub>, _L_<sub>12</sub>\[_e_\] in _L_<sub>2</sub> and _L_<sub>23</sub>\[_L_<sub>12</sub>\[_e_\]\] in _L_<sub>3</sub> form a \(\delta\)-temporal triangle.

Now suppose that the edges _e_<sub>1</sub>_,e_<sub>2</sub> and _e_<sub>3</sub> form a \(\delta\)-temporal triangle, with \(e_i\in L_i\) for _i_=1,2,3 and _e_<sub>1</sub>=_e_. It must be the case that \(t(e)\le t(e_2)\le t(e_3)\le t(e)+\delta\). Based on the definition of the lists _L_<sub>12</sub> and _L_<sub>23</sub>, we know that \(t(e)\le t(L_{12}[e])\le t(e_2)\), \(t(e_2)\le t(L_{23}[e_2])\le t(e_3)\) and \(t(L_{12}[e])\le t(L_{23}[L_{12}[e]])\). Since \(t(L_{12}[e])\le t(e_2)\), it follows that \(t(L_{23}[L_{12}[e]])\le t(L_{23}[e_2])\). Putting it all together, we get \(t(e)\le t(L_{12}[e])\le t(L_{23}[L_{12}[e]])\le t(L_{23}[e_2])\le t(e_3)\le t(e)+\delta\). Therefore _e,L_<sub>12</sub>\[_e_\] and _L_<sub>23</sub>\[_L_<sub>12</sub>\[_e_\]\] form a \(\delta\)-temporal triangle. This completes the proof. □

Next, consider the case in which _L_<sub>1</sub> consists of the temporal edges from _v_ to _u_ i.e. \(L_1\leftarrow E_{v,u}\). Set _L_<sub>2</sub> to _E<sub>v,w</sub>_ and _L_<sub>3</sub> to _E<sub>u,w</sub>_. As before, an edge _e_ in _L_<sub>1</sub> forms a \(\delta\)-temporal triangle with _w_ if there exists a pair in \(L_2\times L_3\), that satisfies the temporal window and ordering constraints. Since the edges in _L_<sub>2</sub> are not incident on the source _u_ of the edge (_u,v_), the algorithm cannot make a pass through the edges in this list. Therefore, it uses uses algorithm-2 instead. The following claim establishes the correctness of algorithm-2.

Theorem 3.2. _Consider a temporal edge e_=(_v,u,t_) _with_ \(\pi(u)<\pi(v)\) _and an out-neighbour w of u which is adjacent to v in G<sub>S</sub>. e will form at least one_ \(\delta\) _temporal triangle with w if and only if_ \(t(e)\le t(L_{12}[e])\le t(L_{13}[e])\le t(e)+\delta\)_, where the lists L_<sub>1</sub>_,L_<sub>2</sub>_,L_<sub>3</sub>_,L_<sub>12</sub> _and L_<sub>23</sub> _are defined as above._

Proof. If the condition \(t(e)\le t(L_{12}[e])\le t(L_{13}[e])\le t(e)+\delta\) is satisfied, then the edges _e_ in _L_<sub>1</sub>, _L_<sub>1</sub>\[_e_\] in _L_<sub>2</sub> and _L_<sub>13</sub>\[_e_\] in _L_<sub>3</sub> form a \(\delta\)-temporal triangle.

Now suppose that the edges _e_<sub>1</sub>_,e_<sub>2</sub> and _e_<sub>3</sub> form a \(\delta\)-temporal triangle, with \(e_i\in L_i\) for _i_=1,2,3 and _e_<sub>1</sub>=_e_. Clearly \(t(e)\le t(e_2)\le t(e_3)\le t(e)+\delta\). Based on the definitions of the lists _L_<sub>12</sub> and _L_<sub>13</sub>, it follows that \(t(e)\le t(L_{12}[e])\le t(e_2)\) and \(t(e_3)\le t(L_{13}[e])\le t(e)+\delta\). Putting these together, we get \(t(e)\le t(L_{12}[e])\le t(e_2)\le t(e_3)\le t(L_{13}[e])\le t(e)+\delta\). Therefore, we can conclude that the edges _e,L_<sub>12</sub>\[_e_\] and _L_<sub>13</sub>\[_e_\] form a \(\delta\)-temporal triangle. □

Combining the two cases, the overall procedure for dealing with the out-neighbours is outlined in algorithm-3.

Theorem 3.3. _The procedure OutNeighbours runs in_ \(O(m\alpha log\sigma_\mathrm{max})\) _time._

Proof. The overall time spent by the algorithm is<br>
\(O(\sum_{(u,v)\in G_\pi^-}\sum_{w\in N_\pi^+(u)}(\sigma(u,v)+\sigma(u,w))log\sigma_\mathrm{max})\). Since \(|N_\pi^+(u)|\le\alpha\) for every \(u\in V(G_\pi^-)\), it follows that the time complexity can be upper bounded by \(O(\sum_{(u,v)\in G_\pi^-}(\sigma(u,v))(\alpha log\sigma_\mathrm{max}))=O(m\alpha log\sigma_\mathrm{max})\). □

Note that in the end, for every \(e=(u,v,t)/(v,u,t)\in E(G)\), assuming \(\pi(u)<\pi(v)\), out-count\[_e_\] will contain the number of out-neighbours of _u_ which form at least one \(\delta\)-temporal triangle with _e_.

## 3.2 Dealing with In-Neighbours

After dealing with the out-neighbours, we need to compute in- count\[_e_\] for every temporal edge _e_.

Fix a temporal edge _e_=(_u,v,t_). Assume for the moment that \(\pi(u)<\pi(v)\). Suppose \(w\in N_\pi^-(u)\cap N(v)\). Observe that if \(w\in N_\pi^-(u)\cap N(v)\), then \(u\in N_\pi^+(w)\). Also \(v\in N_\pi^+(w)\) as \(\pi(u)<\pi(v)\). Consequently, in-count\[_e_\] must be updated when considering the edge \((w,u)\in E(G_\pi^-)\) and its out-neighbor \(v\in N_\pi^+(u)\) . In this case, we set _L_<sub>2</sub> to _E<sub>u,w</sub>_ and _L_<sub>3</sub> to _E<sub>v,w</sub>_ respectively. Since _w_ is the source, we cannot enumerate the edges in the list _E<sub>u,v</sub>_.

As before, _e_ forms a \(\delta\)-temporal triangle with _w_ if there is a pair of edges \((e_2,e_3)\in L_2\times L_3\) that satisfies \(t\le t(e_2)\le t(e_3)\le t+\delta\). For every \(e\in L_2\), let _L_<sub>23</sub>\[_e_\] be the first edge in _L_<sub>3</sub> with timestamp at least _t(e_). Define _I<sub>w,u,v</sub>_ as the following collection of intervals, \(I_{w,u,v}:=\{[\mathrm{max}\{0,t(L_{23}[e])-\delta\},t(e)]|\{e\in L_2\}\wedge\{t(e)\le t(L_{23}[e])\le t(e)+\delta\}\). We begin by stating the following theorem.

Theorem 3.4. _The temporal edge e_=(_u,v,t_) _forms at least one_ \(\delta\)_-temporal triangle with w if and only if there exists an interval in I<sub>w,u,v</sub> that contains t=t(e_).

Proof. Let us assume that the edges _e_<sub>1</sub>_,e_<sub>2</sub> and _e_<sub>3</sub> form a \(\delta\)- satisfying triangle, where _e_<sub>1</sub>=_e_ and \(e_i\in L_i\) for _i_=1,2,3. We would like to show that there exists an interval in _I<sub>w,u,v</sub>_ which contains _t(e_<sub>1</sub>). From the definition of the list _L_<sub>23</sub>, we know that<tbc>

