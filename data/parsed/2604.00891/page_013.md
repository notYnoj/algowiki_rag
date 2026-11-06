of possible intersections of a solution with the portal set subexponential, we restrict ourselves to those solutions that do not contain any discarded vertices and sufficiently few light vertices. On the flip side, the number of heavy vertices will be quite small and the number of light vertices will be somewhat small. The pebble set describes which vertices in _B_ should be contained in the solution. This should be seen as the interface of a partial solution to the rest of the graph. Each request variant will take an integer _x_ as input which will limit how many vertices of the solution we allow to be contained in _B_. Intuitively, this simply counts how many cycle separators are contained in _B_ but this intuition will not quite work due to technicalities when we compute cycle separators that separate other cycle separators in a balanced way. We then consider pebble sets for the tuple \((B,d,\alpha_\pi,x)\). Recall that these are sets \(\mathcal{M}\subseteq B_\mathrm{he}\cup B_\mathrm{li}\) with \(|\mathcal{M}\cap B_\mathrm{li}|\le 20x\alpha_\pi\sqrt{d}\mathrm{log}(d)\).

We also allow requests to depend on one additional value, which we will use for problem specific information. We denote these by \(S_\pi\) and we only have one minimal requirements regarding these: they should be maintainable in subexponential time. In many cases, the set \(S_\pi\) simply contains weight functions and for Independent Set Request, this set will be empty. In particular, a request for Independent Set Request will only consist of a pebble set M. We can now formally define Independent Set Request and afterwards give a definition for request variants in general.

Independent Set Request

**Input:** An integer _d_, a _d_-outerplanar graph _G_=(_V,E_), a portal set _B_=(_B_<sub>he</sub>_,B_<sub>li</sub>_,B_<sub>di</sub>), and an integer _x_.

**Task:** Output a lookup table that returns for each request _r_=M for each pebble set M for (_B,d,_1_,x_), the maximum size of an independent set I in _G_ where \(\mathcal{I}\cap(B_\mathrm{he}\cup B_\mathrm{li}\cup B_\mathrm{di})=\mathcal{M}\) (or \(-\infty\) if no such set exists).

Recall that a pair (_B,x_)--consisting of a set _B_ of vertices partitioned into heavy, light, and discarded vertices and an integer _x_--is almost measured with respect to two integers _d_ and \(\alpha_\pi\) if \(x\le\mathrm{max}(200\mathrm{log}^7(d),1)\), \(|B_\mathrm{he}|\le 40x\alpha_\pi\sqrt{d}\), and \(|B_\mathrm{li}|\le 60x\alpha_\pi d\mathrm{log}(d)\).

**Definition 1.** _A_ request variant \(\pi\)-Request _of locality_ \(\alpha_\pi\) _takes a tuple_ \((d,G,B,x,S_\pi)\) _as input where B_=(_B_<sub>he</sub>_,B_<sub>li</sub>_,B_<sub>di</sub>) _is partitioned into heavy, light, and discarded vertices, G is a_ \(\alpha_\pi d\)_- outerplanar graph, and_ (_B,x_) _is almost measured with respect to d and_ \(\alpha_\pi\)_. It outputs a lookup table with an entry for each request_ \(r\in R_\pi(d,G,B,\mathcal{M},S_\pi)\) _where_ M _is a pebble set for_ \((B,d,\alpha_\pi,x)\)_. The output represents some solution where the vertices in the solution contained in_ \(B_\mathrm{he}\cup B_\mathrm{li}\cup B_\mathrm{di}\) _is exactly_ M.

## 2.3 Results Used in our Algorithm

Finally, we state a number of results from the literature, which we will subsequently rely on. The first one is a well-known strategy due to Baker to transform a planar graph into several _d_-outerplanar graphs.

**Lemma 1** (\[Bak94\])**.** _Given a planar graph G and an integer d, one can compute in linear time a partition of the vertices of G into sets A_<sub>1</sub>_,A_<sub>2</sub>_,...,A<sub>d</sub> such that for each_ \(i\le d\)_, the graph G-A<sub>i</sub> is_ (_d_-1)_-outerplanar._

The second result allows us to triangulate a _d_-outerplanar graph.

**Lemma 2** (\[Bie15\], Corollary 1)**.** _Any d-outerplanar graph G can be triangulated in_ O(_n_<sup>2</sup>) _time such that the resulting graph has outer-planarity at most d_+1.

