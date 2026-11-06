# Improved Quantum Algorithms for Subset Sum and _k_-SUM

Nikolai Chukhin <sup>∗</sup> Alexander S. Kulikov <sup>†</sup> Maksim Levitskii <sup>‡</sup> Ivan Mihajlin \(^\mathsection\)

**Abstract**

The Subset Sum problem asks whether, given _n_ integers and a target, some subset of the integers sums to the target. Its best known worst-case running time is _O_<sup>∗</sup>(2<sup>_n/_2</sup>) (Horowitz and Sahni, 1974), whereas the best quantum upper bound is _O_<sup>∗</sup>(2<sup>_n/_3</sup>) (Bernstein, Jeffery, Lange, and Meurer, 2013). The _k_-SUM problem is a parameterized version of Subset Sum asking whether there are _k_ integers that sum to the target. The best classical upper bound for it is \(\widetilde{O}(n^{\lceil k/2\rceil})\), whereas the best quantum running time is \(\widetilde{O}(n^{k/3})\) (Tani, 2009). For random instances, a quantum algorithm with running time \(\widetilde{O}(n^{\Phi_k})\) is known, where

\(\Phi_k=\frac{2k-\lfloor k/7\rfloor-\lfloor(k+3)/7\rfloor}{6}\)

(Schrottenloher, 2021).

We present a new quantum algorithm solving worst-case _k_-SUM in time \(\widetilde{O}(n^{\Psi_k})\), where

\(\Psi_k=\Phi_k-\frac{[k\equiv 3mod7]}{9}-\frac{[k\equiv 6mod7]}{18}.\)

The algorithm is not only faster for all _k_ congruent to 3 or 6 modulo 7, but also gives a worst-case guarantee rather than a guarantee restricted to single-solution random instances. Combining our algorithm for 7-SUM with the standard block reduction technique yields an _O_<sup>∗</sup>(2<sup>_n/_7</sup>) quantum algorithm for Subset Sum, improving the previously known _O_<sup>∗</sup>(2<sup>_n/_3</sup>) algorithm.

<sup>∗</sup>JetBrains Research. Email: `buyolitsez1951@gmail.com` <sup>†</sup>JetBrains Research. Email: `alexander.s.kulikov@gmail.com` <sup>‡</sup>Neapolis University Pafos and JetBrains Research. Email: `max.levitsky.5@gmail.com` \(^\mathsection\)JetBrains Research. Email: `ivmihajlin@gmail.com`

