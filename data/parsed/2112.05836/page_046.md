Now, we will make _N_<sup>_k_-2</sup> calls to 2-SD. Each call takes time \((|\Sigma|+1)N\mathrm{lg}(N(|\Sigma|+1))\) time. Thus, we take time \(O(|\Sigma|N^{k-1}\mathrm{lg}(N|\Sigma|))\).

This gives a total time of \(O(|\Sigma|N^{k-1}\mathrm{lg}(N|\Sigma|))\).

## 8.2 The Lower Bound

We will now show that we can produce _k_ strings of length _N=n<sup>a</sup>_ that compress to length _an_ such that an algorithm that runs faster than _n_<sup>(_k_-1)_a-o_(1)</sup>=_N_<sup>_k_-1-_o_(1)</sup> violates SETH and the (_k_-1)_a_-OV hypothesis. This will give a tight lower bound. Additionally, it says that strings that compress from length _N_ to length \(N^\epsilon\) do not have faster algorithms than those that don’t compress.

To do this we will use the interleaving representation defined previously. Recall that we defined the interleaving version as:<tbc>

\(\mathbf{String}_\mathbf{I}_\ell(L)=\circlearrowleft_{i=1}^d\left(\circlearrowleft_{j_1\in[1,n]\dots,j_\ell\in[1,n]}L[j_1][i]\cdot L[j_2][i]\cdot\cdots\cdot L[j_\ell][i]\right).\)

<tbc>Recall that this is equivalent to

\(\mathbf{String}_\mathbf{I}_\ell(L)=\circlearrowleft_{i\in[1,d]}\circlearrowleft_{j\in[1,n^\ell]}\mathbf{List}(L)[j][i].\)

Finally, recall that in \(\mathbf{String}_\mathbf{I}_\ell(L)\) the vector \(\vec{v}=\mathbf{List}(L)[i]\) appears as bits _i,i+n<sup>k</sup>,...,i_+(_d_-1)_n<sup>k</sup>_.

**Theorem 8.3.** _Let a and k be constants. Let N be the input string length for k-SD._

_If the_ (_a(k_-1))-_OV hypothesis holds then k-SD requires N_<sup>_k_-1-_o_(1)</sup> _time even when the strings compress down to length m=N_<sup>1_/a+o_(1)</sup> _with an alphabet of size O_(1).

_Proof._ We take as input a (_a(k_-1))-OV instance with (_a(k_-1)) lists of _n_ vectors each. Each vector has length _d_ and _d=n_<sup>_o_(1)</sup>. Recall that the (_a(k_-1))-OV hypothesis states that (_a(k_-1))-OV requires _n_<sup>_a(k_-1)-_o_(1)</sup> time.

We will use four characters 0,1,%,@,∗<sub>1</sub>_,...,_∗<sub>2_k_</sub>. The zero and ones will be used to signify the zeros and ones of the OV instance. The @ and ∗_<sub>i</sub>_ symbols will be used to force alignment in a way that is easy to prove. We note that one can almost certainly prove the same result with a smaller alphabet. However, allowing this larger alphabet makes our proof much easier.

Given a (_a(k_-1))-OV instance split the lists of vectors up into _k_-1 groups each with _a_ lists of vectors. Call these groups of _a_ lists _L_<sub>1</sub>_,...,L_<sub>_k_-1</sub>. We are going to form strings _X_<sub>1</sub>_,...,X_<sub>_k_-1</sub> by slight alterations to **String**<sub>**I**<sub>_a_</sub></sub>(_L_<sub>1</sub>)_,...,_**String**<sub>**I**<sub>_a_</sub></sub>(_L_<sub>1</sub>). The final string _X<sub>k</sub>_ will remain constant regardless of the input instance of OV.

Let \(\hat{X}_i=\mathbf{String}_\mathbf{I}_a(L_i)\) then \(i\in[1,k-1]\). Let \(\hat{X}_k\) be a string of all zeros except in positions 0_,n<sup>a</sup>,...,(d_-1)_n<sup>a</sup>_. Like the other strings we give a total length of _dn<sup>a</sup>_ for \(\hat{X}_k\). Note that by choosing an offset for each string from \(\hat{X}_k\) we are effectively choosing one vector from each list _L_<sub>1</sub>_,...,L_<sub>_k_-1</sub> to align with the ones in \(\hat{X}_k\). We want to design ways to right out the zeros and ones that simultaneously: (1) force alignment and (2) have the same value if there is at least one zero and a lower match value if they are all ones. If we can do this, then the best alignment will be picking the "most orthogonal" set of _k_-1 vectors, which will let us find if any vectors are fully orthogonal.

We will now design _h_<sub>1_,i_</sub> and _h_<sub>0_,i_</sub> which will have the property that the offset score of _h_<sub>_b_<sub>1</sub>,1</sub>_,h_<sub>_b_<sub>2</sub>,2</sub>_,...,h_<sub>_b<sub>k</sub>,k_</sub> with all deltas zero is 0 if all _b<sub>i</sub>_=1 and is 1 otherwise. We will consider all strings in {0,1}_<sup>k</sup>_. Let _H_ be all 2_<sup>k</sup>_ of those strings in sorted order, with the all ones string last. Let _H_\[_j_\] be the _j<sup>th</sup>_ string in _H_ note that _H_\[2_<sup>k</sup>_\] is the all ones string (we will one index this list). Now

\(h_{b,i}[j]=\left\{\begin{array}{ c c }
1 & \text{if}H[j][i]=b\text{and}j\neq 2^k \\
0 & \text{if}i<k\text{and the above does not apply}. \\
\% & \text{else}
\end{array}\right.\)

So we get strings of length 2_<sup>k</sup>_. Note that _h<sub>b,i</sub>_ for \(i\in[1,k-1]\) uses only 0,1 symbols, however, _h<sub>b,k</sub>_ uses only 0,% symbols. If we are aligning _h_<sub>_b_<sub>1</sub>,1</sub>_,h_<sub>_b_<sub>2</sub>,2</sub>_,...,h<sub>b<sub>k</sub>,k</sub>_ we are simply counting locations where they are all 1. This only occurs in the location that is associated with the string in \(Hb_1b_2\cdots b_k\), if it is not the all ones string. So, the offset score of _h_<sub>_b_<sub>1</sub>,1</sub>_,h_<sub>_b_<sub>2</sub>,2</sub>_,...,h<sub>b<sub>k</sub>,k</sub>_ with all deltas zero is 0 if _b<sub>i</sub>_=1 for all _i_ and is 1 otherwise, as desired.

We will now design _T_<sub>1_,i_</sub> and _T_<sub>0_,i_</sub> that will force alignment. Let \(\circlearrowleft\) represent concatenation:<tbc>

\(T_{b,i}=\circlearrowleft_{j=0}^{2^k}*_jh_{b,i}[j].\)

