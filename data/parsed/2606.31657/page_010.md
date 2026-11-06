## 2.1 Sensitivity

Let \((\Omega,d)\) be a finite metric space and let \(\mu,\nu\) be distributions over \(\Omega\). The _earth mover’s distance_ between \(\mu\) and \(\nu\) is

\(\mathsf{EMD}_d(\mu,\nu):=inf_{\pi\in\Pi(\mu,\nu)}\sum_{x,y\in\Omega} d(x,y)\pi(x,y),\)

where \(\Pi(\mu,\nu)\) denotes the set of all couplings of \(\mu\) and \(\nu\). When the metric is clear from context we write simply \(\mathsf{EMD}(\mu,\nu)\). If _d_ is the discrete metric on \(\Omega\), i.e., _d(x,y_)=1 when \(x\neq y\) and 0 otherwise, then \(\mathsf{EMD}_d(\mu,\nu)=\mathsf{TV}(\mu,\nu)\), the total variation distance between \(\mu\) and \(\nu\).

Consider a problem in which an input instance _I_ consists of elements _e_<sub>1</sub>_,...,e<sub>n</sub>_ and the output space is a metric space \((\Omega,d)\). For an element \(e\in I\), let _I-e_ denote the instance obtained by deleting _e_. The _sensitivity_ of a (possibly randomized) algorithm A at _I_ is

\(\mathsf{Sens}(\mathcal{A},I):=max_{i\in[n]}\mathsf{EMD}_d(\mathcal{A}(I),\mathcal{A}(I-e_i)),\)

where we identify A(_I_) with its output distribution.

## 2.2 Locally Testable s

For \(w\in\Sigma^n\) and a subset \(C\subseteq\Sigma^n\), we set \(\delta_\mathrm{H}(w,C):=min_{c\in C}\delta_\mathrm{H}(w,c)\).

**Definition 2.1** (Error-correcting code)**.** Let \(n,k\in\mathbb{N}\) with \(n\ge k\) and let \(\Sigma\) be a finite alphabet. A _(block) error-correcting code_ of length _n_ and message length _k_ over \(\Sigma\) is a pair (_C,f_), where \(C\subseteq\Sigma^n\) and the encoder \(f:\Sigma^k\rightarrow C\) is a bijection. The _rate_ of the code is _r=k/n_, and its _(relative) distance_ is \(min_{c,c^\prime\in C,c\neq c^\prime}\delta_\mathrm{H}(c,c')\). We often identify the code with the subset _C_ when the encoder is clear from context.

**Definition 2.2** (Linear code)**.** A code (_C,f_) over F_<sub>p</sub>_ is _linear_ if _C_ is a linear subspace of \(\mathbb{F}_p^n\), equivalently if _f_ is a linear map. The (absolute) distance of a linear code equals the minimum Hamming weight of a nonzero codeword.

**Definition 2.3** (Locally testable codes)**.** Let \(r,\delta,\kappa\in\mathbb{R}_{\ge 0}\), \(q,\theta\in\mathbb{N}\). We say an error-correcting code (_C,f_) is a _locally testable code_ (LTC) with detection probability \(\kappa\), _q_ queries, and variable degree \(\theta\) if the following properties hold:

• There exists a collection S of _q_-subsets of \[_n_\] such that each subset _S_ is associated with a set \(V_S\subseteq\Sigma^S\) called _allowed local views_, satisfying \(c|_S\in V_S\) for all \(c\in C\), and<tbc>

<tbc>\(\forall w\in\Sigma^n:\mathbf{Pr}_{S\sim\mathcal{S}}\left[w|_S\notin V_S\right]\ge\kappa\cdot\delta_\mathrm{H}(w,C),\)<tbc>

<tbc>where _S_∼S denotes the uniform distribution over S.<tbc>

• For any \(i\in[n]\), we have \(\sum_{S\in\mathcal{S}}\unknown\left[i\in S\right]\le\theta\).

When we need to emphasize the local tests, we denote the LTC by \((C,f,\mathcal{S},\mathcal{V})\), where \(\mathcal{V}=\{V_S\}_{S\in\mathcal{S}}\).

**Definition 2.4** (Systematic code)**.** Let \(n,k\in\mathbb{N}\) with \(n\ge k\) and let \(\Sigma\) be a finite alphabet. Let \(\pi:\Sigma^n\rightarrow\Sigma^k\) be the projection onto the first _k_ coordinates. A _systematic code_ of length _n_ and message length _k_ over \(\Sigma\) is an error-correcting code (_C,f_) with an encoder \(f:\Sigma^k\rightarrow\Sigma^n\) such that \(\pi\circ f=\mathrm{id}_{\Sigma^k}\). Thus the message _x_ appears verbatim as the first _k_ entries of the codeword _f(x_). We also say that a code \(C\subseteq\Sigma^n\) is _systematic_ if it admits such an encoder.

