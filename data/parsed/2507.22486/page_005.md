our algorithm. The algorithm computes an \(\mathsf{LIS}\) of \(\mathsf{Project}(y,\pi)\), with respect to \(\pi\). This LIS is also a common subsequence of _x_ and _y_, and is considered as a candidate for the output.

The third part of the algorithm iteratively finds \(\pi'\), an approximate longest decreasing subsequence of _x_ with respect to \(\pi\). As in the second part, the algorithm interprets \(\pi'\) as a total order over the symbols of \(\pi'\), and computes an LIS of \(\mathsf{Project}(y,\pi')\), with respect to \(\pi'\), as a candidate. At the end of the iteration, the algorithm removes all occurrences of symbols in \(\pi'\) from _x_, and halts if _x_ becomes empty. Finally, the algorithm returns the longest candidate found throughout all three parts.

In the pseudo-code below, we use the following notation. For two sequences _L_ and \(L'\), the notation \(L\leftarrow^\mathrm{max}L'\) means that if \(|L'|>|L|\), then _L_ is updated to \(L'\); otherwise, _L_ remains unchanged. In addition, we use the notation \(\mathsf{ALDS}_\pi(x)\) to denote a 2-approximation of \(\mathsf{LDS}_\pi(x)\) obtained by Lemma 4.

**Algorithm 1** Approx-LCS(_x,y_)

`// Part 1: Best match;`<br> \(L\leftarrow\mathsf{BestMatch}(x,y)\);<br> `// Part 2: LIS with respect to` \(\pi\)`;`<br> \(\pi\leftarrow\mathsf{RF}(x)\);<br> \(L\leftarrow^\mathrm{max}\mathsf{LIS}_\pi(y)\);<br> `// Part 3: Greedy LDS peeling of` _x_`;`<br> **while** \(x\neq\emptyset\) **do**<br> \(\pi'\leftarrow\mathsf{ALDS}_\pi(x)\);<br> \(L\leftarrow^\mathrm{max}\mathsf{LIS}_{\pi^\prime}(y)\);<br> \(x\leftarrow\mathsf{Exclude}(x,\pi')\);<br> **return** _L_`;`

Running Time We describe how to implement Algorithm 1 in near-linear time. Com puting BestMatch(_x,y_) in Line 1 can be implemented in \(\tilde{O}(n)\) time straight-forwardly. Computing \(\pi=\mathsf{RF}(x)\) in Line 2 is also trivial to implement in \(\tilde{O}(n)\) time. Finding \(\mathsf{LIS}_\pi(y)=\mathsf{LIS}_\pi(\mathsf{Project}(y,\pi))\) is implemented by straightforwardly finding \(\mathsf{Project}(y,\pi)\) in \(\tilde{O}(|y|+|\pi|)=\tilde{O}(|y|+|x|)=\tilde{O}(n)\) time, and then applying a near-linear time LIS algorithm to obtain \(\mathsf{LIS}_\pi(\mathsf{Project}(y,\pi))\).

We proceed to describe how to implement the while loop in Line 4. An efficient computation of this loop boils down to developing an efficient data structure for finding all occurrences of a given symbol \(\sigma\) in _x_ and in _y_. Since _x_ undergoes deletions throughout the algorithm, this data structure needs to support symbol deletion as well. We introduce the data structure in the following simple lemma, which is proved for the sake of completeness in Appendix A.

\(\blacktriangleright\) **Lemma 6.** _There exists a data structure maintaining a dynamic sequence x supporting the following operations:_

\(\blacksquare\) `Init(_x_) - initialize the data structure; runs in` \(\tilde{O}(|x|)\) _time._`

\(\blacksquare\) `Occ(\(\sigma\)) - returns all the indices in which the symbol` \(\sigma\) _occur, i.e.,_ \(\{i|x_i=\sigma\}\)_; runs in_ \(\tilde{O}(\#_\sigma(x))\) _time._`

\(\blacksquare\) `Delete(_i_) - deletes the ith element of x; runs in` \(\tilde{O}(1)\) _time._`

We now proceed to describe the implementation of the while loop. We begin by initializing the data structure _D_LIS from Lemma 4 for _x_ with respect to the order \(\pi\), as well as two instances of the data structure from Lemma 6: \(D_\mathsf{Occ}^x\) for _x_ and \(D_\mathsf{Occ}^y\) for _y_.

\(\blacksquare\) `Init(_x_) - initialize the data structure; runs in` \(\tilde{O}(|x|)\) _time._`

\(\blacksquare\) `Occ(\(\sigma\)) - returns all the indices in which the symbol` \(\sigma\) _occur, i.e.,_ \(\{i|x_i=\sigma\}\)_; runs in_ \(\tilde{O}(\#_\sigma(x))\) _time._`

