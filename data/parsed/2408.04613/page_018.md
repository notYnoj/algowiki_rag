\(\delta(A^*)+\delta(B^*))\)_, builds a_ \(p\times q\) _Monge matrix A and a_ \(q\times r\) _Monge matrix B such that_ \(p\le\delta(A^*)+1\), \(q\le\delta(A^*)+\delta(B^*)+1\), \(r\le\delta(B^*)+1\), \(\delta(A)=\delta(A^*)\)_, and_ \(\delta(B)=\delta(B^*)\)_. The_ `Decompress` _algorithm, given the condensed representations of A_<sup>∗</sup>_, B_<sup>∗</sup>_, and_ \(A\otimes B\)_, where_ (_A,B_)=`Compress`(_A_<sup>∗</sup>_,B_<sup>∗</sup>)_, computes the condensed representation of_ \(A^*\otimes B^*\) _in time_ \(\mathcal{O}(p^*+r^*+\delta(A^*)+\delta(B^*))\).

**Proof.** We first describe how to convert _A_<sup>∗</sup> into a \(p\times q^*\) Monge matrix \(A'\) such that \(p\le\delta(A^*)+1\) and \(\delta(A')=\delta(A^*)\).

Call the _i_-th row of _A_<sup>∗</sup> for \(i\in(0..p^*)\) _redundant_ if \(\delta_{i-1,.}(A^*)=0\). To obtain \(A'\), we remove all redundant rows of _A_<sup>∗</sup>. The matrix \(A'\) is Monge by Observation 3.3.

We now show how to compute the condensed representation of \(A'\) in \(\mathcal{O}(p^*+q^*+\delta(A^*))\) time. To find redundant rows, we iterate over core(_A_<sup>∗</sup>) and mark all rows that contain any core elements. The topmost row of \(A'\) is the same as the topmost row of _A_<sup>∗</sup>. To get the leftmost column of \(A'\), we filter out all elements of the leftmost column of _A_<sup>∗</sup> that lie in the redundant rows. It remains to compute the core of \(A'\). Consider a function _f_ that maps the rows of \(A'\) to the corresponding rows of _A_<sup>∗</sup>. For any \(i\in[0..p-1)\) and \(j\in[0..q-1)\), due to Observation 3.1, we have

\(A'_{i,j}^{\square}=A'_{i,j+1}+A'_{i+1,j}-A'_{i,j}-A'_{i+1,j+1}\)<br>
\(=A_{f(i),j+1}^*+A_{f(i+1),j}^*-A_{f(i),j}^*-A_{f(i+1),j+1}^*\)<br>
\(=\delta^\Sigma(A^*[f(i)..f(i+1)][j..j+1])\)<br>
\(=A_{f(i),j}^{*\square}+A_{f(i)+1,j}^{*\square}+\cdots+A_{f(i+1)-1,j}^{*\square}\)<br>
\(=A_{f(i+1)-1,j}^{*\square},\)

where the last equality holds as \(A_{f(i),j}^{*\square}=A_{f(i)+1,j}^{*\square}=\cdots=A_{f(i+1)-2,j}^{*\square}=0\) because _f(i_) and _f(i_+1) are two consecutive non-redundant rows of _A_<sup>∗</sup>. Therefore, the set \(core(A')=\{(i,j,A'_{i,j}^{\square})|i\in[0..p-1),j\in[0..q-1),A'_{i,j}^{\square}\neq 0\}=\{(f^{-1}(i+1)-1,j,A_{i,j}^{*\square})|(i,j,A_{i,j}^{*\square})\in core(A^*)\}\) is of size \(\delta(A')=\delta(A^*)\) and can be computed in time \(\mathcal{O}(\delta(A^*)+1)\). Furthermore, for every \(i\in[0..p-1)\), we have \(\delta_{i,.}(A')\neq 0\) by the definition of \(A'\), and thus \(p\le\delta(A')+1=\delta(A^*)+1\).

Analogously (up to a transposition), in \(\mathcal{O}(q^*+r^*+\delta(B^*))\) time we convert _B_<sup>∗</sup> into a \(q^*\times r\) Monge matrix \(B'\) such that \(r\le\delta(B^*)+1\) and \(\delta(B')=\delta(B^*)\).

The last step of the compression algorithm is to convert \(A'\) and \(B'\) into Monge matrices _A_ and _B_ of sizes \(p\times q\) and \(q\times r\), respectively, such that \(q\le\delta(A')+\delta(B')+1\), \(A\otimes B=A'\otimes B'\), \(\delta(A)=\delta(A')\), and \(\delta(B)=\delta(B')\). Consider an arbitrary segment \([j_L..j_R)\subseteq[0..q^*)\) such that \(\delta(A'[0..p)[j_L..j_R))=\delta(B'[j_L..j_R)[0..r))=0\). Pick \(j_\mathrm{opt}:=argmin\{A'_{0,j}+B'_{j,0}|j\in[j_L..j_R)\}\). For all \(i\in[0..p)\), \(j\in[j_L..j_R)\), and \(r\in[0..r)\), we have

\(A'_{i,j}+B'_{j,k}=(A'_{0,j}+A'_{i,j_\mathrm{opt}}-A'_{0,j_\mathrm{opt}})+(B'_{j,0}+B'_{j_\mathrm{opt},k}-B'_{j_\mathrm{opt},0})\)<br>
\(=A'_{i,j_\mathrm{opt}}+B'_{j_\mathrm{opt},k}+(A'_{0,j}+B'_{j,0})-(A'_{0,j_\mathrm{opt}}+B'_{j_\mathrm{opt},0})\)<br>
\(\ge A'_{i,j_\mathrm{opt}}+B'_{j_\mathrm{opt},k}\)

by Observation 3.1 and the definition of _j_<sub>opt</sub>. Therefore, indices \(j\in[j_L..j_R)\backslash\{j_\mathrm{opt}\}\) are not needed for the computation of any entry \((A'\otimes B')_{i,k}\). We can thus split \[0_..q_<sup>∗</sup>) into \(q\le\delta(A')+\delta(B')+1\) such disjoint segments \[_j<sub>L</sub>..j<sub>R</sub>_) and pick a single "optimal" index _j_<sub>opt</sub> in each such segment. To obtain the resulting matrices _A_ and _B_, we drop all columns of \(A'\) and rows of \(B'\) that correspond to indices that are not picked. The condensed representations

