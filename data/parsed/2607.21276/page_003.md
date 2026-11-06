## 2 General Setting

### 2.1 Fine-grained Reductions

**Definition 1.** _Let P,Q be problems,_ \(p,q:\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}_{\ge 0}\) _be non-decreasing functions, and_ \(\delta:\mathbb{R}_{>0}\rightarrow\mathbb{R}_{>0}\)_. We say that_ \((P,p(n))\delta\)-fine-grained reduces _to_ (_Q,q(n_)) _and write_ \((P,p(n))\le_\delta\left(Q,q(n)\right)\)_, if for every_ \(\varepsilon>0\) _and_ \(\delta=\delta(\varepsilon)>0\)_, there exists an algorithm_ A _for P with oracle access to Q, a constant_ \(\alpha\)_, and a function_ \(t(n):\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}_{\ge 0}\)_, such that on any instance of P of size n, the algorithm_ A

• _runs in time at most_ \(\alpha\cdot(p(n))^{1-\delta}\);<tbc>

• _produces at most t(n_) _instances of Q adaptively: every instance depends on the previously produced instances as well as their answers of the oracle for Q;_<tbc>

• _the sizes n<sub>i</sub> of the produced instances satisfy the inequality_<tbc>

<tbc>\(\sum_{i=1}^{t(n)}q(n_i)^{1-\varepsilon}\le\alpha\cdot(p(n))^{1-\delta}.\)<tbc>

Edge Coloring, 2m
2O(s)
k-SAT, 2n
Hitting Set, 2n
Sparse 3-Coloring, a n
log s
[17]
[2]
8-Dominating Set, n8
[3]
OV, n2
4-SUM, n2
3-SUM, n2
Edit Distance, n2
[6]
[19]
Exact Triangle, n3
[19]
APSP, n3
Sparse All Pairs Max Flows, n1.5
4
(7/4 -
- Approximate Sparse Diameter, n4/3
2-SUM, n

Figure 1: A partial web of known fine-grained reductions. We assume the following encoding of the input for various problems. For problems dealing with sequences of _n_ integers (Orthogonal Vectors, _k_-SUM, Edit Distance), the input is encoded in binary directly. Since one can assume that that the integers have absolute values bounded by a polynomial in _n_, \(s=\Theta(nlogn)\). For problems dealing with sparse graphs (Sparse All Pairs Max Flows and Sparse Diameter), the input is given as a list of edges, hence \(s=\Theta(nlogn)\). For the remaining graph problems, the input graph can be dense, so we encode it as its adjacency matrix, hence \(s=\Theta(n^2)\). For _k_-SAT, the input is a list of _m_ clauses, each of length at most _k_, hence \(s=\Theta(mlogn)\).

