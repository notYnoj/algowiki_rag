<tbc>algorithm and they collide over the carry bits is \(\Theta(1/(p^4q^2\sqrt{n}))\). Combining this result and using the Local Central Limit Theorem again for the remaining bits, we have \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathrm{int})}\right)=\Omega(1/(np^4q^2r))\). Since there are \(\Theta(4^n)\) pairs of binary vectors such that their Hamming weights satisfy _certain_ specific conditions (mentioned in Section 7), we have \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathrm{int})}\right)=\Omega(1/n)\).

## Second moment.

At this point, we know that the expected number of collisions is positive (and in the modular case, even bounded away from 0). However, a lower bound on E\[C\] alone does not imply that the algorithm succeeds on a typical input. Indeed, a random variable can have expectation 1 while being 0 with overwhelming probability and very large on a tiny exceptional set. Thus, the first moment identifies only the correct _scale_ of the number of collisions; by itself, it _does not_ yield a lower bound on P\[C_\>_0\].

Therefore, to prove that the filtering algorithm succeeds with substantial probability, it is essential to control the second moment of C. This is precisely why our analysis focuses on bounding E\[C<sup>2</sup>\], and, in the integer case, why we first pass through the more tractable modular variable C<sup>(_pqr_)</sup> in Section 6.

As discussed above, analyzing \(\mathcal{C}_{ij}^{(\mathrm{int})}\) directly is challenging because of the interaction between pseudo-uniform distributions and carry propagation. In particular, obtaining a useful upper bound on its second moment appears substantially _more delicate_ than in the modular setting. However, since \(\mathcal{C}_{ij}^{(\mathrm{int})}\le\mathcal{C}_{ij}^{(\mathrm{pqr})}\) and our goal is to upper-bound the second moment, it is enough to study the second moment of \(\mathcal{C}_{ij}^{(\mathrm{pqr})}\) instead!<sup>9</sup> This modular quantity is considerably more tractable, since it can be analyzed using the structural advantages of the Chinese Remainder Theorem and modular arithmetic. Thus, the modular case is not merely a warm-up: it provides the key input for controlling the second moment, and hence the success probability, in the integer setting.

Next, we explain how to compute the second moment C<sup>(pqr)</sup>. The second moment of C<sup>(pqr)</sup> can be written as follows (we replace C<sup>(pqr)</sup> with C for the ease of presentation):

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)=\mathbb{E}_\mathbf{a}\left(\sum\mathcal{C}_{ij}\cdot\sum\mathcal{C}_{\ell k}\right)\)<br>
\(=\sum_{i<j,\ell<k}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\cdot\mathcal{C}_{\ell k}\right)\)<br>
\(=\sum_{(i,j)\neq(\ell,k)}\mathbb{P}_\mathbf{a}\left(\mathcal{C}_{ij}=1\wedge\mathcal{C}_{\ell k}=1\right)+\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)\)

The main difficulty in analyzing the second moment stems from dependencies between events induced by linear relationships among the binary vectors.

To address this issue, we partition the set _S_ of all possible 4-tuples of binary vectors into cells such that, for every tuple within a given cell, the joint probability \(\mathbb{P}_\mathbf{a}(\mathcal{C}_{ij}=1\wedge\mathcal{C}_{\ell k}=1)\), admits a uniform upper bound, while the size of each cell can also be tightly bounded. This structured partitioning allows us to control the contribution of dependent events to the second moment. The construction and analysis of these cells rely on a combination of linear-algebraic and combinatorial techniques. After analyzing all these dependencies, we get the desired result that \(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^2\right)=\mathcal{O}(1)\) (see Section 6 for details).

<sup>9</sup>In principle, the relevant moments in the modular case can also be approached using exponential sums. However, this becomes convoluted at the level of the second moment, so we instead adopt an algebraic approach. We expect that a more refined use of exponential sums could potentially improve the success probability by exploiting additional randomness in the filtering algorithm.

