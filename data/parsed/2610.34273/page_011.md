**Organization.** Section 2 defines the tensor operations and the spectral framework. Section 3 proves simultaneous separation and its entropy consequence. Section 4 develops the polynomial profile, proves its concavity and shifted tripling inequalities, and uses diagonal growth to establish the complete graph bound and its consequences for the questions of \[CVZ19\]. Section 5 defines the formal polynomial system and proves the operational barrier. Appendix A gives the flattening and rank bounds and the triangle-cover argument; Appendix B gives the tensor-language proof of the minimum-cut formula for asymptotic subrank.

## 2 Preliminaries

In this section, we define the tensor operations and the asymptotic parameters used in the proof. Our spectral framework is the asymptotic spectrum theory developed by Strassen \[Str88, Section 3\]; Wigderson and Zuiddam \[WZ26\] give a detailed account of its semiring formulation, applications, and extensions. We first specify tensor arrays and their coordinate operations. We then identify arrays that differ only by independent coordinate permutations within their legs, define the resulting tensor semiring, and introduce the asymptotic parameters and graph tensors. Unless a coefficient semiring R is explicitly specified, all tensors are over C.

We write N={0,1,2_,..._} and \[_q_\]<sub>0</sub>={0_,...,q_-1} for every positive integer _q_. All coordinate indices start at 0. We use log for the logarithm to base 2 and ln for the natural logarithm. For a positive integer _s_, a _probability vector_ is a vector \(\theta=(\theta_1,\dots,\theta_s)\) with \(\theta_h\ge 0\) for \(1\le h\le s\) and \(\sum_{h=1}^s\theta_h=1\). Its entropy is

\(H(\theta)=-\sum_{h=1}^s\theta_h\mathrm{ln}\theta_h,\)

where 0ln0=0. Thus entropy factors below take the form \(e^{H(\theta)}\).

### 2.1 Tensor coordinates and operations

We begin with coordinate operations, and then specify which coordinate choices are identified. The distinction matters when several tensor blocks share a leg.

**Definition 2.1** (tensor arrays)**.** Let R be a commutative semiring: (R,+<sub>R</sub>,0<sub>R</sub>) and \((\mathcal{R},\cdot_\mathcal{R},1_\mathcal{R})\) are commutative monoids, multiplication distributes over addition, \(0_\mathcal{R}\cdot_\mathcal{R}x=0_\mathcal{R}\) for all \(x\in\mathcal{R}\), and \(1_\mathcal{R}\neq 0_\mathcal{R}\). For positive integers _k,n_<sub>1</sub>_,...,n<sub>k</sub>_, a _k-th order tensor array_ of dimension (_n_<sub>1</sub>_,...,n<sub>k</sub>_) over R is a function

\(T:[n_1]_0\times\cdots\times[n_k]_0\longrightarrow\mathcal{R}.\)

We write _T_<sub>_i_<sub>1</sub>_,...,i<sub>k</sub>_</sub> for its value at (_i_<sub>1</sub>_,...,i<sub>k</sub>_) and set dim(_T_)=(_n_<sub>1</sub>_,...,n<sub>k</sub>_). The _d_-th index, for \(1\le d\le k\), is called the _d_-th _leg_. Let Arr_<sub>k</sub>_(R) be the disjoint union of these array spaces over all positive dimension vectors. When R=C, we call its elements _complex k-th order tensor arrays_. An array is nonzero if its support is nonempty.

For \(A,B\in\mathsf{Arr}_k(\mathcal{R})\) with the same dimension (_n_<sub>1</sub>_,...,n<sub>k</sub>_) and \(c\in\mathcal{R}\), define their _entrywise sum_ and scalar multiple by<tbc>

\((A+B)_{i_1,\dots,i_k}=A_{i_1,\dots,i_k}+_\mathcal{R}B_{i_1,\dots,i_k},(cA)_{i_1,\dots,i_k}=c\cdot_\mathcal{R}A_{i_1,\dots,i_k}\)

<tbc>for \(0\le i_d<n_d\) and \(1\le d\le k\). The _support_ of _T_ is<tbc>

\(\mathrm{supp}(T)=\big\{(i_1,\dots,i_k)\in[n_1]_0\times\cdots\times[n_k]_0:T_{i_1,\dots,i_k}\neq 0_\mathcal{R}\big\}.\)

