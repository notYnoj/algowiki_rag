(_i)_ _there is a deterministic one-pass_ \((1+\varepsilon)\)_-approximation algorithm for_ Min-CSP(_R_) _using_ \(O_{R,\varepsilon}(\mathsf{NRD}_n(R^\star)\mathrm{polylog}(n,m,1/\varepsilon))\) _bits of space;_<tbc>

_(ii)_ _every randomized bounded-error one-pass finite-factor approximation algorithm for_ Min-CSP(_R_) _uses_ \(\Omega_R(\mathsf{NRD}_n(R^\star))\) _bits._

_Consequently,_

\(\Omega_R(\mathsf{NRD}_n(\mathrm{core}(R)))\le\mathsf{SPACE}(\mathsf{Min}-\mathsf{CSP}_{1+\varepsilon}(R))\le O_{R,\varepsilon}(\mathsf{NRD}_n(\mathrm{core}(R))\mathrm{polylog}(n,m,1/\varepsilon)).\)

We first prove Theorem 6.1. The proof of Corollary 6.2 is given at the end of the section.

## 6.1 Sparsification

At a high level, we use a sparsify-merge-sparsify procedure for building sparsifiers in insertion-only streams. These sparsifiers have been used before in insertion-only streams; see, for instance, \[McG14\]. The only sparsification result we need as a black box is the following theorem of Brakensiek and Guruswami.

**Fact 6.3** (\[BG25\])**.** _If_ \(\mathcal{C}\subseteq\{0,1\}^M\) _is a binary code and_ \(0<\eta<1\)_, then there is a nonnegative weight vector z such that_<tbc>

\(\langle z,c\rangle\in(1\pm\eta)\|c\|_1\text{\textit{for every}}c\in\mathcal{C},\)

<tbc>_and, for an absolute constant c_<sub>BG</sub>_\>_0,

\(|\mathrm{supp}(z)|\le c_\mathrm{BG}\mathsf{NRD}(\mathcal{C})\frac{\mathrm{log}_2^6(4M)}{\eta^2}.\) (6.4)

_Importantly, their proof allows z to be chosen with nonnegative integer entries. Indeed, their induction starts with unit weights and, in the recursive step, assigns weight_ 1 _to the explicitly retained coordinates and multiplies the recursively produced weights by_ 3.

Subsequent work sharpened and broadened this code-sparsification framework. Lovett, Meka, and Wang \[LMW26\] improved the dependence on the block length from polylogarithmic to logarithmic, while Khanna, Putterman, and Sudan \[KPS26\] developed a unified sparsification theory for nonnegative real-valued codes.

Note that in the above, NRD(C) refers to the largest _identity_ submatrix that can be found in C (when its vectors are listed as rows).

We now prove the following basic fact which shows that weighted instances (with small weights) can effectively be sparsified as _unweighted_ instances, just by repeating constraints.

**Lemma 6.5** (Integral-weight reduction)**.** _Let J be an integer-weighted R-instance on at most n variables. Let_<tbc>

\(W(J)=\sum_{C\in\mathrm{supp}(J)}w_J(C),\)

<tbc>_denote the total weight of the instance. For every_ \(0<\eta<1\)_, there is an integer-weighted subinstance_ \(\mathrm{Red}_\eta(J)\subseteq J\) _such that, simultaneously for every assignment_ \(\alpha\),

\(\mathrm{unsatval}_{\mathrm{Red}_\eta(J)}(\alpha)\in(1\pm\eta)\mathrm{unsatval}_J(\alpha),\) (6.6)

_and_

\(|\mathrm{supp}(\mathrm{Red}_\eta(J))|\le c_\mathrm{BG}\mathsf{NRD}_n(R)\frac{\mathrm{log}_2^6(4\mathrm{max}\{W(J),1\})}{\eta^2}.\) (6.7)

