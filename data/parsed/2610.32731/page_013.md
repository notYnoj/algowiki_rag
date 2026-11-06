each \(y\in C\). Let _z=y._`orig`. If _z._copies_\<z._`weight`, then insert another copy. That is, create a new element \(z'\) with \(z'.\mathtt{orig}=z\) and \(\mathrm{key}(z')=\mathrm{key}(z)\), call _H._`insert`(_x_), and increment _z._copies`. If instead \(z'.\mathtt{copies}\ge z'.\mathtt{weight}\), then set \(z.\mathtt{wsh-corr}\leftarrow 1\), and do not create a copy. In the end, return the set \(C'\) of all WSH elements _z_ which we just marked as corrupted with \(z.\mathtt{wsh-corr}\leftarrow 1\).

The operation `increase-weight`(_x,w_) sets \(x.\mathtt{weight}\leftarrow x.\mathtt{weight}+w\). If _x._`wsh-corr`=0, we are done. Otherwise, insert a new copy of _x_ as above, and set \(x.\mathtt{wsh-corr}\leftarrow 0\).

**Observation 15.** _The following invariants hold after each operation:_

• _Each element contained in the WSH is also contained in H._<tbc>

• _Each element in H is either contained in the WSH or a copy of an element contained in the WSH. That is, for each element x of H, x._`orig` _is contained in the WSH._<tbc>

• _For each element x in the WSH, H contains_ \(x.\mathtt{copies}\le x.\mathtt{weight}\) _copies of x (including x itself)._<tbc>

• _Each element x in the WSH is corrupted in the WSH (i.e., x._`wsh-corr`=1_) if and only if x._`copies`=_x._`weight` _and all copies of x (including x itself) are corrupted in H._

**Lemma 16. find-min** _is correct, that is, its returned element x satisfies_ \(\mathrm{key}(x)\le\mathrm{key}(y)\) _for each uncorrupted element y in the WSH._

_Proof._ Recall that `find-min` first calls \(x\leftarrow H.\mathtt{find-min}()\) and then returns _y=x._`orig`. By correctness of _H_, we know that key(_y_)=key(_z_) is no larger than each uncorrupted key in _H_. Suppose for the sake of contradiction that there exists an element _z_ in the WSH that is uncorrupted and satisfies key(_z)\<_key(_x_). If _z_ is uncorrupted in _H_, then we immediately have a contradiction. Otherwise, observe that _H_ must contain at least one uncorrupted copy \(z'\) of _z_. But then \(\mathrm{key}(z')=\mathrm{key}(z)<\mathrm{key}(x)\), so _H._`find-min`() should not have returned _x_, again a contradiction.

**Lemma 17.** _The corruption invariant of the WSH holds. That is, we have_ \(W_{corrupted}\le\varepsilon(m+W_{deleted})\) _where m is the number of_ `insert` _operations so far, W<sub>corrupted</sub> be is sum of weights of corrupted elements currently in the soft heap, and W<sub>deleted</sub> is the sum of weights of deleted elements at the time of their deletion._

_Moreover, the total number of insertions into the soft heap H is_ O(_m+W<sub>deleted</sub>)._

_Proof._ First note that `increase-weight` may un-corrupt an element (which can only decrease _W_<sub>corrupted</sub>), and increases the weight of an afterwards uncorrupted element (which does not affect the invariant). Thus, applying `increase-weight` cannot violate the corruption invariant.

Let \(m'\) be the number of insertions into _H_ so far, let \(d'\) be the number of deletions from _H_ so far, and let \(c'\) be the number of corrupted elements currently in _H_. We have \(c'\le\varepsilon'm'\) by correctness of _H_. Moreover, observation 15 implies that

• Each corrupted element _x_ corresponds to precisely _x._`weight` corrupted elements of _H_, so \(W_\mathrm{corrupted}\le c'\).<tbc>

