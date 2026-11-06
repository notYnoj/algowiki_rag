\(\text{\texttt{select}}_B(k)=min\{j\in[1,n]:\text{\texttt{rank}}_B(j)=k\}\text{\textit{that returns the position of the kth one in}}B\text{\texttt{.}}\)

We use a folklore technique called _static space allocation_, which allows us to store \(\ell\) items of different size in a compact manner, e.g., a sequence of self-delimiting numbers. The following formal description is adapted from [35]. Let _S_ be a sequence of \(\ell\) items _B<sub>k</sub>_ such that each item _B<sub>k</sub>_ occupies _d<sub>k</sub>_ bits for \(k\in\{1,\dots,\ell\}\) and let \(N=\sum_{k\in\{1,\dots,\ell\}}d_k\). Using a simple bitstring _B_ of length _N_ with a bit set to 1 exactly at all indices \(k+\sum_{j=1}^{k-1}d_k\) for all values _k_, following by constructing a rank-select data structure for _B_, one can easily gain random-access to each element \(B_k\in S\) as obtaining the index of the first bit that belongs to _B<sub>k</sub>_ as `select`_<sub>B</sub>(k_)-_k_. This requires \(|S+\ell|+o(|S+\ell|)\) bits in addition to the bits required to store _S_.

A final data structure we require is a _choice dictionary_.

\(\blacktriangleright\) **Lemma 2.** _(choice dictionary [36, 37]) There is a data structure C initialized for universe_ \(U=\{1,\dots,\ell\}\) _that occupies_ \(\ell+o(\ell)\) _bits and is initialized in_ \(O(\ell)\) _time. The data structure allows the following constant time (per element) operations:_

\(\text{\texttt{insert}}(i)\text{\textit{: Insert}}x\in U\text{\textit{into}}C\)

\(\text{\texttt{remove}}(i)\text{\textit{: Remove}}x\in U\text{\textit{from}}C\)

\(\text{\texttt{contains}}(i)\text{\textit{: Return true exactly if}}x\in C\text{\textit{.}}\)

\(\text{\texttt{choice}}(i)\text{\textit{: Return an arbitrary element x from}}C\)

\(\text{\texttt{iterate}}\text{\textit{: Iterate over all elements}}x\in C\text{\textit{.}}\)

## 3 Sorting and Ranking

In this section we consider sorting and ranking of _k_ self-delimiting numbers, stored within an _N_-bit sequence _S_. We make use of _lookup tables_, which are precomputed tables storing the answer for every possible state of a finite universe, typically of small size. We use such tables to quickly solve sub-problems that occur in our algorithms. For the rest of this section we assume that a parameter \(\tau\) with \(logN\le\tau\le w\) (where _w_ represents the word size) is given to our algorithms, which we use as a parameter to construct lookup tables for binary sequences of length \(\lceil\tau/2\rceil\). To give an intuitive example of such lookup tables, the universe might consist of all integers of size at most \(2^{\lceil\tau/2\rceil}\) and answer queries if the given number is prime. Such a table has \(2^{\lceil\tau/2\rceil}\) entries, and each index into the table requires \(\lceil\tau/2\rceil\) bits. Note that larger values of \(\tau\) result in faster runtimes at the cost of increased space-usage.

In our application for sorting, _S_ is a sequence of _N_ bits containing self-delimiting numbers. By this, each number in _S_ is of size _m=O_(2_<sup>N</sup>_). Let \(q=2^{N/\tau}\) and call \(x\in S\) _big_ if _q\<x_, otherwise call _x small_. We have to handle small and big numbers differently. To divide the problem we scan through _S_ and write each small number of _S_ into a sequence \(S_{\le q}\) and each big number into a sequence _S<sub>\>q</sub>_. On the word-RAM model, scanning through an _N_-bit sequence _S_ and reporting all _k_ numbers takes \(O(k+N/\tau)\) time, which is the time bound of all our sorting algorithms. After sorting both sequences we write the sorted numbers of \(S_{\le q}\), followed by the sorted numbers of _S<sub>\>q</sub>_, into a sequence \(S'\) of _N_ bits.

We first consider the sequence \(S_{\le q}\). Our idea is to run first an adaptation of stable counting sort to _presort_ the numbers in several _areas_ such that an area _A<sub>i</sub>_ consists of all numbers that require exactly _i_ bits as self-delimiting number. By doing so we roughly sort the sequence \(S_{\le q}\) as all numbers of area _A<sub>i</sub>_ are smaller than any number of area _A<sub>j</sub>_ for all _i\<j_. We then sort each area independently by another stable counting-sort algorithm.

