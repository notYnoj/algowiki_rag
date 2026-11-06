2. Let \(n':=\mathrm{log}n\). Interpret _A_ as \(n/n'\) super-pieces, each super-piece consists of \(n'\) elements. For each super-piece, recursively call \(\mathbf{TC}_{n^\prime,w}\) to sort \(n'\) elements in the super-piece. Let _B_ be the concatenation of all resulting super-pieces.<tbc>

3. Let \(m':=(\mathrm{log}n)^{1/3}\). Interpret _B_ as \(n/m'\) pieces, each piece consists of \(m'\) elements. For each piece, identify itself as 0-, 1-, or mixed-piece, where 0-piece consists of only 0-elements, and 1-piece consists of only 1-elements. Notice that there are at most \(n/n'\) mixed-pieces.<tbc>

4. Invoke \(\mathbf{LargeTC}_{n/m^\prime,w\cdot m^\prime}\) so that all 0-pieces are moved to the front, and similarly all 1-pieces are moved to the back. Invoke \(\mathbf{LargeTC}_{n/m^\prime,w\cdot m^\prime}\) so that all mixed-pieces are moved to a short scratch array which consists of \((n/n')\cdot m'=n/(m')^2\) elements.<tbc>

5. Invoke \(\mathbf{LargeTC}_{n/(m^\prime)^2,w}\) so that all elements in the scratch array are sorted.<tbc>

6. Merge the sorted scratch array elements with those 0- and 1-pieces using another \(\mathbf{LargeTC}_{n/m^\prime,w\cdot m^\prime}\) on pieces. Output the merged array.

We claim the following.

**Theorem C.5.** _Suppose_ **LargeTC**_<sub>n,w</sub> is a correct tight compaction and takes circuit size_ \(O(nw+n\cdot\mathrm{loglog}n)\) _and depth O_(log_n). Then,_ **TC**_<sub>n,w</sub> is a correct tight compaction that sorts n elements each with w-bit payload, takes circuit size_ \(O(nw\cdot(1+\mathrm{log}^*n-\mathrm{log}^*w))\) _and depth O_(log_n)._

_Proof._ Correctness follows inductively: the base case is correct by **LargeTC**, and then other cases follows as we correctly sort 0- and 1-pieces in Step 4 and mixed-pieces in Step 5. Next, we focus on the circuit size and depth.

The circuit size is<tbc>

\(S(n,w)=\left\{\begin{array}{ c c }
(n/\mathrm{log}n)\cdot S(\mathrm{log}n)+4S_{\mathbf{LargeTC}_{n/m^\prime,w\cdot m^\prime}}+S_{\mathbf{LargeTC}_{n/(m^\prime)^2,w}} & \mathrm{loglog}n>w \\
O(n\cdot w) & \mathrm{loglog}n\le w
\end{array}\right..\)

<tbc>By Theorem C.3, we have

\(4S_{\mathbf{LargeTC}_{n/m^\prime,w\cdot m^\prime}}+S_{\mathbf{LargeTC}_{n/(m^\prime)^2,w}}=4\cdot O(nw+2n)+O(nw+2n)=O(nw)\)

for all _n\>_2<sup>2</sup><sup>3</sup> since \(m'=(\mathrm{log}n)^{1/3}>(1/2)\mathrm{loglog}n\) for all _n\>_2<sup>2</sup><sup>3</sup>. Because the recursive call to **TC** itself reduces the problem size to log_n_ at Step 2, the recursion reaches the base case at depth log<sup>∗</sup>_n_-log<sup>∗</sup>_w_. Then the total circuit size \(O(nw\cdot(1+\mathrm{log}^*(n)-\mathrm{log}^*(w)))\) follows by a simple summation over each recursion depth.

To calculate the circuit depth, observe that "for each piece/super-piece" steps in the procedure are all performed in parallel, and that only **LargeTC** and identifying 0, 1, or mixed pieces take depth _O_(log_n_). Moreover, for each recursion depth _i_, **LargeTC** and the identification work on at most _n<sub>i</sub>_ items, where _n<sub>i</sub>_=log<sup>(_i_)</sup>_n_ denotes the number of elements in the input of the recursive call **TC**. Hence, the total depth is

\(D(n)=\sum_{i=0}^{\mathrm{log}^*(n)-\mathrm{log}^*(w)}O(\mathrm{log}n_i)=O(\mathrm{log}n).\)

**Putting everything together.** By plugging Theorem C.3 into **LargeTC**, we obtain Theorem C.5 as claimed. Then, plugging Theorem C.5 into our 1-bit to _k_-bit upgrade (described in Section 15), we get Theorem C.1.

