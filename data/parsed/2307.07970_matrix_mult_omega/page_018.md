<tbc>We refer to this above coarsened partition of \(T^{(\ell)}\) as the _level-_\(\ell\) _partition_. Note that we can also view this partition as obtained from coarsening the level-(\(\ell-1\)) partition, i.e.,

\(X_i^{(\ell)}=\sqcup_{0\le i^\prime\le i0\le i^\prime,i-i^\prime\le 2^\ell} X_{i^\prime}^{(\ell-1)}\otimes X_{i-i^\prime}^{(\ell-1)}.\)

We can partition the variable sets \(Y^{(\ell)}\) and \(Z^{(\ell)}\) similarly.

Under the level-\(\ell\) partition, we use \(T_{i,j,k}^{(\ell)}\) to denote the subtensor \(T^{(\ell)}|_{X_i^{(\ell)},Y_j^{(\ell)},Z_k^{(\ell)}}\) and note that \(T_{i,j,k}^{(\ell)}\) is nonzero if and only if \(i+j+k=2^\ell\). So we have

\(T^{(\ell)}=\mathrm{CW}_q^{\otimes 2^{\ell-1}}=\sum_{i,j,k\ge 0i+j+k=2^\ell} T_{i,j,k}^{(\ell)}.\)

We call each \(T_{i,j,k}^{(\ell)}\) a _level-_\(\ell\) _constituent tensor_, \(X_i^{(\ell)},Y_j^{(\ell)},Z_k^{(\ell)}\) level-\(\ell\) variable blocks, and we omit the superscript \((\ell)\) when \(\ell\) is clear from context.

## 3.8 Leveled Partition for Large Tensor Powers of CW_<sub>q</sub>_

In the laser method, we consider a large tensor power of CW_<sub>q</sub>_ in the form \((T^{(\ell)})^{\otimes n}=(\mathrm{CW}_q)^{\otimes n\cdot 2^{\ell-1}}\). We set \(N:=n\cdot 2^{\ell-1}\) and note that the leveled partition of \(T^{(\ell)}\) induces a partition on \((T^\ell)^{\otimes n}\). We recall some basic terminology and notations with respect to the leveled-partition of \((T^\ell)^{\otimes n}\).

### Level-1 partition of \((\mathrm{CW}_q)^{\otimes N}\).

In level-1, we view \((\mathrm{CW}_q)^{\otimes N}\) as the tensor \((T^{(1)})^{\otimes N}\) and consider the partition induced by the level-1 partition on _T_<sup>(1)</sup>. Each level-1 _X_-variable block \(X_\hat{I}\) is indexed by a sequence \(\hat{I}=(\hat{I}_1,\dots,\hat{I}_N)\) of length _N_ in {0,1,2}_<sup>N</sup>_. The variable block _X<sub>I</sub>_ is defined as<tbc>

\(X_\hat{I}:=X_{\hat{I}_1}^{(1)}\otimes\cdots\otimes X_{\hat{I}_N}^{(1)},\)

<tbc>where \(X_{I_t}^{(1)}\) for \(t\in[N]\) is the level-1 partition of _T_<sup>(1)</sup>. We call \(X_\hat{I}\) a _level-_1 _variable block_ and \(\hat{I}\) its _level-_1 _index sequence_. The level-1 _Y_ - and _Z_-variable blocks \(Y_\hat{j}\) and \(Z_\hat{K}\) are defined similarly for level-1 index sequences \(\hat{J},\hat{K}\in\{0,1,2\}^N\). Then notice that \(X_\hat{I},Y_\hat{j},Z_\hat{K}\) form a nonzero subtensor of \((T^{(1)})^{\otimes N}\) if \(\hat{I}_t+\hat{J}_t+\hat{K}_t=2\) for all \(t\in[N]\). So we can write \((T^{(1)})^{\otimes N}\) as a sum of subtensors

\((T^{(1)})^{\otimes N}=\sum_{\hat{I},\hat{J},\hat{K}\in\{0,1,2\}^N\hat{I}_t+\hat{J}_t+\hat{K}_t=2\forall t\in[N]}(T^{(1)})^{\otimes N}\big|_{X_\hat{I},Y_\hat{j},Z_\hat{K}}.\)

For convenience, we use \(X_\hat{I}Y_\hat{j}Z_\hat{K}\) to denote the subtensor \((T^{(1)})^{\otimes N}|_{X_\hat{I},Y_\hat{j},Z_\hat{K}}\) and we call \(X_\hat{I}Y_\hat{j}Z_\hat{K}\) a _level-_1 _triple_.

### Level-\(\ell\) partition of \((\mathrm{CW}_q)^{\otimes N}\).

In level-\(\ell\), we view \((\mathrm{CW}_q)^{\otimes N}\) as the tensor \((T^{(\ell)})^{\otimes n}\) where \(n=N/2^{\ell-1}\) and consider the partition induced by the level-\(\ell\) partition on \(T^{(\ell)}\). Each level-1 _X_-variable block _X<sub>I</sub>_ is indexed by a sequence \(I\in\{0,1,\dots,2^\ell\}^n\) of length _n_. The variable block _X<sub>I</sub>_ is defined as<tbc>

\(X_I:=X_{I_1}^{(\ell)}\otimes\cdots\otimes X_{I_n}^{(\ell)}\)

