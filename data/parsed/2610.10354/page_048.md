## 6.4 Min-Witness Convolution

The following lemma is the key step in the reduction to Min-Witness Convolution.

**Lemma 6.4.** _Suppose Min-Witness Convolution can be solved in O(T(n_)) _time, and let_ \(1/3\le\ell\le 1\) _be a constant. Then in_ \(\widetilde{O}(T(n)\cdot n^\ell)\) _time we can list up to_ \(n^\ell\) _witnesses for each output in Min-Plus Convolution instances_ (_A,B_) _where the universe of all elements in A has size n_<sup>1/3</sup>_, and the universe of all elements in B is_ \(\{0,\perp\}\)_. The algorithm succeeds with high probability._

**Proof.** First, since \(B[j]\in\{0,\perp\}\), we can replace each element in _A_ by its rank in the universe without loss of generality, and hence assume that the universe of elements in _A_ is \[_n_<sup>1/3</sup>\]. Let _C=A∗B_, which can be computed in \(\widetilde{O}(n^{4/3})\) time.

By trying all sampling rates _p_=1,2<sup>-1</sup>,2<sup>-2</sup>_,..._, and only keeping sampled elements in _B_ as their original values while setting all other elements as \(\perp\), then with high probability, there will be a round where the number of witnesses for _C_\[_k_\] is \(\Theta(n^\ell)\) if the number of witnesses for _C_\[_k_\] in the original instance is more than \(n^\ell\). Hence, we only need to handle _C_\[_k_\] with \(O(n^\ell)\) witnesses.

In addition, it suffices to list _n_<sup>1/3</sup> witnesses per _C_\[_k_\] in \(\widetilde{O}(T(n)n^{1/3})\) time: If \(\ell>1/3\), we can randomly partition _B_ to \(\Theta(n^{\ell-1/3})\) random subsequences (by keeping elements not in the corresponding subsequence as \(\perp\)), so that for every _C_\[_k_\], each subsequence contains at most _n_<sup>1/3</sup> witnesses, with high probability.

Before we give the actual reduction, let us first give some intuition. The difficulty of reducing Min-Plus Convolution to Min-Witness Convolution is that, in Min-Witness Convolution, there is no value in the inputs. Hence, we somehow need to encode the weight information in the indices. One potential way is to take monotone subsequences of _A_, and create Boolean sequence \(A'\) where \(A'[i]=1\) if _i_ is in the chosen subsequence and create Boolean sequence \(B'\) where \(B'[i]=1\) if _B_\[_i_\]=0. Because the chosen subsequence is monotone, the Min-Witness Convolution naturally favors candidates (_i,k-i_) where _A_\[_i_\] is smaller, as intended. One potential way to choose monotone subsequences is the following: We take all the 1’s in the first _n_<sup>2/3</sup> entries of _A_, all the 2’s in the second _n_<sup>2/3</sup> entries of _A_, and so on. The downside is that, some _C_\[_k_\] might have many witnesses from the subsequence, while some have few. To overcome this issue, we randomly shuffle the indices and work over the shuffled sequences.

Let _N_ be a prime number from \[2_n,_4_n_\], which can be found deterministically in \(\widetilde{O}(n)\) time. We extend _A_ and _B_ to length _N_, where the extra elements are \(\perp\). Now Min-Plus Convolution _C_ between _A_ and _B_ can be equivalently defined by \(C[k]=min_{i\in\mathbb{F}_N}\{A[i]+B[k-i]\}\).

We will repeat the following \(\widetilde{O}(n^{1/3})\) times. Let _x_∼F_<sub>N</sub>_\\{0} and _y_∼F_<sub>N</sub>_ be uniformly random, and let \(f_{x,y}:\mathbb{F}_N\rightarrow\mathbb{F}_N\) where \(f_{x,y}(i)=i\cdot x+y\). Now define the shuffled sequences _A<sub>x,y</sub>_ and _B<sub>x,y</sub>_, where

\(A_{x,y}[f_{x,y}(i)]=A[i]\text{and}B_{x,y}[f_{x,y}(i)]=B[i]\text{for}i\in\mathbb{F}_N.\)

_A<sub>x,y</sub>_ and _B<sub>x,y</sub>_ are well-defined because _f<sub>x,y</sub>_ is invertible. Consider two subsets \(S_{x,y}=\{i\in\mathbb{F}_N:A_{x,y}[i]=\lfloor i/N^{2/3}\rfloor\}\) and \(T_{x,y}=\{i\in\mathbb{F}_N:B_{x,y}[i]=0\}\). We then create two Boolean sequences \(A'_{x,y}\) and \(B'_{x,y}\), which are the indicator sequences for _S<sub>x,y</sub>_ and _T<sub>x,y</sub>_ respectively.

The following claim shows why it is useful to compute the Min-Witness Convolution between \(A'_{x,y}\) and \(B'_{x,y}\) (even though the indices of them are from F_<sub>N</sub>_ rather than Z, we can still use standard Min-Witness Convolution with some simple postprocessing to compute it).

**Claim 6.5.** _Let I<sub>k</sub> be the set of witnesses for C_\[_k_\] _in the Min-Plus convolution C=A∗B. If there is exactly one witness_ \(i\in I_k\) _such that_ \(f_{x,y}(i)\in S_{x,y}\)_, then_ \(\text{Min-Witness}(A'_{x,y},B'_{x,y})[x\cdot k+2y]=f_{x,y}(i)\).<tbc>

