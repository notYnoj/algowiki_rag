<tbc>regarding how to deal with general parameters.

**Algorithm.** Similar to the lossy loose compactor algorithm described in the proof of Theorem 8.1, except that we now parametrize the expander graph family differently as explained above, we run the algorithm on _super-elements_ throughout, and moreover, we introduce the following parameter modifications:

• The array of length \(n'=m\cdot\lfloor d/2\rfloor\) super-elements is divided into _m_ chunks of \(\lfloor d/2\rfloor\) super- elements. We redefine sparse and dense chunks as follows: a _sparse_ chunk is one that has at most _d/_(2log<sup>2</sup>_m_) real super-elements. Any chunk that is not sparse is said to be dense.<tbc>

• We will run the ProposeAcceptFinalize subroutine for \(\text{iter}:=logn'/logn'\) iterations. Moreover, in every iteration, each right vertex sends a rejection if it receives more than _d/_(2log<sup>2</sup>_m_) proposals; otherwise it sends an acceptance message. Each left vertex become satisfied if it receives at least \(\lfloor d/2\rfloor\) acceptance messages.<tbc>

• After the dense chunks distribute their real super-elements to the right vertices, we compress all chunks such that each chunk contains \(\lfloor d/(2log^2m)\rfloor\) super-elements, without losing any real super-elements in the process (see Fact 13.5).

Last but not the least, the circuit implementations of the ProposeAcceptFinalize subroutine and the online routing phase are somewhat non-trivial, and needs to use the **SlowDistr** and **SlowTC** primitives -- we will explain these details later.

Note that for sufficiently large _n_, \(logm=\Theta(logn)\) and therefore the above algorithm produces an output that is \(\Theta(1/log^2n)<1/logn\) fraction of the original length.

**Lemma 13.4.** _In each iteration of the_ ProposeAcceptFinalize _algorithm, at most_ 32/log<sup>4</sup>_m fraction of the remaining unsatisfied left vertices remain unsatisfied._

_Proof._ Let \(B:=\lfloor d/2\rfloor\) be the number of super-elements of a chunk. The fraction of dense chunks is at most \(1/(logn)^{C_\triangledown-3}\), since otherwise the total number of real elements in the input array would be greater than<tbc>

\(B\cdot\frac{1}{log^2m}\cdot\frac{1}{(logn)^{C_\triangledown-3}}\cdot\frac{n'}{B}\ge\frac{n}{(logn)^{C_\triangledown}}\)

<tbc>Let \(U\subseteq L\) be the set of unsatisfied vertices at beginning of any given iteration, let \(R_\text{neg}\subseteq\text{neighbors}(U)\subseteq R\) be the set of neighbors that respond with a rejection. Then, \(e(U,R_\text{neg})>|R_\text{neg}|\cdot d/(2log^2m)\). From the expander mixing lemma (Lemma A.1 of Appendix A), we obtain<tbc>

\(\frac{|R_\text{neg}|\cdot d}{2log^2m}<e(U,R_\text{neg})\le\frac{d|U||R_\text{neg}|}{m}+\epsilon d\sqrt{|U||R_\text{neg}|}.\)

<tbc>Dividing by |_R_neg|_d_ and rearranging, we have that \(\epsilon\sqrt{|U||/|R_\text{neg}|}>1/(2log^2m)-|U|/m\). Since \(|U|/m\le 1/(logn)^{C_\triangledown-3}\) (recall that _U_ is initially all the dense chunks on the left), we have that

\(\sqrt{|U||/|R_\text{neg}|}>\frac{1}{\epsilon}\cdot\frac{1}{2log^2m}-\frac{1}{\epsilon}\cdot\frac{|U|}{m}>\frac{1}{\epsilon}\cdot\left(\frac{1}{2log^2m}-\frac{1}{(logn)^{C_\triangledown-3}}\right),\)

Since \(C_\triangledown>8\), and \(\epsilon\le\frac{1}{log^4m}\), we have that \(\sqrt{|U||/|R_\text{neg}|}\ge 0.25log^2m\), i.e., \(|U||/|R_\text{neg}|\ge\frac{1}{16}\cdot log^4m\), that is, \(|R_\text{neg}|\le 16|U|/log^4m\).

We conclude that the number of vertices in _R_ that respond with a rejection is at most 16|_U_|/log<sup>4</sup>_m_. Therefore, the number of edges that receive a rejection is at most 16|_U|d/_log<sup>4</sup>_m_. For a left vertex<tbc>

