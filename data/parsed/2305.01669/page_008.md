<tbc>For q=2, the DAG in Figure 4(a) is recorded. The edge labeled with the local partial derivative _b_<sub>2,2</sub> (=x\[0\] for i=1) spans two layers making the DAG not layered. We aim to transform it into a layered tripartite DAG representing the local Jacobian product \(A\cdot B\), where \(A\equiv(a_{j,i})\) as well as \(B\equiv(b_{j,i})\). The \(\partial_{j^\prime,i^\prime}\) are replaced by _a<sub>j,i</sub>_ or _b<sub>j,i</sub>_. This slight modification in the notation is expected to make he upcoming examples easier to follow.

Edge splitting makes the DAG layered by inserting _l_-1=_j-i_-1 dummy vertices for all edges connecting vertices in layers _i_ and _j_ (here, _l_=2-0=2 yields one additional vertex labelled 3,0 to mark it as split vertex of edge (0,3)). One of the resulting new edges keeps the original label while the others are labelled with ones as in Figure 4(b) (_l_-1=1 dummy vertex). The Jacobian \(F'\) turns out to be invariant under edge splitting as an immediate consequence of the chain rule of differentiation. For example,

\(F'=\left(\begin{array}{ c c }
a_{1,1} & 0 \\
a_{2,1} & 1
\end{array}\right)\left(\begin{array}{ c c }
b_{1,1} & b_{1,2} \\
0 & b_{2,2}
\end{array}\right)=\left(\begin{array}{ c c }
a_{1,1}b_{1,1} & a_{1,1}b_{1,2} \\
a_{2,1}b_{1,1} & a_{2,1}b_{1,2}+b_{2,2}
\end{array}\right).\)

Invertibility of \(F'\) implies invertibility of all elemental Jacobians in the resulting uniformly layered DAG.

Definition 4.2 (Edge Splitting). _Let G_=(_V,E_) _be a DAG as in Definition 2.2. An_ edge (_i,j_) _with label_ \(\lambda\) _is_ split _by replacing it with two new edges_ (_i,k_) _and_ (_k,j_), \(k\unknown\in V\)_, and labeling them with_ \(\partial_{k,i}=\lambda\) _and_ \(\partial_{j,k}=1\) _(or vice versa), respectively._

Consequences of the two choices for labelling the new edges are the subject of ongoing investigations. Both alternatives are regarded as equivalent for the purpose of the upcoming discussions.

Lemma 4.3. _Let a DAG G induce an invertible Jacobian_ \(F'\in\mathbb{R}^{n\times n}\) _under the chain rule of differentiation as in Lemma 4.1._

1. _The Jacobian is invariant under edge splitting as in Definition 4.2._<tbc>

2. _If repeated edge splitting yields a uniformly layered DAG as in Definition 2.4, then the local Jacobians of each layer are invertible._

_Proof._

1. Equation (4.1) is invariant under edge splitting.<tbc>

2. Let the uniformly layered DAG have depth _q_. Equation (4.1) yields \(F'=F'_q\cdot\dots\cdot F'_1\) and hence

\((F')^{-1}=(F'_q\cdot\dots\cdot F'_1)^{-1}=(F'_1)^{-1}\cdot\dots\cdot(F'_q)^{-1}\)

implying invertibility of all \(F'_j\), _j_=1_,...,q_.

Obviously, edge splitting terminates as soon as the DAG becomes layered.

**4.2. Preaccumulation.** Making DAGs layered by edge splitting turned out to be rather straightforward. Unfortunately, the resulting layered DAGs are rarely uniform. Moreover, invertibility of the Jacobian implies that the sizes of all layers are at least equal to _n_. We propose _preaccumulation_ of local sub-Jacobians followed by the decomposition of the resulting bipartite sub-DAGs into layered tripartite sub-DAGs as a method for making such DAGs uniformly layered.

Figure 5(a) shows a non-uniformly layered tripartite DAG _G_ with _n=m_=3 sources, respectively, sinks and _p_=4 intermediate vertices. Connected components of the bipartite sub-DAGs induce pure layered tripartite sub-DAGs of _G_ as formally

