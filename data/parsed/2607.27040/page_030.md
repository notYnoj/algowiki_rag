the buffer memories in step 3 requires \(C'(n_{i,<})\) comparisons and \(M'(n_{i,<})\) moves. Lastly, partitioning \(B_\ge\) to remove equal elements requires \(n_{i,\ge}\) comparisons and 2_n_<sub>_i,_=</sub>+1 moves.

By straightforward induction, we bound \(n_i\le(3/4)^in\). With _I_ as the number of iterations, we have

\(\sum_{i=1}^In_i\le n\sum_{i=1}^I\left(3/4\right)^i\le n/(1-3/4)=4n\) (D.1)

As every iteration expands _A<sub>S</sub>_ by _n_<sub>_i,\<<_</sub>+_n_<sub>_i,_=</sub>+1 until its size reaches \(|\mathcal{A}'|\) and the algorithm terminates, then

\(\sum_{i=1}^In_{i,<}\le\left(\sum_{i=1}^In_{i,<}+n_{i,=}+1\right)=|\mathcal{A}'|\le n\) (D.2)

Summing over all iterations, the number of comparisons _C(n_) to sort the input array _A_ is

\(C(n)=O(n)+\left(\sum_{i=1}^IO(n_i)+n_i+C'\left(n_{i,<}\right)+n_{i,\ge}\right)\)<br> \(=O(n)+\left(\sum_{i=1}^IC'\left(n_{i,<}\right)+O(n_i)\right)\)

Applying (D.1), we obtain

\(C(n)=O(n)+\sum_{i=1}^IC'(n_{i,<})\)

Let _F(m_) denote all terms in \(C'(m)\) that grow super-linearly. From Theorems 2.6 and 2.7, _F(m_)=_m_lg_m_ or _F(m_)=_m_lg_m+m_lg<sup>(_t_)</sup>_m_. Separating \(C'(n_{i,<})\) gives:

\(C(n)=O(n)+\sum_{i=1}^I\left(F(n_{i,<})+O(n_{i,<})\right)\)

For both variations of _F(m_), the expression _F(m)/m_ is non-decreasing when _F(m_) is well defined. Therefore, _F(m_) is superadditive. Using (D.2) and the superadditivity of _F(m_):

\(C(n)\le F(n)+O(n)=C'(n)+O(n).\)

By a parallel derivation for the moves _M(n_) (note that _F(m_)=0 as \(M'(m)\) grows linearly with _m_)

\(M(n)=O(n)+\left(\sum_{i=1}^I\varepsilon n_i+2n_{i,<}+1+M'\left(n_{i,<}\right)+2n_{i,=}+1\right)\)<br> \(\le M'(n)+O(n).\)

(Where \(\varepsilon>0\) denotes an arbitrarily small, but fixed, real constant.)

\(\blacktriangleright\) **Lemma D.1.** _The input array_ A _can be sorted in-place using no more than_ \(C'(n)+O(n)\) _comparisons and_ \(M'(n)+O(n)\) _moves given an algorithm that sorts a sequence of m elements with additional memory using_ \(C'(m)\) _comparisons and_ \(M'(m)\) _moves._

