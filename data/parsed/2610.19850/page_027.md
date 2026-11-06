**Theorem 7.** _Let_ \(X\subseteq V(G)\) _be a shy set. Assume there exists a triplet_ (_a,b,S_) _such that:_

• _a and b are two distinct vertices and in particular_ \(a\in X\),<tbc>

• _S is the X-close_ (_a,b)-separator,_<tbc>

• _S is X-shy with regards to C<sub>G</sub>(a,S)._

_Then we can identify in time O(n_<sup>3</sup>) _a PMC_ \(\Omega\subseteq X\) _such that_ \(S\unknown\Omega\subseteq S\cup(C_G(a,S)\cap X)\).

_Proof._ The set \(X\cap C_G(a,S)\) is nonempty because otherwise _S_ could not be _X_-shy with regard to _C<sub>G</sub>(a,S_), the latter being a full component for _S_ in _G_. Consider set \(Y=S\cup(X\cap C_G(a,S))\) which is a subset of _X_. Set _Y_ admits no full component in _G_\\_Y_ : the components full for _S_ that do not contain _a_ are not adjacent to \(X\cap C_G(a,S)\), and the connected components of _G_\\_Y_ included into _C<sub>G</sub>(a,S_) are not full for _S_ because _S_ is _X_-shy with regard to _C<sub>G</sub>(a,S_). So, _Y_ is a shy set. Either _Y_ is a PMC, and in this case, _X_ is obviously a PMC superset. Or, there is at least one conflict pair within _Y_ . We apply conflict-greedy on set _Y_ , but we orient the choice of the protected vertex at each iteration. In particular, we maintain the fact that \(S\subseteq U\), where _U_ is the variable set in line 3 in Algorithm 1, \(U\subseteq Y\) .

For the selection of the protected vertex _u_ (line 5 of Algorithm 1), we apply the following rule:

• if there is at least one conflict pair (_s,v_) for _U_ which belongs to \(S\times(C_G(a,S)\cap X)\), fix \(u=s\in S\),<tbc>

• otherwise, if there are only conflict pairs in \((C_G(a,S)\cap X)\times(C_G(a,S)\cap X)\), fix _u_ arbitrarily.

In other words, we fix as a priority that the protected vertex belongs to _S_. Observe that there cannot be a conflict pair in \(S\times S\) because such pairs are visible despite _Y_ , seeing each other through the component _C<sub>G</sub>(b,S_) which does not intersect _Y_ by definition. We prove that the result of conflict-greedy(_Y_), with this specific selection process which does not influence the time complexity, is a PMC.

Let _Z_=conflict-greedy(_Y_). As we privilege vertices in _S_ for the protected vertex and there are no \(S\times S\) conflict pairs, we have \(S\unknown Z\). From Theorem 5, conflict-greedy returns a brightening of set _Y_ , regardless the choice of protected vertices. Hence, if _Z_ admits a full component, then it is a native component for _Y_ , _i.e._ a connected component initially present in _G_\\_Y_ . As a first remark, we cannot have _Z=S_, otherwise _C<sub>G</sub>(a,S_) would be a non- native full component for _S_: _C<sub>G</sub>(a,S_) would be non-native as \(Y\cap C_G(a,S)=X\cap C_G(a,S)\neq\emptyset\). Therefore, \(Z\cap C_G(a,S)\neq\emptyset\). Let _B_ be a (native) full component for _Z_. Due to the previous remark, _B_ cannot be a connected component of _G_\\_S_ different from _C<sub>G</sub>(a,S_): such a component would not be adjacent to \(Z\cap C_G(a,S)\neq\emptyset\), contradicting the fact that _B_ is full for _Z_. So, \(B\unknown C_G(a,S)\). In this case, as _B_ is native, this means there exists a connected component of _G_\\_Y_ which is fully adjacent to _Z_, and thus in particular to \(S\unknown Z\). Note that, by definition of _Y_ , _B_ is also a connected component of _G_\\_X_ included into _C<sub>G</sub>(a,S_). This yields a contradiction since _S_ is _X_-shy with regard to _C<sub>G</sub>(a,S_). As a consequence, _Z_ does not admit any native full component: _Z_ is a PMC.

In summary, conflict-greedy with a priority rule on _S_-vertices produces a PMC \(Z\subseteq Y\subseteq X\). The running time needed is the one of conflict-greedy, already given in Theorem 5.

