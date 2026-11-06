_3. The number of dead blocks is at most L(i,j_)-1.<tbc>

_4. If n=N(i,j_) _is the number of symbols in U and m\<_2_L(i,j_) _the number of blocks,_ \(i=\alpha(n,m)\pm O(1)\)_, and_ \(|U|=\Theta(n2^{\alpha(n,m)})\).

_Proof._ <u>Part 1.</u> The claim holds in the base cases _U_(1_,j_) and _U(i,_0). All live blocks in _U_<sub>bot</sub>=_U(i,j_-1) have length _j_-1 by induction, and each receive one symbol in the shuffling operation \((U_\mathrm{top}\circ U_\mathrm{mid})\unknown U_\mathrm{bot}\). All symbols in _U_<sub>bot</sub>=_U(i,j_-1) appear in 2<sup>_i_-1</sup> live blocks. Those in \(U_\mathrm{top}=U(i-1,\unknown U(i,j-1)\unknown)\) appear in 2<sup>_i_-2</sup> live blocks, and therefore in 2<sup>_i_-1</sup> live blocks in \(U_\mathrm{sub}=U_\mathrm{top}\circ U_\mathrm{mid}\) since _U_<sub>mid</sub> doubles the number of live occurrences. The property that first occurrences appear in dead blocks is preserved by composition and shuffling. <u>Part 2.</u> Note that both \(j\cdot L(i,j)\) and \(2^{i-1}\cdot N(i,j)\) both count the total length of all live blocks. <u>Part 3.</u> The claim holds in all base cases. By induction, the number of dead blocks in _U_<sub>top</sub> is at most _L(i_-1_,L(i,j_-1))-1. \(U_\mathrm{bot}^*\) consists of 2_L(i_-1_,L(i,j_-1)) copies of _U_<sub>bot</sub>=_U(i,j_-1), so \(U_\mathrm{bot}^*\) has \(2L(i-1,L(i,j-1))(L(i,j-1)-1)\) dead blocks. In total there are _L(i_-1_,L(i,j_-1))(2_L(i,j_-1)-1)-1 \(\unknown L(i,j)-1\) dead blocks. <u>Part 4.</u> Proving Ackermann-like functions are equivalent inasmuch as their inverses differ by \(\pm O(1)\) is tedious, but straightforward. See \[Pet06, Lemma 3.10\] for an example of such a proof.

**Lemma 4.2.** _Let U=U(i,j_) _be obtained from U_<sub>top</sub>_,U_<sub>mid</sub>_,U_<sub>bot</sub>_. Suppose a\<b are two symbols in_ \(\Sigma(U)\) _appearing in a common live block._

1. _The restriction of U to letters_ {_a,b_} _is of the form a_<sup>∗</sup>_b_<sup>∗</sup>(_ab)b_<sup>∗</sup>_a_<sup>∗</sup>.<tbc>

_2._ _If_ \(a\in\Sigma(U_\mathrm{top})\), \(b\in\Sigma(U_\mathrm{bot}^*)\)_, then a\<c for every symbol c appearing in b’s copy of U_<sub>bot</sub>.

_Proof._ The claim is true in the base cases _U_(1_,j_) and _U(i,_0). Consider the moment that _a_ is shuffled into _b_’s live block, where \(a\in\Sigma(U_\mathrm{top})\) and \(b\in\Sigma(U_\mathrm{bot}^*)\). All occurrences of _b_ appear in one copy of _U_<sub>bot</sub> in \(U_\mathrm{bot}^*\), and exactly one occurrence of _a_ is shuffled into this copy. It follows that the restriction of _U_ to letters {_a,b_} is of the form _a_<sup>∗</sup>|_b_<sup>∗</sup>(_ab)b_<sup>∗</sup>|_a_<sup>∗</sup>, where the bars mark the boundary of _b_’s copy of _U_<sub>bot</sub>. Furthermore, since the first occurrence of _a_ is in a dead block, which is inserted between two copies of _U_<sub>bot</sub> in \(U_\mathrm{bot}^*\), _a\<c_ for _every c_ in _b_’s copy of _U_<sub>bot</sub>.

**Lemma 4.3.** _U=U(i,j_) _does not contain any subsequences order-isomorphic to_ 41213.

_Proof._ Since _U_ is in canonical form, the existence of 41213 implies the existence of a subsequence order-isomorphic to<tbc>

\(\sigma=31213\)

<tbc>Suppose that \(\sigma\) first appears in \(U(i,j)=U_\mathrm{sub}\unknown U_\mathrm{bot}=(U_\mathrm{top}\circ U_\mathrm{mid})\unknown U_\mathrm{bot}\). If \(\sigma\) already appears in _U_<sub>sub</sub> but did not appear in _U_<sub>top</sub>, then _U_<sub>top</sub> must have contained \(\sigma'\).<tbc>

\(\sigma'=31(12)3\)

<tbc>Note that {2,3} cannot share a live block in _U_<sub>top</sub> without also including 1, and if {1,2,3} shared a live block in _U_<sub>top</sub>, the restriction of _U_<sub>top</sub> to {1,2,3} would, by Lemma 4.2(1), be:<tbc>

\(1^*2^*3^*(123)3^*2^*1^*\)

<tbc>and the restriction of _U_<sub>sub</sub> to {1,2,3} would be:<tbc>

\(1^*2^*3^*(321)(123)3^*2^*1^*,\)

