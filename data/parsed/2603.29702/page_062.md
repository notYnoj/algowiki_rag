**Lemma 7.11** (Restated)**.** _Let_ \(\widehat{p}\) _be the longest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) _path. Suppose_ \(w(\widehat{p})=n/2^{o\left(log^{0.01}(n)\right)}\)_. With probability_ 1-_o_(1), est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_\<_(1+_o_(1))_w_(\(\widehat{p}\));

_Proof._ For each active scale _s_, we consider the following question: how much would we overestimate if there were no subsampling on active scales larger than _s_? To capture this, consider the Scale-_s_ Sparsified Grid Graph G_<sub>s</sub>_ defined on est (Definition 7.9), namely the following graph:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified LCS Grid Graph with the additional constraint that _I<sub>s</sub>|x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_s,y'\rangle\) (if both exist) such that \(|y'-y|\le I_s\) with a weight of \(est[x,y,x+I_s,y']\).

Let A_<sub>s</sub>_ be the length of the longest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path in G_<sub>s</sub>_. We can see that \(\mathcal{A}_0=w(\widehat{p})\), and that \(\mathcal{A}_S=est[0,n_X,n_X+n_Y,n_Y]\), namely our final estimate for \(w(\widehat{p})\). To see how much larger A_<sub>S</sub>_ can be compared to A<sub>0</sub>, we go through each scale _s_ and examine the difference between A<sub>_s_-1</sub> and A_<sub>s</sub>_.

If scale-_s_ is passive, then since we compute est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] to be the length of the longest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)- \(\langle r,y_r\rangle\) path in the Scale-(_s_-1) Sparsified Grid Graph, A_<sub>s</sub>_=A<sub>_s_-1</sub>.

If scale-_s_ is active, then from Claim 7.8, for est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] such that (_l,r_\] is a scale-_s_ interval:

• The length of the longest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in G<sub>_s_-1</sub> is \(X:=\sum_{i=1}^Mest[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\);<tbc>

• The length of the longest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in G_<sub>s</sub>_, namely est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\], is, with probability \(1-exp\left(-\omega\left(log^{0.02}(n)\right)\right)\), at most \(\left(1+O(1/log^{0.02}(n))\right)X\). Notice that the our estimate for the length of a path from column _l_ to column _r_ cannot be more than the "width" _r-l=I<sub>s</sub>_. Even if the error guarantee fails, the overestimation is at most _I<sub>s</sub>_.

Thus, going from A<sub>_s_-1</sub> to A_<sub>s</sub>_, we have:

• Type I: per scale-_s_ interval (_l,r_\], multiplicative overestimation of at most \(\left(1+O(1/log^{0.02}(n))\right)\);<tbc>

• Type II: for est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] such that (_l,r_\] is a scale-_s_ interval, there is a probability of \(exp\left(-\omega\left(log^{0.02}(n)\right)\right)\) that est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] has an overestimation of at most _I<sub>s</sub>_.

We now prove that with probability 1-_o_(1), either error across all scales and intervals is \(o(w(\widehat{p}))\).

Recall that \(|\widetilde{S}|=O(S^{0.02})=o\left(log^{0.02}n\right)\) w.p. 1-_o_(1). Thus the total type I multiplicative overesti mation across all \(\left|\widetilde{S}\right|\) active scales is (1+_o_(1)) w.p. 1-_o_(1).

For type II overestimation, we say an estimate est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] is "bad" if it exhibits an overestimation of \((1+\Omega(1/log^{0.02}(n)))\). the total overestimation from estimates being bad is upper bounded by the following model:

**Definition 7.14** (Upper Bound for Overestimation due to "Bad" Estimates)**.** Consider the following graph:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified LCS Grid Graph with the additional constraint that _I<sub>s</sub>|x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_s,y'\rangle\) such that \(|y'-y|\le I_s\) with a weight of either _I<sub>s</sub>_, if \(est[x,y,x+I_s,y']\) is "bad," or 0 otherwise.

