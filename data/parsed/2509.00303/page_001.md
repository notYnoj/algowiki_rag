# Access Paths for Efficient Ordering with Large Language Models

### Abstract

In this work, we present the LLM ORDER BY semantic operator as a logical abstraction and conduct a systematic study of its physical implementations. First, we propose several improvements to existing semantic sorting algorithms and introduce a semantic-aware external merge sort algorithm. Our extensive evaluation reveals that no single implementation offers universal optimality on all datasets. From our evaluations, we observe a general scaling relationship between sorting cost and the ordering quality for LLM ranking algorithms. Building on these insights, we design a budget-aware optimizer that utilizes heuristic rules, LLM-as-Judge evaluation, and consensus aggregation to dynamically select the near-optimal access path for LLM ORDER BY. In our extensive evaluations, our optimizer consistently achieves ranking accuracy on par with or superior to the best static methods across benchmarks. We believe that this work provides foundational insights into the principled optimization of semantic operators essential for building robust, large-scale LLM-powered analytic systems.

### Keywords

Semantic Ranking, LLM Order By, AISQL, Hybrid Queries

### 1 Introduction

Recent advances in large language models (LLMs) have facilitated complex data processing, such as automatically translating natural language questions into SQL queries [15, 16, 19, 30, 78], powering autonomous problem-solving agents [22, 36, 47, 58, 60, 77, 79, 83], and introducing new declarative query languages with AI operators [18, 34, 55, 74, 76]. Building LLM declarative interfaces through semantic operators have also attracted significant attention from industry, with systems such as BigQuery ML [20], Snowflake AI SQL [34, 59], and Amazon Redshift’s user-defined functions [3].

In this work, we focus on the implementation of one specific LLM/AI semantic operator: LLM ORDER BY, commonly used for sorting or ranking. Sorting is a fundamental operation in data processing and underpins a wide range of analytical and decision-making tasks. LLM ORDER BY enables ranking items based on semantic signals, user preferences, or task-specific criteria that are difficult to capture with traditional methods. For example, in information retrieval, it is common to use LLMs to re-rank retrieved documents or passages based on the user’s question or preferences [81]. In the context of relational data processing, LLMs can be leveraged to rank selected rows based

on attributes that are not explicitly stored in the relational table, such as inferred sentiment or other factual information [76, 80]. Let’s consider the following two concrete examples:

Example 1.1. _A user provides a query and, after an initial index filter (e.g., BM25 [52]) on a large documents corpus, the user invokes the_ LLM ORDER _BY operator to re-rank the retrieved subset based on the criteria (e.g., document relevance to bmt medical). This approach allows the LLM to generate high quality ordered results based on a nuanced semantic understanding of the user’s query and preferences._

Example 1.2. _A company wants to rank customer feedback based on specific criteria, such as product dissatisfaction or satisfaction level, and to improve its product based on the feedback. Because "dissatisfaction" or "satisfaction" is a subjective attribute, the data analyst can invoke the_ LLM ORDER _BY operator to rank the customer feedback based on this specific criteria, requiring the LLM to highlight the subtle and nuanced levels of customer sentiment. This capability enables the company to directly address the most critical product pain points or capitalize on successful features._

Given the importance of data ordering and ranking, researchers have explored a wide range of approaches in conjunction with LLMs. Prior works mainly study three classes of methods to implement sorting on top of LLMs: (i) pointwise sorting derives the value independently for each given key (e.g., passage relevance score, review sentiment score) [13, 54, 65, 76], (ii) pairwise sorting compares two keys and then determines the relative order between them [38, 51, 57], and (iii) listwise sorting considers an entire set of keys simultaneously to produce a ranked order [39, 61]. There is no clear consensus on which approach is better. For example, Lotus [48], a recent LLM-powered data processing system, implements LLM-based ordering using a pairwise approach with quicksort. BigQuery ML implements LLM-based ordering using a pointwise method [29]. Furthermore, on some benchmarks, researchers find listwise sorting often provide high accuracy [39, 50], and on other benchmarks, researchers find that pairwise sorting provide higher accuracy [51].

Fuheng Zhao<sup>1</sup>, Jiayue Chen<sup>2</sup>, Yiming Pan<sup>3</sup>, Tahseen Rabbani<sup>2</sup>

Shaib<sup>4</sup>, Divyakant Agrawal<sup>4</sup>, Amr El Abbadi<sup>4</sup>

Paritosh Aggarwal<sup>5</sup>, Anupam Datta<sup>5</sup>, Dimitris Tsirogiannis<sup>5</sup>

