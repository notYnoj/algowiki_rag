To make the matrix multiplication tensors appearing in (1.2) "square" (i.e., of the form \(\langle p,p,p\rangle\)), we use the symmetrisation operation \(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot T\) for any tensor _T_, the tensor product of the six tensors obtained from _T_ by permuting its legs. For all integers \(k,\ell,m\ge 1\),<tbc>

\(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\langle k,\ell,m\rangle\cong\langle k\ell m,k\ell m,k\ell m\rangle^{\otimes 2},\)

<tbc>which depends only on the product \(k\ell m\). In particular, the symmetrisation of \(\langle 1,1,n\rangle\) is \(\langle n,n,n\rangle^{\otimes 2}\), and that of \(\langle 2a-1\rangle\) is \(\langle 2a-1\rangle^{\otimes 6}\). So symmetrising both sides of (1.2) gives

\(\langle 2a-1\rangle^{\otimes 6}\otimes\langle n,n,n\rangle^{\otimes 2}\supseteq\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\big(\langle a,1,s\rangle\oplus_1\langle 1,a,t\rangle\big).\) (1.3)

From the right-hand side of (1.3) we will construct an asymptotic restriction to one square matrix multiplication tensor (in a manner reminiscent of the laser method, but simpler):

\(\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\big(\langle a,1,s\rangle\oplus_1\langle 1,a,t\rangle\big)\unknown\langle a(s+t),a(s+t),a(s+t)\rangle^{\otimes 2}.\) (1.4)

The idea of the proof of (1.4) is to take the _N_th tensor power of \(\langle a,1,s\rangle\oplus_1\langle 1,a,t\rangle\), for large _N_, and to keep only its summands with a fixed number _k_ of factors \(\langle a,1,s\rangle\). These are \(h:=\genfrac(){pt}{2}{N}{k}\) tensors that share the first leg, each isomorphic to \(M:=\langle a^k,a^{N-k},s^kt^{N-k}\rangle\). By ingredients (D2) and (D1), with \(\mathsf{P}_{1,h}\cong\langle 1,1,h\rangle\) and \(\mathsf{P}_{h,h}\triangleleft\langle 2h-1\rangle\), their partial direct sum _Y_ satisfies

\(\langle h\rangle\otimes\big(M\otimes\langle 1,1,h\rangle\big)\triangleleft\langle 2h-1\rangle\otimes Y.\)

The left-hand side consists of _h_ copies of \(M\otimes\langle 1,1,h\rangle\), and the right-hand side of fewer than 2_h_ copies of _Y_ . The product of the three parameters of \(M\otimes\langle 1,1,h\rangle\) is \(a^N\genfrac(){pt}{2}{N}{k}s^kt^{N-k}\). For the _k_ at which \(\genfrac(){pt}{2}{N}{k}s^kt^{N-k}\) is largest, this product is at least (_a(s+t_))_<sup>N</sup>/(N_+1), since the _N_+1 numbers \(\genfrac(){pt}{2}{N}{k}s^kt^{N-k}\) add up to (_s+t)<sup>N</sup>_. The factors 2 and _N_+1 do not matter as \(N\rightarrow\infty\), and the symmetrisation makes the result square.

Composing the degeneration (1.3) and the asymptotic restriction (1.4) gives<tbc>

\(\langle 2a-1\rangle^{\otimes 6}\otimes\langle n,n,n\rangle^{\otimes 2}\unknown\langle a(s+t),a(s+t),a(s+t)\rangle^{\otimes 2}.\) (1.5)

<tbc>Suppose (essentially without loss of generality, after taking tensor powers and rounding down) that _a(s+t_)=_cn_ for an integer \(c\ge 2\). Then \(\langle cn,cn,cn\rangle\cong\langle c,c,c\rangle\otimes\langle n,n,n\rangle\), and (1.5) reads<tbc>

\(\langle 2a-1\rangle^{\otimes 6}\otimes\langle n,n,n\rangle^{\otimes 2}\unknown\langle c,c,c\rangle^{\otimes 2}\otimes\langle n,n,n\rangle^{\otimes 2}.\)

<tbc>Then \(\langle n,n,n\rangle^{\otimes 2}\) acts as a catalyst: it is needed as input, but also returned as an output. A common nonzero tensor factor can be cancelled in an asymptotic restriction \[WZ26, Lemmas 3.5 and 3.7\], which for us gives

\(\langle 2a-1\rangle^{\otimes 6}\unknown\langle c,c,c\rangle^{\otimes 2},\)

so \(\omega_\mathbb{F}\le 3log(2a-1)/logc\).

## 1.2.3 Concrete example of applying ingredients (D3) and (D4)

As a concrete example (already leading to a non-trivial upper bound on \(\omega_\mathbb{F}\)), we now carry out the above steps for _a_=2. Ingredients (D3) and (D4) turn four copies of P<sub>2,2</sub> into matrix<tbc>

