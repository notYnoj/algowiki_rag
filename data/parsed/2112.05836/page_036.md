Now we will apply the above Lemma 6.21 and Theorem 6.22 to get a _k_-center edit distance lower bound from SETH.

**Reminder of Theorem 6.4.** _Given an instance of k-center edit distance on strings of lengths_ \(M_1\le M_2\le\cdots\le M_k\) _where these strings can all be compressed into a SLP of size m, then, an algorithm for k-center edit distance that runs in time_ \(((M_2+1)\cdots(M_k+1)\cdot m)^{1-\epsilon}\) _time for constant_ \(\epsilon>0\) _violates SETH._

_Proof._ We will use Theorem 1.1, Lemma 6.21 and Theorem 6.22.

Say we are given an instance of _k_-LCS with strings _S_<sub>1</sub>_,...,S<sub>k</sub>_ of length _M_ and an SLP compression of all strings of size _m_. Determining if the _k_-LCS is some integer _C_ requires (_M_<sup>_k_-1</sup>_m_)<sup>1-_o_(1)</sup> time if SETH is true by Theorem 1.1.

Then Lemma 6.21 simply appends at most _M_ symbols @ or #_<sub>i</sub>_ to each string making a new problem \(S'_1,\dots,S'_k\) of length \(M'\). Note that the size of the compression is now \(m'=m+O(k\mathrm{lg}(M))\). Now determining if the _k_-LCS is \(M'/2\) requires \(\left((M')^{k-1}m'\right)^{1-o(1)}\) if SETH is true.

Now we will apply Theorem 6.22. We can produce an instance of (_k_+1)-center edit distance that has strings \(S'_1,\dots,S'_k,\gamma\) that distinguishes between the _k_-LCS of \(S'_1,\dots,S'_k\) being \(M'/2\) or not. Now note that \(M_i=|S'_i|\) and _M_<sub>_k_+1</sub>=0. So \((M_2+1)\cdots(M_{k+1}+1)=\Theta((M')^{k-1})\). The compression of this empty string means that the new compression has size \(m''=m'+O(1)=m+O(k\mathrm{lg}(M))\).

We can run this a second time where we add two characters to each string: \(S'_i=S_i\%_i\%_i\). These characters are unmatchable. Also, if the LCS used to be at least \(M'/2+1\) it will still be at least half the length of the strings. So, we can distinguish the exact value. Similarly, the compression of these strings is of size at most \(m''+O(k)=m''+O(1)\).

Hence, an algorithm for (_k_+1)-median edit distance that runs in \(((M_2+1)\cdots(M_{k+1}+1)\cdot m)^{1-\epsilon}\) time for constant \(\epsilon>0\) violates SETH.

## 6.9 Edit Distance Lower Bounds from SETH

In this section we show a better lower bound for _k_-edit-distance by reducing from SETH directly. A recent paper has given _M_<sup>_k-o_(1)</sup> lower bounds for Edit Distance from SETH where _M_ is the length of the strings \[HBGT20\]. In this section we show a _M_<sup>_k_-1-_o_(1)</sup>_m_ lower bound for compressed _k_-edit-distance where _m_ is the size of the SLP describing the strings. Our reduction uses the ideas from the SETH lower bound for _k_-edit-distance to achieve this. We will use the same ideas and list structures that we used in the _k_-LCS lower bound. We use many of the same notions of gadgets, however, to distinguish between them, we add _ED_ to the end of the name of the gadgets (for Edit Distance). Note that the structure of this proof mirror almost exactly the _k_-LCS lower bound. However, due to the different distance measures we need to generate different gadgets.

The main takeaway of this section is that in order to build an interleave gadget for edit distance we need to generate a selector gadget that has one value if all values match, and another if not all values match.

The primary difficulty in generalizing this lower bound comes from the variable costs of partial matches. That is, if we have the edit distance of \(\delta_E(a,a,a,a,b)=1\), where as \(\delta_E(a,a,b,b,c)=3\). By contrast, the LCS of both is LCS(_a,a,a,a,b_)=LCS(_a,a,b,b,c_)=0. So, the overall structure needs to account for this in some way. We want to re-create a perfect alignment gadget, but for Edit-Distance. This will give us two results. First we generalize the 2-LCS lower bound into a 2-edit distance lower bound, answering an explicit open problem given by \[ABBK17\].

We will use the pre-existing coordinate gadgets and alignment gadgets from \[HBGT20\]. So, we have two primary tasks. We need to generate and prove the correctness of _perfect_ alignment gadgets. Additionally, we need to analyze the size of the compression of both our gadgets and the \[HBGT20\] gadgets.

## 6.10 Selection Gadgets

We want an additional gadget. A selector gadget. These allow us to say either strings _A_<sub>1</sub>_,...,A<sub>k</sub>_ are compared or strings _B_<sub>1</sub>_,...,B<sub>k</sub>_ are compared but not both. We will use a version that works for single characters.

**Lemma 6.23.** _There exist single character selection gadgets_ \(SCSG_i(\cdot)\) _such that the length is polynomial in k and they add a single character to the alphabet. The k-edit distance of k SCSG<sub>i</sub>(c<sub>i</sub>_) _strings is either_<tbc>

