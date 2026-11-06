_Proof._ For the upper bound, \(Z_\lambda(G)\le\sum_{S\subseteq V}\lambda^{|S|}=(1+\lambda)^{|V|}\) by the binomial theorem. For the lower bound, since _G_ has a _k_-coloring, one color class has size at least |_V|/k_, so it contains an independent set \(I'\subseteq V\) with \(|I'|\ge|V|/k\). By the binomial theorem,<tbc>

\(Z_\lambda(G)\ge\sum_{I\subseteq I^\prime}\lambda^{|I|}=(1+\lambda)^{|I^\prime|}\ge(1+\lambda)^{|V|/k}.\square\)

<tbc>**Proposition 9.** _Let_ \(\lambda>0\)_, and let G_=(_V,E_) _be a graph. For disjoint vertex sets_ \(S,T\subseteq V\) (\(S\cap T=\emptyset\)),

\(Z_\lambda(G[S\cup T])\le Z_\lambda(G[S])\cdot(1+\lambda)^{|T|}.\)

_Proof._ Each \(I\in\mathcal{I}(G[S\cup T])\) can be written as \(I=I_S\cup I_T\), where \(I_S\in\mathcal{I}(G[S])\) and \(I_T\in\mathcal{I}(G[T])\). Therefore, \(Z_\lambda(G[S\cup T])\le Z_\lambda(G[S])\cdot Z_\lambda(G[T])\). By Proposition 8, we have \(Z_\lambda(G[T])\le(1+\lambda)^{|T|}\), which proves the desired inequality. □

## 3.2 The Size of Independent Sets

We analyze the expected size of an independent set. Note that the case \(\lambda=1\) was already studied by Nilli (1988) \[Nil88\], who showed that the average size of independent sets for a _k_-colorable graph is \(\Omega(\frac{n}{klogk})\) and proved that this bound is tight.

**Lemma 10.** _Let_ \(\lambda\in(0,1]\)_, and let G_=(_V,E_) _be a k-colorable graph. Then,_<tbc>

\(\mathbb{E}_{I\sim\mathsf{IS}_\lambda(G)}[|I|]\ge\frac{\lambda}{3kln(3k)}|V|.\)

<tbc>_Proof._ First, the function \(f(x)=(\frac{1}{3k})^x\) is convex, so it follows from Jensen’s inequality that:

\(\left(\frac{1}{3k}\right)^{\mathbb{E}[|I|]}\le\mathbb{E}\left[\left(\frac{1}{3k}\right)^{|I|}\right]\)<br>
\(=\frac{1}{Z_\lambda(G)}\cdot\left(\sum_{I\in\mathcal{I}(G)}\left(\frac{1}{3k}\right)^{|I|}\lambda^{|I|}\right)=\frac{Z_{\lambda/3k}(G)}{Z_\lambda(G)}\le\frac{(1+\lambda/3k)^{|V|}}{(1+\lambda)^{|V|/k}}\)

The last inequality is due to Proposition 8. Therefore:

\(\mathbb{E}[|I|]\ge-log_{3k}\frac{(1+\lambda/3k)^{|V|}}{(1+\lambda)^{|V|/k}}\)<br>
\(=\frac{1}{ln(3k)}\left\{\frac{|V|}{k}ln(1+\lambda)-|V|ln\left(1+\frac{\lambda}{3k}\right)\right\}\)<br>
\(\ge\frac{1}{ln(3k)}\left\{\frac{|V|}{k}\cdot\frac{2}{3}\lambda-|V|\cdot\frac{\lambda}{3k}\right\}=\frac{\lambda}{3kln(3k)}|V|\)

The last inequality follows from \(\frac{2}{3}x\le ln(1+x)\le x\) for all \(x\in[0,1]\). □

