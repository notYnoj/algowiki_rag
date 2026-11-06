The study of \(\alpha_k\) (\(\alpha_4\) and \(\alpha_2\) in particular) only started more recently in the context of DNA reconstruction from reads with errors \[10\] and nearest neighbor search \[16\]. The best bounds known on the \(\alpha_k\) have been obtained recently \[3, 17\].

The main contribution of this article is to improve the upper bounds on the value of \(\alpha_k\) for small _k_ (see table 1a). For this, we adapt the technique that Lueker introduced to lower bounds \(\gamma_2\) \[14\]. We emphasize the fact that our proof relies on adapting the ideas of \[14\]. The proof requires the computation of a large vector obtained by the iteration of a particular transformation. We also provide another implementation of the technique used by Lueker for \(\gamma_k\) (which is also what was recently done in \[11\]). We improve the bounds for all considered values of \(\gamma_k\) other than \(\gamma_2\) and \(\gamma_4\) (see table 1b).

\begin{tabular}{cccc}
 & \multicolumn{2}{c}{Upper bounds} & Lower bounds \\
k & Our results & from \[3\] & from \[3\] \\
2 & **0.315514** & 0.36932 & 0.17372\[14\] \\
3 & **0.47276** & 0.53426 & 0.28366 \\
4 & **0.56578** & 0.63182 & 0.35978 \\
5 & **0.6325** & 0.70197 & 0.41517 \\
6 & **0.68424** & 0.75149 & 0.45776 \\
7 & **0.72016** & 0.79031 & 0.49183 \\
8 & **0.74896** & 0.81166 & 0.51990 \\
9 & **0.77264** & & \\
10 & **0.7925** & & \\
11 & **0.8095** & & \\
12 & **0.82432** & & \\
13 & **0.83744** & & \\
14 & **0.84646** & & \\
15 & **0.85608** & & \\
16 & **0.86462** & 0.89554 & 0.64475 \\
17 & **0.87228** & & \\
18 & **0.87916** & & \\
19 & **0.88536** & & \\
20 & **0.89102** & & \\
21 & **0.89614** & & \\
22 & **0.90084** & & \\
23 & **0.90514** & & \\
24 & **0.90912** & & \\
25 & **0.91278** & & \\
32 & **0.93228** & 0.96588 & 0.73867 \\
100 & **0.97946** & & \\
100 & **0.97982** & & \\
\end{tabular}

\begin{tabular}{cccc}
 & \multicolumn{2}{c}{Lower bounds} & Upper bounds \\
k & Our results & Previous best & from \[7\] \\
2 & 0.789872 & **0.792665 \[11\]** & 0.8263\[14\] \\
3 & **0.68422** & 0.682218 \[11\] & 0.76581 \\
4 & 0.61422 & **0.614333 \[11\]** & 0.70824 \\
5 & **0.56206** & 0.549817 \[11\] & 0.66443 \\
6 & **0.51850** & 0.4992299 \[11\] & 0.62932 \\
7 & **0.48712** & 0.466481 \[11\] & 0.60019 \\
8 & **0.46074** & 0.438799 \[11\] & 0.57541 \\
9 & **0.43806** & 0.414876 \[11\] & 0.55394 \\
10 & **0.41826** & 0.393811 \[11\] & 0.53486 \\
11 & **0.40072** & 0.37196 \[7\] & 0.51785 \\
12 & **0.38504** & 0.35899 \[7\] & 0.50260 \\
13 & **0.37088** & 0.34737 \[7\] & 0.48880 \\
14 & **0.35798** & 0.33687 \[7\] & 0.47620 \\
15 & **0.34616** & 0.32732 \[7\] & 0.46462 \\
16 & **0.33528** & & \\
17 & **0.32518** & & \\
18 & **0.31580** & & \\
19 & **0.30702** & & \\
20 & **0.29880** & & \\
21 & **0.29106** & & \\
22 & **0.28376** & & \\
23 & **0.27686** & & \\
24 & **0.27032** & & \\
25 & **0.26412** & & \\
50 & **0.16930** & & \\
100 & **0.0991** & & \\
1000 & **0.01164** & & \\
\end{tabular}

(a) New upper bounds on \(\alpha_k\)

(b) New lower bounds on \(\gamma_k\)

1: A summary of the bounds provided in this article. We indicate in bold the best results.

