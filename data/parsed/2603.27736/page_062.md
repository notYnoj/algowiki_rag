<tbc>is order-preserving, and such that \(|h'(x)|\le d^{O(logd)}|Q|\). Let

\(R=\left\{\sum_{i=1}^d\ell_ix_i:|\ell_i|\le\left\lfloor\frac{L_i}{8}\right\rfloor\right\}.\)

We claim that the restriction of \(h'\) to the domain _R_ is sum-order-preserving. Indeed, fix any \(x_1,x_2,y_1,y_2\in R\), and suppose that _x_<sub>1</sub>+_x_<sub>2</sub>_\<y_<sub>1</sub>+_y_<sub>2</sub>. Note that _x_<sub>1</sub>+_x_<sub>2</sub> is an element of _P_, and thus \(h'(x_1)+h'(x_2)=h'(x_1+x_2)\) by definition. The same holds for _y_<sub>1</sub> and _y_<sub>2</sub>. Moreover, we have \(h'(x_1+x_2)<h'(y_1+y_2)\) as \(h'\) is order- preserving. Combining these facts we indeed have \(h'(x_1)+h'(x_2)<h'(y_1)+h'(y_2)\).

Next, observe that _O_(1)_<sup>d</sup>_=exp((log_K_)<sup>_O_(1)</sup>) translates of _R_ cover _P_, and in turn exp((log_K_)<sup>_O_(1)</sup>) translates of _P_ cover _X_. Hence, for some translate _t_ the set \(Y=(R+t)\cap X\) has size \(|X|/exp((logK)^{O(1)})\). Let \(h:Y\rightarrow\mathbb{Z}\) be defined by \(h(x)=h'(x-t)\). The sum-order-preserving property is maintained under linear transformations, hence _h_ is sum-order-preserving. Moreover, recall that for all \(x\in Y\) we have that

\(|h(x)|=|h'(x-t)|\le d^{O(d)}|Q|\)<br>
\(\le d^{O(d)}O(1)^d|P|\)<br>
\(\le d^{O(d)}O(1)^dexp((logK)^{O(1)})|X|\)<br>
\(\le exp((logK)^{O(1)})|X|,\)

and thus \(h:Y\rightarrow\{-K'|X|,\dots,K'|X|\}\) for some \(K'=exp((logK)^{O(1)})\).

A final cosmetic modification is to restrict the range of _h_ to {0_,...,|X_|} as in the theorem statement. To this end partition \(\{-K'|X|,\dots,K'|X|\}\) into \(O(K')\) intervals of size at most |_X_|. Take the range with largest preimage in _Y_ , and restrict _Y_ to that preimage. This preserves at least an exp((log_K_)<sup>_O_(1)</sup>)-fraction of the elements in _Y_ and the remaining map is clearly still sum-order-preserving.

## A.2 Polynomial Bounds?

It is an open question whether the quasi-polynomial bounds from the previous section can be improved to polynomial. This is exactly Hypothesis 1.12--the hypothesis that our full universe reduction for APSP is conditioned on:

**Hypothesis 1.12** (Sum-Order-Preserving Hashing with Polynomial Bounds)**.** _There is a constant c such that for every integer set X with doubling_ \(|X+X|\le K|X|\) _there is a subset_ \(Y\subseteq X\) _of size_ \(|Y|\ge\Omega(|X|/K^c)\) _and a sum-order-preserving function_ \(h:Y\rightarrow\{0,\dots,|X|\}\)_. Moreover, given X one can compute Y and h in time_ |_X_|<sup>1+_o_(1)</sup>_K_<sup>_O_(1)</sup>.

In the following paragraphs we muse on a possible proof of Hypothesis 1.12.

It seems plausible that a proof of Hypothesis 1.12 could work along the same lines as in the previous subsection. This would require two improvements: strengthening the Freiman-Ruzsa theorem as well as the condensing lemma to have polynomial bounds. The first is exactly the famous _Polynomial Freiman-Ruzsa (PFR) Conjecture_. Its finite field analogue has recently been resolved in a celebrated paper by Gowers, Green, Manners, and Tao \[59\]. The second is not as well-studied. However, the proof of the condensing lemma relies on the same "geometry of numbers" technique that the state-of-the-art proofs for the Freiman-Ruzsa theorem also rely on \[87\]. For this reason it is reasonable to hope that a resolution of the PFR Conjecture might resolve our second issue along the way.

On a technical level, there is one more obstacle: The PFR Conjecture is known to be _false_ for generalized arithmetic progressions by a counterexample due to Lovett and Regev \[76\]. That is, we cannot expect that Theorem A.1 as it is stated here can be improved to polynomial bounds. Instead, the usual formulation of the PFR Conjecture involves more general objects called _convex progressions_; see also \[77\]. The consequence for us is that, in a hypothetical proof of Hypothesis 1.12 along the lines we described before, the condensing lemma would also need to be generalized to convex progressions. Alternatively, this issue could be avoided by resorting to the following even weaker version of Hypothesis 1.12:

