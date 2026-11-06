<tbc>\(t(L_{23}[e_2])\le t(e_3)\). Therefore, \(t(L_{23}[e])-\delta\le t(e_3)-\delta\). Since _e_<sub>1</sub>_,e_<sub>2</sub> and _e_<sub>3</sub> form a \(\delta\)-temporal triangle, \(t(e_3)\le t(e_1)+\delta\le t(e_2)+\delta\). As a consequence, \(t(e_3)-\delta\le t(e_2)\). Hence we get \(t(L_{23}[e_2])-\delta\le t(e_3)-\delta\le t(e_2)\). Equivalently, \(t(e_3)-\delta\in[t(L_{23}[e_2])-\delta,t(e_2)]\). Since \(t(e_3)\le t(e_1)+\delta\), it follows that \(t(e_3)-\delta\le t(e_1)\le t(e_2)\). Since \(t(e_3)-\delta\in[t(L_{23}[e_2])-\delta,t(e_2)]\), we can conclude that \(t(e_1)\in[t(L_{23}[e_2])-\delta,t(e_2)]\). Further, since \(t(e_2)\le t(L_{23}[e_2])\le t(e_3)\le t(e_1)+\delta\le t(e_2)+\delta\), we can conclude that \(t(e_2)\le t(L_{23}[e])\le t(e_2)+\delta\). Combined with the fact that \(e_2\in L_2\) implies that the interval \([t(L_{23}[e_2])-\delta,t(e_2)]\in I_{w,u,v}\). Hence we have found an interval in _I<sub>w,u,v</sub>_ that contains _t(e_<sub>1</sub>).

For the other direction, let us assume that there exists an interval _I_=\[_t_<sub>1</sub>_,t_<sub>2</sub>\] in _I<sub>w,u,v</sub>_ that contains _t=t(e_). Then there must exist an edge \(e^{^\prime}\in L_2\) such that \(t(L_{23}[e^{^\prime}])-\delta=t_1\) and \(t(e^{^\prime})=t_2\). Therefore, \(t(L_{23}[e^{^\prime}])-\delta\le t(e)\le t(e^{^\prime})\). Since \(t(e^{^\prime})\le t(L_{23}[e^{^\prime}])\), we have that \(t(L_{23}[e^{^\prime}])-\delta\le t(e)\le t(e^{^\prime})\le t(L_{23}[e^{^\prime}])\), which is equivalent to \(t(e)\le t(e^{^\prime})\le t(L_{23}[e^{^\prime}])\le t(e)+\delta\). So there exist edges \(e^{^\prime}\in L_2\) and \(L_{23}[e^{^\prime}]\in L_3\) that form a \(\delta\)-satisfying triangle with the edge _e_.

This completes the proof. □

Note that a similar result can be proved for the temporal edges of the form (_v,u,t_) by setting \(L_1\leftarrow E_{v,u},L_2\leftarrow E_{v,w}\) and \(L_3\leftarrow E_{u,w}\). Equipped with theorem-3.4, the algorithm proceeds as follows: for every edge \((u,v)\in G_\pi^{\rightarrow\rightarrow}\) and \(w\in N_\pi^+(u)\cap N(v)\), it gets the edge- lists \(L_1\leftarrow E_{w,v},L_2\leftarrow E_{w,u}\) and \(L_3\leftarrow E_{v,u}\). The goal is compute in-count\[_e_\] for every \(e\in L_1\). In the following discussion, we will stick to the case \(L_1\leftarrow E_{w,v},L_2\leftarrow E_{w,u},L_3\leftarrow E_{v,u}\), since the other one can be handled analogously.

Once the algorithm has the lists _L_<sub>2</sub> and _L_<sub>3</sub>, it invokes FindExceedingEntryLS(_L_<sub>2</sub>_,L_<sub>3</sub>) to get the list _L_<sub>23</sub>. It uses this list to get the intervals in the set _I<sub>u,v,w</sub>_. Next, the algorithm iterates through the temporal edges in _L_<sub>1</sub>. For every \(e\in L_1\), if it discovers an interval in _I<sub>u,v,w</sub>_ which contains _t_, it increments the value of in-count\[_e_\] by 1. Note that if \(L_1\leftarrow E_{w,v}\), then the algorithm sets \(L_2\leftarrow E_{w,u}\) and \(L_3\leftarrow E_{v,w}\). All the remaining steps will be the same.

However, observe that in this case, the algorithm iterates through the temporal edges \(e\in L_1\) for every in-neighbor \(x\in N_\pi^-(u)\cap N(v)\). To achieve the \(O(m\alpha)\) bound, we need to avoid this from happening at all.

To get around this issue, we adopt the following approach: for every static edge {_u,v_}, create two instances of a data structure that can be used store intervals. The first one, which we denote by _D<sub>u,v</sub>_, is used to deal with the temporal edges of the form _e_=(_u,v,t_). The second one, denoted by _D<sub>v,u</sub>_, is used to deal with temporal edges _e_=(_v,u,t_). When the algorithm gets the list _I<sub>u,v,w</sub>_, it inserts the intervals which belong to this list into _D<sub>v,w</sub>_. Similarly, it inserts the intervals of the list _I<sub>u,w,v</sub>_ in _D<sub>w,v</sub>_. It repeats this procedure for all \((u,v)\in G_\pi^{\rightarrow\rightarrow}\) and \(w\in N_\pi^+(u)\).

Finally, the algorithm iterates over the temporal edges in _G_. The hope is that for every temporal edge _e_=(_x,y,t_), the data structure _D<sub>x,y</sub>_ efficiently computes and returns the number of distinct lists _I<sub>a,x,y</sub>_ which consist of at least one interval containing _t_ in it, as _a_ varies across \(N_\pi^-(x)\)(or \(N_\pi^-(y)\) if \(\pi(y)<\pi(x)\)). In the next section, we offer a brief overview of how segment trees can be used for this purpose. A detailed discussion can be found in the supplementary<tbc>

<tbc>**Algorithm 4** : InNeighbours(\(G,G_S,G_\pi^{\rightarrow\rightarrow},\delta\), in-count\[_e_\])

Input: \(G,G_S,G_\pi^{\rightarrow\rightarrow},\delta\)<br>
For every \(\{u,v\}\in G_S\), build segment trees T<sub>u,v</sub> and T<sub>v,u</sub><br>
for \((u,v)\in E(G_\pi^{\rightarrow\rightarrow})\) do<br>
   for \(w\in N^+(u)\) do<br>
   if w is adjacent to v then<br>
   Get the lists \(L_2\leftarrow E_{v,u},L_3\leftarrow E_{w,u},L_2^{^\prime}\leftarrow E_{w,u}\)<br>
   and \(L_3^{^\prime}\leftarrow E_{v,u}\).<br>
   \(L_{23}\leftarrow\text{FirstExceedingEntryLS}(L_2,L_3)\)<br>
   \(L_{23}^{^\prime}\leftarrow\text{FirstExceedingEntryLS}(L_2^{^\prime},L_3^{^\prime})\)<br>
   Get the list I<sub>u,v,w</sub> using L<sub>23</sub> and L<sub>2</sub><br>
   Get the list I<sub>u,w,v</sub> using \(L_{23}^{^\prime}\) and \(L_2^{^\prime}\)<br>
   InsertSegTree(I<sub>u,v,w</sub>,T<sub>v,w</sub>,u)<br>
   InsertSegTree(I<sub>u,w,v</sub>,T<sub>w,v</sub>,u)<br>
   for \(\{u,v\}\in E(G_S)\) do<br>
   for \(e\in E_{u,v}\) do<br>
   count \(\leftarrow\text{LookUpSegTree}(t(e),T_{u,v})\)<br>
   in-count\[_e_\] \(\leftarrow\) in-count\[_e_\] + count<br>
   for \(e\in E_{v,u}\) do<br>
   count \(\leftarrow\text{LookUpSegTree}(t(e),T_{v,u})\)<br>
   in-count\[_e_\] \(\leftarrow\) in-count\[_e_\] + count

<tbc>material. The overall algorithm to handle in-neighbours is presented in algorithm-4.

## 3.3 Using Segment Trees to handle In-neighbors

Fix a temporal edge _e_=(_u,v,t_). Our goal is to compute in-count\[_e_\]. Let _T_ be the segment tree associated with the edge (_u,v_). Assume that the intervals which were inserted in this tree came from three lists: _L_<sub>1</sub>_,L_<sub>2</sub> and _L_<sub>3</sub>. Each node of _T_, in addition to a segment, stores a counter which may or may not be updated every time an interval is inserted in _T_. Note that by inserting an interval, we mean that we simulate the process of inserting an interval. The tree itself does not store any intervals.

When queried with _t_, the algorithm looks for the segments in _T_ that contain _t_. All these segments lie on a path in _T_. The algorithm traverses this path, adds the values of the counters stored in the nodes on this path, and returns the resulting sum. And the hope is that this sum is equal to the number of lists among _L_<sub>1</sub>_,L_<sub>2</sub>_,L_<sub>3</sub>, which contain at least one interval with _t_ in it.

For the sake of simplicity, assume that each of the three lists contain at least one interval with _t_ in it. Further, consider the simple procedure, in which every time an interval is inserted at a node _x_ in _T_, the procedure increments its counter by 1. Ideally, if exactly one interval in each list contains _t_, then there is nothing to worry about, and the sum of counters correctly evaluates to 3. However, dealing with the case in which there exist multiple intervals containing _t_ within the same list is not as straightforward.

We briefly describe the issue here. Let _x_ and _y_ be two nodes on the path of the segments containing _t_. Assume _y_ to be a descendant of _x_ on this path. Suppose _L_<sub>1</sub> contains intervals _I<sub>x</sub>_ and _I<sub>y</sub>_, which will be stored at _x_ and _y_ respectively. If _I<sub>x</sub>_ is inserted before _I<sub>y</sub>_, then we can avoid increasing the counter of _y_. This is because when looking for _y_, the algorithm will encounter _x_ on its path. The moment is<tbc>

