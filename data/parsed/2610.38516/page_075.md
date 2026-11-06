<tbc>(gcc 13) gives masks identical to the wrapper’s on the three 512<sup>2</sup> cases it was run on (`proba.pgm` differs by \(\pm 1\) byte on a few hundred pixels, single-precision rounding across compilers). The float potentials come from a six-line dump patch at the end of `PowerWatershed\_q2`. Both codes get the identical graph (the reference’s own edge order), the identical integer weights (our costs are 255-w = |I\_u-I\_v|, read back from the reference’s dump; the squared cost of the rest of the report is a monotone transform with the same ties, hence the same limit, and the 2<sup>-20</sup> quantisation of `pw\_limit\_numpy` plays no role with 8-bit costs) and the identical seeds. Cases: 80 random \(24\times 24\) images with four grey levels (plateaus everywhere; 40 two-label with three seed pixels per label, 40 with 3-5 labels), the 512<sup>2</sup> cases of section 1 (synthetic \(\sigma=0.05\) / 0.1 with seeds eroded by 5 and 30 px and scribbles, camera and astronaut eroded by 5 and 30 px), and three multi-label 512<sup>2</sup> cases (the synthetic shapes as four labels, camera and astronaut in three intensity classes, all eroded by 5 px).

**Result: the two codes agree.** Released mode against ours on the raw weights:

- The potentials agree to single precision everywhere (the reference’s `float`), on the plateau pixels included (6 % to 36 % of the pixels are solved on a plateau in the natural-image cases).<tbc>

- The only label differences are tie-breaks. With our strict rule (x \> 0.5 \(\rightarrow\) foreground) the pixels at exactly 0.5 go to the background, with the reference’s to the foreground: 85 / 627 / 559 pixels on the noisy synthetic cases, 77 / 122 on camera, 761 / 817 on astronaut (0.03-0.3 % of the pixels, none on the clean synthetic image); both codes have exactly the same set of 0.5 pixels. In the multi-label cases the 11 differing pixels have two labels at the same probability to 1e-15 and the reference’s single-precision sum picks the other one.<tbc>

- Our K-vector multi-label solve equals K one-hot runs of the scalar code to 1e-15, and the two-label case of the multi-label code equals the scalar code, on every case.<tbc>

- The reference run with `-g 1` is also reproduced by our code on the reconstructed weights (no label difference, 6e-8 on the potentials).<tbc>

- Fed the raw weights for both arguments (not reachable from the program), the reference disagrees with ours on 0-91 347 pixels per 512<sup>2</sup> case and with itself across `rand()` seeds (9 387 label changes over 40 random cases, none in the released mode): the no-reconstruction variant is not the limit. Its bucket-sort option (`quicksort = true`, hard-wired off in the program) returns positions instead of edge indices inside a plateau and yields potentials outside \[0, 1\]; irrelevant to the released program.<tbc>

**-** Timings (Mac, Apple M-series, 512<sup>2</sup>, 262 144 pixels, 523 264 edges): the reference’s `PowerWatershed\_q2` call takes 0.04-0.07 s, 0.11-0.17 s with its weights and reconstruction (0.17-0.22 s for the whole released executable on<tbc>

\begin{tabular}{ccccccccc}
cases & pixels & potentials, max abs. & difference & labels (reference rule, \(\ge 0.5\rightarrow\) label 1) & & pixels exactly at 0.5 & / tied & \\
80 random 24<sup>2</sup>, 2-5 labels & 46 080 & 6.1e-8 & & 0 differ & & 3 at 0.5, 25 tied (same in both) & & \\
10 two-label 512<sup>2</sup> & 2.6 M & 6.0e-8 & & 0 differ & & 0 (clean synthetic), 77-817 per noisy & / natural case & \\
3 multi-label 512<sup>2</sup> (K = 3, 4) & 0.8 M & 4.6e-8 & & 11 differ, all on tied top-two probabilities (gap \< 1e-15) & & 0 / 765 / 680 tied & & \\
\end{tabular}

