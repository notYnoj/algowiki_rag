<tbc>For a random _k_-SAT formula \(\Phi\sim\Phi(k,n,\lfloor\alpha n\rfloor)\), we say that \(\Phi\) is _M-loose_ if, with high probability over the pair \((\Phi,\sigma)\), where \(\sigma\sim\mu_\Phi\), all variables \(v\in V\) are _M_-loose with respect to \(\sigma\).

Looseness is conjectured to hold for random _k_-SAT up to the clustering threshold \(\alpha_\mathrm{clust}\approx 2^k(\mathrm{ln}k)/k\) \[AC08, Conjecture 1\]. Here, we prove looseness at the considered densities.

**Theorem 4.13** (looseness of random _k_-SAT)**.** _Under the condition of Theorem 1.2, the random k-SAT formula_ \(\Phi(k,n,\lfloor\alpha n\rfloor)\) _is_ (poly(_k_)log_n)-loose._

_Proof._ We will prove Theorem 4.13, by modifying the random process introduced in Definition 4.8 to find a local neighbor of a solution. The modified process proceeds as follows.

The input consists of an atomic CSP formula \(\Phi=(V,\lfloor q\rfloor,C)\), a solution \(\sigma^\mathrm{in}\in\Omega_\Phi\), and a variable \(v\in V\) . The process produces an output assignment \(\sigma^\mathrm{out}\in\Omega_\Phi\) as described below:

(1) Choose an arbitrary value \(x\in\lfloor q\rfloor\backslash\left\{\sigma^\mathrm{in}(v)\right\}\).<tbc>

(2) Run the random process in Definition 4.8 with the following alterations:<tbc>

\(\bullet\) The initial sets of constraints are E<sub>0</sub>=F<sub>0</sub>=C, and the initial partial assignments are both specified only at _v_, with \(\sigma_0(v)=\sigma^\mathrm{in}(v)\) and \(\tau_0(v)=x\);<tbc>

\(\bullet\) Set X as \(\sigma^\mathrm{in}\) and \(\mathfrak{Y}\sim\mu_C^{\tau_0}\). That is, \(\mathfrak{Y}\in\Omega^C\) is chosen uniformly at random conditioned on Y(_v)=x_.<tbc>

<tbc>Let \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) be the outcome of the random process.<tbc>

(3) If the outcome \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) satisfy that |**_T_**|=_M_, then let \(\sigma^\mathrm{out}\leftarrow\sigma^\mathrm{in}\). Otherwise, update \(\sigma^\mathrm{in}\) by changing the values of the variables assigned in \(\tau\) to \(\tau\), i.e. set \(\sigma^\mathrm{out}\leftarrow\tau\wedge\sigma_{V\backslash\Lambda(\tau)}^\mathrm{in}\).

We can make the following observations about this process:

\(\bullet\) Similar to Algorithm 2 or Definition 4.8, this random process is an idealized algorithm, as it requires sampling from the non-trivial distribution \(\mu_C^{\tau_0}\). The process is constructed to prove the looseness of random CSP formulas (Theorem 4.13).<tbc>

\(\bullet\) In Item 2, the sets of pinned constraints \(\mathcal{E}^\sigma\) and \(\mathcal{F}^\tau\) may have discrepancies at the constraints involving _v_. Since these constraints are connected in \(G_\Phi\), the proof for Proposition 4.5 hold in this setting as well.<tbc>

\(\bullet\) In Item 3, if the outcome \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) satisfies |**_T_**|_\<M_, then by Definition 4.8, we must have \(\mathcal{E}^\sigma=\mathcal{F}^\tau\). Since \(\mathfrak{X}=\sigma^\mathrm{in}\), the output assignment \(\sigma^\mathrm{out}\) is a satisfying assignment with \(\sigma^\mathrm{out}(v)\neq\sigma^\mathrm{in}(v)\) and \(d_\mathrm{Ham}(\sigma^\mathrm{in},\sigma^\mathrm{out})\le kM\).

Finally, Theorem 4.13 follows from applying the same argument used in the proofs of Theorems 1.9 and 1.11, by invoking Theorem 4.1 to the setting where the initial instances differ in one variable rather than in one constraint. □

## 5. Linear program for counting and sampling

In this section, we introduce a linear programming approach that translates the coupling result from the previous section into algorithms for counting and sampling, and prove Theorem 3.2. Similar to the coupling, this linear program is adapted from the one in \[WY24\], with key modifications to accommodate the criticality of random instances.

### 5.1. Marginal probabilities.

We introduce the marginal probabilities associated with the coupling procedure, which correspond to the variables of the linear program.

Consider an atomic CSP formula \(\Phi=(V,\lfloor q\rfloor,C)\), and let \(c_0\in C\) be an arbitrary constraint. Fix an integer \(M\ge 1\). Recall the random process \(P^\mathrm{cp}=P_M^\mathrm{cp}=\{(\mathcal{E}_t,\mathcal{F}_t,\sigma_t,\tau_t,T_t,\varsigma_t)\}_{t\ge 0}\) and its outcome distribution \(\mu^\mathrm{cp}=\mu_M^\mathrm{cp}\), along with their supports V<sup>cp</sup> and L<sup>cp</sup>, as constructed in Definition 4.8.

We define a family of marginal probabilities induced by the random process _P_<sup>cp</sup>.

**Definition 5.1** (marginal probabilities)**.** Let _X_ and _Y_ be generated as follows:

\(\bullet\) draw \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\sim\mu^\mathrm{cp}\);<tbc>

\(\bullet\) draw \(X\sim\mu_\mathcal{E}^\sigma\), and similarly \(Y\sim\mu_\mathcal{F}^\tau\).<tbc>

