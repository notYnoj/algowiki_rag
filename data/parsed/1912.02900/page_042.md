## Instance \(\hat{X}\):

Next, we construct an instance \(\hat{X}\), by combining the instances \(X^{s,s^\prime}\) for \(0\le s,s'<N\). In order to do so, let \(\hat{\mathcal{C}}\) be a set of _N_<sup>2</sup> columns, with integral _x_-coordinates 1_,...,N_<sup>2</sup>. We partition \(\hat{\mathcal{C}}\) into subsets C<sub>1</sub>,C<sub>2</sub>_,...,_C_<sub>N</sub>_, each of which contains _N_ consecutive columns, they appear in this left-to-right order. We call each such set C_<sub>i</sub>_ a _super-column_. We denote by \(S_i^V\) the smallest vertical strip containing all columns of C_<sub>i</sub>_.

Similarly, we let \(\hat{\mathcal{R}}\) be a set of _N_<sup>2</sup> rows, with integral _y_-coordinates 1_,...,N_<sup>2</sup>. We partition \(\hat{\mathcal{R}}\) into subsets R<sub>1</sub>_,...,_R_<sub>N</sub>_, each of which contains _N_ consecutive rows, such that R<sub>1</sub>_,...,_R_<sub>N</sub>_ appear in this bottom-to-top order. We call each such set R_<sub>i</sub>_ a _super-row_. We denote by \(S_i^H\) the smallest horizontal strip containing all rows of R_<sub>i</sub>_. For all \(1\le i,j\le N\), we let _B(i,j_) be the intersection of the horizontal strip \(S_i^H\) and the vertical strip \(S_i^V\). We plant the instance _X_<sup>(_i_-1),(_j_-1)</sup> into the box _B(i,j_). This completes the construction of instance \(\hat{X}\). Let \(N^*=|\hat{X}|=N^2logN\) (recall that each instance \(X^{s,s^\prime}\) contains log_N_ points.)

Observe that, for each vertical strip \(S_i^V\), all instances planted into \(S_i^V\) have the same vertical shift - (_i_-1); the horizontal shift \(s'\) of each instance increases from 0 to _N_-1 as we traverse \(S_i^V\) from bottom to top. In particular, the instance planted into \(S_1^V\) is precisely the instance \(\hat{X}\) from Section 4.3 (if we ignore inactive rows). For each _i\>_1, the instance planted into \(S_i^V\) is very similar to the instance \(\hat{X}\) from Section 4.3, except that each of its corresponding sub-instances is shifted vertically by exactly (_i_-1) rows.

Similarly, for each horizontal strip \(S_j^H\), all instances planted into \(S_j^H\) have the same horizontal shift - (_j_-1); the vertical shift \(s'\) of each instance increases from 0 to _N_-1 as we traverse \(S_j^H\) from left to right.

Since, for every instance \(X^{s,s^\prime}\), \(\mathsf{OPT}(X^{s,s^\prime})=\Omega(logNloglogN)\), we obtain the following bound.

**Observation 5.4** \(\mathsf{OPT}(\hat{X})=\Omega(N^2logNloglogN)=\Omega(N^*loglogN^*)\).

Since instance \(\hat{X}\) is symmetric, and every point lies on one of the _N_<sup>2</sup> rows of \(\hat{\mathcal{R}}\) and on one of the _N_<sup>2</sup> rows of \(\hat{\mathcal{C}}\), we obtain the following.

**Observation 5.5** _Every row in_ \(\hat{\mathcal{R}}\) _contains exactly_ log_N points of_ \(\hat{X}\)_. Similarly, every column of_ \(\hat{\mathcal{C}}\) _contains exactly_ log_N points of_ \(\hat{X}\).

## Final instance:

Lastly, in order to turn \(\hat{X}\) into a permutation _X_<sup>∗</sup>, we perform a similar transformation to that in Section 4.3: for every column \(C\in\mathcal{C}\), we replace _C_ with a collection B(_C_) of log_N_ consecutive columns, and we place all points that lie on _C_ on the columns of B(_C_), so that they form an increasing sequence, while preserving their _y_-coordinates. We replace every row \(R\in\mathcal{R}\) by a collection B(_R_) of log_N_ rows similarly. The resulting final instance _X_<sup>∗</sup> is now guaranteed to be a permutation, and it contains _N_<sup>∗</sup>=_N_<sup>2</sup>log_N_ points. Using the same reasoning as in Section 4.3, it is easy to verify that \(\mathsf{OPT}(X^*)\ge\mathsf{OPT}(\hat{X})\ge\Omega(N^*loglogN^*)\). In the remainder of this section, we will show that cGB(_X_<sup>∗</sup>)=_O(N_<sup>∗</sup>logloglog_N_<sup>∗</sup>).

Abusing the notation, for all \(1\le i\le N^2\), we denote by \(S_i^V\) the vertical strip obtained by taking the union of all blocks B(_C_) of columns, where _C_ belonged to the original strip \(S_i^V\). We define the horizontal strips \(S_i^H\) similarly. Note that, from Lemma 5.2, it is enough to prove that WB(_X_<sup>∗</sup>)=_O(N_<sup>∗</sup>logloglog_N_<sup>∗</sup>) and that \(\mathsf{WB}'(X^*)=O(N^*logloglogN^*)\). We do so in the following two subsections.

