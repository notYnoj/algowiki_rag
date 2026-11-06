and

\(\frac{v^\top L_{G_\ell} v}{v^\top L_Gv}\ge\prod_{i\in[\ell]}(1-\varepsilon_i)\ge 1-\sum_{i\in[\ell]}\varepsilon_i\ge 1-\frac{\varepsilon}{8}\ge 1-\varepsilon.\)

which concludes that \(G_\ell\) is an \(\varepsilon\)-spectral sparsifier of _G_ as wished.

## C Finding a Large Flow via Communication: Improved Analysis

The goal of this section is to prove Lemma 3.5, thereby concluding our minimum _s-t_ cut algorithm in the two-player communication model. We first state our main claim.

**Claim C.1.** _Let_ \(f,k,k'\) _be known parameters such that_ \(k'<k\le f\) _with a promise that_ \(\nu(G)\ge f\)_, and also given explicitly is a subgraph_ \(H\unknown G\) _with_ \(\nu(H)\ge f-k\)_. Then, there is a deterministic protocol which communicates_ \(\widetilde{O}\left(nf\cdot\frac{\sqrt{k}}{k'}\right)\) _bits and outputs_ \(H^\text{after}\unknown G\) _with_ \(\nu(H^\text{after})\ge f-k'\).

As a corollary, we can obtain a "promise" version of Lemma 3.5.

**Corollary C.2.** _Let f and_ \(\Delta\le f\) _be parameters with a promise that_ \(\nu(G)\ge f\)_.Then, there is a deterministic protocol which communicates_ \(\widetilde{O}\left(\frac{nf}{\sqrt{\Delta}}\right)\) _bits and outputs_ \(H\unknown G\) _with_ \(\nu(H)\ge f-\Delta\).

_Proof._ Use Claim C.1 recursively with \((k,k')=(f,f/2),\dots,(2\Delta,\Delta)\) with _H_ being _H_after from the previous iteration (for the first iteration, set \(H=\emptyset\).) Inductively, each iteration is successful to obtain \(\nu(H^\text{after})\ge f-k'\). Thus, upon the completion we obtain _H_ with \(\nu(H)\ge f-\Delta\). In total, the number of cut-queries made to _G_ is \(\widetilde{O}\left(\frac{nf}{\sqrt{\Delta}}\right)\) due to the geometric sum.

Now let’s prove Lemma 3.5 from Corollary C.2

**Lemma 3.5** (Finding a large flow via communication)**.** _Let G be an input graph, and let_ \(\Delta\le n\) _be an additive error parameter. Then, there is a deterministic protocol that computes_ \(H\unknown G\) _with_ \(\nu(H)\ge\nu(G)-\Delta\)_. The protocol uses_ \(\widetilde{O}\left(\frac{n\cdot\nu(G)}{\sqrt{\Delta}}+\frac{n\cdot\nu(G)^2}{\Delta^2}\right)\) _bits of communication and always succeeds._

_Proof._ Consider the following deterministic communication protocol.

1. Compute \(\hat{f}\) such that \(0.99\nu(G)\le\hat{f}\le 1.01\nu(G)\) using \(\widetilde{O}(n)\) bits via Lemma 2.12.<tbc>

2. If \(\hat{f}\le 0.99\Delta\), output \(H:=\emptyset\).<tbc>

3. Else, we have \(\hat{f}\ge 0.99\Delta\). Set \(\lambda=\frac{\Delta}{20\hat{f}}\le\frac{1}{10}\).<tbc>

4. Compute _f_ such that \((1-\lambda)\nu(G)\le f\le(1+\lambda)\nu(G)\) using \(O(n/\lambda^2)\) bits via Lemma 2.12.<tbc>

5. If \(f\le(1-\lambda)\Delta\), output \(H=\emptyset\).<tbc>

6. If \(f\ge(1-\lambda)\Delta\), use Corollary C.2 with \((f,\Delta)\leftarrow\left(\frac{f}{1+\lambda},\frac{\lambda f}{10}\right)\) and output such _H_.<tbc>

