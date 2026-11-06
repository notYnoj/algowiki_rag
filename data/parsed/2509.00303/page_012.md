<tbc>Self-Consistency and LLM-as-a-Judge selection policies. Increasing the sample size from 16 to 28 does not produce a statistically distinguishable change in final NDCG@10: the 80% confidence intervals overlap substantially for both the self-consistency and judge policies. In contrast, the probing costs grow roughly linearly. Since ranking quality does not measurably improve with larger samples, a small sample of 20 suffices and is our default.

**Inquiry Prompt.** We evaluate how reliably the inquiry prompt separates factual world knowledge (_parametric_) from context- dependent (_non-parametric_) knowledge. To do so, we construct a balanced benchmark of 274 questions with ground-truth labels: 137 factal world knowledge questions drawn from Natural Questions \[28\]. This dataset only contains factual world knowledge questions (e.g., _who wrote the novel Pride and Prejudice"_). Hence, we include another 137 _non-parametric_ questions drawn from SituatedQA \[75\], which contain questions that require context information (e.g., _when did we last win a national championship?_). As shown in  5, the direct inquiry prompt distinguishes the two knowledge types with 88.7%-90.1% accuracy across three model families. These results suggest that the inquiry prompt provides a robust and model-agnostic mechanism. We also find that the direct inquiry prompt works perfectly on the NBA and world population test datasets.

## 7 Discussion and Future Work

In this work, we introduced the LLM ORDER BY semantic operator and systematically studied its physical implementations. In<tbc>

<tbc>addition to adapting existing semantic sorting methods, we developed two new access paths: external merge sort and quicksort with majority voting, which further expand the accuracy-cost design space. External merge sort achieves strong ranking quality at relatively low cost, while quicksort with majority voting can match or exceed its quality only with a substantially larger computational budget. Moreover, our evaluation reveals a consistent pattern: no single access path dominates across all queries and datasets. The best implementation depends on both the task and the underlying data, motivating adaptive access-path selection rather than a fixed execution strategy. We find that sorting quality improves rapidly as the ranking budget increases from low to moderate levels, but the gains diminish and plateau at higher budgets. Building on this observation, we developed an optimizer that selects among access paths under a user-specified ranking budget without requiring ground-truth labels. By probing only a small sample of the input, the optimizer can identify high-quality execution strategies.

Through extensive experiments, we find that our proposed LLM Order By optimizer can select effective access paths without ground-truth labels, recovering near-optimal points on the cost- quality frontier and matching or exceeding the best standalone access path in most settings. Its two policies offer complementary trade-offs along this frontier. The self-consistency policy combines multiple access paths to achieve the highest quality, while the LLM-as-judge policy selects a single path and achieves competitive quality at substantially lower cost. Overall, these results demonstrate that adaptive, budget-aware access-path selection is a practical execution strategy for the LLM ORDER BY operator.

In future work, we plan to extend the optimizer to explicitly account for ranking latency. While industrial systems often use embedding-based retrieval to first narrow the candidate set to hundreds of relevant documents \[37, 39, 61\], exhaustively ranking millions of documents with LLMs remains prohibitively expensive and slow. A promising direction is to incorporate ideas from Google’s proxy-model-based semantic ranking approach \[9\], which trains a lightweight ranking model online to approximate LLM-based ranking. The lightweight ranking model is orders of magnitude cheaper and faster, at the cost of reduced ranking accuracy relative to the LLM. Our optimizer could then jointly reason about LLM and proxy-model execution, trading off ranking quality, monetary cost, and latency. Furthermore, we plan to expand the capability of our optimizer to support other operators, such as semantic JOIN \[62, 63\], Extract \[33, 64\], and Filter \[59\].

## References

\begin{tabular}{cccccccccc}
 & \multicolumn{3}{c}{**DL20**} & \multicolumn{3}{c}{**HellaSwag**} & \multicolumn{3}{c}{**NFCorpus**} \\
**Alg** & Llama-3.170b & GPT-5mini & Haiku-4.5 & Llama-3.170b & GPT-5mini & Haiku-4.5 & Llama-3.170b & GPT-5mini & Haiku-4.5 \\
ext\_point\_4 & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% \\
point & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% & 0.0% \\
ext\_merge\_4 & 7.0% & 6.4% & 6.3% & 3.9% & 4.0% & 3.4% & 3.1% & 3.6% & 3.8% & \\
ext\_bubble\_4 & 4.2% & 4.2% & 4.2% & 1.0% & 1.0% & 1.0% & 0.2% & 0.2% & 0.2% & 0.2% \\
quick & 32.0% & 33.0% & 31.2% & 23.4% & 29.8% & 32.4% & 1.7% & 18.7% & 25.1% \\
quick\_3 & 35.0% & 37.1% & 36.6% & 27.6% & 34.2% & 29.9% & 17.2% & 18.5% & 20.9% \\
\end{tabular}

\begin{tabular}{ccccc}
Ranking budget & Llama & Haiku & Sonnet & RRF \\
$1 & 16.7% & 18.5% & 18.5% & 14.8% \\
$2 & 16.7% & 20.4% & 22.2% & 24.1% \\
$4 & 22.2% & 25.9% & 24.1% & 31.5% \\
$6 & 22.2% & 33.3% & 25.9% & 33.3% \\
\end{tabular}

\begin{tabular}{cc}
Model & Accuracy \\
Llama-3.1-70B & 88.7% \\
GPT-5-mini & 90.1% \\
Haiku-4.5 & 88.7% \\
\end{tabular}

** 3: Mean absolute % deviation of the estimated number of LLM calls from the number actually issued by the full run.**

** 4: Percentage of DL20 queries for which the selected ranking strategy matches or outperforms the best static access path, using Llama-3.1 70b as the ranker.**

** 5: Accuracy of the inquiry prompt at distinguishing world knowledge from context-dependent questions**

