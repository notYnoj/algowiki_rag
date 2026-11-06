In the following we will use the example wave numbers

\(k_m^0=k_\mathrm{L}\left(1+\frac{2m+1}{2M}\right)\) (23)

with _m_=0_,...,M_-1 and uniform _f<sub>m</sub>_=1_/M_. Taking into account \(\mathbf{k}_m^x\) only, the interaction along the _x_-direction \(\mathbf{r}\|\mathbf{k}_m^x\) at lattice site distances \(r_j=j\pi/k_\mathrm{L}=ja\) has the values

\(\tilde{\mathcal{A}}(r_j)=\left\{\begin{array}{ c c }
(-1)^l & \text{for}j=2Ml,l\in\mathbb{Z} \\
0 & \text{otherwise},
\end{array}\right.\) (24)

as shown in Appendix D. If we guarantee that -2_M\<j\<_2_M_ this results in an interaction which is zero everywhere apart from _j_=0, i.e. at zero distance. So for repulsive interactions (_U_<sub>Q</sub>_\>_0 and thus \(\tilde{\Delta}_{c,m}>0\)), the wave vectors \(\mathbf{k}_m^x\) create the non-attacking interaction along the _y_-direction (\(\tilde{A}_{ijkl}=1\) if _i=k_ and 0 otherwise) as long as \(N\le 2M\). This is illustrated in Fig. 4(a) for _M=N_=5. Analogously, \(\mathbf{k}_m^\pm\) cause the non-attacking interactions along the diagonals. In a square lattice the diagonals have the distance \(r_j/\sqrt{2}\), which is compensated by \(k_m^\pm=|\mathbf{k}_m^\pm|=\sqrt{2}k_m^0\). Since there are 2_N_-1 diagonals, one has to make sure that \(2N-1\le 2M\). Upon combining all wave vectors from three directions we finally obtain the full queens interaction, as shown in Fig. 4(b), which is realized with _M_<sub>tot</sub>=3_M_=3_N_ frequencies in our example.

Note that there are several combinations of wave numbers and mode strengths which, at least approximately, create the desired line-shaped interactions perpendicular to the light propagation direction. For this it is insightful to reformulate the interaction as a Fourier transform. To deal with continuous functions, we define an envelope _f(k_) with _f(k<sub>m</sub>_)=_f<sub>m</sub>_, which is sampled at the wave numbers \(n\Delta k\) with \(n\in\mathbb{Z}\) containing all \(k_m^\mu\). Considering one illumination direction for simplicity, the interaction \[Eq. (22)\] along \(\mathbf{r}\|\mathbf{k}_m^\mu\) with _r_=|**_r_**| can be written as

\(\tilde{\mathcal{A}}(r)=\mathrm{Re}\left[\sqrt{2\pi}\mathcal{F}\left\{f(k)\sum_{n=-\infty}^\infty\delta(k-n\Delta k)\right\}(r)\right]\)<br>
\(=\sum_{l=-\infty}^\infty\mathrm{Re}\left[\sqrt{2\pi}\mathcal{F}\{f\}\left(r-l\frac{2\pi}{\Delta k}\right)\right],\) (25)

where \(\mathcal{F}\{f\}(r)=\int_{-\infty}^\infty\mathrm{d}kf(k)e^{ikr}/\sqrt{2\pi}\) is the Fourier transform of _f(k_) and \(\delta(x)\) is a Dirac

delta at _x_=0. See Appendix D for a detailed derivation.

The last line allows for a simple interpretation: The interaction consists of peaks repeating with a spatial period \(R=2\pi/\Delta k\). Each of these peaks has the shape of the real part of the Fourier transform of the envelope function _f(k_) with a width corresponding to the inverse of the mode bandwidth \(\sigma\sim 2\pi/\Delta k_\mathrm{BW}\).

For the (approximate) non-attacking condition (\(\tilde{\mathcal{A}}(ja)\approx 1\) for _j_=0 and \(|\tilde{\mathcal{A}}(ja)|\checkmark 1\) otherwise) there are two conditions. Firstly, at most one peak should be within the region of the atoms. Thus the period has to be larger than the (diagonal) size of the optical lattice \(R\ge Na\) (\(R\ge\sqrt{2}Na\)). Secondly, the width of one peak has to be smaller than the lattice spacing \(\sigma\lesssim a\). Combining these conditions to \(R\unknown N\sigma\), we see that the minimum number of modes per direction _M_ scales linearly with _N_

\(M\approx\Delta k_\mathrm{BW}/\Delta k\unknown N.\) (26)

Therefore, with only ∼_N_ modes this quite generically allows for creating an interaction along lines perpendicular to the light propagation. Note however, that the second condition also implies that the spatial frequency spread has to be at

(a) -0.5 0
0.5 1
(b) -2 -1 0
1 2
3 4
3 2
y/a 1
0 0
1 2
3 4
0 1
2 3
4 x/a x/a

Figure 4: _Energy penalty created by one atom._ - These density plots show the energy penalty \(\tilde{\mathcal{A}}(\mathbf{x}-\mathbf{x}_a)\) for an atom at position **_x_**=(_x,y)<sup>T</sup>_ created by an atom at position **_x_**_<sub>a</sub>_=(_a,a)<sup>T</sup>_ (red dot) for _N=M_=5 \[see Eq. (22)\]. The dots indicate lattice site positions and the solid (dashed) contour lines indicate where \(\tilde{\mathcal{A}}(\mathbf{x}-\mathbf{x}_a)=0\) (\(\tilde{\mathcal{A}}(\mathbf{x}-\mathbf{x}_a)=1\)) is fulfilled. (a) Pumping along the _x_-axis with the wave vectors \(\mathbf{k}_m^x=(k_m^0,0)^T\) with \(k_m^0/k_\mathrm{L}=1.1,1.3,1.5,1.7,1.9\) \[according to Eq. (23)\] creates interactions along _y_. (b) Additionally including diagonal pump lasers \(\mathbf{k}_m^+=(k_m^0,k_m^0)^T\) and \(\mathbf{k}_m^-=(k_m^0,-k_m^0)^T\) implements the full queens interaction along diagonals and vertical lines \[Eq. (3)\].

