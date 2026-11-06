If instead \(\ell=k^\star\), we use the comparison \(L_\ell\le L_h\). By (3),<tbc>

\(\mu^\star-2\beta_\ell=\mu_\ell-2\beta_\ell\le L_\ell\le L_h\le\mu_h.\)

<tbc>Since \(h\neq k^\star\), we have<tbc>

\(\mu_h=\mu^\star-\Delta_h\le\mu^\star-\Delta_{k^\star}.\)

<tbc>Thus<tbc>

\(\mu^\star-2\beta_\ell\le\mu^\star-\Delta_{k^\star},\)

<tbc>and so<tbc>

\(2\beta_\ell\ge\Delta_{k^\star}=\Delta_\ell.\)

<tbc>Therefore, in all subcases with \(h\neq k^\star\),<tbc>

\(2\beta_\ell\ge\Delta_\ell.\)

<tbc>Combining this with (4) yields<tbc>

\(B_h\le 2\beta_\ell\le-\Delta_\ell+4\beta_\ell.\)

<tbc>Consequently,<tbc>

\(B_h\le min\{2\beta_\ell,-\Delta_\ell+4\beta_\ell\}=min\{0,-\Delta_\ell+2\beta_\ell\}+2\beta_\ell.\)

<tbc>_Case 2: the sampled arm is k=h._ The sampling rule gives \(\beta_h\ge\beta_\ell\). We first show that \(U_\ell\le U_h\). Suppose, for contradiction, that \(U_\ell>U_h\). Then<tbc>

\(L_\ell=U_\ell-2\beta_\ell>U_h-2\beta_\ell\ge U_h-2\beta_h=L_h.\)

<tbc>Since \(U_\ell=max_{a\neq h}U_a\), and since \(U_\ell>U_h\), we have<tbc>

\(max_{a\neq\ell} U_a\le U_\ell.\)

<tbc>Hence<tbc>

\(B_\ell=max_{a\neq\ell} U_a-L_\ell<U_\ell-L_h=B_h,\)

<tbc>contradicting the minimality of _h_. Thus \(U_\ell\le U_h\), and

\(B_h=U_\ell-L_h\le U_h-L_h=2\beta_h.\) (5)

We next prove<tbc>

\(B_h\le-\Delta_h+4\beta_h.\)

<tbc>If _h=k<sup>⋆</sup>_, then every \(a\neq h\) satisfies \(\mu_a\le\mu^\star-\Delta_h\). In particular,<tbc>

\(B_h=U_\ell-L_h\le(\mu_\ell+2\beta_\ell)-(\mu^\star-2\beta_h)\le-\Delta_h+2\beta_\ell+2\beta_h\le-\Delta_h+4\beta_h.\)

<tbc>If \(h\neq k^\star\), then \(k^\star\neq h\), and<tbc>

\(U_\ell=max_{a\neq h}U_a\ge U_{k^\star}\ge\mu^\star.\)

<tbc>Since we already proved \(U_h\ge U_\ell\), it follows that \(U_h\ge\mu^\star\). Combining this with \(U_h\le\mu_h+2\beta_h\) gives<tbc>

\(2\beta_h\ge\mu^\star-\mu_h=\Delta_h.\)

<tbc>Thus<tbc>

\(2\beta_h\le-\Delta_h+4\beta_h,\)

<tbc>and (5) implies<tbc>

\(B_h\le-\Delta_h+4\beta_h.\)

<tbc>Therefore

\(B_h\le min\{2\beta_h,-\Delta_h+4\beta_h\}=min\{0,-\Delta_h+2\beta_h\}+2\beta_h.\)

The two cases prove the lemma.

**Lemma 22** (A fixed-clipping sampled arm has large stochastic radius)**.** _On_ E<sub>fix</sub>_, if_ FIXEDCLIP- 1BITBAI _samples arm k in a non-stopping round, then_<tbc>

\(r_\varepsilon(N_k,\delta/K)>\frac{\widetilde{\Delta}_k}{4}.\)

