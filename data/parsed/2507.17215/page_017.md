(1) If _I_ does not contain the timestamps in _T_, then _I_ will not cause any update in to the fields of the nodes, stored in _T<sub>u,v</sub>_, which is fine.<tbc>

(2) However, if _I_ does contain at least one of the timestamps in _T_, then using binary-search, we can find the largest interval in _I_ with both endpoints in _T_ . For eg: if _I_ contains \(t_i\le t_{i+1}\le\)<tbc>

<tbc>**Algorithm 7** Phase1(_T,I_)

Input: I: interval, T: root of the segment tree T<br>
if Color(T) = Grey then<br>
return<br>
if \(\mathsf{Seg}(T)\subseteq I\) then<br>
\(\mathsf{Color}(T)\leftarrow\)<br>
G<br>
return<br>
if \(I\cap\mathsf{Seg}(\mathsf{LeftChild}(T))\neq\phi\) then<br>
if Color(LeftChild(T)) = Grey then<br>
return<br>
else<br>
Phase1(LeftChild(T), I)<br>
if \(I\cap\mathsf{Seg}(\mathsf{RightChild}(T))\neq\phi\) then<br>
if Color(RightChild(T)) = Grey then<br>
return<br>
else<br>
Phase1(RightChild(T), I)

\(\cdots\le t_j\), then using binary search, we can extract the interval \[_t<sub>i</sub>,t<sub>j</sub>_\] and subsequently use it as a proxy for _I_ during the insertion process.

Putting it all together, the overall procedure is presented in Algorithm-4.

Theorem A.1. _The InNeighbours subroutine runs in_ \(O(m\alpha log\sigma_\mathrm{max}\) _time_

Proof. First, for every static edge {_u,v_}, the algorithm constructs a pair of segment trees. This takes \(O(\sigma(u,v)log\sigma_\mathrm{max})\) time. So the overall time to construct the segment trees is<br>
\(O(\sum_{\{u,v\}\in E(G_S)}\sigma(u,v)log\sigma_\mathrm{max})=O(mlog\sigma_\mathrm{max})\).

Now consider a edge \((u,v)\in G_\pi^-\rightarrow\) and \(w\in N_\pi^+(u)\). First, in line 5, the algorithm gets the lists _L_<sub>1</sub>_,L_<sub>2</sub> and _L_<sub>3</sub>. Then it invokes FindExceedingEntryLS, which takes \(O(\sigma(u,v)+\sigma(u,w))\) time. Next, it inserts into the segment tree. Let _h_<sub>max</sub> be the maximum height of the segment trees associated with the static edges in _G<sub>S</sub>_.

Consider the subroutine InsertSegTree(_I<sub>u,v,w</sub>,T<sub>v,w</sub>,u_). This subroutine inserts the intervals of the list _I<sub>u,v,w</sub>_ in the segment tree _T<sub>v,w</sub>_. Insertion of an interval in _T<sub>v,w</sub>_ takes _O(h_<sub>max</sub>) time \[refer chp. 10 of \[9\]\]. Therefore, the overall time it takes to insert the intervals which belong to the list _I<sub>u,v,w</sub>_ in _T<sub>v,w</sub>_ is given by _O_(|_I<sub>u,v,w</sub>|h_<sub>max</sub>). However, note that \(|I_{u,v,w}|\le\sigma(u,v)\).

Putting these facts together, the time it takes for the algorithm to insert the intervals in the segment tree is<br>
\(O(\sum_{(u,v)\in E(G_\pi^-)}\sum_{w\in N_\pi^+(u)}\sigma(u,v)h_\mathrm{max})\). Note that \(h_\mathrm{max}\le log\sigma_\mathrm{max}\). Therefore, the overall run time is \(O(m\alpha log\sigma_\mathrm{max})\).

Additionally, for every temporal edge _e_, getting the value of in count\[_e_\] essentially involves looking up a path in a suitable segment tree. This can be done in time, proportional to the height of the tree. Therefore, the overall run time of lines 16-18 is \(O(mlog\sigma_\mathrm{max})\).

Combining all these together, the overall run time of the subroutine is \(O(m\alpha log\sigma_\mathrm{max})\).

□

[7,16]
[7,10]
[6,13]
[12,16]
[7,8]
[9,10]
[12,14]
[15,16]
[8,10]
L1= {[8,10], [6,13]), L2= {[8,14]]

[7,16]
[7,10]
[6,13]
[12,16]
[7,8]
[9,10]
[12,14]
[15,16]
[8,10]
L1= {[8,10], [6,13]), L2= {[8,14]}

[7,16]
[7,10]
[6,13]
[12,16]
[7,8]
[9,10]
[12,14]
[15,16]
[8,10]
L1= {[8,10], [6,13]), L2= {[8,14]}

**(a) Phase 1: Insert the intervals into the segment tree, update suitable colors but donot update the counters**

**(b) Phase 2: Note the node with segment** \[7,10\] **is the only grey node which is reachable from the root via an entirely white path. So we would like to retain its color. During insertion of** \[6,13\]**, the algorithm encounters** \[7,10\]**, in which case it will update FOUND to true, go all the way to node containing** \[8,10\]**, and change its color back to white.**

**(c) Update the counters of grey nodes only.**

**Figure 9: Insertion into Segment Trees, different phases**

