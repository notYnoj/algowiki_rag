## Low-Skew Mapping.

A monotone mapping \(\mu:\mathcal{A}\rightarrow\mathcal{B}\) is said to have skew at most _D_ if for all \(a,a'\in\mathcal{A}\) we have:

\(\frac{1}{D}|s(a)-s(a')|\le|s(\mu(a))-s(\mu(a'))|\le D|s(a)-s(a')|\)

We next show that any monotone mapping \(\mu\) can be transformed into a low-skew mapping with \(D=\frac{1}{\epsilon}\) with negligible loss. Along with Lemma 10, this ensures there exists a near-optimal low-skew mapping, which we will exploit in our algorithm design.

**Lemma 11.** _For every monotone mapping_ \(\mu:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\)_, and for every_ \(\epsilon>0\)_, there exists a monotone mapping_ \(\mu':\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\) _such that:_ \(\mathrm{ED}(\mu')\le(1+2\epsilon)\mathrm{ED}(\mu)\) _and_ \(\mu'\) _has a skew that is at most_ \(1/\epsilon\).

_Proof._ Consider \(D=\frac{1}{\epsilon}\). Let \(S\subset\mathcal{A}\times\mathcal{A}\) be the set of all pairs (_a_<sub>1</sub>_,a_<sub>2</sub>) which have more than \(\frac{1}{\epsilon}\) skew, and let \(s(a_1)\le s(a_2)\). We put a partial ordering on _S_ such that \((a_1,a_2)\unknown(a_3,a_4)\) if \(s(a_3)\le s(a_1)\le s(a_2)\le s(a_4)\). Let \(S'\subseteq S\) be the set of pairs that are maximal with respect to this relation.

We also say (_a_<sub>1</sub>_,a_<sub>2</sub>) is disjoint from (_a_<sub>3</sub>_,a_<sub>4</sub>) if either \(s(a_2)\le s(a_3)\) or \(s(a_4)\le s(a_1)\). We now build a set of pair-wise disjoint elements from _S_ by repeatedly picking a maximal element and discarding all elements in _S_ that intersects it. Let us call this set _T_. Label the elements of _T_ by (_a_<sub>1</sub>_,a_<sub>2</sub>),(_a_<sub>3</sub>_,a_<sub>4</sub>)_,...,(a_<sub>2_k_-1</sub>_,a_<sub>2_k_</sub>) such that \(s(a_1)\le s(a_2)\le\cdots\le s(a_{2k-1})\le s(a_{2k})\). For all windows _a_ such that \(s(a_{2i-1})\le a<s(a_{2i})\), set \(\mu'(a)=\perp\). Otherwise, keep \(\mu'(a)=\mu(a)\). Note that \(\mu'\) has skew at most \(\frac{1}{\epsilon}\) since for each \((a,a')\in S\), either \(\mu'(a)=\perp\) or \(\mu'(a')=\perp\). We now show that \(\mathrm{ED}(\mu')\le(1+\epsilon)\mathrm{ED}(\mu)\). Pick \((a_1,a_2)\in T\). If \(|s(\mu(a_1))-s(\mu(a_2))|\ge\frac{1}{\epsilon}|s(a_1)-s(a_2)|\), then

\(\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))\ge|s(\mu(a_1))-s(\mu(a_2))|-|s(a_1)-s(a_2)|\)<br>
\(\ge|s(a_1)-s(a_2)|(\frac{1}{\epsilon}-1)\)

On the other hand, by setting for every \(a\in\mathcal{A}\) with \(s(a_1)\le s(a)<s(a_2)\), \(\mu'(a)=\perp\), we pay an edit cost of at most

\(\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))+|s(a_1)-s(a_2)|\le(1+\frac{\epsilon}{1-\epsilon})\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2))).\)

Note that the edit cost of \(\mu\) restricted to the substring _A_\[_s(a_<sub>1</sub>)_,s(a_<sub>2</sub>)) is only higher than \(\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))\) due to possible double-counting indices which are part of consecutive windows within the interval \[_s(a_<sub>1</sub>)_,s(a_<sub>2</sub>)) that overlap under \(\mu\).

If \(|s(\mu(a_1))-s(\mu(a_2))|\ge\epsilon|s(a_1)-s(a_2)|\), then again, we have

\(\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))\ge|s(a_1)-s(a_2)|-|s(\mu(a_1))-s(\mu(a_2))|\)<br>
\(\ge(1-\epsilon)|s(a_1)-s(a_2)|.\)

On the other hand, by setting for every \(a\in\mathcal{A}\) with \(s(a_1)\le s(a)<s(a_2)\), \(\mu'(a)=\perp\), we pay an edit cost of at most

\(\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))+|s(\mu(a_1))-s(\mu(a_2))|\)<br>
\(\le\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2)))+\epsilon|s(a_1)-s(a_2)|\)<br>
\(\le(1+\frac{\epsilon}{1-\epsilon})\mathrm{ED}(A[s(a_1),s(a_2)),B[\mu(s(a_1)),\mu(s(a_2))).\)

