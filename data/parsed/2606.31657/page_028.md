inequality for EMD<sub>_d_<sub>H</sub></sub>,

\(\text{EMD}_{d_\mathrm{H}}\big(A(\Phi(m)),A(\Phi(m^{\oplus i}))\big)\le\sum_{t=1}^L\text{EMD}_{d_\mathrm{H}}\big(A(\Psi_{t-1}^{m,i}),A(\Psi_t^{m,i})\big).\)

Averaging over _m_ and _i_ and using item 1 completes the proof.

## The hard embedding is itself simple.

Define the explicit input embedding

\(x(m):=\mathrm{Enc}_{n,M}(\Phi(m))\in\{0,1\}^N.\)

Each output bit of _x_ is either a fixed variable-index bit or a sign bit of a clause in one gadget, and the sign pattern of that gadget is determined by a single local E3LIN2 test. Since the tester query complexity is constant, each output bit of _x_ depends on only _O_(1) message coordinates. Thus _x_ is computable by a linear-size _NC_<sup>0</sup> circuit. This is important for the randomized circuit corollary below: the hardness is not coming from a complicated front end, but from the randomized algorithm itself.

Because the relevant input family and output space are finite, any such randomized algorithm can be realized on a common finite probability space. We therefore fix a random seed _R_ and a realization \(A(\cdot;R)\) whose law is \(A(\cdot)\) on every input. For the rest of the section write<tbc>

\(F_R(m):=A(x(m);R)=\big(f_{1,R}(m),\dots,f_{n,R}(m)\big)\in\{0,1\}^n.\)

<tbc>For each fixed seed _r_ and output coordinate _v_, the slice \(f_{v,r}:\{0,1\}^k\rightarrow\{0,1\}\) is an ordinary Boolean function. For a Boolean function \(f:\{0,1\}^k\rightarrow\{0,1\}\), write<tbc>

\(\mathrm{Inf}(f):=\sum_{i=1}^k\mathbf{Pr}_{m\in\{0,1\}^k}\big[f(m)\neq f(m^{\oplus i})\big].\)

<tbc>We call

\(\mathrm{SCInf}(A):=\mathbb{E}_R\big[\sum_{v=1}^n\mathrm{Inf}(f_{v,R})\big]\)

the _seed-averaged cumulative influence_ of the pullback of _A_ to the hard family. When _A_ is deterministic, this is exactly the ordinary cumulative influence from the deterministic version of the section.

## Why the pullback is the right object.

The theorem above is already stated in the standard formula-input model. We pass to the cube coordinates \(m\in\{0,1\}^k\) because the classical structural results we want to invoke, i.e., junta theorems, pseudo-junta theorems, and average-sensitivity upper bounds for bounded-depth circuits and formulas, are formulated for Boolean functions on product spaces. Moreover, by Theorem 6.2, adjacent points of the hard cube map to formulas whose standard encodings differ in only _O_(1) bits, so the pullback does not create artificial hardness: it is simply a convenient coordinate system for an explicit, genuinely local subfamily of ordinary SAT inputs. The role of the random seed is only to turn the randomized algorithm into deterministic slices to which these classical Boolean-function bounds apply.

