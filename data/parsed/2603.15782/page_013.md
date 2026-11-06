_Proof of Theorems 1 and 5._ Theorem 11 and Proposition 10 give oracle implementations with and without Assumption 1, respectively. In both cases the oracle width is \(\rho=O(\alpha n^{-1+O(\varepsilon)}\text{polylog}(n))\). Thus, the number of iterations in Theorem 7 with \(\delta=\alpha/2\) is \(T=O\left(\frac{n^2\rho^2logn}{\alpha^2}\right)=n^{O(\varepsilon)}\text{polylog}(n)\). Moreover, \(\eta\rho T=O(\rho nlogn/\alpha)=n^{O(\varepsilon)}\text{polylog}(n)\). Since \(\gamma=\Omega(1/logn)\), Theorem 9 uses dimension _d=O_(log<sup>3</sup>_n_) and \(n^{O(\varepsilon)}\text{polylog}(n)\) matrix-vector products per iteration. Each such product can be computed in \(O(mn^{O(\varepsilon)}\text{polylog}(n))\) times, so we need \(O(mn^{O(\varepsilon)}\text{polylog}(n))\) extra time per iteration. This time is dominated by the runtime of the reduced oracle.

The total number of iterations will be \(T'=T\cdot O(logn)=T\cdot O(logn)\), since we need to run the algorithm inside the binary search over \(\alpha\in[1,8W]\). Each iteration succeeds with probability at least \(1-n^{-\Theta(1)}\), so all \(T'\) iterations succeed with probability at least \(1-T'n^{-\Theta(1)}\ge 1-o(1)\).

This gives the statements of Theorems 1 and 5, except that the complexities have factors \(n^{O(\varepsilon)}\) instead of \(n^\varepsilon\). Rescaling \(\varepsilon\) by an appropriate constant gives the desired results.

In Sections 6 and 7 below we describe the two implementations of the reduced oracle stated in Theorem 11. To simplify notation, we will assume that vectors \(\tilde{v}_i\) for \(i\in V\) are unique, and rename the nodes in _V_ so that \(\tilde{v}_x=x\) for each \(x\in V\) . Thus, we now have \(V\subseteq\mathbb{R}^d\). The "true" vector in R_<sup>n</sup>_ corresponding to \(x\in V\) is still denoted as _v<sub>x</sub>_.

For a path _p_=(_x,...,y_) we will denote \(\partial p=\{x,y\}\) to be the pair of its endpoints.

We write _u_∼N(0_,I<sub>d</sub>_) for a standard Gaussian vector in R_<sup>d</sup>_, whose components are independent N(0,1) variables. Notation \(\mathtt{Pr}_u[\cdot]\) denotes probability over this choice of _u_.

## 5 Maximum flow subroutine

Before presenting the two approaches, we describe a construction that will be used in both of them.

For disjoint subsets \(A,B\subseteq S\) and parameter \(\mu>0\) let \(\mathcal{N}(A,B,\mu)\) be the directed weighted graph with the nodes \(\{x^+,x^-:x\in V\}\cup\{e^-,e^+:e\in E\}\cup\{s,t\}\) and the edges

\(\bigcup_{x\in V}\underbrace{\{(x^+,x^-)\}}_{w(x)/2}\cup\bigcup_{e=xy\in E}\underbrace{\{(e^-,e^+),(x^-,e^-),(y^-,e^-),(e^+,x^+),(e^+,y^+)\}}_\infty\cup\bigcup_{x\in A}\underbrace{\{(s,x^+)\}}_\mu\cup\bigcup_{y\in B}\underbrace{\{(y^-,t)\}}_\mu\)

(The numbers below the edges indicate their weights).

An _s-t_ cut (_S_<sub>cut</sub>_,T_<sub>cut</sub>) in \(\mathcal{N}(A,B,\mu)\) will be called _valid_ if there is no node \(x\in V\) with \(x^+\in T_\mathrm{cut},x^-\in S_\mathrm{cut}\). An invalid cut can be converted to a valid one by moving _x_<sup>+</sup> to _S_<sub>cut</sub> whenever \(x^-\in S_\mathrm{cut}\); this transformation does not increase the cost of the cut. Let us define a mapping<tbc>

S
μ
x+
e+
y+
w(x)/2
w(xy)
w(y)/2
x
e
y
u
t

Figure 1: The network \(\mathcal{N}(\{x\},\{y\},\mu)\) for a graph consisting of one edge _e=xy_. Arc labels are capacities.

