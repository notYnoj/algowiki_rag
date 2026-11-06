_Proof._ Set \(\lambda=(c\cdot\mathrm{log}n)^{-1}\) for sufficiently large constant _c_. Denote _G_<sub>0</sub> by _G_. For each _i_, let _G<sub>i</sub>_ denote an \(\varepsilon_i\)-spectral sparsifier of _G_<sub>_i_-1</sub> obtained from Lemma B.7 with respect to \(\lambda\). Let _m<sub>i</sub>_ denote the number of edges of _G<sub>i</sub>_. Via Lemma B.7, for each _i_, we have \(m\cdot\left(\frac{1}{2}-\lambda\right)^i\le m_i\le m\cdot\left(\frac{1}{2}+\lambda\right)^i\) and \(\varepsilon_i=\sqrt{\frac{Cn\mathrm{log}^2n}{m_i}}\) for some universal constant _C\>_0. Let \(\ell\) be the largest non-negative integer such that

\(\sqrt{\frac{n\mathrm{log}^2n}{m}}\cdot\left(\frac{1}{2}-\lambda\right)^{-\ell/2}\le\frac{\varepsilon}{40\sqrt{C}}.\)

We claim that \(G_\ell\) is the desired \(\varepsilon\)-spectral sparsifier of _G_. Note here that \(\ell=O(\mathrm{log}n)\).

## Maximum weight of \(G_\ell\).

Notice that maximum weight of \(G_\ell\) is \(2^\ell\), and we have<tbc>

\(2^\ell\le\left(\frac{1}{2}-\lambda\right)^{-\ell}\le O\left(\frac{\varepsilon^2m}{n\mathrm{log}^2n}\right)=O\left(\frac{\varepsilon^2d}{\mathrm{log}^2n}\right).\)

## Number of edges of \(G_\ell\).

<tbc>By definition of \(\ell\), we have \(\sqrt{\frac{n\mathrm{log}^2n}{m}}\cdot\left(\frac{1}{2}-\lambda\right)^{-(\ell+1)/2}>\frac{\varepsilon}{40\sqrt{C}}\). This further implies \(\left(\frac{1}{2}-\lambda\right)^\ell<400C\cdot\frac{n\mathrm{log}^2n}{\varepsilon^2m}\) . We then have:

\(m_\ell\le m\cdot\left(\frac{1}{2}+\lambda\right)^\ell=m\cdot\left(\frac{1}{2}-\lambda\right)^\ell\cdot\left(\frac{1+2\lambda}{1-2\lambda}\right)^\ell\)<br>
\(\le\frac{n\mathrm{log}^2n}{\varepsilon^2}\cdot\left(400C\cdot e^{6\lambda\ell}\right)(\frac{1+2\lambda}{1-2\lambda}\le 1+6\lambda\le e^{6\lambda})\)<br>
\(=O\left(\frac{n\mathrm{log}^2n}{\varepsilon^2}\right)(\lambda=O(\frac{1}{\mathrm{log}n})\text{and}\ell=O(\mathrm{log}n))\)

## Approximation factor.

Let us first bound \(\varepsilon_1+\dots+\varepsilon_\ell\). Consider the following derivation.

\(\sum_{i\in[\ell]}\varepsilon_i=\sum_{i\in[\ell]}\sqrt{\frac{Cn\mathrm{log}^2n}{m_i}}=\sqrt{\frac{Cn\mathrm{log}^2n}{m}}\cdot\sum_{i\in[\ell]}\left(\frac{1}{2}-\lambda\right)^{-i/2}\)<br>
\(=\sqrt{\frac{Cn\mathrm{log}^2n}{m}}\cdot 5\cdot\left(\frac{1}{2}-\lambda\right)^{-\ell/2}\text{(geometric sum)}\)<br>
\(\le\sqrt{\frac{Cn\mathrm{log}^2n}{m}}\cdot 5\cdot\left(\frac{\varepsilon}{40\sqrt{C}}\cdot\sqrt{\frac{n\mathrm{log}^2n}{m}}\right)\text{(definition of}\ell\text{)}\)<br>
\(\le\frac{\varepsilon}{8}.\)

Next, we compare \(v^\top L_{G_\ell} v\) and \(v^\top L_Gv\) for any vector \(v\in\mathbb{R}^n\). Again, we omit the corner case of \(v=\vec{1}\). Then, we have:

\(\frac{v^\top L_{G_\ell} v}{v^\top L_Gv}\le\prod_{i\in[\ell]}(1+\varepsilon_i)\le e^{\sum_{i\in[\ell]}\varepsilon_i}\le e^{\varepsilon/8}\le 1+\varepsilon.\)

