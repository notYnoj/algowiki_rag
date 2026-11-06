## B.4 Interpretation of the bounded-support correction

The expression in eq. 80 can be written schematically as

\(k_{[a,b]}(x,y)=k_\mathrm{rel}(x-y)k_\mathrm{sup}\left(\frac{x+y}{2}\right),\) (81)

where

\(k_\mathrm{rel}(x-y)=\mathrm{exp}\left(-\frac{(x-y)^2}{4\sigma^2}\right)\) (82)

depends only on the point separation, while

\(k_\mathrm{sup}(m)=\frac{\sqrt{\pi}\sigma}{2(b-a)}\left[\mathrm{erf}\left(\frac{b-m}{\sigma}\right)-\mathrm{erf}\left(\frac{a-m}{\sigma}\right)\right]\) (83)

depends on the midpoint _m_=(_x+y)/_2.

This decomposition shows explicitly why the bounded-center kernel is generally nonstationary. If the center support is finite, two pairs of points with the same separation _x-y_ can have different covariance if their midpoints lie at different distances from the center-support boundaries.

Away from the edges _a_ and _b_, and provided the support is wide relative to \(\sigma\), the two error functions approach +1 and -1, respectively, so that the support correction becomes approximately constant. Near the edges, however, the finite-support correction modifies the kernel.

## B.5 Full-line limit

The relationship with the standard Gaussian or squared-exponential kernel is obtained by taking

\(a\rightarrow-\infty,b\rightarrow+\infty.\) (84)

Since

\(\mathrm{lim}_{z\rightarrow+\infty}\mathrm{erf}(z)=1,\mathrm{lim}_{z\rightarrow-\infty}\mathrm{erf}(z)=-1,\) (85)

the bracketed factor in eq. 80 tends to 2.

If one considers the unnormalized center measure

\(d\mu(c)=dc,\) (86)

rather than the uniform probability density 1/(_b-a_), the corresponding full-line feature integral is

\(\widetilde{k}_\mathbb{R}(x,y)=\int_{-\infty}^\infty\phi_c(x)\phi_c(y)dc\)<br>
\(=\sqrt{\pi}\sigma\mathrm{exp}\left(-\frac{(x-y)^2}{4\sigma^2}\right).\) (87)

After normalization of the amplitude, this is a squared-exponential kernel with effective length scale

\(\ell=\sqrt{2}\sigma,\) (88)

under the conventional form

\(k_\mathrm{SE}(x,y)=\mathrm{exp}\left(-\frac{(x-y)^2}{2\ell^2}\right).\) (89)

Thus, the usual stationary Gaussian kernel is recovered as the infinite-support limit of the Gaussian center-feature construction, while the bounded-center model retains additional support information.

