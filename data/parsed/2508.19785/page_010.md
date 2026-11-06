where we used the inequality \(\genfrac(){pt}{2}{\eta}{2}\le\left(\frac{e\eta}{z}\right)^z\).

By using the union bound on all _i_ and the inequality \(8logN\le\ell\le\frac{M}{432}<N-1\), we can upper bound the sought probability as:

\(N\cdot\frac{\ell+1}{2^\ell}<\frac{N^2}{2^8logN}=N^{-6}.\) □

Lemma 3.2 allows us to show that if _A_ and _B_ are sequences containing randomly selected elements, the sequence obtained by simultaneously inserting element _x_ of _B_ into _A_ in the position returned by NoisySearch is likely to have a dislocation that is at most a constant factor larger than the dislocation of _A_. This is formalized as follows.

Lemma 3.3. _Let A be a sequence of_ \(m\ge max\{64,\sqrt{n}\}\) _elements chosen u.a.r. from S, and let B be a set of at most m elements chosen u.a.r. from S_\\_A (both without replacement). Let d be an integer such that_ \(max\{disl(A),logn\}\le d\le\frac{\sqrt{n}}{2160\alpha}\) _and, for each_ \(x\in B\)_, let_ \(r_x\in\{1,\dots,m\}\) _be an integer that satisfies_ \(|r_x-rank(x,A)|\le\alpha d\)_. The sequence_ \(\widetilde{S}\) _obtained from simultaneously inserting each element_ \(x\in B\) _into position r<sub>x</sub> of A (breaking ties arbitrarily) has a maximum dislocation of at most_ \(\gamma d\) _with probability at least_ 1-_O(n_<sup>-3</sup>).

Proof. Let _S_<sup>∗</sup> be the correctly sorted sequence of the elements in _S_ and observe that, since the elements in _A_ and _B_ are selected u.a.r. from _S_, we can relate their distribution in _S_<sup>∗</sup> with the distribution of the drawn balls in the urn experiment of Lemma 3.2: the urn contains _N_=|_A_|+|_B_| balls each corresponding to an element in \(A\cup B\), a ball is white if it corresponds to one of the _M=m_ elements of _A_, and black if it corresponds to one of the at most _m_ elements of _B_.

Then, by Lemma 3.2 with \(\ell=2\lfloor 2\alpha d\rfloor+2\), we have that all contiguous subsequences of _S_<sup>∗</sup> with least \(54\ell\) elements contain more than \(\ell\) elements from _A_ with probability at least \(1-m^{-6}\ge 1-n^{-3}\). Hence, with the aforementioned probability, all contiguous subsequences of _S_<sup>∗</sup> containing up to \(\ell\) elements from _A_ have a length of at most \(54\ell\le 216\alpha d+108\). In the rest of the proof we assume that this is the case, and we argue that this implies that the dislocation of \(\widetilde{S}\) is at most \(226\alpha d=\gamma d\).

For an element \(y\in A\cup B\), let _X<sub>y</sub>_ denote the set of all elements \(x\in B\) such that \(|rank(x,A)-rank(y,A)|\le 2\alpha d\). We separately study the dislocation \(disl(y,\widetilde{S})\) for \(y\in A\) and for \(y\in B\).

We consider the case \(y\in A\) first. Observe that inserting element \(x\in B\) can affect the dislocation of _y_ only if one of the following two (mutually exclusive) conditions holds: (i) _x\<y_ and \(r_x\ge pos(y,A)\), or (ii) _x\>y_ and \(r_x\le pos(y,A)\). Indeed, all other elements in _B_ are guaranteed to be in the correct relative order w.r.t. _y_ in \(\widetilde{S}\).<br>
If (i) holds, we have:<tbc>

\(rank(y,A)\ge rank(x,A)\ge r_x-\alpha d\ge pos(y,A)-\alpha d\ge rank(y,A)-(\alpha+1)d.\)

<tbc>If (ii) holds, we have:

\(rank(y,A)\le rank(x,A)\le r_x+\alpha d\le pos(y,A)+\alpha d\le rank(y,A)+(\alpha+1)d.\)

Hence, all the elements _x_ that can affect the dislocation of _y_ following their insertion are contained in _X<sub>y</sub>_, and we have \(disl(y,\widetilde{S})\le d+|X_y|\).

We now consider the case \(y\in B\). Observe that if were to insert only element _y_ in position _r<sub>y</sub>_ of sequence _A_, the dislocation of _y_ in the resulting sequence would be upper bounded by \(\alpha d\). By simultaneously inserting all elements in _B_ into _A_ (with arbitrary tie-breaking), the above upper bound on the dislocation of _y_ can only be affected by the elements in \(x\in B\backslash\{y\}\) that satisfy one of the following two (mutually exclusive) conditions: (i) _x\<y_ and \(r_x\ge r_y\), or (ii) _x\>y_ and \(r_x\le r_y\). If (i) holds, we have:<tbc>

\(rank(y,A)\ge rank(x,A)\ge r_x-\alpha d\ge r_y-\alpha d\ge rank(y,A)-2\alpha d.\)

