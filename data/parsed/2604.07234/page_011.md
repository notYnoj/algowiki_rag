<tbc>two unknowns _x_ and _y_. Solving this system produces the explicit formulas for \(x_\alpha\) and \(y_\alpha\), and substituting them back gives

\(\mathsf{R}(\alpha)=-\mathrm{log}x_\alpha-\alpha\mathrm{log}y_\alpha,\)

which concludes the proof.

### 1.4. Notation and conventions.

We employ standard asymptotic notation throughout, occasionally subscripted to clarify the relevant limiting variable (e.g., _o<sub>b</sub>_(1) denotes a quantity that vanishes as \(b\rightarrow\infty\)), though _o<sub>p</sub>_ retains its usual probabilistic meaning. Unless otherwise stated, all asymptotics are taken as \(N,M\rightarrow\infty\) with \(\alpha=M/N\) fixed, and we omit floor and ceiling symbols when doing so does not affect asymptotic behavior. Because many of our estimates are meaningful only up to subexponential factors, we introduce the shorthand

\(f(N)\approx g(N)\Longleftrightarrow\frac{f(N)}{g(N)}=e^{o(N)}\text{and}\frac{g(N)}{f(N)}=e^{o(N)}.\)

It is immediate that ≈ defines an equivalence relation on functions from N to R<sub>_\>_0</sub>. Given \(p\in[0,1]\), we let BDC_<sub>p</sub>(X_) denote the (random) string resulting from passing _X_ through the binary deletion channel with deletion probability _p_. All logarithms in this paper are taken base _e_.

### 1.5. Organization.

The rest of the paper is organized as follows. In Section 2, we prove the lower bound of (1.8) and establish the weak limits of (1.6) and (1.7). Proving the strict inequalities of (1.6) and (1.8) constitutes the main technical challenge of the proof of Theorem 1.1. We carry this out in Section 3 and then establish Theorem 1.1 and Corollary 1.2. In Section 4, we derive the exact annealed free energy formula of Theorem 1.3. We conclude in Section 5 with some open problems and suggestions for future research.

## 2. Weak Limits for the Null and Planted Models

We initiate the proof of Theorem 1.1 by establishing the existence of weak limits \(f_\mathrm{null}(\alpha)>0\) (for values \(\alpha\in(0,1/2)\) of the density parameter) and \(f_\mathrm{pl}(\alpha)>0\) for which (1.6) and (1.7) hold.

### 2.1. Null model.

Throughout Section 2.1, we fix \(\alpha\in(0,1/2)\). We begin by observing that the existence of the weak limit \(f_\mathrm{null}(\alpha)\) is enough to prove the first inequality of (1.8). Towards this end, we first observe that there is a natural greedy algorithm [DG01; Mit09] for attempting to embed _Y_ into \(X'\). Writing \(\tau(i)\) for the position selected at step _i_ and setting \(\tau(0):=0\), we define \(\tau(i)\) recursively as the least index \(t>\tau(i-1)\) such that \(X'_t=Y_i\) whenever such an index exists. If no such index exists at some step, we say that the greedy embedding algorithm fails. Then<tbc>

\(Z_{X^\prime,Y}=0\Longleftrightarrow\text{the greedy embedding algorithm fails,}\)

<tbc>since any \(\sigma\in S_{X^\prime,Y}\) must satisfy \(\tau(i)\le\sigma(i)\) at every step for which the greedy algorithm is defined. Equivalently, the event that \(Z_{X^\prime,Y}=0\) is exactly the event that

\(\sum_{i=1}^MG_i>N,\)

where _G_<sub>1</sub>_,...,G<sub>M</sub>_ are i.i.d. Geom(1/2) random variables. Here, _G<sub>i</sub>_ corresponds to the number of bits of \(X'\) that must be examined after \(\tau(i-1)\) in order to locate \(\tau(i)\). It easily follows from this latter representation that \(Z_{X^\prime,Y}=0\) with high probability for \(\alpha>1/2\), and that at \(\alpha=1/2\), the event \(Z_{X^\prime,Y}=0\) has probability tending to 1/2. This explains why the weak limit (1.7) is stated only for \(\alpha\in(0,1/2)\).

We now fix \(\sigma\in S_{X^\prime,Y}\), which corresponds to the following _skip vector_ \(v\in\mathbb{N}^M\). For each \(i\in[M]\), we let _v<sub>i</sub>_ denote the number of instances of _Y<sub>i</sub>_ strictly after the earliest instance of _Y<sub>i</sub>_ following \(X'_{\sigma(i-1)}\) (for _i_=1, this is the earliest instance of _Y_<sub>1</sub> in \(X'\)) up to and including \(X'_{\sigma(i)}\). We think of _v<sub>i</sub>_ as the number of

