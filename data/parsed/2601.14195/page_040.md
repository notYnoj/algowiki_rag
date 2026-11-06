Now, for the sake of argument below, we also construct the smi instance \(I=(A^I,\succ^I)\) from _B_ as in the proof of Theorem 4.4. From Claims 7-8 we know that _B_ is satisfiable \(\Leftrightarrow I\) admits a perfect matching with at most _n+m_ blocking pairs \(\Leftrightarrow I\) admits a perfect matching in which no communication edge between clause and variable gadgets is blocking \(\Leftrightarrow I\) admits a perfect matching _M_ with \(max_{a_r\in A^I}|bp_{a_r}^I(M)|\le 1\). We will now establish the following claims.

**Claim 13.** _If I admits a perfect matching M with_ \(max_{a_r\in A^I}|bp_{a_r}^I(M)|\le 1\) _then J admits a maximum-cardinality matching_ \(M'\) _such that_ \(max_{a_r\in A}|bp_{a_r}^J(M')|\le 1\).

_Proof of Claim 13._ Suppose that _I_ admits a perfect matching _M_ with \(max_{a_r\in A^I}|bp_{a_r}^I(M)|\le 1\). To start, let \(M'=M\). Now, for every communication edge \(\{x_i^r,c_j^s\}\) in _I_, either \(M(x_i^r)\succ_{x_i^r}^Ic_j^s\) or \(M(c_j^s)\succ_{c_j^s}^Ix_i^r\), otherwise they would be a blocking pair (and we know by Claim 8 that this cannot be the case). If \(M(x_i^r)\succ_{x_i^r}^Ic_j^s\), then, for every \(1\le\gamma\le\gamma_*\), add \(M_{i,\gamma,r}^1\) to \(M'\), where \(M_{i,\gamma,r}^1\) is as defined below the construction of the connector gadgets. Otherwise, add \(M_{i,\gamma,r}^2\) (also defined below the connector gadget) to \(M'\). Consider the final matching \(M'\). Clearly, \(M'\) is a maximum-cardinality matching of _J_ (_M_ is a perfect matching of _I_, and the only unmatched agents in _J_, if any, are the agents in _A<sub>r</sub>_ who can never be matched due to empty preference lists). Furthermore, for every agent \(t_{i,\gamma}^{r,1}\), either \(t_{i,\gamma}^{r,2}=M'(t_{i,\gamma}^{r,1})\succ_{t_{i,\gamma}^{r,1}}c_j^s\) or \(p_j^s=M'(c_j^s)\succ_{c_j^s}t_{i,\gamma}^{r,1}\). Similarly, for every agent \(t_{i,\gamma}^{r,7}\), either \(M'(t_{i,\gamma}^{r,7})=t_{i,\gamma}^{r,6}\succ_{t_{i,\gamma}^{r,7}}x_i^r\) or \(M'(x_i^r)\succ_{x_i^r}t_{i,\gamma}^{r,7}\). Hence, no \(t_{i,\gamma}^{r,1}\) and no \(t_{i,\gamma}^{r,7}\) can block with an agent outside the connector gadget, and we already argued below the construction of the connector gadgets that no such agent blocks with agents within the connector gadget. Hence, \(max_{a_r\in A}|bp_{a_r}^J(M')|=max_{a_r\in A^I}|bp_{a_r}^I(M)|\le 1\) as required.

**Claim 14.** _If, for every perfect matching M of I,_ \(max_{a_r\in A^I}|bp_{a_r}^I(M)|>1\)_, then, for every maximum-cardinality_ \(M'\) _of J,_ \(max_{a_r\in A}|bp_{a_r}^J(M')|\ge\frac{\gamma_*}{2}\) .

_Proof of Claim 14._ Clearly, every maximum-cardinality matching of _J_ consists of a perfect matching of _I_ together with either \(M_{i,\gamma,r}^1\) or \(M_{i,\gamma,r}^2\) for every \(1\le i\le n\), \(1\le\gamma\le\gamma_*\) and \(1\le r\le 4\).

We know from Claims 7-8 that _I_ admits a perfect matching _M_ with \(max_{a_r\in A^I}|bp_{a_r}^I(M)|\le 1\) if and only if _I_ admits a perfect matching in which no communication edge between clause and variable gadgets is blocking. Thus, because \(max_{a_r\in A^I}|bp_{a_r}^I(M)|>1\) for all perfect matchings _M_ of _I_, then, for every such _M_, there must exist a communication edge that is blocking. Formally, for some communication edge \(\{x_i^r,c_j^s\}\) (in _I_), both \(c_j^s\succ_{x_i^r}^IM(x_i^r)\) and \(x_i^r\succ_{c_j^s}^IM(c_j^s)\). However, by construction of \(\succ_{x_i^r}\) and \(\succ_{c_j^s}\) (where \(c_j^s\) and \(x_i^r\) are replaced by \(\gamma_*\) many copies of \(t_{i,\gamma}^{r,7}\) and \(t_{i,\gamma}^{r,1}\), respectively), we must also have that \(t_{i,\gamma}^{r,7}\succ_{x_i^r}M'(x_i^r)\) and \(t_{i,\gamma}^{r,1}\succ_{c_j^s}M'(c_j^s)\) for any maximum- cardinality matching \(M'\) of _J_ where \(M\subset M'\), and for any \(1\le\gamma\le\gamma_*\). Now, to minimise \(max_{a_i\in\{x_i^r,c_j^s\}}|bp_{a_i}^J(M')|\), we can do no better than to add \(M_{i,\gamma,r}^1\) for \(1\le\gamma\le\frac{\gamma_*}{2}\) and \(M_{i,\gamma,r}^2\) for<tbc>

2 Gtr i,1
2
2 Gtr i,2
2
2
2
3
3
3
x r i
2
2
2

Figure 13: Illustration of the gap-introducing gadget connections

