## Composition.

Suppose _U_<sub>top</sub> is a sequence in which all live blocks have length _j_ and _U_<sub>mid</sub> is a sequence with ∥_U_<sub>mid</sub>∥=_j_. The _composition_ \(U_\mathrm{sub}=U_\mathrm{top}\circ U_\mathrm{mid}\) is obtained by replacing each live block _L_ of _U_<sub>top</sub> with a copy _U_<sub>mid</sub>(_L_) over the alphabet of _L_, whereas dead blocks of _U_<sub>top</sub> are inherited by _U_<sub>sub</sub> verbatim. In general _U_<sub>mid</sub>(_L_) can contain both live and dead blocks \[Pet15b\], but in our particular construction _U_<sub>mid</sub>(_L_) contains only live blocks.

## Shuffling.

Now suppose _U_<sub>sub</sub> is a sequence whose live blocks have length _j_ and _U_<sub>bot</sub> is a sequence with (|_U_<sub>bot</sub>|)=_j_. The _left-shuffle_ \(U_\mathrm{sub}\otimes U_\mathrm{bot}\) is obtained as follows. Let \(U_\mathrm{sub}=D_0L_1D_1L_2D_2\cdots L_kD_k\), where _L<sub>i</sub>_ is the _i_th live block, _D<sub>i</sub>_ is zero or more dead blocks, and \(k=(\left|U_\mathrm{sub}\right|)\). Let \(U_\mathrm{bot}^*=U_\mathrm{bot}^{(1)}\cdots U_\mathrm{bot}^{(k)}\) be the concatenation of _k_ copies of _U_<sub>bot</sub> over disjoint alphabets. The _left-shuffle_ is obtained by taking, for all _i_, the block \(L_i=(a_1a_2\cdots a_j)\) and inserting \(a_\ell\), for \(\ell\in[1,j]\), at the _left end_ of the \(\ell\)th live block of \(U_\mathrm{bot}^{(i)}\), then inserting dead blocks _D<sub>i</sub>_ between \(U_\mathrm{bot}^{(i)}\) and \(U_\mathrm{bot}^{(i+1)}\).<sup>5</sup>

## Sequence Construction.

_U(j_) and _U(i,j_) are blocked sequences, where square brackets indicate dead blocks and parentheses indicate live blocks. _U(i,j_) is a variation on order-4 Davenport- Schinzel sequences \[ASS89\], adapted specifically to exclude a small pattern that arises from \(P\otimes(\bullet)\)- type patterns.

\(U(j)=(j\left(j-1\right)\cdots 1)(12\cdots j)2\text{live blocks}U(1,j)=[12\cdots j](12\cdots j)\text{first block dead, second live}U(i,0)=()^22\text{empty live blocks}U(i,j)=(U_\mathrm{top}\circ U_\mathrm{mid})\otimes U_\mathrm{bot}\text{where}U_\mathrm{top}=U(i-1,(\left|U(i,j-1)\right|)),U_\mathrm{mid}=U((\left|U(i,j-1)\right|)),\text{and}U_\mathrm{bot}=U(i,j-1)\)

Let \(N(i,j)=\left|\left|U(i,j)\right|\right|\) be the alphabet size and \(L(i,j)=(\left|U(i,j)\right|)\) be the number of live blocks. _N,L_ obey the following recurrence:

\(L(1,j)=1L(i,0)=2L(i,j)=L(i,j-1)\cdot 2\cdot L(i-1,L(i,j-1))N(1,j)=jN(i,j)=N(i,j-1)\cdot 2\cdot L(i-1,L(i,j-1))+N(i-1,L(i,j-1))\)

**Lemma 4.1.** _Fix any U=U(i,j)._

1. _All live blocks in U have length j. Each symbol appears_ 2<sup>_i_-1</sup>+1 _times in U, its first occurrence appearing in a dead block, and the remaining_ 2<sup>_i_-1</sup> _times in live blocks._<tbc>

_2._ _As a consequence of part 1,_ \(N(i,j)=(j/2^{i-1})\cdot L(i,j)\).<tbc>

<sup>5</sup>The _right shuffle_ \(U_\mathrm{sub}\otimes U_\mathrm{bot}\) is defined in the same way, except that \(a_\ell\) is inserted at the _right end_ of the \(\ell\)th live block of \(U_\mathrm{bot}^{(i)}\). We only use left-shuffles but there are cases where it is desirable to use both \[Pet11b, Pet15b\].

