## 5.3. Entity-Claim Promotion for Generation

On the generation side, a topic-level attack must induce diverse unseen topic queries toward the same attacker- specified outcome. We therefore adopt entity-claim promotion as a shared generation objective across all poisoned documents, making them consistently support a target claim _ct_ associated with the target entity _et_. Evidence anchoring increases the likelihood that the model adopts _ct_ as a supported conclusion, while entity-claim coupling binds _et_ to _ct_, translating claim adoption into target-entity promotion.

**5.3.1. Evidence Anchoring.** Directly inserting _ct_ into a poisoned document may leave it as an isolated assertion the LLM can ignore. Evidence anchoring embeds _ct_ within a structured argument. For a document _x_, we compose domain background, mechanism, applicable conditions, outcome evidence, and the target claim, written as \(x=\mathrm{Compose}\big(b_x,m_x,a_x,r_x,ct\big)\), where _b<sub>x</sub>_, _m<sub>x</sub>_, _a<sub>x</sub>_, and _r<sub>x</sub>_ denote the supporting components. For Hubs, these components emphasize topic-level concepts, mechanisms, and decision criteria shared across query regions, providing a rationale for _ct_. For Satellites, they reflect local intents and decision conditions in _Qk.j_, adapting the argument to each query region while preserving _ct_. In this way, evidence anchoring makes _ct_ more likely to be adopted as a supported conclusion rather than ignored as an isolated assertion.

**5.3.2. Entity-Claim Coupling.** Evidence anchoring increases the likelihood that the model adopts the target claim _ct_. Building on this, entity-claim coupling further translates claim adoption into target-entity promotion by making _et_ an indispensable component of both _ct_ and its supporting argument. Specifically, we explicitly attribute the mechanism and outcome supporting _ct_ to _et_, such that removing _et_ makes the target claim incomplete and disrupts the mechanism-outcome-claim reasoning chain. We express this dependency as \(m_x(et)\rightarrow r_x(et)\rightarrow ct(et)\). By maintaining this dependency throughout the supporting argument, entity-claim coupling increases the likelihood that the model retains and promotes _et_ when adopting _ct_.

A generation-effective candidate should fully express _ct_, provide coherent evidence supporting it, and maintain a strong dependency between _et_ and the supporting argument. We jointly capture these properties as

Here, _S_claim measures the completeness of the target claim; _S_evid measures the completeness and consistency of the background, mechanism, conditions, and outcome evidence supporting _ct_; and _S_link measures the degree to which _et_ is explicitly tied to the mechanism, outcome, and target claim. The \(\lambda\) terms control the relative contributions of the three scores. This reward favors candidates that present a complete and well-supported claim while maintaining a strong dependency between _et_ and _ct_ throughout the supporting argument.

Beyond improving individual-document generation effectiveness, the shared entity-claim design provides cross- document benefits for retrieval and generation. (1) _Retrieval-side semantic basis_. Although Satellites target different local query regions, they share the same target entity _et_ and target claim _ct_. This shared semantics gives Satellites a natural similarity basis, making them more likely to occupy nearby HNSW neighborhoods and form structural associations while preserving local query alignment. (2) _Generation-side evidence consistency_. Although poisoned documents adapt their arguments to different query regions, they consistently target the same _et_ and _ct_. When cascading retrieval brings multiple poisoned documents into context, they provide consistent and mutually reinforcing evidence for _ct_, increasing the likelihood that the model adopts _ct_ and promotes _et_.

## 5.4. Two-Level Candidate Optimization

Poisoned documents must provide both retrieval and generation utility, while selecting Satellites solely by individual scores may introduce semantic redundancy and leave long-tail query regions undercovered. We therefore adopt a two-level optimization strategy. At the document level, _multi-candidate joint scoring_ jointly considers retrieval and generation utility to evaluate and filter both Hub and Satellite candidates, ensuring the quality of individual poisoned documents. After the Hub is selected, set-level _greedy complementary selection_ operates only on Satellite candidates and constructs the final set based on their marginal query- coverage gain and association with the selected Hub, thereby improving overall coverage complementarity under a fixed poisoning budget.

**5.4.1. Multi-Candidate Joint Scoring.** Because LLM generation is stochastic, a single generated candidate may exhibit insufficient retrieval utility or weak generation influence. We therefore generate multiple candidates for each Hub or Satellite role and jointly evaluate their retrieval and generation utility. For a candidate Hub _h_ and Satellite _p_, we define the joint scores as

The \(\alpha\) and \(\eta\) weights balance retrieval and generation utility. Candidates for each target position are ranked by their joint scores. The top-ranked Hub candidates are retained to form _H_, while the top-ranked Satellite candidates form the filtered pool \(\mathcal{P}_\mathrm{cand}\) for subsequent set-level complementary selection.

**5.4.2. Greedy Complementary Selection.** Document-level joint scoring evaluates Satellite candidates independently and thus cannot account for coverage redundancy across candidates. Score-only selection may therefore overcon- concentrate on the same semantic regions and leave long- tail queries undercovered. We address this with set-level<tbc>

\begin{tabular}{cc}
Rgen(x) & = λclaimSclaim(x,ct) + λevidSevid(x,ct) \\
 & + λlinkSlink(x,et,ct).
\end{tabular}

\begin{tabular}{cc}
\(R_\mathrm{hub}^\mathrm{joint}(h)=\alpha_hR_\mathrm{hub}^\mathrm{ret}(h)+\eta_hR_\mathrm{gen}(h),\) & \\
\(R_\mathrm{sat}^\mathrm{joint}(p;k,j)=\alpha_sR_\mathrm{sat}^\mathrm{ret}(p;k,j)+\eta_sR_\mathrm{gen}(p).\) & \\
\end{tabular}

