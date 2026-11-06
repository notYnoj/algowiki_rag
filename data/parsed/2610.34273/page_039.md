three _z_ sectors places them in the matched-sector order. The weight maps and these changes of coordinates act only on the unshared legs, so they can again be extended by the identity on an appended partial summand.

Rule (v) is Lemma 5.4. For full sums, first align the two leading degrees by multiplying the first local map of one construction by a nonnegative power of its parameter. Block-diagonal local maps then give the sum of the leading terms. For products, the leading terms multiply and their degrees add. Leg permutations simply renumber the local maps.

For transitivity, suppose that polynomial local maps give

\(A(\delta)\cdot Y=\delta^aX+\delta^{a+1}X'(\delta),B(\varepsilon)\cdot Z=\varepsilon^bY+\varepsilon^{b+1}Y'(\varepsilon),\)

where \(a,b\ge 0\) and the primed expressions have polynomial entries in the stated output coordinates. Choose an integer _L\>a_, substitute \(\varepsilon=\delta^L\), and compose the local maps. The desired term has degree _a+bL_. The error from \(X'\) has degree at least _a+bL_+1, and the error from \(Y'\) has degree at least (_b_+1)_L\>a+bL_, because _A_ has polynomial entries. Hence _X_ is the leading coefficient of a degeneration from _Z_. Reflexivity, transitivity, and rule (i) therefore preserve valid degenerations. Induction on a finite derivation proves the lemma.

On expressions in F_<sub>n</sub>_, these rules include the finite separation used in Section 3. Indeed, take _m=t=M_ in rule (v), and use interpolation on its auxiliary atom. Its rank is

\(D=(n-2)(M-1)+M=(n-1)M-(n-2)\le(2n-1)M.\)

Full distributivity identifies \(A\otimes_K\mathbf{I}_n(D)\) with _D_ full-sum copies of _A_, and block deletion supplies any larger copy budget. Thus the resource form contains the earlier separation comparison, in addition to its variants with arbitrary _m,t_. Type extraction, full sums, products, and the two polynomial comparisons may all be combined within the specified rules. The common-context rule is limited to constructions whose shared coordinates remain fixed.

## 5.3 A comparison function for polynomial lengths

The permitted derivations are now fixed. To show their limitation, we assign positive numbers to their polynomial atoms. The required estimates reduce to a function of the input lengths. Sorting these lengths allows one formula to handle all possible choices of the largest input.

**Definition 5.7** (comparison function)**.** Let \(d\ge 2\) be an integer and let \(\mathbf{a}=(a_1,\dots,a_d)\in[1,\infty)^d\). Write its entries in nondecreasing order as \(b_1\le\cdots\le b_d\). For \(1\le j\le d\), put<tbc>

\(L_j=(d+2-j)b_j+\sum_{i=1}^{j-1}b_i-(d-1),c_j=\frac{2}{(d+1-j)(d+2-j)}.\)

<tbc>Define

\(H_d(\mathbf{a})=\prod_{j=1}^d\left(\frac{L_j}{2}\right)^{c_j}.\)

Repeated entries cause no choice in the sorted list. The function is positive and symmetric.

The next lemma proves the estimates in the order needed by the rules. Coordinate monotonicity handles truncation, separate concavity handles neighboring lengths, and the affine tail of a one-coordinate slice gives shifted tripling. A final estimate supplies the budget for the polynomial resource in Lemma 5.4.

