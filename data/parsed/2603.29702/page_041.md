• _Each edge has weight_ 1 _with probability at most p=O_(1_/d_<sup>2</sup>);<tbc>

• _Edges from different layers are independent in weights. Specifically, let E be a set of edges, and let e be a layer-L edge. Suppose that no edge in E is also a layer-L edge. Then_ **Pr**(_e’s weight is_ 1)=**Pr**(_e’s weight is_ 1|_weights of E are known)._

_With probability_ \(1-N^{-\omega(1)}\)_, no path from u has a length (sum of edge weights) of_ \(\omega(h\sqrt{\mathrm{log}(N)}/\mathrm{min}(d,B))\).

Before proving the ingredient above, we first give our main analysis that our estimate is sound:

**Lemma 6.10** (Restated)**.** _Let_ \(\widehat{p}\) _be the shortest_ \(\widetilde{S}\)_-regular_ \(\langle 0,n_X\rangle\)_-_\(\langle n_X+n_Y,n_Y\rangle\) _path. Suppose_ \(w(\widehat{p})=n/2^{o\left(\mathrm{log}^{0.01}(n)\right)}\)_. With probability_ 1-_o_(1), est\[0_,n<sub>X</sub>,n<sub>X</sub>+n<sub>Y</sub>,n<sub>Y</sub>_\]_\>_(1-_o_(1))_w_(\(\widehat{p}\));

_Proof._ For each active scale _s_, we consider the following question: how much would we underestimate if there were no subsampling on active scales larger than _s_? To capture this, consider the Scale-_s_ Sparsified Grid Graph G_<sub>s</sub>_ defined on est (Definition 6.8), namely the following graph:

**Vertices** We only consider vertices \(\langle x,y\rangle\) in the Sparsified Edit Distance Grid Graph with the additional constraint that _I<sub>s</sub>|x_;

**Edges** There is an edge from \(\langle x,y\rangle\) to \(\langle x+I_s,y\rangle\) (if both exist) such that \(|y'-y|\le I_s\) with a weight of \(\mathrm{est}[x,y,x+I_s,y']\).

Let A_<sub>s</sub>_ be the length of the shortest \(\widetilde{S}\)-regular \(\langle 0,n_X\rangle\)-\(\langle n_X+n_Y,n_Y\rangle\) path in G_<sub>s</sub>_. We can see that \(\mathcal{A}_0=w(\widehat{p})\), and that \(\mathcal{A}_S=\mathrm{est}[0,n_X,n_X+n_Y,n_Y]\), namely our final estimate for \(w(\widehat{p})\). To see how much smaller A_<sub>S</sub>_ can be compared to A<sub>0</sub>, we go through each scale _s_ and examine the difference between A<sub>_s_-1</sub> and A_<sub>s</sub>_.

If scale-_s_ is passive, then since we compute est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] to be the length of the shortest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in the Scale-(_s_-1) Sparsified Grid Graph, A_<sub>s</sub>_=A<sub>_s_-1</sub>.

If scale-_s_ is active, then from Claim 6.7, for est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] such that (_l,r_\] is a scale-_s_ interval:

• The shortest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in G<sub>_s_-1</sub> is \(X:=\sum_{i=1}^M\mathrm{est}[m_{i-1},\overline{y_i},m_i,\overline{y_i}]\);<tbc>

• The shortest \(\widetilde{S}\)-regular \(\langle l,y_l\rangle\)-\(\langle r,y_r\rangle\) path in G_<sub>s</sub>_, namely est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\], is at least \(X-o\left(\frac{w(\widehat{p}(l,r])}{\mathrm{log}^{0.02}(n)}\right)\) with probability \(1-\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\). Even if the error guarantee fails, the underestimation is at most \(X\le I_s\).

Thus, going from A<sub>_s_-1</sub> to A_<sub>s</sub>_, we have:

• Type I: per scale-_s_ interval (_l,r_\], underestimation of at most \(o\left(\frac{w(\widehat{p}(l,r])}{\mathrm{log}^{0.02}(n)}\right)\);<tbc>

• Type II: for est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] such that (_l,r_\] is a scale-_s_ interval, there is a probability of \(\mathrm{exp}\left(-\omega\left(\mathrm{log}^{0.02}(n)\right)\right)\) that est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] has an underestimation of at most _I<sub>s</sub>_.

We now prove that with probability 1-_o_(1), the total error across both types and all scales and intervals is \(o(w(\widehat{p}))\).

Recall that \(|\widetilde{S}|=O(S^{0.02})=o\left(\mathrm{log}^{0.02}n\right)\) w.p. 1-_o_(1). Thus the total type I underestimation across all \(\left|\widetilde{S}\right|\) active scales is \(o((w(\widehat{p})))\) w.p. 1-_o_(1).

For type II underestimation, we say an estimate est\[_l,y<sub>l</sub>,r,y<sub>r</sub>_\] is "bad" if it exhibits an underestimation of \(\Omega(w(p(l,r])/\mathrm{log}^{0.02}(n))\). The total underestimation from estimates being bad is upper bounded by the following model:

