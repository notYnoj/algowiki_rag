# How to Sort in a Refrigerator: Simple Entropy-Sensitive Strictly In-Place Sorting Algorithms

**Abstract.** While modern general-purpose computing systems have ample amounts of memory, it is still the case that embedded computer systems, such as in a refrigerator, are memory limited; hence, such embedded systems motivate the need for strictly in-place algorithms, which use only _O_(1) additional memory besides that used for the input. In this paper, we provide the first comparison-based sorting algorithms that are strictly in-place and have a running time that is optimal in terms of the run-based entropy, H(_A_), of an input array, _A_, of size _n_. In particular, we describe two remarkably simple paradigms for implementing stack-based natural mergesort algorithms to be strictly in-place in _O(n_(1+H(_A_))) time.

## 1 Introduction

Embedded computer systems are designed for a specific function within a larger device, and they comprise a processor and a limited amount of memory. They are found in diverse applications such as household appliances, vehicles, and medical equipment. Unlike with general-purpose computers, it is often difficult to extend the limited memory in an embedded systems; hence, embedded systems are a natural application domain for strictly in-place algorithms, which use only _O_(1) additional memory besides that used for the input. Further, embedded systems that utilize non-volatile main memory (NVMM) [27] have additional need of strictly in-place algorithms, because these memories degrade if they are overwritten many times, such as if they had to maintain a data structure such as a stack. Still, we would like to be able to implement fast algorithms in embedded systems, since they often have real-time performance requirements.

For example, in **_beyond worst-case analysis of algorithms_** [22, 23], we are interested in algorithms whose running time can beat worst-case bounds depending on parameters or metrics defined for problem instances that capture typical properties for expected inputs. For example, suppose we are given an array, _A_=[_x_<sub>1</sub>_,x_<sub>2</sub>_,...,x<sub>n</sub>_], of elements that come from a total order. If we let \(\mathcal{R}=\{R_1,R_2,\dots,R_{\rho(A)}\}\) be a partition of _A_ into a set of maximal increasing or decreasing **_runs_** (i.e., subsequences of consecutive elements), and we let _r<sub>i</sub>_

Ofek Gila<sup>[0009-0005-5931-771X]</sup>, Michael T. Goodrich<sup>[0000-0002-8943-191X]</sup>, and Vinesh Sridhar<sup>[0009-0009-3549-9589]</sup>

University of California, Irvine, USA {`ogila,goodrich,vineshsl`}@uci.edu

