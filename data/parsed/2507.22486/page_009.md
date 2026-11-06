Recall that \(L'=\mathsf{Project}(L,\Sigma_{[f..2f)}(L))\). Consider the subsequence \(\mathsf{RF}(L')\) of \(L'\) in which an arbitrary occurrence of each symbol is taken and everything else is deleted. Since every symbol occurs in \(L'\) less than 2_f_ times, we have that \(|\mathsf{RF}(L')|>|L'|/2f\ge\frac{|\mathsf{LCS}(x,y)|}{2logn}/2f=\frac{n^{3/4+t}}{4flogn}\) .

Assume that \(|\mathsf{LIS}_\pi(\mathsf{RF}(L'))|\ge n^t/logn\). Since \(\mathsf{LIS}_\pi(\mathsf{RF}(L'))\) is a subsequence of _y_, we have in particular that \(|\mathsf{LIS}_\pi(y)|\ge n^t/logn\). In this case, Line 3 returns a candidate of length at least _n<sup>t</sup>/logn_, which is an _n_<sup>3/4</sup>log_n_-approximation for LCS(_x,y_).

Assume from now on that \(|\mathsf{LIS}_\pi(\mathsf{RF}(L'))|<n^t/logn\). By Erdős-Szekeres theorem (Lemma 5), it holds that \(|\mathsf{LDS}_\pi(\mathsf{RF}(L'))|\ge|\mathsf{RF}(L')|/(n^t/logn)\ge\frac{n^{3/4}}{4f}\) . Consider the _i_th iteration of the while loop in Line 4. Denote \(\pi^i\) as the value of \(\pi'\) in this iteration, let \(\ell_i\) be the length of \(\mathsf{LIS}_{\pi^\prime}(y)\) in Line 6 in this iteration, and let _x<sup>i</sup>_ the value of \(x'\) at the beginning of the iteration \((x^0=x')\). We say that the _i_th iteration is _bad_, if \(\ell_i<\frac{n^t}{200}\) . Clearly, if there is some iteration that is not bad, the algorithm finds a candidate that is an _O(n_<sup>3/4</sup>)- approximation of LCS(_x,y_). In the following lemma we prove that there is an iteration that is not bad. This concludes the proof that Algorithm 2 is an _O(n_<sup>3/4</sup>log_n_)-approximation algorithm for the LCS problem, proving Theorem 1.

\(\triangleright\) Claim 9. There is at least one iteration that is not bad.

Proof. Assume by contradiction that all the iterations performed by the algorithm are bad. Let \(D=\mathsf{LDS}_\pi(\mathsf{RF}(L'))\), let \(D_i=\mathsf{Exclude}(D,\bigcup_{j=0}^{i-1}\pi^j)=\mathsf{Exclude}(D_{i-1},\pi^{i-1})\), and let \(x^i=\mathsf{Exclude}(x',\bigcup_{j=0}^{i-1}\pi^j)=\mathsf{Exclude}(x^{i-1},\pi^{i-1})\). Notice that _D<sub>i</sub>_ is a subsequence of _x<sup>i</sup>_ which is decreasing with respect to \(\pi\). Since \(\pi^i\) is a 2-approximation of \(\mathsf{LDS}_\pi(x^i)\), it holds that \(|\pi^i|\ge|\mathsf{LDS}_\pi(x^i)|/2\ge|D_i|/2\).

Let \(\tau^i=\mathsf{Project}(D_i,\pi^i)\). Since \(\tau^i\) is a subsequence of _D_, \(\tau^i\) is a decreasing subsequence of _y_ with respect to \(\pi\). Since \(\pi^i\) is also decreasing with respect to \(\pi\), then \(\tau^i\) is increasing with respect to \(\pi^i\). It follows that \(\ell_i=|\mathsf{LIS}_{\pi^i}(y)|\ge|\tau^i|\). Since the _i_th iteration is bad, \(|\tau^i|\le\ell_i\le\frac{n^t}{200}\) . It follows that \(|D_{i+1}|=|\mathsf{Exclude}(D_i,\pi^i)|=|D_i|-|\mathsf{Project}(D_i,\pi^i)|=|D_i|-|\tau^i|\ge|D_i|-\frac{n^t}{200}\) . By applying the above inequality inductively, we obtain \(|D_i|\ge|D|-i\cdot\frac{n^t}{200}>\frac{n^{3/4}}{4f}-i\cdot\frac{n^t}{200}\) .

On the other hand, we have that

\(|x^{i+1}|=|\mathsf{Exclude}(x^i,\pi^i)|\le|x^i|-|\pi^i|\cdot f\le|x^i|-|D_i|\cdot f/2,\)

where the first inequality holds since each symbol of \(\pi^i\) occurs in _x<sup>i</sup>_ at least _f_ times (as \(\pi^i\) is a subsequence of _x<sup>i</sup>_). By applying the above inequality inductively and observing that |_D_<sub>1</sub>|,|_D_<sub>2</sub>|_,...,|D<sub>i</sub>_| is a monotone decreasing sequence, we obtain \(|x^i|\le|x'|-i\cdot|D_i|\cdot f/2\).

Let _z_=25_n_<sup>1/4</sup>. On one hand, the _z_th iteration of the algorithm occurs, since \(|D_z|\ge|D|-25n^{1/4}\cdot\frac{n^t}{200}\ge\frac{n^{3/4}}{4f}-\frac{n^{1/4+t}}{8}\ge\frac{n^{3/4}}{8flogn}\) where the last inequality holds since \(t\le 1/4\) and \(f\le n^{1/4}\). In particular, _x<sup>z</sup>_ is not empty. On the other hand, the length of _x<sup>z</sup>_ in this iteration is \(|x^z|\le|x|-25n^{1/4}\cdot\frac{n^{3/4}}{8f}\cdot f/2\le n-25/16\cdot n\le 0\), in contradiction. \(\triangleleft\)

## References

**AB18** Amir Abboud and Karl Bringmann. Tighter connections between -SAT and shaving logs. In _ICALP_, volume 107 of _LIPIcs_, pages 8:1-8:18, 2018.

**ABW15** Amir Abboud, Arturs Backurs, and Virginia Vassilevska Williams. Tight hardness results for lcs and other sequence similarity measures. In _56th Annual IEEE Symposium on Foundations of Computer Science (FOCS)_, pages 59-78, 2015. `doi:10.1109/FOCS.2015. 14`.

