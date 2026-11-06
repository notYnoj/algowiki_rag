<tbc>depicted with blanks for 0s and bullets for 1s. See Section 2 for explicit definitions regarding 0-1 matrices.) For example, if \(\pi=(1,3,2,4)\), ordering rows from bottom to top:

\(P_\pi=\left(\begin{array}{ c c }
\bullet & \bullet \\
\bullet & \bullet
\end{array}\right)Q=P_\pi\otimes(\bullet)=\left(\begin{array}{ c c c }
\bullet & \bullet & \bullet \\
\bullet & \bullet & \bullet \\
\bullet & \bullet & \bullet \\
\bullet & \bullet & \bullet
\end{array}\right)\)

If _X_ is a fixed 0-1 pattern matrix, define Ex(_X,n_) be the maximum number of 1s in an \(n\times n\) matrix that avoids _X_. Thus, the running time of \[CGK<sup>+</sup>15b\] can be bounded in terms of Ex(_Q,n_) without knowing exactly what it is.

**Theorem 1.1** (Chalermsook, Goswami, Mehlhorn, Kozma, and Saranurak \[CGK<sup>+</sup>15b\])**.** _If S is_ \(\pi\)_-free, BST Sort using_ GreedyFuture _sorts S in O_(Ex(_Q,n_)) _time, where_ \(Q=P_\pi\otimes(\bullet)\).

Observe that _Q_ is a \(2k\times 3k\) _light_ pattern: it contains exactly one 1 per column. There is a well known connection between light patterns and generalized Davenport-Schinzel sequences \[Kla92, FH92, Kes09, Pet11b, Pet15b\]. Applying a simplifying transformation that collapses the first two rows \[FH92, Thm. 2.2\] and then \[Pet15b, Thm. 1.3\], we have the following general upper bound, where \(\alpha(n)\) is the inverse-Ackermann function.

\(\mathrm{Ex}(Q,n)\le\left\{\begin{array}{ c c }
2n\alpha(n)+O(n) & k=2 \\
n\cdot 2^{(1+o(1))\alpha^t(n)/t!} & k\text{odd},t=(3k-5)/2 \\
n\cdot(\alpha(n))^{(1+o(1))\alpha^t(n)/t!} & k\text{even},t=(3k-6)/2
\end{array}\right.\) (1)

Thus, by Theorem 1.1, GreedyFuture sorts _S_ in \(O(n\cdot 2^{\alpha(n)^{3k/2-O(1)}})\) time. On the lower bound side, we know that \(\mathrm{Ex}(Q,n)=\Omega(n\alpha(n))\) as every _Q_ contains one of the two patterns shown below, which are associated with order-3 Davenport-Schinzel sequences \[HS86, FH92\].

\(\left(\begin{array}{ c c }
\bullet &  \\
\bullet & \bullet
\end{array}\right)\left(\begin{array}{ c c }
\bullet &  \\
\bullet & \bullet
\end{array}\right)\)

The Greedy algorithm is theoretically attractive, but cumbersome to implement online as GreedyFuture \[DHI<sup>+</sup>09\]. Kozma and Saranurak \[KS20\] introduced a new heap data structure called a SmoothHeap, and proved Heap Sort with SmoothHeap is _equivalent_ to BST Sort with Greedy. Moreover, SmoothHeap is "naturally" an online algorithm, and is easier to implement than GreedyFuture. One can define an \(n\times n0\)-1 matrix _A_<sub>SmoothHeap(_S_)</sub> in the same way, where _A_<sub>SmoothHeap(_S_)</sub>(_i,j_)=1 iff the _i_th Delete-Min touches the element with rank _j_. It is proved that _A_<sub>SmoothHeap</sub> avoids a matrix equivalent to _Q_.<sup>2</sup>

**Theorem 1.2** (Kozma and Saranurak \[KS20\])**.** _If S is_ \(\pi\)_-free, Heap Sort using_ GreedyFuture _sorts S in O_(Ex(_Q,n_)) _time, where_ \(Q=P_\pi\otimes(\bullet)\).

<sup>2</sup>Strictly speaking the equivalence between Greedy and SmoothHeap swaps the roles of time and space. Sorting _S_ with Greedy is isomorphic to sorting _S<sup>T</sup>_ with SmoothHeap, where _S<sup>T</sup>_ is the transpose permutation: \(S(i)=j\Leftrightarrow S^T(j)=i\). Note that _S<sup>T</sup>_ avoids \(\pi^T\). Since the extremal functions for _Q_ and _Q<sup>T</sup>_ are identical on square matrices, we infer that the time to sort _S<sup>T</sup>_ is also _O_(Ex(_Q,n_)).

