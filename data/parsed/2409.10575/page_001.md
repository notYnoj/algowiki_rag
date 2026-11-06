# A Tie-breaking based Local Search Algorithm for Stable Matching Problems

Junyuan Qiu

Columbia University.

Contributing authors: jq2388@columbia.edu;

**Abstract**

The stable marriage problem with incomplete lists and ties (SMTI) and the hospitals/residents problem with ties (HRT) are important in matching theory with broad practical applications. In this paper, we introduce a tie-breaking based local search (TBLS) algorithm designed to achieve a weakly stable matching of maximum size for both the SMTI and HRT problems. TBLS begins by arbitrarily resolving all ties and iteratively refines the tie-breaking strategy by adjusting the relative order within ties based on preference ranks and the current stable matching. Additionally, we introduce TBLS-E, an equity-focused variant of TBLS, specifically designed for the SMTI problem. This variant maintains the objective of maximizing matching size, while enhancing equity through two simple modifications. In comparison with ten other approximation and local search algorithms, TBLS achieves the highest matching size, while TBLS-E exhibits the lowest sex equality cost. Significantly, TBLS-E preserves a matching size comparable to that of TBLS. Both our algorithms demonstrate faster computational speed than other local search algorithms in solving large-scale instances. Moreover, our scalability analysis shows that both algorithms maintain efficient performance as problem size increases.

**Keywords:** Local search, Tie-breaking, Fair matching, SMTI, HRT, Blocking pairs

### 1 Introduction

In 1962, Gale and Shapley introduced the concept of stable matchings through two problems: the stable marriage (SM) problem and the hospitals/residents (HR) problem, with the latter initially referred to as the "college admissions problem" (Gale and<tbc>

