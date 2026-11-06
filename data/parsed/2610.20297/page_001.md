Simple, Faster (min,+) Matrix Multiplication and APSP

**Abstract**

In this note, we provide a deterministic algorithm that computes the (min,+)-Matrix Product _C=A∗B_ of two \(N\times N\) matrices _A_ and _B_ with polynomially bounded integer entries in \(\tilde{O}(N^{2.9964})\) time, improving upon the exponent of _O(N_<sup>2.9995</sup>) time obtained in the recent breakthrough by Anthropic (Alman and Vassilevska Williams, 2026). Our algorithm uses a phased approach first proposed by Bringmann, Grandoni, Saha, and Vassilevska Williams in 2016. The phased approach produces an approximation \(\tilde{C}\) of _C_ in truly subcubic time such that the number of remaining triples (_i,k,j_):_A<sub>i,k</sub>+B<sub>k,j</sub>\<C_(_i,j_) is truly subcubic. This provided strong evidence that a truly subcubic (min,+)-Matrix Product and therefore, a truly subcubic algorithm for All Pairs Shortest Paths (APSP) may exist. However, to find the remaining triples in subcubic time, a sparse certificate is needed whose construction was not known. We use the thin matrix product theorem of the recent breakthrough to provide such a certificate. This gives a simple modular subcubic algorithm for APSP.

<sup>∗</sup>Supported by NSF HDR TRIPODS Phase II grant 2217058 (EnCORE Institute).

Barna Saha<sup>∗</sup><br> University of California San Diego<br> `bsaha@ucsd.edu`

Christopher Ye<sup>∗</sup><br> University of California San Diego<br> `czye@ucsd.edu`

October 15, 2026

