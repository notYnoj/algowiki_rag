For symmetric envelopes centered around _k<sub>c</sub>_ we can further simplify using the shift theorem

\(\tilde{\mathcal{A}}(r)=\sum_{l=-\infty}^\infty\sqrt{2\pi}\mathcal{F}\{\tilde{f}\}\left(r-l\frac{2\pi}{\Delta k}\right)cos\left(k_c\left(r-l\frac{2\pi}{\Delta k}\right)+2\pi l\frac{k_s}{\Delta k}\right),\) (51)

where \(\tilde{f}(k)=f(k+k_c)\) is the shifted envelope centered around _k_=0, whose Fourier transform is real.

Let us apply this to our example described in Section 3.2 and find out why the interaction has the desired property given in equation Eq. (24). There we had uniform _f<sub>m</sub>_=1_/M_ and wave numbers

\(k_m^0=k_\mathrm{L}\left(1+\frac{2m+1}{2M}\right)\) (52)

with _m_=0_,...,M_-1. These have a mode spacing of \(\Delta k=k_\mathrm{L}/M\) and are centered around _k<sub>c</sub>_=3_k_<sub>L</sub>/2. One can see that only the odd modes of the cavity (wave numbers \(k_n=n\Delta k_\mathrm{FSR}\) with _n_ odd and free spectral range \(\Delta k_\mathrm{FSR}\)) are used. Therefore, \(\Delta k=2\Delta k_\mathrm{FSR}\) and \(k_s=\Delta k/2\), because the comb has to be shifted to fit the odd modes. Due to the uniform _f<sub>m</sub>_ the envelope is a rectangular function with width _k_<sub>L</sub> and height 1_/M_ centered at _k<sub>c</sub>_

\(f(k)=\mathrm{rect}((k-k_c)/k_\mathrm{L})/M=\left\{\begin{array}{ c c } 1/M & \text{for}k\in[k_c-k_\mathrm{L}/2,k_c+k_\mathrm{L}/2] \\ 0 & \text{otherwise.} \end{array}\right.\) (53)

The Fourier transform of a rectangular function centered around zero with unit width and height is a sinc function sinc(_x_)=sin(_x)/x_. Using the addition theorem for the cosine and noting that \(cos(\pi l)=(-1)^l\) and \(sin(\pi l)=0\) we obtain an analytical expression for the interaction

\(\tilde{\mathcal{A}}(r)=\sum_{l=-\infty}^\infty(-1)^l\mathrm{sinc}\left(\frac{k_\mathrm{L}}{2}\left(r-l\frac{2\pi}{\Delta k}\right)\right)cos\left(k_c\left(r-l\frac{2\pi}{\Delta k}\right)\right).\) (54)

For _l_=0 and at lattice site spacings \(r_j=j\pi/k_\mathrm{L}\) it takes the values

\(\mathrm{sinc}(\pi j/2)cos(3\pi j/2)=\left\{\begin{array}{ c c } 1 & \text{for}j=0 \\ 0 & \text{otherwise,} \end{array}\right.\) (55)

as desired. This comes from well known properties of sinc and cosine

\(\mathrm{sinc}(\pi j/2)=\left\{\begin{array}{ c c } 1 & \text{for}j=0 \\ 0 & \text{for}j\text{even} \\ (-1)^\frac{j-1}{2}\frac{2}{\pi j} & \text{for}j\text{odd} \\ cos(3\pi j/2)=\left\{\begin{array}{ c c } (-1)^\frac{j}{2} & \text{for}j\text{even} \\ 0 & \text{for}j\text{odd.} \end{array}\right.\)

The other summands have the same form, but are shifted by \(R=2\pi/\Delta k=2\pi M/k_\mathrm{L}=r_{2M}\) (2_M_ lattice sites) and have alternating signs. Since _R_ is an integer multiple of the lattice spacing this adds up to the desired interaction given in Eq. (24) in the main text.

Thus for rectangle envelopes the bandwidth \(\Delta k_\mathrm{BW}\) determines the zeros of the interaction. Taking \(\Delta k_\mathrm{BW}=2k_\mathrm{L}\) would lead to zeros at all lattice sites. For the smaller bandwidth \(\Delta k_\mathrm{BW}=k_\mathrm{L}\) used here, only even sites become zero. This can be compensated by choosing a central wave number _k<sub>c</sub>=nk_<sub>L</sub>/2 with _n_ odd, which is responsible for the zeros at odd sites. The mode spacing \(\Delta k\) determines the peak distance. Finally, using odd cavity modes (specifying _k<sub>s</sub>_) leads to alternating peaks, which does not have an effect in our implementation, since -2_M\<j\<_2_M_.

