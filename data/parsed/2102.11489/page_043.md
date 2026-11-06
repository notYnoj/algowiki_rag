3. _Swap._ Call \(\widehat{\mathbf{Swap}^n}(\mathbf{X})\) (to be defined below) to swap almost all the `blue` elements each with a `red` element -- here we use a payload of size _w_+1 and not _w_ as we also include the distinguished-indicator as part of the payload. Return the outcome.

\(\widehat{\mathbf{Swap}^n}(\mathbf{X})\) is defined in a very similar to the **Swap**_<sup>n</sup>_ algorithm of Theorem 9.3; except that now, we simply use a lossy loose compactor to extract the residual `red` and `blue` elements, and then recurse on the extracted array. In comparison, in the earlier **Swap**_<sup>n</sup>_ algorithm, we used a lossy loose compactor to extract `blue` elements and used a near-sorter to extract the `red` elements.

\(\widehat{\mathbf{Swap}^n}(\mathbf{X})\)<br>
\(\bullet\) **Input:** An array **X** of \(m\le n\) elements, each has a _w_-bit payload<sup>9</sup>and a 2-bit label indicating whether the element is colored, and if so, whether the element is `blue` or `red`. _n_ is the size of the original problem when **Swap** is first called; the same _n_ will be passed into all recursive calls since it is used to decide when the recursion stops.<br>
\(\bullet\) **Algorithm:**<br>
(a) _Base case._ Same as Step (a) of the earlier **Swap**_<sup>n</sup>_ of Theorem 9.3.<br>
(b) _Approximate swapper._ Same as Step (b) of the earlier **Swap**_<sup>n</sup>_ of Theorem 9.3; recall that the resulting array is denoted as \(\mathbf{X}'\).<br>
(c) _Lossy-extract colored._ Call an \((\alpha,m,w+1)\)-lossy loose compactor to compact \(\mathbf{X}'\) by a half, where the lossy loose compactor treats the colored elements as real, and all other elements as fillers (i.e., the loose compactor treats the first bit of the color label as a real- filler indicator, and the second bit of the color label is treated as part of the payload).<br>
Let the outcome be **Y** whose length is half of **X**.<br>
(d) _Recurse._ Recursively call \(\widehat{\mathbf{Swap}^n}(\mathbf{Y})\), and let the outcome be \(\mathbf{Y}'\).<br>
(e) _Reverse route._ Reverse the routing decisions made by all selector gates during Steps (c) (see Remark 4 in the proof of Theorem 9.3). In this way, we can reverse-route elements in \(\mathbf{Y}'\) to an array (denoted \(\widetilde{\mathbf{X}}\)) whose length is _m_.<br>
(f) _Output._ Return **O** which is formed by a performing coordinate-wise select operation between \(\mathbf{X}'\) and \(\widetilde{\mathbf{X}}\). For every \(i\in[m]\):<br>
- if \(\mathbf{X}'[i]\) originally had a colored element and the element was not lost during Step (c), then let \(\mathbf{O}[i]:=\widetilde{\mathbf{X}}[i]\);<br>
- else let \(\mathbf{O}[i]:=\mathbf{X}'[i]\);

Suppose that _n_ is sufficiently large. Then, the recursive call will hit the base case after at most \(\left\lceil log_{1.9}\frac{1}{\alpha}\right\rceil\) steps of recursion.

**Fact 12.2.** _Assume that n is greater than a sufficiently large constant. The remaining number of colored elements at the end of the algorithm is at most_ \(8\alpha n\).

_Proof._ The total number of elements lost during Step (c) of the algorithm is upper bounded by \(\alpha n+\alpha n/1.9+\alpha n/1.9^2\dots\le 3\alpha n\). Also, the recursion stops when \(m\le\alpha n\), all remaining colored elements will not get swapped. Therefore, the total number of colored elements remaining at the end is upper bounded by \(2\cdot 3\alpha n+\alpha n<8\alpha n\), where the factor 2 comes from the fact that we may lose all \(3\alpha n\) in `blue` color and thus there are another \(3\alpha n\) in `red`.

Our approximate tight compaction algorithm actually requires a swapper where elements are of bit-length _w_+1, but for convenience we rename the variable to _w_ in the description of the swapper.

