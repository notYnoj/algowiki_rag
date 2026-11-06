<tbc>sort with majority votes are consistently among the strongest standalone algorithms, providing a robust baseline on which the optimization framework builds.

## 6.3 Latency and Estimated Cost

In this subsection, we discuss the latency associated with each algorithm, and estimated costs based on  1 and samples.

**Latency.** Figure 4 shows the average latency per query (_x_-axis in log scale) and the quality (_y_-axis), running GPT-5 mini on DL20. To measure latency, we assume that at most 100 LLM requests are in flight at any time. We note that service providers often impose rate limits; for example, Snowflake caps Llama-3.1 70b at 200 requests per minute, whereas Claude Haiku-4.5 has a higher threshold. Value-based methods are the fastest but also the lowest quality. Comparison-based algorithms trade latency for quality: quick sort (37 seconds) is the fastest because the comparisons against each pivot run concurrently, and external merge sort (59 seconds) reaches 0.687. External bubble sort is a cautionary case. It attains the best standalone quality (0.691) but takes 580s, roughly 10\(\times\) of our proposed external merge sort, because its passes are inherently sequential. The two optimizers occupy complementary regions of the frontier. The LLM-as-judge reaches 0.690 at 250s, since it executes only the single path it selects. The self-consistency optimizer improves monotonically with the budget to the highest quality (0.695) at 470s, higher accuracy and faster than external bubble sort.

**LLM Calls Estimation.** The optimizer estimates each candidate’s full cost by executing it on 20 samples and then extrapolate according to the algorithm’s LLM-call complexity ( 1).  3 reports, for each algorithm and model on DL20, HellaSwag and NFCorpus, the mean absolute percentage error (MAPE) between the number of LLM calls predicted by the complexity formula and the number actually issued by the full run. The call counts of the value-based paths are exact, and those of external bubble sort and external merge sort are within 0.2-7%: their formulas only round the window and chunk counts, so the error shrinks as the input grows (for bubble sort from 4.2% on 100 passages to 0.2% on 3.6k documents). Quicksort is the main exception, with errors of 2-37%. Its number of comparisons depends on the pivot choices; quicksort with majority voting exhibits a similar relative error.

## 6.4 Ablation Studies

**Judge model.** Figure 5 isolates the effect of the judge model. We fix Llama-3.1 70B as the ranking model and vary the LLM- as-judge among Llama-3.1 70B, Claude Haiku-4.5, and Claude Sonnet-4.5, with the self-consistency (RRF) optimizer included as a reference. Across ranking budgets, the three judges perform similarly, and using a stronger judge does not consistently improve path selection. At the largest budget, Haiku-4.5 performs best among the judges (0.689), ahead of the larger and more expensive Sonnet-4.5 (0.671), while the Llama-3.1 70B self-judge peaks earlier (0.695 at the $4 budget). This suggests that judge effectiveness is not monotonic in model capability and can vary substantially across models. The self-consistency optimizer is more robust and achieves the highest overall quality (0.697), albeit at a larger budget because it executes and fuses multiple complete rankings rather than selecting a single access path.

4 provides a complementary view by reporting the fraction of queries for which the selected ranking matches or outperforms the best static access path. For all policies, the fraction generally increases with the available budget. At the largest budget, self-consistency and the Haiku-4.5 judge are the most reliable, matching or outperforming the best static path on 33% of queries, compared with 22%-26% for the other two judge-based policies. Among the judges, the trend is consistent with Figure 5: Haiku- 4.5 performs best (33.3%), ahead of the larger and more expensive Sonnet-4.5 (25.9%) and of the Llama-3.1 70B self-judge (22.2%).

**Sample size.** Figure 6 varies the number of items the optimizer probes to estimate each access path’s quality and cost, holding the base ranker (Haiku-4.5)and budget ($28) fixed, for both the<tbc>

Algorithm
point
quick
ext_bubble_4
Self-Cons
ext_point_4
quick_3
ext_merge_4
Judge
0.68
0.66
0.64
0.62
101
102 average query latency (s)

Llama-3.1 70B judge
Sonnet-4.5 judge
Haiku-4.5 judge
Self-Cons (RRF)
0.695
0.690
0.685
0.680
ndcg@10
0.675
0.670
1
2
3
4
5
6
Price ($)

Self-Cons
Judge
0.800
0.775
0.750
0.725
0.700
ndcg@10
0.675
0.650
0.625
0.600
16
20 optimizer sample size
24
28

**Figure 4: DL20 GPT-5 mini Latency.**

**Figure 5: Judge-model ablation on DL20, using Llama-3.1 70b as the ranker.**

**Figure 6: Optimizer sample-size ablation on DL20 (base ranker Haiku-4.5).**

