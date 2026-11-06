<tbc>Furthermore, we have from Proposition 2.2 that<tbc>

\(\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(p(i))=(1\pm b)n(-1+O(n^{-\alpha_\mathrm{gr}}\mathrm{log}(n))),\)

<tbc>and it follows that

\(\mathrm{log}(N_1)=\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(n^2)+4\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(p(i))\)<br>
\(\pm\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}2bn^{4\alpha_\mathrm{gr}}\mathrm{log}(n)\)<br>
\(=n\mathrm{log}(n^2)+O(n^{1-\alpha_\mathrm{gr}}\mathrm{log}(n^2))-4n+O(n^{1-\alpha_\mathrm{gr}}\mathrm{log}(n))\)<br>
\(\pm O(bn^{1+4\alpha_\mathrm{gr}}\mathrm{log}(n))\)<br>
\(=n(2\mathrm{log}(n)-4\pm n^{-\alpha_\mathrm{gr}/2}).\)

Now, fixing a perfect matching _M_ in T , the number of times _M_ could be counted in this process is at most the number of ways to pick from T<sup>-_A_<sup>∗</sup></sup> (with order) the first \((1\pm b)n-n^{1-\alpha_\mathrm{gr}}\) edges of _M_, that is \(N_2:=\prod_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}((1\pm b)n-i)\). Again taking logs we have

\(\mathrm{log}(N_2)=\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}((1\pm b)n-i)=\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}((1\pm b)p(i)n)\)<br>
\(=\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(p(i))+\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(n)\)<br>
\(+\sum_{i=0}^{(1\pm b)n-n^{1-\alpha_\mathrm{gr}}-1}\mathrm{log}(1\pm b)\)<br>
\(=n(-1+O(n^{-\alpha_\mathrm{gr}}\mathrm{log}(n))+\mathrm{log}(n)\pm O(b\mathrm{log}(n)))\)<br>
\(=n(\mathrm{log}(n)-1\pm n^{-\alpha_\mathrm{gr}/2}).\)

It follows that<tbc>

\(\mathrm{log}(T(n))\ge\mathrm{log}\left(\frac{N_1}{N_2}\right)=n(\mathrm{log}(n)-3\pm 2n^{-\alpha_\mathrm{gr}/2}),\)

<tbc>and so (using a Taylor expansion),

\(T(n)\ge\left(e^{\mathrm{log}(n)}\cdot e^{-3}\cdot e^{\pm 2n^{-\alpha_\mathrm{gr}/2}}\right)^n\)<br>
\(=\left(\frac{n}{e^3}(1\pm n^{-\alpha_\mathrm{gr}/3})\right)^n\)<br>
\(=\left((1+o(1))\frac{n}{e^3}\right)^n,\)

as claimed. □

Thus the problem of lower bounding _T(n_) becomes the problem of proving Lemma 5.6.

