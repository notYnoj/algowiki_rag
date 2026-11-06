## 4.4.1 First Instance

In this subsection we construct our first final instance \(\hat{X}\), which is a semi-permutation containing _N_ columns. Intuitively, we create _N_ instances _X_<sup>0</sup>_,X_<sup>1</sup>_,...,X_<sup>_N_-1</sup>, where instance _X<sup>s</sup>_ is an exponentially-spaced BRS instance that is shifted by _s_ units. We then stack these instances on top of one another in this order.

Formally, for all \(0\le j\le N-1\), we define a set R_<sub>j</sub>_ of _n_ consecutive rows with integral coordinates, such that the rows of R<sub>0</sub>,R<sub>1</sub>_,...,_R<sub>_N_-1</sub> appear in this bottom-to-top order. Specifically, set R_<sub>j</sub>_ contains all rows whose _y_-coordinates are in {_jn_+1_,jn_+2_,...,(j_+1)_n_}.

For every integer \(0\le s\le N-1\), we define a set of points _X<sup>s</sup>_, which is a cyclic shift of instance \(\text{ES-BRS}(\ell,\mathcal{R}_s)\) by _s_ units. Recall that \(|X^s|=2^\ell=n\) and that the points in _X<sup>s</sup>_ appear on the rows in R_<sub>s</sub>_ and a set C_<sub>s</sub>_ of columns, whose _x_-coordinates are in \(\{\left(2^j+s\right)modN:1\le j\le n\}\). We then let our final instance be \(\hat{X}=\bigcup_{s=0}^{N-1}X^s\). From now on, we denote by \(N^*=|\hat{X}|\). Recall that \(|N^*|=N\cdot n=NlogN\).

Observe that the number of active columns in \(\hat{X}\) is _N_. Since the instance is symmetric and contains _N_<sup>∗</sup>=_N_log_N_ points, every column contains exactly log_N_ points. Each row contains exactly one point, so \(\hat{X}\) is a semi-permutation. (See Figure 5 for an illustration).

Lastly, we need the following bound on the value of the optimal solution of instance \(\hat{X}\).

**Observation 4.5** \(\text{OPT}(\hat{X})=\Omega(N^*loglogN^*)\)

**Proof:** From Claims 4.3 and 4.4, for each \(0\le s\le N-1\), each sub-instance _X<sup>s</sup>_ has \(\text{OPT}(X^s)\ge\Omega(nlogn)=\Omega(logNloglogN)\). Therefore, \(\text{OPT}(\hat{X})\ge\sum_{s=0}^{N-1}\text{OPT}(X^s)=\Omega(NlogNloglogN)=\Omega(N^*loglogN^*)\) (we have used the fact that _N_<sup>∗</sup>=_N_log_N_). \(\square\)

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

Figure 5: A small example of _X_<sup>0</sup>, _X_<sup>1</sup>, and _X_<sup>2</sup> (shown in different colors) placed from bottom to top, when the parameter \(\ell=2\). In this case, each _X<sup>s</sup>_ contains 4 points, and there are _N_=16 copies of shifted sub-instances (but we show only 3). The dotted columns are the active columns of _X_<sup>2</sup>.

