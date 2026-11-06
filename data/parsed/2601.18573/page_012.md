_Proof of Claim 2._ Suppose that _I_ admits a perfect matching _M_ such that \(\bigcup_{a_i\in D}bp_{a_i}^I(M)=\varnothing\). Define \(M'=M\cup\{\{b_i^1,b_i^2\};1\le i\le|A|\}\). Then \(M'\) is a perfect matching of _J_. Furthermore, for every \(a_i\in A\), by construction of _J_, we have that \(M(a_i)=M'(a_i)\succ_{a_i}^JB_i^\gamma\) (for \(\gamma\in\{1,2\}\)). Hence, \(bp_{a_i}^J(M')=bp_{a_i}^I(M)\) and for all \(b_q^\gamma\in A_B\), \(bp_{b_q^\gamma}(M')=\varnothing\). Therefore, \(\bigcup_{a_i\in D_J}bp_{a_i}^J(M')=\bigcup_{a_i\in D\cup A_B}bp_{a_i}^J(M')=\varnothing\) as required.

Conversely, suppose that _J_ admits a matching \(M'\) such that \(\bigcup_{a_i\in D_J}bp_{a_i}^J(M')=\varnothing\) and consider the matching \(M=M'\backslash\{\{b_i^1,b_i^2\};1\le i\le|A|\}\). Then for all \(a_i\in A\), it must be true that \(M'(a_i)\succ_{a_i}^JB_i^\gamma\) (for \(\gamma\in\{1,2\}\)), otherwise at least one of \(\{a_i,b_i^1\}\), \(\{a_i,b_i^2\}\) or \(\{b_i^1,b_i^2\}\) would block \(M'\) in _J_, in which case \(\bigcup_{a_i\in A_B}bp_{a_i}^J(M')\neq\varnothing\), a contradiction. Hence, _M_ is a perfect matching of _I_. Furthermore, clearly \(\bigcup_{a_i\in D}bp_{a_i}^I(M)=\bigcup_{a_i\in D}bp_{a_i}^J(M')\subseteq\bigcup_{a_i\in D_J}bp_{a_i}^J(M')=\varnothing\) as required.

Due to this correspondence, and by the fact that 0-Deviator-Perfect-smi-Dec is NP- complete even when preference lists are of length at most 3, we can immediately conclude that 0-Deviator-sri-Dec is NP-complete even when preference lists are of length at most 5.

Now, to extend this result to complete preference lists, we construct the instance \(J'=(A_J,\succ^{J^\prime})\) from _J_ by arbitrarily appending previously unranked agents to the end of the preference lists of all agents. To see that the intractability result holds even when preference lists are complete, observe the following.

**Claim 3.** _J admits a matching M such that_ \(\bigcup_{a_i\in D_J}bp_{a_i}(M)=\varnothing\) _if and only if_ \(J'\) _admits a matching_ \(M'\) _such that_ \(\bigcup_{a_i\in D_J}bp_{a_i}(M')=\varnothing\).

_Proof of Claim 3._ Suppose that _J_ admits a matching _M_ such that \(\bigcup_{a_i\in D_J}bp_{a_i}^J(M)=\varnothing\). We already characterised the set of such matchings in the proof of Claim 2 as complete matchings in _J_. Clearly _M_ also satisfies \(\bigcup_{a_i\in D_J}bp_{a_i}^{J^\prime}(M)=\varnothing\).

Now suppose conversely that \(J'\) admits a matching \(M'\) such that \(\bigcup_{a_i\in D_J}bp_{a_i}^{J^\prime}(M')=\varnothing\). It remains to show that \(M'\) only contains pairs that are acceptable in _J_, in which case also \(\bigcup_{a_i\in D_J}bp_{a_i}^J(M')=\varnothing\). Clearly, it remains true that any agent \(a_i\in A\) is matched to someone on _P<sub>a<sub>i</sub></sub>_ (by the same argument as in Claim 2. Furthermore, suppose that some agent \(b_i^\gamma\) is not matched to \(b_i^{\gamma+1}\) (\(\gamma\in\{1,2\}\) and addition taken modulo 2) in \(M'\). Then, because previously unranked agents were appended to the end of the preference lists, it must be the case that \(b_i^\gamma\succ_{b_i^{\gamma+1}}^{J^\prime} M(b_i^{\gamma+1})\) and \(b_i^{\gamma+1}\succ_{b_i^\gamma}^{J^\prime} M(b_i^\gamma)\). Hence, \(\{b_i^1,b_i^2\}\in bp^{J^\prime}(M')\), which contradicts our assumption \(\bigcup_{a_i\in D_J}bp_{a_i}^{J^\prime}(M')=\varnothing\) as \(\{b_i^1,b_i^2\}\subseteq D_J\). Thus, \(\{b_i^1,b_i^2\}\in M'\), so every match in \(M'\) is acceptable with respect to _J_ too.

This completes the proof of Theorem 3.5.

**Remark 3.6.** _We note that this intractability result could also be derived from a different_ 3-sat _reduction in the proof of Theorem 2.1 of technical report \[9\] on the_ sri _with free edges problem._<sup>1</sup> _However, we include our method for completeness, as it is a simple extension of our reduction in Theorem 3.1._

We can conclude the following intractability result for our original optimisation problem of interest using a similar argument as in the proof of Corollary 3.2.

**Corollary 3.7.** _k_-Deviator-sri _is_ para-NP-hard _with respect to k and, in particular, is_ NP- complete _even when k_=0 _and regardless of whether preference lists are of length at most 5 or complete. Thus,_ Deviator-sri _is_ NP-hard _in equally restricted settings, and cannot be in_ XP _with respect to the optimum parameter value, unless_ P=NP.

<sup>1</sup>Theorem 2.1 in \[9\] says that deciding the existence of a stable matching with free edges, where the set of free edges is spanned by a subset of the vertices, is NP-complete. When taking the set of edges between (acceptable) conformists, i.e., the edges spanned by the set of conformists, as the free edges, the results become equivalent.

