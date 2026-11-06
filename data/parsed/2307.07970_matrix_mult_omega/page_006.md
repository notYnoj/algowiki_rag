Observe that

\(\sum_{i=1}^q(x_0y_iz_i+x_iy_0z_i+x_iy_iz_0)\equiv\langle 1,1,q\rangle+\langle q,1,1\rangle+\langle 1,q,1\rangle,\)

so CW_<sub>q</sub>_ is the sum of six matrix multiplication tensors where the other three are copies of \(\langle 1,1,1\rangle\). Next, we describe the leveled partitions of CW_<sub>q</sub>_ and \(\mathrm{CW}_q^{\otimes 2^\ell}\) that are crucial to our analysis. For simplicity, we denote \(T^{(\ell)}:=\mathrm{CW}_q^{\otimes 2^{\ell-1}}\).

For _T_<sup>(1)</sup>=CW_<sub>q</sub>_, its variable sets are partitioned into three parts

\(X^{(1)}=X_0^{(1)}\sqcup X_1^{(1)}\sqcup X_2^{(1)}=\{x_0\}\sqcup\{x_1,\dots,x_q\}\sqcup\{x_{q+1}\},\)<br>
\(Y^{(1)}=Y_0^{(1)}\sqcup Y_1^{(1)}\sqcup Y_2^{(1)}=\{y_0\}\sqcup\{y_1,\dots,y_q\}\sqcup\{y_{q+1}\},\)<br>
\(Z^{(1)}=Z_0^{(1)}\sqcup Z_1^{(1)}\sqcup Z_2^{(1)}=\{z_0\}\sqcup\{z_1,\dots,z_q\}\sqcup\{z_{q+1}\}.\)

Notice that under this partition, a constituent tensor \(T_{i,j,k}^{(1)}\) is nonzero if and only if _i+j+k_=2.

For \(T^{(\ell)}=\mathrm{CW}_q^{\otimes 2^{\ell-1}}\) with variable sets \(X^{(\ell)},Y^{(\ell)},Z^{(\ell)}\), the above partition on _T_<sup>(1)</sup> directly induces a partition on the variable sets \(X^{(\ell)},Y^{(\ell)},Z^{(\ell)}\) where each part of the partition is indexed by a {0,1,2}- sequence of length \(2^{\ell-1}\). Specifically, this gives the partition

\(X^{(\ell)}=\sqcup_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^\ell-1})\in\{0,1,2\}^{2^{\ell-1}}}X_{\hat{i}_1}^{(1)}\otimes X_{\hat{i}_2}^{(1)}\otimes\cdots\otimes X_{\hat{i}_{2^\ell-1}}^{(1)}\)

for _X_-variables and analogous partitions for _Y_ - and _Z_-variables.

One can use the laser method on these partitions. However, this would not yield an improved bound on \(\omega\) from what one would get just by analyzing _T_<sup>(1)</sup>. The reason behind the improvement obtained by analyzing higher powers of CW_<sub>q</sub>_ comes from the fact that we can consider the following coarsening of the above partition where the parts corresponding to sequences with the same sum are "merged" into a single part. More specifically, we have<tbc>

\(X^{(\ell)}=\sqcup_{i=0}^{2^\ell} X_i^{(\ell)},\text{where}X_i^{(\ell)}:=\sqcup_{(\hat{i}_1,\hat{i}_2,\dots,\hat{i}_{2^\ell-1})\in\{0,1,2\}^{2^{\ell-1}}\sum_t\hat{i}_t=i}X_{\hat{i}_1}^{(1)}\otimes X_{\hat{i}_2}^{(1)}\otimes\cdots\otimes X_{\hat{i}_{2^\ell-1}}^{(1)}.\)

<tbc>We refer to this specific partition of \(T^{(\ell)}\) as the _level-_\(\ell\) _partition_. Note that we can also view this partition as obtained from coarsening the level-(\(\ell-1\)) partition, i.e.,

\(X_i^{(\ell)}=\sqcup_{0\le i^\prime\le i0\le i^\prime,i-i^\prime\le 2^\ell} X_{i^\prime}^{(\ell-1)}\otimes X_{i-i^\prime}^{(\ell-1)}.\)

We can partition the variable sets \(Y^{(\ell)}\) and \(Z^{(\ell)}\) similarly. Then we use \(T_{i,j,k}^{(\ell)}\) to denote the subtensor of \(T^{(\ell)}\) restricted to the variable subsets \(X_i^{(\ell)},Y_j^{(\ell)},Z_k^{(\ell)}\) and note that \(T_{i,j,k}^{(\ell)}\) is nonzero if and only if \(i+j+k=2^\ell\). We call \(T_{i,j,k}^{(\ell)}\) a level-\(\ell\) _constituent tensor_, \(X_i^{(\ell)},Y_j^{(\ell)},Z_k^{(\ell)}\) level-\(\ell\) variable blocks, and we omit the superscript \((\ell)\) when \(\ell\) is clear from context.

