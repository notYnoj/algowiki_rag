<tbc>exactly two unnegated and two negated occurrences of each literal in _B_. Notice that the choice of first or second occurrence in the preference list construction within the variable gadgets will be irrelevant, and that this is an arbitrary choice we make. This completes the construction of _I_. Notice that the construction of each gadget can be performed in constant time due to the bounded size of each gadget, so _I_ can be constructed from _B_ in polynomial time.

We will now show that the gadget \(G_{F(v_i^z)}\) does indeed force \(v_i^z\) to be matched to someone on \(P_{v_i^z}\) for any matching in which no agent is in more than one blocking pair.

**Claim 1.** _Let_ \(G_{F(v_i^z)}\) _be an occurrence of the forcing gadget, and let M be a matching of I. If_ \(M(v_i^z)\notin P_{v_i^z}\)_, then_ \(max_{a_r\in A[G_{F(v_i^z)}]}|bp_{a_r}(M)\cap E[G_{F(v_i^z)}]|>1\).<sup>2</sup>

_Proof of Claim 1._ Suppose that \(M(v_i^z)\notin P_{v_i^z}\). Then at least one agent in each of \(\{v_i^z,f_i^{1,z},f_i^{2,z}\}\), \(\{f_i^{3,z},f_i^{4,z},f_i^{5,z}\}\) and \(\{f_i^{6,z},f_i^{7,z},f_i^{8,z}\}\) must be matched to someone worse than both other members of their preference cycle. Without loss of generality (by symmetry in the preference construction), let these be \(f_i^{2,z},f_i^{5,z}\) and \(f_i^{8,z}\). Notice that immediately we must have \(\{\{f_i^{1,z},f_i^{2,z}\}\), \(\{f_i^{4,z},f_i^{5,z}\}\), \(\{f_i^{7,z},f_i^{8,z}\}\}\subseteq bp(M)\). Notice, furthermore, that we can match at most two of the agents \(f_i^{2,z},f_i^{5,z}\) and \(f_i^{8,z}\) to each other. However, again, these three agents form a preference cycle of odd length. Without loss of generality, suppose that \(f_i^{8,z}\) remains unmatched, then \(\{f_i^{5,z},f_i^{8,z}\}\in bp(M)\). Hence, \(|bp_{f_i^{5,z}}(M)|=|bp_{f_i^{8,z}}(M)|=2>1\) and both of these blocking pairs are within \(G_{F(v_i^z)}\), i.e., it must be the case that \(max_{a_r\in A[G_{F(v_i^z)}]}|bp_{a_r}(M)\cap E[G_{F(v_i^z)}]|>1\).

Notice that, by the contrapositive of Claim 1, if \(max_{a_r\in A[G_{F(v_i^z)}]}|bp_{a_r}(M)\cap E[G_{F(v_i^z)}]|\le 1\), then \(M(v_i^z)\in P_{v_i^z}\). Conversely, if \(\{\{f_i^{1,z},f_i^{2,z}\},\{f_i^{3,z},f_i^{4,z}\},\{f_i^{5,z},f_i^{6,z}\},\{f_i^{7,z},f_i^{8,z}\}\}\subseteq M\) and \(M(v_i^z)\in P_{v_i^z}\), then, within the gadget \(G_{F(v_i^z)}\), _M_ admits precisely the blocking pairs \(\{f_i^{4,z},f_i^{5,z}\}\) and \(\{f_i^{6,z},f_i^{8,z}\}\) (and possibly blocking pairs involving \(v_i^z\) and agents outside of \(G_{F(v_i^z)}\)), so no agent within \(G_{F(v_i^z)}\) is in more than one blocking pair with other agents within \(G_{F(v_i^z)}\).

Next, we will establish several properties about the full variable gadgets construction.

**Claim 2.** _Let G<sub>V<sub>i</sub></sub> be an occurrence of the variable gadget, and let M be a matching of I. Then_

• \(ifmax_{a_r\in A[G_{V_i}]}|bp_{a_r}(M)\cap E[G_{V_i}]|\le 1\) _then_ \(\{\{v_i^T,v_i^1\},\{v_i^F,v_i^2\}\}\subset M\) _or_ \(\{\{v_i^T,v_i^2\},\{v_i^F,v_i^1\}\}\subset M\);<tbc>

• _if_ \(\{\{v_i^T,v_i^1\},\{v_i^F,v_i^2\}\}\unknown\subset M\wedge\{\{v_i^T,v_i^2\},\{v_i^F,v_i^1\}\}\unknown\subset M\)_, then_ \(max_{a_r\in A[G_{V_i}]}|bp_{a_r}(M)\cap E[G_{V_i}]|>1\);<tbc>

• _if_ \(\{\{v_i^T,v_i^1\},\{v_i^F,v_i^2\}\}\subseteq M\)_, then_ \(bp(M)|_{G_{V_i}}=bp(M)|_{G_{F(v_i^1)}}\cup bp(M)|_{G_{F(v_i^2)}}\).<sup>3</sup><tbc>

<sup>2</sup>We use the notation \(A[G_{F(v_i^z)}]\) to refer to the agents contained in \(G_{F(v_i^z)}\) and the notation \(E[G_{F(v_i^z)}]\) to refer to the edges of the acceptability graph induced by \(G_{F(v_i^z)}\). <sup>3</sup>We use the notation \(bp(M)|_{G_{F(v_i^z)}}\) to indicate that we restrict the set of blocking pairs admitted by _M_ to those that involve only pairs both contained in the part \(G_{F(v_i^z)}\) of _I_.

