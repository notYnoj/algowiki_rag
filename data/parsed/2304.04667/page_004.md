<tbc>showing that for most settings of All-Pairs Max-Flow, deterministic SETH-based reductions proving _n_<sup>4-_o_(1)</sup> conditional lower bounds can be ruled out assuming a hypothesis called NSETH<sup>10</sup> \[CGI<sup>+</sup>16\]. We do so by designing subquartic nondeterministic algorithms<sup>11</sup> suited for each setting, and then applying a non-reducibility framework by Carmosino et al. \[CGI<sup>+</sup>16\]. First, we present a general method by which we obtain our nondeterministic algorithms. In what follows, the volume of an _st_-flow _f<sub>st</sub>_, denoted **volume**(_f<sub>st</sub>_), is the number of edges in the support of _f<sub>st</sub>_ in the input graph.

**Informal Theorem 1.2.** _Suppose there is a randomized Las Vegas algorithm for All-Pairs Max-Flow that makes q Max-Flow calls on input graphs G_=(_V,E_) _and spends_ \(\hat{O}(t)\) _time outside of these calls, and let_ \(\mu\) _be a volume upper bound on the maximum st-flow in G, for all pairs_ \(s,t\in V\) _. Then there is a nondeterministic algorithm for All-Pairs Max-Flow with time_ \(\hat{O}(q\cdot\mu+n^{\omega(log_nq,1,1)}+t)\)<sup>12</sup>.

Note that for \(\omega=2\), this time becomes \(\hat{O}(q\cdot\mu+qn+t)\). In the remaining of this section we present our non-reducibility results for each variant.

<sup>10</sup>The Nondeterministic Strong Exponential Time Hypothesis (NSETH) asserts that SETH holds against co- nondeterministic algorithms. <sup>11</sup>A nondeterministic algorithm can make guesses (i.e. nondeterministic choices) and eventually produce either a correct output, or "don’t know" (i.e. aborts). Importantly, every input has at least one sequence of guesses leading to a correct output. <sup>12</sup>\(\omega(a,b,c)\) is the time it takes to multiply an \(n^a\times n^b\) matrix by an \(n^b\times n^c\) matrix.

n5
Running time
combinatorial
n4
n1/5 (alg. (HLSW'23)
n2m (alg. trivial)
n2 (alg. here, lower bound (HLSW'22)
n3
n2 (alg. here, if = 2, here)
mn (nondet. alg. if (SETH lower bound, here)
n3/2 + n2 (SETH lower bound, here)
n2
n
n5/4
n3/2
n7/4
n2
Value of m

Figure 1: New and old bounds for All-Pairs Max-Flow on undirected graphs with unit node-capacities.

