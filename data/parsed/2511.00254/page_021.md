<tbc>_v<sub>i</sub>v,vv<sub>j</sub>_ by a subpath _v<sub>i</sub>_, _u_<sub>_i,d_-1</sub>, _u_<sub>_i,d_-2</sub>, _... u_<sub>_i,d-k_</sub>, _u_<sub>_i_+1_,d-k_</sub>, _u_<sub>_i_+2_,d-k_</sub>, ... , _u_<sub>_j,d-k_</sub>, _u_<sub>_j,d-k_+1</sub>, ... , _u_<sub>_j,d_-1</sub>, _v<sub>j</sub>_, with _k=j-i_+1. This subpath uses the rays indexed by _i_ and _j_ and the ring indexed by _d-k_. We claim that no two such subpaths share an edge. Indeed all the rays are distinct, and if two paths used the same ring, one from _v<sub>i</sub>_ to _v<sub>j</sub>_ and the other from \(v_{i^\prime}\) to \(v_{j^\prime}\), as \(j-i=j'-i'\), we must have _v<sub>i</sub>_, \(v_{i^\prime}\), _v<sub>j</sub>_, \(v_{j^\prime}\) appearing in that order cyclically around _v_. Hence the two corresponding paths cross, contradiction.

In the second case _H_ has some demands terminating at _v_; this case is depicted in Figure 9. Let (_s,v_) be the arbitrary demand in _H_ terminating at _v_ that is replaced in \(H'\) by a demand (_s,t_), where _t=u_<sub>0,1</sub>. Let _v<sub>i</sub>v_ be the last edge in the _s,v_-path _P_ in P. Replace in _P_ the edge _v<sub>i</sub>v_ by the subpath _v<sub>i</sub>_, _v_<sub>_i,d_-1</sub>, _v_<sub>_i,d_-2</sub>, ... , _v<sub>i,i</sub>_, _v_<sub>_i_-1_,i_</sub>, _v_<sub>_i_-1_,i_-1</sub>, ... , _v_<sub>2,2</sub>, _v_<sub>1,2</sub>, _v_<sub>1,1</sub>, _v_<sub>0,1</sub>=_t_. For any other edge _vv<sub>j</sub>_ in _H_ that appears in some path \(Q\in\mathcal{P}\) (either transiting through or terminating at _v_), similarly replace _vv<sub>j</sub>_ in _H_ by a subpath _v_, _v_<sub>_j-k,_1</sub>, _v_<sub>_j-k_+1,1</sub>, _v_<sub>_j-k_+1,2</sub>, ... , _v_<sub>_j-k+i,i_</sub>=_v<sub>j,i</sub>_, _v_<sub>_j,i_+1</sub>, ... , _v_<sub>_j,d_-1</sub>, _v<sub>j</sub>_. Each such subpath is thus spiraling counterclockwise from _v_ (or _t_ for _P_) into the _i_ innermost rings, then goes straight on its own ray, and thus all such subpaths, which are rotations of each other, are disjoint. Moreover, the relative cyclic order of the paths incident to \(v'\) is the same as in _v_ (except for the path _P_ that is not incident to \(v'\)). Therefore, this routing in \(G',H'\) is uncrossed.

We may repeatedly apply the preceding lemma, in polytime until we have a new "equivalent" instance \(G',H'\) with the following properties. If _v_ has no terminals, then it has degree at most four and any terminal node has degree at most 3. The last step of the reduction now applies a degree 4 reduction (Figure 8) to each remaining vertex of degree 4. For each terminal node of degree at most 2 in _G_, we leave it. If a terminal node _v_ has _d<sub>G</sub>(v_)=3, then we subdivide each edge incident to _v_ and add a triangle onto these new degree 2 nodes. We show that this last reduction step is fine as follows.

**Lemma 6.3.** _Let G be a maximum degree_ 4 _planar graph and H an associated demand graph which forms a matching and if_ deg_<sub>H</sub>(v_)=1_, then_ \(deg_G(v)\le 3\)_. Let_ \(G''\) _be the graph obtained by performing the last phase of reductions. H has an integral uncrossed flow in G if and only if it has a totally node-disjoint flow in_ \(G''\).

V2
V1
V3
t
v'
Vo
V4
V6
V5

Figure 9: The spider web gadget: how to decrease the degree of a vertex by one in _G_ and _H_, adding only vertices of degree at most 4. Notice the red terminal that can be used as terminal for one of the demand pair ending at this vertex. In highlight with colors, an example of reconfiguration of four paths as given by the proof, with two paths which had been ending at _v_ (red and blue), and two paths passing through _v_ (yellow and green).

