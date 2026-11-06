# A Predictive Framework for Base-_n_ Radix Sort Optimization

**Abstract.** Sorting is a foundational primitive of computer science and optimizations in sorting subroutines can cascade into significant performance gains for high-throughput systems. In this paper, we analyze the inefficiencies of a non-comparison sorting algorithm, namely, _Base-n Radix Sort_ (BNRS), specifically the ‘zero padding’ problem in skewed datasets. We develop an execution model, called, _Stable Partitioning - Least Significant Digit Radix Sort_ (shortly, SP-LSD), an iterative least significant digit based pruning model designed to address this inefficiency. Based on this development, we derive the _Radix Crossover Framework_ (RCF), an analytic three-point decision framework. The framework is established on the precondition of non-negative integers, which enables the derivation of three critical boundaries. First, the _Asymptotic Crossover_ (_k\<n_log<sub>2</sub>_n_) defines when BNRS and SP-LSD can theoretically outperform the comparison sorting algorithms where _k_ is the maximum value and _n_ is the input size. Second, the _Round-feasibility Crossover_ (_k\>n_<sup>2</sup>) defines when overhead cost of implemented model SP-LSD is amortized. Third, we derive _Pruning Crossover_ parameterized by the ratio of random-access sorting cost to sequential partitioning cost. This model demonstrates that SP-LSD yields a net gain on skewed and uniform distributions over standard BNRS. The experimental results are consistent with the crossover boundaries, providing a deterministic roadmap for adaptive algorithm selection.

**Keywords:** non-comparison sorting algorithms; radix sort; algorithm optimization; skewed and uniform log dataset; adaptive sorting; performance modelling.

### 1 Introduction

The typical application of Radix sort uses base 10 but Base-_n_ Radix Sort (shortly, BNRS) [2] uses base-_n_ instead of base 10, where _n_ is the input size. The working nature of BNRS is discussed in detail in the next section and a demonstration is provided in Appendix. BNRS suffers from ‘zero padding problem’ for certain data distributions. More specifically, this is caused due to non-uniform effective bit widths which occurs when the input dataset has varying significant digit<tbc>

Atharv Pandey<sup>1</sup>[0009-0000-6456-0240] and Lakshmanan Kuppusamy<sup>1</sup>[0000-0003-2358-905X]

School of Computer Science and Engineering, VIT University, Vellore - 632 014, India. `klakshma@vit.ac.in`

