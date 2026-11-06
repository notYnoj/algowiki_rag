The overlap consists of three terms: First, it is the mode function evaluated in between the lattice sites. Second, there is again the Gaussian smoothing term as for the on-site overlap. Lastly, there is an exponential independent of the modes, which comes from the overlap of the two Gaussians. It goes to zero for \(V_\mathrm{L}/E_\mathrm{R}\gg 1\), leading to \(u_m^{ij}=0\).

The order operator is then<tbc>

\(\hat{\Theta}_m^\mathrm{har}=\frac{1}{N}e^{-\left(\frac{k_m^x}{2k_\mathrm{L}}\right)^2}\sqrt{\frac{E_\mathrm{R}}{V_\mathrm{L}}}\sum_{i,j=1}^N\left(h_m(x_i,y_j)\hat{n}_{ij}+h_m((x_i+x_{i+1})/2,y_j)\hat{B}_{ij}e^{-\frac{\pi^2}{4}}\sqrt{\frac{V_\mathrm{L}}{E_\mathrm{R}}}\right)\) (47)

<tbc>leading to an interaction Hamiltonian \[Eq. (16)\] given by

\(H_\mathrm{cav}^\mathrm{har}=U_Q\sum_mf_me^{-2\left(\frac{k_m^x}{2k_\mathrm{L}}\right)^2}\sqrt{\frac{E_\mathrm{R}}{V_\mathrm{L}}}\sum_{ijkl}\left(h_m^*(x_i,y_j)\hat{n}_{ij}+h_m^*((x_i+x_{i+1})/2,y_j)\hat{B}_{ij}e^{-\frac{\pi^2}{4}}\sqrt{\frac{V_\mathrm{L}}{E_\mathrm{R}}}\right)\times\left(h_m(x_k,y_l)\hat{n}_{kl}+h_m((x_k+x_{k+1})/2,y_l)\hat{B}_{kl}e^{-\frac{\pi^2}{4}}\sqrt{\frac{V_\mathrm{L}}{E_\mathrm{R}}}\right),\) (48)

which in the "infinitely" deep lattice limit simplifies to Eq. (17). All cavity-induced tunneling terms are suppressed by the exponential and tend to be smaller than density-density terms. Also, since _U_<sub>Q</sub> is maximally on the order of _J_ (at the end of the sweep), cavity-induced tunneling terms are smaller than _H_<sub>kin</sub>. However, also the density-density terms can be small for example when _h<sub>m</sub>(x<sub>i</sub>,y<sub>j</sub>_)=0, which is why we still include cavity-induced tunneling in the simulations.

In the main text we chose uniform _f<sub>m</sub>_=1_/M_. To compensate for Gaussian smoothing one might want to include the exponential as correction

\(\tilde{f}_m=f_me^{2\left(\frac{k_m^x}{2k_\mathrm{L}}\right)^2}\sqrt{\frac{E_\mathrm{R}}{V_\mathrm{L}}},\) (49)

which leads to even better results (\(\tilde{A}\) is closer to _A_ for finite lattice depths). Note that this correction does only depend on _V_<sub>L</sub> and not on the problem size or number of modes in our implementation, since the range of \(k_m^x\) is fixed.

## D Shape of the interaction

Here we reformulate the interaction in the infinitely deep lattice limit from Eq. 22 with Fourier transforms by defining a real envelope function _f(k_) such that _f(k<sub>m</sub>_)=_f<sub>m</sub>_. To get back the discrete wave numbers, this function is sampled with a Dirac comb at the lines \(m\Delta k+k_s\) with \(m\in\mathbb{Z}\), where _k<sub>s</sub>_ is a constant shift and \(\Delta k\) is the spacing between the pumped modes. In the main text we only consider the case _k<sub>s</sub>_=0 for simplicity. We define the Fourier transform as \(\mathcal{F}\{f\}(r)=\int_{-\infty}^\infty\mathrm{d}kf(k)e^{ikr}/\sqrt{2\pi}\) and denote the convolution as \((f*g)(t)=\int_{-\infty}^\infty f(\tau)g(t-\tau)\mathrm{d}\tau\).

For simplicity, we take parallel wave vectors **_k_**_<sub>m</sub>_. Along this direction \(\mathbf{r}\|\mathbf{k}_m\) we write

\(\tilde{\mathcal{A}}(r)=\sum_mf_m\mathrm{cos}(k_mr)=\int_{-\infty}^\infty\mathrm{d}kf(k)\sum_{m=-\infty}^\infty\delta(k-m\Delta k-k_s)\mathrm{cos}(kr)\)<br>
\(=\mathrm{Re}\left[\sqrt{2\pi}\mathcal{F}\left\{f(k)\sum_{m=-\infty}^\infty\delta(k-m\Delta k-k_s)\right\}(r)\right]=\mathrm{Re}\left[\sqrt{2\pi}\mathcal{F}\{f\}(r)*\sum_{l=-\infty}^\infty\delta\left(r-l\frac{2\pi}{\Delta k}\right)e^{ik_sr}\right]\)<br>
\(=\sum_{l=-\infty}^\infty\mathrm{Re}\left[\sqrt{2\pi}\mathcal{F}\{f\}\left(r-l\frac{2\pi}{\Delta k}\right)e^{i2\pi l\frac{k_s}{\Delta k}}\right],\) (50)

where _r_=|**_r_**|. We used the convolution and shift theorem from Fourier analysis in the second to last line and evaluated the convolution integrals by pulling out the sum in the last line.

