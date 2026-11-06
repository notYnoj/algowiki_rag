## 5.1. A conjectural formula for \(f_\mathrm{pl}(\alpha)\).

We recall that our main motivation in this paper is the identity (1.3), which reduces the problem of computing the uniform capacity of the deletion channel to understanding the planted quenched free energy \(f_\mathrm{pl}(\alpha)\) with \(\alpha=1-p\). While Theorem 1.3 gives an exact formula for the corresponding annealed free energy, the problem of computing the quenched free energy is likely to be much more challenging. In particular, as suggested by Figure 1, we expect the following analogue of Theorem 1.1 to hold. In words, Conjecture 5.1 states that the Jensen gap corresponding to the planted Random Subsequence Model is also always nontrivial, just as it was for the null model.

**Conjecture 5.1.** _It holds for any_ \(\alpha\in(0,1)\) _that_

\(f_\mathrm{pl}(\alpha)<f_\mathrm{pl}^\mathrm{ann}(\alpha).\)

Given the suspected difficulty of exactly determining the value \(f_\mathrm{pl}(\alpha)\), a first step is to at least aim for a convincing conjectural description of this quantity. We illustrate why even non-rigorously deriving such a prediction for this free energy is challenging, by considering two very natural approaches to this problem and discussing the key obstructions that each approach encounters.

**The replica method.** In light of Theorem 1.3, perhaps the most natural candidate method for deriving a prediction is with a replica calculation. Let \(Z=Z_{X^\prime,Y}\) be under the null law on independent uniform strings \(X'\in\{0,1\}^N\) and \(Y\in\{0,1\}^M\). By Nishimori’s identity, if (_X,Y_) are distributed according to the planted law, we have<tbc>

\(\mathbb{E}[\mathrm{log}Z_{X,Y}]=\left.\frac{\mathbb{E}[Z\mathrm{log}Z]}{\mathbb{E}[Z]}=\left.\frac{\partial}{\partial q}\mathrm{log}\mathbb{E}[Z^q]\right|_{q=1}.\)

<tbc>Thus, a replica computation for \(f_\mathrm{pl}(\alpha)\) would begin by studying<tbc>

\(\Phi_r(\alpha):=\mathrm{lim}_{N\rightarrow\infty}\frac{1}{N}\mathrm{log}\mathbb{E}[Z^r]\text{for integers}r\ge 1,\)

<tbc>and then seeking (non-rigorous) continuation in the replica number. The difficulty is that the integer moments already appear to be highly nontrivial. Indeed, for \(r\in\mathbb{N}\),

(5.1) \(\mathbb{E}[Z^r]=\sum_{\sigma^1,\dots,\sigma^r\in\Sigma_{N,M}}\mathbb{P}\left(X_{\sigma^1}=\cdots=X_{\sigma^r}=Y\right).\)

For a fixed _r_-tuple \(\left(\sigma^1,\dots,\sigma^r\right)\), this probability depends on the full structure of the bipartite union graph \(G=G\left(\sigma^1,\dots,\sigma^r\right)\) on vertex set \([M]\sqcup[N]\) obtained by connecting each \(j\in[M]\) to those \(\sigma^a(j)\in[N]\) used by the replicas for \(a\in[r]\). More precisely, we have that

\(\mathbb{P}\left(X_{\sigma^1}=\cdots=X_{\sigma^r}=Y\right)=2^{\kappa(G)-(M+N)},\)

where \(\kappa(G)\) is the number of connected components of _G_. Thus the contribution of a replica configuration is not determined merely by a pairwise overlap matrix on configurations in \(\Sigma\) for values \(r\ge 3\), as was the case in Section 4, which is equivalent to the _r_=2 case of the above computation. Starting at _r_=3, tuples with the same pairwise overlap statistics can have different union graph topology and hence different weights in (5.1). In particular, there does not seem to be a candidate finite-dimensional order parameter in terms of which the replica computation can be closed.

**The cavity method.** Another appealing route is via the cavity method. Starting from the recursion of (1.4) applied to the entire strings \((X,Y)\in\{0,1\}^N\times\{0,1\}^M\), i.e.,<tbc>

\(Z_{N,M}=\unknown\{X_N=Y_M\}Z_{N-1,M-1}+Z_{N-1,M},\)

<tbc>we can eventually obtain

\(\mathbb{E}\left[\mathrm{log}Z_{N,M}\right]-\mathbb{E}\left[\mathrm{log}Z_{N-1,M}\right]=-\mathbb{E}\left[\mathrm{log}\langle\sigma_1\neq 1\rangle_{N,M}\right],\)

