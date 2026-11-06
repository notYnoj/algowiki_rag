<tbc>number of biased stretches of _Y_ is typically modest, which we combine with (3.26) to prove (3.22) uniformly over all \(\left(Y^{(1)},\dots,Y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(Y)\).

**Proposition 3.12** (Few biased stretches)**.** _With probability_ \(\ge 1-e^{-\Omega(N)}\)_, Y has_ \(\le M\cdot b^{-(1+2\epsilon)}\) _biased stretches._

_Proof._ It holds for any contiguous substring _Z_ of _Y_ of length \(\ell\le b^{1/2+2\epsilon}\) that

(3.27) \(\mathbb{P}\left(\Delta(Z)\ge b^{1/2-2\epsilon}\right)^{\left(\mathrm{Hoeffding}\right)}\le^{\left(\mathrm{Hoeffding}\right)}2\mathrm{exp}\left(-\frac{2\left(b^{1/2-2\epsilon}\right)^2}{4\ell}\right)^{\left(\ell\le b^{1/2+2\epsilon}\right)}2\mathrm{exp}\left(-\frac{b^{1/2-6\epsilon}}{2}\right).\)

So for any \(M/\ell\) disjoint contiguous substrings _Z(i_) of _Y_ , each with length at most \(\ell\le b^{1/2+2\epsilon}\),

(3.28) \(\mathbb{P}\left(\frac{1}{M/\ell}\sum_{i=1}^{M/\ell}\unknown\left\{\Delta\left(Z(i)\right)\ge b^{1/2-2\epsilon}\right\}\ge b^{-(4+8\epsilon)}\right)\)

(3.29) \(\le^{\left(\mathrm{Chernoff}\right)}\mathrm{exp}\left(-\frac{M}{\ell}\cdot D_\mathrm{KL}\left(b^{-(4+8\epsilon)}\right\|\left\|\frac{1}{M/\ell}\sum_{i=1}^{M/\ell}\mathbb{P}\left(\Delta\left(Z(i)\right)\ge b^{1/2-2\epsilon}\right)\right)\right)\)<br>
\(\le^{\left(\ell\le b^{1/2+2\epsilon}\right),(\mathrm{3}.27),(b\mathrm{large})}\mathrm{exp}\left(-\frac{M}{b^{1/2+2\epsilon}}\cdot D_\mathrm{KL}\left(b^{-(4+8\epsilon)}\right\|2e^{-b^{1/2-6\epsilon}/2}\right)\right)=e^{-\Omega(N)}.\)

We can handle (i.e., correspond to an indicator summand in (3.28)) all contiguous substrings of _Y_ of length \(\ell\le b^{1/2+2\epsilon}\) using

\(b^{1/2+2\epsilon}\cdot b^{1/2+2\epsilon}=b^{1+4\epsilon}\)

bounds of the form (3.29). Specifically, for each candidate length \(\ell\le b^{1/2+2\epsilon}\) of the contiguous substrings, we take some \(j\le\ell\) and sequentially equipartition the substring of _Y_ starting at position _j_ into contiguous substrings of length \(\ell\) until there are strictly fewer than \(\ell\) bits left. This produces at most \(M/\ell\) contiguous substrings of length \(\ell\), which we then correspond to the indicator summands studied in (3.29). Furthermore, any contiguous substring of _Y_ of length \(\le b^{1/2+2\epsilon}\) is contained in at most<tbc>

\(b^{1+\epsilon}\cdot b^{1+\epsilon}=b^{2(1+\epsilon)}\)

<tbc>biased stretches. This bound is observed by fixing the length of a candidate biased stretch to be at most \(b^{1+\epsilon}\), then counting the number of candidate biased stretches with said length that contain the contiguous substring of _Y_ . Altogether, a union bound over the conditions for all of the bounds (3.29) that we consider yields that with probability

\(\ge 1-b^{1+4\epsilon}\cdot e^{-\Omega(N)}=1-e^{-\Omega(N)},\)

there are at most

\(\underbrace{b^{1+4\epsilon}}_\mathrm{num.bds.ofform(3.29)}\cdot\underbrace{M\cdot b^{-(4+8\epsilon)}}_\mathrm{upperbd.from(3.29)}\cdot\underbrace{b^{2(1+\epsilon)}}_\mathrm{upperbd.onnum.biasedstretchesforaubstring}=M\cdot b^{-(1+2\epsilon)}\)

biased stretches in _Y_ . □

We now put everything together to derive the desired uniform approximation-type bound (3.22). Let \(y\in\{0,1\}^M\) be such a string with at most \(M\cdot b^{-(1+2\epsilon)}\) biased stretches. We fix an arbitrary induced near-equipartition

\(\left(y^{(1)},\dots,y^{(B)}\right)\in\mathcal{N}\mathcal{E}_\mathrm{ind}(y),\)

