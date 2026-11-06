For every fixed \(\lambda\neq 0\), the displayed expression is a sum of _n_<sup>3</sup>+6_n_<sup>2</sup> products of three linear forms. To verify the limit, classify a monomial by the three superscripts selected from {0,1,2}. If the three superscripts are distinct, each of the three \(\lambda^{-1}\) sums contains at least two factors multiplied by \(\lambda\), and the monomial survives with coefficient one. If exactly two superscripts agree, the sum corresponding to the repeated superscript contains exactly one factor multiplied by \(\lambda\) and cancels the monomial from the first line; the other two sums vanish in the limit. If all three superscripts equal _s_, the first line contributes _n_ times the diagonal product of the _s_-block, the corresponding \(\lambda^{-1}\) sum contributes \(-\lambda^{-1}\) times that product, and the last line contributes \(-(n-\lambda^{-1})\) times it. These contributions sum to zero. Hence precisely the six monomials with distinct superscripts remain, which are the balanced restriction of \(\phi_\mathrm{CW}^{\otimes 3}\). Thus

\(\underline{R}(\psi_\mathrm{CW})\le n^3+6n^2.\) (180)

The third tensor power of the decomposition of \(\phi_\mathrm{CW}\), or the trilinear aggregation with centering, padding, and weighting, instead gives (_n_+2)<sup>3</sup>=_n_<sup>3</sup>+6_n_<sup>2</sup>+12_n_+8.

## D Unequal-shape complete-tripartition constructions

The correction counts determine each budget by (101). In particular, for the 22-product family every product has volume _n_<sup>6</sup>, so

\(22n^{2\omega}\le\rho_{22}(n)=(n+1)^6+6(n+1)^5+12(n+1)^4.\) (181)

The minimizing integer _n_=11 yields \(\omega\le 2.560147\dots\); its limiting retained fraction is at least 1/212.

The full tripartition lists and exponents are in the auxiliary directory `anc/constructions/`, in the files `general10.txt`, `general13.txt`, and `general22.txt`, respectively.

## E Incomplete tripartitions of the big CW tensor

### E.1 Constructions and multiplication counts

For the incomplete families in  7, _m<sub>g</sub>_ counts products of volume _n<sup>g</sup>_, and the exponent bound is determined by

\(\sum_gm_gn^{\omega g/3}\le(n+2)^d.\) (182)

\begin{tabular}{ccccccc}
products & shape counts & \(h\le\) & \(\theta\ge\) & correction counts & optimizing _n_ & \(\omega_\mathrm{eff}\) \\
10 & 6(2,2,2)+4(1,2,3) & 1 & 1/2 & (6,3) & 17 & 2.706 \\
13 & 3(2,2,2)+10(1,2,3) & 2 & 1/3 & (6,6) & 14 & 2.660 \\
22 & 8(2,2,2)+10(1,2,3)+4(1,1,4) & 211 & 1/212 & (6,12) & 11 & 2.560 \\
\end{tabular}

\begin{tabular}{ccccccc}
_d_ & products & counts by covered size & & optimizing _n_ & \(\omega_\mathrm{eff}\) \\
6 & 51 & _m_<sub>6</sub>=15, _m_<sub>5</sub>=2, _m_<sub>4</sub>=4, _m_<sub>3</sub>=18, _m_<sub>2</sub>=8, _m_<sub>1</sub>=1, _m_<sub>0</sub>=3 & & 14 & 2.636 \\
9 & 68 & _m_<sub>9</sub>=57, _m_<sub>8</sub>=11 & & 14 & 2.639 \\
\end{tabular}

6: Complete-tripartition families of equal volume and unequal shapes. A shape (_r,s,t_) abbreviates all products whose ordered exponent triple is a permutation of that triple. The height column gives an upper bound, and the accuracy column its corresponding lower bound. The final column gives the asymptotic-sum bound on \(\omega\), rounded to three decimal places.

7: Conflict-free families of incomplete tripartitions. Products have unequal volumes and often unequal shapes; _m<sub>s</sub>_ counts products with _s_ covered coordinates. The exponent follows from (182) and is rounded to three decimal places.

