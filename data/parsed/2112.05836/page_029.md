then<tbc>

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),SAG_y(Y))=D,\)

<tbc>otherwise<tbc>

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),AG_y(Y))\le D-1.\)

<tbc>Then, because of the @ symbols if there is a perfect alignment \(\Lambda\) in which there are exactly _mk_-tuples such that<tbc>

\(\mathrm{LCS}(X_1[i_{j,1}],\dots,X_{k-1}[i_{j,k-1}],X_y[i_{j,k}])=z+1,\)

<tbc>then<tbc>

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D,\)

<tbc>if all perfect alignments have less than _mk_-tuples then

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D-1.\)

Proving our desired result.

Now, we will also want to use this gadget for regular alignment. In this case we will care about distinguishing between a single _k_-tuple with high value versus no strings having high value.

**Theorem 6.12.** _We are given as input k lists of strings X_<sub>1</sub>_,...,X_<sub>_k_-1</sub>_,Y. Where_ |_X<sub>i</sub>_|=_n,_ |_Y_|=_m, and m\<n. Furthermore all strings_ \(S\in X_i\) _and_ \(S'\in Y\) _have length_ \(|S|=|S'|=\ell\).

_Additionally, given any set of k strings_ \(S_i\in X_i\) _and_ \(S_y\in Y\) _the LCS distance is either z or z_+1 _for some constant z._

_Finally define_ \(\hat{X}_i\) _as a list that is simply two copies of X<sub>i</sub>. That is_ \(\hat{X}_i[j]=\hat{X}_i[n+j]=X_i[j]\).

_In the first case there is exactly one k-tuple where_<tbc>

\(\mathrm{LCS}(X_1[i_{1,1}],\dots,X_{k-1}[i_{1,k-1}],X_y[i_{1,k}])=z+1,\)

<tbc>_and there exists a perfect alignment that can align this k-tuple. That is_ \(n-i_{1,j}\ge m-i_{1,k}\) _and_ \(i_{1,j}\le i_{1,k}\)_. In this first case we want:_<tbc>

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D.\)

<tbc>_In the second case there are zero k-tuples that have an LCS of z_+1 _then we want:_

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D-1.\)

_These strings use an additional alphabet of size O(k). The total length of strings is_ \(O(\ell n)\)_. The value of is_ \(D=2\ell(2m+(k-1)n)+zm+1\).

_Additionally, let c be the size of an SLP that gives a single variable for all_ (_k_-1)_n+m strings X<sub>i</sub>_\[_j_\] _and Y_\[_j_\]_. Then there is a SLP representation of all the strings AG_<sub>1</sub>(_X_<sub>1</sub>)_,...,AG_<sub>_k_-1</sub>(_X_<sub>_k_-1</sub>)_,AG<sub>y</sub>(Y_) _of size_ \(O(c+\mathrm{lg}(\ell)k+\mathrm{lg}(n)+kn+m)\).

_Proof._ As in the above theorem: in the _SAG_ gadgets note that if we match any @ character we have a maximum LCS of _D_-1, and we can always achieve this. If we match any characters from _AG<sub>i</sub>_, then we can match no @ symbols. Thus, what remains to be proven is that if there is an alignment with exactly one _k_-tuple such that<tbc>

\(\mathrm{LCS}(X_1[i_{j,1}],\dots,X_{k-1}[i_{j,k-1}],X_y[i_{j,k}])=z+1,\)

<tbc>then<tbc>

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),SAG_y(Y))=D,\)

<tbc>if there are no _k_-tuples with an LCS of _z_+1 then:

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),SAG_y(Y))\le D-1.\)

## Case 1 \[There is 1 "good" _k_-tuple, lower bound\]:

Consider aligning the strings where the _k_-tuples of strings which have a LCS of _z_+1 line up. Now, we can match _m_ copies of _B_. What about $_<sub>i</sub>_ symbols? There are \(2\ell n\) copies of the $_<sub>i</sub>_ symbol in _AG<sub>i</sub>(X<sub>i</sub>_), they only appear in the copies of _A_ (they don’t appear in _A_<sub>-_i_</sub>). If we are matching up with a perfect alignment we can match all \(2\ell n\) of these symbols. They either line up with copies of _A_ in other strings, or copies of _A_<sub>-_j_</sub>. Finally, there are \(2\ell m\) copies of $_<sub>y</sub>_ in _AG<sub>y</sub>(Y_). In a perfect alignment these symbols will all get matched to symbols that appear in copies of _A_ in other strings. So, in total<tbc>

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),AG_y(Y))\ge 2\ell m+2\ell(m+(k-1)n)+zm+1=D.\)

