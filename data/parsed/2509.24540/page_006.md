## 23:6 Simple in-place yet comparison-optimal Mergesort

index whenever a cycle end is detected, is sufficient, as depicted in the pseudocode given in Algorithm 1. These optimizations slightly enhance the STL rotation algorithms given in [10].

\(\blacktriangleright\) Note 1. A rotation in the opposite direction can be achieved with a negative offset _r_, which can also be done with the corresponding positive offset _n-r_. For simplicity reasons, the given pseudocode works for \(0\le r<n\) and rotates the given array to the left.

As this optimal rotation algorithm moves every element exactly once, its running time is trivially bounded by O(_n_). Since it uses only a few basic variables, it needs O(1) additional space to do so. It is important to note that this array rotation only moves, i.e., copies, data elements, but it does not do any element comparisons at all.

## 2.2 Co-ranking

It has been commonly known for at least 30 years how to find the shared median element of two given sorted arrays in logarithmic time (see, e.g., exercise 9.3-8 in [5] on page 223). However, in the case of _Mergesort_, we do not want to split an array at the median element but instead at the middle position (cf. Algorithm 3). Although somewhat similar in nature, utilizing such a median solution becomes difficult, especially when also considering duplicate keys and thus ensuring stability. As such, finding the corresponding indices of this middle position within the two given arrays seemed harder, i.e., slower than logarithmic time, before and was sometimes even disputed as being possible in an efficient way. The relatively new _co-ranking_ algorithm solves this problem directly and will thus be the second prerequisite that we utilize for our _in-place Mergesort_. The theoretical foundations of _co-ranking_ are published in [12], and various practical implementations for distributed memory machines using _MPI_ one-sided communications are presented in [11]. This algorithm was originally developed to parallelize the _Merge_ step of _Mergesort_ efficiently. Only later did we realize that

Listing 1 optimal_rotate(A,r) rotates a given array // optimal_rotate(A,r) rotates an array A[] with n elements // by an arbitrary offset r (with 0 ≤ r<n) to the left. // It runs in optimal time O(n) using only O(1) additional space. int work,s,i,n,next type first n ← |A| // number of elements in A if (n>0)&& (r>0) work ← n // number of elements to move for s ← 0;work>0;s++ i ← s first ← A[s] // keep "old" first element of cycle repeat next ← i + r if next ≥ n next ← next-n // handle wrap-around end if if next == s A[i] ← first // last element in cycle else A[i] ← A[next] // move one element end if i ← next work-- until i ==s // Cycle completed? end for end if

