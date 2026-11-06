Assume now that \(R\in\mathcal{R}_i\) and \(R'\unknown\in\mathcal{R}_i\); recall that we assume that \(R'\) lies above _R_. Then all rows that lie between _R_ and \(R'\) must be empty, so it is easy to verify that _R_ must be the last row of R_<sub>i</sub>_ (or it must be the last row of \(\mathcal{R}'_i\)). In either case, at most one such crossing is possible.

Lastly, we assume that \(R\unknown\in\mathcal{R}_i\) and \(R'\in\mathcal{R}_i\). The analysis is symmetric; it is easy to see that at most one such crossing is possible.

We conclude that for each \(1\le i\le logN\), at most four type-(2b) crossings of the line _L_ may involve copies of _p<sub>i</sub>_, and so the total number of type-(2b) crossings of _L_ is bounded by _O_(log_N_).

To summarize, we have shown that for every ordering \(\sigma\) of the auxiliary columns in \(\mathcal{L},\mathsf{cost}_1(\sigma),\mathsf{cost}_2(\sigma)\le O(N^*logloglogN^*)\), and so \(\mathsf{WB}_\sigma(\hat{X})=O(N^*logloglogN^*)\). Since \(\mathsf{OPT}(\hat{X})=\Omega(N^*loglogN^*)\), we obtain a gap of \(\Omega(loglogN^*/logloglogN^*)\) between \(\mathsf{OPT}(\hat{X})\) and \(\mathsf{WB}(\hat{X})\).

## 4.6 Upper Bound for WB(_X_<sup>∗</sup>)

In this section we show that WB(_X_<sup>∗</sup>)=_O(N_<sup>∗</sup>logloglog_N_<sup>∗</sup>). Recall that instance _X_<sup>∗</sup> is obtained from instance \(\hat{X}\) by replacing every active column _C_ of _X_<sup>∗</sup> with a block B(_C_) of columns, and then placing the points of _C_ on the columns of B(_C_) so that they form a monotone increasing sequence, while preserving their _y_-coordinates. The resulting collection of all blocks B(_C_) partitions the set of all active columns of _X_<sup>∗</sup>. We denote this set of blocks by B<sub>1</sub>_,...,_B_<sub>N</sub>_. The idea is to use Theorem 3.6 in order to bound WB(_X_<sup>∗</sup>).

Consider a set of lines \(\mathcal{L}'\) (with half-integral _x_-coordinates) that partition the bounding box _B_ into strips, where the _i_th strip contains the block B_<sub>i</sub>_ of columns, so \(|\mathcal{L}'|=(N-1)\). We consider a split of instance _X_<sup>∗</sup> by \(\mathcal{L}'\): This gives us a collection of strip instances \(\{X_i^s\}_{1\le i\le N}\) and the compressed instance _X<sup>c</sup>_. Notice that the compressed instance is precisely \(\hat{X}\), and each strip instance \(X_i^s\) is a monotone increasing point set.

Since each strip instance \(X_i^s\) is monotonously increasing, from Observation 4.2 and Claim 2.9, for all _i_, \(\mathsf{WB}(X_i^s)\le O(\mathsf{OPT}(X_i^s))\le O(|X_i^s|)\). From Theorem 3.6, we then get that:

\(\mathsf{WB}(X^*)\le 4\mathsf{WB}(\hat{X})+8\sum_i\mathsf{WB}(X_i^s)+O(|X^*|)\le 4\mathsf{WB}(\hat{X})+O(|X^*|)\le O(N^*logloglogN^*).\)

## 4.7 Separating WB<sup>(2)</sup> and WB

In this section, we extend our \(\Omega(\frac{loglogn}{logloglogn})\)-factor separation between WB and OPT to a separation between WB and the _second Wilber bound_ (denoted by WB<sup>(2)</sup>), which is defined below.<sup>4</sup>

Let _X_ be a set of points that is a semi-permutation, with |_X_|=_m_. Consider any point \(p\in X\). The funnel of _p_, denoted by funnel(_X,p_) is the set of all points \(q\in X\), such that _q,y\<p.y_, and \(\square_{p,q}\) contains no point of _X_\\{_p,q_}. Denote funnel(_X,p_)={_a_<sub>1</sub>_,...,a<sub>r</sub>_}, where the points are indexed in the increasing order of their _y_-coordinates. Let alt(_X,p_) be the number of indices \(1\le i<r\), such that _a<sub>i</sub>_ lies strictly to the left of _p_ and _a_<sub>_i_+1</sub> lies strictly to the right of _p_, or the other way<tbc>

<sup>4</sup>Wilber originally defined this bound based on the tree view. We use an equivalent geometric definition as discussed in \[DHI<sup>+</sup>09, Iac13\].

