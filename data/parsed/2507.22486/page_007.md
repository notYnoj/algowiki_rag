<tbc>this reasoning, we conclude that _x_ is reduced relatively quickly - _D_ is barely affected by a sequence of _bad_ iterations and therefore remains a candidate for the next \(\pi'\). By carefully selecting a threshold that distinguishes _good_ from _bad_ iterations, we show that if all iterations are _bad_, then _x_ is completely deleted after a certain number of iterations. On the other hand, under this assumption, some symbols of _D_ must still remain in _x_ after this many iterations - a contradiction. Hence, we conclude that at least one iteration must be _good_.

We now proceed to formally bound the approximation ratio achieved by the algorithm. Consider the _i_th iteration of the while loop in Line 4. Denote by \(\pi^i\) the value of \(\pi'\) in this iteration, let \(\ell_i\) be the length of \(\mathsf{LIS}_{\pi^\prime}(y)\) in Line 6 in this iteration, and let _x<sup>i</sup>_ be the value of _x_ at the beginning of the iteration (_x_<sup>0</sup>=_x_). We say that the _i_th iteration is _bad_, if \(\ell_i<n^t/4\). Clearly, if there is some iteration that is not bad, the algorithm finds a candidate that is a 4_n_<sup>4/5</sup>-approximation of LCS(_x,y_). In the following lemma we prove that there is an iteration that is not bad. This concludes the proof that Algorithm 1 is a 4_n_<sup>4/5</sup>-approximation algorithm for the LCS problem.

\(\triangleright\) Claim 7. There is at least one iteration that is not bad.

Proof. Assume by contradiction that all the iterations performed by the algorithm are bad. Let \(D=\mathsf{LDS}_\pi(\mathsf{RF}(L))\), and for every iteration _i_ let \(D_i=\mathsf{Exclude}(D,\bigcup_{j=0}^{i-1}\pi^j)=\mathsf{Exclude}(D_{i-1},\pi^{i-1})\), and let \(x^i=\mathsf{Exclude}(x,\bigcup_{j=0}^{i-1}\pi^j)=\mathsf{Exclude}(x^{i-1},\pi^{i-1})\). Notice that _D<sub>i</sub>_ is a subsequence of _x<sup>i</sup>_ which is decreasing with respect to \(\pi\). Since \(\pi^i\) is a 2-approximation of \(\mathsf{LDS}_\pi(x^i)\), it holds that \(|\pi^i|\ge|\mathsf{LDS}_\pi(x^i)|/2\ge|D_i|/2\).

Let \(\tau^i=\mathsf{Project}(D_i,\pi^i)\). Since \(\tau^i\) is a subsequence of _D_, \(\tau^i\) is a decreasing subsequence of _y_ with respect to \(\pi\). Since \(\pi^i\) is also decreasing with respect to \(\pi\), then \(\tau^i\) is increasing with respect to \(\pi^i\). It follows that \(\ell_i=|\mathsf{LIS}_{\pi^i}(y)|\ge|\tau^i|\). Since the _i_th iteration is bad, \(|\tau^i|\le\ell_i\le n^t/4\). It follows that \(|D_{i+1}|=|\mathsf{Exclude}(D_i,\pi^i)|=|D_i|-|\mathsf{Project}(D_i,\pi^i)|=|D_i|-|\tau^i|\ge|D_i|-n^t/4\). By applying the above inequality inductively, we obtain \(|D_i|\ge|D|-i\cdot n^t/4>n^{4/5-t}-i\cdot n^t/4\).

On the other hand, we have that

\(|x^{i+1}|=|\mathsf{Exclude}(x^i,\pi^i)|\le|x^i|-|\pi^i|\le|x^i|-|D_i|/2,\)

where the first inequality holds since each symbol of \(\pi^i\) occurs in _x<sup>i</sup>_ at least once (as \(\pi^i\) is a subsequence of _x<sup>i</sup>_). By applying the above inequality inductively and observing that |_D_<sub>1</sub>|,|_D_<sub>2</sub>|_,...,|D<sub>i</sub>_| is a monotone decreasing sequence, we obtain \(|x^i|\le|x|-i\cdot|D_i|/2\).

Let _z_=2_n_<sup>1/5+_t_</sup>. On one hand, the _z_th iteration of the algorithm occurs, since \(|D_z|\ge|D|-2n^{1/5+t}\cdot n^t/4\ge n^{4/5-t}-n^{1/5+2t}/2\ge n^{4/5-t}/2\) where the last inequality holds since \(t\le 1/5\). In particular, _x<sup>z</sup>_ is not empty. On the other hand, the length of _x<sup>z</sup>_ in this iteration is \(|x^z|\le|x|-2n^{1/5+t}\cdot|D_z|/2\le n-2n^{1/5+t}\cdot n^{4/5-t}/2=n-n=0\), in contradiction. \(\triangleleft\)

## 4 Better Algorithm - Proof of Theorem 1

In this section, we present an improved approximation algorithm that achieves an _O(n_<sup>3/4</sup>log_n_)- approximation to LCS(_x,y_).

For an interval of numbers [_a..b_] denote \(\Sigma_{[a..b]}(x)=\{\sigma\in\Sigma|\#_\sigma(x)\in[a..b]\}\). The following pseudocode describes the algorithm.

