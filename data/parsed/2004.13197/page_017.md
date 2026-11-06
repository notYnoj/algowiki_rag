Denote the nodes that are descendants of _v_<sub>new</sub> in T as _v_<sub>1</sub>_,...,v<sub>M/w</sub>_. Let the corresponding search intervals be \(S_1^{p-1},\dots,S_{M/w}^{p-1}\), respectively. Let \(X=\cup_{i=1}^{M/w}S_i^{p-1}\) and _Y=S_<sub>new</sub>\\_X_. The set _Y_ is a union of at most _M/w_+1 intervals, each of which we denote by _Y<sub>i</sub>_. Let _Z_ be the largest interval from the set \(\{S_1^{p-1},\dots,S_{M/w}^{p-1},Y_1,\dots,Y_{M/w}\}\). Hence, \(|Z|\ge|S_\mathrm{new}|/(2M/w)\).

There are two cases to consider. The first case is when \(Z=S_i^{p-1}\) for some _i_. In this case, \(S_\mathrm{new}=S_i^{p-1}\). In doing this we have given at most _O_(log_M_) bits. Now we proceed as in Case 1 to resolve the conflict with at most _O_(1) extra bits. Otherwise, if _Z=Y<sub>i</sub>_ for some _i_, then the adversary allots \(\ell_\mathrm{new}^p\) to the highest node _v_ in T such that \(I(v)\subseteq Z\).

## 5.1 Analysis

We have the following auxiliary lemmas:

**Lemma 11.** _On a small-block input, the adversary gives at most O_(log(_n<sub>p,i</sub>_+1)) _bits to_ \(\ell_i^p\).

_Proof._ Observe that

\(\|P_j\|\ge\frac{\|S_i^{p-1}\|}{(n_{pi}+1)}.\)

Divide \(S_i^{p-1}\) into 2(_n<sub>p,i</sub>_+1) equal parts (with the last one being possibly smaller). If _P<sub>j</sub>_ is equal to the union of two consecutive such parts, there is a node in T corresponding to _P<sub>j</sub>_, and the adversary has given exactly log(_n<sub>p,i</sub>_+1) bits. Otherwise, _P<sub>j</sub>_ contains at least one of these parts, for which there is a node log(_n<sub>p,i</sub>_+1)+1 levels below \(v(\ell_i^{p-1})\), which is how many bits the adversary gives in this scenario.

In either case, the maximum number of bits given by the adversary is _O_(log(_n<sub>p,i</sub>_+1)), as claimed.

**Lemma 12.** _On a small-block input, the adversary gives at most O(B_) _bits._

_Proof._ This follows easily from Lemma 11. Let _G_ denote the total number of bits given by the adversary during the input of a block of small elements. It can be seen that \(G=\sum_{i=1}^B(\mathrm{log}(n_{p,i}+1)+1)\). By definition \(\sum_{i=1}^Bn_{pi}=B\), implying that \(\sum_{i=1}^B\mathrm{log}(n_{p,i}+1)\le B\), which in turn implies that _G\<_2_B=O(B_).

**Lemma 13.** _During the input of a large element, the adversary gives at most O_(log_M_) _bits._

