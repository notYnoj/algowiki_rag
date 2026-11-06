## 5.2 Algorithm correctness: Proving Lemma 7

Let \(n_j=|S\cap I_j|\) and \(n_{j-1}=|S\cap I_{j-1}|\). Our goal is to show that \(n_j<\rho\cdot n_{j-1}\) for some constant \(\rho\in(0,1)\).

For notational convenience, let \(m_{j-1}=N(\Gamma)\), i.e., _m_<sub>_j_-1</sub> is the number of distances of \(S\cap I_{j-1}\) recorded in \(\Gamma\). Define \(m'_{j-1}\) as the number of distances of \(S\cap I_{j-1}\) not recorded in \(\Gamma\). Then \(n_{j-1}=m_{j-1}+m'_{j-1}\).

By Theorem 3, \(m_{j-1}\ge 0.4n_{j-1}\), and therefore \(m'_{j-1}\le 0.6n_{j-1}\).

Let _S<sub>j</sub>_ denote the set of distances of \(S\cap I_j\) not recorded in \(\Gamma\), and _S_<sub>_j_-1</sub> the set of distances of \(S\cap I_{j-1}\) not recorded in \(\Gamma\). Since \(I_j\subseteq I_{j-1}\), we have \(S_j\subseteq S_{j-1}\), and hence \(|S_j|\le|S_{j-1}|=m'_{j-1}\).

Define _q<sub>j</sub>_ as the number of distances of \(S\cap I_j\) recorded in \(\Gamma\). Then

\(n_j=q_j+|S_j|\le q_j+m'_{j-1}\le q_j+0.6n_{j-1}.\)

Since \(m_{j-1}\le n_{j-1}\), Lemma 7 follows immediately from the following lemma.

**Lemma 8.** _There exists a constant_ \(\rho'\in(0,0.4)\) _such that_ \(q_j\le\rho'\cdot m_{j-1}\).

### Proof of Lemma 8.

We refer to the intervals of I as _basic intervals_. Recall that \(\delta^*\in I_j\), which implies \(\delta_{u_1}<\delta_{u_2}\) and therefore _u_<sub>1</sub>_\<u_<sub>2</sub>.

If _u_<sub>1</sub>=_u_<sub>2</sub>-1, then _I<sub>j</sub>_ consists of the single basic interval \(I'_{u_1+1}\). If _u_<sub>1</sub>=_u_<sub>2</sub>-2, then _I<sub>j</sub>_ consists of the two basic intervals \(I'_{u_1+1}\) and \(I'_{u_2}\). Otherwise, _u_<sub>1</sub>_\<u_<sub>2</sub>-2, and _I<sub>j</sub>_ can be partitioned into three intervals: \(I'_{u_1+1}\), \((\delta_{u_1+1},\delta_{u_2-1}]\), and \(I'_{u_2}\). In the following, we only analyze the third case (i.e., _u_<sub>1</sub>_\<u_<sub>2</sub>-2) since it is the most general case and the other two cases can be analyzed similarly but in a much easier way.

Let \(\hat{I}=(\delta_{u_1+1},\delta_{u_2-1}]\), and define \(\Delta=c_0\cdot n^{4/3}(log^{(i)}n)^4\), which is the term in Theorem 2(3).

**Lemma 9** (Middle interval bound)**.** \(|S\cap\hat{I}|\le 2\Delta\).

_Proof._ Since _u_<sub>1</sub>_\<u_<sub>1</sub>+1_\<u_<sub>2</sub>-1_\<u_<sub>2</sub>, the definition of _u_<sub>1</sub> implies that the quasi-decision algorithm of Theorem 2 reports "unsure" on \(I''_{u_1+1}=[0,\delta_{u_1+1}]\). Therefore, \(|\kappa(I''_{u_1+1})-K|\le\Delta\).

Similarly, the algorithm reports "unsure" on \(I''_{u_2-1}=[0,\delta_{u_2-1}]\), and thus \(|\kappa(I''_{u_2-1})-K|\le\Delta\).

Consequently,

\(|S\cap\hat{I}|=\kappa(I''_{u_2-1})-\kappa(I''_{u_1+1})\le 2\Delta.\)

The lemma thus follows.

Let _I_<sup>∗</sup> be the union of the two boundary basic intervals \(I'_{u_1+1}\) and \(I'_{u_2}\). Let \(S(\Gamma)\) denote the set of distances recorded in \(\Gamma\). Since \(\hat{I}\) and _I_<sup>∗</sup> form a partition of _I<sub>j</sub>_,

\(q_j=|S(\Gamma)\cap\hat{I}|+|S(\Gamma)\cap I'|.\) (8)

The first term is controlled by Lemma 9, while the second term will be bounded using the expander analysis.

By Lemma 9,

\(|S(\Gamma)\cap\hat{I}|\le|S\cap\hat{I}|\le 2\Delta=2c_0\cdot n^{4/3}(log^{(i)}n)^4.\)

Since _m_<sub>_j_-1</sub>_\>c_<sub>1</sub>_n_<sup>4/3</sup>(log<sup>(_i_)</sup>_n_)<sup>4</sup>, we obtain

\(|S(\Gamma)\cap\hat{I}|<\frac{2c_0}{c_1}m_{j-1}.\) (9)

To bound the second term of (8), we use the following lemma.

