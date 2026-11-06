<tbc>The consensus total distance is a lower bound for the total distance between any _l_-mer _M_ and the _l_-mers in _T_ because, regardless of _M_, the distance contributed by column _i_ to the total distance is at least _k-m<sub>i</sub>_. The consensus total distance for a set of two _l_-mers _A_ and _B_ will be denoted by _Cd(A,B_). Also notice that _Cd(A,B_)=_Hd(A,B_). We can easily prove the following lemma.

**Lemma 1.** _Let T be a set of l-mers and k_=|_T|. Let d_<sub>1</sub>_,d_<sub>2</sub>_,...d<sub>k</sub> be non- negative integers. There exists a l-mer M such that_ \(Hd(M,T_i)\le d_i,\forall i\)_, only if_ \(Cd(T)\le\Sigma_{i=1}^kd_i\).

**Theorem 1.** _Let T be a set of 3 l-mers and d_<sub>1</sub>_,d_<sub>2</sub>_,d_<sub>3</sub> _be non-negative integers. There exists a l-mer M such that_ \(Hd(M,T_i)\le d_i,\forall i,1\le i\le 3\) _if and only if the following conditions hold:_

**i)** \(Cd(T_i,T_j)\le d_i+d_j,\forall i,j,1\le i<j\le 3\)

**ii)** \(Cd(T)\le d_1+d_2+d_3\)

_Proof._ The "only if" part follows from lemma 1. For the "if" part we show how to construct a common neighbor _M_ provided that the conditions hold.

We say that a column _k_ where _T_<sub>1</sub>\[_k_\]=_T_<sub>2</sub>\[_k_\]=_T_<sub>3</sub>\[_k_\] is of type _N_<sub>0</sub>. If \(T_1[k]\neq T_2[k]=T_3[k]\) then the column is of type _N_<sub>1</sub>. If \(T_1[k]=T_3[k]\neq T_2[k]\) the column is of type _N_<sub>2</sub> and if \(T_1[k]=T_2[k]\neq T_3[k]\) then the column is of type _N_<sub>3</sub>. If all three characters in the column are distinct, the column is of type _N_<sub>4</sub>. Let \(n_i,\forall i,0\le i\le 4\) be the number of columns of type _N<sub>i</sub>_. Consider two cases:

Case 1) There exists \(i,1\le i\le 3\) for which \(n_i\ge d_i\). We construct _M_ as illustrated in the left panel of figure 4. Pick _d<sub>i</sub>_ columns of type _n<sub>i</sub>_. For each chosen column _k_ set _M_\[_k_\]=_T<sub>j</sub>_\[_k_\] where \(j\neq i\). For all other columns set _M_\[_k_\]=_T<sub>i</sub>_\[_k_\]. Therefore _Cd(T<sub>i</sub>,M_)=_d<sub>i</sub>_. For \(j\neq i\) we know that \(Cd(T_i,T_j)\le d_i+d_j\) from our assumptions. We also know that \(Cd(T_i,M)+Cd(M,T_j)\le Cd(T_i,T_j)\) from the triangle inequality. It follows that \(Cd(M,T_j)\le d_j\). Since _Cd(M,T<sub>j</sub>_)=_Hd(M,T<sub>j</sub>_) it means that _M_ is indeed a common neighbor of the three _l_-mers.

Case 2) For all \(i,1\le i\le 3\) we have _n<sub>i</sub>\<d<sub>i</sub>_. We construct _M_ as shown in the right panel of figure 4. For columns _k_ of type _N_<sub>0</sub>_,N_<sub>2</sub> and _N_<sub>3</sub> we set _M_\[_k_\]=_T_<sub>1</sub>\[_k_\]. For columns of type _N_<sub>1</sub> we set _M_\[_k_\]=_T_<sub>2</sub>\[_k_\]. For any \(i,1\le i\le 3\) the following applies. If \(n_i+n_4\le d_i\) then the Hamming distance between _M_ and _T<sub>i</sub>_ is less than _d<sub>i</sub>_ regardless of what characters we choose for _M_ in the columns of type _N_<sub>4</sub>. On the other hand, if _n<sub>i</sub>+n_<sub>4</sub>_\>d<sub>i</sub>_ then _M_ and _T<sub>i</sub>_ have to match in at least _n<sub>i</sub>+n_<sub>4</sub>-_d<sub>i</sub>_ columns of type _N_<sub>4</sub>. Thus, we pick _max_(0_,n<sub>i</sub>+n_<sub>4</sub>-_d<sub>i</sub>_) columns of type _N_<sub>4</sub> and for each such column _k_ we set _M_\[_k_\]=_T<sub>i</sub>_\[_k_\]. Now we prove that we actually have enough columns to make the above choices, in other words \(\Sigma_{i=1}^3max(0,n_i+n_4-d_i)\le n_4\). This is equivalent to the following conditions being true:

**a)** For any \(i,1\le i\le 3\) we want \(n_i+n_4-d_i\le n_4\). This is true because _n<sub>i</sub>\<d<sub>i</sub>_.

**b)** For any \(i,j,1\le i<j\le 3\) we want \((n_i+n_4-d_i)+(n_j+n_4-d_j)\le n_4\). This can be rewritten as \(n_i+n_j+n_4\le d_i+d_j\). The left hand side is _Hd(T<sub>i</sub>,T<sub>j</sub>_) which we know is less or equal to _d<sub>i</sub>+d<sub>j</sub>_.

**c)** We want \(\Sigma_{i=1}^3n_i+n_4-d_i\le n_4\). This can be rewritten as \(n_1+n_2+n_3+2n_4\le d_1+d_2+d_3\). The left hand side is _Cd(T_) which we know is less than _d_<sub>1</sub>+_d_<sub>2</sub>+_d_<sub>3</sub>.

