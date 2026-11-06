Now, based on the input HintedKnapsackExtend<sup>+</sup> instance _K_, we define _k_ new instances _K_<sup>(1)</sup>_,...,K_<sup>(_k_)</sup> as follows: for each \(1\le j\le k\), let<tbc>

\(\mathcal{I}^{(j)}=\big\{i\in\{-L,\dots,L\}:S[i]\text{is isolated by}h_j\text{, but not by any}h_{j^\prime}(j'<j)\big\}.\)

<tbc>Then \(\{\mathcal{I}^{(j)}\}_{j=1}^k\) form a partition of {-_L,...,L_}. Let instance \(K^{(j)}=\big(U,\{Q_w\}_{w\in U},S^{(j)}[],q^{(j)}[]\big)\) be derived from the input instance \(K=\big(U,\{Q_w\}_{w\in U},S[],q[]\big)\) with the following modification:<tbc>

\(S^{(j)}[i]:=\left\{\begin{array}{ c c }
S[i] & i\in\mathcal{I}^{(j)}, \\
\emptyset & \text{otherwise},
\end{array}\right.\)

<tbc>and

\(q^{(j)}[i]:=\left\{\begin{array}{ c c }
q[i] & i\in\mathcal{I}^{(j)}, \\
-\infty & \text{otherwise}.
\end{array}\right.\)

Clearly, max(_K_<sup>(1)</sup>_,...,K_<sup>(_k_)</sup>)=_K_ (see Definition 4.6), so by Lemma 4.7 it suffices to solve each _K_<sup>(_j_)</sup> and obtain solution _Y_ <sup>(_j_)</sup>, and finally the combined solution _Y_ :=max{_Y_ <sup>(1)</sup>_,...,Y_ <sup>(_k_)</sup>} is a correct solution to _K_.

Now we focus on each instance _K_<sup>(_j_)</sup>. The sets _S_<sup>(_j_)</sup>\[_i_\] are isolated by the coloring _h<sub>j</sub>_ (note that there are at most |I<sup>(_j_)</sup>| many non-empty sets _S_<sup>(_j_)</sup>\[_i_\]). So we can iteratively apply the algorithm for singletons (Lemma 4.1) to solve for each color class \(U_c:=h_j^{-1}(c)(c\in[b^2])\), in the same fashion as in the proof of Theorem 3.11. More precisely, starting with instance _K_<sub>1</sub>:=_K_<sup>(_j_)</sup>, we iterate \(c\leftarrow 1,2,\dots,b^2\), and do the following (using notations from Section 4.2):

• Solve the restricted instance (_K<sub>c</sub>_)|<sub>_U<sub>c</sub>_</sub> using Lemma 4.1 in _O(L_+|I<sup>(_j_)</sup>|log_L_) time, and obtain solution _Y<sub>c</sub>_.<tbc>

• Define the updated instance \(K_{c+1}:=(K_c)^{(U_c\leftarrow Y_c)}\).

Finally, return the composed solution \(Y^{(j)}:=Y_{b^2}\circ\cdots\circ Y_2\circ Y_1\). By inductively applying Lemma 4.5, we know _Y_ <sup>(_j_)</sup> is a correct solution to _K_<sup>(_j_)</sup>.

It remains to analyze the time complexity. Each of the _k_ instances _K_<sup>(_j_)</sup> is solved by _b_<sup>2</sup> applications of the singleton-case algorithm (Lemma 4.1) in _O(L_+|I<sup>(_j_)</sup>|log_L_) time each. Hence the total time complexity over all _k_ instances is \(\sum_{j=1}^kb^2\cdot O(L+|\mathcal{I}^{(j)}|logL)=O(kb^2L+b^2\sum_{j=1}^k|\mathcal{I}^{(j)}|logL)=O(Lb^2(k+logL))=O(Lb^2logL)\). Combined with the deterministic coloring step at the beginning, the overall time complexity is _O(Lb_<sup>2</sup>log_L+Lb(b_<sup>2</sup>+log_L_))=_O(Lb_<sup>2</sup>(_b_+log_L_)).

## Acknowledgements

I thank Ryan Williams and Virginia Vassilevska Williams for useful discussions. I thank anonymous reviewers for useful comments on previous versions of this paper.

## References

