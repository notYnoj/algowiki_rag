## C.3 Comparisons at integer dimensions

The following comparisons use the same dimensions and number of independent products, at dimensions where the comparison bases apply recursively without padding. For _n_=12, the nine-product construction `br9` has budget 7,054,567, compared with 9,000,000 from two tensor levels of the Bini square base for each product. The fourteen-product construction `ex14` has budget 13<sup>9</sup>=10,604,499,373, compared with 15,748,096,000 from three tensor levels of the exact size-12 base for each product.

For a balanced family with _q=n<sup>N</sup>_, the asymptotic-sum inequality is

\(pn^{N\omega}\le r(n),\omega\le\omega_\mathrm{eff}(p,q,r(n)).\) (174)

Appendix A gives a recursive argument for the exact case.

## C.4 A border-rank decomposition of the balanced little-CW cube

The balanced restriction of \(\phi_\mathrm{CW}^{\otimes 3}\) consists of six matrix-multiplication forms sharing variable blocks; it is not a direct sum of six independent products. The following decomposition reduces the border-rank bound for this shared-variable tensor. In a one-subscript entry of _X_, _Y_ , or _Z_, the omitted subscript is summed over. The restriction of the third tensor power of the little CW tensor to balanced tripartitions admits the following border-rank decomposition,

\(\psi_\mathrm{CW}(X,Y,Z)=\mathrm{lim}_{\lambda\rightarrow 0}\sum_{i,j,k}(X_{jk}^{(\{0\})}+X_{ik}^{(\{1\})}+X_{ij}^{(\{2\})})(Y_{jk}^{(\{0\})}+Y_{ik}^{(\{1\})}+Y_{ij}^{(\{2\})})(Z_{jk}^{(\{0\})}+Z_{ik}^{(\{1\})}+Z_{ij}^{(\{2\})})\) (175)

\(-\lambda^{-1}\sum_{j,k}(X_{jk}^{(\{0\})}+\lambda X_k^{(\{1\})}+\lambda X_j^{(\{2\})})(Y_{jk}^{(\{0\})}+\lambda Y_k^{(\{1\})}+\lambda Y_j^{(\{2\})})(Z_{jk}^{(\{0\})}+\lambda Z_k^{(\{1\})}+\lambda Z_j^{(\{2\})})\) (176)

\(-\lambda^{-1}\sum_{i,k}(\lambda X_k^{(\{0\})}+X_{ik}^{(\{1\})}+\lambda X_i^{(\{2\})})(\lambda Y_k^{(\{0\})}+Y_{ik}^{(\{1\})}+\lambda Y_i^{(\{2\})})(\lambda Z_k^{(\{0\})}+Z_{ik}^{(\{1\})}+\lambda Z_i^{(\{2\})})\) (177)

\(-\lambda^{-1}\sum_{i,j}(\lambda X_j^{(\{0\})}+\lambda X_i^{(\{1\})}+X_{ij}^{(\{2\})})(\lambda Y_j^{(\{0\})}+\lambda Y_i^{(\{1\})}+Y_{ij}^{(\{2\})})(\lambda Z_j^{(\{0\})}+\lambda Z_i^{(\{1\})}+Z_{ij}^{(\{2\})})\) (178)

\(-(n-\lambda^{-1})\big[\sum_{j,k}X_{jk}^{(\{0\})}Y_{jk}^{(\{0\})}Z_{jk}^{(\{0\})}+\sum_{i,k}X_{ik}^{(\{1\})}Y_{ik}^{(\{1\})}Z_{ik}^{(\{1\})}+\sum_{i,j}X_{ij}^{(\{2\})}Y_{ij}^{(\{2\})}Z_{ij}^{(\{2\})}\big].\) (179)

\begin{tabular}{cccccc}
_N_ & _p_ & Construction & _h_ & \(\beta'(0)\) & \(\sigma_0/\sigma_c\) \\
2 & 6 & `br6` & 3 & 6(_n_+1)+3 & 1.024 \\
2 & 7 & `br7` & 15 & 8(_n_+1)+5 & 1.024 \\
2 & 8 & `br8` & 1 & 10(_n_+1)+2 & 1.692 \\
2 & 9 & `br9` & 2 & 8 & 1.692 \\
2 & 9 & `br9q` & \(\frac{8}{3}\) & 3(_n_+1)+6 & 1.692 \\
2 & 10 & `br10` & 7 & 3(_n_+1)+16 & 1.692 \\
3 & 32 & `br32` & 1 & (_n_+1)<sup>3</sup>+(_n_+1)<sup>2</sup>+20 & 4.310 \\
3 & 35 & `br35full` & \(\frac{15}{8}\) & 32 & 4.310 \\
3 & 35 & `br35` & 2 & 15(_n_+1)<sup>2</sup>+35 & 4.310 \\
3 & 36 & `br36` & 3 & 22(_n_+1)<sup>2</sup>+40 & 4.310 \\
3 & 37 & `br37` & 3 & 15(_n_+1)<sup>2</sup>+50 & 4.310 \\
3 & 39 & `ub9` & 12 & (_n_+1)<sup>3</sup>+(_n_+1)<sup>2</sup>+4 & 4.310 \\
4 & 125 & `br125` & 1 & (_n_+1)<sup>4</sup>+21(_n_+1)<sup>3</sup>+161 & 14.828 \\
4 & 133 & `br133` & 2 & (_n_+1)<sup>4</sup>+70(_n_+1)<sup>3</sup>+163 & 14.828 \\
4 & 141 & `br141` & 3 & (_n_+1)<sup>4</sup>+36(_n_+1)<sup>3</sup>+245 & 14.828 \\
4 & 150 & `ub12` & 11 & 10(_n_+1)<sup>3</sup>+24 & 14.702 \\
\end{tabular}

5: Leading coefficients at _n_=126,25,11 for _N_=2,3,4, respectively. The ratios \(\sigma_0/\sigma_c\) are rounded to three decimal places. Construction identifiers refer to the data in Appendix F.

