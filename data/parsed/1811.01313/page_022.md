<tbc>The total expected communication therefore becomes:<tbc>

\(O\left(nlg(\sqrt{rw/n}+2)+\sqrt{nwr}lg(\sqrt{nw/r})\right)=O\left(nlg(\sqrt{rw/n}+2)+\sqrt{nwr}lg(nw/r)\right).\)

<tbc>Observe now that \(\sqrt{rw/n}\ge 2\Rightarrow r\ge n/w\). For such _r_, it also holds that \(\sqrt{nwr}\ge n\). Moreover, \(lg(nw/r)=\Omega(lg(\sqrt{rw/n}))\) for all choices of \(r\le nw\) (which is the maximum possible _r_). Therefore, the whole expression simplifies to:

\(O\left(n+\sqrt{nwr}lg(nw/r)\right).\)

## 4.2 Oblivious Sorting and Permuting

In this section we prove Theorem 4, i.e. that there is an \(\Omega(nlgn)\) lower bound for oblivious word-RAM sorting algorithms when the integers and word size are \(\Theta(lgn)\) bits. In fact, we prove something slightly stronger, namely an I/O lower bound of \(\Omega((n/B)lg_{2M/B}(n/B))\) for oblivious permuting (with error probability 1/3). Theorem 4 follows by setting \(B=\Theta(1)\) and \(M=\Theta(B)=\Theta(1)\).

Observe that for an oblivious algorithm A, the memory access pattern is always the same. This means that the I/O-graph _G_ corresponding to an execution of A is the same for all inputs. We can now fix the randomness of A to obtain a deterministic algorithm A<sup>∗</sup> that is correct on at least a (2/3)-fraction of all possible inputs. Re-executing the argument in the proof of Lemma 10, we get:

**Lemma 12** _There exists a permutation_ \(\pi\) _and a collection of values_ \(\mathcal{F}\subseteq\{\{0,1\}^w\}^n\) _such that in the I/O-graph G corresponding to_ A_’s execution, the following holds:_

1. _For all_ \((d_1,\dots,d_n)\in\mathcal{F}\) _it holds that the algorithm_ A _executed on the input array A corresponding to inputs_ \(\pi\) _and d_<sub>1</sub>_,...,d<sub>n</sub> results in the I/O-graph G and_ A<sup>∗</sup> _is correct on A._<tbc>

2. \(|\mathcal{F}|\ge 2^{nw-1}\).<tbc>

_3._ _There are at least_ (4/5)_n indices_ \(i\in\{1,\dots,n\}\) _for which_ \(dist(\pi,i,G)\ge(1/2)lg_{2m/b}(nw/b)\).

**Proof.** We only sketch the proof as it follows the proof of Lemma 10 uneventfully. First observe that by Markov’s inequality, there are at least _n!/_3 permutations \(\pi'\) for which A<sup>∗</sup> errs on at most (1/3)(3/2)2<sup>_nw_</sup>=2<sup>_nw_-1</sup> of the input arrays corresponding to \(\pi'\) and a set of bit strings (_d_<sub>1</sub>_,...,d<sub>n</sub>_). In the proof of Lemma 10, we saw that there are no more than _n!/(nw/b_)<sup>_n/_20</sup> permutations with more than _n/_5 indices _i_ such that \(dist(\pi,i,G)<(1/2)lg_{2m/b}(nw/b)\). The lemma follows immediately.

Re-executing the proof of Theorem 2 using Lemma 12 instead of Lemma 10, we see that the constraint \(|\mathcal{F}|\ge 2^{nw-o(nw)}\) is trivially satisfied. Moreover, Lemma 12 has no constraints on _t_ like there was in Lemma 10. Thus the only constraint we get is \(t=\Omega((nw/b)lg_{2m/b}(nw/b))=\Omega(n/Blg_{2M/B}(n/B))\) as claimed. We have thus shown:

**Theorem 13** _Assuming Conjecture 1, any oblivious randomized algorithm for the external memory permutation problem, having error probability at most_ 1/3_, must make an expected_

\(\Omega\big(\frac{n}{B}\cdot lg_{2M/B}\frac{n}{B}\big)\)

_I/Os._

We note that Theorem 4 follows as an immediate corollary by setting \(B=\Theta(1)\) and \(M=\Theta(B)\).<tbc>

