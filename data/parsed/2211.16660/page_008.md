of two. By abuse of notation, if _i_ is a \(\ell\)-flag, we may also call the _i_-th one of _x_ a \(\ell\)-flag. Note that there are many more zeros than ones between the _i_th and \((i+\ell)\)-th one, so flags tell us where it is more advantageous to use zeros rather than ones in finding long subsequences.

The basis for the algorithmic structure lemma is a combinatorial structure lemma for strings, which we inherit from \[GHL22, Lemma 4.1\]. We use a weaker form of the lemma, which has a significantly simpler statement and proof, and is also tailored to our algorithmic application. The proof is given in Appendix A.

**Lemma 4.4** (Combinatorial Structure Lemma)**.** _For_ \(\varepsilon=10^{-5}\) _and w sufficiently large, at least one of the following two conditions holds for every string_ \(x\in\{0,1\}^w\).

1. _There exists_ \(\ell\in[\varepsilon^2w,w]\) _equal to a power of two and an_ 0.1_-imbalanced interval I in x of length_ \(\ell\).<tbc>

_2._ _There exists_ \(\ell\in[1,\varepsilon^2w)\) _equal to a power of two such that the number of_ \(\ell^+\)_-flags in x is at least_ \(\varepsilon w\)_, and x contains_ \((0^\ell 1^\ell)^{\varepsilon w/\ell}\) _as a subsequence._

For the remainder of Section 4, fix \(\varepsilon:=10^{-5}\). Lemma 4.4 shows that every sufficiently long string _x_ is of one of the below types, of which there are log_w_ total.

**Definition 4.5.** Let \(\ell\) be a power of two, \(\ell\in[1,w]\), and \(x\in\{0,1\}^w\).

1. We say that _x_ is \(\ell\)_-coarse_ if \(\ell\ge\varepsilon^2w\) and there is a \(\varepsilon^2\)-imbalanced interval _I_ in _x_ of length \(\ell\). We say _x_ is _coarse_ if it is \(\ell\)-coarse for some \(\ell\ge\varepsilon^2w\).<tbc>

2. We say that _x_ is \(\ell\)_-fine_ if it is not coarse, \(\ell<\varepsilon^2w\), the number of \(\ell^+\)-flags in _x_ is at least \(\varepsilon w\), and _x_ contains \((0^\ell 1^\ell)^{\varepsilon w/\ell}\) as a subsequence. We say _x_ is _fine_ if it is \(\ell\)-fine for some \(\ell<\varepsilon^2w\).

Note that for the convenience of our later proofs, we change the imbalanced threshold from 0.1 in Lemma 4.4 to the much smaller \(\varepsilon^2\) in the above definition. Since every 0.1-imbalanced interval is also \(\varepsilon^2\)-imbalanced, Lemma 4.4 implies every sufficiently long string _x_ is of one of the above two types.

## 4.3 Algorithmic structure lemma ingredients

As in the last section, we fix \(\varepsilon=10^{-5}\). Also, for brevity, for every positive integer \(\ell\), define the special string

\(y_\ell:=(0^\ell 1^\ell)^{\varepsilon w/(5\ell)}.\)

We prove two ingredients to justify our "_Q<sub>t</sub>_" properties in the algorithmic structure lemma. The first is the simple observation that if _x_ is \(\ell\)-fine and \(\mathsf{LCS}(x,y)\ge(1-\delta_{code})|x|\), then _y_ inherits the easily testable subsequence \(y_\ell\) from _x_.

**Lemma 4.6.** _Let_ \(0<\delta<\varepsilon/10\), \(\ell\) _be a power of two, and_ \(w>\varepsilon^{-2}\ell\)_. If x is an_ \(\ell\)_-fine string of length w and_ \(\mathsf{LCS}(x,y)\ge(1-\delta)w\)_, then_ \(y_\ell\) _is a subsequence of y._

_Proof._ By definition, if _x_ is \(\ell\)-fine then _x_ contains \((0^\ell 1^\ell)^{\varepsilon w/\ell}=y_\ell^5\) as a subsequence. Since \(\mathsf{LCS}(x,y)\ge|x|-\delta w\) and \(y_\ell^5\) is a subsequence of _x_, we have \(\mathsf{LCS}(y_\ell^5,y)\ge|y_\ell^5|-\delta w\). Thus, there is a subsequence of _y_ obtained by applying \(\delta w\) deletions to \(y_\ell^5\). By counting, at most \(2\delta w/\ell\) of the chunks \(0^\ell 1^\ell\) in \(y_\ell^5\) receive more than \(\ell/2\) of these deletions. The remaining \(\varepsilon w/\ell-2\delta w/\ell>4\varepsilon w/(5\ell)\) chunks each have at least \(\ell/2\) zeros and \(\ell/2\) ones. Taking \(\ell\) zeros from the first two chunks, \(\ell\) ones from the next two, and so on, we see that _y_ contains \(y_\ell\) as a subsequence, as desired.

The second ingredient implies that if _x_ is \(\ell\)-fine, then a substring of _x_ can be matched advantageously with \(y_\ell\).

