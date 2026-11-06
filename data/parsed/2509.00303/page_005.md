<tbc>is upper bounded by \(O(\frac{N}{m})\). The Merge phase requires \(O(\frac{N}{m}(1+logK))\). Hence, the total LLM function calls can be approximated as \(O(\frac{N}{m}(2+log\frac{K}{m}))\).

## 4 Initial Evaluation

In this section, we evaluate our proposed algorithms alongside existing baselines on two different datasets. We report results in terms of both effectiveness (ranking quality) and cost (price), highlighting the trade-offs between value-based and comparison- based approaches. The main question we would like to answer in this section: **Is there a single sorting algorithm that always gives the best ranking quality?**

**Datasets.** Two datasets were used:

\(\bullet\) NBA: Contains 200 player names \[46\] ordered by height.<tbc>

\(\bullet\) DL19: TREC-DL19 is a widely used benchmark dataset in information retrieval literature \[11\]. The test sets contains 43 queries and 8.8 million passages.

### 4.1 Implementation and Metrics

In our experiments, all LLM models (Llama3.1-70b, OpenAI GPT- 5 mini and Claude Haiku-4.5) are directly accessed through Snowflake Cortex REST API. For all experiments, we use the structured API and set the temperature to 0, which adopted greedy decoding to obtain the most deterministic outputs \[44\], and set reasoning effort to minimal. The input JSON schema was designed following the best practices of chain-of-thought prompting \[69\], as recommended in the OpenAI structured outputs guide \[45\]. All algorithms were implemented in Python. The pointwise \[31\] (_point_) and external pointwise (_ext\_point_) methods use the rating scale prompt from \[82\]; comparison based algorithms follow the prompt design in \[39, 51\]; and external comparison based algorithms utilize the listwise prompt from \[61\].

Notably, as we later demonstrate, the value-based approaches achieve high accuracy on strictly factual, non-reasoning tasks, such as estimating the heights of NBA players. Such high accuracy is achieved because these queries directly leverage the extensive world knowledge embedded within the models’ pre- training corpora \[41, 43\]. To maximize the factual accuracy in these scenarios, we naturally augmented the value-based approaches with a web search tool, allowing the model to ground its values based on web search information.

In evaluating sorted-ness on the NBA dataset, we adopt the well-established kendall’s tau metric \[25\], with values near 1 indicating strong agreement and values near -1 indicating strong disagreement. In evaluating the sorted-ness on DL19, we adopt the standard _nDCG@10_ metric \[68\]. In addition, we follow the conventions in DL19, in which the LLM Order By is applied<tbc>

<tbc>on the top 100 passages retrieved by BM25 for each query \[52\]. We directly use the pyserini toolkit \[32\] for BM25 retrieval. Normalized discounted cumulative gain (nDCG) yields values from 0.0 to 1.0, where higher values indicate rankings that are closer to the ideal order.

### 4.2 Observations

**NBA Player Height Ranking.** The first row of graphs in Figure 1, where x-axis is monetary budget and y-axis reports Kendall’s tau score comparing predicted orderings with the ground truth for the NBA dataset. Overall, the _value-based_ approach emerges as the top performing algorithm among all three models. The pointwise method consistently achieves high accuracy across all models, whereas the performance of the external pointwise method is slightly lower. Furthermore, when equipped with web search capabilities, the pointwise approach can achieve near- perfect accuracy. Sometimes, web search can return conflicting information, typically due to discrepancies in how players’ heights are recorded (e.g., measured with shoes v.s. without shoes). The success of the value-based method implies that for factual data, LLMs excel at directly inferring statistics they have memorized from their training corpora. In contrast, comparison- based approaches consistently underperform. Having the chain- of-thought reasoning steps in comparison based approaches does not close this gap, suggesting that the direct retrieval of internalized facts is more reliable than multi-step reasoning. Additionally, our proposed quick sort with majority voting (_quick\_3_) always outperforms standard quick sort in accuracy across all three models, albeit at a higher cost. Our proposed semantic external merge sort algorithm achieves performance comparable to semantic external bubble sort, while significantly reducing the overall monetary costs.

**DL19 Passage Ranking.** The second row of graphs in Figure 1 reports the evaluation of different algorithms in DL19. The x-axis is the dollar cost for running each access paths and the y-axis is the mean _nDCG@10_ across 43 queries (higher is better). The error bars denote the 80% confidence interval of the per-query _nDCG@10_, and the dashed logarithmic fit achieves \(R^2\ge 0.95\) across all three models, indicating that quality improves log- linearly with cost with strongly diminishing returns. For passage ranking tasks, comparison-based sorting algorithms excel. Our proposed semantic external merge sort (_ext\_merge\_4_) and quick sort with majority voting (_quick\_3_) consistently achieve the best mean _nDCG@10_. For example, using GPT-5 mini, standard quick sort and external bubble sort achieve average scores of 0.72 and 0.73, respectively. Our proposed quick sort with majority voting and external merge Sort both attain the score of 0.73. These performance gains come with distinct cost trade-offs: the additional voting mechanism increases the cost of quick sort with majority voting by nearly \(2.5\times\) compared to the standard variant. Conversely, external merge sort maintains high accuracy while decreasing costs by \(6\times\) relative to external bubble Sort. The value based approach performs worse for passage ranking. When the task is not centered on deriving factual information, value-based approaches are less effective, as they lack the comparative reasoning needed to capture subtle relevance signals, which has also been observed in prior works \[39, 50\].

**Trade-off between Sorting Accuracy and Computation.** Our initial observations reveal a consistent trade-off between sorting accuracy and computational cost in semantic ranking tasks (e.g.,<tbc>

\begin{tabular}{ccc}
 & \multicolumn{2}{c}{LLM Calls} \\
Algorithm & Full Sort & Limit _K_ \\
Pointwise & _O(N_) & _O(N_) \\
Ext Pointwise & _O(N/m_) & _O(N/m_) \\
Quick Sort (_v_) & _O(vNlogN_) & _O(v(N+KlogK_)) \\
Ext Bubble & _O(N_<sup>2</sup>_/m_<sup>2</sup>) & _O(KN/m_<sup>2</sup>) \\
Ext Merge & \(O(\frac{N}{m}(1+log\frac{N}{m}))\) & \(O(\frac{N}{m}(2+log\frac{K}{m}))\) \\
\end{tabular}

** 1: LLM call complexity by algorithm, where** _N_ **is the number of keys,** _m_ **is batch size,** _v_ **is votes, and top-**_k_ **items.**

