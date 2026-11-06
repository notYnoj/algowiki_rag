<tbc>**G3 - RtP wins when queries contain niche brand references.**

• _"NYC trip, local craft breweries"_ \(\rightarrow\) PtR generates `local\_business\_search` + `recipe\_search` (wrong decomposition, recall 0.0); RtP matches "brewery" directly, retrieving the correct Brewery API (recall 0.5).<tbc>

• _"birthday party, create video for friend"_ \(\rightarrow\) PtR stub `vimeo\_video\_search` matches `searchUsers` instead of `searchVideos` (recall 0.0); RtP retrieves `Vimeo/searchVideos` via raw query (recall 0.25).

## I Scaling Study Details

Sub-registries are constructed by including all Ground-Truth APIs for the subset under study plus proportionally sampled distractor APIs from all 50 ToolBench categories to reach the target size; the G1 and G2 recall curves use their respective Ground-Truth sets, and the divergence column is measured on the G1 sub- registries. Each size is run with 5 random seeds (different distractor samples); the full registry (46,984 APIs) has no randomness and is run once. Because G2’s Ground-Truth set (1,048 APIs) already exceeds the 1k target, the smallest G2 point is gold-only, slightly larger than 1k, and has zero seed variance. PtR reuses the saved stubs from the main experiment (stub generation is independent of registry size), so no additional LLM calls are made; only FAISS retrieval is recomputed per sub-registry.  10 reports the full numerical results.

## J Model Generalization: gpt-oss-120b Replication

We replicate the main experiment using gpt-oss-120b (OpenAI et al., 2025), holding all other components fixed (GTE-base embeddings, same FAISS index, same ToolBench test sets, _k_=5), to test whether the findings from the main text hold for a different model family.  11 reports results.

\begin{tabular}{cccccc}
 & \multicolumn{2}{c}{**G1 Recall**} & \multicolumn{2}{c}{**G2 Recall**} & \\
**Registry size** & **RtP** & **PtR** & **RtP** & **PtR** & **Div%** \\
1,000 & **.646**\(\pm\).001 & .586\(\pm\).004 & .339\(\pm\).000 & **.366**\(\pm\).000 & 88.4\(\pm\)0.0 \\
2,000 & **.603**\(\pm\).004 & .544\(\pm\).009 & .300\(\pm\).006 & **.336**\(\pm\).005 & 89.2\(\pm\)1.2 \\
5,000 & **.536**\(\pm\).008 & .470\(\pm\).012 & .249\(\pm\).003 & **.294**\(\pm\).004 & 92.5\(\pm\)1.1 \\
10,000 & **.484**\(\pm\).002 & .414\(\pm\).008 & .215\(\pm\).005 & **.260**\(\pm\).003 & 94.1\(\pm\)1.2 \\
20,000 & **.430**\(\pm\).002 & .357\(\pm\).003 & .184\(\pm\).003 & **.226**\(\pm\).003 & 95.6\(\pm\)0.8 \\
46,984 & **.375** & .297 & .143 & **.185** & 97.5 \\
\end{tabular}

\begin{tabular}{ccccccc}
 & \multicolumn{2}{c}{**Precision**} & \multicolumn{2}{c}{**Recall**} & \multicolumn{2}{c}{**Pass Rate**} \\
**Subset** & RtP & PtR & RtP & PtR & RtP & PtR \\
G1 & **0.274** & 0.186\(\pm\)0.006<sup>∗∗∗</sup> & **0.372** & 0.259\(\pm\)0.012<sup>∗∗∗</sup> & **0.855**\(\pm\)**0.018** & 0.786\(\pm\)0.024<sup>∗∗</sup> \\
G2 & 0.168 & **0.207**\(\pm\)**0.004**<sup>∗∗∗</sup> & 0.143 & **0.194**\(\pm\)**0.003**<sup>∗∗∗</sup> & 0.826\(\pm\)0.029 & 0.820\(\pm\)0.029<sup>n.s.</sup> \\
G3 & **0.135** & 0.123\(\pm\)0.008<sup>n.s.</sup> & **0.160** & 0.146\(\pm\)0.008<sup>∗</sup> & 0.790\(\pm\)0.008 & **0.805**\(\pm\)**0.013**<sup>n.s.</sup> \\
\end{tabular}

** 10** Scaling study: RtP vs. PtR recall by registry size for the G1 (RtP-advantage) and G2 (PtR-advantage) subsets, with G1 tool-selection divergence (\(\pm\) std across 5 random seeds; full registry has no randomness). **Bold** marks the better architecture per subset: the crossover (RtP _\>_ PtR on G1, PtR _\>_ RtP on G2) holds at every registry size. The full-registry recall gaps are statistically significant on both subsets ( 3). G2’s Ground-Truth set (1,048 APIs) exceeds the 1k target, so the smallest G2 point is gold-only (no distractors, zero variance).

** 11** gpt-oss-120b replication (mean\(\pm\)std, 4 runs). RtP precision and recall are deterministic. **Bold**: better architecture (by mean). Superscripts on PtR values denote significance of the PtR-RtP difference (one-sample _t_- test vs. deterministic RtP for precision/recall; two-sample for pass rate): <sup>∗</sup>_p\<_0.05, <sup>∗∗</sup>_p\<_0.01, <sup>∗∗∗</sup>_p\<_0.001, n.s. = not significant. The G1 (RtP) and G2 (PtR) crossover replicates and is significant on precision and recall; on G3 the differences are small and the recall gap weakly reverses toward RtP, indicating G3 behavior is model-dependent.

