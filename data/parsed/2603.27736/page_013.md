most general form of Theorem 1.18 (which is necessary e.g. for the doubling reduction) we are forced to open up their algorithm, recast it in a restricted framework of reductions (so-called _potential-adjusting_ reductions to be defined in Section 2.3), and generalize all steps to rectangular matrices. Fortunately, along the way we manage to simplify one of the highly technical steps in \[4\] (again leveraging the expressiveness of the novel select-plus rank), and in doing so, we even obtain a slightly faster APSP algorithm for the few-weights case.<sup>9</sup>

As in \[4\], our subcubic-time algorithm also works for the strictly harder low-rank _Exact Triangle_ problem. In this problem we are additionally given a matrix _C_, and the goal is to report all entries in the min-plus product _A∗B_ that coincide with _C_. We now describe the key insights behind this algorithm for low-rank Exact Triangle.

## Main Idea: Reduction to Slice-Uniform Instances.

Let (_A,B,C_) be a given Exact Triangle instance with select-plus rank \(r(C)\le r\). Let \(C_\ell\) denote the submatrix of _C_ consisting of all entries that are captured by the \(\ell\)-th part of the rank decomposition (i.e., \(C[i,j]=U[i,\ell]+V[\ell,j]\)), where all other entries are replaced by some dummy symbol \(\perp\). Our strategy is to iteratively solve the subinstances (_A,B,C_<sub>1</sub>)_,...,(A,B,C<sub>r</sub>_) one- by-one. As we aim for total time \(O(n^{3-\epsilon})\), each such subinstance must be solved in time \(O(n^{3-\epsilon}/r)\). Recall that the most interesting case is when _r_ is very close to _n_, so this time budget is just barely superquadratic. Focus on an instance \((A,B,C_\ell)\), and define matrices \(A',B'\) by

\(A'[i,k]=A[i,k]-U[i,\ell],\)<br>
\(B'[k,j]=-(B[k,j]-V[\ell,j]).\)

Then any exact triangle \(A[i,k]+B[k,j]=C_\ell[i,j]\) corresponds to a solution of the much simpler equality condition \(A'[i,k]=B'[k,j]\). This remaining problem is typically called _Equality Product_ (where in our case the set of relevant outputs is only the non-\(\perp\) entries in \(C_\ell\)). Up to this point the algorithm can be seen as the "Fredman’s trick" part of the "Fredman’s trick meets dominance product" technique \[35\]. Next, this technique would solve the Equality Product instances each in time \(\tilde{O}(n^{(3-\omega)/2})\) by Matoušek’s algorithm \[79\] applied as a black-box. This running time is too slow for our purposes, so from now on our algorithm differs.

Matoušek’s algorithm can be viewed as a simple heavy/light trick, so it is natural to proceed similarly. Call an entry in \(A'\) _light_ if in its respective column in the same integer entry appears at most \(n^{1-\epsilon}/r\) times, and _heavy_ otherwise. This threshold is chosen in such a way that a simple brute-force algorithm can deal with instances containing _no_ heavy entries in our time budget, \(O(n^{3-\epsilon}/r)\).

More interestingly, consider the other extreme where _all_ entries in \(A'\) are heavy. If we ever reach this situation then we will "give up" on the iterative algorithm, go back to the original instance (_A,B,C_), and solve it in one shot. How? Let \(C'\) be the matrix defined by

\(C'[i,j]=C[i,j]-U[i,\ell].\)

This is chosen in a way that the instances (_A,B,C_) and \((A',B,C')\) are exactly equivalent (as the term \(U[i,\ell]\) cancels in \(A'[i,k]+B[k,j]=C'[i,j]\)). It thus suffices to solve the augmented instance \((A',B,C')\). The benefit is that the augmented instance satisfies the extra constraint that each column in \(A'\) contains a truly sublinear number \(d\le r\cdot n^\epsilon\) of distinct entries (as each heavy entry repeats at least \(n^{1-\epsilon}/r\) times per column in \(A'\)). This is exactly the _d-slice-uniform_ special case known to be in subcubic time due to Abboud, Fischer, Jin, Vassilevska W., and Xi \[4\].

## Technical Challenge: Regular Rank Decompositions.

Unfortunately, the previous paragraph just treats the unrealistic situations that either _no_ or _all_ entries are heavy--but what if only _some_ entries are heavy? This remaining case poses some serious technical challenges. Our solution involves two subcases. The good subcase is when the number of heavy entries is still quite large, say at least \(n^{2-\delta}\) for some<tbc>

<sup>9</sup>To be precise, the previously fastest APSP algorithm with at most \(n^{3-\omega-\epsilon}\) distinct edge weights per node \[4\] runs in subcubic time \(O(n^{3-\Omega_\epsilon(1)})\) where the hidden dependence on \(\epsilon\) is polynomial. This unusual dependence is due to a complicated recursion. In our newer version we obtain a more streamlined recursion leading to a linear dependence \(\Omega(\epsilon)\) as in Theorem 1.18.

