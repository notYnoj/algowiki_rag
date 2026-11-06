# Computing faster with a full memory:Catalytic algorithms break time-space lower bounds

**Abstract**

We show that adding "catalytic space" (which starts full and must have its original contents restored at the end of computation) provably speeds up time-and-space-bounded computation. In a natural output model, with _O_(log(_n_)) free space and poly(_n_) catalytic space, we give algorithms for sorting and the discrete Fourier transform running in time _n_<sup>1+_o_(1)</sup>, and an algorithm for matrix multiplication running in time \(n^{\omega+o(1)}\). In the same output model, without additional catalytic space, sorting and DFT are known to require time-space product \(\Omega(n^2)\), and matrix multiplication is known to require time-space product \(\Omega(n^3)\) [BC80; Bea91; Yes84; Abr91]. This is the first unconditional demonstration that (uniform, non-relativized) catalytic logspace algorithms can outperform their (non-catalytic) counterparts.

We give several further results relevant to fast catalytic algorithm design. We observe that many applications of sorting, FFT, and fast matrix multiplication (e.g., \(\kappa\)SUM, integer multiplication, and clique counting) can be performed catalytically, giving catalytic logspace algorithms matching (up to subpolynomial factors) the best known unbounded-space runtimes. Furthermore, we give a fast and simple catalytic algorithm for evaluating low-depth threshold circuits, improving the previously known runtime bound from \(\widetilde{O}\left(|C|4^df\right)\) to \(\widetilde{O}\left(|C|2^d\right)\), where |_C_| is the total size (i.e. number of wires) of the circuit, _d_ is the depth, and _f_ is the maximum fan-in.

<sup>∗</sup>Work supported in part by an NSF GRFP fellowship. <sup>†</sup>Work supported in part by NSF CCF-2127597 and NSF CCF-2420092. **AI disclosure:** We used several models to search for references, and to proofread the paper.

Adelmo Morrison Orozco<br>
MIT<br>
adelmo@mit.edu

Nathan Sheffield<sup>∗</sup><br>
MIT<br>
shefna@mit.edu

Ryan Williams<sup>†</sup><br>
MIT<br>
rrw@mit.edu

