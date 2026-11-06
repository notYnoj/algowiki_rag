If no _K_<sub>4</sub> is found, we remove _u<sub>i</sub>_ from _G<sub>i</sub>_ in time O(|_N<sub>G<sub>i</sub></sub>(u<sub>i</sub>_)|) to obtain _G_<sub>_i_+1</sub> (and move to the next iteration of the for loop). This concludes the algorithm.

Each iteration takes O((_d_+1)_n_)=O<sub>C</sub>(_n_) time because \(|A_i|\le d\). The preprocessing of _M_ takes O<sub>C</sub>(_n_<sup>2</sup>) time. Therefore, the overall running time is O<sub>C</sub>(_n_<sup>2</sup>). The correctness follows as in the proof of Theorem 8.

We now describe the randomized O<sub>C</sub>(_n_log<sup>5</sup>_n+m_log_n_)-time algorithm, which first calls Theorem 2. In addition to the sd-degeneracy sequence, we will rely on a Welzl order for _G_; more specifically, in time O<sub>C</sub>((_n+m_)log_n_) we compute a vertex ordering \(\prec\): _w_<sub>1</sub>_w_<sub>2</sub>_...w<sub>n</sub>_ such that the neighborhood of every vertex of _G_ is the union of \(\mathcal{O}_\mathcal{C}(\mathrm{log}^2n)\prec\)-intervals \[23\]. We further compute, for every \(v\in V(G)\), the \(\prec\)-intervals _I_<sub>1</sub>(_v),...,I<sub>h<sub>v</sub></sub>(v_) with _h<sub>v</sub>_=O<sub>C</sub>(log<sup>2</sup>_n_) such that \(N_G(v)=\unknown_{j\in[h_v]}I_j(v)\); overall this takes time O(_n+m_). We observe that the orderings _u_<sub>1</sub>_u_<sub>2</sub>_..._ and _w_<sub>1</sub>_w_<sub>2</sub>_..._ are a priori unrelated. For every \(v\in V(G)\), we denote by \(\pi(v)\) the integer _i_ such that _v=w<sub>i</sub>_.

We create the following planar point set _P_, with |_P_|=2_m_. For every \(uv\in E(G)\), we add points \((\pi(u),\pi(v))\) and \((\pi(v),\pi(u))\) to _P_. In O(_m_log_n_) preprocessing time, a data structure D_<sub>P</sub>_ can be computed that answers rectangle query (given an axis-parallel rectangle _R_, yield a point in \(R\cap P\)) in time O(log_n_) \[20, Theorem 2\].

Let<tbc>

\(\widehat{Z}_{i,a}:=N_G(u_i)\cap N_G(a),\)

<tbc>and note the _G_ subscripts (so in particular \(\widehat{Z}_{i,a}\supseteq Z_{i,a}\)). We proceed as the deterministic O<sub>C</sub>(_n_<sup>2</sup>)- time algorithm, except we decide if \(G[\widehat{Z}_{i,a}]\) (not _G<sub>i</sub>_\[_Z<sub>i,a</sub>_\]) has an edge with the \(\prec\)-intervals _I<sub>j</sub>(v_) and D_<sub>P</sub>_. (We do not compute _M_ nor _z<sub>i,a</sub>_.) We compute \(\widehat{Z}_{i,a}\) as the intersection of

\(\unknown_{j\in[h_{u_i}]}I_j(u_i)\text{and}\unknown_{j\in[h_a]}I_j(a).\)

This intersection is itself the union of \(\mathcal{O}_\mathcal{C}(\mathrm{log}^2n)\prec\)-intervals, say _J_<sub>1</sub>_,...,J<sub>p</sub>_, computed in O<sub>C</sub>(log<sup>2</sup>_n_) time. For every \(j,k\in[p]\), we test if _E<sub>G</sub>(J<sub>j</sub>,J<sub>k</sub>_) is nonempty with the query rectangle \(J_j\times J_k\) on D_<sub>P</sub>_. If so, we return the corresponding 4-vertex clique, and terminate. This test takes O<sub>C</sub>(log<sup>5</sup>_n_) time in total, hence the claimed O<sub>C</sub>(_n_log<sup>5</sup>_n+m_log_n_) running time.

We can go one step further and find 5-vertex cliques in randomized almost linear time.

**Theorem 10.** _For every graph class_ C _of linear neighborhood complexity, a K_<sub>5</sub> _subgraph can be found in expected time_ O<sub>C</sub>(_n_log<sup>9</sup>_n+m_log<sup>5</sup>_n_) _on n-vertex m-edge graphs of_ C.

_Proof._ The proof exactly follows the second part of that of Theorem 9. We now need to detect a triangle of _G_ between a triple _J<sub>h</sub>,J<sub>j</sub>,J<sub>k</sub>_ of \(\prec\)-intervals of \(\widehat{Z}_{i,a}=N_G(u_i)\cap N_G(a)\) with \(h,j,k\in[p]\). Instead of the planar point set _P_, we build the following integral point set _Q_ in Z<sup>4</sup>. To simplify the presentation, we assume that _V(G_)=\[_n_\] and that 1,2_,...,n_ is the Welzl order computed in time O<sub>C</sub>((_n+m_)log_n_) such that the neighborhood of every vertex of _G_ is the union of \(\mathcal{O}_\mathcal{C}(\mathrm{log}^2n)\prec\)-intervals \[23\].

For every \(uv\in E(G)\), let<tbc>

\(N_G(u)\cap N_G(v)=[\ell_1,r_1]\unknown\dots\unknown[\ell_s,r_s]\)

<tbc>where each \([\ell_t,r_t]\) is an \(\prec\)-interval and _s_=O<sub>C</sub>(log<sup>2</sup>_n_), and add the point<tbc>

\(q_{u,v,t}:=(u,v,\ell_t,-r_t)\)

