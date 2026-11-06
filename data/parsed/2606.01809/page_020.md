## D Reduction from Dynamic DDG to Decremental DDG in the Online Setting

**Theorem D.1.** _Given an online data structure_ D_, that for any graph H, an r-capped recursive decomposition_ R_<sub>H</sub> of H with roots H_<sub>1</sub>_,H_<sub>2</sub>_,...,H<sub>k</sub>, and for any i, maintains the DDGs of all pieces in the tree rooted at H<sub>i</sub>, with preprocessing time T<sub>pre</sub>(r), handles each edge weight increase affecting H<sub>i</sub> in amortized update time T<sub>u</sub>(r_) _and has query time T<sub>q</sub>(r)._

_Then, there exists an_ online _data structure_ F_, that given a dynamic graph G, an r-division_ \(G_1,G_2,\dots,G_{k^\prime}\)_, maintains the DDG of each piece G<sub>j</sub> with pre-processing time_ \(\tilde{O}(T_{pre}(r))\) _and amortized update time_ \(\tilde{O}(\sqrt{T_{pre}(r)}\cdot T_q(r)\cdot\sqrt{r}+T_u(r))\) _and query time_ \(\tilde{O}(T_q(r))\).

The proof of the above theorem is rather straight-forward: for a fixed piece _P=G<sub>j</sub>_, we initiate a decremental data structure D on _P_ and then rebuild every \(\Delta\) updates to _P_, the entire data structure D on _P_.

For convenience, at any time step, let us define B to be the batch of insertions that were applied to _P_ since the last time that D was rebuild. Then, at each time step, if an edge weight increase was issued by the adversary, the update is forwarded to D. Independently of the type of update, we can then use the current DDGs of D and the batch B as inputs to the algorithm in Theorem 5.1 to obtain a DDGs of the current graph _H_.

It is easy to convince oneself of correctness. The running time consists of \(T_{pre}(r)/\Delta\) amortized time to rebuild the data structure D, each update to D is processed in time _T<sub>u</sub>(r_) and finally, Theorem 5.1 with the guarantee that B never exceeds size \(\Delta\) (since we rebuild the data structure and reset B after \(\Delta\) updates) ensures that the final DDG data structure that can be queried is created in time \(\tilde{O}(\Delta\cdot\sqrt{r}T_q(r))\) and query time \(\tilde{O}(T_q(r))\). By choice of \(\Delta=\sqrt{\frac{T_{pre}(r)}{T_q(r)\cdot\sqrt{r}}}\), we obtain the stated amortized update time.

## E Dynamic max flow

In this section, we prove Corollary 2.4. We assume that the reader is familiar with the details of \[20\]. It is useful to separate the running time of their data structure into two parts: \(\tilde{O}(n/\sqrt{r}+r)\) worst-case and \(\tilde{O}(n/\sqrt{r})\) amortized time. We focus on each part separately.

The \(\tilde{O}(n/\sqrt{r})\) amortized bound comes from the data structure having to recompute the _r_- division every \(\sqrt{r}\) updates. This recomputation is necessary since \[20\] supports edge insertions and deletions and an inserted edge might have endpoints in distinct pieces, violating the properties of an _r_-division. The way this is handled is to regard each such edge as a trivial piece consisting of only that edge. The issue then is that the number of pieces and the number of boundary vertices of a piece may grow over time. However, by recomputing every \(\sqrt{r}\) updates, the properties of the _r_-division are maintained. Since we only allow edge weight changes, this issue cannot arise so we can immediately eliminate the amortized time bound.

The \(\tilde{O}(n/\sqrt{r}+r)\) worst-case bound is the time it takes to

1. recompute the DDG of the piece containing the edge whose weight was changed,<tbc>

2. recompute candidate min _st_-separating cycles fully contained in that piece, and<tbc>

3. running the coarse version of Reif on the set of boundary vertices of the _r_-division.<tbc>

