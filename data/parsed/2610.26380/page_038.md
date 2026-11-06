<tbc>To illustrate what the interaction terms represent, we write them explicitly for three examples. The order-zero interaction term is the value with no further evaluation, \(\Gamma_\emptyset=V_\mathrm{myopic}(0|p_{t-1})=0\). For a single evaluation \(u\in\{1,\dots,U\}\), \(\Gamma_{\{u\}}=V_\mathrm{myopic}(n_{\{u\}}|p_{t-1})-V_\mathrm{myopic}(0|p_{t-1})\) is its standalone value of information. For a pair of distinct evaluations \(\{u,u'\}\),

\(\Gamma_{\{u,u^\prime\}}=V_\mathrm{myopic}(n_{\{u,u^\prime\}}|p_{t-1})-V_\mathrm{myopic}(n_{\{u\}}|p_{t-1})-V_\mathrm{myopic}(n_{\{u^\prime\}}|p_{t-1})+V_\mathrm{myopic}(0|p_{t-1})\)

is the net value of observing the two evaluations together beyond the sum of their individual effects. Applying the Boolean Möbius inversion to the set function \(G\mapsto V_\mathrm{myopic}(n_G|p_{t-1})\) gives Lemma A.1, which says we can write _V_<sub>myopic</sub>(_n|p_<sub>_t_-1</sub>) as the sum of the \(\Gamma_H\) terms.

LEMMA A.1 **(Boolean Möbius inversion)**. _For a batch with count matrix n and positions_ {1_,...,U},_

\(V_{myopic}(n|p_{t-1})=\sum_{H\subseteq\{1,\dots,U\}}\Gamma_H.\)

We next define the truncated approximation. For any integer \(w\ge 1\), define the order-_w_ truncation \(\widehat{V}_{\mathrm{myopic},w}(n|p_{t-1}):=\sum_{H\subseteq\{1,\dots,U\},|H|\le w}\Gamma_H\).

APPROXIMATION A.1. _We approximate_ \(V_{myopic}(n|p_{t-1})\approx\widehat{V}_{myopic,w}(n|p_{t-1})\) _with error_

\(V_{myopic}(n|p_{t-1})-\widehat{V}_{myopic,w}(n|p_{t-1})=\sum_{H\subseteq\{1,\dots,U\},|H|\ge w+1}\Gamma_H.\)

If there are no interaction terms of higher order than _w_, i.e., if the batch size is at most _w_, then the approximation is exact. This truncation makes the value function tractable, while still allowing us to capture some of the interaction effects between evaluations in a batch. Every retained interaction term involves computing _V_<sub>myopic</sub> on sub-batches of size at most _w_, which requires sums over at most 2_<sup>w</sup>_ outcome vectors with multivariate normal CDFs of dimension at most _w_, regardless of the batch size _U_.

## A.2.3. Batch construction

Using Approximation A.1 for some fixed _w_, we build batches in a similar fashion to Algorithm 4. Consider a partially committed batch (_i_<sub>1</sub>_,j_<sub>1</sub>)_,...,(i<sub>U</sub>,j<sub>U</sub>_) with count matrix _n_. For a (feasible) candidate evaluation \((i,j)\in\mathcal{I}\), appended to the batch as (_i_<sub>_U_+1</sub>_,j_<sub>_U_+1</sub>), define its marginal gain by

\(\Delta_n^{(w)}((i,j)):=\widehat{V}_{\mathrm{myopic},w}(n+F^{ij}|p_{t-1})-\widehat{V}_{\mathrm{myopic},w}(n|p_{t-1})=\sum_{H\subseteq\{1,\dots,U\},|H|\le w-1}\Gamma_{H\cup\{U+1\}}.\) (A.5)

In words, the marginal gain of (_i,j_) under Approximation A.1 is the sum, over all subsets of at most _w_-1 already committed evaluations, of the interaction term of that subset together with the new candidate evaluation.

Starting from the empty batch, we repeatedly add the feasible candidate with the largest per-unit-resource marginal gain. As discussed in §2.3, all marginal gains may be zero, in which case we fall back to the evaluation that Algorithm 4 would choose. We use the elastic round budgets of §6.1. The procedure terminates<tbc>

