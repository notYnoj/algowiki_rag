Theorem 5.11 in Subsection 5.4 proves this statement and its asymptotic version with subexponential overhead and common auxiliary factors. We next describe the certificate and explain how it accounts for each ingredient of the polynomial method.

**Formal expressions and their numerical values.** An expression records how its tensor is constructed, including the coordinates shared in a partial direct sum. Its atoms are reflected polynomial tensors: the expression C_<sub>n</sub>(a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>) evaluates to C_<sub>n</sub>(a_<sub>1</sub>_,...,a_<sub>_n_-1</sub>) after reversing the output coordinate. Definitions 5.1 and 5.2 specify these atoms and the set F_<sub>n</sub>_ of expressions. Besides full sums and Kronecker products, an expression may use \(X\boxdash_eY\) , which shares the coordinates outside the two legs in _e_ and uses disjoint matched sectors on those two legs. Its coordinate meaning is given in Definition 2.9. Distinct expressions remain distinct even when they evaluate to isomorphic tensors. Lemma 5.6 verifies that every permitted derivation gives a valid tensor degeneration.

For the rest of this overview, fix \(n\ge 3\), and put _d=n_-1 and \(\eta_n=n/(2(n-1))\). The certificate V_<sub>n</sub>_ from Definition 5.9 assigns a positive real number to each expression. Full sums and products receive ordinary sums and products of values, whereas a partial sum receives a different power sum:

\(\mathcal{V}_n(X\oplus_KY)=\mathcal{V}_n(X)+\mathcal{V}_n(Y),\)<br>
\(\mathcal{V}_n(X\otimes_KY)=\mathcal{V}_n(X)\mathcal{V}_n(Y),\)<br>
\(\mathcal{V}_n(X\boxdash_eY)=\left(\mathcal{V}_n(X)^{1/\eta_n}+\mathcal{V}_n(Y)^{1/\eta_n}\right)^{\eta_n}.\)

These formulas apply whenever the expressions are defined. The choice of \(\eta_n\) will make the cost of separating shared coordinates agree with the value of the edge retained by separation. The remaining task is to assign values to the polynomial atoms so that every permitted rule preserves the required inequality.

**A comparison function for all input lengths.** For \(\mathbf{a}=(a_1,\dots,a_d)\in[1,\infty)^d\), sort the entries as \(b_1\le\cdots\le b_d\). Definition 5.7 introduces

\(L_j=(d+2-j)b_j+\sum_{i=1}^{j-1}b_i-(d-1),c_j=\frac{2}{(d+1-j)(d+2-j)}(1\le j\le d),\)<br>
\(H_d(\mathbf{a})=\prod_{j=1}^d\left(\frac{L_j}{2}\right)^{c_j}.\)

For positive integer input lengths, set \(\mathcal{V}_n(\mathsf{C}_n(\mathbf{a}))=H_d(\mathbf{a})^{\eta_n}\). For a general atom, remove one largest leg dimension and apply the same formula to the remaining dimensions. This assignment is invariant under permutations of the legs. For _n_=3, it recovers the symmetric certificate of \[ABZ26, Equation (5.3)\].

The factors in _H<sub>d</sub>_ are chosen to handle both changes of input length and changes of their sorted order. Within each fixed order, differentiation proves monotonicity and concavity in each coordinate. When two entries cross, the first derivatives agree. Thus the same properties hold across all sorting intervals. Once one coordinate exceeds the others, _H<sub>d</sub>_ is affine in that coordinate, with the offset needed for shifted tripling. Lemma 5.8 proves these facts, together with<tbc>

\(H_d(\mathbf{a})\le\prod_{i=1}^da_i,H_d(\mathbf{a})^{\eta_n}\le 1+\sum_{i=1}^d(a_i-1).\)

<tbc>The first bound accounts for the rule that constructs a polynomial tensor from a star of edge tensors; the second accounts for interpolation. Concavity and shifted tripling give the<tbc>

