## A Appendix

### A.1 Segment-Trees to deal with in-neighbours

#### A.1.1 Primer on Segment Trees:

Before we proceed, we specify that when talking about a temporal edge _e_=(_x,y,t_), we will assume \(\pi(x)<\pi(y)\) for the ease of presentation. The other case can be handled analogously.

Recall that for every static edge {_u,v_}, the algorithm creates two segment trees, namely _T<sub>u,v</sub>_, and _T<sub>v,u</sub>_. A segment tree is a balanced binary tree, used to store intervals. Every node of this tree contains a segment. We will use Seg(_v_) to denote the segment stored at _v_. For every _v_ in _T_, Seg(_v_) is obtained by combining the segments stored in the left and right children of _v_. In particular, if Seg(LeftChild(_v_))=\[_a,b_\] and Seg(RightChild(_v_))=\[_c,d_\], then Seg(_v_)=\[_a,d_\]. For our setting, in addition to a segment, every node contains a counter, which we denote by Counter(_v_) and a vertex, denoted by Vertex(_v_). Given a node _v_ in _T_ and a set of intervals _I_, the _canonical subset_ of _v_ consists of intervals in _I_, which contain Seg(_v_), but do not contain Seg(parent(_v_)). In a segment tree, if the canonical subset of a node contains an interval _I_, then _I_ is stored at that node. Although _I_ may belong to the canonical subset of several nodes in _T_, it is well known that at any given level, there can be at most 2 nodes where the _I_ might be stored \[9\]. This fact is crucial in establishing the _O_(log_n_) complexity for inserting an interval in a segment tree. In particular, given an interval _I_, the time needed to look for the nodes, whose canonical subset contains _I_, is _O(h_), where _h_ is the height of the tree.

Coming back to the algorithm, note that for every \((u,v)\in G_\pi^-\rightarrow\) and \(w\in N_\pi^+(u)\), the algorithm first computes a list _I<sub>u,v,w</sub>_ of intervals, and then inserts them in the segment tree _T<sub>v,w</sub>_. Finally, given a temporal edge _e_=(_u,v,t_), the algorithm traverses along a path in _T<sub>u,v</sub>_. Every node on this path consists of a segment that contains _t_. We shall refer to this path as the _suitable path for t in T<sub>u,v</sub>_. The algorithm accumulates the values of Counter(_v_) for every node _v_ on this path and subsequently returns the sum. The hope is that this value represents the number of vertices in \(N_\pi^-(u)\cap N(v)\), which form at least one \(\delta\)-temporal triangle with _e_. This is precisely what in-count\[_e_\] is expected to store.

**_First Attempt :_**

Consider the intervals in _I<sub>w,u,v</sub>=L_ for some \(w\in N_\pi^-(u)\cap N(v)\). Suppose the algorithm does the following: for every \(I\in L\), it looks for the node(s) in _T<sub>u,v</sub>_ whose canonical subset contains _I_. For every such node _x_, it increments Counter(_x_) by 1.

We will use Figure-8a as a running example. Suppose _I<sub>w,u,v</sub>=L_<sub>1</sub>={\[6,13\],\[8,10\]}. Observe that the intervals \[6,13\] and \[8,10\] belong to the canonical subset of nodes 1(i.e. node with segment \[7,10\]) and 2(i.e. node with segment \[9,10\]) respectively. As a result, after inserting the intervals in _L_<sub>1</sub>, the algorithm updates Counter(1) and Counter(2) to 1. Now suppose _e_=(_u,v,_9). In order to compute in-count\[_e_\], the algorithm looks for the suitable path of 9 in _T<sub>u,v</sub>_. In this case, this path consists of nodes 1,2 and 4(i.e. node with segment \[9,10\]). The algorithm adds the counters stored at these nodes and then returns the sum 2. However, both the intervals belong to the same list _L_<sub>1</sub>. Therefore, ideally, the sum should have been 1 (to account for the in-neighbour _w_). More concretely, the algorithm has over-counted the contribution of _w_.

**_Case when I_<sub>1</sub> _inserted before I_<sub>2</sub>**:**

