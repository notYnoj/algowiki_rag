## Construction of _H_.

The additional Steiner nodes in our Steiner reachability shortcut set _H_ will correspond to a collection of points in a three-dimensional grid. Specifically, we define a set of Steiner nodes _W_ to be

\(W=\{-1\}\times\{1,4r\}\times\{1,4r\}\times[1,4r^2].\)

(We add the -1 in the first coordinate of _W_ to distinguish the vertices in _W_ from the vertices in _V(G_).) The edge set _E(H_) of our Steiner shortcut will satisfy \(E(H)\subseteq(L_0\times W)\cup(W\times L_{2r})\).

Before we can define _E(H_), we need to introduce some new definitions. For every \(d\in[r]\) and every \(i\in\{1,2\}\), we define integer \(z_d^i\ge 0\) as follows:

\(z_d^1=\sum_{j\in[0,r-1]}f_d(2j)\text{and}z_d^2=\sum_{j\in[0,r-1]}f_d(2j+1).\)

Using integers \(z_d^i\), we are now ready to construct _E(H_).

• For every node \((0,x,y,z)\in S\) and every \(d\in[r]\), add the edge<tbc>

<tbc>\((0,x,y,z)\rightarrow\big(-1,x+r,y,z+z_d^1\big)\)<tbc>

<tbc>to _E(H_) if \(\big(-1,x+r,y,z+z_d^1\big)\in W\) is a valid point in _W_.<tbc>

• For every node \((-1,x,y,z)\in W\) and every \(d\in[r]\), add the edge<tbc>

<tbc>\((-1,x,y,z)\rightarrow\big(2r,x,y+r,z+z_d^2\big)\)<tbc>

<tbc>to _E(H_) if \(\big(2r,x,y+r,z+z_d^2\big)\in L_{2r}\) is a valid node in layer _L_<sub>2_r_</sub>.

This completes the construction of Steiner shortcut set _H_ and additional edges _E(H_).

## Analysis of _H_.

First we will bound the number of Steiner nodes in _W_ and the number of additional edges _E(H_) in our Steiner shortcut set. We observe that |_W_|=4<sup>3</sup>_r_<sup>4</sup>=_O(r_<sup>4</sup>), as claimed. Additionally, we observe that the total number of edges in our Steiner shortcut is at most

\(|E(H)|\le|S|\cdot r+|W|\cdot d\le 2^7r^5=O(r^5),\)

as claimed.

We next verify that _H_ is a valid Steiner reachability shortcut set, i.e., that the reachability relation between nodes in _V(G_) remains the same in \(G\cup H\). Let \(u,v\in V(G)\) be nodes such that path (_u,w,v_) exists in graph \(G\cup H\) for some \(w\in W\). Then we claim that _u_ can reach _v_ in _G_ as well. Let _u_=(0_,x,y,z_). We can write \(u\rightarrow w\rightarrow v\) as<tbc>

\((0,x,y,z)\rightarrow(-1,x+r,y,z+z_{d_1}^1)\rightarrow(2r,x+r,y+r,z+z_{d_1}^1+z_{d_2}^2),\)

<tbc>for some choice of \(d_1,d_2\in[1,r]\). We claim that critical path \(P_{d_1,d_2}^u\in\mathcal{P}\) is a \(u\rightsquigarrow v\) path in _G_. Notice that by construction, path \(P_{d_1,d_2}^u\) begins at node _u_ and ends at node \(v'\), where

\(v'=\left(2r,x+r,y+r,z+\sum_{i=0}^{r-1}f_{d_1}(i)+\sum_{i=0}^{r-1}f_{d_2}(i)\right)=(2r,x+r,y+r,z+z_{d_1}^1+z_{d_2}^2)=v.\)

We conclude that \(P_{d_1,d_2}^u\) is a \(u\rightsquigarrow v\) path in _G_, as claimed.

Finally, we verify that for every \(s\rightsquigarrow t\) path \(P_{d_1,d_2}^s\in\mathcal{P}\), there exists an \(s\rightsquigarrow t\) path in \(G\cup H\) of length two. Notice that by our construction of P, if \(P_{d_1,d_2}^s\) is an \(s\rightsquigarrow t\) path, then nodes _s_ and _t_ can be written as<tbc>

\(s=(0,x,y,z)\text{and}t=\left(2r,x+r,y+r,z+z_{d_1}^1+z_{d_2}^2\right).\)

<tbc>Then we can identify the following \(s\rightsquigarrow t\) path in \(G\cup H\) of length two:

\((0,x,y,z)\rightarrow(-1,x+r,y,z+z_{d_1}^1)\rightarrow\left(2r,x+r,y+r,z+z_{d_1}^1+z_{d_2}^2\right).\)

This completes the proof of Theorem C.3.

