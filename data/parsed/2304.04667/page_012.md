• (_Max-Flow._) We use the notation Max-Flow_<sub>G</sub>(s,t_) for the minimum _st_-cut, or Min-Cut for short, in _G_. Depending on the context, this could either be the actual value or a query to an algorithm for computing it. In some cases, we may omit the graph _G_ subscript or the input (_s,t_) if it is clear from the context.

### Min-Cut data structure.

Following notations from \[AKT20a\], a _Min-Cut data structure_ for a graph family F is a data structure that given a graph \(G\in\mathcal{F}\), after a preprocessing phase which makes _t<sub>pq</sub>(m_) Max-Flow calls on _G_ and spends _t<sub>po</sub>(m_) time outside of these calls, can answer Min-Cut queries for any two nodes \(s,t\in V\) in amortized query time (or output sensitive time) _t<sub>mc</sub>(k<sub>st</sub>_), where _k<sub>st</sub>_ denotes the output size (number of edges or nodes in the output cut or separator). In particular, it means that the preprocessing time is at most \(t_{pq}(m)\cdot\hat{O}(m)+t_{po}(m)\) using \[CKL<sup>+</sup>22, vdBCP<sup>+</sup>23\], and the query time is \(O(k_{st}\cdot t_{mc}(k_{st}))\). We may also be interested in Min-Cut data structures that support queries of Max-Flow values instead of cuts, and we denote their query time by _t<sub>mf</sub>(m_).

### Non-reducibility.

Using notations from \[AKT20b\], a search problem _P_ is a binary relation, and we say that _S_ is a solution to instance _x_ iff \((x,S)\in P\). Let \(\mathrm{SOL}(x)=\{S:(x,S)\in P\}\) denote the set of solutions for instance _x_. We say that _P_ is a _total function_ if every instance _x_ has at least one solution, i.e. \(\mathrm{SOL}(x)\neq\emptyset\). Let \(\perp\) be the "don’t know" symbol and assume \(\perp\notin\mathrm{SOL}(x)\) for all _x_. In particular, in our context of Min-Cut data structures, _x_ is a graph, and SOL(_x_) is the set of all Min-Cut data structures with \(t_{mc}(m)=\hat{O}(1)\) for _x_ where _m_ is the number of edges in _x_. Next, we define the nondeterministic complexity of a total function.

**Definition 1.8** (Definition 3.1 from \[AKT20b\]. See also \[CGI<sup>+</sup>16\])**.** _We say that a total function P has nondeterministic time complexity T(n_) _if there is a deterministic Turing Machine M such that for every instance x of P with size_ |_x_|=_n:_

a. \(\forall g,\mathsf{DTIME}(M(x,g))\le T(n)\)_, i.e., the time complexity of M is bounded by T(n);_<tbc>

b. \(\exists g,M(x,g)\in\mathrm{SOL}(x)\)_, i.e., at least one guess leads M to output a solution;_<tbc>

c. \(\forall g,M(x,g)\in\{\perp\}\cup\mathrm{SOL}(x)\)_, i.e., every guess leads M to output either a solution or "don’t know"._

The following is a definition of (deterministic) fine-grained reductions from a decision problem to a total function. These are Turing reductions.

**Definition 1.9** (Definition 3.12 from \[AKT20b\]. See also \[Wil18\])**.** _Let L be a language and P be a total function, and let_ \(T_L(\cdot)\) _and_ \(T_P(\cdot)\) _be time bounds. We say that_ (_L,T<sub>L</sub>_) _admits a fine-grained reduction to_ (_P,T<sub>P</sub>_) _if for all_ \(\varepsilon>0\) _there is a_ \(\gamma>0\) _and a deterministic Turing machine M<sup>P</sup> (with an access to an oracle that generates a solution to every instance of P) such that:_

1. _M<sup>P</sup> decides L correctly on all inputs when given a correct oracle for P._<tbc>

_2._ _Let_ \(\tilde{Q}(M^P,x)\) _denote the set of oracle queries made by M<sup>P</sup> on input x of length n. Then the query lengths obey the bound_<tbc>

<tbc>\(\forall x,\mathsf{DTIME}(M^P,|x|)+\sum_{q\in\tilde{Q}(M,x)}(T_P(|q|))^{1-\varepsilon}\le(T_L(n))^{1-\gamma}.\)<tbc>

<tbc>Theorem 3.13 in \[AKT20b\], provided below, further showed a non-reducibility result under NSETH for total functions with small nondeterministic complexity.

