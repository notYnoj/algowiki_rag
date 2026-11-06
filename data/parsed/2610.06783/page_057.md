\((XY)[r,c]=\sum_{(k,\beta)}X[r,(k,\beta)]Y[(k,\beta),c]\) is the number of pairs (_x,y_) of the same color with blk(_x)\<_blk(_y_), as required, and the entries of _X_ and _Y_ are between 0 and _d_ because a list has at most _d_ numbers. We use _O(nd_log_n_) comparisons to sort and then fill in _X_ and _Y_ in \(O(nD'')\) time.

_Same block._ For every color _k_ and block \(\beta\), let _I_ be the numbers _x_ of row lists in the block, each with its row, and let _J_ be the numbers _y_ of column lists in the block, each with its column, so that \(|I|+|J|\le s\). For every \((x,y)\in I\times J\) with pos(_x)\<_pos(_y_) whose row and column form a pair \((r,c)\in P\) (this can be tested via a binary search in _P_ after it is sorted), we add 1 to \(\gamma_2(r,c)\). Then \(\gamma_2\) counts the pairs of the second kind. Since \(|I||J|\le s^2/4\) and there are at most 2_nd/s+d_ blocks, we enumerate at most \((2nd/s+d)s^2/4\le nds+ds^2\) pairs (_x,y_). Together with sorting _P_ and outputting the |_P_| integers \(\gamma_2(r,c)\), this takes _O_((|_P_|+_nds+ds_<sup>2</sup>)log_n_) time.

**Corollary 38.** _Let_ \(d\le n^{1/40}\)_, and let n be larger than a suitable constant. Given row lists_ R_<sub>r</sub> and column lists_ C_<sub>c</sub> as above and a set_ \(P\subseteq[n]^2\)_, the counts_ \(\gamma(r,c)\), \((r,c)\in P\)_, with\<or with_ \(\le\)_, can be computed deterministically in_

\(O\big(|P|n^{0.0229}+n^2/d^{0.126}+n^{2-1/440}logn\big)\)

_time, by an algorithm whose only operations on real numbers are comparisons._

_Proof._ Apply Lemma 37 with \(s:=\lceil n^{1-1/440}/d\rceil\), so that \(D''\le 2d^2n^{1/440}+d+1\le 3d^2n^{1/440}\), and pad the product to the inner dimension \(D^*:=\lceil 3d^2n^{1/440}\rceil\) with zero columns of _X_ and zero rows of _Y_ . Since \(d\le n^{1/40}\), we have \(D^*\le 4n^{23/440}\), so \((D^*)^{18}\le 4^{18}n^{0.941}\le n\), and Corollary 26 with _N_:=_n_ and _D_:=_D_<sup>∗</sup> computes (_XY_)\[_r,c_\] for all \((r,c)\in P\) deterministically in _O_(|_P_|(_D_<sup>∗</sup>)<sup>0.437</sup>+_n_<sup>2</sup>/(_D_<sup>∗</sup>)<sup>0.063</sup>) time. Here \((D^*)^{0.437}\le 4^{0.437}n^{0.437\cdot 23/440}=O(n^{0.0229})\) and \((D^*)^{0.063}\ge(3d^2)^{0.063}\ge d^{0.126}\).

Since \(nD^*=O(n^{1.06})\), \(nds\le 2n^{2-1/440}\) and \(ds^2\le 4n^{2-1/440}\), the time of Lemma 37 itself is

\(O(nD^*+(|P|+nds+ds^2)logn)=O(|P|n^{0.0229}+n^{2-1/440}logn).\)

_Proof of Theorem 35._ Let \(d:=\lfloor n^{1/40}\rfloor\), apply Lemma 36 with this _d_, and answer every comparison count by Corollary 38.

(min,+)_-product, APSP, and Exact Triangle._ By Corollary 38, the _d_ comparison counts of a counting call cost<tbc>

\(\sum_{k\in[d]}O\big(|P_k|n^{0.0229}+n^2/d^{0.126}+n^{2-1/440}logn\big)=O(n^{2.0229}logn),\)

<tbc>since \(\sum_k|P_k|=n^2\), \(d\cdot n^2/d^{0.126}\le n^{2+0.874/40}\le n^{2.0219}\), and \(d\cdot n^{2-1/440}\le n^{2+1/40-1/440}\le n^{2.0228}\), forming the lists costs _O(nd_<sup>2</sup>)=_O(n_<sup>1.05</sup>). So the \(\tilde{O}(n/d)\) counting calls of Lemma 36(a) cost

\(\tilde{O}\big((n/d)n^{2.0229}\big)=\tilde{O}\big(n^{3-1/40+0.0229}\big)\le O(n^{2.998})\)

expected time, and its additional time is \(\tilde{O}(n^3/d)=\tilde{O}(n^{2.975})\).

3_SUM._ By Corollary 38, a comparison count of Lemma 36(b) costs<tbc>

\(O\big(\frac{n^2}{d}n^{0.0229}+\frac{n^2}{d^{0.126}}+n^{2-1/440}logn\big)=O\big(n^{2-1/40+0.0229}logn\big)=O(n^{1.9979}logn),\)

