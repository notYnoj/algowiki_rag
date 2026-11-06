<tbc>solution. Fig.5 shows that VGSM outperformed the baselines and obtained solutions are relatively close to the exact optimal solution. In addition to failing to distribute APs at effective positions to maximize the coverage, the baseline also violated the constraints specified in the prompt (Fig.5, right). This includes assigning APs in the walls despite explicitly told not to, or placing multiple APs at the same position. These invalid APs are removed when evaluating the solution. While the number of violations reduced with thinking, it did not completely go away despite suffering from a significant runtime increase, exposing the lack of soundness in LLMs.

## Retrieval Augmented Generation (RAG)

Given the success of VGSM in tasks with a known explicitly-defined submodular evaluation function, we next evaluate VGSM on an evaluation function _implicitly, informally_ defined by the queries. One such task is RAG, a mainstream approach for reducing LLM hallucinations by retrieving documents relevant to the query from a database and appending them to the prompt so that LLMs can draw correct answers from the documents.

While existing work tends to simply rank the documents via vector embedding similarity search, this approach fails when the task requires combining information in multiple documents to draw conclusions, because all the top-ranked documents may be similar to each other and lack crucial information. To address this limitation, existing work formulated _multi-hop Q&A tasks_ \[Yang et al., 2018\] and observed that there are several types in each ground-truth retrieval (e.g., bridging, comparison, etc), differing in how they chain multiple information together. Existing work proposed various heuristic methods that additionally require fine-tuning \[Park et al., 2025\], based on the observations.

On the other hand, traditional approaches to multi-hop reasoning utilize submodularity. For example, _Maximum Marginal Relevance (MMR)_ rule \[Carbonell and Goldstein, 1998\] takes an explicitly defined evaluation function _f_ and makes it submodular. However, in a LLM-based retriever, _f_ is only implicitly defined by the prompt, making it difficult to apply this insight.

Greedy submodular maximization guarantees 1-1_/e_ optimality under a monotone submodular function _f_. In contrast, due to the lack of explicit _f_, VGSM can only make a much weaker statement, such as _if f is indeed submodular, then_ it can guarantee 1-1_/e_ optimality. One may wonder if such a weak statement is meaningful, but this question is _logically inverted_. The submodular assumption is a model simplification of the real-world task anyway. Given a model (implicit or explicit), _it is in fact in the realm of empirical study to verify its correctness_, as was done for the log-distance model with the actual physics experiments. Since VGSM would work if the implicit _f_ was monotone submodular and not if otherwise, we could verify the monotone submodularity of _f_ by evaluating VGSM.

We evaluated two RAG datasets: HotpotQA \[Yang et al., 2018\] (fullwiki, hard) and CUAD \[Hendrycks et al., 2021\]. Each dataset contains a set of 4-tuples (_Q,A,S_<sup>∗</sup>_,D_) where _D_ is a set of documents, _Q_ is the question, _A_ is the ground-truth answer, and _S_<sup>∗</sup> is the ground-truth retrieval. We assume a generative model \(p(A|D,Q)=\sum_Sp_\phi(A|S,Q)p_\psi(S|Q,D)\), where _S_ is the documents selected by the retrieval model \(\psi\), and \(p_\phi(A|S,Q)\) represents the likelihood of the answer by an answering model \(\phi\). Given \(\psi\) and \(\phi\), we retrieve _k_=3,6,12 documents with \(\psi\) and evaluate the performance<tbc>

Access Point Optimization
10
ragbench_hotpotqa, k=6
base
vsgm
better emb.
0.5
base, think
vsgm, think
e+Kwick, k2:12
e+VGSM, k2:12
0.4
1.7
0
e+Kwick, k2:24
e+VGSM, think, k2:12
0.3
1.7
e+Kwick, think, k2:12
e+VGSM, think, k2:24
gap_opt
1.7
logp
0.2
1.7
4
4
32
32
4
4
32
32
4
32
32
0.1
4
32
32
1.7
4
32
32
32
0.0
better
-20
4
102
102
102
102
104
Access Point Optimization
ragbench_cuad, k=6
1.7
better
32
32
32
32
1.0
4
4
32
4
32
32
4
32
32
0.5
1.7
4
32
32
32
32
0.0
logp
4
4
4
32
32
32
4
32
4
32
0.0
101
102
103
102
103
104

Figure 5: The speed-accuracy Pareto front of submodular maximization tasks. In all subplots, log_x_- axis is the runtime per query. _y_-axes are: (Top left) Optimality gap of WiFi tasks. (Bottom left) The number of AP location violations in WiFi tasks. (Right) LOGP of RAG tasks (hotpotQA, CUAD) retrieving _k_=6 documents. _k_=3,12 and Jaccard distance results are available in the appendix.

