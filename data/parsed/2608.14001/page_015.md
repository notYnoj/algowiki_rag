<tbc>of the system being studied and the choice of observation vector. Thus, just as increasing the number of lags used in a delay-coordinate map can mitigate the ill-conditioning of the embedding for a uniformly-sampled signal, so too in general does increasing the number of time lags in the non-uniform sampling setting improve the embedding quality.

However, the numerical simulations do suggest that standard, uniformly-spaced delay-coordinate maps tend to perform better than, and converge faster than, the non-uniform case. The theoretical results from Conjecture 1 detailing when a generalized Vandermonde matrix (14) has full column rank-at least with 1-3 distinct frequencies-agree with the numerical results: they show that more restrictive conditions are needed in addition to those for typical Fourier Vandermonde matrices (10). Thus, that generalized Vandermonde matrices must satisfy more conditions than typical Vandermonde matrices indicates that uniformly-spaced delay-coordinate maps ought to perform better than their non-uniformly-spaced counterparts. These insights lead to a number of further areas of investigation. Deriving estimates for the rate of convergence would be a helpful metric for comparing uniformly-sampled and non- uniformly-sampled maps. This also leads to an open question of whether uniform sampling is the guaranteed optimal sampling approach for linear systems that are not necessarily multi-scale. Some future directions will be to examine stable linear embeddings using non-uniform time sampling for linear systems exhibiting frequencies across multiple timescales, and for linear systems observed using multiple observation functions as a means to embed multivariate time series.

From the viewpoint of applications, sensing strategies and signal processing techniques continue to be critically important for state-estimation and control in almost every domain of science and engineering. Leveraging the time-history of limited point sensors for reconstruction of full state spaces is clearly an important paradigm for practical deployment. The non-uniform sampling of signals, especially in the context of emerging event-based sampling strategies, are also important for efficient data acquisition strategies. The current work aims to establish rigorous estimates and bounds on when non- uniform sampling can guarantee faithful state-space estimation, which can then be used for critical downstream tasks such as control.

## V. CODE AND DATA AVAILABILITY

The code used for the numerical experiments is available at: https://github.com/fisherng19/Stable-Linear-Takens- Embedding-Theorem-with-Unevenly-Spaced-Delays.it

## VI. ACKNOWLEDGMENT

We acknowledge support from the Air Force Office of Scientific Research (FA9550-24-1-0141).

## REFERENCES

[1] F. Takens, "Detecting strange attractors in turbulence," in _Dynamical Systems and Turbulence, Warwick 1980_, D. Rand and L.-S. Young, Eds. Berlin, Heidelberg: Springer Berlin Heidelberg, 1981, pp. 366-381.

[2] T. Sauer, J. A. Yorke, and M. Casdagli, "Embedology," _Journal of Statistical Physics_, vol. 65, no. 3/4, 1991.

[3] H. L. Yap, A. Eftekhari, M. B. Wakin, and C. J. Rozell, "A first analysis of the stability of takens’ embedding," 2014. [Online]. Available: https://arxiv.org/abs/1406.3831

[4] A. Eftekhari, H. L. Yap, M. B. Wakin, and C. J. Rozell, "Stabilizing embedding: Geometry-preserving delay-coordinate maps," _Physical Review E_, vol. 97, no. 2, Feb 2018. [Online]. Available: http://dx.doi.org/10.1103/PhysRevE.97.022222

[5] H. L. Yap and C. J. Rozell, "Stable takens’ embedding for linear dynamical systems," in _49th IEEE Conference on Decision and Control (CDC)_, 2010, pp. 2948-2953.

[6] ----, "Stable takens’ embeddings for linear dynamical systems," _CoRR_, vol. abs/1010.5938, 2011. [Online]. Available: http://arxiv.org/abs/1010. 5938

[7] P. Sommer and K. Janse, "On the relationship between uniform and recurrent nonuniform discrete-time sampling schemes," _IEEE Transactions on Signal Processing_, vol. 56, no. 10, pp. 5147-5156, 2008.

[8] I. Vlachos and D. Kugiumtzis, "Nonuniform state-space reconstruction and coupling detection," _Physical Review E--Statistical, Nonlinear, and Soft Matter Physics_, vol. 82, no. 1, p. 016207, 2010.

[9] L. Faes, G. Nollo, and A. Porta, "Information-based detection of nonlinear granger causality in multivariate processes via a nonuniform embedding technique," _Physical Review E--Statistical, Nonlinear, and Soft Matter Physics_, vol. 83, no. 5, p. 051112, 2011.

[10] M. Han, W. Ren, M. Xu, and T. Qiu, "Nonuniform state space reconstruction for multivariate chaotic time series," _IEEE transactions on cybernetics_, vol. 49, no. 5, pp. 1885-1895, 2018.

[11] M. Tao, K. Poskuviene, N. F. Altayem, M. Cao, and M. Ragulskis, "Permutation entropy based on non-uniform embedding," _Entropy_, vol. 20, no. 8, 2018. [Online]. Available: https://www.mdpi.com/ 1099-4300/20/8/612

[12] K. Judd and A. Mees, "Embedding as a modeling problem," _Physica D: Nonlinear Phenomena_, vol. 120, no. 3, pp. 273-286, 1998. [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S016727899800089X

[13] Y. Hirata, H. Suzuki, and K. Aihara, "Reconstructing state spaces from multivariate data using variable delays," _Phys. Rev. E_, vol. 74, p. 026202, Aug 2006. [Online]. Available: https://link.aps.org/doi/10. 1103/PhysRevE.74.026202

[14] C. Gao, Q. Lin, J. Ni, W. Guo, and Q. Li, "A nonuniform delay- coordinate embedding-based multiscale predictor for blast furnace systems," _IEEE Transactions on Control Systems Technology_, vol. 29, no. 5, pp. 2223-2230, 2021.

[15] E. Tan, S. Algar, D. Corrêa, M. Small, T. Stemler, and D. Walker, "Selecting embedding delays: An overview of embedding techniques and a new method using persistent homology," _Chaos: An Interdisciplinary Journal of Nonlinear Science_, vol. 33, no. 3, Mar 2023. [Online]. Available: http://dx.doi.org/10.1063/5.0137223

[16] T. Sauer, "Reconstruction of dynamical systems from interspike intervals," _Phys. Rev. Lett._, vol. 72, pp. 3811-3814, Jun 1994. [Online]. Available: https://link.aps.org/doi/10.1103/PhysRevLett.72.3811

[17] J. P. Huke and D. S. Broomhead, "Embedding theorems for non- uniformly sampled dynamical systems," _Nonlinearity_, vol. 20, no. 9, p. 2205, aug 2007. [Online]. Available: https://doi.org/10.1088/0951-7715/ 20/9/011

[18] M. Shen, W.-N. Chen, J. Zhang, H. S.-H. Chung, and O. Kaynak, "Optimal selection of parameters for nonuniform embedding of chaotic time series using ant colony optimization," _IEEE Transactions on Cybernetics_, vol. 43, no. 2, pp. 790-802, 2013.

[19] J. A. Gómez-García, J. I. Godino-Llorente, and G. Castellanos- Dominguez, "Non uniform embedding based on relevance analysis with reduced computational complexity: Application to the detection of pathologies from biosignal recordings," _Neurocomputing_, vol. 132, pp. 148-158, 2014, innovations in Nature Inspired Optimization and Learning Methods Machines learning for Non-Linear Processing. [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S0925231213009016

[20] S. Gerschgorin, "über die abgrenzung der eigenwerte einer matrix," _Izv. Math._, pp. 749-754, 1931.

[21] R. A. Horn and C. R. Johnson, _Matrix Analysis_. Cambridge University Press, 1985.

[22] G. H. Golub and C. F. Van Loan, _Matrix computations (3rd ed.)_. USA: Johns Hopkins University Press, 1996.

[23] V. Y. Pan, "How bad are vandermonde matrices?" _SIAM Journal on Matrix Analysis and Applications_, vol. 37, no. 2, pp. 676-694, 2016.

[24] M. Fekete, "Über die verteilung der wurzeln bei gewissen algebraischen glei-chungen mit ganzzahligen koeffizienten," _Mathematische_

