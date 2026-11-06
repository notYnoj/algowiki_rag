**Algorithm 3.1** Basic algorithm for CMM with _f<sub>E</sub>_. Some operations require care to implement efficiently; see the proof of Theorem 3.1.

**Input:** Graph _G_=(_V,E_) with \(V\subseteq\Sigma^*\), integer \(\ell>0\)<br>
**Output:** Motif pair {_X<sup>⋆</sup>,Y<sup>⋆</sup>_} from \(\Sigma^\ell\) maximizing _f<sub>E</sub>_

1: Let \(C:\Sigma^\ell\rightarrow\mathbb{Z}_{\ge 0}\) be indexed using SA ranks<br>
\((X^\star,Y^\star)\leftarrow(\perp,\perp)\)<br>
for each distinct length-\(\ell\) substring _X_ in _V_<br>
   \(V_X\leftarrow\{u\in V|X\text{is a substring of}u\}\)<br>
   for each \(\{u,v\}\in E\) with \(u\in V_X\)<br>
   for each distinct length-\(\ell\) substring _Y_ of v<br>
   if \(X\unknown Y\)<br>
   \(C[Y]\leftarrow C[Y]+1\)<br>
   for each \(\{u,v\}\in E\) with \(u,v\in V_X\)<br>
   for each distinct length-\(\ell\) substring _Y_ of u<br>
   if \(X\unknown Y\) and _Y_ is not a substring of v<br>
   \(C[Y]\leftarrow C[Y]+1\)<br>
   Update {_X<sup>⋆</sup>,Y<sup>⋆</sup>_} if max(_C)\>f<sub>E</sub>(G,{X<sup>⋆</sup>,Y<sup>⋆</sup>_})<br>
   Reset (the touched entries of) _C_<br>
   return {_X<sup>⋆</sup>,Y<sup>⋆</sup>_}

<tbc>labels are relatively short. The latter is natural because in many practical instances, the labels have roughly the same length (thus, relatively short compared to _N_).

_Remark_ 3.3 (Enumeration). Instead of simply optimizing _f<sub>E</sub>_ in Algorithm 3.1, we can build a complete sorted list of all motif pairs and their support value (storing them using ranks). Since the values of the support measure are bounded by \(|E|\le N^2\), we can do this while maintaining the O(_N_<sup>2</sup>) running time using an algorithm like radix sort. Unfortunately, this increases the space complexity to O(_N_<sup>2</sup>) in the worst case. In practice, we are only interested in the top-_k_ motif pairs. These we can maintain with an O(log_k_) multiplicative overhead by keeping a heap with the top-_k_ pairs.

We defer the changes required for \(f_{\chi^2}\) and the SETH lower bounds for both _f<sub>E</sub>_ and \(f_{\chi^2}\) to Appendix A.

## 4 An exact algorithm for \((\ell,d)\)-CMM.

Algorithm 3.1 for CMM (Theorem 3.1) will serve as a basis for our exact algorithm for \((\ell,d)\)-CMM.

The basic premise is simple: iterate over all possible combinations of wildcard positions in the two motifs and then run a modified version of Algorithm 3.1 that ignores the characters at these positions. While this seems easy, achieving it without losing efficiency is somewhat tricky, especially when targeting O(_N_) space. Recall that in Algorithm 3.1, we heavily relied on the rank of every length-\(\ell\) substring in the suffix array (SA) of the concatenated node strings. In particular, we relied on the fact that this rank is a compact representation of<tbc>

<tbc>the substrings. Thus, we were able to compare any two substrings for equality by simply comparing their ranks. With the _d_ wildcards, we need to treat substrings that are actually different as the same, that is, we have a relaxed notion of equality that ignores the wildcarded positions. Defining the right notion of rank and implementing access to it efficiently requires a substantial amount of care. We show the following core lemma.

Lemma 4.1. _Given a set_ \(V\subseteq\Sigma^*\) _of strings of total length N over_ \(\Sigma=\{1,2,\dots,N\}\)_, an integer_ \(\ell\in[1,N]\)_, and a set_ \(H\subseteq[\ell]\) _with_ \(d:=|H|<\ell\)_, we can construct an_ O(_N)-size data structure in_ O((_d_+1)_N_) _time and_ O(_N_) _working space answering the following queries in_ O(1) _time: given_ (_u,i), with_ \(u\in V\) _and_ \(i\in[1,|u|-\ell+1]\)_, return a_ rank _(a unique identifier) of string M of length_ \(\ell\)_, such that, for all_ \(j\in[1,\ell]\):

\(M[j]:=\left\{\begin{array}{ c c }
\diamond & \text{\textit{if}}j\in H, \\
u[i+j-1] & \text{\textit{if}}j\notin H.
\end{array}\right.\)

_In particular, the output rank is an integer from_ \[0_,N)._

_Proof._ Consider Algorithm 4.1. We show that this algorithm solves exactly the claimed task.

Let \(H=\{h_1<\cdots<h_d\}\). Further let \(S_V=v_1\#_1v_2\#_2\dots v_{|V|}\#_{|V|}\) be the concatenation of the input strings with appropriate separators and let _N<sub>V</sub>_:=|_S<sub>V</sub>_|-|_V_|. (We will ignore suffixes of _S<sub>V</sub>_ starting with separators.) In O(_N<sub>V</sub>_) time, we construct the suffix array SA<sub>_S<sub>V</sub>_</sub> \[12\] and the LCP array LCP<sub>_S<sub>V</sub>_</sub> \[13\].

Consider the list of the suffixes of _S<sub>V</sub>_. The characters that occur at the positions _h_<sub>1</sub>_,...,h<sub>d</sub>_ of every suffix are replaced by wildcards to obtain _N<sub>V</sub>_ suffixes each split into (_d_+1) fragments. The above replacements are _implicit_; we never apply them. Moreover, we are interested only in the length-\(\ell\) prefix of each suffix. Some care is needed: if a suffix is shorter than \(\ell\), we ignore it from any further computation; and if a suffix contains a separator #_<sub>i</sub>_ in its length-\(\ell\) prefix, we also ignore it. Using SA<sub>_S<sub>V</sub>_</sub> and starting with the first _N<sub>V</sub>_ substrings (prefixes of suffixes) of length exactly (_h_<sub>1</sub>-1), a new rank is assigned to each of them according to the lexicographical ordering of these substrings; this can be easily derived from a single scan of LCP<sub>_S<sub>V</sub>_</sub> in O(_N<sub>V</sub>_) time. We then proceed to _h_<sub>2</sub> analogously, and so on. To maintain O(_N<sub>V</sub>_) space, for every consecutively considered pair of wildcard positions, we use radix sort over the _N<sub>V</sub>_ pairs of ranks (corresponding to the _N<sub>V</sub>_ suffixes) to obtain a new integer ranking over \[0_,N<sub>V</sub>_), and the process continues. In the end, we have a new lexicographical ordering of the length-\(\ell\) prefixes of suffixes of _S<sub>V</sub>_ that disregards the characters at the _h_<sub>1</sub>- th_,...,h<sub>d</sub>_-th positions. Moreover, for every two successive length-\(\ell\) prefixes in this order, we know whether they<tbc>

