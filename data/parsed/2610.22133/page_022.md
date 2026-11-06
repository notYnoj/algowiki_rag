## 22 Asteroidal Triples and Friends in (Likely Necessary) Matrix Multiplication Time

**Our Algorithm.** To maintain the values \(\delta_i(v)\) up to date, suppose we just removed a vertex, and we need to compute \(\delta_i\) for time step _i_. Then:

(i) If _i=t<sub>j</sub>_, i.e., we are at the start of phase _j_, then we compute

\(\delta_i(v)=\frac{1}{2}\sum_{x\in N_i(v)}|N_i(v)\backslash N_i[x]|,\)

where the values |_N<sub>i</sub>(v_)\\_N<sub>i</sub>[x_]| for all pairs of vertices _v_, \(x\in V_i\) are computed as follows:

If _j_=0 (and so _i_=0), we compute these values via the product \(A_0\bar{A}_0\).

Otherwise, if _j\>_0, let _D<sub>j</sub>=V_<sub>_t<sub>j</sub>_-1</sub>\\_V<sub>t<sub>j</sub></sub>_ be the set of vertices removed during the (_j_-1)-th phase. We obtain |_N<sub>t<sub>j</sub></sub>(v_)\\_N<sub>t<sub>j</sub></sub>[x_]| from |_N_<sub>_t<sub>j</sub>_-1</sub>(_v_)\\_N_<sub>_t<sub>j</sub>_-1</sub>[_x_]| by computing

\(|N_{t_j}(v)\backslash N_{t_j}[x]|=|N_{t_{j-1}}(v)\backslash N_{t_{j-1}}[x]|-|(N_{t_{j-1}}(v)\backslash N_{t_{j-1}}[x])\cap D_j|.\)

We observe that we can compute the second term simultaneously for all \(v,x\in V_{t_j}\) by multiplying the \(n\times|D_j|\) adjacency matrix between _V_<sub>_t<sub>j</sub>_-1</sub> and _D<sub>j</sub>_ with the \(|D_j|\times n\) non-adjacency matrix between _D<sub>j</sub>_ and _V_<sub>_t<sub>j</sub>_-1</sub>, whose entry for (_y,x_) is 1 exactly when \(y\notin N_{t_{j-1}}[x]\).

(ii) Otherwise, if \(i\neq t_j\) (we are not at the beginning of the phase), let _x_<sub>_i_-1</sub> be the vertex removed from **G**<sub>_i_-1</sub> to form **G**_<sub>i</sub>_. For each \(v\in N_{i-1}(x_{i-1})\), we set

\(\delta_i(v)=\delta_{i-1}(v)-|N_{i-1}(v)\backslash N_{i-1}[x_{i-1}]|,\)

where we compute

\(|N_{i-1}(v)\backslash N_{i-1}[x_{i-1}]|=|N_{t_j}(v)\backslash N_{t_j}[x_{i-1}]|-|(N_{t_j}(v)\backslash N_{t_j}[x_{i-1}])\cap D|.\)

Here, _D=V<sub>t<sub>j</sub></sub>_\\_V_<sub>_i_-1</sub> is the set of vertices removed so far in the current phase. We compute the intersection by iterating over all nodes in _D_ in time \(\mathcal{O}(|D|)=\mathcal{O}(\Delta)\).

**Correctness.** The correctness relies on maintaining the exact number of missing edges in each vertex’s neighborhood, and should be obvious to see.

**Runtime.** Over the entire algorithm, we perform \(\lceil n/\Delta\rceil\) phase initializations. The first initialization takes \(\mathcal{O}(n^\omega)\) time to compute \(A_0\bar{A}_0\). Each subsequent phase initialization computes the rectangular matrix product of an \(n\times|D_j|\) matrix and a \(|D_j|\times n\) matrix. Since \(|D_j|\le\Delta\), this takes \(\mathcal{O}(\mathrm{MM}(n,\Delta,n))\) time per phase, requiring a total time of \(\mathcal{O}(n/\Delta\cdot\mathrm{MM}(n,\Delta,n))\). (Also note that \(\mathcal{O}(n^\omega)=\mathcal{O}(n/\Delta\cdot\mathrm{MM}(n,\Delta,n))\) for every \(\Delta\), so the latter term dominates the former.)

The updates within the phases take \(\mathcal{O}(\Delta)\) time for each neighbor of the removed vertex. Over all _n_ removals, the sum of the degrees of the removed vertices is bounded by 2_m_. This yields a total intra-phase update time of \(\mathcal{O}(m\cdot\Delta)\).

## 4.6 Lower Bound for Finding _uv_-trails

We show that verifying whether a graph **G** contains a _uv_-trail with \(d_\mathbf{G}(u,v)\ge 3\), even for a single fixed pair of vertices _u,v_, cannot be performed faster than the time required to detect whether a graph contains a triangle. This is in stark contrast with the case _d_**<sub>G</sub>**(_u,v_)=2, where we can solve the same problem in time O(_n_<sup>2</sup>). We start by proving the following for the case _d_**<sub>G</sub>**(_u,v_)=3.

**Lemma 4.15.** _Let_ **G** _be an n-node graph. Then, in time_ O(_n_<sup>2</sup>)_, we can build a_ (3_n_+4)_-node graph_ **H** _containing two designated vertices u and v such that both of the following hold:_

(i) _d_**<sub>H</sub>**(_u,v_)=3;

(ii) **H** _contains a uv-trail if and only if_ **G** _contains a triangle._

