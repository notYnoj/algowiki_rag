<tbc>decision problems \[38\] and verification that a designated element is the maximum \[39\], rather than selection of one design at a fixed budget.

## 5 Rank laws of quantum algorithms

The classical degree bound limits how output probabilities can vary with rank. We now derive the corresponding bound for coherent comparisons and show that it can be attained. The factor two in the degree bound occurs because a probability is quadratic in the amplitudes.

**Theorem 2.** _Let_ \(n\ge 2\) _and let an admissible quantum algorithm use at most q calls to_ (1) _on every branch. After the symmetrization of Proposition 1, its rank law w<sub>t</sub>_=Pr\[_x<sub>I</sub>=t_\], \(t\in[n]\)_, is independent of the order and satisfies w<sub>t</sub>=p(t_) _for a polynomial p of degree at most_ min(2_q,n_-1)_. The degree bound is attained for every q and n._

_Proof._ Write sgn_<sub>ab</sub>(x_)=sgn(_x<sub>a</sub>-x<sub>b</sub>_)=(-1)<sup>**1**</sup><sub>{_x<sub>a</sub>\<x<sub>b</sub>_}</sub> for one orientation of each unordered pair. In the \(|\pm\rangle\) basis of the response bit, each call acts on the address sector (_a,b_) as \(\Pi_++\mathrm{sgn}_{ab}\Pi_-\), on the reversed sector (_b,a_) as \(\Pi_+-\mathrm{sgn}_{ab}\Pi_-\), and on a self-address as the identity. Every unnormalized Kraus trajectory with _k_ calls therefore has amplitudes of degree at most _k_ in the signs, and input-independent operations do not raise the degree. The unconditional probability of each output label is a sum over trajectories, Kraus indices and initial mixtures, so it has degree at most 2_q_. Using \(\mathrm{sgn}_{ab}^2=1\), the probability of output _a_ on order _x_ is

\(p_a(x)=\sum_{E:|E|\le 2q}c_{a,E}\prod_{\{u,v\}\in E}\mathrm{sgn}_{uv}(x),\) (7)

which is the polynomial method \[40\] written in comparison signs.

Regard a monomial in (7) as a graph _G_ with edge set _E_, add the output label _a_ as a vertex, and let the component of _a_ contain _k_ other vertices. Let \(\mu_j\) be the average of the sign product of a detached component _C<sub>j</sub>_ over its internal orders, and let \(\beta_h\) be the average sign product of the root component over the orders of its vertices in which exactly _h_ of the other _k_ vertices have a smaller rank than _a_, with \(\beta_0=1\) when _k_=0. For a uniform order _X_,

\(\mathbb{E}\big[\prod_{\{u,v\}\in E}\mathrm{sgn}_{uv}(X)\big|X_a=t\big]=\big(\prod_{j\ge 1}\mu_j\big)\frac{\sum_{h=0}^k\beta_h\genfrac(){pt}{2}{t-1}{h}\genfrac(){pt}{2}{n-t}{k-h}}{\genfrac(){pt}{2}{n-1}{k}}.\) (8)

To derive (8), we group the orders with _X<sub>a</sub>=t_ by the rank sets assigned to the graph components. Within each group, internal assignments are independent and uniform, with rank _t_ fixed at _a_. Each detached component contributes its average sign product \(\mu_j\). The root component’s other _k_ ranks form a uniform subset of \[_n_\]\\{_t_}, so the probability that exactly _h_ fall below _t_ is the displayed hypergeometric weight. The right side of (8) has degree at most \(k\le\mathrm{min}(|E|,n-1)\) in _t_. The symmetrized law is \(w_t=n^{-1}\sum_a\mathbb{E}[p_a(X)|X_a=t]\), which proves the bound.

For attainment, pick a uniform root label _a_ and a uniform _d_-subset of the other labels, with _d_=min(2_q,n_-1). Pair these labels. For a pair {_u,v_}, prepare a selector qubit in \(|+\rangle\) and the response in \(|-\rangle\), encode the selector into the addresses (_a,u_) and (_a,v_), call the oracle once and undo the encoding. Apply a Hadamard gate to the selector and measure it to determine the product sgn_<sub>au</sub>_sgn_<sub>av</sub>_ exactly \[41\]. If _d_ is odd, read the last sign with one more call. Output<tbc>

