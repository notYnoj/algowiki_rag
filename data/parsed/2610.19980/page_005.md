and solver status.

### 3.3 Recursive guillotine hardness

In the guillotine cutting problem, we are given a finite family R of pairwise interior-disjoint axis-parallel rectangles in a bounding box, and we seek a recursive sequence of guillotine cuts that preserves as many rectangles as possible. A guillotine cut of a current box is a horizontal or vertical segment spanning the box; rectangles it crosses are destroyed and rectangles strictly on each side recurse. The recursion continues until every region contains at most one rectangle, and no separate bound on the number of cuts is imposed: since a cut can only destroy the rectangles it crosses, an optimal strategy never uses more than |R|-1 cuts. Let save(R) be the maximum number of rectangles preserved by an optimal recursive strategy. The score is

\(\text{score}_\text{guill}(\mathcal{R})=1-\frac{\text{save}(\mathcal{R})}{|\mathcal{R}|}.\)

Informally, one recursively slices the bounding box with full horizontal or vertical cuts, and a difficult instance is a packing from which every guillotine sequence must destroy a large fraction of the rectangles. Figure 1 (right) shows a small instance and the outcome of an optimal cutting sequence.

Guillotine separability and cutting sequences were studied by Pach and Tardos [28], Abed et al. [1], and Khan and Pittu [22]. The central quantity is the fraction of rectangles a guillotine sequence can separate. For general disjoint rectangles, Pach and Tardos showed that an \(\Omega(1/logn)\) fraction can always be separated and conjectured that a constant fraction always suffices [28]; this remains open. For squares the separable fraction is at least a constant: Abed et al. showed that some constant fraction can always be separated [1], and the best explicit guarantee was improved to 1/40 [22] and then to 9/256≈3.51% [10]. In the other direction, there is an arrangement of squares from which no guillotine sequence can separate more than half. The optimal constant for squares therefore lies between 9/256 and 1/2. Such separability bounds translate directly into dynamic-programming approximations for the corresponding independent-set problems. The exact verifier is a dynamic program over coordinate-induced rectangle-subset states; the certificate stores saved and destroyed counts, the optimal recursive cut tree, first- cut and threshold diagnostics, the DP state count, and solver status.

Each problem is scored by an exact objective computed by a verifier that is independent of the search, so that the exact score, and not a surrogate, is the value reported everywhere. Appendix A gives small, easily ver<tbc>

<tbc>ifiable instances that certify a non-trivial objective for each problem: an integrality gap above 1 for MISR and unit-square stabbing, and a destroyed fraction above 0 for guillotine cutting.

## 4 PatternBoost/Explorer framework

**The PatternBoost/Explorer loop.** PatternBoost [11] was recently proposed as a framework for discovering mathematical constructions with the help of a trained model. It alternates two phases over a growing database of scored constructions. In the _local-search_ phase, existing constructions are perturbed by small targeted moves and improved ones are kept; in the _global- learning_ phase, a transformer trained on the highest- scoring constructions in the database generates new candidates, which are handed back to local search. The transformer supplies globally informed starting points that local search alone would rarely reach, while local search supplies the correction that turns rough generated candidates into valid constructions; the combination outperforms either phase alone [11]. In principle, only the problem-specific scoring function needs to change between problems. However, we discovered in this work that the local search operation and the representation also need to be carefully engineered for each problem. Figure 2 shows the loop; pseudocode is given in Appendix F. It is a population-based search: each generation scores the population with the surrogate, exactly audits the elites at a fixed interval, periodically retrains a fresh model on the archive, and refills the population by mutating elites with the configuration’s local-search operator and adding a few random newcomers.

_The transformer._ A construction is serialized as a canonical JSON string and tokenized character by character, with start and end markers. The model is a decoder-only transformer that predicts the next token autoregressively and is trained by next-token cross-entropy on the elite database, so it learns the<tbc>

ML Model generates instances
Local Search improves instances

Figure 2: The PatternBoost loop: local search and transformer generation alternate over a database of high-scoring constructions. Adapted from [11].

