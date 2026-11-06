Note that this wrapper is just adding special characters that force alignment of the bits in _h<sub>b,i</sub>_ by making the only way to match the ∗_<sub>j</sub>_ characters also force an alignment of the _h<sub>b,i</sub>_\[_j_\] characters. Note that \(|T_{b,i}|=2\cdot 2^k=\ell\). Note that the offset score of _T_<sub>_b_<sub>1</sub>,1</sub>_,T_<sub>_b_<sub>2</sub>,2</sub>_,...,T<sub>b<sub>k</sub>,k</sub>_</sub> with all deltas zero is 2_<sup>k</sup>_ if _b<sub>i</sub>_=1 for all _i_ and is 1+2_<sup>k</sup>_.

Let _S_<sub>1_,i_</sub> be the representation of a 1 in string _X<sub>i</sub>_. Let _S_<sub>0_,i_</sub> be the representation of a 0 in string _X<sub>i</sub>_. We will set

\(S_{1,i}=@^\ell T_{1,i}\text{and}S_{0,i}=@^\ell T_{0,i}.\)

Note that this wrapper adds these @ characters which further enforce alignment. Note that the offset score of _S_<sub>_b_<sub>1</sub>,1</sub>_,S_<sub>_b_<sub>2</sub>,2</sub>_,...,S<sub>b<sub>k</sub>,k</sub>_</sub> with all deltas zero is \(2^k+\ell\) if _b<sub>i</sub>_=1 for all _i_ and is \(1+2^k+\ell\) otherwise.

## Correctness

Now, we want to claim that one of the best alignments of _X_<sub>1</sub>_,...,X<sub>k</sub>_ will have deltas that are multiples of \(|S_{b,i}|=2\ell\). That is, the best alignment will align these representations of single bits. Consider if \(\Delta_imod2\ell=f\). If \(f\neq 0mod2\ell\) then the ∗_<sub>j</sub>_ symbols can’t be aligned with those in _X<sub>k</sub>_. Additionally, at most \(\ell-j\) of the @ characters will be matched. Giving a maximum match of: \(\ell-j+2^k\) (even if every 0, 1, and % characters were matched, which is of course unrealistic, we can’t match 0 characters as none appear in the _X<sub>k</sub>_ string). This is worse than the worst alignments when \(\Delta_i\)s are multiples of \(2\ell\).

So, the best alignment has all \(\Delta_i\) as multiples of \(2\ell\). Thus, the alignment of _X_<sub>1</sub>_,...,X<sub>k</sub>_ is an alignment of \(|\hat{X}_i|S_{b,i}\) gadgets. Each gadget promises to return \(2^k+\ell\) if _b<sub>i</sub>_=1 for all _i_ and is \(1+2^k+\ell\) otherwise.

Now, note that given our construction of \(\hat{X}_1,\dots,\hat{X}_k\), if we choose a set of deltas \(\Delta_i=2\ell\delta_i\) we are effectively picking _k_-1 vectors and comparing them because of how we structured \(\hat{X}_k\). So, if there are an orthogonal _k_-1 vectors which are orthogonal in our list representation (which corresponds to _a(k_-1) vectors in the original OV instance) then we get a score of: \(|\hat{X}_1|(1+2^k+\ell)\). Otherwise, we get a score at least one less than that. This shows our reduction will give the correct answer.

## Time

So with _k_ strings of length _n<sup>a</sup>_ and a constant sized alphabet (\(|\Sigma|=O(2^k)\)) we can solve (_a(k_+1))-OV. Notably _N=n_<sup>_a+o_(1)</sup>. So an algorithm running in faster than _N_<sup>_k_-1-_o_(1)</sup> time will violate the (_a(k_+1))-OV hypothesis. This fulfills the statement in the theorem.

## Compression

Now we will argue that these strings are compress-able with SLP. We will mostly be using the same structure as \[ABBK17\]. First we can build variables in our SLP for all of our base characters with _O_(2_<sup>k</sup>_) variables. Next we can build \(@^\ell\) with \(lg(\ell)=O(k)\) variables. Next we can build all _S<sub>b,i</sub>_ for all _i_ and _b_ with at most _O(k_2_<sup>k</sup>_) variables. Next, we want to build our longer strings.

Now we will use the recursive structure of **String**<sub>**I**_<sub>a</sub>_</sub>(_L_). Let<tbc>

\(\mathbf{String}_{\mathbf{I}_\ell}(L)^{[i]}=\circ_{j_1\in[1,n].\dots,j_\ell\in[1,n]}L[j_1][i]\cdot L[j_2][i]\cdots\cdot L[j_\ell][i].\)

<tbc>Note that<tbc>

\(\mathbf{String}_{\mathbf{I}_a}(L)=\circ_{i=1}^d\left(\mathbf{String}_{\mathbf{I}_a}(L)^{[i]}\right).\)

<tbc>We are just pulling out the part related to the _i<sup>th</sup>_ bit of every vector. Now note that

\(\mathbf{String}_{\mathbf{I}_a}(L)^{[i]}=\circ_{j\in[1,n]}\left\{\begin{array}{ c c }
\mathbf{String}_{\mathbf{I}_{a-1}}(L)^{[i]} & \text{if}L[j][i]=1 \\
0^{(n^{a-1})} & \text{if}L[j][i]=0
\end{array}\right..\)

Where 0<sup>(_n_<sup>_a_-1</sup>)</sup> is _n_<sup>_a_-1</sup> zeros in a row.

Note that we can make SLP variables for all 0<sup>(_n<sup>i</sup>_)</sup> strings for \(i\in[1,a]\) with _a_lg(_n<sup>a</sup>_)=_a_<sup>2</sup>lg(_n_) variables. Next note that given an SLP variable for **String**<sub>**I**<sub>_a_-1</sub></sub>(_L_)<sup>\[_i_\]</sup> we can add _n_ variables and form **String**<sub>**I**<sub>_a_</sub></sub>(_L_)<sup>\[_i_\]</sup>. It takes _n_ variables to form **String**<sub>**I**<sub>1</sub></sub>(_L_)<sup>\[_i_\]</sup>. So, with an SLP with _an+a_<sup>2</sup>lg(_n_) variables we can represent **String**<sub>**I**<sub>_a_</sub></sub>(_L_)<sup>\[_i_\]</sup>. So, with an SLP with _d(an+a_<sup>2</sup>lg(_n_)) variables we can represent **String**<sub>**I**<sub>_a_</sub></sub>(_L_). To replace all zeros with _S_<sub>0_,i_</sub> and all ones with _S_<sub>1_,i_</sub> requires an additional _O_(2_<sup>k</sup>_) variables.

So, we can compress all of our strings with _O(d(n_+lg(_n_))) variables. Given our restrictions on _d_ we can write this as _n_<sup>1+_o_(1)</sup>. So our compression has length _m=n_<sup>1+_o_(1)</sup>. Our input to our k-SD instance is _N=n_<sup>_a+o_(1)</sup>. So _N_<sup>1_/a+o_(1)</sup>=_n_<sup>1+_ao_(1)</sup>=_n_<sup>1+_o_(1)</sup>. Fulfilling the statement of the theorem.

