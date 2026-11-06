Combining Equation 1, Equation 2, and \(|Y(\mathcal{H})|\ge|X(\mathcal{H})|/k\), we obtain

\(\sum_{\mathcal{H}\in\mathbb{H}^\prime}\left\{p(\mathcal{H})\cdot\left\{1+\frac{\lambda}{(1+\lambda)^t}\right\}^{|X(\mathcal{H})|/k}\right\}\le 1.\)

Lemma 19 follows directly from this inequality. □

## 5.2.3 Deriving the Degree Bound

**Lemma 20.** _Let_ \(\lambda\in(0,1]\) _be the parameter of the hardcore model. Suppose G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) _is a fixed k-colorable graph. For every vertex_ \(v\in V^*\) _and every positive integer_ \(t\le\frac{1}{\lambda}\),

\(Pr\left[v\in J_t\text{\textit{and}}|N(v)\cap J_t|\ge\frac{10klnn}{\lambda}\right]\le\frac{1}{n^3}.\) (3)

_Proof._ First, for every positive integer \(t\le\frac{1}{\lambda}\), we have

\(\frac{\lambda}{(1+\lambda)^t}\ge\frac{\lambda}{(1+\lambda)^{1/\lambda}}\ge\frac{\lambda}{e}.\)

Therefore, Lemma 19 implies that the following inequality also holds for \(t\le\frac{1}{\lambda}\):

\(\mathbb{E}\left[(1+\lambda/e)^{|N(v)\cap J_t|/k}\text{if}v\in J_t\text{, otherwise}0\right]\le 1.\) (4)

By Markov’s inequality, Equation 4 implies \(Pr[v\in J_t\text{and}(1+\lambda/e)^{|N(v)\cap J_t|/k}\ge n^3]\le\frac{1}{n^3}\). By taking the logarithm of both sides, the condition above becomes

\(|N(v)\cap J_t|\ge\frac{3klnn}{ln(1+\lambda/e)}.\) (5)

Here,

\(\frac{3klnn}{ln(1+\lambda/e)}\le\frac{3klnn}{(3/10)\cdot\lambda}=\frac{10klnn}{\lambda}.\) (6)

This is due to \(ln(1+x/e)\ge\frac{3}{10}x\) for all \(x\in[0,1]\). Therefore, combining Equation 5 and Equation 6, the probability that \(v\in J_t\) and \(|N(v)\cap J_t|\ge\frac{10klnn}{\lambda}\) is at most \(\frac{1}{n^3}\). □

**Lemma 21.** _Let_ \(\lambda\in(0,1]\) _be the parameter of the hardcore model, and let_ \(t\le\frac{1}{\lambda}\) _be a positive integer. Suppose G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>) _is a fixed k-colorable graph. The probability that the maximum degree of G_<sup>∗</sup>\[_J<sub>t</sub>_\] _exceeds_ \(\frac{10klnn}{\lambda}\) _is at most_ \(\frac{1}{n^2}\).

_Proof._ The maximum degree of _G_<sup>∗</sup>\[_J<sub>t</sub>_\] exceeds \(\frac{10klnn}{\lambda}\) only if the event of Equation 3 occurs for at least one \(v\in V^*\). Hence, by Lemma 20 and the union bound, this probability is at most \(\frac{1}{n^3}\cdot|V^*|=\frac{1}{n^2}\). □

**Lemma 22.** _With_ \(\lambda:=\frac{1}{6kln(3k)lnn+2}\)_, for every fixed k-colorable graph G_<sup>∗</sup>=(_V_<sup>∗</sup>_,E_<sup>∗</sup>)_, G_<sup>∗</sup>\[_J_<sub>1</sub>\]_,...,G_<sup>∗</sup>\[_J<sub>r</sub>_\] _all have maximum degrees at most_ \(10klnn\cdot(6kln(3k)lnn+2)\) _with probability at least_ \(1-\frac{3}{n}\).

_Proof._ We apply Lemma 21 with parameter \(\lambda:=\frac{1}{6kln(3k)lnn+2}\). That is, for each \(t\le 6kln(3k)lnn+2\), the maximum degree of _G_<sup>∗</sup>\[_J<sub>t</sub>_\] exceeds \(10klnn\cdot(6kln(3k)lnn+2)\) with probability at most \(\frac{1}{n^2}\). Hence, the probability that both of the following conditions hold:

