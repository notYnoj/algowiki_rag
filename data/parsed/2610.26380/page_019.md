<tbc>**Proof idea.** We outline the two main components of the proof. The first and more technically challenging part is to show that the set of evaluations the algorithm samples infinitely many times spans \(\mathbf{1}^\perp:=\{\mathbf{x}\in\mathbb{R}^I:\mathbf{1}^\top\mathbf{x}=0\}\), the decision-relevant subspace, which we prove by contradiction. For an evaluation (_i,j_), we refer to **_e_**_<sub>i</sub>_-**_e_**_<sub>j</sub>_ as its "direction". Let \(E_\infty\) be the set of directions sampled infinitely often. Our goal is then to prove that \(\mathbf{1}^\perp\subseteq span(E_\infty)\) almost surely. Equivalently, for any fixed set of directions E whose span does not contain \(\mathbf{1}^\perp\), the event \(\Omega_\mathcal{E}:=\{E_\infty=\mathcal{E}\}\) has probability 0. Suppose for contradiction that \(\Omega_\mathcal{E}\) has positive probability. On \(\Omega_\mathcal{E}\), after some finite random time, every subsequently sampled direction is in E. This reduces the proof to showing two results: (i) the marginal scores of directions in E tend to 0, and (ii) at least one direction not in E has a marginal score bounded away from 0. Together these imply that in some round SA chooses a direction not in E, a contradiction. The second component then demonstrates that if \(\mathbf{1}^\perp\subseteq span(E_\infty)\), the posterior variance on \(\mathbf{1}^\perp\) goes to 0, and thus EOC decays to 0 as well.

The significance of this result lies not in the asymptotic guarantee itself, but in what it reveals about the surrogate’s structure. Despite being short-sighted and having no designated randomization or "exploration" phase, the policy explores sufficiently.

**5. The endgame**

Conceptually, the allocation rule in SA is compelling, particularly for early and middle rounds: even if it is not forward-looking in a dynamic sense, it values evaluations that are useful beyond their potential influence on this round’s posterior top-_k_ set. But near the end of the horizon, the value of such exploration is small, and in the last round it is zero. Hence, since the surrogate objective is not horizon-aware, this strength of SA can turn negative in _the endgame_. To "zoom in" on the items that are actual top-_k_ candidates in the endgame is precisely the nature of KG-type policies. We develop the KG policy for our problem in §5.1 and a rule for when to switch to it in §5.2.

**5.1. The sequential KG policy**

Recall from §2.3 that the KG policy chooses an evaluation

\((i_t,j_t)\in argmax_{(i,j)\in\mathcal{I}:r_j\le R_t}\psi_{t,ij}^\text{KG}\text{where}\psi_{t,ij}^\text{KG}:=\frac{V_\text{myopic}((i,j)|p_{t-1})}{r_j}.\)

To compute _V_myopic((_i,j_)|_p_<sub>_t_-1</sub>), whose expression is given in (4), Lemma 3 gives explicit expressions for the probability of each outcome of an evaluation and the resulting posterior means given the outcome.

LEMMA 3. _Starting with prior_ \(N(\mu_{t-1},\Sigma_{t-1})\)_, for evaluation_ \((i,j)\in\mathcal{I}\) _and outcome_ \(x\in\{-1,1\}\),

\(\mathbb{P}(X_{ij}=x|p_{t-1})=\Phi(x\alpha_{t,ij})\text{\textit{and}}\mu_t(x|(i,j))=\mu_{t-1}+\frac{x\beta_J\phi(x\alpha_{t,ij})}{\Phi(x\alpha_{t,ij})\sqrt{1+\beta_j^2\sigma_{t-1,ij}^2}}\Sigma_{t-1}(\mathbf{e}_i-\mathbf{e}_j),\)

_where_ \(\alpha_{t,ij}\) _is defined in Lemma 2._

As discussed in §2.3, when no outcome of any affordable evaluation can change the posterior top-_k_ set, all of the myopic gains \(\psi_{t,ij}^\text{KG}\) are zero. The KG policy then requires a fallback rule to determine which evaluation to conduct. Algorithm 3 gives the resulting KG procedure.

