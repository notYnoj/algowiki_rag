**Lemma 2.12.** _Let_ \(f:D\rightarrow\mathbb{R}_{\ge 0}\cup\{\infty\}\) _be a function. For any set_ \(S\subseteq D\) _where_ (G_<sub>f</sub>_)<sub>|_S_</sub> _is defined, it is the unique choice that minimizes_ E<sub>_x_∼D<sub>|_S_</sub></sub>[_f(x_)]-S(D<sub>|_S_</sub>) _over all distributions supported on S._

We use H<sub>2</sub>(_p_)=_p_log(1_/p_)+(1-_p_)log(1/(1-_p_)) to denote the _binary entropy_ of a Bernoulli random variable with probability _p_. We use the following standard inequality on H<sub>2</sub>.

**Proposition 2.13.** \(\mathrm{H}_2(p)\le p\mathrm{log}(e/p)\).

_Proof._

\(\mathrm{H}_2(p)=p\mathrm{log}(1/p)+(1-p)\mathrm{log}(1/(1-p))\)<br>
\(=p\mathrm{log}(1/p)+(1-p)\frac{\mathrm{ln}(1/(1-p))}{\mathrm{ln}2}\)<br>
\(\le p\mathrm{log}(1/p)+\frac{p}{\mathrm{ln}2}\mathrm{since}\mathrm{ln}(x)\le x-1\)<br>
\(=p\mathrm{log}(1/p)+p\mathrm{log}e\)<br>
\(=p\mathrm{log}(e/p).\)

We also require the following standard inequality.

**Proposition 2.14** (Hoeffding’s inequality \[Hoe63\])**.** _Let_ U _be the uniform distribution on n bits and_ \(t\le n/2\)_. Then_

\(\mathrm{Pr}_{x_1,\dots,x_n\sim\mathcal{U}}\left[\sum_{i\in[n]}x_i\le n/2-t\right]=\mathrm{Pr}_{x_1,\dots,x_n\sim\mathcal{U}}\left[\sum_{i\in[n]}x_i\ge n/2+t\right]\le e^{-2t^2/n}.\)

## 2.1 Our model

While we will focus on circuits in this document, the ideas used in this section are sufficiently general to apply to any computational model that performs deterministic local transformations at fixed time steps.

### Heat and entropy flow

To simplify our math, we will assume that all computation is performed at a fixed temperature T and units are chosen such that _k<sub>B</sub>_Tln2=1. Throughout this paper we analyze how much entropy a computational device must release into its environment to obey the second law of thermodynamics. We will be assuming that each logical state of the machine has the same energy level and number of microstates.<sup>18</sup> In principle this entropy can take many forms, but for our analysis it is safe to assume that it is always released as heat. This motivates what we will call _heat functions_ as a way to abstract away messy details for how computations release excess entropy.

<sup>18</sup>We use the term "microstate" in this paper to mean the various different physical states a machine can be in while still representing the same logical state. As a concrete example, a Boolean gate implemented with semiconductors has a logical state identified by the bits on the input and output wires, which generally will correspond to many different physical microstates, depending on the precise positions and motion of electrons in the wires.

