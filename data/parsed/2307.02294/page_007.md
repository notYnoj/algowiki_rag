## 2 Preliminaries

Let \(A\in\{0,1\}^{n\times m}\) and \(P\in\{0,1\}^{k\times l}\). The _weight_ of _A_, denoted as \(\|A\|_1\), is the number of 1’s in _A_. We say _P_ is _contained_ in _A_, written _P\<A_ if there are row indices \(r_1<\cdots<r_k\) and column indices \(c_1<\cdots<c_l\) such that \(P(i,j)=1\rightarrow A(r_i,c_j)=1\). In other words, you can obtain _P_ from _A_ by deleting rows and columns, and flipping some 1s to 0. The extremal functions are defined as follows.

\(\mathrm{Ex}(P,n,m)=\mathrm{max}\{\|A\|_1|A\in\{0,1\}^{n\times m},P\nmid A\},\)<br>
\(\mathrm{Ex}(P,n)=\mathrm{Ex}(P,n,n).\)

If _P_ is a \(k\times k\) permutation matrix, it is known that both Ex(_P,n_) and \(\mathrm{Ex}(P\otimes\genfrac(){pt}{2}{\bullet}{},n)\) are _O<sub>k</sub>(n_), but we will be interested in the leading constants as well.

**Theorem 2.1** (Marcus and Tardos \[MT04\], Geneson \[Gen09\], Fox \[Fox13\], Cibulka and Kyncl \[CK17\], Geneson \[Gen15\], Geneson and Tian \[GT17\])**.** _Let P be any permutation matrix. Then there exists constants_ \(C_k,C'_k\le 2^{(4+o(1))k}\) _such that_

\(\mathrm{Ex}(P,n,m)\le C_k(n+m),\)<br>
\(\mathrm{Ex}(P\otimes\genfrac(){pt}{2}{\bullet}{},n,m)\le C'_k(n+m).\)

## 3 The Upper Bound

### 3.1 Establishing the General Recurrence

Let _P_ be a \(k\times k\) permutation matrix and \(Q=P\otimes(\cdot)\) be the \(2k\times 3k\) forbidden pattern. Define _Q<sub>a,b</sub>_ to be the \(2k\times(3k-(a+b))\) matrix derived from _Q_ by removing the first _a_ and last _b_ columns. For reasons that will become clear later, we must redefine the _contains_ relation _\<_ differently for the _Q<sub>a,b</sub>_ matrices.

**Definition 3.1.** We will say that _Q<sub>a,b</sub>\<A_ if there are 2_k_ rows \(r_1<\cdots<r_{2k}\) and 3_k-a-b_ columns \(c_1<\cdots<c_{3k-a-b}\) such that

• _Q<sub>a,b</sub>(i,j_)=1 implies _A(r<sub>i</sub>,c<sub>j</sub>_)=1<tbc>

• If \(\forall j\). \(Q_{a,b}(i,j)=0\) then \(\exists j'\). \(A(r_i,j')\neq 0\). In other words, an all-0 row \(Q_{a,b}(i,\cdot)\) cannot match an all-0 row of _A_. (Note that \(j'\) need not be in {_c_<sub>1</sub>_,...,c_<sub>3_k-a-b_</sub>}.)

Let _A_ be an \(n\times mQ_{a,b}\)-free matrix with weight Ex(_Q<sub>a,b</sub>,n,m_). We will classify all 1s in _A_ according to the following taxonomy, and bound the number of 1s in each class directly or inductively.

