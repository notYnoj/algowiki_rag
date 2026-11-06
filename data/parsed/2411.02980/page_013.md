Instance:an atomic CSP formula \(\Phi=(V,[q],\mathcal{C})\);<br>
Input :two subsets of pinned formulas \(\mathcal{E},\mathcal{F}\subseteq\mathcal{C}^*\), and two partial assignments \(\sigma,\tau\in[q]^\Lambda\)<br>
specified on the same subset \(\Lambda\subseteq V\) of variables;<br>
Output :a pair of assignments \((X,Y)\in[q]^V\times[q]^V\);<br>
if \(\mathcal{E}^\sigma=\mathcal{F}^\tau\) then<br>
   let (X,Y) be drawn according to the coupling of \(\mu_\mathcal{E}^\sigma\) and \(\mu_\mathcal{F}^\tau\) that always satisfies<br>
   \(X_{V\backslash\Lambda}=Y_{V\backslash\Lambda}\);<br>
   return (X,Y);<br>
   if \(\mathcal{F}^\tau\unknown\in\mathcal{E}^\sigma\) then<br>
   choose the smallest \(c\in\mathcal{F}^\tau\backslash\mathcal{E}^\sigma\);<br>
   with probability \(\mu_\mathcal{E}^\sigma(c)\) do<br>
   return<br>
Couple<br>
\((\mathcal{E}\cup\{c\},\mathcal{F},\sigma,\tau)\)<br>
;<br>
   else<br>
   let \(\pi=\mathtt{False}(c)\) and draw a random \(\rho\sim\mu_{\mathcal{F},\mathtt{vbl}(c)}^\tau\);<br>
   return<br>
Couple<br>
\((\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\)<br>
;<br>
   else<br>
   choose the smallest \(c\in\mathcal{E}^\sigma\backslash\mathcal{F}^\tau\);<br>
   with probability \(\mu_\mathcal{F}^\tau(c)\) do<br>
   return<br>
Couple<br>
\((\mathcal{E},\mathcal{F}\cup\{c\},\sigma,\tau)\)<br>
;<br>
   else<br>
   draw a random \(\pi\sim\mu_{\mathcal{E},\mathtt{vbl}(c)}^\sigma\) and let \(\rho=\mathtt{False}(c)\) ;<br>
   return<br>
Couple<br>
\((\mathcal{E},\mathcal{F},\sigma\wedge\pi,\tau\wedge\rho)\)<br>
;

<tbc>Next, observe that in each recursive step, either the size of the symmetric difference \(\mathcal{E}^\sigma\triangleup\mathcal{F}^\tau\) decreases by one, or the number of unassigned variables in \(\sigma\) and \(\tau\) is reduced by at least one. Since Algorithm 2 terminates when \(\mathcal{E}^\sigma=\mathcal{F}^\tau\), the procedure \(\text{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) eventually terminates due to the finiteness of both the number of constraints and the number of variables.

Finally, by applying structural induction in the bottom-up order of recursion, we can verify the following induction hypothesis to ensure the correctness of the coupling:

\(\text{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\text{returns an}(X,Y)\text{such that marginally}X\sim\mu_\mathcal{E}^\sigma\text{and}Y\sim\mu_\mathcal{F}^\tau\text{.}\)

This induction follows the same steps as the one given in the proof of \[WY24, Lemma 3.3\]. The correctness holds as long as the coupling procedure is well-defined and terminates, which we have already established. □

## 4.2. The witness tree and witness assignment.

The novelty of Theorem 4.1 lies in an improved analysis of the coupling procedure (Algorithm 2). This new analysis of the coupling establishes an exponential decay of correlation by leveraging new structural properties of the underlying hypergraph for the CSP formula. The main slackness in previous analysis of the coupling \[WY24\] arises from the use of a combinatorial structure called a 2-tree, originally introduced in \[Alo91\], serving as a witness for a large discrepancy between satisfying assignments. To achieve an improved analysis, we employ a witness tree structure, constructed similarly to the witness tree used in the analysis of the Moser-Tardos algorithm \[MT10\]. This replaces the 2-tree with a new certificate for the discrepancy in the coupling. This use of the Moser-Tardos witness tree is crucial for approaching the satisfiability threshold.

We begin with a formal definition of the execution log for Algorithm 2.

**Definition 4.3** (execution log)**.** Given a run of Algorithm 2 from \(\text{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing)\), the _execution_ \(logL=L(\mathcal{C},c_0)=(c_1,c_2,\dots,c_\ell)\) is a random sequence of (unpinned) constraints from C, constructed as follows:

\(\bullet\) initialize _L_ as the empty list;<tbc>

**Algorithm 2:** \(\text{Couple}(\mathcal{E},\mathcal{F},\sigma,\tau)\) \[WY24\]

