## 3 (Non-)Termination Verification as Constraint Solving

We explain how to encode (non-)termination verification to constraint solving.

Following \[30\], we formalize our target class pwCSP of predicate constraint satisfaction problems parametrized by a first-order theory T .

**Definition 6.** Given a formula \(\phi\), let \(ftv(\phi)\) be the set of free term variables and \(fpv(\phi)\) be the set of free predicate variables in \(\phi\).

**Definition 7.** A pwCSP is defined as a pair (C,R) where C is a finite set of clauses of the form

\(\phi\vee\left(\vee_{i=1}^\ell X_i(\widetilde{t}_i)\right)\vee\left(\vee_{i=\ell+1}^m\neg X_i(\widetilde{t}_i)\right)\) (4)

and \(\mathcal{R}\subseteq fpv(\mathcal{C})\) is a set of predicate variables that are required to denote _well- founded_ relations. Here, \(0\le\ell\le m\). Meta-variables _t_ and \(\phi\) range over T -terms and T -formulas, respectively, such that \(ftv(\phi)=\emptyset\). Meta-variables _x_ and _X_ range over term and predicate variables, respectively.

A pwCSP (C,R) is called CHCs (constrained Horn clauses, \[9\]) if \(\mathcal{R}=\emptyset\) and \(\ell\le 1\) for all clauses \(c\in\mathcal{C}\). The class of CHCs has been widely studied in the verification community \[12, 14, 27, 35\].

**Definition 8.** A _predicate substitution_ \(\sigma\) is a finite map from predicate variables _X_ to closed predicates of the form \(\lambda x_1,\dots,x_{\mathrm{ar}(X)}.\phi\). We write \(\mathrm{dom}(\sigma)\) for the domain of \(\sigma\) and \(\sigma(\mathcal{C})\) for the application of \(\sigma\) to C.

**Definition 9.** A predicate substitution \(\sigma\) is a _(genuine) solution_ for (C,R) if (1) \(fpv(\mathcal{C})\subseteq\mathrm{dom}(\sigma)\); (2) \(\vDash\wedge\sigma(\mathcal{C})\) holds; and (3) for all \(X\in\mathcal{R}\), \(\sigma(X)\) represents a well-founded relation, that is, \(\mathrm{sort}(\sigma(X))=(\widetilde{s},\widetilde{s})\rightarrow\bullet\) for some sequence \(\widetilde{s}\) of sorts and there is no infinite sequence \(\widetilde{v}_1,\widetilde{v}_2,\dots\) of sequences \(\widetilde{v}_i\) of values of the sorts \(\widetilde{s}\) such that \(\vDash\rho(X)(\widetilde{v}_i,\widetilde{v}_{i+1})\) for all \(i\ge 1\).

### Encoding termination.

Given a set of initial state \(\iota(\widetilde{x})\) and a transition relation \(\tau(\widetilde{x},\widetilde{x}')\), the termination verification problem is expressed by the pwCSP (C,R) where R={_R_}, and C consists of the following clauses.

\(\iota(\widetilde{x})\Longrightarrow I(\widetilde{x})\tau(\widetilde{x},\widetilde{x}')\wedge I(\widetilde{x})\Longrightarrow I(\widetilde{x}')\tau(\widetilde{x},\widetilde{x}')\wedge I(\widetilde{x})\Longrightarrow R(\widetilde{x},\widetilde{x}')\)

We use \(\phi\Longrightarrow\psi\) as syntax sugar for \(\neg\phi\vee\psi\), so this is a pwCSP. The well- founded relation _R_ asserts that \(\tau\) is terminating. We also consider an invariant _I_ for \(\tau\) to avoid synthesizing ranking functions on unreachable program states.

