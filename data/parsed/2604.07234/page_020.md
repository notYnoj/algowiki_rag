<tbc>Indeed, the desired result would then readily follow via

\(\mathbb{P}_x\big(\{0,1\}^M\backslash\mathcal{G}(x)|\{0,1\}^M\big)=^\text{(3.11)}\mathbb{P}_x\big(\mathcal{A}(x)^c\cap\{0,1\}^M|\{0,1\}^M\big)\)<br>
\(=\mathbb{P}_x\big(\mathcal{A}(x)^c|\{0,1\}^M\big)\le^\text{(3.3)}\Theta(N^{1/2})\mathbb{P}_x\big(\mathcal{A}(x)^c\big)\le^\text{(3.13)}\Theta(N^{1/2})e^{-\Omega(N)}=e^{-\Omega(N)}.\)

The remainder of the proof of Proposition 3.8 involves routine techniques from probabilistic combinatorics. The work lies not in developing novel ideas, but in adapting these arguments to the framework and definitions introduced in Section 3.1 (which are necessary to carry out the argument of Section 3.3). For this reason, we defer the proof to Appendix C.

## 3.3. Failure of biased alignment under the null model.

Proposition 3.8 shows that, for any typical ambient string _x_, an _x_-random string lies in G(_x_) with overwhelming probability. In this subsection we prove the complementary statement under the null model. Specifically, for \((X',Y)\in\{0,1\}^N\times\{0,1\}^M\) drawn from the null model, we show that with overwhelming probability,

\(Y\notin\mathcal{G}(X').\)

This result produces the desired separation, which we exploit in Section 3.4 to prove Theorem 1.1.

As usual, we decompose<tbc>

\(X'=\big(X'^{(1)},\dots,X'^{(B)}\big)\)

<tbc>via equipartitioning \(X'\) into _B_ contiguous blocks of length _b_. Since _Y_ is uniformly distributed on {0,1}_<sup>M</sup>_, we heuristically expect that for any fixed induced near-equipartition \(\big(Y^{(1)},\dots,Y^{(B)}\big)\in\mathcal{NE}_\text{ind}(Y)\), the average

\(\frac{1}{B}\sum_{i=1}^BA_\text{loc}\big(X^{\prime(i)},Y^{(i)}\big)\)

should concentrate near 1/2. The difficulty is to make such a bound uniform over all induced near- equipartitions of _Y_ . Indeed, the class NE<sub>ind</sub>(_Y_) is too large for the most naive approaches (for instance, a union bound over an \(\epsilon\)-net defined in terms of block endpoints) to yield guarantees of sufficient strength. To overcome this, we show that induced total alignment can be approximated by standardized total alignment, in which we restrict most blocks to have exactly the same average length \(\alpha b\) at the expense of permitting more blocks which deviate from this length.

We begin by establishing that this approach can yield a bound of the desired form.

**Proposition 3.9** (Standardized alignment bound)**.** _It holds with probability_ \(\ge 1-e^{-\Omega(N)}\) _that_<tbc>

\(T_\text{std}\big(X',Y\big)<\frac{1+\beta^\star(\alpha)}{2}.\)

<tbc>_Proof._ It readily follows from Definition 3.3 that

(3.14) \(\big|\mathcal{NE}_\text{std}(Y)\big|\le\left(\begin{array}{ c }
B \\
3\gamma B
\end{array}\right)(b+1)^{3\gamma B}\approx^\text{(3.4)}exp\left(B\cdot h(3b^{-\epsilon})+B\cdot 3b^{-\epsilon} log(b+1)\right)=e^{B\cdot\alpha_b(1)}.\)

Furthermore, Definition 3.5 also readily implies that for any \(\big(Y^{(1)},\dots,Y^{(B)}\big)\in\mathcal{NE}_\text{std}(Y)\),

\(\mathbb{P}\left(\frac{1}{B}\sum_{i=1}^BA_\text{loc}\big(X^{\prime(i)},Y^{(i)}\big)\ge\frac{1+\beta^\star(\alpha)}{2}\right)\)<br>
\(\le\mathbb{P}\left(\frac{1}{B}\sum_{i=1}^B\unknown\left\{\text{maj}(X^{\prime(i)})=\text{maj}(Y^{(i)}),\Delta(Y^{(i)})>0\right\}\ge\frac{1+\beta^\star(\alpha)}{2}\right)\le^\text{(Hoeffding)}exp\left(-B\cdot\frac{\beta^\star(\alpha)^2}{4}\right).\) (3.15)

