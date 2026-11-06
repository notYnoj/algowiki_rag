**Proof.** Let _q_ be a parameter to be determined later. We design a recursive algorithm that transforms the given low-rank instances in three steps into (1) slice-uniform instances, (2) uniform instances, (3) uniform and regular instances. The third step is incomplete in the sense that we cannot deal with some entries _A_<sub>sm</sub>_,B_<sub>sm</sub>_,C_<sub>sm</sub> in the matrices _A,B,C_. For these remaining entries, however, we can compute rank decompositions of strictly smaller rank \(r'<r\), so in a fourth step we will simply recurse on these matrices. In detail:

1. _(Low-Rank to Slice-Uniform)_ Run the potential-adjusting reduction from Lemma 4.4 with some parameter _t_<sub>sl</sub> to transform the given low-rank instance into _r_-slice-uniform instances; let (I<sub>sl</sub>,T<sub>sl</sub>) denote the output.<tbc>

<tbc>_Running Time:_ \(\tilde{O}(n_1n_2n_3/t_\mathrm{sl}+(n_1n_2+n_2n_3+n_1n_3)rt_\mathrm{sl}^2)\).<tbc>

2. _(Slice-Uniform to Uniform)_ We further reduce (in a potential-adjusting way) to (I<sub>unif</sub>,T<sub>unif</sub>) as follows. Initialize \(\mathcal{I}_\mathrm{unif}\leftarrow\emptyset,\mathcal{T}_\mathrm{unif}\leftarrow\mathcal{T}_\mathrm{sl}\). For each instance \((A',B',C')\in\mathcal{I}_\mathrm{sl}\) run Lemma 4.5 with some parameter _t_<sub>unif</sub> to obtain an _r_-uniform instances \((\mathcal{I}',\mathcal{T}')\). Let \(\mathcal{I}_\mathrm{unif}\leftarrow\mathcal{I}_\mathrm{unif}\cup\mathcal{I}'\) and \(\mathcal{T}_\mathrm{unif}\leftarrow\mathcal{T}_\mathrm{unif}\cup\mathcal{T}'\). This is the composition of two potential-adjusting reductions, and thus also potential-adjusting.<tbc>

<tbc>_Running Time:_ \(\tilde{O}(|\mathcal{I}_\mathrm{sl}|\cdot(n_1n_2n_3/t_\mathrm{unif}+(n_1n_2+n_2n_3+n_1n_3)rt_\mathrm{unif}^2))\).<tbc>

3. _(Uniform to Uniform Regular)_ Next, we reduce the instances in I<sub>unif</sub> further to regular instances I<sub>reg</sub> (where initially \(\mathcal{I}_\mathrm{reg}\leftarrow\emptyset\)). In this reduction step we will miss some exact triangles, but we will make sure that each missed triangle is part of one of the three instances (_A_<sub>sm</sub>_,B,C),(A,B_<sub>sm</sub>_,C),(A,B,C_<sub>sm</sub>). These three instances are required to be low-rank, hence we will also maintain low-rank decompositions of _A_<sub>sm</sub>_,B_<sub>sm</sub>_,C_<sub>sm</sub>. Initially, _A_<sub>sm</sub>_,B_<sub>sm</sub>_,C_<sub>sm</sub> are all-\(\perp\) matrices and we start with trivial rank-0 decompositions.<tbc>

<tbc>Enumerate all instances \((A',B',C')\in\mathcal{I}_\mathrm{unif}\). Since \((A',B',C')\) is a potential adjustment of the initial instance, there are potential functions \(u\in\mathbb{Z}^{n_1},v\in\mathbb{Z}^{n_2}\) such that<tbc>

<tbc>\(A'[i,k]=A[i,k]+u[i]+v[k]\text{or}A'[i,k]=\perp\)<tbc>

<tbc>for all entries. Let _q_ be a parameter. We call an entry \(A'[i,k]\) _row-heavy_ if the same entry appears in more than a _q/r_-fraction of the entries in its row (i.e., \(|\{k':A'[i,k]=A'[i,k']\}|>q/r\cdot n_2\)), otherwise we call the entry _column-heavy_ if it appears in more than a _q/r_-fraction of the entries in its column (i.e., \(|\{i':A'[i,k]=A'[i',k]\}|>q/r\cdot n_1\)), and otherwise we call the entry _light_. Let<tbc>

<tbc>\(A'=A'_\mathrm{row}\sqcup A'_\mathrm{col}\sqcup A'_\mathrm{light}\)<tbc>

<tbc>denote the partition of \(A'\) into the row-heavy, column-heavy and light entries, respectively. In the same way we obtain partitions of _B_ and _C_ into their row-heavy, column-heavy and light parts, respectively. We proceed in two substeps:

3.1. _(Light Entries)_ By definition each entry in \(A'_\mathrm{light}\) appears at most in a _q/r_-fraction of its row and column. By a simple transformation we can further partition \(A'_\mathrm{light}\) into _q_<sup>2</sup> matrices where each entry appears in at most a 1_/r_-fraction of its row and column. Hence, we can transform the subinstance \((A'_\mathrm{light},B'_\mathrm{light},C'_\mathrm{light})\) (in a potential-adjusting way) to _q_<sup>6</sup> instances that are _r_-uniform and 1_/r_-regular. Insert these instances into I<sub>reg</sub>.<tbc>

<tbc>\(\tilde{O}(|\mathcal{I}_\mathrm{unif}|\cdot q^6\cdot(n_1n_2+n_2n_3+n_1n_3))\).<tbc>

