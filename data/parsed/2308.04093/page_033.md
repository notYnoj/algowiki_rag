<tbc>|_U_|log_r_) time a coloring \(h:U\rightarrow[r]\), such that for every \(i\in\{-L,\dots,L\}\) and every color \(c\in[r]\), \(S[i]\cap h^{-1}(c)\le b_1\) for some _b_<sub>1</sub>=_O_(log_L_).

Then, we iteratively apply the algorithm from Lemma 4.8 with size bound _b_<sub>1</sub>, to solve for each color class \(U_c:=h^{-1}(c)(c\in[r])\). More precisely, let _K_ denote the input HintedKnapsackExtend<sup>+</sup> instance, and starting with instance _K_<sub>1</sub>:=_K_, we iterate \(c\leftarrow 1,2,\dots,r\), and do the following (using notations from Section 4.2):

• Solve the restricted instance (_K<sub>c</sub>_)|<sub>_U<sub>c</sub>_</sub> using Lemma 4.8 (with size bound _b_<sub>1</sub>), and obtain solution _Y<sub>c</sub>_.<tbc>

• Define the updated instance \(K_{c+1}:=(K_c)^{(U_c\leftarrow Y_c)}\).

Finally, return the composed solution \(Y:=Y_r\circ\cdots\circ Y_2\circ Y_1\). By inductively applying Lemma 4.5, we know _Y_ is a correct solution to _K_.

We remark on the low-level implementation of the procedure described above. When we construct the new input instance for the next iteration (namely, \((K_c)^{(U_c\leftarrow Y_c)}\)), we need to prepare the new input sets \(S'[\cdot]\subseteq(U_{c+1}\cup\cdots\cup U_r)\), based on the current input sets \(S[\cdot]\subseteq(U_c\cup\cdots\cup U_r)\) and the current solution \(z[\cdot]\), according to Eq. (20). However, each set _S_\[_i_\] may have size as large as _b_, so it would be to slow to copy them explicitly. In contrast, note that an instance (_K<sub>c</sub>_)|<sub>_U<sub>c</sub>_</sub> only asks for sets \(S[i]\cap U_c\) as input, which have much smaller size _b_<sub>1</sub>=_O_(log_m_). So the correct implementation should be as follows: at the very beginning, each of the sets _S_\[-_L\],...,S_\[_L_\] receives an integer handle, and when we need to copy the sets we actually only pass the handles. And, given the handle of a set _S_\[_i_\] and a color class _U<sub>c</sub>_, we can report the elements in \(S[i]\cap U_c\) in _O(b_<sub>1</sub>)=_O_(log_m_) time (because we can preprocess these intersections at the very beginning). In this way, the time complexity for preparing the input instances to Lemma 4.8 is no longer a bottleneck.

It remains to analyze the time complexity. There are _r_ applications of Lemma 4.8, taking \(O(Lb_1^2(b_1+logL))\le O(Llog^3L)\) time each, and \(O(r\cdot Llog^3L)\le O(Lblog^2L)\) time in total. Combined with the time complexity of deterministic coloring at the beginning, the total time is \(O(LrlogLlogr+|U|logr+Lblog^2L)\le O(Lblogr+|U|logr+Lblog^2L)\). Here we can assume \(|U|\le\sum_{-L\le i\le L}|S[i]|\le O(Lb)\) without loss of generality. Hence, the total time becomes \(O(Lblogr+Lblog^2L)\le O(Lblog^2(Lb))\).

It remains to describe the _O(Lb_<sup>2</sup>(_b_+log_L_))-time algorithm claimed in Lemma 4.8. It relies on the following birthday-paradox-type color-coding lemma, which is derandomized using a standard application of pessimistic estimators:

**Lemma 4.10.** _Given m sets_ \(S_1,S_2,\dots,S_m\in[n]\) _with_ \(|S_i|\le b\)_, there is a deterministic algorithm in O(n_log_m+mb_<sup>3</sup>) _time that computes_ \(k\le log_2(2m)\) _colorings_ \(h_1,h_2,\dots,h_k:[n]\rightarrow[b^2]\)_, such that for every_ \(i\in[m]\) _there exists an h<sub>j</sub> that assigns distinct colors to elements of S<sub>i</sub>._

We include a proof of Lemma 4.10 in Appendix B.5. Now we prove Lemma 4.8.

_Proof of Lemma 4.8._ Without loss of generality, assume \(|U|\le\sum_{-L\le i\le L}|S[i]|\le O(Lb)\). We apply Lemma 4.10 to the sets \(S[-L],S[-L+1]\dots,S[L]\subseteq U\), and in \(O(|U|logL+Lb^3)\le O(Lb(b^2+logL))\) time obtain _k=O_(log_L_) colorings \(h_1,\dots,h_k:U\rightarrow[b^2]\) such that every set _S_\[_i_\] is isolated by some _h<sub>j</sub>_ (i.e., _S_\[_i_\] receives distinct colors under coloring _h<sub>j</sub>_).

