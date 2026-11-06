More formally: Recall that \(\delta_E(S_i,S')\) denotes the edit distance of _S<sub>i</sub>_ and \(S'\). Recall that the _k_-median distance is:

\(\delta_E(S_1,S_2,\dots,S_k)=min_{S^\prime\in\text{All Strings}}\left(\sum_{i=[1,k]}\delta_E(S_i,S')\right).\)

We can use inspiration from \[NR05\] to get lower bounds for the center version of this problem as well. Let us remind the definition of _k_-center edit distance problem.

**Definition 6.18.** Given _k_ strings _S_<sub>1</sub>_,...,S<sub>k</sub>_ of lengths _M_<sub>1</sub>_,M_<sub>2</sub>_,...,M<sub>k</sub>_. We define the _k_-center edit distance of those strings is the minimum of the maximum of the distances of those strings to a string \(S'\). The allowed edits are deleting a character, adding a character and replacing a character (Levenshtein distance).

More formally: Let \(\delta_E(S_i,S')\) be the edit distance of _S<sub>i</sub>_ and \(S'\). Now the _k_-center distance is:

\(\delta_{CE}(S_1,S_2,\dots,S_k)=min_{S^\prime\in\text{All Strings}}\left(max_{i=[1,k]}\delta_E(S_i,S')\right).\)

## 6.7 Median Edit Distance

**Theorem 6.19.** _We are given a k-LCS instance with strings S_<sub>1</sub>_,...,S<sub>k</sub> all of length M. Let the k-LCS of these strings be denoted by_ LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>). The_ (2_k_-1)_-median edit distance on S_<sub>1</sub> _through S<sub>k</sub> and k_-1 _copies of the empty string_ \(\gamma\) _is related to the k-LCS of S_<sub>1</sub> _through S<sub>k</sub>:_

\(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)=Mk-\text{LCS}(S_1,\dots,S_k).\)

_Proof._ First, let us prove that \(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)\le Mk-\text{LCS}(S_1,\dots,S_k)\). Let _T_ be the target string of LCS(_S_<sub>1</sub>_,...,S<sub>k</sub>_)=|_T_|. Then, the sum of edit distances to _T_ is _k(n_-|_T_|)+(_k_-1)|_T_|=_kn_-|_T_|.

Second, let us prove that \(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)\ge Mk-\text{LCS}(S_1,\dots,S_k)\). Let \(T'\) be a target string. Now let _d<sub>j</sub>,i<sub>j</sub>,b<sub>j</sub>_ be the number of deletions, insertions and substitutions to go from _S<sub>j</sub>_ to \(T'\). Let _e<sub>j</sub>=d<sub>j</sub>+i<sub>j</sub>+b<sub>j</sub>_ be the edit distance of _S<sub>j</sub>_ to \(T'\). Now note that \(e_j\ge M-|T|+2i_j+b_j\). Additionally, note that the distance from \(\gamma\) to \(T'\) is \(|T'|\). So the total distance is<tbc>

\(kM-k|T'|+\sum_{j=1}^k2i_j+b_j+(k-1)|T'|=kM-|T'|+\sum_{j=1}^k2i_j+b_j.\)

<tbc>So, \(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)\) can only be less if \(|T'|>|T|\). Note, that \(\sum_{j=1}^k2i_j+b_j\ge|T'|-|T|\). The target _T_ is the longest string to be achieved with only deletions. Any change from this _T_ (notably added characters) must involve at least one substitution or an insertion. So we can say that the total distance is

\(kM-|T'|+\sum_{j=1}^k2i_j+b_j\ge kM-|T'|+|T'|-|T|=kM-|T|.\)

So, \(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)\ge Mk-\text{LCS}(S_1,\dots,S_k)\).

Thus, \(\delta_E(S_1,\dots,S_k,\gamma,\dots,\gamma)=Mk-\text{LCS}(S_1,\dots,S_k)\).

Now that we have a tight relationship between the edit distance and LCS, we can use this to get a lower bound from SETH through LCS.

**Theorem 6.20.** _Given an instance of k-median edit distance on strings of lengths_ \(M_1\le M_2\le\cdots\le M_k\) _where these strings can all be compressed into a SLP of size m. Then, an algorithm for k-median edit distance that runs in_ \(\left((M_2+1)\cdots(M_{2k-1}+1)\cdot m\right)^{1-\epsilon}\) _time for constant_ \(\epsilon>0\) _violates SETH._

_Proof._ We will use Theorem 1.1 and Theorem 6.19.

Say we are given an instance of _k_-LCS with strings _S_<sub>1</sub>_,...,S<sub>k</sub>_ of length _M_ and a SLP compression of all strings of size _m_. Then, by Theorem 6.19 we can solve this with an instance of (2_k_-1)-median edit distance on _k_ strings \(S_1,\dots,S_k,\gamma,\dots,\gamma\). We can compress these _k_ strings with a compression of size \(m'=m+O(k)\) (we need only compress the empty string in addition).

_k_-LCS requires (_M_<sup>_k_-1</sup>_m_)<sup>1-_o_(1)</sup> if SETH is true. Note that for our chosen strings \(M^{k-1}=M_2\cdots M_k\). Now note that our compression is of size \(m'=O(m)\). The reduction takes constant time (simply append the empty string and make a call to _k_-median edit distance). So _k_-median edit distance requires \(((M_2+1)\cdots(M_{2k-1}+1)\cdot m)^{1-o(1)}\) time if SETH is true. We can re-state this as an algorithm running time \(((M_2+1)\cdots(M_{2k-1}+1)\cdot m)^{1-\epsilon}\) time for constant \(\epsilon>0\) violates SETH.

