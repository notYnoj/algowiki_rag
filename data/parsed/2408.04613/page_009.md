\(\blacktriangleright\) **Fact 4.1** (\[23, Lemma 4.4\])**.** _There exists an algorithm that, given the condensed representation of a matrix A of size_ \(p\times q\)_, in time_ \(\mathcal{O}(p+q+\delta(A)log(1+\delta(A)))\) _builds a_ core-based matrix oracle data structure CMO(_A_) _that provides_ \(\mathcal{O}(log(2+\delta(A)))\)_-time random access to the entries of A._

**Proof Sketch.** By Observation 3.1 applied for _a=c_=0, it suffices to answer orthogonal range sum queries on top of core(_A_). According to \[49, Theorem 3\], it can be done in \(\mathcal{O}(\delta(A)log(1+\delta(A)))\) preprocessing time and \(\mathcal{O}(log(2+\delta(A)))\) query time. \(\blacktriangleleft\)

\(\blacktriangleright\) **Definition 4.2.** _Let A be a_ \(p\times q\) _matrix. For every_ \(i\in[0..p-1)\)_, denote_ \(core_{i,,}(A)=\{(i,j,A_{i,j}^\square)|j\in[0..q-1),A_{i,j}^\square\neq 0\}\) _and_ \(\delta_{i,,}(A)=|core_{i,,}(A)|\)_. Analogously, for every_ \(j\in[0..q-1)\)_, denote_ \(core_{,j}(A)=\{(i,j,A_{i,j}^\square)|i\in[0..p-1),A_{i,j}^\square\neq 0\}\) _and_ \(\delta_{,j}(A)=|core_{,j}(A)|\).

\(\blacktriangleright\) **Observation 4.3.** \(\delta(A)=\sum_{i\in[0..p-1)}\delta_{i,,}(A)=\sum_{j\in[0..q-1)}\delta_{,j}(A)\).

We now design another matrix oracle as an alternative to CMO(_A_) for the situation in which one wants to query an entry of _A_ that is adjacent to some other already known entry.

\(\blacktriangleright\) **Lemma 4.4.** _There is an algorithm that, given the condensed representation of a_ \(p\times q\) _matrix A, in time_ \(\mathcal{O}(p+q+\delta(A))\) _builds a_ local core oracle data structure lco(_A_) _with the following interface._

**_Boundary access:_** _given indices_ \(i\in[0..p)\) _and_ \(j\in[0..q)\) _such that i_=0 _or j_=0_, in time_ O(1) _returns A<sub>i,j</sub>._

**_Vertically adjacent recomputation:_** _given indices_ \(i\in[0..p-1)\) _and_ \(j\in[0..q)\)_, in time_ \(\mathcal{O}(\delta_{i,,}(A)+1)\) _returns A_<sub>_i_+1_,j_</sub>-_A<sub>i,j</sub>._

**_Horizontally adjacent recomputation:_** _given indices_ \(i\in[0..p)\) _and_ \(j\in[0..q-1)\)_, in time_ \(\mathcal{O}(\delta_{,j}(A)+1)\) _returns A_<sub>_i,j_+1</sub>-_A<sub>i,j</sub>._

**Proof.** The local core oracle data structure of _A_ stores all the values of the topmost row and the leftmost column of _A_, as well as two collections of lists: core<sub>_i,,_</sub>(_A_) for all \(i\in[0..p-1)\) and core<sub>_,j_</sub>(_A_) for all \(j\in[0..q-1)\). The values of the topmost row and the leftmost column of _A_ are already given. The lists core<sub>_i,_</sub>(_A_) and core<sub>_,j_</sub>(_A_) can be computed in \(\mathcal{O}(p+q+\delta(A))\) time from core(_A_). Hence, we can build lco(_A_) in time \(\mathcal{O}(p+q+\delta(A))\).

Boundary access can be implemented trivially. We now show how to implement the vertically adjacent recomputation. Suppose that we are given \(i\in[0..p-1)\) and \(j\in[0..q)\). Due to Observation 3.1, we have _A<sub>i,j</sub>+A_<sub>_i_+1,0</sub>=_A_<sub>_i_+1_,j_</sub>+_A_<sub>_i,_0</sub>+\(\delta^\Sigma(A[i..i+1][0..j])\). Note that the values _A_<sub>_i,_0</sub> and _A_<sub>_i_+1,0</sub> can be computed in constant time using boundary access queries, and \(\delta^\Sigma(A[i..i+1][0..j])\) can be computed from core<sub>_i,_</sub>(_A_) in time \(\mathcal{O}(\delta_{i,,}(A)+1)\). Hence, _A_<sub>_i_+1_,j_</sub>-_A<sub>i,j</sub>_ can be computed in time \(\mathcal{O}(\delta_{i,,}(A)+1)\).

The horizontally adjacent recomputation is implemented analogously so that _A_<sub>_i,j_+1</sub>-_A<sub>i,j</sub>_ can be computed in time \(\mathcal{O}(\delta_{,j}(A)+1)\). \(\blacktriangleleft\)

Note that vertically and horizontally adjacent recomputations allow computing the neighbors of any given entry _A<sub>i,j</sub>_.

\(\blacktriangleright\) **Lemma 4.5.** _Given the condensed representation of a_ \(p\times q\) _matrix A, the condensed representation of any contiguous submatrix_ \(A'\) _of A can be computed in time_ \(\mathcal{O}(p+q+\delta(A))\).

**Proof.** Say, \(A'=A[i..i'][j..j']\). Note that \(core(A')\) can be obtained in time \(\mathcal{O}(\delta(A))\) by filtering out all elements of core(_A_) that lie outside of \([i..i')\times[j..j')\). It remains to obtain the topmost row and the leftmost column of \(A'\). In time \(\mathcal{O}(p+q+\delta(A))\) we build lco(_A_) of Lemma 4.4. By starting from _A_<sub>_i,_0</sub> and repeatedly applying the horizontally adjacent recomputation, we can compute _A_\[_i..i_\]\[0_..q_\] (and thus \(A[i..i][j..j']\)) in time \(\mathcal{O}(\sum_{j\in[0..q)}(\delta_{,j}(A)+1))=\mathcal{O}(q+\delta(A))\). The leftmost column of \(A'\) can be computed in time \(\mathcal{O}(p+\delta(A))\) analogously. \(\blacktriangleleft\)

