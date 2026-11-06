# Faster Algorithms for Induced Patterns

15

### A An example finding 4-paths in Bull graph B

For the homomorphism polynomial, \(Hom_{P_4,\mathcal{B}}((y_v)_{v\in V(\mathcal{B})})\), consider variables \(y_v\in R\), where _R_ is a commutative ring with characteristic char(_R_)=2, and _y_<sup>2</sup>=0 for all \(y\in R\). The automorphism group of _P_<sub>4</sub> has two elements, the identity and the reversal 1-2-3-4 \(\leftrightarrow\) 4-3-2-1. Therefore, each homomorphism from _P_<sub>4</sub> to B contributes a coefficient of 2 to the corresponding monomial in the homomorphism polynomial. Since we are working over a ring of characteristic 2, all coefficients are even and hence vanish identically over _R_. The even number of

automorphisms of _P_<sub>4</sub> can be eliminated by imposing the condition \(\phi(2)<\phi(3)\) on the homomorphisms \(\phi:V(P_4)\mapsto V(\mathcal{B})\). The four types of monomials present in the homomorphism polynomial are as follows:

#### Homomorphisms onto a single edge.

If all three edges of _P_<sub>4</sub> (i.e., 1-2, 2-3, 3-4) map onto the same edge \((i,j)\in E(\mathcal{B})\), the contribution is

\(\sum_{(i,j)\in E(\mathcal{B})}2y_i^2y_j^2.\)

Since this term carries a square factor \(y_i^2\), it vanishes identically over _R_.

#### Homomorphisms onto a 2-edge walk.

If the image of _P_<sub>4</sub> revisits a vertex, for example, 1-2-3-4 \(\mapsto\) _a-b-c-a_, the resulting monomial still contains a repeated (squared) variable, and hence again vanishes due to the property of the ring R.

#### Homomorphisms where P_<sub>4</sub> _embeds as a subgraph._

When the image of _P_<sub>4</sub> is an actual (injective) subgraph of B, no variable is repeated, and the resulting monomial is multilinear, these are the terms in the homomorphism polynomial which can contribute to induced subgraph counting.

For example, take 1-2-3-4 \(\mapsto\) _a-b-e-d_. The automorphism group of _P_<sub>4</sub> (reversal, 1-2-3-4 \(\leftrightarrow\) 4-3-2-1) maps this to the same image, contributing the term _y<sub>a</sub>y<sub>b</sub>y<sub>e</sub>y<sub>d</sub>_ with coefficient 2. Because B contains the extra edge _b-e_, there is a second homomorphism, 1-2-3-4 \(\mapsto\) _b-a-e-d_, which (together with its own reversal) contributes the same monomial _y<sub>a</sub>y<sub>b</sub>y<sub>e</sub>y<sub>d</sub>_ with coefficient 2 as well. Combining

a
1
2
3
4
P4
Bull graph

