\begin{tabular}{cc}
No. & Model specification \\
1 & Algorithmic progress in both _N_ and _D_ \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
2 & No algorithmic progress in parameters _N_ \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
3 & No algorithmic progress in data _D_ \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
4 & Benchmark-specific in \(\alpha_\mathrm{year}\) \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha'_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
5 & Benchmark-specific in \(\beta_\mathrm{year}\) \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta'_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
6 & Benchmark-specific in \(\alpha_\mathrm{year}\) and \(\beta_\mathrm{year}\) \\
 & \(L=\mathrm{exp}[\alpha_\mathrm{const}-\alpha'_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta_\mathrm{const}-\beta'_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
7 & Benchmark-specific in \(\alpha_\mathrm{const}\) and \(\beta_\mathrm{const}\) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
8 & Benchmark-specific in \(\alpha_\mathrm{const}\) and \(\beta_\mathrm{const}\), with no algorithmic progress in _N_ \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
9 & Benchmark-specific in \(\alpha_\mathrm{const}\) and \(\beta_\mathrm{const}\), with no algorithmic progress in _D_ \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
10 & Benchmark-specific in \(\alpha_\mathrm{const},\alpha_\mathrm{year},\beta_\mathrm{const},\beta_\mathrm{year}\) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha'_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta'_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
11 & Benchmark-specific in \(\alpha_\mathrm{const},\alpha_\mathrm{year},\alpha_\mathrm{param},\beta_\mathrm{const},\beta_\mathrm{year}\) and \(\beta_\mathrm{data}\) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha'_\mathrm{year}(Y-Y_0)-\alpha'_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta'_\mathrm{year}(Y-Y_0)-\beta'_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
12 & ‘Hicks-neutral’ model \\
 & \(L=(\mathrm{exp}[\alpha'_\mathrm{const}+\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}+\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)])\mathrm{exp}[-\alpha_\mathrm{year}(Y-Y_0)]\) \\
13 & Transformer vs non-transformer scaling \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}^*(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}^*(\mathrm{log}D-\mathrm{log}D_0)]\) \\
14 & Progress only via changing scaling exponents \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{data}^\dagger(\mathrm{log}D-\mathrm{log}D_0)]\) \\
15 & Changing \(\alpha_\mathrm{year},\beta_\mathrm{year},\alpha_\mathrm{param}\), and \(\beta_\mathrm{data}\) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}^\dagger(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}^\dagger(\mathrm{log}D-\mathrm{log}D_0)]\) \\
16 & Benchmark-specific Hoffmann et al. 2022 scaling law (for comparison only) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
17 & Transformer-specific scaling law (for comparison only) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{param}^*(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{data}^*(\mathrm{log}D-\mathrm{log}D_0)]\) \\
18 & Compute-only model (for comparison only) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{compute}(\mathrm{log}(6ND)-\mathrm{log}(6N_0D_0)]\) \\
19 & Vocabulary fixed-effects (for comparison only) \\
 & \(L=\gamma\mathrm{log}(\mathrm{vocab})+\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
20 & Same as model 7 but with imputed epochs (for comparison only) \\
 & \(L=\mathrm{exp}[\alpha'_\mathrm{const}-\alpha_\mathrm{year}(Y-Y_0)-\alpha_\mathrm{param}(\mathrm{log}N-\mathrm{log}N_0)]+\mathrm{exp}[\beta'_\mathrm{const}-\beta_\mathrm{year}(Y-Y_0)-\beta_\mathrm{data}(\mathrm{log}D-\mathrm{log}D_0)]\) \\
\end{tabular}

10: Model specifications for leave-one-out cross validation.

