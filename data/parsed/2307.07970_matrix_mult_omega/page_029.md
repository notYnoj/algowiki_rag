and

\(S_{*,*,k}^{(K)}:=\{t\in[n]|K_t=k\}.\)

If clear from the context, we will drop the superscript (_I,J,K_) or (_K_).

Recall that in T<sub>hash</sub>, every level-\(\ell\) block _X<sub>I</sub>_ is in a unique block triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_. For every level-1 block \(X_\hat{I}\in X_I\), we will zero out \(X_\hat{I}\) if \(\text{split}(\hat{I},S_{i,j,k})\neq\beta_{X,i,j,k}\) for any _i,j,k_ (recall the definition of \(\text{split}(\hat{I},S_{i,j,k})\) in Definition 3.5). Similarly, every level-\(\ell\) block _Y<sub>J</sub>_ is in a unique block triple, and we zero out every \(Y_\hat{j}\in Y_J\) where \(\text{split}(\hat{J},S_{i,j,k})\neq\beta_{Y,i,j,k}\) for any _i,j,k_.

We can not perform the same zeroing out for _Z_-variables, because in T<sub>hash</sub> each level-\(\ell Z\)-block is not in a unique block triple and _S<sub>i,j,k</sub>_ is not well-defined just given the _Z_-block. Instead, for every level-1 block \(Z_\hat{K}\in Z_K\), we zero out \(Z_\hat{K}\) if \(\text{split}(\hat{K},S_{*,*,k})\neq\overline{\beta_{Z,*,*,k}}\) for any _k_, where

\(\overline{\beta_{Z,*,*,k}}=\frac{1}{\sum_{i+j=2^\ell-k}\alpha(i,j,k)}\sum_{i+j=2^\ell-k}\alpha(i,j,k)\cdot\beta_{Z,i,j,k}\)

is the average complete split distribution for constituent tensors whose third coordinate is _k_.

We call the tensor after the previous zeroing-outs T<sub>comp</sub>.

Next, we are ready to define the notion of compatibility. The notion is adapted from \[DWZ23\], which is a crucial ingredient in their analysis (and ours).

**Definition 5.8** (Compatibility)**.** For some _I,J,K_, a level-1 block \(Z_\hat{K}\in Z_K\) is compatible with a level-\(\ell\) triple _X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>_ if

1. For every \((i,j,k)\in\mathbb{Z}_{\ge 0}^3\) with \(i+j+k=2^\ell,i=0\) or _j_=0, \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\).<tbc>

2. For every index \(k\in\{0,1,\dots,2^\ell\}\), \(\text{split}(\hat{K},S_{*,*,k})=\overline{\beta_{Z,*,*,k}}\).

**Claim 5.9.** _In_ T<sub>comp</sub>_, for every level-1 block triple_ \(X_\hat{I}Y_\hat{j}Z_\hat{K}\) _and the level-_\(\ell\) _block triple X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub> that contains it,_ \(Z_\hat{K}\) _is compatible with X<sub>I</sub>Y<sub>J</sub>Z<sub>K</sub>._

_Proof._ First of all, Item 2 is clearly satisfied, because we zeroed out every \(\hat{K}\) with \(\text{split}(\hat{K},S_{*,*,k})\neq\overline{\beta_{Z,*,*,k}}\) for any _k_. Next, we show that Item 1 is also satisfied.

Recall that we zeroed out all \(X_\hat{I}\) where \(\text{split}(\hat{I},S_{i,j,k})\neq\beta_{X,i,j,k}\) for any _i,j,k_. Let \((i,j,k)\in\mathbb{Z}_{\ge 0}^3\) where \(i+j+k=2^\ell\) and _j_=0. As \(X_\hat{I}Y_\hat{j}Z_\hat{K}\) remains in T<sub>comp</sub>, \(\text{split}(\hat{I},S_{i,j,k})=\beta_{X,i,j,k}\). Because _j_=0, _J<sub>t</sub>_=0 for every \(t\in S_{i,j,k}\), which implies that \(\left(\hat{J}_{(t-1)\cdot 2^{\ell-1}+1},\hat{J}_{(t-1)\cdot 2^{\ell-1}+2},\dots,\hat{J}_{t\cdot 2^{\ell-1}}\right)=\overline{0}\). As \(\hat{I}_\hat{t}+\hat{J}_\hat{t}+\hat{K}_\hat{t}=2\) for every \(\hat{t}\), we have that

\(\left(\hat{K}_{(t-1)\cdot 2^{\ell-1}+1},\hat{K}_{(t-1)\cdot 2^{\ell-1}+2},\dots,\hat{K}_{t\cdot 2^{\ell-1}}\right)=\overline{2}-\left(\hat{I}_{(t-1)\cdot 2^{\ell-1}+1},\hat{I}_{(t-1)\cdot 2^{\ell-1}+2},\dots,\hat{I}_{t\cdot 2^{\ell-1}}\right)\)

for every \(t\in S_{i,j,k}\). Thus, for every \(L\in\{0,1,2\}^{2^{\ell-1}}\), the proportion of _L_ appearing in \(\left(\hat{I}_{(t-1)\cdot 2^{\ell-1}+1},\hat{I}_{(t-1)\cdot 2^{\ell-1}+2},\dots,\hat{I}_{t\cdot 2^{\ell-1}}\right)\) over \(t\in S_{i,j,k}\) is exactly the proportion of \(\overline{2}-L\) appearing in \(\left(\hat{K}_{(t-1)\cdot 2^{\ell-1}+1},\hat{K}_{(t-1)\cdot 2^{\ell-1}+2},\dots,\hat{K}_{t\cdot 2^{\ell-1}}\right)\). In other words, \(\text{split}(\hat{K},S_{i,j,k})(L)=\text{split}(\hat{I},S_{i,j,k})(\overline{2}-L)=\beta_{X,i,j,k}(\overline{2}-L)\). By Remark 5.2, this implies that \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\).

We can show that \(\text{split}(\hat{K},S_{i,j,k})=\beta_{Z,i,j,k}\) with _i_=0 similarly.

