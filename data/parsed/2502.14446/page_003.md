using their _fingerprints_, the distances are verified only on matching fingerprint pairs, allowing the algorithm to compute just a fraction of all the distance computations.

Using LSH requires setting up a number of parameters. The framework developed by PUFFIN \[5\] is capable of automatically tuning these parameters for _k_-nearest neighbors queries. Christiani et al. \[13\] developed a technique to automatically find the best number of concatenations and repetitions to successfully answer a nearest neighbor query with a certain probability even when the probability of collision between pairs of points is unknown. We follow the PUFFINN implementation \[5\], expanding on the case where the pairs are actually ordered sets.

## 3 PRELIMINARIES

### 3.1 Time Series and Motifs

We will start our introduction from the special case of a single dimension time series.

**Definition 3.1.** A _time series_ \(T\in\mathbb{R}^n\) is an ordered sequence of real valued numbers \(T=[t_1,\dots t_n]:t_u\in\mathbb{R},\forall i\in[1,n]\) where _n_ is the length of the time series.

**Definition 3.2.** A _time series subsequence_ \(T_{u,w}\in\mathbb{R}^w\) is a subset of adjacent elements from T starting at position _u_ and length _w_, _T<sub>u,w</sub>=_\[_t<sub>u</sub>,...t_<sub>_u+w_-1</sub>\].

**Definition 3.3.** The _z-normalized Euclidean Distance_ between two time series subsequences _T<sub>u,w</sub>_ and _T<sub>v,w</sub>_ is defined as:

\(dist\left(T_{u,w},T_{v,w}\right)=\sqrt{\sum_{i\in[w]}\left(\frac{T_u(i)-\mu(T_{u,w})}{\sigma(T_{u,w})}-\frac{T_v(i)-\mu(T_{v,w})}{\sigma(T_{v,w})}\right)^2}\) (1)

where \(\mu\) and \(\sigma\) are the means and the standard deviations of the subsequences, respectively, and _T<sub>u</sub>(i_) is the _i_-th value of subsequence _T<sub>u,w</sub>_.

**Definition 3.4.** A _time series motif_ is the pair of subsequences _T<sub>u,w</sub>_ and _T<sub>v,w</sub>_:

\(dist\left(T_{u,w},T_{v,w}\right)\le dist\left(T_{a,w},T_{b,w}\right)\)

for all \(a,b\in[1,\dots n-w+1]\).

It comes that overlapping sequences are more likely to satisfy the condition above, these pairs are excluded in the problem formulation by ensuring no trivial matches.

**Definition 3.5.** A pair of subsequences _T<sub>u,w</sub>_ and _T<sub>v,w</sub>_ is a _trivial match_ when: _v=u_ or if, given an exclusion zone \(\epsilon>0\), then \(|u-v|\le\epsilon\).

Common values for the exclusion zone \(\epsilon\) are fractions of _w_ to exclude matches in the neighboring area of a subsequence \[42, 44\]. We employ \(\epsilon=w/2\).

Expanding upon the single dimensional case, the notions for the _multidimensional_ case are derived.

**Definition 3.6.** A _multidimensional time series_ \(\mathbf{T}\in\mathbb{R}^{n\times D}\) is a tuple of _D_ time series \(T^{(j)}\in\mathbb{R}^n:\mathbf{T}=\left(T^{(1)},\dots T^{(D)}\right)\) where _D_ is the dimensionality of **T** and _n_ is its length.

**Definition 3.7.** A _multidimensional subsequence_ \(\mathbf{T}_{u,w}\in\mathbb{R}^{w\times D}\) is a tuple of unidimensional subsequences from **T** starting at position _u_ and length _w_, \(\mathbf{T}_{u,w}=\left(T_{u,w}^{(1)},\dots T_{u,w}^{(D)}\right)\).

When clear from context we will omit the subscript _w_ from the subsequence notation.

Given two multidimensional subsequences, we are interested in computing their distance. However, as we mentioned oftentimes considering all dimensions in this computation is uninteresting at best, misleading at worst. Following \[41\] we therefore consider only a subset of _d_ dimensions when computing the distance.

**Definition 3.8.** The _d_-dimensional distance between two subsequences **T**_<sub>a</sub>_ and **T**_<sub>b</sub>_ is<tbc>

\(dist_d\left(\mathbf{T}_a,\mathbf{T}_b\right)=min_{F\subseteq 2^{\left\lfloor D\right\rfloor,\left|F\right|=d}}\sum_{f\in F}dist\left(\mathbf{T}_a^f,\mathbf{T}_b^f\right)\)

<tbc>In other words, we select a subset of the dimensions of size _d_ such that the sum of the distances between the individual dimensions is minimized. Similarly, with<tbc>

\(dims_d\left(\mathbf{T}_a,\mathbf{T}_b\right)=argmin_{F\subseteq 2^{\left\lfloor D\right\rfloor,\left|F\right|=d}}\sum_{f\in F}dist\left(\mathbf{T}_a^f,\mathbf{T}_b^f\right)\)

<tbc>we denote the _d_ dimensions that define the distance between two subsequences. Note that this set of dimensions is potentially different for different pairs of subsequences. Furthermore, for a given pair of subsequences we name the distance of the dimensions maximally far apart among the ones belonging to dims_<sub>d</sub>_ (**T**_<sub>a</sub>,_**T**_<sub>b</sub>_):<tbc>

\(dist_d^{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)=max_{f\in dims_d\left(\mathbf{T}_a,\mathbf{T}_b\right)}dist\left(\mathbf{T}_a^f,\mathbf{T}_b^f\right)\) (2)

<tbc>**Definition 3.9.** A _d_-dimensional motif is the pair of subsequences **T**_<sub>a</sub>,_**T**_<sub>b</sub>_ such that

\(dist_d\left(\mathbf{T}_a,\mathbf{T}_b\right)\le dist_d\left(\mathbf{T}_u,\mathbf{T}_v\right)\forall u,v\in[n-w+1]\)

We are interested in finding the most similar subsequences in an unknown subspace.

**Definition 3.10.** Given a _D_-dimensional time series **T**, motif length _w_, motif dimensionality _d_, and a distance function _dist_, the _top-k multidimensional motifs_ are the _k_ subsequences and their subspaces _F_ that minimize the _d_-dimensional distance with respect to all other

\begin{tabular}{cc}
**T** & Multidimensional time series \\
**Tw** & Set of subsequences from **T** of length _w_ \\
**T**_<sub>a</sub>_ & Subsequence at index _a_ \\
\(\mathbf{T}_a^f\) & Dimension _f_ of subsequence **T**_<sub>a</sub>_ \\
_D_ & Dimensionality of the time series \\
_d_ & Dimensionality of the motifs to discover \\
\(dist\left(\cdot,\cdot\right)\) & Distance function \\
\(dist_d\left(\cdot,\cdot\right)\) & _d_-dimensional distance function \\
\(dims_d\left(\cdot,\cdot\right)\) & dimensions involved in the computation of the _d_-dimensional distance function \\
_k_ & Number of motifs to find \\
\(h_{i,j}\left(\mathbf{T}_a^f\right)\) & hash value of length _i_ at repetition _j_ for dimension _f_ of subsequence **T**_<sub>a</sub>_ \\
_L_ & Number of repetitions for LSH \\
_K_ & Number of concatenations for LSH \\
\end{tabular}

** 1:  of symbols.**

