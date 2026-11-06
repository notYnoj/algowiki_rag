<tbc>only edges involved are those incident to _u,v,a_<sub>1</sub>_,a_<sub>2</sub> (the vertices within distance 1 of _u_). The leaves _a_<sub>11</sub>_,...,b_<sub>22</sub> enter only through their seeds and their states at times 1 and 2 are never needed, so which other vertices a leaf is connected to does not matter. In particular, the dashed edge of Fig. 1 plays no role. Repeating the argument for \(\sigma_v\), the pair \((\sigma_u,\sigma_v)\) is a function of the seeds of the 14 vertices within distance 2 of _u_ or _v_, computed using only the solid edges of Fig. 1.

The same unfolding applies at any depth _p_ and on any 3-regular graph _G_, since each layer brings in the seeds of vertices one step farther away and the edges involved are those incident to the vertices whose state at some time \(n\ge 1\) is needed. Thus, the pair \((\sigma_u,\sigma_v)\) at an edge (_u,v_) is a function of the seeds of the vertices within distance _p_ of _u_ or _v_, computed using only the edges incident to the vertices within distance _p_-1 of _u_ or _v_. We call this set of vertices and edges the radius-_p_ neighborhood of the edge (_u,v_). Nothing outside it can change whether the edge is cut or not.

Now let _G_ have girth \(g\ge 2p+2\). Then the radius-_p_ neighborhood of any edge contains no cycle, and is thus a tree. Since _G_ is 3-regular, it is always the same tree, consisting of the endpoints _u,v_ joined by the root edge, each carrying a complete binary tree of depth _p_, as in Fig. 1 for _p_=2. Level _q_ of this tree is the set of vertices at distance _q_ from the nearer of _u_ and _v_, and contains 2<sup>_q_+1</sup> vertices for _q_=0_,...,p_. In total the number of<tbc>

<tbc>vertices in the tree is

\(N_p=2+4+\cdots+2^{p+1}=4\cdot 2^p-2.\) (6)

Since the algorithm sees nothing beyond this tree, and the seeds on it are i.i.d., the joint probability of \((\sigma_u,\sigma_v)\) is identical for every edge of every 3-regular graph of girth at least 2_p_+2. We call

\(c_\mathrm{VIRAL}(p)=\mathrm{Prob}\big[\sigma_u\neq\sigma_v\big],\) (7)

where (_u,v_) is the root edge of the depth-_p_ tree decorated with i.i.d. seeds, the value of the algorithm on the tree. It is a property of the 2_p_+1 parameters alone, not of any specific graph. Note that the tree itself is bipartite, so its own maximum cut fraction is 1, attained by the alternating 2-coloring of its vertices. This coloring, however, is not a local function of the seeds. The reason is that the outputs of a local algorithm at two vertices at distance \(\ell\) of the 3-regular tree have a correlation that decays as \(2^{\ell/2}\) \[17\], while the 2-coloring has correlation \((-1)^\ell\). Consistently, Eq. (10) below shows that _c_<sub>VIRAL</sub>(_p_) never exceeds \(\mathrm{lim}_{g\rightarrow\infty} M_g\le 0.92386\).

_From the tree to a bound on M<sub>g</sub>_ - Let us consider any 3-regular graph _G_ of girth \(g\ge 2p+2\) and run the algorithm on it with the fixed parameters and fresh i.i.d. seeds \(\epsilon\). The output \(\sigma(\epsilon)\) is a random cut of _G_, whose

