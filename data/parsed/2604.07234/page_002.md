<tbc>We often write \(X'\) for an independent copy of _X_ to distinguish the null ambient string from the planted one, so that the null partition function is \(Z_{X^\prime,Y}\) and the planted one is _Z<sub>X,Y</sub>_.

## 1.1. Connections.

Before presenting our results, we connect the Random Subsequence Model to some longstanding problems in information theory, discrete probability, theoretical computer science, and statistical physics. The connections to problems in information theory are repeated here for the reader’s convenience from \[PIW24\], where the planted variant of the Random Subsequence Model was implicitly studied. For further such background, including connections to Slepian-Wolf theory and distributed storage, we refer the reader to the introduction of that paper.

### 1.1.1. _The deletion channel._

The _binary deletion channel with deletion probability_ \(p\in[0,1]\) is the communication channel which takes input \(x\in\{0,1\}^N\) and deletes each bit of _x_ independently with probability _p_ to produce a random output \(y\in\{0,1\}^*\). The deletion channel is often regarded as the canonical example of a channel with synchronization errors, that is, in which synchronization between input and output bit positions is lost. Dobrushin’s classical coding theorem for synchronization channels \[Dob67\] showed that the _capacity_ of the deletion channel, which can be thought of informally as the maximum rate at which one can reliably transmit information through the channel, admits the variational representation

\(lim_{N\rightarrow\infty} max_X\frac{1}{N}I\left(X;Y\right),\)

where the maximum is over all distributions of _X_ supported on {0,1}_<sup>N</sup>_, _Y_ is the output of the deletion channel on input _X_, and \(I(\cdot;\cdot)\) is the mutual information. Finding an analytic formula expressing the capacity above as a function of the deletion probability _p_ has been one of the outstanding problems of information theory over the past several decades.

A natural relaxation of the capacity problem is to consider _X_∼Unif{0,1}_<sup>N</sup>_ rather than optimizing over all possible laws of _X_. We refer to the corresponding limit

(1.2) \(lim_{N\rightarrow\infty}\frac{1}{N}I\left(X;Y\right),X\sim\text{Unif}\{0,1\}^N\)

as the _uniform capacity_ of the deletion channel, which gives a lower bound on the full channel capacity, and can be interpreted as the maximum rate that can be achieved with _uniformly random error correcting codes_. Uniformly random codes are of substantial importance as they are known to be asymptotically optimal (i.e., they achieve the channel capacity) in many well-understood memoryless channels like the binary symmetric channel and the binary erasure channel (e.g., see \[Sha48\]), the latter of which is often thought of as the memoryless analogue of the binary deletion channel. As such, uniform codes are widely studied throughout information theory and coding theory. While it is known (e.g., see \[DSV12\] and \[DM06\]) that uniform codes cannot achieve the capacity of the deletion channel for _p_ close to 1, we believe that studying uniformly-random codes in this setting is both interesting in its own right and potentially an important stepping stone towards the full capacity problem, since deriving an analytic formula or even a convincing conjectural expression for (1.2) is wide open.

The uniform capacity of the deletion channel is closely connected to the planted variant of the Random Subsequence Model, and this connection is the primary motivation for the present work. Specifically, it is easy to show (see Appendix A) that, letting \(\alpha=1-p\), one can write

(1.3) \(lim_{N\rightarrow\infty}\frac{1}{N}I(X;Y)=\alpha log2-h(\alpha)+lim_{N,M\rightarrow\infty M/N=\alpha}\frac{1}{N}\mathbb{E}\left[logZ_{X,Y}\right],\)

where all logs are taken base _e_ and

\(h(\alpha)=-\alpha log\alpha-(1-\alpha)log(1-\alpha)\)

