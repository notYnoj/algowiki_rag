(1) none of the intervals in _L_ belong to the canonical subset of _x_ or<tbc>

(2) _x_ has an ancestor whose canonical subset contains an inter- \(\mathrm{val}I\in L\)

In our example, at the end of phase 2, only node 1 will be grey in color. In fact, consider the suitable path _P_ of _t_ in _Tu,v_ for some temporal edge _e=(u,v,t_). Let _v_<sub>1</sub>_,v_<sub>2</sub> and _v_<sub>3</sub> denote the grey nodes on this path, in the decreasing order of their height. At the end of phase 2, only _v_<sub>1</sub> will be grey, since it is the only grey node on _P_, which is reachable from the root via an entirely white path. Further, this will holds irrespective of the order on which the intervals are inserted. Finally, we have phase 3.

**_Phase 3:_** Once the algorithm has identified the nodes in _S_, now all it needs to do is suitably update the counters of these nodes by reinserting the intervals in _L_. In this phase, the algorithm re-inserts the intervals of _L_. As before, during the insertion of an interval _I_,

(1) If the algorithm encounters a grey node, or it visits a white node _v_ with Counter(_v_) \> 1, then it simply returns and moves on to the next input interval.<tbc>

(2) On the other hand, if the algorithm ends in a grey node, then it changes the color of that node back to white and updates its counter by adding 1 to it.

**_Why the Vertex field in the node structure?_**

Suppose there exists a list _L_<sub>2</sub>=_I<sub>z,u,v</sub>=_{[8,14]}. Observe that _I_<sub>3</sub>=[8,14] belongs to the canonical subset of node 2. Therefore, during the insertion of _I_<sub>3</sub>, the algorithm will visit node 1. Since Counter(1) \> 0, it will simply return. Therefore, the suitable path for _e=(u,v,_9) will return 1 as opposed to 2, since _z_ and _w_ are 2 different vertices in \(N_\pi^-(u)\cap N(v)\), which have the property that their corresponding lists _I<sub>w,u,v</sub>_ and _I<sub>z,u,v</sub>_, contain at least one interval with 9 in it. This is where the vertex field comes to the rescue.

For a node _v_ in _T_, Vertex(_v_) keeps track of the most recent vertex which caused Counter(_v_) to be updated.

In particular, after inserting the intervals of _I<sub>w,u,v</sub>_, suppose the algorithm needs to insert intervals in _I<sub>z,u,v</sub>_ for some \(z\neq w\) in phase 3. Given an interval \(I\in I_{z,u,v}\),

(1) If the algorithm encounters a grey node, then simply return and move on to the next interval of _I<sub>z,u,v</sub>_.<tbc>

(2) If the algorithm visits a white node _x_ with Counter(_x_) \> 0, then check for Vertex(_x_). If \(\mathrm{Vertex}(x)\neq z\), then continue with the insertion process. On the contrary, if Vertex(_x_) = _z_, then return.<tbc>

(3) If the algorithm reaches(i.e. ends in) a grey node _x_, then simply update its color to white, increment it’s associated counter by 1 and set Vertex(_x_) to _z_.

Note that phases 1 and 2 will not change. The above procedure is used in phase 3.

Combining these ideas, the overall algorithm is presented in Algorithms-5.

**_How to build the Segment Tree?_**

All throughout, we assumed that each static edge comes with pre-initialised segment trees. We now describe how to build the segment tree _Tu,v_. Note that in order to construct a segment tree, it is sufficient to specify the segments which will be stored in the leaves of the tree.

Typically, given a collection of intervals _L_, its segment tree is built using the distinct endpoints of the intervals in _L_ [9]. However, in our case, the number of such endpoints can be very large. Instead we build _Tu,v_(and _Tv,u_) using the timestamps of the temporal edges (_u,v,t_)(and (_v,u,t_)) for \(t\in\mathbb{R}\). In particular, if _T={t_<sub>1</sub>_,t_<sub>2</sub>_,...,t<sub>r</sub>_} denotes the collection of distinct timestamps of the temporal edges from _u_ to _v_, then the leaves of the segment tree will consist of the following segments (_t_<sub>1</sub>_,t_<sub>1</sub>], (_t_<sub>1</sub>_,t_<sub>2</sub>], (_t_<sub>2</sub>_,t_<sub>2</sub>], (_t_<sub>2</sub>_,t_<sub>3</sub>]_,...,(t<sub>r</sub>,t<sub>r</sub>_].

Note that the intervals we wish to insert in _Tu,v_ may not necessarily have the same endpoints as timestamps in _T_. However given an interval _I_:

[7,16]
[7,10]
[6,13]
[12,16]
[7,8]
[9,10]
[12,14]
[15,16]
[8,10]
L1= {[6,13], [8,10]), L2= {[8,14]]

[7,16]
[7,10]
[6,13]
[12,16]
[7,8]
[9,10]
[12,14]
[15,16]
L1= {[6,13], [8,10]), L2= {[8,14]]

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

**(a) Insertion of intervals into a segment tree**

**(b) Insertion into segment tree. The algorithm encounters a node with non-zero counter during the insertion of** [8,10]**, so it re- turns.**

**(c) If the orders of the intervals** [6,13] **and** [8,10] **are switched, we end up with the same issue.**

**Figure 8: Insertion into Segment Trees**

