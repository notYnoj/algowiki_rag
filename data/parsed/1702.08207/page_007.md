assignment _S_, which additionally encodes the starting time of search query job. If the query sequence _S_ of a node _v_ is of the form _S(v_)=(_v_<sub>1</sub>_,...,v<sub>k</sub>_), _k_=|_S(v_)|, then the corresponding schedule for _v_ will be given as \(\hat{S}(v)=((v_1,t_1),\dots,(v_k,t_k))\), with \(t_i\in\mathbb{R}_{\ge 0}\) denoting the starting time of the query for _v<sub>i</sub>_. We will call \(\hat{S}(v)\) the _schedule of node v_. We will call a schedule assignment \(\hat{S}\) _consistent_ with respect to search in a given tree _T_ if the following conditions are fulfilled:

(i) No two jobs in the schedule of a node overlap: for all \(v\in V\) , for two distinct jobs \((u_1,t_1),(u_2,t_2)\in\hat{S}(v)\), we have \(|[t_1,t_1+w(u_1)]\cap[t_2,t_2+w(u_2)]|=0\).<tbc>

(ii) If _v_ is the parent of \(v'\) in _T_ and \((u,t)\in\hat{S}(v')\), then we either also have \((u,t)\in\hat{S}(v)\), or the job \((v,t_v)\in\hat{S}(v)\) completes before the start of job (_u,t_): \(t_v+w(v)\le t\).

It follows directly from the definition that a consistent schedule assignment (and the underlying query sequence assignment) is uniquely determined by the collection of jobs \(\{(v,t_v):(v,t_v)\in\hat{S}(u),u\in V\}\). Note that not every vertex has to contain a query to itself in its schedule; we will occasionally write \(t_v=\perp\) to denote that such a job is missing. In this case, the jobs of all children of _v_ have to be contained in the schedule of node _v_.

By extension of notation for sequence assignments, we will denote a strategy following a consistent schedule assignment \(\hat{S}\) (i.e., executing the query jobs of schedule \(\hat{S}\) at the prescribed times) as \(\mathcal{A}_\hat{S}\). We will then have:<tbc>

\(\mathtt{COST}_{\mathcal{A}_\hat{S}}(T)=|\hat{S}|,\)

<tbc>where \(|\hat{S}|\) is the _duration_ of schedule assignment \(\hat{S}\), given as:<tbc>

\(|\hat{S}|=max_{v\in V}|\hat{S}(v)|,\)

<tbc>with:

\(|\hat{S}(v)|=max_{(u,t)\in\hat{S}(v)}(t+w(u)).\)

We remark that there always exists an optimal search strategy which is based on a consistent schedule. By a well-known characterization (cf. e.g. \[8\]), tree _T_ satisfies \(\mathtt{OPT}(T)=\tau\in\mathbb{R}\) if and only if there exists an assignment \(I:V\rightarrow\mathcal{I}_\tau\) of intervals of time to nodes before deadline \(\tau\), \(\mathcal{I}_\tau=\{[a,b]:0\le a<b\le\tau\}\), such that |_I(v_)|=_w(v_) and if \(|I(u)\cap I(v)|>0\) for any pair of nodes \(u,v\in V\) , then the _u-v_ path in _T_ contains a separating vertex _z_ such that \(maxI(z)\le min(I(u)\cup I(v))\). The corresponding schedule assignment of duration \(\tau\) is obtained by adding, for each node \(u\in V\) , the job (_u,minI(u_)) to the schedule of all nodes on the path from _u_ towards the root, until a node _v_ such that \(maxI(v)\le minI(u)\) is encountered on this path. The consistency and correctness of the obtained schedule is immediate to verify.

**Observation 2.2.** _For any tree T, there exists a query sequence assignment S and a corresponding consistent schedule_ \(\hat{S}\) _on T such that_ \(|\hat{S}|=\mathtt{OPT}(T)\).

## 3 The Results

### 3.1 \((1+\varepsilon)\)-Approximation in \(n^{O(logn/\varepsilon^2)}\) Time

We first present an approximation scheme for the weighted tree search problem with _n_<sup>_O_(log_n_)</sup> running time. The main difficulty consists in obtaining a constant approximation ratio for the problem with this running time; we at once present this approximation scheme with tuned parameters, so as to achieve \((1+\varepsilon)\)-approximation in \(n^{O(logn/\varepsilon^2)}\) time.

