The proof is a reduction from INDEX<sub>_N<sup>d</sup>_</sub>. Alice will associate one constraint with each vector in \[_N_\]_<sup>d</sup>_ and stream that constraint exactly when the corresponding bit is 1. Bob must determine whether Alice streamed one chosen constraint. To do this, he will consider 2_<sup>d</sup>_ assignments and add or subtract their values. The next lemma shows that these signs can be chosen so that the selected constraint has a nonzero total contribution. Later, we will arrange that every other constraint has total contribution zero.

More precisely, each of the _d_ relevant coordinates will take either a basepoint 0 or one fixed value _a<sub>i</sub>_. The assignments are indexed by the sets \(S\subseteq[d]\) of coordinates that receive _a<sub>i</sub>_. The expression in the next lemma is simply the value on these 2_<sup>d</sup>_ choices, added with a plus sign when _d_-|_S_| is even and a minus sign when it is odd.

**Lemma 7.4.** _Let_ \(R\subseteq D^k\) _and suppose_ \(\mathrm{deg}_D(\mathbf{1}_R)=d\ge 1\)_. Fix any basepoint_ \(0\in D\)_. Then there are distinct coordinates_ \(t_1,\dots,t_d\in[k]\) _and values_ \(a_1,\dots,a_d\in D\backslash\{0\}\) _such that, after fixing every coordinate outside_ {_t_<sub>1</sub>_,...,t<sub>d</sub>_} _to_ 0_, the resulting function_ \(h:D^d\rightarrow\{0,1\}\) _satisfies_

\(c:=\sum_{S\subseteq[d]}(-1)^{d-|S|}h(y^S)\neq 0,\)

_where_ \(y_i^S=a_i\) _for_ \(i\in S\) _and_ \(y_i^S=0\) _otherwise._

_Proof._ For \(j\in[k]\) and \(a\in D\backslash\{0\}\), define _Z<sub>j,a</sub>(x_)=**1**\[_x<sub>j</sub>=a_\]. As in the upper bound, the definition of degree gives an expansion

\(\mathbf{1}_R(x)=\sum_{T\subseteq[k]}\sum_{b\in(D\backslash\{0\})^T}c_{T,b}\prod_{j\in T}Z_{j,b_j}(x).\)

Since the degree is _d_, there is a set _T_={_t_<sub>1</sub>_,...,t<sub>d</sub>_} and a choice of values \(a_1,\dots,a_d\in D\backslash\{0\}\) for which the coefficient _c<sub>T,a</sub>_ is nonzero. Fix every coordinate outside _T_ to 0. Any term involving one of those coordinates is now zero because all the indicators in the expansion correspond to nonzero values.

Consider the signed sum in the statement one term of the expansion at a time. If a term does not use coordinate _t<sub>i</sub>_, then its value is unchanged when _i_ is added to or removed from _S_. The sets _S_ and \(S\triangleup\{i\}\) have opposite signs, so their contributions cancel. Therefore, only terms that use all _d_ coordinates in _T_ can remain. There are no terms of degree larger than _d_, and among the degree-_d_ terms on _T_, only the term requiring the values _a_<sub>1</sub>_,...,a<sub>d</sub>_ is nonzero on the chosen 2_<sup>d</sup>_ tuples. Its total contribution is its coefficient _c<sub>T,a</sub>_. Hence the number _c_ in the statement equals _c<sub>T,a</sub>_ and is nonzero.

We now use these 2_<sup>d</sup>_ choices in the reduction. The queried constraint will see all of them and will therefore contribute _c_. Any other constraint will be unaffected by at least one of the choices. Pairing the two assignments that differ only in that choice will make its contribution cancel.

_Proof of Theorem 7.3._ Without loss of generality, we may assume that the coordinates _t_<sub>1</sub>_,...,t<sub>d</sub>_ from Lemma 7.4 are the first _d_ coordinates. This is because if they are not, we can permute the coordinates of _R_ and apply the same permutation to every scope without changing the streaming problem. Fix the values _a_<sub>1</sub>_,...,a<sub>d</sub>_ and the nonzero integer _c_ given by that lemma. If _k_=1 and |_D|\>_1, a unary relation always has a non-bijective endomorphism. For a nonempty relation, use a constant map to a value in the relation. For the empty relation, use any non-bijective map. Thus a unary core relation has a one-element domain and degree zero. It follows that \(d\ge 1\) implies \(k\ge 2\), as required in Lemma 4.6.

