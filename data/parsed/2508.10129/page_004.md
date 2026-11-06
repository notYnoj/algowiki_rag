_v<sub>j</sub>_ are _matched_. If there is no pair \(e\in M\) such that \(v_i\in e\), then we say that _v<sub>i</sub>_ is _unmatched_, denoted as \(M(v_i)=\perp\). We assume that every agent _v<sub>i</sub>_ prefers to be matched with an acceptable agent over being unmatched \(\perp\).

Given a matching _M_ of P, a pair \(\{v_i,v_j\}\in E(G)\) of agents is a _blocking_ pair of and _blocks M_ if \(\{v_i,v_j\}\notin M\) and the following two conditions hold:

(i) _v<sub>i</sub>_ is unmatched or prefers _v<sub>j</sub>_ to _M(v<sub>i</sub>_), and

(ii) _v<sub>j</sub>_ is unmatched or prefers _v<sub>i</sub>_ to _M(v<sub>j</sub>_).

We call a matching _M stable_ if there is no blocking pair; otherwise we call it _unstable_. If every agent is matched, then we call the matching _perfect_.

## Problem definitions.

We are ready to formally define the computational problems studied in this paper.

Minimum Blocking Pairs SMI (in short Min-BP-SMI)<br>
**Input:** A marriage instance \(\mathcal{P}=(U\cup W,(\unknown_i)_{i\in U\cup W})\) with strict preferences and a non-negative integer _k_.<br>
**Task:** Find a matching _M_ of size \(|M|\ge k\) with minimum number of blocking pairs.

Minimum Blocking Pairs SRI (in short Min-BP-SRI)<br>
**Input:** A roommates instance \(\mathcal{P}=(V,(\unknown_i)_{i\in V})\) with strict preferences.<br>
**Task:** Find a matching with minimum number of blocking pairs.

The standard parameterized decision variants of Min-BP-SMI and Min-BP-SRI, called Min-BP-SMI- dec and Min-BP-SRI-dec, additionally have as input a number \(\beta\), and asks whether there exists a solution with at most \(\beta\) blocking pairs.

Now, we turn to preferences with ties.

Maximum Size-SMTI (in shortMax-SMTI)<br>
**Input:** A marriage instance \(\mathcal{P}=(U\cup W,(\unknown_i)_{i\in U\cup W})\) with incomplete preferences possibly containing ties.

**Task:** Find a stable matching _M_ with maximum size.

The parameterized decision variant of Max-SMTI, called Max-SMTI-dec, has an additional parameter _k_ in the input and asks whether there exists a stable matching of size at least _k_.

For more details on algorithmic complexity of stable matching problems, we refer to the textbook by Manlove \[21\].

## Fixed-parameter approximability.

We assume basic knowledge of parameterized complexity and refer the textbook by Cygan et al. \[8\] for more details.

The definitions for fixed-parameter approximability are based on the definitions by Marx \[23\].

We define an _optimization problem_ as a 4-tuple \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\), where

- \(\Pi\) is a set of instances,<tbc>

- sol is a function that assigns to each instance _I_ a set consisting of all feasible solutions, i.e., for each \(I\in\Pi\), sol(_I_) is a collection of feasible solutions,<tbc>

- cost is a function that assigns to each instance _I_ and each feasible solution \(x\in\mathrm{sol}(I)\) an integer that describes the quality of the solution,<tbc>

- goal is min for minimization problems and max for maximization problems.

For instance, for the Min-BP-SMI problem, \(\Pi\) consists of all tuples _I_=(P_,k_) such that P is a marriage instance with strict preferences, _k_ is a non-negative integer, sol(_I_) consists of all matchings of size at least _k_, cost(_M,I_) is the number of blocking pairs in _M_, and goal=min.

**Definition 1** (Polynomial-time approximation algorithms)**.** To define approximation algorithms, let us first consider minimization problems. Let \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) be a minimization problem and _I_ an instance of \(\Pi\).

For a given constant \(\rho\ge 1\), we say that an algorithm _A_ is a _factor-_\(\rho\) _approximation algorithm_ for \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) if it outputs a solution _x_ with \(\mathrm{cost}(x,I)\le\rho\cdot\mathrm{OPT}\), where OPT(_I_) is the cost of an optimal solution of _I_, i.e., \(\mathrm{OPT}(I)=\mathrm{argmin}_{x\in\mathrm{sol}}\mathrm{cost}(x,I)\). If \((\Pi,\mathrm{sol},\mathrm{cost},\mathrm{goal})\) is a maximization problem instead, then we require<tbc>

