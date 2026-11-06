<tbc>uncertainty, since those are the items that, if misclassified, will incur a high expected mismatch loss. Hence, this surrogate preserves the key feature of EOC: mistakes are penalized by their magnitude. Second, an evaluation can still be valuable even when its outcome cannot change this round’s posterior top-_k_ membership if it tightens the posterior of items near _q_. This is in part because the evaluation informs where to direct later evaluations. Attempting a sports analogy: we don’t only give credit for scoring goals but also for assists.

However, adaptively combining ratings and pairwise comparisons using this mismatch loss has a less than obvious nuance to it. Which items belong in the top-_k_ depends only on the relative utilities, not on the average utility \(\overline{\theta}\). Thus, information about a change in \(\overline{\theta}\) that shifts all utilities equally is _decision-irrelevant_, and the surrogate should catch this. However, (5) may reward learning such information, since reducing uncertainty about such a common shift reduces the expectations \(\mathbb{E}[(q-\theta_i)^+],\mathbb{E}[(\theta_i-q)^+]\). Ratings can provide information about \(\overline{\theta}\) since they contain information about an item’s absolute quality, while comparisons cannot since they only contain relative information. A surrogate based on this mismatch loss can therefore favor ratings over comparisons because it rewards decision-irrelevant uncertainty reduction.

Initially we addressed this by replacing \(\theta\) with its sum-to-zero counterpart \(\widetilde{\theta}=\theta-\overline{\theta}\mathbf{1}\), where **1** is the all-ones vector, and computing the mismatch loss based on the differences \(\widetilde{\theta}_i-q\) and \(q-\widetilde{\theta}_i\), so that learning \(\overline{\theta}\) does not affect the loss. We will next present a formal and more general treatment of mismatch loss, including its link to EOC. As a motivation for this, notice that \(\widetilde{\theta}_i-q=\theta_i-(q+\overline{\theta})\), so the mismatch loss with the fixed threshold _q_ applied to \(\widetilde{\theta}\) can be thought of as our original mismatch loss with a random \(\theta\)-dependent threshold \(q+\overline{\theta}\). This observation invites the question of what is the "best" such _random_ top-_k_ threshold that allows for tractable analysis.

## 3.2. Mismatch loss: formal derivation

We begin by formally defining mismatch loss and showing how it relates to EOC. For any utility vector \(\theta\) and any threshold function \(a:\mathbb{R}^I\rightarrow\mathbb{R}\), define the mismatch loss

\(\mathcal{M}(\theta;S_k,a):=\sum_{i\in S_k}\left(a(\theta)-\theta_i\right)^++\sum_{i\notin S_k}\left(\theta_i-a(\theta)\right)^+=ka(\theta)-\sum_{i\in S_k}\theta_i+\sum_{i=1}^I\left(\theta_i-a(\theta)\right)^+,\) (6)

where the second equality uses the identity _x_<sup>+</sup>=_x_+(-_x_)<sup>+</sup>. Lemma 1 says that expected mismatch loss is an upper bound on EOC and that for specific threshold functions it equals EOC.

LEMMA 1. _Let_ \(\theta^{(k)},\theta^{(k+1)}\) _denote the kth and_ (_k_+1)_th order statistics of_ \(\theta\) _respectively._

(_i)_ _For any threshold function a,_ \(\text{EOC}(S_k;p_{t-1})\le\mathbb{E}\big[\mathcal{M}(\theta;S_k,a)\big|p_{t-1}\big]\).<tbc>

_(ii)_ _If_ \(a(\theta)\in[\theta^{(k+1)},\theta^{(k)}]\) _almost surely, then_ \(\text{EOC}(S_k;p_{t-1})=\mathbb{E}\big[\mathcal{M}(\theta;S_k,a)\big|p_{t-1}\big]\).

_Proof._ All proofs are provided in the Appendix.

Lemma 1 applies to an arbitrary state _p_<sub>_t_-1</sub> but does not involve future evaluations. Thus, its usefulness is in ensuring that, over the course of the evaluation rounds, if we conduct evaluations that make mismatch<tbc>

