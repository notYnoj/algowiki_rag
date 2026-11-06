<tbc>DL19). In relational Order By, any correct sorting algorithm produces the same deterministic output, so the choice of algorithm is purely a matter of efficiency. In a _semantic_ Order By, in contrast, the algorithm directly determines output quality with different LLM access paths. As shown by the DL19 results in Figure 1, sorting accuracy (_nDCG_@10) and monetary cost are tightly coupled: the across-query means follow a log-linear trend, with a high coefficient of determination (_R_<sup>2</sup> between 0.95 and 0.98 across the three models). This trend reflects diminishing returns: accuracy improves rapidly with modest initial spending but plateaus as cost continues to grow. While the 80% confidence intervals show that individual queries vary, the mean trend across the 43 queries remains stable and closely tracks the logarithmic fit. The overarching pattern is clear: higher computational expenditure generally yields higher sorting accuracy.

**A universal best algorithm?** Our results demonstrate that no single sorting algorithm is universally optimal across different domains. For instance, when ranking factual data such as NBA player heights, the pointwise approach excels and, with web search tools, it can reach nearly perfect accuracy. On the other hand, comparison-based approaches excel for reasoning-heavy tasks like DL19 passage relevance. To better understand this variance in reasoning tasks, we further analyzed the 43 individual user queries contained within the DL19 dataset.

Figure 2 demonstrate the accuracy distribution for each algorithm for the llama-3.1 70b model. The star denotes the mean _nDCG_@10 for each algorithm. The x-axis represents the different algorithms and the y-axis is _nDCG_@10. The sorting accuracy can change drastically by using different algorithms. The dashed line tracks the accuracy for the specific query with id 1113437. It was chosen because it demonstrates a case where both quick sort has better ranking quality than quick sort with majority vote and external merge sort has better ranking quality than external bubble sort, despite quick sort and external merge sort having lower mean _nDCG_@10 than quick sort with majority vote and external bubble sort respectively. This example illustrates that within the same passage ranking benchmark, there is still no universally optimal algorithm across all queries.

## 5 Optimizer Design

Designing an efficient optimizer for selecting the physical implementation of the semantic LLM Order By operator poses two challenges: (i) understanding the ranking quality of each candidate access path without any ground-truth labels; and (ii) deciding which access path(s) to execute from a small sample of the input, rather than running every candidate over the entire dataset. We look back at classical database query optimization<tbc>

Algorithm
Algorithm
point
quick
ext_bubble_4
w/ search
point
quick
ext_bubble_4
w/ search
point
quick
ext_bubble_4
w/ search
1.0
1.0
0.9
0.9
0.8
0.8
0.8
0.7
0.7
0.6
0.6
0.6
NBA
0.4
0.3
0.5
0.5
0.2
0.4
0.4
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.0
0.5
1.0
1.5
2.0
0.4
-2
0
2
4
6
10
12
14
Price ($)
Price ($)
Price ($)
Price ($)
(a) llama-3.1 70b
(b) GPT-5 mini
(c) Haiku-4.5
Algorithm
Algorithm
bm25
ext_point_4
quick_3
ext_merge_4
bm25
ext_point_4
quick_3
ext_merge_4
bm25
ext_point_4
quick_3
ext_merge_4
point
quick
ext_bubble_4
log fit (R=0.948)
point
quick
ext_bubble_4
log fit (R=0.956)
point
quick
ext_bubble_4
log fit (R=0.980)
0.9
0.9
0.8
0.8
0.7
0.7
DL19
0.6
0.6
0.5
0.5
0.4
0.4
0
5
10
15
20
0.4
0
5
10
15
20
25
30
35
0.4
0
50
100
150
200
Price ($)
Price ($)
Price ($)
(d) llama-3.1 70b
(e) GPT-5 mini
(f) Haiku-4.5

