Next we will use similar ideas to show hardness for center edit distance.

## 6.8 Center Edit Distance

Nicolas and Rivals present a very simple reduction from a specific version of (_k_-1)-LCS to _k_-Center Edit Distance. This reduction simply adds the empty string as the last string. The same concept works here. We can distinguish between the case where a (_k_-1)-LCS is greater than or equal to some constant _c_. Because, if all the strings in the _k_-LCS are of length _M_ adding a single empty string distinguishes between the (_k_-1)-LCS less than _M/_2 or greater than or equal to it. Why? Because, if the _k_-LCS at least _M/_2 then every string is _M/_2 deletions away from the target string _and_ the new empty string is as well! Otherwise, if the LCS is less than _M/_2, we are more than _M/_2 edits away provably. By adding characters to our (_k_-1)-LCS strings we can artificially increase the match (adding a large number of matching characters to each string), or artificially decrease it (add a large number of not-matching characters). By doing this we can go from our (_k_-1)-LCS being _c_ to our (_k_-1)-LCS being \(M'/2\), for our new length of strings.

**Lemma 6.21.** _Assume a k-LCS instance over k strings of length exactly M. If deciding whether the k-LCS distance is equal to M/_2 _over an alphabet of size_ \(|\Sigma|\) _can be done in T(M_) _time, then we can decide whether the k-LCS distance is equal to C over an alphabet of size_ \(|\Sigma|+k+1\) _for any constant C in time O(T(M_)+_kM)._

_Proof._ Let _S_<sub>1</sub>_,...,S<sub>k</sub>_ be an instance of _k_-LCS where we want to decide if the distance is exactly _C_. Let the _k_-LCS be LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>_).

For integers _a_ and _b_ let<tbc>

\(S'_i=@^aS_i\#_i^b.\)

<tbc>That is, we append _a_ @ symbols at the start and _b_#_<sub>i</sub>_ symbols at the end of each string. The#_<sub>i</sub>_ strings can not be matched. The @ symbols can be trivially matched. So we have that \(|S'_i|=M'=M+a+b\) and

\(\text{LCS}(S'_1,\dots,S'_k)=\text{LCS}(S_1,\dots,S_k)+a=C+a.\)

We simply want to choose values of _a_ and _b_ such that 2(_C+a_)=_n+a+b_. This simplifies to _a=M+b_-2_C_. If 2_C\>M_ then _b_=2_C-M_ and _a_=0. If 2_C\<M_ then _b_=0 and _a=M_-2_C_.

The length of these strings is \(M'=2C\) or \(M'=2M-2C\), both are less than 2_M_. So, in _O(kM_) time we can produce new strings of length \(M'\) where determining if the _k_-LCS is exactly \(M'/2\) determines if the original instance had distance exactly _C_.

Now we will show that _k_-center edit distance solves (_k_-1)-LCS.

**Theorem 6.22.** _We are given a k-LCS instance with strings S_<sub>1</sub>_,...,S<sub>k</sub> all of length M where k-LCS of these strings is denoted by_ LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>). The_ (_k_+1)_-center edit distance of S_<sub>1</sub>_,...,S<sub>k</sub> and emptystring_ \(\gamma\) _and k-LCS are related as follows._

\(\delta_{CE}(S_1,\dots,S_k,\gamma)\left\{\begin{array}{ c c }
=M/2 & \text{\textit{if}}\text{LCS}(S_1,\dots,S_k)\ge M/2, \\
>M/2 & \text{\textit{if}}\text{LCS}(S_1,\dots,S_k)<M/2.
\end{array}\right.\)

_Proof._ Consider first, what’s the length of a target string for \(\delta_{CE}(S_1,\dots,S_k,\gamma)=M/2\). Call this target central string _T_. If |_T|\>M/_2 then the distance from \(\gamma\) to _T_ is greater than _M/_2. If |_T|\<M/_2 then the strings _S<sub>i</sub>_ must have more than _M/_2 deletions, giving a distance greater than _M/_2. So, to hit _M/_2 the target string must have length _M/_2 exactly.

Next note that for the empty string to reach length _M/_2 it must simply have _M/_2 insertions. For any of the _S<sub>i</sub>_ strings to go down to _M/_2 they must simply have _M/_2 deletions.

Note that LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>_) is defined as _M_ minus the number of deletions needed in each string to reach the minimal target. Thus, with this addition of an empty string

\(\delta_{CE}(S_1,\dots,S_k,\gamma)\left\{\begin{array}{ c c }
=M/2 & \text{if}\text{LCS}(S_1,\dots,S_k)\ge M/2 \\
>M/2 & \text{if}\text{LCS}(S_1,\dots,S_k)<M/2
\end{array}\right..\)

