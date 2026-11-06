<tbc>Thus, in this paper, we aim to address the following question: **Given a semantic LLM ORDER BY task and a fixed monetary budget, how can we maximize sorting accuracy while remaining within the budget?** Before answering this question, we first explore whether there exists a universal optimal approach that achieves the best quality for all given tasks and datasets. To this end, we implemented existing approaches, proposed new LLM-based sorting algorithms, and conducted a systematic evaluation of different approaches within a unified experimental framework across different tasks. We observe that no algorithm outperforms the others across all tasks. In some cases, pointwise method (often criticized for its limited accuracy [51]) can, in fact, achieve strong accuracy in certain scenarios, while pairwise and listwise approaches excel in others. This highlights the importance of tailoring the ranking strategy to the task setting rather than relying on a one-size-fits-all solution. This highlights the importance of tailoring the ranking strategy to the task setting rather than relying on a static LLM Access Path <sup>1</sup>. It also suggests that the LLM Access Path, i.e., the strategy for invoking an LLM to implement a semantic operator, should be carefully selected based on the query characteristics, underlying model, and data. Although this paper does not aim to optimize the selection of the access paths for all operators, we present an optimizer that determines a highly accurate sorting approach for the LLM ORDER BY operator.

After thoroughly examining the efficiency-effectiveness tradeoffs in the initial evaluations, we conjecture a scaling relationship between compute cost and quality in semantic sorting, where increased computation consistently correlates with higher quality results. Building upon this insight, we propose two distinct optimizer configurations for the LLM ORDER BY operator: (i) an LLM-as-Judge optimizer that evaluates candidate quality, and (ii) a self-consistency optimizer that leverages aggregation to derive a robust consensus. The LLM-as-Judge approach leverages direct reasoning and reflection to maximize accuracy. The self-consistency optimization functions as a highly robust ensemble strategy, employing consensus aggregation to filter out anomalies and to ensure superior stability on complex ranking tasks.

To conclude, our contributions can be summarized as follows:

\(\bullet\) We propose several improvements to existing semantic sorting algorithms as well as a new semantic sorting algorithm which is an adaptation of the classical two-way merge sort algorithm [56].<tbc>

\(\bullet\) Based on empirical data, we conjecture that LLM-based sorting obeys the scaling behavior, which relates computational expenditure to output quality, forming a foundation for an intelligent optimizer.<tbc>

\(\bullet\) We design and implement an optimizer that leverages heuristics, LLM judgment, and consensus voting to achieve high ranking quality within budget constraints.<tbc>

\(\bullet\) Across five benchmarks and three LLMs, our optimizer consistently competitive with and often exceeds the best static algorithm, whose identify changes across datasets and models.

This paper is structured as follows: Section 2 provides background information on semantic sorting and establishes the notation. Section 3 reviews existing algorithms and introduces our proposed extensions, including the new semantic merge sort algorithm. Section 4 details our evaluation on two benchmarks,<tbc>

<tbc>demonstrating that no single algorithm is universally optimal and quantifying the relationship between the computational budget and accuracy. Section 5 introduces an optimizer that incorporates heuristic rules, LLM guidance, and consensus aggregation. Section 6 presents extensive experiments validating the effectiveness of our proposed optimizers. Finally, Section 7 concludes with a discussion of our findings.

## 2 Preliminaries

The **LLM ORDER BY** semantic operator takes as input a list of data points along with a ranking criterion and produces an ordered list. These data points may represent diverse items, such as documents or reviews, while the ranking criterion specifies the basis for ordering, such as relevance to a user question. Unlike traditional database settings, where the ordering attribute is explicitly stored in the table, LLM-based ordering relies on semantic judgments or inferred attributes.

Previous LLM sorting algorithms are typically designed for passage or document ranking and are commonly categorized as pointwise, pairwise, or listwise. In this paper, we adopt a slightly different terminology. We refer to pointwise methods as **value- based**, pairwise methods as **comparison-based**, and further divide listwise methods into two variants: **external value-based** and **external comparison-based**. The intuition is that listwise methods can be viewed as batching multiple data points: either batching the derivation of values for multiple data points (external value-based) or batching the determination of the correct permutation (external comparison-based) for multiple data points. Value-based ordering methods are commonly implemented in current LLM-powered analytic systems [29, 65, 76], typically excelling on benchmarks that test factual accuracy (e.g., ranking based on masked attributes of sports players’ height or celebrity’ birthday). On the other hand, systems like Lotus [48] employ comparison-based ordering for semantic ordering, achieving top- tier accuracy on sentence understanding tasks.

In our work, we focus on the semantic LLM ORDER BY operator and the method of implementing the operator through standard generation APIs, i.e., treating the large language model as a semantic black box. In modern data infrastructures, models, whether proprietary or managed open-source, are predominantly exposed via high-level inference interfaces to abstract away the complexities of multi-tenant serving, hardware optimization, and security. Furthermore, emerging LLM-based analytical systems [36, 58, 63] increasingly rely on these standardized endpoints to ensure broad compatibility among different providers (e.g., OpenAI API [45], Snowflake Cortex API [59], LiteLLM [4]). Also, the monetary cost of using these models can be calculated directly from the input and output tokens.

## 3 LLM Sorting

In this section, we review existing semantic sorting algorithms (e.g., standard pointwise [42], quicksort [48], and external bubble sort [61]) and present our proposed optimizations: quick sort with majority voting, and semantic external merge sort.

### 3.1 Value-Based Ordering

In value-based ordering, the LLM assigns a value to each key, and the final ranking is obtained by sorting the keys according to these values. This approach is often the default implementation in many LLM-powered data systems [2, 18, 29, 76]. The value- based method requires _O(N_) LLM function calls where _N_ is the<tbc>

<sup>1</sup>Inspired by access paths in relational database systems [56]

