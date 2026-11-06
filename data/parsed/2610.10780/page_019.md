**Lemma 10.** _There exists a constant_ \(\rho''\in(0,0.18)\) _such that_ \(|S(\Gamma)\cap I''|<\rho''m_{j-1}\) _for every basic interval_ \(I''\) _of I_<sup>∗</sup>.

_Proof._ The proof follows the previous work \[20, 28\].

Consider a graph _G<sub>tf</sub>_ computed from (_A<sub>tf</sub>,B<sub>t</sub>_) in our algorithm, where \(1\le f\le g\). Some edges of _G<sub>tf</sub>_ contribute distances in _E_. We partition all such graphs _G<sub>tf</sub>_ into two sets. Let G<sub>1</sub> denote the set of graphs _G<sub>tf</sub>_ that contribute fewer than 3(|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|) distances in \(E\cap I''\), and let G<sub>2</sub> denote the set of the remaining graphs.

## The set G<sub>1</sub>.

Let \(I''=(\delta',\delta'']\). For a graph \(G_{tf}\in\mathcal{G}_1\), built on the pair (_A<sub>tf</sub>,B<sub>t</sub>_), let D_<sub>tf</sub>_ be the set of annuli centered at the points of _A<sub>tf</sub>_ with radii \(\delta'\) and \(\delta''\). Consider a 1_/r_-cutting \(\Xi\) for D_<sub>tf</sub>_, where _r_ is a constant to be chosen later. The cutting partitions the plane into _O(r_<sup>2</sup>) cells so that, for every cell \(\sigma\), at most |D_<sub>tf</sub>|/r_ annuli in D_<sub>tf</sub>_ have a boundary circle intersecting the interior of \(\sigma\).

For each cell \(\sigma\in\Xi\), let \(B_t(\sigma)\) denote the points of _B<sub>t</sub>_ inside \(\sigma\), let \(A_{tf}(\sigma)\) be the points of _A<sub>tf</sub>_ whose annuli fully contain \(\sigma\), and let \(A'_{tf}(\sigma)\) be the points of _A<sub>tf</sub>_ whose annuli have at least one boundary circle intersecting \(\sigma\). Let _N<sub>tf</sub>_ denote the number of interpoint distances between _A<sub>tf</sub>_ and _B<sub>t</sub>_ that lie in \(I''\). Then<tbc>

\(N_{tf}\le\sum_{\sigma\in\Xi}|A_{tf}(\sigma)||B_t(\sigma)|+\sum_{\sigma\in\Xi}|A'_{tf}(\sigma)||B_t(\sigma)|.\)

<tbc>Since \(|A'_{tf}(\sigma)|\le|A_{tf}|/r\) and \(\sum_{\sigma\in\Xi}|B_t(\sigma)|=|B_t|\), we obtain<tbc>

\(\sum_{\sigma\in\Xi}|A'_{tf}(\sigma)||B_t(\sigma)|=O\big(\frac{|A_{tf}||B_t|}{r}\big).\)

<tbc>Now consider \(\sum_{\sigma\in\Xi}|A_{tf}(\sigma)||B_t(\sigma)|\). Note that for any \(a\in A_{tf}(\sigma)\) and \(b\in B_t(\sigma)\), we have \(\|ab\|\in I''\). If the edge (_a,b_) exists in _G<sub>tf</sub>_, then \(\|ab\|\) must lie in \(E\cap I''\). Since \(G_{tf}\in\mathcal{G}_1\), it has fewer than 3(|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|) such edges. By \[20, Corollary 2.5\], if _X_ and _Y_ are two vertex subsets of a _d_-regular expander graph on _M_ vertices and there are fewer than 3_M_ edges between _X_ and _Y_ , then \(|X||Y|\le 9M^2/d\). Applying this with \(X=A_{tf}(\sigma)\), \(Y=B_t(\sigma)\), and _M_=|_A<sub>tf</sub>_|+|_B<sub>t</sub>_|, we get<tbc>

\(\sum_{\sigma\in\Xi}|A_{tf}(\sigma)||B_t(\sigma)|\le O(r^2)\cdot\frac{9(|A_{tf}|+|B_t|)^2}{d}=O\big(\frac{r^2(|A_{tf}|+|B_t|)^2}{d}\big).\)

<tbc>Therefore,<tbc>

\(N_{tf}=O\big(\frac{|A_{tf}||B_t|}{r}\big)+O\big(\frac{r^2(|A_{tf}|+|B_t|)^2}{d}\big).\)

<tbc>Since \(|B_t|\le|A_{tf}|\le 2|B_t|\), we have \((|A_{tf}|+|B_t|)^2\le 5|A_{tf}||B_t|\). Hence,<tbc>

\(N_{tf}=O\big(\left[\frac{1}{r}+\frac{r^2}{d}\right]|A_{tf}||B_t|\big).\)

<tbc>Choosing _r=d_<sup>1/3</sup> and taking _d_ sufficiently large, we obtain<tbc>

\(N_{tf}\le 0.01\cdot|A_{tf}||B_t|.\)

<tbc>Summing over all graphs \(G_{tf}\in\mathcal{G}_1\) gives<tbc>

\(N(\mathcal{G}_1)\le 0.01\cdot\sum_{G_{tf}\in\mathcal{G}_1}|A_{tf}||B_t|,\)

