We set

\(A_i:=N_{G_i}(u_i)\backslash N_{G_i}(v_i)\text{and}X_i:=N_{G_i}(u_i)\cap N_{G_i}(v_i)\)

for every \(i\in[n-1]\).

For _i_ going from 1 to _n_-2, the algorithm proceeds as follows. Compute _A<sub>i</sub>_ in time O(|_N<sub>G<sub>i</sub></sub>(u<sub>i</sub>_)|) by filtering out the vertices of _N<sub>G<sub>i</sub></sub>(u<sub>i</sub>_) that are adjacent to _v<sub>i</sub>_. By assumption, \(|A_i|\le d\). For every \(a\in A_i\) and every \(b\in N_{G_i}(u_i)\) check if \(ab\in E(G_i)\). If so, return the triangle _u<sub>i</sub>ab_ (break from the for loop, and terminate). Even if all the checks are unsuccessful, this takes \(\mathcal{O}\left((d+1)\cdot|N_{G_i}(u_i)|\right)\) time. If no triangle is found, remove _u<sub>i</sub>_ from _G<sub>i</sub>_ in time O(|_N<sub>G<sub>i</sub></sub>(u<sub>i</sub>_)|) to obtain _G_<sub>_i_+1</sub> (and move to the next iteration of the for loop).

**Correctness.** If there is a triangle in _G<sub>i</sub>_ that contains _u<sub>i</sub>_ but the algorithm does not return one at the _i_th iteration of the for loop, it is of the form _u<sub>i</sub>xy_ with \(\{x,y\}\subseteq X_i\). Then _G_<sub>_i_+1</sub> still contains at least the triangle _v<sub>i</sub>xy_.

**Running time.** Computing the sd-degeneracy sequences takes randomized time O<sub>C</sub>(_n+m_). The rest of the algorithm takes time

\(\mathcal{O}\left(\sum_{i\in[n-2]}(d+1)\cdot(|N_{G_i}(u_i)|+1)\right)=\mathcal{O}_\mathcal{C}(n+m).\)

We now build on the scheme of the previous proof to detect a 4-vertex clique. The randomized almost linear algorithm relies on both an sd-degeneracy sequence _and_ a Welzl order.

**Theorem 9.** _For every graph class_ C _of linear neighborhood complexity, a K_<sub>4</sub> _subgraph can be found in expected_ O<sub>C</sub>(_n_log<sup>5</sup>_n+m_log_n_) _or in deterministic_ O<sub>C</sub>(_n_<sup>2</sup>) _time on n-vertex m-edge graphs of_ C.

_Proof._ We obtain an sd-degeneracy sequence (_u_<sub>1</sub>_,v_<sub>1</sub>)_,...,(u_<sub>_n_-1</sub>_,v_<sub>_n_-1</sub>) of the input graph _G_ of width _d_=O<sub>C</sub>(1) in randomized O<sub>C</sub>(_n+m_) time by Theorem 2, or deterministic O(_n_<sup>2</sup>) time by Theorem 1. For every \(i\in[n-1]\), we define _G<sub>i</sub>,A<sub>i</sub>,X<sub>i</sub>_ as in the proof of Theorem 8.

Our general strategy remains the same. Now, for every \(a\in A_i\), we do not merely need to know if \(Z_{i,a}\neq\emptyset\) but rather whether _G<sub>i</sub>_\[_Z<sub>i,a</sub>_\] contains an edge, where

\(Z_{i,a}:=N_{G_i}(u_i)\cap N_{G_i}(a).\)

We start describing the deterministic O(_n_<sup>2</sup>)-time algorithm, which naturally uses Theorem 1 as opening step.

Let _M_ be an arbitrary adjacency matrix of _G_, on which we compute the data structure of Theorem 7 (associated sparse matrix) in O<sub>C</sub>(_n_<sup>2</sup>) time. For _i_ going from 1 to _n_-3, the algorithm proceeds as follows. It computes _A<sub>i</sub>_ in time O(|_N<sub>G<sub>i</sub></sub>(u<sub>i</sub>_)|). For every \(a\in A_i\), it computes the indicator (column) vector _z<sub>i,a</sub>_ of _Z<sub>i,a</sub>_ in time O(_n_).

We observe that

\(z_{i,a}^TMz_{i,a}=2|E(G_i[Z_{i,a}])|,\)

and compute the matrix-vector product _y<sub>i,a</sub>_:=_Mz<sub>i,a</sub>_ in time O<sub>C</sub>(_n_), by Theorem 7. We now check in O(_n_) time whether there is a \(j\in[n]\) such that both _z<sub>i,a</sub>_\[_j_\] and _y<sub>i,a</sub>_\[_j_\] are nonzero. If this happens, we know that there is at least one edge in _G<sub>i</sub>_\[_Z<sub>i,a</sub>_\] incident to the _j_th vertex, say _x_, of _G_. We can find the other endpoint of such an edge, say _y_, in O(_n_) time. We return the 4-vertex clique {_u<sub>i</sub>,a,x,y_} (and terminate).

