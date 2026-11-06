**Lemma 8.** _For any fixed_ \(s,t\in\mathcal{A}^*\)_, we have_

\(\gamma_k=lim_{n\rightarrow\infty}\frac{W_n(s,t)}{n}.\)

We let \(\vec{W}_n\) be the vector whose components are the _W<sub>n</sub>(s,t_) where _s_ and _t_ range over all strings of length _h_ for a given _h_. Equation (11) implies lower bounds on the components of \(\vec{W}_n\) based on \(W_{n-1}^{^\prime}\) and \(W_{n-2}^{^\prime}\).

**Fact 9.** _Let_ \(a\in\mathcal{A}\) _and_ \(s,t\in\mathcal{A}^*\)_, then_

\(W_n(as,at)\ge 1+\frac{1}{|\mathcal{A}|^2}\sum_{c,c^\prime\in\mathcal{A}}W_{n-2}(sc,tc').\) (13)

\begin{tabular}{cccccc}
k & Upper bound & _h_ used & Memory consumption & Computation time & Iterations \\
3 & 0.47626 & 8 & 6.4Gb & 1m28s & 50 iterations \\
4 & 0.57552 & 6 & 0.9Gb & 14s & 50 iterations \\
5 & 0.63792 & 6 & 3.4Gb & 1m10s & 50 iterations \\
6 & 0.68424 & 6 & 7.2Gb & 2m46s & 50 iterations \\
7 & 0.72016 & 6 & 9.4Gb & 4m03s & 50 iterations \\
8 & 0.74896 & 6 & 10.3Gb & 4m23s & 50 iterations \\
9 & 0.77264 & 6 & 10.4Gb & 4m43s & 50 iterations \\
10 & 0.7925 & 6 & 10.5Gb & 5m14s & 50 iterations \\
11 & 0.8095 & 6 & 10.5Gb & 5m43s & 50 iterations \\
12 & 0.82432 & 6 & 10.5Gb & 6m15s & 50 iterations \\
13 & 0.83744 & 6 & 10.5Gb & 6m57s & 50 iterations \\
14 & 0.84646 & 6 & 10.5Gb & 9m45s & 150 iterations \\
15 & 0.85608 & 6 & 10.5Gb & 10m54s & 150 iterations \\
16 & 0.86462 & 6 & 10.5Gb & 10m54s & 150 iterations \\
17 & 0.87228 & 6 & 10.5Gb & 10m50s & 150 iterations \\
18 & 0.87916 & 6 & 10.5Gb & 10m47s & 150 iterations \\
19 & 0.88536 & 6 & 10.5Gb & 10m54s & 150 iterations \\
20 & 0.89102 & 6 & 10.5Gb & 10m49s & 150 iterations \\
21 & 0.89614 & 6 & 10.5Gb & 10m55s & 150 iterations \\
22 & 0.90084 & 6 & 10.5Gb & 10m47s & 150 iterations \\
23 & 0.90514 & 6 & 10.5Gb & 10m46s & 150 iterations \\
24 & 0.90912 & 6 & 10.5Gb & 10m35s & 150 iterations \\
25 & 0.91278 & 6 & 10.5Gb & 10m52s & 150 iterations \\
32 & 0.93228 & 6 & 10.5Gb & 10m44s & 150 iterations \\
100 & 0.97946 & 6 & 10.5Gb & 28m & 500 iterations \\
1000 & 0.9982 & 6 & 10.5Gb & 3h40m & 5000 iterations \\
\end{tabular}

4: Our results for larger alphabets using the third version of the code. The results are all obtained using a laptop.

