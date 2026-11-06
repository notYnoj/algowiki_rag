**Proposition 3.2.** _For any fixed_ \(\omega>0\) _there exists a polynomial-time algorithm which for a tree T computes a sequence assignment_ \(R:V\rightarrow V^*\)_, such that, for any strategy_ A_<sub>S</sub> based on a stable sequence assignment S, the sequence assignment S_<sup>+</sup>_, given by_ \(S^+(v)=R(v)\circ S(v)\) _for each_ \(v\in V\) _, has the following property:_

\(\mathtt{COST}_{\mathcal{A}_{S^+}}(T)\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)+4(2c+1)\omega log_2n.\)

The proof of Proposition 3.2 is provided in Section 5.

We are now ready to put together the two bounds. Combining the claims of Proposition 3.1 for \(L=\lceil c^2log_2n\rceil\) (with \(\omega\le\frac{1}{L}\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\le\frac{\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)}{c^2log_2n}\) ) and Proposition 3.2, we obtain:

\(\mathtt{COST}_{\mathcal{A}_{S^+}}(T)\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)+4(2c+1)\omega log_2n\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)+12c\omega log_2n\le\)<br>
\(\le\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)+12clog_2n\frac{\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)}{c^2log_2n}\le\left(1+\frac{12}{c}\right)\mathtt{COST}_{\mathcal{A}_S}^{(\omega,c)}(T)\le\)<br>
\(\le\left(1+\frac{12}{c}\right)^2\mathtt{OPT}(T)\le\left(1+\frac{168}{c}\right)\mathtt{OPT}(T).\)

After putting \(\varepsilon=\frac{168}{c}\) and noting that in stating our result we can safely assume _c=O_(poly(_n_)) (beyond this, the tree search problem can be trivially solved optimally in _O(n<sup>n</sup>_) time using exhaustive search), we obtain the main theorem of the Section.

**Theorem 3.3.** _There exists an algorithm running in_ \(n^{O\left(\frac{logn}{\varepsilon^2}\right)}\) _time, providing a_ \((1+\varepsilon)\)_-approximation solution to the weighted tree search problem for any_ \(0<\varepsilon<1\).

## 3.2 Extension: A Poly-Time \(O(\sqrt{logn})\)-Approximation Algorithm

We now present the second main result of this work. By recursively applying the previously designed QPTAS (Theorem 3.3), we obtain a polynomial-time \(O(\sqrt{logn})\)-approximation algorithm for finding search strategy for an arbitrary weighted tree. We start by informally sketching the algorithm -- we follow here the general outline of the idea from \[7\]. The algorithm is recursive and starts by finding a minimal subtree _T_<sup>∗</sup> of an input tree whose removal disconnects _T_ into subtrees, each of size bounded by \(n/2^{\sqrt{logn}}\). The tree _T_<sup>∗</sup> will be processed by our optimal algorithm described in Section 3.1. This results either in locating the target node, if it belongs to _T_<sup>∗</sup>, or identifying the component of _T-T_<sup>∗</sup> containing the target, in which case the search continues recursively in the component. However, for the final algorithm to have polynomial running time, the tree _T_<sup>∗</sup> needs to be of size \(2^{O(\sqrt{logn})}\). This is obtained by contracting paths in _T_<sup>∗</sup> (each vertex of the path has at most two neighbors in _T_<sup>∗</sup>) into single nodes having appropriately chosen weights. Since _T_<sup>∗</sup> has \(2^{O(\sqrt{logn})}\) leaves, this narrows down the size of _T_<sup>∗</sup> to the required level and we argue that an optimal search strategy for the ‘contracted’ _T_<sup>∗</sup> provides a search strategy for the original _T_<sup>∗</sup> that is within a constant factor from the cost of _T_<sup>∗</sup>.

A formal exposition and analysis of the obtained algorithm is provided in Section 6.

**Theorem 3.4.** _There is a_ \(O(\sqrt{logn})\)_-approximation polynomial time algorithm for the weighted tree search problem._

