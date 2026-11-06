Observe that

\(\sum_{i=1}^qx_0y_iz_i+\sum_{i=1}^qx_iy_0z_i+\sum_{i=1}^qx_iy_iz_0\equiv\langle 1,1,q\rangle+\langle q,1,1\rangle+\langle 1,q,1\rangle,\)

so CW_<sub>q</sub>_ is the sum of six matrix multiplication tensors where the other three are copies of \(\langle 1,1,1\rangle\). It is known from Coppersmith and Winograd \[CW90\] that \(\widetilde{R}(\mathrm{CW}_q)\le q+2\).

## 3.7 Base Leveled Partition of CW_<sub>q</sub>_

We will consider the \(2^{\ell-1}\)-th tensor power of CW_<sub>q</sub>_ for \(\ell\ge 1\). For convenience, we use the notation \(T^{(\ell)}:=\mathrm{CW}_q^{\otimes 2^{\ell-1}}\). There is a natural partitioning of the variables of CW_<sub>q</sub>_ introduced in \[CW90\] and consequently used in all following works including \[Vas12, AV21, LG14, DWZ23\]. We now describe the leveled partition of \(T^{(\ell)}\).

### Level-1 Partition.

For _T_<sup>(1)</sup>=CW_<sub>q</sub>_, its variable sets _X_<sup>(1)</sup>_,Y_<sup>(1)</sup>_,Z_<sup>(1)</sup> are partitioned into three parts

\(X^{(1)}=X_0^{(1)}\sqcup X_1^{(1)}\sqcup X_2^{(1)}=\{x_0\}\sqcup\{x_1,\dots,x_q\}\sqcup\{x_{q+1}\},\)<br>
\(Y^{(1)}=Y_0^{(1)}\sqcup Y_1^{(1)}\sqcup Y_2^{(1)}=\{y_0\}\sqcup\{y_1,\dots,y_q\}\sqcup\{y_{q+1}\},\)<br>
\(Z^{(1)}=Z_0^{(1)}\sqcup Z_1^{(1)}\sqcup Z_2^{(1)}=\{z_0\}\sqcup\{z_1,\dots,z_q\}\sqcup\{z_{q+1}\}.\)

We use \(T_{i,j,k}^{(1)}\) to denote the subtensor _T_<sup>(1)</sup>|_X<sub>i</sub>,Y<sub>j</sub>,Z<sub>k</sub>_ and we call \(T_{i,j,k}^{(1)}\) a _level-_1 _constituent tensor_. Then notice that under the above partition, the constituent tensor \(T_{i,j,k}^{(1)}\) is nonzero if and only if _i+j+k_=2. In particular, we can write CW_<sub>q</sub>_ as a sum of constituent tensors as follows

\(T^{(1)}=\mathrm{CW}_q=\sum_{i,j,k\ge 0i+j+k=2}T_{i,j,k}^{(1)}.\)

### Level-\(\ell\) Partition.

For \(T^{(\ell)}=\mathrm{CW}_q^{\otimes 2^{\ell-1}}\) with variable sets \(X^{(\ell)},Y^{(\ell)},Z^{(\ell)}\), the above level-1 partition on _T_<sup>(1)</sup> directly induces a partition on the variable sets \(X^{(\ell)},Y^{(\ell)},Z^{(\ell)}\) where each part of the partition is indexed by a {0,1,2}-sequence of length \(2^{\ell-1}\). Specifically, this gives the partition

\(X^{(\ell)}=\sqcup_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^\ell-1})\in\{0,1,2\}^{2^\ell-1}}X_{\hat{i}_1}^{(1)}\otimes X_{\hat{i}_2}^{(1)}\otimes\cdots\otimes X_{\hat{i}_{2^\ell-1}}^{(1)}\)

for _X_-variables and analogous partitions for _Y_ - and _Z_-variables.

In order to obtain an improvement by analyzing higher tensor powers of CW_<sub>q</sub>_, we need to consider the following coarsening of the induced partition where the parts corresponding to sequences with the same sum are "merged" into a single part. More specifically, we have

\(X^{(\ell)}=\sqcup_{i=0}^{2^\ell} X_i^{(\ell)},\text{where}X_i^{(\ell)}:=\sqcup_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^\ell-1})\in\{0,1,2\}^{2^\ell-1}}X_{\hat{i}_1}^{(1)}\otimes X_{\hat{i}_2}^{(1)}\otimes\cdots\otimes X_{\hat{i}_{2^\ell-1}}^{(1)}.\)

