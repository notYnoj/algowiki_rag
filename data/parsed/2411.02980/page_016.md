The above observation is formalized by the following lemma that upper bounds the correlation decay of the coupling by the probability of the truncation of the random process _P_cp. The proof of this lemma is similar to that of \[WY24, Lemma 3.9\], and is included for completeness.

**Lemma 4.10.** _Assume_ \(\Phi\) _is satisfiable. Let_ (_X,Y_) _be the output of_ \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\)_, and let_ \((\mathcal{E}^\mathrm{cp},\mathcal{F}^\mathrm{cp},\sigma^\mathrm{cp},\tau^\mathrm{cp},T^\mathrm{cp},\varsigma^\mathrm{cp})\sim\mu^\mathrm{cp}\) _be the outcome of the process P_cp_. Then, we have_<tbc>

\(\mathbf{Pr}\left[d_\mathrm{Ham}(X,Y)\ge k\cdot M\right]\le\mathbf{Pr}\left[|V(T^\mathrm{cp})|=M\right].\)

<tbc>_Proof._ By the construction of witness tree in Definition 4.4 and Proposition 4.5, each time a recursive call is made to \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\) at Line 10 or Line 17 of Algorithm 2, at most _k_ variables are assigned into \(\sigma\) and \(\tau\), and the size of the current witness tree _T=T(L_) increases by one. Furthermore, by Line 3 of Algorithm 2, the Hamming distance between _X_ and _Y_ is upper bounded by the total number of variables assigned in \(\sigma\) and \(\tau\) during the recursion \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\). Hence, we have

\(d_\mathrm{Ham}(X,Y)\ge k\cdot M\Longrightarrow|V(T)|\ge M.\)

We now argue that the witness tree _T=T(L_), constructed from the execution log _L_ of a run of Algorithm 2 from \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\emptyset,\emptyset)\), can be coupled with the witness tree _T_cp constructed during the process _P_cp described in Definition 4.8. Specifically, whenever a recursive call to \(\mathrm{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) is made in Algorithm 2, with the current witness tree being _T_ and witness assignment \(\varsigma\), the process _P_cp moves to a state \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\). Under this coupling, the lemma follows immediately.

It is important to note that this coupling between the two processes, Algorithm 2 and _P_cp, does not hold trivially, because the randomness used in the construction of _P_cp is explicitly identified to the random satisfying assignments:<tbc>

\(\mathfrak{X}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\text{and}\mathfrak{Y}\sim\mu_\mathcal{C}.\)

<tbc>Nevertheless, this perfect coupling between Algorithm 2 and _P_cp can be verified by structural induction, proceeding in the top-down order of recursion, with a strengthened hypothesis: conditioning on the process _P_cp being at the state \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\), Algorithm 2 is at the same state, and it further holds:

(3) \(\mathfrak{X}\sim\mu_\mathcal{E}^\sigma\text{and}\mathfrak{Y}\sim\mu_\mathcal{F}^\tau.\)

With (3), the transition probabilities to the next state are identical in both processes. Therefore, the two processes are perfectly coupled. Additionally, it can be verified that (3) continues to hold for each possible branch of the process _P_cp. This concludes the proof of the lemma. □

The proof of Theorem 4.1 now reduces to establishing an upper bound of 2<sup>-_M_</sup> on the truncation probability **Pr**\[|_V(T_cp)|=_M_\]. A crucial step in this process is the following technical lemma, which assumes Condition 3.1 and will also play a key role in the algorithmic implication of the coupling later.

**Lemma 4.11.** _Assume_ \(\Phi\) _is satisfiable. Let_ \(\mathfrak{X}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\) _and_ \(\mathfrak{Y}\sim\mu_\mathcal{C}\)_. For any subset of variables_ \(S\subseteq V\),

\(\forall X\in[q]^S,\mu_{\mathcal{C}\backslash\{c_0\}}(X)=\mathbf{Pr}\left[\mathfrak{X}_S=X\right]\le q^{-|S\cap V_\mathrm{good}|}\cdot(1-\mathrm{e}q^{-(1-\varepsilon_1)k})^{-|S|p_1\alpha};\)<br>
\(\forall Y\in[q]^S,\mu_\mathcal{C}(Y)=\mathbf{Pr}\left[\mathfrak{Y}_S=Y\right]\le q^{-|S\cap V_\mathrm{good}|}\cdot(1-\mathrm{e}q^{-(1-\varepsilon_1)k})^{-|S|p_1\alpha}.\)

_Proof._ We only prove the first inequality, and the second one follows similarly. For any \(\tau\in[q]^{V_\mathrm{bad}}\) with \(\mathbf{Pr}\left[\mathfrak{X}_{V_\mathrm{bad}}=\tau\right]>0\), the following bound holds:

(4) \(\mathbf{Pr}\left[\mathfrak{X}_{\mathrm{vbl}(T)\cap V_\mathrm{good}}=X_{\mathrm{vbl}(T)\cap V_\mathrm{good}}|\mathfrak{X}_{V_\mathrm{bad}}=\tau\right]\le q^{-|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot(1-\mathrm{e}q^{-(1-\varepsilon_1)k})^{-|\mathrm{vbl}(T)|p_1\alpha}.\)

This is because, given the pinning \(\mathfrak{X}_{V_\mathrm{bad}}=\tau\), the resulting pinned formula has each variable with a degree of at most _p_<sub>1</sub>_d_ (by Fact 3.8) and each constraint containing at least \((1-\varepsilon_1)k\) variables (by Fact 3.9). Applying Theorem 2.4 by setting the parameter \(x(c)=\mathrm{e}q^{-(1-\varepsilon_1)k}\) for each constraint _c_ in the pinned formula, we derive the bound in (4).

Now, we can bound the probability of X<sub>vbl(_T_)</sub>=_X_ as follows:

\(\mathbf{Pr}\left[\mathfrak{X}_{\mathrm{vbl}(T)}=X\right]=\sum_{\tau\in[q]^{V_\mathrm{bad}}}\mathbf{Pr}\left[\mathfrak{X}_{V_\mathrm{bad}}=\tau\right]\cdot\mathbf{Pr}\left[\mathfrak{X}_{\mathrm{vbl}(T)\cap V_\mathrm{good}}=X_{\mathrm{vbl}(T)\cap V_\mathrm{good}}|\mathfrak{X}_{V_\mathrm{bad}}=\tau\right]\)<br>
\(\text{(by (4))}\le q^{-|\mathrm{vbl}(T)\cap V_\mathrm{good}|}\cdot(1-\mathrm{e}q^{-(1-\varepsilon_1)k})^{-|\mathrm{vbl}(T)|p_1\alpha}.\)

