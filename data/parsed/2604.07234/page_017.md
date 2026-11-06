<tbc>string. We assume that _N_ is a large positive integer which tends to infinity. We occasionally suppress the dependence of certain quantities on _N_ in our notation - this should never raise any confusion.

For convenience in the argument there, throughout Section 3.2 (namely the proof of Proposition 3.8), we proceed with the understanding that we are given a fixed typical (as defined in Definition 3.6) deterministic string \(x\in\{0,1\}^N\) and work with the decomposition

(3.1) \(x=\big(x^{(1)},\dots,x^{(B)}\big),\)

studying how an _x_-random string aligns with the structure of _x_. We begin by introducing shorthand for the corresponding "planted" probability measure induced by a deterministic string.

**Definition 3.1** (_x_-planted measure)**.** For a fixed string \(x\in\{0,1\}^N\), we let the _x-planted measure_ P_<sub>x</sub>_ denote the probability measure on \(\bigcup_{k=0}^N\{0,1\}^k\) corresponding to including each bit of _x_ independently with probability \(\alpha\). Specifically, for \(0\le k\le N\) and \(y\in\{0,1\}^k\), we define<tbc>

\(\mathbb{P}_x(y):=\alpha^k(1-\alpha)^{N-k}Z_{x,y}.\)

<tbc>**Remark 3.2.** Given \(x\in\{0,1\}^N\), it is clear that<tbc>

(3.2) \(\mathbb{P}_x\big(\cdot|\{0,1\}^M\big)|_{\{0,1\}^M}\)

<tbc>denotes the law of an _x_-random string, while a local limit theorem (e.g., see [Dur19, Theorem 3.5.3]) yields<tbc>

\(\mathbb{P}_x\big(\{0,1\}^M\big)=\Theta\big(N^{-1/2}\big).\)

<tbc>Thus, we have that

(3.3) \(\mathbb{P}_x\big(\cdot|\{0,1\}^M\big)\le\Theta\big(N^{-1/2}\big)\mathbb{P}_x(\cdot).\)

As we strictly concern ourselves with the exponential orders of rare events under (3.2), it suffices to work with the unconditional measure P_<sub>x</sub>_. \(\triangleup\)

Next, we introduce those parameters needed to derive concentration guarantees at the desired level of granularity. We take \(\epsilon>0\) to be some small fixed constant (\(\epsilon=1/24\) suffices for the argument to hold), and we introduce shorthand for

(3.4) \(\delta:=b^{-1/2+\epsilon};\gamma:=b^{-\epsilon}.\)

We now elaborate on the specific roles that these quantities play over the course of our proof. We recall that our aim is to demonstrate a distinction between samples (_X,Y_) drawn from the null and the planted variants of the Random Subsequence Model. Loosely, we will show that near-equipartitions into _B_ blocks of _Y_ drawn from the planted model resemble the structure of the corresponding block decomposition of _X_, while there is no near-equipartition of _Y_ drawn from the null model for which such a resemblance is attained. We proceed with the relevant definitions, which crucially rely upon our choices of the parameters introduced in (3.4).

**Definition 3.3** (Induced and standardized near-equipartitions)**.** Given \(y\in\{0,1\}^*\), the collection of _induced near-equipartitions_ of _y_ is<tbc>

\(\mathcal{NE}_\mathrm{ind}(y):=\left\{\begin{array}{ c }
\big(y^{(1)},\dots,y^{(B)}\big)\in\big(\{0,1\}^*\big)^B\big| \\
y=y^{(1)}\cdots y^{(B)}; \\
|y^{(i)}|\in\{0,1,\dots,b\}\text{for all}i\in[B]; \\
\big|\big\{i\in[B]:|y^{(i)}|\notin\big[(1-\delta)\alpha b,(1+\delta)\alpha b\big]\big\}\big|\le\gamma B
\end{array}\right\}.\)

<tbc>On the other hand, the collection of _standardized near-equipartitions_ of _y_ is

\(\mathcal{NE}_\mathrm{std}(y):=\left\{\begin{array}{ c }
\big(y^{(1)},\dots,y^{(B)}\big)\in\big(\{0,1\}^*\big)^B\big| \\
y=y^{(1)}\cdots y^{(B)}; \\
|y^{(i)}|\in\{0,1,\dots,b\}\text{for all}i\in[B]; \\
\big|\big\{i\in[B]:|y^{(i)}|\neq\alpha b\big\}\big|\le 3\gamma B
\end{array}\right\}.\)

