Now we show that with probability at least \(1-\mathrm{exp}(-\Omega(\epsilon^2\sqrt{n}\lambda))\),

\(\sum_{i\in T}\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\ge(1-2\epsilon)\sum_{i\in S}\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i).\) (13)

For each \(i\in S\), let _X<sub>i</sub>_ denote a random variable such that

\(X_i=\left\{\begin{array}{ c c }
\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i), & \text{with probability of}i\in T; \\
0, & \text{with probability of}i\notin T,
\end{array}\right.\)

and \(X=\sum_{i\in S}X_i\). By Lemma 6.1 (with \(\delta=\epsilon\)), We have

\(\mathbf{E}[X]\ge(1-\epsilon)\sum_{i\in S}\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i).\)

By Hoeffding bound (Theorem A.2),

\(\mathrm{Pr}[X-\mathbf{E}[X]\ge\epsilon\mathbf{E}[X]]\le 2\mathrm{exp}\left(-\frac{2\epsilon^2(\mathbf{E}[X])^2}{\sum_{i\in S}\left(\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\right)^2}\right)\)<br>
\(\le 2\mathrm{exp}\left(-\frac{2\epsilon^2(1-\epsilon)^2\left(\sum_{i\in S}\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\right)^2}{n^{3/2}}\right)\)<br>
\(\le 2\mathrm{exp}(-2\epsilon^2(1-\epsilon)^4\sqrt{n}\lambda)\)<br>
\(\le\mathrm{exp}(-\Omega(\epsilon^2\sqrt{n}\lambda)).\)

Hence, Equation (13) holds with probability at least \(1-\mathrm{exp}(-\Omega(\epsilon^2\sqrt{n}\lambda))\).

Conditioned on Equation (13), we have

\(\sum_{i\in T}\mathrm{lis}^{[\alpha_i,a_{\beta_i}]}(\mathsf{sa}_i)\ge\sum_{i\in T}(1-\epsilon)\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\)<br>
\(\ge(1-\epsilon)(1-2\epsilon)\sum_{i\in S}\mathrm{lis}^{[\mathsf{sm}(\mathsf{sa}_i),\mathsf{lg}(\mathsf{sa}_i)]}(\mathsf{sa}_i)\) (14)

\(\ge(1-\epsilon)(1-2\epsilon)(\mathrm{lis}(A)-\epsilon n\lambda)\)<br>
\(\ge(1-4\epsilon)\mathrm{lis}(A)\)

where the first inequality follows from the definition of _T_, the second inequality follows from Equation (13), the third inequality follows from Equation (12) and the last inequality follows from \(\mathrm{lis}(A)\ge n\lambda\).

Finally, by Equation (13) and (14), we have

\(\mathrm{Pr}\left[\sum_{i\in T}\mathrm{lis}^{[\alpha_i,a_{\beta_i}]}(\mathsf{sa}_i)\ge(1-4\epsilon)\mathrm{lis}(A)\right]\ge 1-\mathrm{exp}(-\Omega(\epsilon^2\sqrt{n}\lambda)).\)

