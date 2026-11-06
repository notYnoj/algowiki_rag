**Claim 8.** _I admits a perfect matching M such that_ \(|bp(M)|\le n+m\) _if and only if I admits a perfect matching in which no communication edge is blocking if and only if I admits a perfect matching M with_ \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\).

Together with Claim 7, we can conclude that _B_ is satisfiable if and only if _I_ admits a perfect matching _M_ such that \(max_{a_r\in A}|bp_{a_r}(M)|\le 1\). This establishes that 1-Max-AlmostStable- Perfect-smi is NP-hard, even if all preference lists are of length at most 3, and thus completes the proof that _k_-Max-AlmostStable-Perfect-smi is NP-complete.

**Corollary 4.5.** _The problem_ Minimax-AlmostStable-Max-smi _is_ para-NP-hard _with respect to parameter_ \(\kappa=min_{M\in\mathcal{M}^+}max_{a_i\in A}|bp_{a_i}(M)|\) _even if all preference lists are of length at most 3. By generalisation, this also applies to_ Minimax-AlmostStable-Max-sri.

_Proof._ This follows immediately from Theorem 4.4.

Notice that this result cannot be extended to smi instances with complete preference lists, as all stable matchings of such instances are maximum-cardinality matchings (notice: any two unmatched agents on opposite sides are acceptable and thus would be blocking).

## 4.4 Further Intractability Results

In Theorem 4.1, we proved that, even in the restricted case where _k_=1, _k_-Max-AlmostStable- sri is NP-complete, and we could therefore conclude immediately in Corollary 4.3 that Minimax- AlmostStable-sri is para-NP-hard with respect to the optimal solution value. Here, this problem differs from other almost-stable matching problems such as MinBP-AlmostStable-sri and MinBA-AlmostStable-sri, which are in XP with respect to the optimal solution value \[1, 12\]. Given this strong intractability frontier, it is interesting to know whether Minimax- AlmostStable-sri becomes efficiently solvable for larger optimal solution values. However, we will show below that our original reduction can be extended to show that _k_-Max-AlmostStable- sri remains NP-complete for any positive integer _k_ (although with preference list lengths increasing proportionally to _k_).

**Theorem 4.6.** _k_-Max-AlmostStable-sri _is_ NP-complete _for any fixed positive integer k._

_Proof._ In the proof of Theorem 4.1, we already noted that _k_-Max-AlmostStable-sri is in NP. To prove this new intractability result, we modify the reduction in the remainder of that proof slightly. Specifically, we need to generalise the forcing gadget _G_<sub>_F(a<sub>r</sub>_)</sub>. Recall that the forcing gadget attaches to an agent _a<sub>r</sub>_ with original preference list _P<sub>a<sub>r</sub></sub>_, contributes eight new agents, and enforces that in any matching _M_ where no agent is in more than one blocking pair, there exists some agent \(a_s\in P_{a_r}\) such that \(\{a_r,a_s\}\in M\). Conversely, whenever no such agent _a<sub>s</sub>_ exists on _P<sub>a<sub>r</sub></sub>_, it must be the case that, for any matching, at least one agent is in more than one blocking pair.

We introduce the following parametrised version of the forcing gadget: let \(G_{F_\omega(a_r)}\) (for some \(\omega\in\mathbb{N}\)) denote the generalisation of _G_<sub>_F(a<sub>r</sub>_)</sub> which introduces 3_<sup>w</sup>_-1 additional agents (rather than 8) and has the nested preference cycles constructed as in Proposition 3.4. Specifically, _a<sub>r</sub>_ retains _P<sub>a<sub>r</sub></sub>_ at the top of their preference list, followed by the nested preference list construction. We highlight that _G_<sub>_F_<sub>2</sub>(_a<sub>r</sub>_)</sub>=_G_<sub>_F(a<sub>r</sub>_)</sub>.

Now, for an arbitrary \(G_{F_\omega(a_r)}\), if _a<sub>r</sub>_ is not matched to some agent on _P<sub>a<sub>r</sub></sub>_, then the result from Proposition 3.4 applies, in which case \(min_{M\in\mathcal{M}}max_{a_r\in A}|bp_r(M)|\ge\omega\). The contrapositive of this immediately implies that if \(max_{a_r\in A}|bp_r(M)|<\omega\) for some matching _M_, then \(\{a_r,a_s\}\in M\) for some \(a_s\in P_{a_r}\). Notice that this naturally extends Claim 1.

Now, for the reduction, let \(k\ge 1\) be fixed and let _B_ be a boolean formula given as an instance of the NP-complete problem (2,2)-e3-sat, where _V_={_V_<sub>1</sub>_,V_<sub>2</sub>_,...,V<sub>n</sub>_} is the set of variables and _C_={_C_<sub>1</sub>_,C_<sub>2</sub>_,...,C<sub>m</sub>_} is the set of clauses. We construct an instance \(I=(A,\succ)\)<tbc>

