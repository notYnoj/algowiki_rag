## Mapping between windows.

We say that a mapping \(\mu:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\) between windows is monotone if for all \(a,a'\in\mathcal{A}\) such that \(\mu(a),\mu(a')\neq\perp\) and \(s(a)\le s(a')\) we also have that \(s(\mu(a))\le s(\mu(a'))\) and \(e(\mu(a))\le e(\mu(a'))\). Setting \(\mu(a)=\perp\) represents deleting _a_ from the string. As such, we define \(ED(a,\perp)=d\) for all windows _a_.

By abuse of notation, we let \(\mu\subset\mathcal{A}\) denote the set of _A_-windows such that \(\mu(a)\neq\perp\). For \(a\in\mu\), let _a_.next denote the window \(a'\in\mu\) immediately after _a_ (note that next depends on the mapping \(\mu\)). If _a_ is the last window in \(\mu\), we define _a_.next :=\(\perp\). We define _a_.prev in the analogous way.

For a monotone mapping \(\mu\) we define its _edit distance_ as:

\(\mathrm{ED}(\mu)=\sum_{a\in\mathcal{A}}\mathrm{ED}(a,\mu(a))+\sum_{i=1}^n\big|\#\{a\text{s.t.}i\in\mu(a)\}-1\big|\)

The first term is just sum of the edit distances between matched windows. To understand the second term, notice that for each _i_ we expect it to appear in the image \(\mu(a)\) of exactly 1 window. The second term sums the difference between the number of appearances of _i_ and 1; it is a penalty for either overlap of windows (requiring deletions) or excessive spacing (requiring insertions).

The next lemma asserts that the cost of a minimal monotone mappings provides a good approximation for the actual edit distance between the input strings _A,B_.

**Lemma 10.** _Let_ \(A,B\in\Sigma^n\)_, then the following holds:_

1. _For every monotone mapping_ \(\mu:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\) _we have:_ \(\mathrm{ED}(\mu)\ge\mathrm{ED}(A,B)\).<tbc>

_2._ _There exists a monotone mapping_ \(\mu:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\) _satisfying:_ \(ED(\mu)\le(1+8\epsilon)\mathrm{ED}(A,B)\).

_Proof._ (Part 1.) Using \(\mu\) we construct an explicit mapping from _A_ to _B_. For each window, \(a\in\mathcal{A}\), transform the characters of _a_ in _A_ into \(\mu(a)\). If \(\mu(a)=\perp\), then delete all the characters of _a_. Finally, if _a_ is not the last window, \(\mu(a)\neq\perp\) and \(e(\mu(a))-s(\mu(a.\text{next}))>0\) then delete that many characters from the end of \(\mu(a)\).

Let \(\mu(A)\) be the currently transformed string. Then, by construction

\(\mathrm{ED}(A,\mu(A))\le\sum_{a\in\mathcal{A}}\mathrm{ED}(a,\mu(a))+\sum_{i:\#\{a\text{s.t.}i\in\mu(a)\}\ge 1}[\#\{a\text{s.t.}i\in\mu(a)\}-1]\)

Here the second term counts for all indices of _B_ that are counted more than once in \(\mu\).

Furthermore, since we deleted any overlaps between \(\mu(a)\)s, we have \(\mu(A)\) as a subsequence of _B_. Thus,

\(\mathrm{ED}(\mu(A),B)=|B-\mu(A)|=\sum_{i:\#\{a\text{s.t.}i\in\mu(a)\}=0}[1-\#\{a\text{s.t.}i\in\mu(a)\}]\)

Here we account for all indices of _B_ that are not counted in \(\mu\).

Putting the above two inequalities together and using the triangle inequality, we get

\(\mathrm{ED}(A,B)\le\mathrm{ED}(A,\mu(A))+\mathrm{ED}(\mu(A),B)=\mathrm{ED}(\mu)\)

(Part 2.) Consider the optimal sequence of edits from _A_ to _B_. This can be viewed as \(\ell\) substitutions of characters of _A_, _k_ deletions of characters, and then _k_ insertions, where \(2k+\ell=\mathrm{ED}(A,B)\). Let \(A'\) be the subsequence of characters of _A_ which are either untouched or substituted to match a character in _B_. Let \(B'\) be the corresponding subsequence of _B_. Let \(\mu':A'\rightarrow B'\) be the monotone correspondence between the characters of these solution.

