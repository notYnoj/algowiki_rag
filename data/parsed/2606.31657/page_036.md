## A Proof of Lemma 2.5

It suffices to exhibit an encoder _f_ whose image is _C_ and whose message coordinates appear in fixed positions after a permutation of coordinates. Since _C_ is linear, \(C=M\mathbb{F}_p^k\) for some \(M\in\mathbb{F}_p^{n\times k}\) of rank _k_. By the definition of rank, there exists a set of indices \(I=\{i_1,i_2,\dots,i_k\}\subseteq[n]\) such that the rows of _M_ indexed by _I_ span \(\mathbb{F}_p^k\). Let \(\Pi\in\mathbb{F}_p^{n\times n}\) be the permutation matrix that moves the coordinates in _I_ to the first _k_ positions and let \(\widetilde{M}:=\Pi M\). The first _k_ rows of \(\widetilde{M}\) span \(\mathbb{F}_p^k\), so the projection matrix \(P\in\mathbb{F}_p^{k\times n}\) onto those rows satisfies that \(P\widetilde{M}\) is invertible. Define \(\tilde{f}(m):=\widetilde{M}(P\widetilde{M})^{-1}m\) for \(m\in\mathbb{F}_p^k\). We have

1. \(\tilde{f}(\mathbb{F}_p^k)=\widetilde{M}\mathbb{F}_p^k=\Pi C\);<tbc>

2. The first _k_ coordinates of \(\tilde{f}(m)\) equal \(P\tilde{f}(m)=P\widetilde{M}(P\widetilde{M})^{-1}m=m\).<tbc>

<tbc>Thus \(\tilde{f}\) is a systematic encoder for the permuted code \(\Pi C\), witnessing that \(\Pi C\) is systematic with the same parameters. Undoing the permutation shows that _C_ becomes systematic after the fixed coordinate permutation \(\Pi\), as claimed.

