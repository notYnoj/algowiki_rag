Given that we have shown that at the end of the best-response dynamics in BR-Sim, the players are playing an approximate equilibrium, it only remains to construct a decoding function for the players to recover their own sequence of actions in the dynamics. Observe that BR-Sim outputs the list of update steps across all counters, which allows each player to simulate the history of the approximate counts. Therefore the decoding function is straightforward: first call ExtractCount to extract the history of counts in the best-response dynamics; then each player _i_ first forms her own initial flow by picking the shortest path in her action set, and then at every time step _t_ such that \((tmodn)\equiv i\), she decides whether to switch to a best-response with respect to the counts. Since her best response, after breaking ties lexicographically, is uniquely determined, in this way she is able to determine which path she is playing along at the end of the dynamics, which is her part of the approximate equilibrium. The full description of the algorithm ExtractPath is presented in Algorithm 6.

**Algorithm 6** \(\text{ExtractPath}((s_i,d_i),\{U_e\}_{e\in E},\alpha,r)\)

**Input:** a player _i_’s source-destination pair (_s<sub>i</sub>,d<sub>i</sub>_), message containing update steps \(\{U_e\}_{e\in E}\) for the \(\{\text{Counter}(e)\}_{e\in E}\), best-response parameter \(\alpha\) and refinement parameter

**Initialize:** \(l=\alpha-2\lambda mr-\lambda m\)

**for** each edge \(e\in E\):

Let _C<sub>e</sub>_=ExtractCount(_U<sub>e</sub>,r,T_) be the history of approximate counts

**Form the initial flow:**

Let _f_<sup>(_i_)</sup> be the _s<sub>i</sub>-d<sub>i</sub>_ path with the fewest number of edges, break ties lexicographically

**for** \(t=1,\dots,\frac{mn}{l}\) :

Let flow \(g=(C_e(tn+i))_{e\in E}\)

**if** _f_<sup>(_i_)</sup> is not an \(\alpha\)-best-response w.r.t. _g_

Switch _f_<sup>(_i_)</sup> to a best-response w.r.t. _g_

**Output:** the final _s<sub>i</sub>-d<sub>i</sub>_ path _f_<sup>(_i_)</sup>

**Claim 5.** _Suppose that_ \(\text{BR-Sim}((G,\{(s_i,d_i)\}_i,c),\alpha,r)\) _outputs a set of update step lists_ \(\{U_e\}_{e\in E}\)_, then for each player i, her output flow from the instantiation_ \(\text{ExtractPath}((s_i,d_i),\{U_e\}_{e\in E},\alpha,r)\) _is the same as the final flow in the best-response dynamics in_ BR-Sim.

**Theorem 7.** _Fix any_ \(\varepsilon>2\lambda m\)_. Let_ \(r=\frac{\varepsilon-2\lambda m}{6\lambda m}\) _, and_ \(\alpha=\varepsilon-\lambda mr-\lambda m\)_. Then given any routing game instance_ \(\Gamma=(G,\{(s_i,d_i)\}_i,c)\)_, the coordination protocol_ \((\text{BR-Sim}(\Gamma,\alpha,r),\text{ExtractPath}((s_i,d_i),\{U_e\}_{e\in E},\alpha,r))\) _coordinates the players to play an_ \(\varepsilon\)_-approximate equilibrium flow and has coordination complexity of_

\(\widetilde{O}\left(\frac{\lambda m^2n}{(\varepsilon-2\lambda m)^2}\right).\)

_Proof._ Given the parameters we choose, the players will end up playing an \(\varepsilon\)-approximate equilibrium by Lemma 16.

Next, we bound the encoding length of the output from BR-Sim. Recall that \(l=\alpha-2\lambda mr-\lambda m\), and each time a player makes a deviation in the best-response dynamics, the potential function decreases by _l_. By the same analysis of Lemma 16, we know that the total number of deviations that occur in the dynamics (across all edges) is bounded _T=mn/l_. Since each counter updates its count only if the count is changed by _r_, the total number of updates across all counters is bounded by _mT/r_. Also, the total length of each counter is bounded (_T_+1)_n_. By Claim 4, the output list of update steps among all counters has encoding<tbc>

