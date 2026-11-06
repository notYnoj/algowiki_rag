## Comparison with entropic OT transfer.

The advantage of our method is that it is in _O(n_), where _n_ is the number of pixels, whereas Sinkhorn’s algorithm is in _O(n_<sup>2</sup>). We can use entropic OT for transferring the colours of small enough images, for instance using the barycentric transport map \(T(x_i)=\sum_jP_{ij}^\varepsilon y_j/\sum_jP_{ij}^\varepsilon\) (which can be evaluated lazily with POT’s GeomLoss backend and KeOps \[Cha+21\], removing the need to store the full transport matrix). Using every pixel with regularisation \(\varepsilon=0.01\) gives a convincing transfer in 24.5 seconds on one RTX A4000, compared with 55 seconds for MW<sub>2</sub> (see Fig. 26). However, for larger images, at about one million pixels, the times we measure on an H100 are 17.3 seconds for MW<sub>2</sub> and 98.7 seconds for entropic transfer. Entropic barycentric colour transfer with 4096 quantised colours was already studied in \[BSR18, Section 6.1\]. A related colour-transfer method using the gradient of the Sinkhorn divergence (which differs from projecting one transport plan) is illustrated in \[Fey20, Figure 3.33\].



















(a) Result with _K_=1

(b) Result with _K_=10

(c) Target

Figure 25: Colour transfer with (a) _K_=1 components and (b) _K_=10 components.

Source

MW<sub>2</sub>

Target

\(\varepsilon=1\)

\(\varepsilon=0.1\)

\(\varepsilon=0.01\)

Figure 26: Colour transfer: barycentric transfer with entropic OT, and our method.

