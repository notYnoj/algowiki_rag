<tbc>the instance. The freezing paradigm and its variant are also applied by all recent counting/sampling algorithms for random CSPs \[GGGY21, HWY23, CGG<sup>+</sup>24\]. Hence, we naturally circumvent this barrier for random CSPs.

However, the bound in \[WY24\] has an exponent of 2+_o<sub>q</sub>_(1), which only approaches 2 for large domain sizes and rises to ≈4.82 for the worst-case of atomic CSPs with Boolean domains, such as for _k_-SAT. The way we improve this exponent to 1+_o_(1) is by leveraging _a new analysis of the coupling procedure based on the structural properties of random CSPs_. Random CSPs enjoy good structural properties such as large constraint expansion, as already observed and utilized in \[HWY23\]. Our main novelty lies in designing a new analysis for the coupling in \[WY24\] that takes advantage of this structural property. Technically, we replace the 2-tree witness employed in the analysis of the coupling in \[WY24\] by a denser witness structure, constructed similarly as the witness tree structure for analyzing the Moser-Tardos algorithm \[MT10\], thereby achieving the improved bound.

This refined analysis of the coupling procedure immediately establishes properties such as replica symmetry and non-reconstruction at the same density. We believe this new analysis is of independent interest and may have further applications in both bounded-degree and random CSPs.

### 1.4. Organization.

This paper is organized as follows.

In Section 2, we formally define atomic CSPs and introduce relevant preliminaries and notations.

In Section 3, we define the main structural condition (Condition 3.1), stated generally with respect to atomic CSPs. We then claim that this condition suffices for efficient sampling and counting of solutions (Theorem 3.2), and prove that both the random _k_-SAT instance in Theorem 1.2 and the random hypergraph coloring instance in Theorem 1.4 satisfy this condition.

Section 4 and Section 5 together proves Theorem 3.2, which concludes the proof of Theorem 1.2 and Theorem 1.4. Specifically, Section 4 introduces the coupling in \[WY24\] with our new analysis and establishes Theorem 1.7. Section 5 shows how to effectively convert this coupling into an efficient counting and sampling algorithm.

In Section 4.4, we prove the properties related to the correlation decay phenomenon and the geometry of the solution space, namely Theorems 1.9, 1.11 and 4.13, using the refined analysis of the coupling developed in Section 4.

## 2. Preliminaries

### 2.1. Atomic CSPs and related notations.

A constraint satisfaction problem (CSP) is described by a collection of constraints defined on a set of variables. Formally, an instance of a constraint satisfaction problem, called a _CSP formula_, is denoted by \(\Phi=(V,[q],\mathcal{C})\). Here, _V_ is a set of _n_=|_V_| random variables, where each random variable \(v\in V\) has a finite domain \[_q_\]. The collection of local constraints is given by C, where each constraint \(c\in\mathcal{C}\) is a function defined as \(c:[q]^{\mathrm{vbl}(c)}\rightarrow\{\mathsf{True},\mathsf{False}\}\) over a subset of variables denoted as \(\mathrm{vbl}(c)\subseteq V\) . For any subset of of constraints \(\mathcal{E}\subseteq\mathcal{C}\), denote \(\mathrm{vbl}(\mathcal{E})\unknown\bigcup_{c\in\mathcal{E}}\mathrm{vbl}(c)\). An assignment \(\sigma\in[q]^V\) is called _satisfying_ for \(\Phi\) if

\(\Phi(\sigma)\unknown\wedge_{c\in\mathcal{C}}c\left(\sigma_{\mathrm{vbl}(c)}\right)=\mathsf{True}.\)

Furthermore, we say \(\Phi\) is _satisfiable_ if at least one satisfying assignment to \(\Phi\) exists. We use \(\Omega_\Phi\) to denote the set of satisfying assignments to \(\Phi\), and use \(Z(\Phi)=|\Omega_\Phi|\) to denote the number of satisfying assignments to \(\Phi\).

We say a constraint \(c\in\mathcal{C}\) is defined by _atomic bad events_, or simply, _atomic_, if it is violated by exactly one configuration in \[_q_\]<sup>vbl(_c_)</sup>. For an atomic constraint _c_, we use False(_c_) to denote its only violating configuration in \[_q_\]<sup>vbl(_c_)</sup>. Moreover, when all constraints in C are atomic, we say \(\Phi\) is atomic. It is important to note that any constraint with a constant number _N_ of violating configurations can be decomposed into _N_ atomic constraints. As a result, both SAT and hypergraph coloring instances fall within the category of atomic CSPs.

#### 2.1.1. _Notations for (partial) assignments._

For a partial assignment \(\sigma\in[q]^\Lambda\) specified over a subset of variables \(\Lambda\subseteq V\) , we use \(\Lambda(\sigma)=\Lambda\) to denote the set of assigned variables in \(\sigma\). For any partial<tbc>

