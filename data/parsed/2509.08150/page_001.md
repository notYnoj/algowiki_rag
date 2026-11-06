# Verbalized Algorithms: Classical Algorithms are All You Need (Mostly)

**Abstract**

Reasoning is a fundamentally algorithmic task. Yet current work on LLM-based reasoning relies on free-form generation whose theoretical guarantees (soundness, completeness, complexity, optimality) remain poorly understood. We argue that we should not treat them as general-purpose reasoners, and as an alternative, we propose a paradigm we call _verbalized algorithms_ (VAs), which combines LLMs and various algorithms with established guarantees. Instead of betting on LLM’s ability to solve a reasoning task, VAs limit their scope by decomposing the task down to simple elementary operations on strings that they can answer reliably. For example, sorting a list of natural language strings could be done by using an LLM as a binary comparison oracle in a parallel or approximate sorting algorithm. We push the accuracy-runtime Pareto front with _verbalized maximum_, _sorting_, _clustering_, and _submodular maximization_, for numerical reasoning, topic clustering, Wi-Fi access point optimization, and multi-hop Q&A RAG task. These results suggest improving LLM-based reasoning through standard algorithmic analysis is a feasible and better grounded research direction.

### 1 Introduction

Imagine receiving thousands of customer complaints and having to quickly sort them by how urgently they need support. Feeding such a large set of input strings blindly into a transformer-based large language model (LLM) is ineffective and impractical due to various limitations. Examples of such limitations include limited context lengths from hardware limitation (GPU memory limit from _O(n_<sup>2</sup>) attentions), sequential runtime for processing a long input, deteriorating accuracy from the longer context, and its limited ability to perform the sorting task itself. LLMs provide no guarantees on the correctness of their outputs for computational reasoning tasks, including but not limited to sorting, beyond anecdotal, empirical observations that they _sometimes_ do. Despite recent improvements in Chain-of-Thoughts [Wei et al., 2022] and think tags [Guo et al., 2025], their behavior is fundamentally an approximation of formal reasoning, and thus contains hallucinations.

We argue that most reasoning tasks are informal representations of formal tasks for which **an efficient and well-analyzed classical algorithm already exists in the literature**, thus training a model hoping that it may learn to solve it by itself is often a reinvention of the wheel. For example, for sequential comparison sort, _O(n_log_n_) algorithms are asymptotically optimal, thus no algorithm can improve over it anyways **-- then why don’t we just use them?**

**Supriya Lall**<br>
MIT CSAIL<br>
MIT-IBM Watson AI Lab<br>
supriya@mit.edu

**Christian Farrell**<br>
Marist University<br>
IBM Infrastructure<br>
`christian.farrell@ibm.com`

**Hari Pathanjaly**<br>
UC Irvine<br>
IBM Infrastructure<br>
`hari.pathanjaly@ibm.com`

**Marko Pavic**<br>
Marist University<br>
IBM Infrastructure<br>
`marko.pavic@ibm.com`

**Sarvesh Chezhian**<br>
IBM Infrastructure<br>
`schez@ibm.com`

**Masataro Asai**<br>
MIT-IBM Watson AI Lab<br>
IBM Research Cambridge, USA<br>
`masataro.asai@ibm.com`

