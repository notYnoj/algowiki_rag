_Then, if there is a perfect alignment_ \(\Lambda\) _in which there are exactly m k-tuples such that_<tbc>

\(\mathrm{LCS}(X_1[i_{j,1}],\dots,X_{k-1}[i_{j,k-1}],X_y[i_{j,k}])=z+1,\)

<tbc>_then_

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D,\)

_if all perfect alignments have less than m k-tuples with a_ LCS _of z_+1 _then_

\(\mathrm{LCS}(SAG_1(X_1),SAG_2(X_2),\dots,SAG_{k-1}(X_{k-1}),SAG_y(Y))=D-1.\)

_These strings use an additional alphabet of size O(k). The total length of strings is_ \(O(\ell n)\)_. The value of is_ \(D=2\ell(2m+(k-1)n)+(z+1)m\).

_Proof._ In the _SAG_ gadgets note that if we match any @ character we have a maximum LCS of _D_-1, and we can always achieve this. If we match any characters from _AG<sub>i</sub>_, then we can match no @ symbols. Thus, what remains to be proven is that if there is a perfect alignment \(\Lambda\) in which there are _mk_-tuples such that if we have _m_ matches where<tbc>

\(\mathrm{LCS}(X_1[i_{j,1}],\dots,X_{k-1}[i_{j,k-1}],X_y[i_{j,k}])=z+1,\)

<tbc>then<tbc>

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),SAG_y(Y))=D,\)

<tbc>otherwise

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),SAG_y(Y))\le D-1.\)

Recall \(D=2\ell(2m+(k-1)n)+(z+1)m\). Now we have three cases to argue.

## Case 1 \[There are _m_ "good" _k_-tuples, lower bound\]:

Consider aligning the strings in the perfect alignment \(\Lambda\) which has _mk_-tuples of strings which have a LCS of _z_+1. Now, we can match _m_ copies of _B_. What about $_<sub>i</sub>_ symbols? There are \(2\ell n\) copies of the $_<sub>i</sub>_ symbol in _AG<sub>i</sub>(X<sub>i</sub>_), they only appear in the copies of _A_ (they don’t appear in _A_<sub>-_i_</sub>). If we are matching up with a perfect alignment we can match all \(2\ell n\) of these symbols. They either line up with copies of _A_ in other strings, or copies of _A_<sub>-_j_</sub>. Finally, there are \(2\ell m\) copies of $_<sub>y</sub>_ in _AG<sub>y</sub>(Y_). In a perfect alignment these symbols will all get matched to symbols that appear in copies of _A_ in other strings. So, in total

\(\mathrm{LCS}(AG_1(X_1),AG_2(X_2),\dots,AG_{k-1}(X_{k-1}),AG_y(Y))\ge 2\ell m+2\ell(m+(k-1)n)+(z+1)m\ge D.\)

## Case 2 \[There are _m_ "good" _k_-tuples, upper bound\]:

Across all % and $_<sub>i</sub>_ symbols the maximum number of matches is \(2\ell(m+m+n(k-1))\). What if we don’t match the strings in a perfect alignment manner? There are two ways to do this. One is to skip matching some strings in _Y_ (e.g. merging _Y_\[_j_\] and _Y_\[_j_+1\] and matching that to some single string somewhere else, or simply skipping over a string in _Y_ ). If this happens we miss out on the characters in at least one _B_. The advantage gleaned for every skipped string in _Y_ is at most \(|Y[j]|=\ell\), but skipping out on _B_ is worse, we lose \(2\ell\) matches. The next case is skipping strings in _X<sub>i</sub>_. That is, matching _Y_\[_j_\] with \(X_i[j']\) but matching _Y_\[_j_\] with \(X_i[j'+1+\Delta]\) for some \(\Delta\ge 1\). This looses at least \(2\ell\) $_<sub>i</sub>_ characters. Any _k_-tuple of strings has, by assumption in the lemma, a _k_-LCS of at most _z_+1. So, this causes the _k_-LCS less than _D_. Finally, any time we match multiple strings in _X<sub>i</sub>_ with a single string in _Y_ , _Y_\[_j_\], can increase the match in _Y_\[_j_\] by at most \(\ell\). However, we loose at least \(2\ell\) symbols $_<sub>i</sub>_ in _X<sub>i</sub>_. This means the _k_-LCS of _AG<sub>i</sub>_ strings is at most \(D-\ell\).

## Case 3 \[There are less than _m_ "good" _k_-tuples\]:

Now, if there are less than _m_ matches with a _k_-LCS of _z_+1 then what is the maximum _k_-LCS? Similarly to case 2, if we skip as string in _Y_ or merge _Y_\[_j_\] and _Y_\[_j_+1\] we loose at least one _B_. Because the _B_ copies are in-between every pair of adjacent _Y_ strings. If we matching some symbol in each _Y_\[_j_\], then the maximum value if we match one string from each _X<sub>i</sub>_ to each string in _Y_ is \(D-2\ell\) because we must skip some \(2\ell\) characters $_<sub>i</sub>_, so the maximum match would be at most \(D-2\ell\). Finally, we could merge multiple strings from _X<sub>i</sub>_ and match with a single string from _Y_ , in this setting we could potentially get \(D-2\ell+\ell\). While we can potentially match all \(\ell\) characters in _Y_ , we must miss out on at least \(2\ell\) $_<sub>i</sub>_ characters.

So, we have proven the result that if we have _m_ matches where<tbc>

\(\mathrm{LCS}(X_1[i_{j,1}],\dots,X_{k-1}[i_{j,k-1}],X_y[i_{j,k}])=z+1,\)

