where the asymptotic restriction follows from the inequalities above for all spectral points, by Strassen’s duality theorem, and the degeneration from ingredient (D1), with the legs permuted and tensor products taken.

## 1.4 Barriers for obtaining better bounds

We have seen how some combination of the degeneration ingredients gives \(\omega_\mathbb{F}\le 9/4\) (and in a similar way bounds on the rectangular matrix multiplication exponents). Can we do better? Not with current ingredients.

### 1.4.1 No barrier from irreversibility

First of all, standard barriers are not effective here. Christandl, Vrana and Zuiddam \[CVZ21, Theorem 3.1\] (see also Alman \[Alm19\] and Christandl, Le Gall, Lysikov and Zuiddam \[CLGLZ25\]) proved a barrier for upper bounds on \(\omega_\mathbb{F}\) from a fixed tensor _S_ (generalising previous barriers of Ambainis, Filmus and Le Gall \[AFLG15\]): every upper bound obtained from asymptotic restrictions \(\langle 2^n,2^n,2^n\rangle\lesssim S^{\otimes m}\) is at least 2irr(_S_), where the irreversibility irr(_S_) is the ratio of the logarithms of the asymptotic rank and the asymptotic subrank of _S_.

This irreversibility barrier does not explain why the proof of Theorem 1.1 gives no bound below 9/4: for the tensors \(S_a=\otimes_{\pi\in\mathfrak{S}_3}\pi\cdot\mathsf{P}_{a,a}\) of (1.6), with \(a\ge 2\), the degenerations \(\langle a\rangle\unknown\mathsf{P}_{a,a}\unknown\langle 2a-1\rangle\) give \(\mathrm{irr}(S_a)\le\mathrm{log}(2a-1)/\mathrm{log}a\), so the barrier tends to the trivial value 2 as \(a\rightarrow\infty\). A similar analysis for rectangular matrix multiplication gives no irreversibility barrier there.

### 1.4.2 Tight barrier for (D0)-(D4)+(C1)-(C4)

No derivation from the ingredients (D0)-(D4) by the rules (C1)-(C4), with (D3) and (D4) also inside partial direct sums, gives an upper bound on \(\omega_\mathbb{F}\) below 9/4, and neither does a limit of such bounds (Theorem 5.4). This remains true for the asymptotic consequences of the rules, among them the asymptotic restriction (1.6). Likewise, for all real numbers \(a\ge b\ge c\ge 0\), no such derivation gives a better upper bound on \(\omega_\mathbb{F}(a,b,c)\) than Theorem 1.2.

We prove the barrier with a dual certificate. For all values of their parameters, write the degenerations of the ingredients (D0)-(D4) as \(S_i\unknown T_i\), for _i_ in an index set _I_. Add the restrictions \(T\le T\oplus S\), \(T\le T\oplus_1S\), \(T\oplus_1S\le T\oplus S\), \(\mathsf{P}_{a,c}\le\mathsf{P}_{a,b}\) for \(c\le b\), and \(\mathsf{P}_{a,b}\le\mathsf{P}_{a,1}\otimes\langle 1,1,b\rangle\), and the isomorphisms that express the associativity and commutativity of \(\oplus\), \(\otimes\) and \(\oplus_1\) and the distributivity of \(\otimes\) over \(\oplus\) and \(\oplus_1\), the identities of the permutations of the legs, the isomorphisms between products and permutations of matrix multiplication tensors, the isomorphism between the partial direct sum of _r_ copies of _T_ and \(T\otimes\langle 1,1,r\rangle\), and \(\mathsf{P}_{a,b}\cong(12)\cdot\mathsf{P}_{b,a}\) (Section 5.1). By the rules (C1)-(C4), with (D3) and (D4) also applied inside partial direct sums, these generate a relation \(\unknown\) on formal combinations of the tensors.

Let \(\Delta_\unknown\) be the set of functions \(\phi\) on these formal combinations that are additive and multiplicative, satisfy \(\phi(\langle 1\rangle)=1\), and satisfy \(\phi(T)\le\phi(S)\) whenever \(T\unknown S\); in particular, \(\phi(S_i)\le\phi(T_i)\) for every \(i\in I\). The set \(\Delta_\unknown\) does not depend on the field F. For every field F, every spectral point agrees with an element of \(\Delta_\unknown\) on the tensors \(\pi\cdot\mathsf{P}_{a,b}\) and the matrix multiplication tensors, so \(\Delta_\unknown\) is an outer approximation of the asymptotic spectrum: \(\Delta_\mathbb{F}\subseteq\Delta_\unknown\) in this sense. The proof of Theorem 1.1 is in terms of spectral points \(\phi\in\Delta_\mathbb{F}\), but it works almost verbatim for every \(\phi\in\Delta_\unknown\), so<tbc>

\(2^{\omega_\mathbb{F}}=\mathrm{max}_{\phi\in\Delta_\mathbb{F}}\phi(\langle 2,2,2\rangle)\le\mathrm{max}_{\phi\in\Delta_\unknown}\phi(\langle 2,2,2\rangle)\le 2^{9/4}.\) (1.7)

<tbc>The point is that the second inequality in (1.7) is an equality: we will construct an explicit function \(F^\star\in\Delta_\unknown\) with \(F^\star(\langle 2,2,2\rangle)=2^{9/4}\) (Section 5), a "dual certificate". This<tbc>

