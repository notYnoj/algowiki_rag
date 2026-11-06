Substituting this identity proves the claimed concavity inequality.

## 4.3 Shifted tripling

We next compare an input length _h_ with 3_h+S_, where _S_ is the sum of the other input degrees. The resulting factor of three provides a lower bound on a long increment of the profile; concavity will then give a lower bound on a single increment. The construction extends \[Ope26a, Lemma 4.2\]. We specify its coordinate sectors by their offsets and lengths, using the same convention as Theorem 3.1.

**Lemma 4.9** (shifted tripling)**.** _Let_ \(n\ge 3\) _be an integer, let_ \(\phi\in\Phi_n\)_, and let_ \(P_\phi\) _be its profile. For all positive integers a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>_,h, put_ \(S=\sum_{j=1}^{n-2}(a_j-1)\)_. Then_

\(P_\phi(a_1,\dots,a_{n-2},3h+S)\ge 3P_\phi(a_1,\dots,a_{n-2},h).\)

_Proof._ Set _B_=3_h+S_. Index a supported entry of C_<sub>n</sub>(a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>_,B_) by its shared input indices _i_<sub>1</sub>_,...,i_<sub>_n_-2</sub>, its last-input index _y_, and its output index _z_. The defining conditions are<tbc>

\(0\le i_j<a_j(1\le j\le n-2),0\le y<B,z=y+\sum_{j=1}^{n-2}i_j.\)

<tbc>In particular, \(0\le\sum_{j=1}^{n-2}i_j\le S\) and \(0\le z<B+S\). Introduce three last-input lengths _b_<sub>0</sub>=_b_<sub>2</sub>=_h_ and _b_<sub>1</sub>=_h+S_, and three output lengths _c_<sub>0</sub>=_c_<sub>2</sub>=_h+S_ and _c_<sub>1</sub>=_h_. For \(r\in\{0,1,2\}\), put

\(\beta_r=\sum_{t=0}^{r-1}b_t,\gamma_r=\sum_{t=0}^{r-1}c_t,Y_r=\{\beta_r+i:0\le i<b_r\},Z_r=\{\gamma_r+j:0\le j<c_r\}.\)

The sums for _r_=0 are empty. These are disjoint partitions of \[_B_\]<sub>0</sub> and \[_B+S_\]<sub>0</sub>, since \(\sum_{r=0}^2b_r=B\) and \(\sum_{r=0}^2c_r=B+S\). Their offsets satisfy \(\beta_0=\gamma_0=0\), \(\beta_1=h\), \(\gamma_1=h+S\), and \(\beta_2=\gamma_2=2h+S\).

Give a last-input coordinate weight +1 when it belongs to _Y_<sub>1</sub>, and weight zero otherwise. Give an output coordinate weight -1 when it belongs to _Z_<sub>1</sub>, and weight zero otherwise. All shared coordinates have weight zero. If \(y\in Y_0\), then _y\<h_ and \(z\le h-1+S\), so \(z\in Z_0\). If \(y\in Y_2\), then \(2h+S\le y<B\) and \(2h+S\le z<B+S\), so \(z\in Z_2\). Consequently, \(z\in Z_1\) requires \(y\in Y_1\).

It follows that every supported entry has nonnegative total weight. The entries with \(y\in Y_r\) and \(z\in Z_r\), for some \(r\in\{0,1,2\}\), have weight zero. Every other supported entry has \(y\in Y_1\) and \(z\in Z_0\cup Z_2\), and hence has weight +1. Applying the weight degeneration retains exactly the three matched blocks in the sectors \(Y_r\times Z_r\).

Let _C_=C_<sub>n</sub>(a_<sub>1</sub>_,...,a_<sub>_n_-2</sub>_,h_). In sector _r_=0, write \(y=y'\) and \(z=z'\). In sector _r_=2, write \(y=2h+S+y'\) and \(z=2h+S+z'\). In either case, the support condition becomes

\(0\le y'<h,0\le z'<h+S,z'=y'+\sum_{j=1}^{n-2}i_j.\)

Every choice of the shared input indices and \(y'\in[h]_0\) gives exactly one allowed \(z'\). Thus, after these translations of the last two coordinates, each outer block equals _C_ in the original shared coordinates.

