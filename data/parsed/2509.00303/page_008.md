<tbc>LLMs are employed as the evaluator. LLM-as-a-Judge approach has been adopted in many different domains [21]. In the context of databases, researchers have used LLM-as-a-Judge to evaluate LLM powered natural language to SQL query translation [26, 77] and to evaluate LLM generated candidate query plans [24, 58]. We explore whether we can also leverage an LLM to determine the best algorithm for a sorting task. We run all candidate algorithms on the sampled data. The resulting list of output rankings, each tagged with a unique candidate identifier, is then compiled and presented. The LLM Judge is subsequently tasked with evaluating this aggregate output and identifying the candidate identifier corresponding to the optimally sorted result for the given input. The list-wise Prompt 5 shows the template used to generate the LLM Judge decision, including the task instruction, the sampled keys, and the execution results of the candidate algorithms. This chain-of-thought [72] prompt is designed in accordance with industry-standard evaluation frameworks such as TruLens [1].

**Prompt Block 5: LLM-as-a-Judge Prompt**

### 5.3.2 Self-Consistency Optimizer.

Our second quality estimator is a heuristic _self-consistency_ optimizer, draws on voting theory [23, 53], and the LLM self-consistency paradigm [67]. The intuition is that while any single sorted run may contain isolated reasoning errors or hallucinations, the consensus of multiple runs is statistically more likely to reflect the true semantic order. We therefore treat the ranking produced by each candidate algorithm as a set of expressed preferences and fuse these "votes" into a consensus ranking that serves as a label-free proxy for the ground truth.

Concretely, we first execute every within-budget candidate on a small data sample. We aggregate their sample rankings into a proxy ground truth using reciprocal rank fusion (RRF) [10], which scores each item by its rank in every run and orders items by the summed score. We note that there are other alternative aggregation mechanism such as the Borda Count [14]. RRF scores each item using the reciprocal of its rank, giving greater weight to agreement at the top of the ranking while reducing the influence of weak candidates that place relevant items far down the list, which linear positional methods such as Borda count may overemphasize. We then measure each candidate’s agreement with this proxy. Finally, we greedily select the highest-agreement candidates whose combined estimated cost fits the budget, execute each on the full input, and fuse their outputs, again via RRF, into the returned ranking; when the budget admits only one candidate, this reduces to selecting the single most consensus- aligned algorithm. By aggregating access paths both to _estimate_ quality and to _produce_ the final ranking, the optimizer is robust to the errors of any individual access path.

## 6 Experiments

We present an evaluation of our proposed LLM-as-Judge and Self-Consistency optimizers (Section 5), building on top of value- based and comparison-based LLM sorting algorithms (Section 3). With systematic evaluation, we demonstrate that our proposed optimizer can achieve near-optimal accuracy through online evaluation.

### 6.1 Experimental Setup

### Evaluation Datasets.

\(\bullet\) 2020 World Population [49]: The query is to order these countries by their population.<tbc>

\(\bullet\) SembenchMovie Q9 [29]: Originally designed to rank items for _Ant-Man and the Wasp_ by positivity, we expanded this task to include 5 distinct queries corresponding to the top 5 most reviewed movies.<tbc>

\(\bullet\) DL20 [12]: Contains 54 search queries associated with the 8.8 million passage corpus.<tbc>

\(\bullet\) NFCorpus [5]: A full-text medical information-retrieval benchmark. Due to the high cost, we use three test queries and each query ranks the full 3.6k document corpus.<tbc>

\(\bullet\) HellaSwag [73]:A commence sentence-completion benchmark. We use the first 100 queries with a corpus of 400 passages, following the same experimental setting as the Google proxy model [9].

**Evaluation Metrics.** We use the kendall’s tau metric to measure the accuracy of the sorted list in the 2020 world population, and use the _nDCG_@10 metric for the remaining datasets. For each query in the remaining datasets, we appended a DESC LIMIT 10 clause. For both metrics, closer to 1.0 indicates better sorting quality.

**Standalone Algorithms.** In this section, we compare our proposed optimizer against a comprehensive set of single-algorithm solutions. For the **value-based** category, we include both external pointwise and standard pointwise algorithms. The pointwise method is implemented as the default in several academic prototypes and utilized by BigQueryfor LLM-based semantic ranking [9, 29, 76]. For instance, we employ the exact pointwise prompt utilized by BigQuery for the SembenchMovie dataset. For the **comparison-based** category, we evaluate standard quick sort [51] and external bubble sort [61], alongside with our proposed semantic ranking methods: quick sort with majority voting and external merge sort. We also note that Lotus [48] utilizes the quick sort method. The fundamental distinction between our proposed optimizer and these baselines is that while single- algorithm solutions apply a static strategy regardless of the input, our optimizer dynamically selects the near-optimal algorithm at runtime.

**Implementation Details.** Our approach does not require fully materializing the input to the LLM Order By operator before optimization. Instead, we adopt a strategy similar to Palimpzest [36]: the system first executes the upstream portion of the query on a small sample of input rows and uses the resulting intermediate tuples to estimate the cost and quality statistics required by our optimizer. Moreover, LLM responses produced during this sampling phase can be stored in a response cache, also implemented in many other systems [35, 36, 48, 76].

For all experiments in this section, we directly accessed LLMs via REST API. The temperature is set to 0 to enable greedy decoding and reasoning effort is set to minimal. The sample size for<tbc>

You are an EXPERT RANKED RESULT RATER. You are given a ranking criteria and a list of CANDIDATE RANKED RESULTS
Your task is to find the best ranked result which sort the input keys based on the ranking criteria.
keys: {keys}
Ranking criteria: {criteria}
CANDIDATE RANKED RESULTS:
{rankings}
You should think step by step about the ranking and return the integer identifier of the best ranking.

