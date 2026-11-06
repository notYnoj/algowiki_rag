_If all players use adaptive learning in the repeated mechanism, then the overall welfare satisfies_

\(\sum_t\mathbb{E}[S(D^t,a^t)]\ge\frac{\lambda}{\rho max\{1,\mu\}}\sum_t\mathbb{E}[\text{OPT}(D^t)]-\frac{nT}{max\{1,\mu\}}\sqrt{2p(1+n(\varepsilon+\delta))ln(NT)},\)

_where N_=max_<sub>i</sub>_|A_<sub>i</sub>|._

Note that if the problem of coordinating a high-welfare allocation has small coordination complexity this implies the existence of a jointly differentially private allocation algorithm with a high welfare guarantee. By combining Theorem 6 and Lemma 12, we obtain the following result.

**Lemma 13.** _Consider a mechanism with dynamic population_ (_M,T,p_) _such that the stage mechanism M is allocation based_ \((\lambda,\mu)\)_-smooth and_ \(T\ge 1/p\)_. Assume there is a coordination protocol_ \((\sigma,\pi)\) _with coordination complexity_ \(\ell\) _and approximation ratio_ \(\rho\) _for the corresponding welfare maximization problem._

_Then if all players use adaptive learning in the repeated mechanism, the average welfare satisfies_

\(\sum_t\mathbb{E}\left[S(D^t,a^t)\right]\ge\frac{\lambda}{\rho max\{1,\mu\}}\sum_t\mathbb{E}[\text{OPT}(D^t)]-\)<br>
\(inf_{\varepsilon>0}\left\{\frac{nT}{max\{1,\mu\}}\sqrt{4pn\varepsilon ln(NT)}+\frac{\lambda T}{\rho max\{1,\mu\}}\frac{2(\ell+log(n))}{\varepsilon}\right\}.\)

## 6 Coordination through Dynamics Simulation

In this section, we give another general technique for designing coordination protocols. The key idea is to broadcast a message that is sufficient for players to derive the sequence of actions that they would have executed in some joint dynamic that is known to converge to the solution to the coordination problem. Similar techniques have been used in the privacy literature, for example \[KMRW15\], \[HHR<sup>+</sup>14\] and \[RR14\]. We will focus on the application of coordinating an equilibrium flow in atomic routing games, which follows the general outline of \[RR14\].

A basic primitive that turns out to be broadly useful when writing down the transcript of some dynamic is being able to keep a running count of a stream of numbers. For many applications, in fact, it is sufficient to be able to maintain an _approximate_ count. Before we start, we introduce two subroutines for keeping track of the approximate count of a binary stream using low communication. The first one compresses a numeric stream \(\tau:[T]\rightarrow\{-1,0,1\}\) into a short message, and the second one decompresses it. See Algorithm 3 for the simple compression protocol.

**Algorithm 3** \(\text{ApproxCount}(\tau,r,T)\)

**Input:** a stream of numbers \(\tau:[T]\rightarrow\{-1,0,1\}\) and refinement parameter _r_

**Initialize:** a counter \(C:[T]\rightarrow\mathbb{N}\), a list of update steps \(U=\emptyset\)

**for** _t_=1_,...,T_:

**if** _t_=1: let _C(t_)=0; **else**: let _C(t_)=_C(t_-1)

**if** \(|C(t)-\sum_{i=1}^t\tau(i)|\ge r\):

**if** \(C(t)<\sum_{i=1}^t\tau(i)\) **then** _C(t_)=_C(t_-1)+_r_ and \(U\leftarrow U\cup\{(t,+)\}\)

**if** \(C(t)>\sum_{i=1}^t\tau(i)\) **then** _C(t_)=_C(t_-1)-_r_ and \(U\leftarrow U\cup\{(t,-)\}\)

**Output:** the list of time steps _U_

This algorithm releases a concise description _U_ that suffices to reconstruct an approximate running count _C(t_) of the stream.

