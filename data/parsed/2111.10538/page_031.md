## 3.2.2 Implementation of lcs-cmp

The goal of this section is to design a data-structure that will be used in our subquadratic time algorithm for LCS. The data structure receives a window _w<sub>a</sub>_, a threshold \(\widetilde{\lambda}\), and a set _S_ of windows _w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>s</sub>_. (To avoid confusing, one can assume _a_=0 and _w<sub>a</sub>=w_<sub>0</sub> but we refer to this special window by _w<sub>a</sub>_ to be consistent with the previous sections.) All the windows _w<sub>a</sub>,w_<sub>1</sub>_,w_<sub>2</sub>_,...,w<sub>s</sub>_ have equal sizes. We present an _O(s|w<sub>a</sub>_|<sup>2</sup>log_n_) time preprocessing algorithm and an _O_(|_w<sub>a</sub>_|) time query algorithm for lcs-cmp such that for any \(i,j\in[s]\)

1. if \(\|\mathsf{lcs}_{w_a}(w_i,w_j)\|\ge\widetilde{\lambda}\), then the query algorithm outputs accept;<tbc>

2. if \(\|\mathsf{lcs}_{w_a}(w_i,w_j)\|<\widetilde{\lambda}^2/4\), then the query algorithm outputs reject.

We bring the high level idea in the following (see also Algorithm 3 for pseudocode). We first compute opt_<sub>a,i</sub>_ for every \(i\in[s]\). Next, for each window _w<sub>i</sub>_, we find a set of at most \(2/\widetilde{\lambda}\) common subsequences between _w<sub>a</sub>_ and _w<sub>i</sub>_. Let us put the corresponding indices in the _w<sub>a</sub>_ side of all such common subsequences in a set _Y<sub>a,i</sub>_ for each window _w<sub>i</sub>_. Our algorithm maintains the property that if we remove all characters corresponding to _Y<sub>a,i</sub>_ from _w<sub>a</sub>_, the LCS of the remainder with _w<sub>i</sub>_ is smaller than \(\frac{|w_a|\widetilde{\lambda}}{2}\) . For each pair \(w_i,w_j\in S\), if \(\mathsf{LCS}_{w_a}(w_i,w_j)\ge|w_a|\widetilde{\lambda}\) then at least half of the characters that contribute to such a solution lie in _Y<sub>a,j</sub>_. Thus, the intersection of at least one common subsequence in _Y<sub>a,j</sub>_ and opt_<sub>a,i</sub>_ should have size \(\frac{|w_a|\widetilde{\lambda}}{2}/(2/\widetilde{\lambda})=|w_a|\widetilde{\lambda}^2/4\).

In what follows, we discuss the details.

**Lemma 3.22** (Initial)**.** _Given a parameter_ \(\widetilde{\lambda}\)_, a window w<sub>a</sub>, and a set of windows_ \(w_1,\cdots,w_s\)_, the_ Initial _procedure of data structure_ lcs-cmp _(Algorithm 3) takes O(s|w<sub>a</sub>_|<sup>2</sup>log_n_) _time, and outputs_ \(\{\mathsf{opt}_{a,i}\}_{i\in[s]}\) _and_ \(\{Y_{a,i}\}_{i\in[s]}\) _such that the following hold._

1. opt_<sub>a,i</sub> corresponds to the w<sub>a</sub> side indices of a fixed longest common subsequence between w<sub>a</sub> and w<sub>i</sub> for every_ \(i\in[s]\).<tbc>

2. _Y<sub>a,i</sub> corresponds to the w<sub>a</sub> side indices of at most_ \(2/\widetilde{\lambda}\) _common subsequence between w<sub>a</sub> and w<sub>i</sub> for every_ \(i\in[s]\).<tbc>

_3. For any common subsequence between w<sub>a</sub> and w<sub>i</sub>, if none of its w<sub>a</sub> side indices are in Y<sub>a,i</sub>, then the length of this common subsequence is less than_ \(\widetilde{\lambda}|w_a|/2\).

_Proof._ In order to construct set _Y<sub>a,i</sub>_ for each window _w<sub>i</sub>_ we run the following algorithm: We start by setting _Y<sub>a,i</sub>_ to an empty set. Next, we set \(w'_a=w_a\) and iteratively compute the LCS of \(w'_a\) and _w<sub>i</sub>_. Each time we find a solution, we compare its size to \(\widetilde{\lambda}|w_a|/2\). If the solution size is smaller, we terminate the algorithm. Otherwise, we add the original positions of the common subsequence in _w<sub>a</sub>_ to set _Y<sub>a,i</sub>_ and continue by removing these characters from \(w'_a\). We stop when the solution size drops below \(\widetilde{\lambda}|w_a|/2\). It immediately follows that since each time the size of _Y<sub>a,i</sub>_ is increased by at least \(\widetilde{\lambda}|w_a|/2\) then we repeat this procedure at most \(2/\widetilde{\lambda}\) times.

To bound the runtime, we state the following fact: when the size of the LCS between a string _Q_ and a string _R_ is bounded by \(\ell\), one can preprocess one of the strings (_R_ in this case) in time _O_(|_R_|log_n_) and then compute the LCS in time \(O(|Q|\ell logn)\) (see Theorem A.8). Notice that in order to construct _Y<sub>a,i</sub>_ for a window _w<sub>i</sub>_, the total size of the LCS’s that we find is bounded by |_w<sub>a</sub>_|. Therefore, for a fixed window _w<sub>i</sub>_, if we preprocess _w<sub>i</sub>_ once and use it for all computations, the total runtime is bounded by

\(O(|w_a||Y_{a,i}|logn+|w_i|logn)=O(|w_a|^2logn+|w_i|logn).\)

Thus, the total preprocessing time of our algorithm over all windows is _O(s|w<sub>a</sub>_|<sup>2</sup>log_n_).

