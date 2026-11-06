If we choose the graph defining a binary or nonbinary homological cycle code uniformly at random from all simple _D_-regular graphs, with \(D\ge 3\) fixed, the resulting ensemble has no positive reliability threshold. That is, for every fixed 0_\<p\<_1-1_/q_, independently changing each symbol with probability _p_, uniformly among the other _q_-1 values, and then using a maximum-likelihood decoder leaves a whole-word error probability, averaged over the graph, that is bounded away from zero as the block size grows. The reason is that short cycles persist with nonvanishing probability, and a fixed pattern of errors on a short cycle can give a competing codeword higher likelihood regardless of the errors elsewhere in the graph. In the binary case, this follows by combining the classical cycle-error criterion \[NZ16, §2.2\] with the short-cycle statistics of random regular graphs \[MWW04\]. We prove the corresponding error-floor bound over every finite field in §3.2, Theorem 3.

Therefore, rather than considering uniformly random _D_-regular graphs without restriction, we consider the _Linial-Simkin random greedy ensemble_ \[LS20\]. Specifically, let _G_ have _n_ labelled vertices and _m=Dn/_2 edges. Fix \(D\ge 3\), a girth coefficient \(c\in(0,1)\), and _n_ even, and put

\(g(n):=\mathrm{max}\{3,\lfloor c\mathrm{log}_{D-1}n\rfloor\}.\) (1)

The Linial-Simkin ensemble consists of simple, connected graphs with girth at least _g(n_). The ensemble is most easily defined by an algorithm for sampling from it, which we do in Definition 4. Throughout the threshold analysis, the block length tends to infinity first, with _D_, _q_, _c_, and _p_ fixed; only afterward do we vary _D_ and _q_.

Given a graph _G_, and a corresponding homological code _C<sub>G</sub>_, we consider the success probability of a maximum-likelihood decoder given a codeword from _C<sub>G</sub>_ in which each symbol has been independently corrupted with probability _p_. Specifically, a corrupted symbol is replaced with another of the _q_-1 elements of F_<sub>q</sub>_ uniformly at random. Let \(P_\mathrm{W}^\mathrm{ML}(G,p)\) denote the probability that a maximum-likelihood decoder fails to recover the correct original codeword. Let E_<sub>G</sub>_ denote the expectation with _G_ drawn from the Linial-Simkin ensemble. Define the reliability threshold by

\(\delta_\mathrm{rel}(D,q):=\mathrm{sup}\big\{p\in[0,1-1/q]:\unknown_GP_\mathrm{W}^\mathrm{ML}(G,p)\rightarrow 0\text{as}n\rightarrow\infty\big\}.\) (2)

The notation \(\delta_\mathrm{rel}(D,q)\) suppresses the fixed girth coefficient _c_.  1 compares two complementary guarantees: _reliable recovery_, where the ML word-error probability tends to zero, and _asymptotically certain failure_, where it tends to one.

For _q=o(D_<sup>2/3</sup>), including fixed _q_ as \(D\rightarrow\infty\), the success and failure bounds are asymptotically equal to (_q_-1)/(4_D_<sup>2</sup>). The explicit finite-parameter statement uses the simple-cycle value<tbc>

\(\delta_\mathrm{cyc}(D,q):=\frac{q-1}{(D-1)\big(\sqrt{D+q-2}+\sqrt{D-2}\big)^2}.\) (3)

<tbc>Whenever \(q/D^{2/3}\le 1/32\), Theorem 5 gives

\(\unknown_GP_\mathrm{W}^\mathrm{ML}(G,p)\rightarrow\left\{\begin{array}{ c c }
0, & 0<p<(1-16q/D^{2/3})\delta_\mathrm{cyc}(D,q), \\
1, & \delta_\mathrm{cyc}(D,q)<p<1-1/q.
\end{array}\right.\) (4)

In fact, \(\unknown_GP_\mathrm{W}^\mathrm{ML}(G,p)\rightarrow 1\) for \(\delta_\mathrm{cyc}(D,q)<p<1-1/q\) holds at every fixed \(D\ge 3\) and _q_. In the binary case \(\unknown_GP_\mathrm{W}^\mathrm{ML}(G,p)\) is known to converge to a perfect step function with transition at \(\delta_\mathrm{cyc}(D,2)\) for every \(D\ge 3\) \[DZ97; NZ16\].

