### Furedi Hajnal limits.

For a permutation \(\pi\), let \(\mathrm{ex}_\pi(n)\) denote the maximum number of 1-entries in a \(\pi\)-avoiding \(n\times n\) binary matrix. The celebrated _Marcus-Tardos theorem_ \[MT04\], previously known as the _Füredi-Hajnal conjecture_, states that \(\mathrm{ex}_\pi(n)\) is at most _O(n_) for each fixed \(\pi\). It was observed by Cibulka \[Cib09\] that the limit \(c_\pi=\mathrm{lim}_{n\rightarrow\infty}\frac{1}{n}\mathrm{ex}_\pi(n)\) exists. This limit is known as the _Füredi-Hajnal limit_ of \(\pi\). Furthermore, we have \(\mathrm{ex}_\pi(n)\le c_\pi\cdot n\) for all _n_ due to the superadditivity of \(\mathrm{ex}_\pi(\cdot)\) \[Cib09\], which easily extends to rectangular matrices.

**Lemma 2.1.** _Every_ \(m\times n\) _binary matrix with strictly more than_ \(c_\pi\cdot\mathrm{max}(m,n)\) _1-entries contains_ \(\pi\).

The _Stanley-Wilf conjecture_ states that the number of \(\pi\)-avoiding permutations of length _n_ grows at most single-exponentially in _n_ . Let \(\mathrm{Av}_n(\pi)\) be the set of all \(\pi\)-avoiding permutations of length _n_. The _Stanley-Wilf limit_ \(s_\pi\) of \(\pi\) is defined as \(s_\pi=\mathrm{lim}_{n\rightarrow\infty}\sqrt{|\mathrm{Av}_n(\pi)|}\).

Klazar \[Kla00\] showed that the Stanley-Wilf conjecture is implied by the Füredi-Hajnal conjecture. Importantly, Cibulka \[Cib09\] proved that \(s_\pi\) and \(c_\pi\) are polynomially related, in particular \(c_\pi\in O(s_\pi^{4.5})\) and \(s_\pi\in O(c_\pi^2)\). This is important for our purposes, since we can use \(\mathrm{log}c_\pi\) and \(\mathrm{log}s_\pi\) interchangeably within asymptotic notation. In particular, from now on we use mostly only the Füredi-Hajnal limit \(c_\pi\).

By applying the information-theoretic lower bound together with the relationship between \(s_\pi\) and \(c_\pi\), we obtain the following observation showing that the dependence on \(\pi\) in Theorem 1.1 is asymptotically optimal.

**Observation 2.2.** _Any comparison-based sorting algorithm must make at least_ \(\Omega((\mathrm{log}c_\pi+1)\cdot n)\) _comparisons in the worst case on_ \(\pi\)_-avoiding sequences._

## 3 Efficient multi-way merge

In this section, we show how we can leverage the Marcus-Tardos theorem \[MT04\] to implement an efficient multi-way merging procedure that can handle up to \(\frac{n}{\mathrm{log}n}\) many pattern-avoiding sequences in linear time.

**Theorem 3.1.** _There is an algorithm that receives on input a_ \(\pi\)_-avoiding sequence S of length n partitioned into m presorted sequences S_<sub>1</sub>_,...,S<sub>m</sub> with_ \(m\le\frac{n}{\mathrm{log}n}\)_, and outputs S sorted in_ \(O((\mathrm{log}c_\pi+1)\cdot n)\) _time even if_ \(\pi\) _is a priori unknown._

Note that Theorem 3.1 immediately implies a divide-and-conquer algorithm for sorting \(\pi\)-avoiding sequences in \(O_\pi(n\mathrm{log}^\star n)\) time. However, that is still very far from beating the fastest previous algorithm that sorts \(\pi\)-avoiding permutations in \(n\cdot 2^{O(|\pi|^2)+(1+o(1))\alpha(n)}\) time \[CPY24\].

