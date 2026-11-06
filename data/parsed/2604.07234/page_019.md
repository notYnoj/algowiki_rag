<tbc>It is easy to justify the use of the term "typical" in Definition 3.6. Indeed, the central limit theorem yields

(3.9) \(\frac{1}{\sqrt{b}}\Delta(X^{(i)})=\frac{1}{\sqrt{b}}\sum_{j=1}^b\left(2(X^{(i)})_j-1\right)\rightarrow^d\mathcal{N}(0,1)\Longrightarrow\mathbb{P}\left(\Delta(X^{(i)})\ge\sqrt{b}\right)>^{(b\text{large})}\frac{3}{10},\)

from which it follows that

\(\mathbb{P}\left(\sum_{i=1}^B\unknown\left\{\Delta(X^{(i)})\ge\sqrt{b}\right\}\le\frac{B}{10}\right)\le^\text{(3.9)}\mathbb{P}\left(\sum_{i=1}^B\unknown\left\{\Delta(X^{(i)})\ge\sqrt{b}\right\}-\mathbb{P}\left(\Delta(X^{(i)})\ge\sqrt{b}\right)\le-\frac{B}{5}\right)\le^\text{(Hoeffding)}e^{-\Omega(N)},\)

so that a uniform random string \(X\in\{0,1\}^N\) is typical, in the sense of Definition 3.6, with probability at least \(1-e^{-\Omega(N)}\). We conclude this section by pinning down our key notion of structural resemblance with a typical string \(x\in\{0,1\}^N\). We let

(3.10) \(\beta^\star(\alpha):=\frac{\beta(\alpha)}{40}:=\frac{1}{40}\left[\mathbb{P}\left(\mathcal{N}\left(\alpha,\alpha\left(1-\alpha\right)\right)\ge 0\right)-\frac{1}{2}\right]>0;\)

we clarify in the forthcoming analysis how this constant shows up.

**Definition 3.7** (Aligned and good sets)**.** Fix \(x\in\{0,1\}^N\). The _x-aligned set_ \(\mathcal{A}(x)\subseteq\{0,1\}^*\) is the collection of all \(y\in\{0,1\}^*\) for which<tbc>

\(T_\text{ind}(x,y)\ge 1/2+\beta^\star(\alpha).\)

<tbc>The _x-good set_ \(\mathcal{G}(x)\subseteq\{0,1\}^M\) is the restriction of A(_x_) to {0,1}_<sup>M</sup>_, i.e.,

(3.11) \(\mathcal{G}(x):=\mathcal{A}(x)\cap\{0,1\}^M.\)

In Section 3.2, we show that for (_X,Y_) drawn from the planted model, _Y_ will overwhelmingly land in G(_X_). On the other hand, we show in Section 3.3 that for \((X',Y)\) drawn from the null model, _Y_ overwhelmingly fails to land in \(\mathcal{G}(X')\). This distinction will then lead to the proof of Theorem 1.1.

## 3.2. Aligned structure under planted measures.

With the machinery of Section 3.1 in place, we are now ready to introduce the regular alignment property, which is the key notion of structural alignment between binary strings which we exploit to prove the upper bound of Theorem 1.1. In the present Section 3.2, we handle the asymptotic behavior of _x_-random strings for typical \(x\in\{0,1\}^N\). Here, we demonstrate via standard concentration arguments that with probability \(1-e^{-\Omega(N)}\), an _x_-random string has large induced total alignment with _x_. Indeed, this is largely as expected - it is natural to suspect that _x_-random strings should resemble _x_ with high probability, and Proposition 3.8 establishes induced total alignment as one such appropriate notion of resemblance. We move on to study the inverse problem in Section 3.3, in which we consider the same problem for random strings (_X,Y_) drawn from the null model and obtain the exact opposite result.

**Proposition 3.8** (Regular alignment property)**.** _Uniformly over all typical_ \(x\in\{0,1\}^N\),

(3.12) \(\genfrac(){pt}{2}{N}{M}^{-1}\left|\left\{S\in\genfrac(){pt}{2}{[N]}{M}:x|_S\notin\mathcal{G}(x)\right\}\right|=\mathbb{P}_x\left(\{0,1\}^M\backslash\mathcal{G}(x)|\{0,1\}^M\right)\le e^{-\Omega(N)}.\)

We observe that the equality of (3.12) is an immediate consequence of Definition 3.1. To establish the inequality of (3.12), it suffices to show that uniformly over all typical \(x\in\{0,1\}^N\), it holds that

(3.13) \(\mathbb{P}_x\big(\mathcal{A}(x)^c\big)=e^{-\Omega(N)}.\)

