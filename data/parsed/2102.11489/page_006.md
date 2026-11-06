\(\epsilon\)-near-sorter to each partition in parallel where \(\epsilon\in(0,1)\) is a sufficiently small constant<sup>3</sup>. Our key observation is the following:

**Observation.** If we execute the AKS algorithm not for the full log_n_ cycles, but only for 6_k_ cycles, it gives a (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly segmenter.

The proof of the above statement is rather technical since it requires us to _use the properties of AKS in a non-blackbox manner_. We defer the proof to the formal technical sections.

**Applying a nearly ordered segmenter to an array with few distinct keys produces an almost sorted array.** One helpful intuition is the following: if we run AKS for only _o_(log_n_) cycles, in general, we cannot guarantee sortedness within each segment of length _n/_2<sup>_o_(log_n_)</sup>. Specifically, had the number of distinct keys been large, running AKS for only _o_(log_n_) cycles could produce an outcome that is far from sorted (i.e., a large number of elements are misplaced in the _wrong position_ even they are in their correct segments).

Fortunately, our input array has relatively few distinct keys -- specifically, at most 2_<sup>k</sup>_ distinct keys. This means that if the array were fully sorted, then almost every segment consists of identical keys except for 2_<sup>k</sup>_ segments. In this case, applying a (2<sup>-8_k_</sup>,2<sup>3_k_</sup>)-orderly segmenter results in an array that is close to fully sorted, i.e., only a small _O_(1/2<sup>2_k_</sup>) fraction of elements are misplaced in the wrong position. Given this crucial observation, what remains to be done is to _extract_ the misplaced elements, _sort_ them, and _route them back_ into the original positions while preserving the sorted order. We now discuss how to accomplish this goal -- doing so turns out to be rather non-trivial, and we first need to construct some new building blocks which we describe next.

## 2.1.2 Additional New Building Blocks

Henceforth, let _K_:=2_<sup>k</sup>_. We will need the following new building blocks to be able to extract, sort, and route back the remaining errors.

**SlowSort**_<sup>K</sup>(A_)**:** an inefficient oblivious sort algorithm -- when given an array _A_ of length _m_ with at most _K_:=2_<sup>k</sup>_ distinct keys, the algorithm outputs a sorted permutation of _A_. We would like to accomplish **SlowSort**_<sup>K</sup>(A_) in _O(mK_) total work and _O_(log_m+k_) depth, since later we will apply **SlowSort**_<sup>K</sup>(A_) to arrays of size _n/K_ where _n_ is the length of the larger array we need to sort.

It turns out that even this slow version is somewhat non-trivial to construct. The most obvious idea, that is, relying on AKS \[AKS83\], does not work. AKS would have incurred _O(m_log_m_) work; and for small choices of _K_, log_m_ could be larger than _K_.

We instead make _K_ copies of the input array: in the _u_-th copy, we want to put elements with the key \(u\in[0,K-1]\) into the right positions, where as all other elements should be fillers. If we can accomplish this, we can sort _A_ by performing a coordinate-wise _K_-way selection among the _K_ arrays.

Specifically, let _s<sub>u</sub>_ be the number of elements smaller than _u_. In the sorted array, elements with the key _u_ should appear in positions _s<sub>u</sub>_+1_,s<sub>u</sub>_+2_,...,s_<sub>_u_+1</sub>. Now, in the _u_-th copy, we preserve all the elements with the key _u_ but replace all other elements with fillers. We mark exactly _s<sub>u</sub>_ fillers with the key \(-\infty\) and the mark rest of fillers with the key \(\infty\). Now, the _u_-th copy of the problem boils down to sorting _m_ elements with 3 different keys. We show that this can be accomplished in linear time and logarithmic depth, if we leverage the linear-work, logarithmic depth oblivious compaction \[AKL<sup>+</sup>20b\] algorithm (we defer the details of the construction to subsequent technical sections).

<sup>3</sup>An \(\epsilon\)-near-sorter is a constant depth comparator circuit described by Ajtai et al. \[AKS83\], which we will formally define in the subsequent technical sections.

