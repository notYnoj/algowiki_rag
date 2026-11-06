# Efficiently Representing Algorithms with Chain-of-Thought Transformers

**Abstract**

The increasing popularity of _reasoning_ models--language models that output a series of reasoning or thought tokens before producing an answer--is justified, in part, by theoretical results showing that chain-of-thought (CoT) transformers can simulate Turing machines, and thus perform arbitrary computation. However, the Turing machine, while suitable for complexity-theoretic analysis, is not convenient, intuitive, or efficient for discussing algorithms. Algorithms are typically designed and analyzed at a higher level of abstraction, captured by the _Word RAM_ model with random-access memory and unit-cost operations on O(log_n_)-bit words. As a result, Word RAM algorithms can be substantially more efficient than their Turing machine counterparts, raising the question: _Can CoT transformers efficiently simulate Word RAM algorithms?_ For instance, can they sort _n_ items in O(_n_log_n_) steps or run Dijkstra’s algorithm in O(_E+V_log_V_) steps? We answer affirmatively, up to polylogarithmic overhead. We first establish this for finite-precision transformers with poly-logarithmic width and rightmost unique hard attention, then strengthen the result to two more practical settings with finite width and log-precision: _continuous_ CoT, where reasoning takes the form of vectors rather than tokens, and a _hybrid_ architecture in which transformer layers sit atop a recurrent (linear RNN) layer. In all three cases, we find that CoT _can_ efficiently simulate any Word RAM algorithm with only a poly-logarithmic overhead in _n_. This overhead reduces to log-square when the Word RAM has a “flat” instruction set, and only logarithmic for multiplication-free flat instructions--in stark contrast to known CoT simulations of Turing machines, which require quadratic overhead over Word RAM.

### 1 Introduction

It has been known for a while that chain of thought (CoT) makes transformers _Turing complete_--able to simulate any algorithm in principle (Pérez et al., 2021). This justifies the empirical practice of training reasoning models to solve complex tasks (e.g., Snell et al., 2024; DeepSeek-AI, 2025; OpenAI, 2026). However, the ability to simulate a Turing machine (TM) does not immediately translate to being able to implement interpretable algorithms efficiently: while TMs provide an established framework for analyzing computational complexity, they are not practical for designing real-world algorithms. For instance, sorting _n_ items takes only O(_n_log_n_) steps on a random-access machine (RAM)--an idealized computer whose memory cells can be read and written in unit time at arbitrary addresses, formalized in §2.1--because each comparison and swap touches an arbitrary array entry in a single step. A TM has no such random access: to reach the addressed cell it must move its head there, scanning a tape region of length up to O(_n+t_) per access. Simulating these<tbc>

arXiv:2606.19697v1 [cs.LG] 18 Jun 2026

**Yanhong Li**<br>
Allen Institute for AI<br>
`yanhongl@allenai.org`

**Ashish Sabharwal**<br>
Allen Institute for AI<br>
`ashishs@allenai.org`

**Anej Svete**<br>
ETH Zürich<br>
`asvete@ethz.ch`

**William Merrill**<br>
Allen Institute for AI<br>
`willm@allenai.org`

