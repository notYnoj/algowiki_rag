1 if \(A=\emptyset\) then return \(\emptyset\);<br>
   \(x\leftarrow\) An element chosen u.a.r. from A;<br>
   \(B\leftarrow\) a set obtained by selecting each element of A\\{x} independently with probability 1/2;<br>
   if \(|B|\le h-1\) then<br>
   return \(B\cup\{x\}\cup\mathsf{RandomSubset}(A\backslash(B\cup\{x\}),h-|B|-1)\)<br>
   else<br>
   return RandomSubset<br>
(<br>
_B,h_<br>
)

## A Sampling a subset of a given size using a linear number of random bits

This appendix is devoted to proving the following lemma, which was used in Section 7.1 as part of our derandomization of RiffleSort.

Lemma 7.1. _There exists an algorithm that, given any set A of N elements and an integer_ \(h\in\{0,\dots,N\}\)_, returns a set chosen uniformly at random among all subsets of A with exactly h elements. The algorithm requires O(N_) _time and at most_ 60_N random bits with probability at least_ \(1-O\left(e^{-\sqrt{N}}\right)\).

To this aim, we design a recursive algorithm named RandomSubset, whose pseudocode is given in Algorithm 3. To sample a random subset of cardinality \(h\in 1,\dots,N\) from an input set _A_ of _N_ elements,<sup>11</sup> RandomSubset starts by choosing an element _x_ u.a.r. from _A_, and a set _B_ that contains each element of _A_\\{_x_} independently with probability \(\frac{1}{2}\). Then, if |_B_| is smaller than _h_, the algorithm returns a set containing _x_, all the elements in _B_, and all the elements in a subset of size _h_-|_B_|-1 that is recursively sampled from \(A\backslash(B\cup\{x\})\). Otherwise, when _B_ contains at least _h_ elements, the algorithm returns a subset of size _h_ that is recursively sampled from _B_ (notice that it might be |_B_|=_h_).

Next lemma shows that the subset returned by RandomSubset (_A,h_) is chosen u.a.r. among all subsets of _A_ with _h_ elements, as desired.

Lemma A.1. _For any set A of N elements, any integer_ \(h\in\{0,\dots,N\}\)_, and any_ \(Z\in\genfrac(){pt}{2}{A}{h}\)_, it holds that_ \(Pr(\mathsf{RandomSubset}(A,h)=Z)=\genfrac(){pt}{2}{|A|}{h}^{-1}\).

Proof. The proof is by induction on _N_. Line 1 of Algorithm 3 ensures that the claim holds for the base case _N_=0. Hence, in the rest of the proof, we consider _N\>_0, we assume that the claim holds for all sets with less than _N_ elements, and we show that it holds for all sets with _N_ elements.

Focus on the execution of RandomSubset (_A,h_), let _R_ be the returned subset, and consider the element _x_ and the set _B_ selected in lines 2 and 3, respectively. Using \(0\le|B|<N\) and \(Pr(|B|=i)=\frac{\genfrac(){pt}{2}{N-1}{i}}{2^{N-1}}\) for _i_=0_,...,N_-1, we have:

\(Pr(R=Z)=\sum_{i=0}^{N-1}Pr(R=Z||B|=i)\cdot Pr(|B|=i)\)<br>
\(=\frac{1}{2^{N-1}}\left(\sum_{i=0}^{h-1}\genfrac(){pt}{2}{N-1}{i}Pr(R=Z||B|=i)+\sum_{i=h}^{N-1}\genfrac(){pt}{2}{N-1}{i}Pr(R=Z||B|=i)\right).\)

<sup>11</sup>The case _h_=0 is trivial and is handled in line 1 by returning the empty set.

**Algorithm 3:** RandomSubset(_A,h_)

