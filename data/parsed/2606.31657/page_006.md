### Locality Lower Bounds for the Non-signaling Model.

Our sensitivity bounds remain strong even in the non-signaling model, which strictly generalizes classical LOCAL, quantum-LOCAL, and bounded-dependence models: satisfiable Max E3LIN2 still requires locality \(\Omega(logn)\), and bipartite Max Cut requires locality \(\Omega(log(1/\varepsilon))\).

In the _non-signaling model_ \[1, 2, 11, 20\], given a graph _G_=(_V,E_), we can produce an arbitrary output distribution as long as it does not violate the non-signaling principle: for any set of vertices \(S\subseteq V\) , modifying the structure of the input graph at more than a distance _t_ from _S_ does not affect the output distribution of _S_. The parameter _t_ is called the _locality_ of the model. This model is stronger than any "physical" synchronous distributed computing model, and in particular, it contains classical LOCAL \[35\], quantum-LOCAL \[20\], and the bounded-dependence model \[29\]. Consequently, any locality lower bound in the non-signaling model applies automatically to these models.

The following observation from \[15\] connects locality to sensitivity. Suppose we generate a distribution in the non-signaling model for a graph problem with locality _t_. Sampling from this distribution and outputting the result yields an algorithm whose sensitivity is \(O(\Delta^t)\), where \(\Delta\) denotes the maximum degree, because deleting an edge can affect the marginal distributions of at most \(\Delta^t\) vertices. Because the CSP instance produced by the _c_<sup>3</sup>-LTC \[12, 38\] has constant degree, Theorem 1.2 translates into the following lower bound:

**Theorem 1.7.** _There exists_ \(\varepsilon>0\) _such that any_ \((1-\varepsilon)\)_-approximate non-signaling distribution for Max E3LIN2 must have locality_ \(\Omega(logn)\)_, even on satisfiable instances._

Marwaha and Hadfield \[36\] showed that achieving a \((1-\varepsilon)\)-approximation on satisfiable instances already requires \(\Omega(logn)\) rounds in quantum-LOCAL, and Fleming and Yoshida \[15\] proved the same locality bound in the non-signaling model for general instances. Our theorem unifies these results by establishing that even satisfiable Max E3LIN2 instances demand \(\Omega(logn)\) locality for non-signaling distributions.

Similarly, Theorem 1.3 yields the following lower bound for the non-signaling model:

**Theorem 1.8.** _There exists a constant_ \(\varepsilon_0>0\) _such that for every even n and every_ \(0<\varepsilon\le\varepsilon_0/\sqrt{n}\)_, any_ \((1-\varepsilon)\)_-approximate non-signaling distribution for the maximum cut problem on bipartite graphs must have locality_ \(\Omega(log(1/\varepsilon))\).

Hence setting \(\varepsilon=n^{-\delta}\) for any small constant \(\delta>0\) forces locality \(\Omega(logn)\). The previously best locality barrier on bipartite graphs is that any _one-round_ quantum-LOCAL algorithm achieves at most a \((\frac{1}{2}+\frac{1}{\sqrt{2d}})\)-approximation on _d_-regular bipartite graphs \[3\]. No stronger locality lower bound was known that rules out \((1-\varepsilon)\)-approximations on bipartite inputs, even for LOCAL.

On general graphs, there exist \((1-\varepsilon)\)-approximation algorithms in LOCAL (and even CONGEST) that run in \(O(poly(1/\varepsilon)\cdot logn)\) rounds \[9\]. By contrast, Fleming and Yoshida \[15\] showed an \(\Omega(logn)\) locality lower bound in the non-signaling model for achieving \((1-\varepsilon)\) approximation for some \(\varepsilon>0\).

## 1.2 Proof Overview

We first sketch the argument underlying Theorem 1.1 and then outline how it yields Theorems 1.2 and 1.3.

### An analogy between optimization problems and systematic LTCs.

We exploit a tight parallel between optimization problems and systematic LTCs, where _systematic_ means that the encoder copies the _k_ message symbols verbatim into designated coordinates, inducing a canonical input/output split. We write \(x\sim x'\) for neighboring instances.

