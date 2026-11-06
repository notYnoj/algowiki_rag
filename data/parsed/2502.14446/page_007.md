From this we now derive two lemmas on the success probability of the discovery. In Lemma 5.3 we allow each motif to fail independently, in Lemma 5.4 we require that all the returned motifs are correct within a probability.

Lemma 5.3. _Algorithm 1 finds the true top-k motifs, each with probability_ \(\ge 1-\delta\).

Proof. Let the stopping condition be met at iteration \(i'\) and concatenation \(j'\), _m_<sub>1</sub>_,...m<sub>k</sub>_ be the set of motifs returned by the algorithm, sorted by increasing distances. We have that the failure probability of _m<sub>h</sub>_, \(h\in[1,k]\) is upper bounded by the failure probability _m<sub>k</sub>_ for the monotonicity of the collision probability. This failure probability is given by Lemma 5.2, by construction the stopping condition ensures that this probability is \(\le\delta\). This is valid for all returned pairs independently.

If the stopping condition is never met the algorithm reaches line 20, where all pairs of subsequences are considered, thus returning the correct motifs with probability 1. □

Given this lemma it is easy to derive the expected recall of the algorithm, that corresponds to \(1-\delta\).

Lemma 5.4. _When called with failure probability_ \(\delta'=\delta/k\)_, Algorithm 1 finds the true top-k motifs with probability_ \(\ge 1-\delta\).

Proof. From Lemma 5.3 we have that each pair fails independently with probability \(\le\delta'=\delta/k\). By applying a union bound on the _k_ pairs we obtain the statement. □

## 5.2 Number of Distance Computations

First, we introduce the concept of _contrast_, which will be useful in capturing the difficulty of a dataset and in relating it to the complexity of our algorithm.

**Definition 5.1.** For a _D_-dimensional time series **T** of length _n_, and for parameters _k_ and _d_ let (**T**_<sub>a<sub>k</sub></sub>,_**T**_<sub>b<sub>k</sub></sub>_) and (**T**_<sub>a<sub>n</sub></sub>,_**T**_<sub>b<sub>n</sub></sub>_) be the _k_-th and _n_-th motifs, respectively. We define

\(\text{contrast}_{d,k|n}(\mathbf{T})=\frac{\text{dist}_d^{max}\left(\mathbf{T}_{a_n},\mathbf{T}_{b_n}\right)}{\text{dist}_d^{max}\left(\mathbf{T}_{a_k},\mathbf{T}_{b_k}\right)}\)

The following theorem ensures that our algorithm computes, in expectation, a subquadratic number of distances in expectation, assuming we give to the algorithm enough memory. The complexity is parameterized by the contrast of the motifs in the multivariate time series: a large contrast implies a smaller complexity.

Theorem 5.5. _On a D-dimensional time series_ **T** _of length n, with parameters_ \(k\ge 1\), \(d\in[1,D]\), \(\delta\in(0,1)\)_, Algorithm 1 computes_

\(O\left(n^{1+1/c}log\frac{1}{\delta}+Lk\right)\)

_distances in expectation, where_ \(c=\text{contrast}_{d,k|n}(\mathbf{T})\)_, for_ \(L\in\Omega\left(n^{1/c}\right)\).

Proof. Let T be the set of all the subsequence pairs of **T**. For any pair of subsequence indices (_a,b_), let \(p_{ab}=P\left(\text{dist}_d^{max}\left(\mathbf{T}_a,\mathbf{T}_b\right)\right)^d\).

Consider (**T**_<sub>a<sub>k</sub></sub>,_**T**_<sub>b<sub>k</sub></sub>_) and (**T**_<sub>a<sub>n</sub></sub>,_**T**_<sub>b<sub>n</sub></sub>_), the _k_-th and _n_-th _d_-dimensional motifs of **T**, and let _p_<sub>1</sub>=_p<sub>a<sub>k</sub>b<sub>k</sub></sub>_ and _p_<sub>2</sub>=_p<sub>a<sub>n</sub>b<sub>n</sub></sub>_. Furthermore, let \(\rho=\frac{log1/p_1}{log1/p_2}\).

For notational convenience, define the following operator that gives the expected number of distance computations carried out in _j_ independent repetitions with hash prefixes of length _i_:

\(\text{ED}\left(i,j\right)=j\cdot\left(\sum_{\left(\mathbf{T}_a,\mathbf{T}_b\right)\in\mathbb{T}}p_{ab}^i\right)\)

Recall that, for hash prefixes of length _i_, examining \(\frac{log1/\delta}{p_1^i}\) inde pendent repetitions ensures that the top _k_ motif pairs are seen at least once with probability at least \(1-\delta\). Using the notation shorthand defined above, the number of expected distance computations in this case is \(\text{ED}\left(i,\frac{log1/\delta}{p_1^i}\right)\).

Now define T_<sub>\>k</sub>_ and T_<sub>\>n</sub>_ as the sets of subsequence pairs that are farther than the _k_-th and _n_-th motifs, respectively. Then we have

\(\text{ED}\left(i,\frac{log1/\delta}{p_1^i}\right)\le\frac{log1/\delta}{p_1^i}\cdot\left(n+\sum_{\left(\mathbf{T}_a,\mathbf{T}_b\right)\in\mathbb{T}_{>n}}p_{ab}^i\right)\le\frac{log1/\delta}{p_1^i}\cdot\left(n+\genfrac(){pt}{2}{n}{2}p_2^i\right)\text{(7)}\)

where the inequality follows from the definition of T_<sub>\>n</sub>_.

Defining \(i^*=\frac{logn}{log\frac{1}{p_2}}\) we have \(\genfrac(){pt}{2}{n}{2}p_2^{i^*}\le n\) and \(\frac{1}{p_1^{i^*}}=n^\frac{log1/p_1}{log1/p_2}=n^\rho\).

Therefore there is a prefix length _i_<sup>∗</sup> for which the number of expected distance computations to see the _k_-th motif colliding at least once is

\(\text{ED}\left(i^*,\frac{log1/\delta}{p_1^{i^*}}\right)=O\left(n^{1+\rho} log\frac{1}{\delta}\right)=O\left(n^{1+\frac{1}{c}}log\frac{1}{\delta}\right)\) (8)

where _c_=contrast_<sub>d,k|n</sub>_(**T**) and the equality follows from the definition of \(\rho\) for the LSH family we employ in our algorithm.

Now, let \(i'\ge i^*\) be the largest prefix _i_ such that the stopping condition holds. With probability \(1-\delta\) the algorithm stops at prefix \(i'\). Conditioned on this event, the number of distance computations carried out at level \(i'\) is

\(\text{ED}\left(i',\frac{log1/\delta}{p_1^{i^\prime}}\right)+\text{ED}\left(i'+1,L-\frac{log1/\delta}{p_1^{i^\prime}}\right)\) (9)

Where the second term accounts for the repetitions considered in iteration \(i'+1\) of the outer loop of the algorithm. First we bound the first term of the addition. Similarly to before, define T_<sub>\>k</sub>_ as the set of subsequence pairs that are farther away than the _k_-th motif.

\(\text{ED}\left(i',\frac{log1/\delta}{p_1^{i^\prime}}\right)\le Lk+\frac{log1/\delta}{p_1^{i^\prime}}\left(\sum_{\left(\mathbf{T}_a,\mathbf{T}_b\right)\in\mathbb{T}_{>k}}p_{ab}^{i^\prime}\right)\le^{(a)}Lk+\frac{log1/\delta}{p_1^{i^*}}\left(\sum_{\left(\mathbf{T}_a,\mathbf{T}_b\right)\in\mathbb{T}_{>k}}p_{ab}^{i^*}\right)\le Lk+\text{ED}\left(i^*,\frac{log1/\delta}{p_1^{i^*}}\right)=^{(b)}O\left(Lk+n^{1+\frac{1}{c}}log\frac{1}{\delta}\right)\)

where (a) follows from the fact that \(p_1\ge p_{ab}\) and (b) follows from Equation (8). The theorem follows by observing that the second term of Equation (9) is a factor 1_/p_<sub>1</sub>=_O_(1) larger than the first term. □

