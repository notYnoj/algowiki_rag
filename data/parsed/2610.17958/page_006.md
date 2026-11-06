<tbc>have an LCP of length at least \(\ell\), which suffices for our purposes. The whole process thus takes \(\mathcal{O}(N_V\cdot(d+1))\) time. Since this list is sorted, identical length-\(\ell\) prefixes (here identical means with _d_ wildcards) are _grouped_ and so each group member gets the same rank from \[0_,N<sub>V</sub>_).

Two length-\(\ell\) substrings are identical under _H_ if and only if their constituent fragments between the indices of _H_ are identical. By treating each substring as a tuple of ranks corresponding to these fragments--specifically (_r_<sub>1</sub>_,r_<sub>2</sub>_,...,r_<sub>_d_+1</sub>)--and applying radix sort, we obtain a lexicographical ordering (of the suffixes) based strictly on the subsequence of non-wildcard characters. This correctly groups all occurrences of a specific motif _M_ into a contiguous range in the sorted list.

The ranks (unique identifiers) are stored in the array R returned by Algorithm 4.1, indexed by the starting position of each suffix in _S<sub>V</sub>_. Given \(u\in V\) and an offset _i_, the length-\(\ell\) prefix of the corresponding suffix is exactly the length-\(\ell\) substring \(u[i..i+\ell-1]\); hence, a single lookup in R returns its identifier in O(1) time, which is invariant under replacing the positions in _H_ by \(\diamond\), as claimed. The _d_ radix-sort rounds and the LCP array scans each cost O(_N<sub>V</sub>_) time. In total, the algorithm costs O((_d_+1)_N_) time and uses O(_N_) working space.\(\square\)

_Remark_ 4.2. The technique in Lemma 4.1 is inspired by the construction of the _gapped suffix array_ \[4\]. A notable difference is the following: since \(\ell\) is fixed, _we avoid the use of LCE queries_ (cf. \[14\]), and compute the relevant LCP values by comparing integers in O(1) time (Lines 8-17). While this makes no difference in theory, it is crucial in practice, as LCE data structures are typically either costly to construct or costly to query.

Theorem 4.3. _There is an algorithm for_ \((\ell,d)\)_- CMM with f<sub>E</sub> running in time_

\(\mathcal{O}\left(\genfrac(){pt}{2}{\ell}{d}^2N^2\right),\)

_where_ \(N:=\sum_{v\in V}|v|\)_. The space used is_ O(_N)._

_Proof._ We solve \((\ell,d)\)-CMM by a slight adaptation of the algorithm from Section 3. Fix a pair \((H,H')\) of wildcard combinations, one for _X_ and one for _Y_ . In a pre-processing step, we sort the characters occurring in all strings \(v\in V\) , thus mapping them onto the range {1,2_,...,N_}. This is done once in O(_N_log_N_) time. We now apply Lemma 4.1 that takes O((_d_+1)_N_) time using O(_N_) space, and obtain, for every length-\(\ell\) substring _X_ (resp. _Y_ ) of a node, an identifier rank(_X_) (resp. rank(_Y_ )) under _H_ (resp. under \(H'\)) such that: any two length-\(\ell\) substrings receive the same identifier if and only if they agree on all non-wildcard positions.

**Algorithm 4.1** Rank assignment to \((\ell,d)\)-motifs. See the proof of Lemma 4.1.

Input: Wildcard positions \(H=\{h_1<\cdots<h_d\}\subseteq[\ell]\); string \(S_V=v_1\#_1v_2\#_2\dots v_{|V|}\#_{|V|}\); suffix array SA<sub>_S<sub>V</sub>_</sub>; LCP array LCP<sub>_S<sub>V</sub>_</sub><br>
Output: Array R such that R\[i\] is the rank of suffix<br>
S<sub>V</sub>\[i..|S<sub>V</sub>|\] by its length-\(\ell\) prefix, in lexicographic order ignoring the positions in H<br>
1: Let S be the positions i such that \(S_V[i..i+\ell-1]\) is defined and contains no separator<br>
\(\mathsf{R}[i]\leftarrow 0\) for each \(i\in\mathcal{S}\)<br>
Add h<sub>0</sub>:=0 and \(h_{d+1}:=\ell+1\) to \(H\triangleright\) Handle intervals before first and after last wildcard<br>
for \(t\leftarrow 0\) to d<br>
   \(I_t=(h_t,h_{t+1})\triangleright\) Non-\(\diamond\) interval<br>
   if I<sub>t</sub> is empty then continue<br>
   \(\blacktriangleright\) Step 1: Compute ranks for I<sub>t</sub><br>
   \(\mathsf{rank}\leftarrow 0\); \(\mathsf{R}'[\mathsf{SA}_{S_V}[1]]\leftarrow 0\)<br>
   for \(j\leftarrow 2\) to |S<sub>V</sub>|<br>
   if LCP<sub>_S<sub>V</sub>_</sub>\[j\]\<|I<sub>t</sub>| then rank \(\leftarrow\) rank+1<br>
   \(\mathsf{R}'[\mathsf{SA}_{S_V}[j]]\leftarrow\) rank<br>
   \(\blacktriangleright\) Step 2: Refine by (current rank, rank for I<sub>t</sub>)<br>
   Stably sort S by key(j)=(R\[S\[j\]\], \(\mathsf{R}'[\mathcal{S}[j]+h_t]\))<br>
   \(\mathsf{rank}\leftarrow 0\); \(\widehat{\mathsf{R}}[\mathcal{S}[1]]\leftarrow 0\)<br>
   for \(j\leftarrow 2\) to |S|<br>
   if \(\mathsf{key}(j)\neq\mathsf{key}(j-1)\) then rank \(\leftarrow\) rank+1<br>
   \(\widehat{\mathsf{R}}[\mathcal{S}[j]]\leftarrow\) rank<br>
   \(\mathsf{R}\leftarrow\widehat{\mathsf{R}}\)<br>
return R

Namely, we view rank(_X_) as the equivalent of the rank from Algorithm 3.1.

These identifiers satisfy the two properties that the proof of Theorem 3.1 requires of the rank: they let us (1) test equality of two (wildcarded) length-\(\ell\) substrings in O(1) time and (2) index the dictionary _C_ in O(_N_) space. Hence, we run Algorithm 3.1 verbatim on the fixed pair \((H,H')\), substituting the wildcard-aware ranks for the plain ranks. By Theorem 3.1, this computes the maximum _f<sub>E</sub>_ over all motif pairs whose wildcards sit at positions \((H,H')\) in O(_N_<sup>2</sup>) time and O(_N_) space.

Since the problem requires maximizing an objective function over unknown (non-fixed) wildcard positions, the algorithm iterates through all possible pairs of _d_- size subsets \(H\subset[\ell]\). This exhaustive search guarantees completeness: if an optimal motif pair {_X,Y_} exists with a specific wildcard configuration, the algorithm will inevitably process it during the iteration. Running the above for each of the \(\genfrac(){pt}{2}{\ell}{d}\) choices of _H_ and \(\genfrac(){pt}{2}{\ell}{d}\) choices of \(H'\) and taking the overall maximum therefore solves

