**Objective** Find the longest path from \(\langle 0,n_X\rangle\) to \(\langle n_X+n_Y,n_Y\rangle\).

We show that such sparsifications do not incur too much error:

**Lemma 5.8** (Sparsified problems approximates original problems)**.**<br>
_Let p be the shortest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path in the Rotated Edit Distance Grid Graph. There exists a path_ \(\widehat{p}\) _with_ \(w(\widehat{p})\le w(p)+n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) _in the Sparsified Edit Distance Grid Graph._

_Similarly, let p be the longest_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path in the Rotated LCS Grid Graph. There exists a path_ \(\widehat{p}\) _with_ \(w(\widehat{p})\ge w(p)-n/2^{\Omega\left(\mathrm{log}^{0.009}(n)\right)}\) _in the Sparsified LCS Grid Graph._

Towards proving Lemma 5.8. For both the Rotated LCS Grid Graph and the Rotated Edit Distance Grid Graph, we have the following lemma, which says that we can slightly change the endpoints of a path so that the resulting paths differ in weights only after a few columns.

**Lemma 5.9** (Rounding the endpoints of a path)**.**<br>
_Let p<sub>A</sub> be a path from any_ \(\langle l,y_l\rangle\) _to any_ \(\langle r,y_r\rangle\) _on the Rotated LCS Grid Graph or the Rotated Edit Distance Grid Graph, where l,y<sub>l</sub>,r,y<sub>r</sub> are all even. For any even_ \(y'_l\) _and_ \(y'_r\)_with_ \(|y'_l-y'_r|\le r-l\)_, we can change p<sub>A</sub> into a path p<sub>B</sub> from_ \(\langle l,y'_l\rangle\) _to_ \(\langle r,y'_r\rangle\) _such that_ \(|w(p_A)-w(p_B)|\le|y_l-y'_l|+|y_r-y'_r|\)_. Moreover, there are at most_ \(|y_l-y'_l|+|y_r-y'_r|\) _columns before which p<sub>A</sub> and p<sub>B</sub> differ in weights._

_Proof._ We will give the proof for the Rotated LCS Grid Graph. The proof for the Rotated Edit Distance Grid Graph is identical.

We first argue that we can locally adjust the endpoint of the path by \(\pm 2\), losing at most a weight of +2. In other words, there is a path of weight \(\ge w(p_A)-2\) from \(\langle l,y_l\rangle\) to \(\langle r,y_r-2\rangle\). (The analogous claim also follows by symmetry for paths from \(\langle l,y_l\rangle\) to \(\langle r,y_r+2\rangle\), and similarly at the left end.)

Suppose \(y_l-(y_r-2)\le r-l\), we will adjust _p<sub>A</sub>_ to get a path \(p_A'\) from \(\langle l,y_l\rangle\) to \(\langle r,y_r-2\rangle\) with a weight difference of at most 2. Let _I_ be the maximum index such that \(p_A(I)-p_A(I-1)\ge 0\). Such an index exists since _y<sub>l</sub>-y<sub>r</sub>\<r-l_ (otherwise _y<sub>l</sub>_-(_y<sub>r</sub>_-2)_\>r-l_). If _p<sub>A</sub>(I_)=_p<sub>A</sub>(I_-1)+1, we let \(p_A'\) be such that<tbc>

\(p_A'(i)=p_A(i)-2\cdot\unknown[i\ge I].\)

<tbc>Otherwise we have _p<sub>A</sub>(I_)=_p<sub>A</sub>(I_-1). This would imply that _p<sub>A</sub>(I_-2)=_p<sub>A</sub>(I_-1) since \(\langle I-1,p_A(I-1)\rangle\) is a vertex created by splitting a shortcut edge. We let \(p_A'\) be such that

\(p_A'(i)=p_A(i)-\unknown[i\ge I-1]-\unknown[i\ge I].\)

Since every edge connecting vertices on different rows has identical weights (0 for LCS), both _p<sub>A</sub>_ and \(p_A'\) have identical weights per column after column _I_. Therefore, in either case, the only possible weight differences between _p<sub>A</sub>_ and \(p_A'\) involve at most two edges, which means that the weight difference between _p<sub>A</sub>_ and \(p_A'\) is at most 2.

To prove the lemma, we now apply this local "\(\pm 2\)" adjustment \(|y_l-y'_l|/2+|y_r-y'_r|/2\) times. (Notice that there always exists an order of the local adjustments where a path exists between every intermediate pair of endpoints.) Each adjustment changes the weight by at most 2, and affects at most one column. Therefore, the total weight difference is at most \(|y_l-y'_l|+|y_r-y'_r|\), and the number of columns where the path differs is also at most \(|y_l-y'_l|+|y_r-y'_r|\), as claimed.

Now we prove Lemma 5.8:

