## 4 Proof of Proposition 3.1: Quasi-Polynomial Computation of Strategies with Small \(\mathtt{COST}^{(\omega,c)}\)

### 4.1 Preprocessing: Time Alignment in Schedules

We adopt here a method similar but arguably more refined than rounding techniques in scheduling problems of combinatorial optimization, showing that we could discretise the starting and finishing time of jobs, as well as weights of vertices, in a way to restrict the size of state space for each node to _n_<sup>_O_(log_n_)</sup>, without introducing much error.

Fix \(c\in\mathbb{N}\) and \(\omega=\frac{a}{cn}\) for some \(a\in\mathbb{N}\). (In subsequent considerations, we will have \(c=\Theta(1/\varepsilon)\), \(a=O(\frac{n}{logn})\) and \(\omega=\Omega(\varepsilon/logn)\).) Given a tree _T_=(_V,E,w_), let \(T'=(V,E,w')\) be a tree with the same topology as _T_ but with weights rounded up as follows:

\(w'(v)=\left\{\begin{array}{ c c }
\lceil w(v)\rceil_\omega, & \text{if}w(v)>c\omega, \\
\lceil w(v)\rceil_\frac{1}{cn}, & \text{otherwise}.
\end{array}\right.\) (4.1)

We will informally refer to vertices with \(w(v)>c\omega\) (equivalently \(w'(v)>c\omega\)) as _heavy vertices_ and vertices with \(w(v)\le c\omega\) (equivalently \(w'(v)\le c\omega\)) as _light vertices_. (Note that \(w(v)\le c\omega\) if and only if \(w'(v)\le c\omega\).) When designing schedules, we consider time divided into _boxes_ of duration \(\omega\), with the _i_-th box equal to \([i\omega,(i+1)\omega]\). Each box is divided into _a_ identical _slots_ of length \(\frac{1}{cn}\).

In the tree \(T'\), the duration of a query to a heavy vertex is an integer number of boxes, and the duration of a query to a light vertex is an integer number of slots. We next show that, without affecting significantly the approximation ratio of the strategy, we can align each query to a heavy vertex in the schedule so that it occupies an interval of full adjacent boxes, and each query to a light vertex in the schedule so that it occupies an interval of full adjacent slots (possibly contained in more than one box).

We start by showing the relationship between the costs of optimal solutions for trees _T_ and \(T'\).

**Lemma 4.1.** \(\mathtt{OPT}(T)\le\mathtt{OPT}(T')\le(1+\frac{2}{c})\mathtt{OPT}(T)\).

_Proof._ The inequality \(\mathtt{OPT}(T)\le\mathtt{OPT}(T')\) follows directly from the monotonicity of the cost of the solution with respect to vertex weights, since we have \(w'(v)\ge w(v)\), for all \(v\in V\) .

To show the second inequality, we note that by the definition of weights (4.1), for any vertex _v_, \(w'(v)\le(1+\frac{1}{c})w(v)+\frac{1}{cn}\).

Consider an optimal strategy O for tree _T_ and let Q<sub>O</sub>(_T,x_)=(_v_<sub>1</sub>_,...,v<sub>k</sub>_) be the time- ordering of queries performed by strategy O on tree _T_ to find a target vertex _x_. Let \(\mathcal{O}'\) be the strategy which follows the same time-ordering of queries when locating target _x_ in \(T'\). We have:

\(\mathtt{COST}_{\mathcal{O}^\prime}(T',x)=\sum_{i=1}^kw'(v_i)\le\sum_{i=1}^k\left(\left(1+\frac{1}{c}\right)w(v)+\frac{1}{cn}\right)\le\frac{1}{c}+\left(1+\frac{1}{c}\right)\sum_{i=1}^kw(v)\le\)<br>
\(\le\left(1+\frac{2}{c}\right)\mathtt{OPT}(T),\)

where we used the fact that, by Observation 2.1, \(\mathtt{OPT}(T)\ge 1\). Since \(\mathtt{OPT}(T')\le max_{x\in V}\mathtt{COST}_{\mathcal{O}^\prime}(T',x)\), the claim follows. \(\square\)

**Lemma 4.2.** _There exists a consistent schedule assignment_ \(\hat{S}\) _for tree_ \(T'\) _such that_ \(\mathtt{COST}_{\mathcal{A}_\hat{S}}(T')\le(1+\frac{3}{c})\mathtt{OPT}(T')\) _and for all_ \(v\in V\) _we have that_

