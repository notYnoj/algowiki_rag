## 3.2 Component Hedge on Multipaths

We implement CH efficiently for learning multipaths in a multi-DAG H=(_V,M_). The multipaths are represented as |_M_|-dimensional count vectors \(\unknown\) (see Definition 7). The algorithm maintains an |_M_|-dimensional mixture vector **_f_** in the convex hull of count vectors. This hull is the following polytope obtained by relaxing the integer constraints on the count vectors:

**Definition 11 (Unit-Flow Polytope)** _Given a multi-DAG_ H=(_V,M), let_ \(\mathbf{f}\in\mathbb{R}_{\ge 0}^{|M|}\) _in which f<sub>m</sub> is associated with_ \(m\in M\)_. Define the inflow_ \(f_{in}(v):=\sum_{m\in M_v^{(in)}}f_m\) _and the outflow_ \(f_{out}(v):=\sum_{m\in M_v^{(out)}}f_m\)_. **f** belongs to the **unit-flow polytope** of_ H _if it has the following properties:_

1. _The outflow f<sub>out</sub>(s_) _of the source s is_ 1.<tbc>

_2._ _For each vertex_ \(v\in V-\mathcal{T}-\{s\}\)_, the outflow is equal to the inflow, i.e. f<sub>out</sub>(v_)=_f<sub>in</sub>(v)._

In each trial, the weight of each multiedge _f<sub>m</sub>_ is updated multiplicatively to \(\widehat{f}_m=f_mexp(-\eta\ell_m)\) and then the weight vector \(\widehat{\mathbf{f}}\) is projected back to the unit-flow polytope via a relative entropy projection:

\(\mathbf{f}^\text{new}:=argmin_{\mathbf{f}\in\text{unit-flow polytope}}\Delta(\mathbf{f}||\widehat{\mathbf{f}}),\text{where}\Delta(\mathbf{a}||\mathbf{b})=\sum_ia_ilog\frac{a_i}{b_i}+b_i-a_i.\)

This projection is achieved by repeatedly cycling over the vertices and project onto the local flow constraints at the current vertex. This method is called iterative Bregman projections (Bregman, 1967). The following lemma shows that projection to each local flow constraint is simply equivalent to scaling the in- and out-flows to the appropriate values.

**Lemma 12** _The relative entropy projection to the local flow constraint at vertex_ \(v\in V\) _is done as follows:_

1. _If v=s, normalize the f<sub>out</sub>(v_) _to_ 1.<tbc>

_2._ _If_ \(v\in V-\mathcal{T}-\{s\}\)_, scale the incoming and outgoing multiedges of v such that_<tbc>

<tbc>\(f_{out}(v):=f_{in}(v):=\sqrt{f_{out}(v)\cdot f_{in}(v)}.\)<tbc>

<tbc>**Proof.** Formally, the projection **_f_** of a given point \(\widehat{\mathbf{f}}\in\mathbb{R}_{\ge 0}^{|M|}\) to constraint _C_ is the solution to the following:

\(argmin_{\mathbf{f}\in C}\sum_{m\in M}f_mlog\left(\frac{f_m}{\widehat{f}_m}\right)+\widehat{f}_m-f_m.\)

_C_ can be one of the two types of constraints mentioned in Definition 11. We use the method of Lagrange multipliers in both cases. Observe that if |_U_|=1 for all multiedge \(m=(v,U)\in M\), then the updates in Koolen et al. (2010) are recovered.

