subsequence such that every element is smaller (according to \(\prec\)) than its predecessor in the sequence.

It is well known that \(\mathsf{LIS}_\prec(x)\) can be computed for an input sequence _x_ of length _n_ in \(\tilde{\mathcal{O}}(n)\) time [Knu73, Fre75]. Our algorithm requires fast approximated LIS computation in the (partially) dynamic settings, where elements are deleted from _x_ and we wish to approximate \(\mathsf{LIS}_\prec(x)\) or \(\mathsf{LDS}_\prec(x)\) throughout the sequence of deletions. To this end, we employ the result of Gawrychowski and Janczewski [GJ21] (see also [KS21]), who provide a dynamic algorithm maintaining a constant approximation of \(\mathsf{LIS}_\prec(x)\) in the more general settings in which both insertions and deletions are allowed.

\(\blacktriangleright\) **Lemma 4** ([GJ21, Theorem 1 and subsequent discussion])**.** _There is a fully dynamic algorithm maintaining a_ 2_-approximation of_ \(|\mathsf{LIS}_\prec(x)|\) _with insertions and deletions from a sequence x working in_ \(\tilde{\mathcal{O}}(1)\) _worst-case time per update. Furthermore, if the returned approximation is k, then in O(k_) _time, the algorithm can also provide an increasing subsequence of length k._

For a sequence _x_ and a set of symbols \(\pi\), we define the following functions:

Project\((x,\pi)\) - the subsequence of _x_ consisting only of symbols in \(\pi\).

Exclude\((x,\pi)\) - the subsequence of _x_ consisting only of symbols not in \(\pi\).

A sequence \(\pi=\pi_1,\pi_2,\dots,\pi_{|\pi|}\) is called _repetition-free_ sequence if for every \(i\neq j\in[|\pi|]\) we have \(\pi_i\neq\pi_j\). When using Project and Exclude, we often abuse notation by using a (repetition-free) sequence in place of a set of symbols. In such cases, we refer to the set implicitly defined by the sequence, namely \(\{\pi_i|i\in[|\pi|]\}\).

We often interpret a repetition-free sequence \(\pi\) as a total order over the symbols of the sequence. Specifically, the total order \(<_\pi\) over the symbols of \(\pi\) is defined as \(\sigma<_\pi\sigma'\) if and only if \(\sigma=\pi_i\), \(\sigma'=\pi_j\) and _i\<j_, i.e., \(\sigma\) occurs before \(\sigma'\) in \(\pi\). We slightly abuse notation by writing \(\mathsf{LIS}_\pi(x)\) (for a sequence _x_ over the symbols of \(\pi\)) to denote a longest increasing subsequence of _x_ with respect to the total order \(<_\pi\) (instead of the more accurate and cumbersome \(\mathsf{LIS}_{<_\pi}(x)\)). We further generalize the notation \(\mathsf{LIS}_\pi(x)\) to be applicable to sequences _x_ over any alphabet. To allow this, we define \(\mathsf{LIS}_\pi(x)=\mathsf{LIS}_\pi(\mathsf{Project}(x,\pi))\) if _x_ contains symbols not in \(\pi\).

**Erdős-Szekeres theorem.** The following well-known lemma by Erdős and Szekeres [ES35] will be useful for our algorithms.

\(\blacktriangleright\) **Lemma 5** (Erdős-Szekeres [ES35])**.** _Let x be a repetition-free sequence of length_ |_x|, and let_ \(\prec\) _be a total order on the elements of x. Let_ \(i=|\mathsf{LIS}_\prec(x)|\) _and_ \(d=|\mathsf{LDS}_\prec(x)|\)_. Then,_ \(i\cdot d\ge|x|\).

## 3 Warm-up Algorithm

In this section, we introduce a warm-up algorithm (see Algorithm 1). The algorithm is composed of three parts. Each part computes a common subsequence of _x_ and _y_ which is a candidate for the output of the algorithm. At the end, the output is the longest candidate.

At the first part of the algorithm, the algorithm computes BestMatch(_x,y_), which is a longest common subsequence of _x_ and _y_ among subsequences composed of a single symbol from \(\Sigma\), as a candidate.

In the second part, the algorithm selects a repetition-free subsequence \(\pi\) of _x_. Specifically, it considers the repetition-free subsequence \(\pi=\mathsf{RF}(x)\), which consists of the first occurrence of each symbol in _x_. We interpret \(\pi\) as a total order over the symbols of _x_. We note that any arbitrary repetition-free subsequence of _x_ containing all symbols of _x_ would be sufficient for

