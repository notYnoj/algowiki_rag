**Theorem 2** _Let_

\(\bullet\) \(L_a^\bar{a}(w)\) _be the minimized (2) for the alphabetic problem,_<tbc>

\(\bullet\) \(L_a^\bar{h}(w)\) _be that obtained using the **l**_<sup>h</sup>_-based approximation algorithm,_<tbc>

\(\bullet\) \(L_a^\bar{\mathrm{s}}(w)\) _be that obtained using the **l**_<sup>s</sup>_-based approximation algorithm,_<tbc>

\(\bullet\) \(L_a^\mathrm{non}(w)=L_a(w,\mathbf{l}^\mathrm{non})\), \(L_a^\mathrm{s}(w)=L_a(w,\mathbf{l}^\mathrm{s})\)_, and_ \(L_a^\mathrm{h}(w)=L_a(w,\mathbf{l}^\mathrm{h})\) _(using those **l** values from Fig. 3)._<tbc>

<tbc>_Then_

\(H_\alpha(w)\le L_a^\mathrm{h}(w)\le L_a^\bar{\mathrm{a}}(w)\le L_a^\bar{\mathrm{h}}(w)<1+L_a^\mathrm{h}(w)<2+H_\alpha(w)\) (4)

\(H_\alpha(w)\le L_a^\mathrm{h}(w)\le L_a^\bar{\mathrm{a}}(w)\le L_a^\bar{\mathrm{s}}(w)<1+L_a^\mathrm{s}(w)<2+H_\alpha(w)\) (5)

_where_ \(H_\alpha(w)\) _is the Rényi entropy for_ \(\alpha=(1+\mathrm{log}_2a)^{-1}\):

\(H_\alpha(w)=\frac{1}{1-\alpha}\mathrm{log}_2\sum_{i=1}^nw(i)^\alpha=(\mathrm{log}_22a)\left(\mathrm{log}_2\sum_{i=1}^nw(i)^\frac{1}{1+\mathrm{log}_2a}\right)\)

**Proof** This is a corollary of Campbell’s Shannon-like bounds for _a\>_0.5 -- \(H_\alpha(w)\le L_a^\mathrm{h}(w)\le L_a^\mathrm{s}(w)<1+H_\alpha(w)\) -- along with the facts that (a) the two approximation algorithm lengths corresponding to items 1 and _n_ are no greater than those in **_l_**<sup>non</sup> and (b) no other length exceeds the corresponding length in **_l_**<sup>non</sup> by 1 or more. This results in \(L_a^\bar{\mathrm{h}}(w)<1+L_a^\mathrm{h}(w)\) and \(L_a^\bar{\mathrm{s}}(w)<1+L_a^\mathrm{s}(w)\) due to (2), and, since no alphabetic tree is better than the optimal alphabetic tree and no alphabetic tree is better than the optimal Huffman-like tree, we arrive at (4) and (5).

The lower limit to \(L_a^\bar{\mathrm{a}}(w)\) is satisfied by (2,2), while the upper limit is approached by \((\epsilon,1-2\epsilon,\epsilon)\), which approaches entropy 0 and penalty 2.

Both these algorithms and the bounds due to analogous inequalities apply to _a\>_1 and to the traditional alphabetic problem (\(a\rightarrow 1\), where _H_<sub>1</sub> is Shannon entropy \[3\]). For the traditional problem, due to Step 4, the Huffman- based approximation version of the above algorithm is a strict improvement on Yeung’s Huffman-based approximation \[11\].

## Acknowledgments

The author would like to thank T. C. Hu and J. David Morgenthaler for discussions and encouragement on this topic.

