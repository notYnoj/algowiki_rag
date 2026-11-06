Skrepetos [6], presented a \((1+\varepsilon)\)-approximate distance oracle with _O_(1) query time that uses \(O_\varepsilon(nlogn)\) storage. (This result actually also works in the weighted setting, where the weight of an edge between two disks is the Euclidean distance between their centers.)

## 2 A clique-based separator for geodesic disks in R<sup>2</sup>

Let _d_ be a metric defined on a closed path-connected subset \(F\subset\mathbb{R}^2\), and let D={_D_<sub>1</sub>_,...,D<sub>n</sub>_} be a set of geodesic disks in _F_, with respect to the metric _d_. Thus each disk<sup>5</sup> _D<sub>i</sub>_ is defined as \(D_i:=\{q\in F:d(q,p_i)\le r_i\}\), where \(p_i\in F\) is the center of _D<sub>i</sub>_ an \(r_i\ge 0\) is its radius. Let D<sub>0</sub>:=D and recall that \(\mathcal{G}^\times(\mathcal{D}_0)\) denotes the intersection graph of D<sub>0</sub>. (The reason for introducing the notation D<sub>0</sub> will become clear shortly.) We denote the set of edges of \(\mathcal{G}^\times(\mathcal{D}_0)\) by _E_ and define _m_:=|_E_|.

### 2.1 A first bound

Our basic construction of a clique-based separator S for \(\mathcal{G}^\times(\mathcal{D}_0)\), yields a separator with _O(n_<sup>4/5</sup>) cliques. In Section 2.2, we will apply a bootstrapping scheme to further reduce the size of the separator. The basic construction proceeds in three steps: in a preprocessing step we reduce the ply of the set of disks we need to deal with, in the second step we prove that if the ply is sublinear then the number of edges in the intersection graph is subquadratic, and in the third step we construct the separator.

**Step 1: Reducing the ply.** For a point \(p\in F\), let \(\mathcal{D}_0(p):=\{D_i\in\mathcal{D}_0:p\in D_i\}\) be the set of disks from D<sub>0</sub> containing _p_--note that D<sub>0</sub>(_p_) forms a clique in \(\mathcal{G}^\times(\mathcal{D}_0)\)--and define ply(_p_):=|D<sub>0</sub>(_p_)| to be the ply of _p_ with respect to D<sub>0</sub>. The ply of the set D<sub>0</sub> is defined as \(\mathrm{ply}(\mathcal{D}_0):=\mathrm{max}\{p\in F:\mathrm{ply}(p)\}\).

We start by reducing the ply of D<sub>0</sub> in the following greedy manner. Let \(\alpha\) be a fixed constant with \(0<\alpha<1\). In the basic construction we will use \(\alpha=1/5\), but in our bootstrapping scheme we will work with other values as well. We check whether there exists a point _p_ such that \(|\mathcal{D}_0(p)|\ge\frac{1}{4}n^\alpha\). If so, we remove D<sub>0</sub>(_p_) from D<sub>0</sub> and add it as a clique to S. We repeat this process until \(\mathrm{ply}(\mathcal{D}_0)<\frac{1}{4}n^\alpha\). Thus in the first step at most \(4n^{1-\alpha}\) cliques are added to S.

To avoid confusion with our initial set D<sub>0</sub>, we denote the set of disks remaining at the end of Step 1 by D<sub>1</sub> and we denote the set of edges of \(\mathcal{G}^\times(\mathcal{D}_1)\) by _E_<sub>1</sub>.

**Step 2: Bounding the size of** _E_<sub>1</sub>**.** To bound the size of _E_<sub>1</sub>, we draw a shortest path \(\pi_{ij}\) between the centers _pi<sub>i</sub>,p<sub>j</sub>_ of every two intersecting disks \(D_i,D_j\in\mathcal{D}_1\), thus obtaining a geometric realization of the graph \(\mathcal{G}^\times(\mathcal{D}_1)\). From now on, with a slight abuse of notation, we will not distinguish between an edge (_D<sub>i</sub>,D<sub>j</sub>_) in \(\mathcal{G}^\times(\mathcal{D}_1)\) and its geometric realization \(\pi_{ij}\). Let \(\Pi(\mathcal{D}_1):=\{\pi_{ij}:(D_i,D_j)\in E_1\}\) be the resulting set of paths. To focus on the main idea behind our proof we will, for the time being, assume that \(\Pi(\mathcal{D}_1)\) is a _proper path set_: a set of paths such that any two paths \(\pi_{ij},\pi_{k\ell}\) have at most two points in common, each intersection point is either a shared endpoint or a proper crossing, and no proper crossing coincides with another proper crossing or with an endpoint. When \(\pi_{ij}\) and \(\pi_{k\ell}\) have a proper crossing, we say that they _cross_, otherwise they do not cross.

We need the following well-known result about the number of crossings in dense graphs, known as the Crossing Lemma [2, 19]. The term _planar drawing_ in the Crossing Lemma

<sup>5</sup> From now on, to simplify the terminology, we omit the adjective _geodesic_ and simply use the term _disk_ to refer to the objects in D.

