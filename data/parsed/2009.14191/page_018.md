the restriction of _M_<sup>∗</sup> to the _d_-sets containing _a_<sub>_i_-1</sub>_,...,a_<sub>_i+k_-1</sub>. The matching _M_<sup>∗</sup> also witnesses that \(\tau[i-1,M_{i-1}]=\mathsf{true}\), and this value is correctly computed by induction. Extending _M_<sub>_i_-1</sub> with _M(a_<sub>_i+k_</sub>) does not lead to a blocking _d_-set containing only agents from _a_<sub>_i_-1</sub>_,...,a_<sub>_i+k_</sub>, as _M_<sup>∗</sup> does not contain such a blocking _d_-set. It follows that the algorithm computed \(\tau[i,M]\) to be true, a contradiction.

Getting rid of parameter _d_, we now extend Proposition 4.4 to an FPT-algorithm for the single parameter \(\kappa\). To do so, we show that if \(\kappa\) is much smaller than _d_, then there always exists a stable matching. Note that we prove this by giving an efficient algorithm for _finding_ a stable matching.

**Lemma 4.5.** _If_ \(4\kappa 2^{4\kappa}\le d\)_, then there exists a stable matching._

_Proof._ We apply Lemma 4.2 to the poset \((A,\unknown_\mathsf{ML})\), getting an order _a_<sub>1</sub>_,...,a<sub>n</sub>_ of the agents in _A_.

**Claim.** _There exists a d-set t_<sup>∗</sup> _such that, for any matching containing t_<sup>∗</sup>_, no blocking d-set contains an agent from t_<sup>∗</sup>.

**Proof of Claim:** For each \(i\in[d-2\kappa]\), let \(t_i:=\{a_i\}\cup t\), where _t_ is the first (_d_-1)-set in the preferences of _a<sub>i</sub>_. By Lemma 4.2, it holds that _t<sub>i</sub>_ contains _a<sub>j</sub>_ for each \(j\in[d-2\kappa]\), and all agents of _t<sub>i</sub>_ are from \(A[\le d+2\kappa]\). Thus, there are at most \(\genfrac(){pt}{2}{4\kappa}{2\kappa}\le 2^{4\kappa}-2\) different classes. Since \(d-4\kappa\ge 4\kappa(2^{4\kappa}-1)>4\kappa(2^{4\kappa}-2)\), there exists a _d_-set _t_<sup>∗</sup> with _t_<sup>∗</sup>=_t<sub>i</sub>_ for at least \(4\kappa\) agents _a<sub>i</sub>_.

Consider any matching _M_ containing _t_<sup>∗</sup>, and assume that there is a blocking _d_-set _t_ containing an agent \(a^*\in t^*\). Let _t_\\_t_<sup>∗</sup>={_a_<sub>_i_<sub>1</sub></sub>_,...,a<sub>i<sub>r</sub></sub>_} with \(i_1<i_2<\cdots<i_r\) and _t_<sup>∗</sup>\\_t_={_a_<sub>_j_<sub>1</sub></sub>_,...,a<sub>j<sub>r</sub></sub>_} with _j_<sub>1</sub>_\<j_<sub>2</sub>_\<...j<sub>r</sub>_. Each agent from _t_\\_t_<sup>∗</sup> is contained in \(A[\ge d-2\kappa+1]\) (because \(A[\le d-2\kappa]\subseteq t^*\)), and _t_\\_t_<sup>∗</sup> contains at most \(2\kappa\) agents from \(A[d-2\kappa+1,d+2\kappa]\) (as the other \(2\kappa\) agents of this set are contained in _t_<sup>∗</sup>). Thus, we have that \(i_p\ge d-2\kappa+p\) for all \(p\in[r]\), and \(i_p\ge d+2\kappa+(p-2\kappa)=d+p\) for all \(p>2\kappa\). Every agent _a<sub>i</sub>_ with \(i\in[d-2\kappa]\) such that _t<sub>i</sub>=t_<sup>∗</sup> is matched to its first choice and thus not contained in _t_. Thus, we have \(j_{4\kappa}\le d-2\kappa\) and therefore, for all \(p\in[4\kappa]\), we have that \(j_p\le d-2\kappa-(4\kappa-p)=d-6\kappa+p<d-4\kappa+p\le i_p-2\kappa\). For \(p>4\kappa\) we have that \(j_p\le d+2\kappa\), while \(i_p\ge d+p>j_p+2\kappa\). By Lemma 4.2 it follows that \(a_{j_p}\succ_\mathsf{ML}a_{i_p}\) for all \(p\in[r]\). Thus, _a_<sup>∗</sup> prefers _t_<sup>∗</sup> to _t_, contradicting that _t_ is a blocking _d_-set.

From the claim, the lemma follows easily: We start with an empty matching \(M=\emptyset\) and as long as there are at least _d_ unmatched agents, we successively compute such a _d_-set _t_<sup>∗</sup>, add _t_<sup>∗</sup> to _M_, delete the agents from _t_<sup>∗</sup>, and repeat. The resulting matching is clearly stable, as the agents from the _d_-sets added to _M_ are not part of a blocking _d_-set.

Finally, it directly follows that MDSR-Poset is fixed-parameter tractable even when parameterized solely by \(\kappa\).

**Theorem 4.6.** MDSR-Poset _can be solved in_ \(O(n^2)+(\kappa^52^{16\kappa})^{O(\kappa^52^{16\kappa})}n\) _time, where_ \(\kappa\) _is the maximum number of agents an agent is incomparable to, and n is the total number of agents._

_Proof._ If \(4\kappa 2^{4\kappa}\le d\), then we can safely answer yes by Lemma 4.5. Otherwise we have \(d\le 4\kappa 2^{4\kappa}\) and thus, Proposition 4.4 yields an algorithm running in \(h(\kappa)+O(n^2)\) time with \(h(\kappa)=f(\kappa,4\kappa 2^{4\kappa})\) where \(f(\kappa,d)=(\kappa d^4)^{O(\kappa d^4)}\).

So far, we considered the decision version of MDSR-Poset. However, the algorithms from Proposition 4.4 and Lemma 4.5 also solve (in the case of Proposition 4.4 after the straightforward<tbc>

