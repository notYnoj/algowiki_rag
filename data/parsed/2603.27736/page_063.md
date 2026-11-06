**Hypothesis A.3.** _For every_ \(\epsilon>0\) _there is some constant_ \(c\ge 0\) _such that the following holds. For every integer set X with doubling_ \(|X+X|\le K|X|\) _there is a subset_ \(Y\subseteq X\) _of size_ \(|Y|\ge\Omega(|X|^{1-\epsilon}/K^c)\) _and a sum-order-preserving function_ \(h:Y\rightarrow\{0,\dots,|X|\}\)_. Moreover, given X one can compute Y and h in time_ \(|X|^{3-\Omega_\epsilon(1)}K^{O_\epsilon(1)}\).

Indeed, when allowing a small polynomial loss of the form \(|X|^\epsilon\) then Lovett and Regev’s counterexample does no longer apply, and it is conceivable that the proof avoids convex progressions. Hypothesis A.3 is still strong enough to imply all of our results implied by Hypothesis 1.12; see Remark 5.15.

As a final note, recall that for us it is necessary to also _compute Y_ and _h_ (as stated in Hypotheses 1.12 and A.3). This is perhaps the smallest concern--prior work on additive combinatorics in algorithm design has already ported many existential theorems to computational versions \[32, 29, 28, 1, 83, 53\], and most of these adaptations did not deviate significantly from their original proofs (a notable exception is \[42\]); relatedly, there has already been recent work on turning the finite-field PFR theorem \[59\] into an efficient algorithm \[12\].

## B Derandomization of the Conflict-Free Covering Lemma

The purpose of this section is to complete the missing proof of Lemma 3.7. The overall idea is to derandomize the simple randomized algorithm described earlier in Section 4 by the method of conditional expectations, however, to achieve a sufficiently efficient algorithm some technical details are necessary.

**Lemma 3.7** (Conflict-Free Covering)**.** _Let_ \(x_1,\dots,x_n\in[r]\) _and let_ \(C_1,\dots,C_n\subseteq[r]\) _be sets of size at most s such that_ \(x_i\unknown\in C_i\) _for all i. We say that a set_ \(S\subseteq[r]\) covers _item i if_ \(x_i\in S\) _and_ \(C_i\cap S=\emptyset\)_. Then there is a collection_ S _of size_ \(|\mathcal{S}|\le O(slogn)\) _so that each_ \(i\in[n]\) _is covered by some set_ \(S\in\mathcal{S}\)_. Moreover, there is a deterministic_ \(\tilde{O}(nr)\)_-time algorithm that constructs_ S_, along with a mapping_ \([n]\rightarrow\mathcal{S}\) _indicating for each item i by which set it is covered._

**Proof.** Let \(\mathcal{S}\leftarrow\emptyset\) be the collection of sets we are about to construct, and let \(I\subseteq[n]\) denote the set of remaining items _i_ that are not covered by S (i.e., \(I=\{i\in[n]:\nexists S\in\mathcal{S}:x_i\in S\text{and}C_i\cap S=\emptyset\}\)). We will repeatedly construct sets _S_ to be inserted into S. We describe how to construct the next such set _S_. Initialize \(S\leftarrow\emptyset\), and consider the partition \(I=B(S)\sqcup G(S)\sqcup U(S)\) into the remaining _bad_, _good_, and _undecided_ items defined by

\(B(S)=\{i\in I:C_i\cap S\neq\emptyset\},\)<br>
\(G(S)=\{i\in I:C_i\cap S=\emptyset\text{and}x_i\in S\},\)<br>
\(U(S)=\{i\in I:C_i\cap S=\emptyset\text{and}x_i\unknown\in S\}\)

which we will maintain throughout the construction of _S_. Write

\(\phi(S)=|G(S)|-\frac{|B(S)|}{2s}\)

for the _potential_ of _S_. As we will prove shortly, we are always in one of two cases: (1) there is some \(j\in[r]\) so that when inserting _j_ into _S_ the potential increases by at least \(\phi(S\cup\{j\})-\phi(S)\ge|I|/(8r)\), or (2) there are many good items, \(|G(S)|\ge|I|/(16s)\). While we are in the first case we insert the respective element into _S_. When we are eventually in the second case we have completed the construction of _S_, so we update \(\mathcal{S}\leftarrow\mathcal{S}\cup\{S\}\), update _I_ appropriately (i.e., remove all indices _i_ covered by _S_), and, while \(I\neq\emptyset\), proceed to the construction of the next set _S_.

This almost completes the description of the algorithm, but we have not described yet how to efficiently find such an element \(j\in[r]\). We will now first analyze that the algorithm is correct, and later describe the missing efficient implementation.

