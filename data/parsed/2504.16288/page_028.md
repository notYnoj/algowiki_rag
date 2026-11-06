define _Z_=$<sup>_d_+1</sup> and define the following two functions that operate on binary vectors:

\(F(v)=\left(\Pi_{j\in[d]:v[j]=0}c_j\right)\$^{d+1}\)<br>
\(G(u)=\left(\Pi_{j\in[d]:u[j]=1}c_j\right)\$^{\|u\|_0}\)

Note that \(Z\unknown_\mathsf{sub}F(v)\) so MinSub(_F(v),Z_)=|_Z_|=_d_+1. Further observe that \(G(u)\unknown_\mathsf{sub}F(v)\Longleftrightarrow v\perp u\) so if \(v\perp u\), we have MinSub(_F(v),G(u_))=|_G(u_)|=_d_.

Consider the regular expression \(Y:=Z\vee G(u_1)\vee G(u_2)\dots\vee G(u_n)\). Then we have:<tbc>

\(\mathsf{MinSub}(F(v),Y)=d+1-\unknown[\exists_{i\in[n]}v\perp u_i]\)

<tbc>Let \(w=\Pi_{i\in[t]}(F(v_i)\#)\) and _R_=(_Y_#)_<sup>t</sup>_. By Claim 7.7, similarly as before, we deduce:

\(\mathsf{MinSub}(w,R)=t(d+2)-|\{i:\exists_{k\in[n]}v_i\perp u_k\}|\)

and hence there exists an orthogonal pair of vectors \((u,v)\in U\times V\) iff MinSub(_w,R)\<t(d_+2).

The rest of the analysis is identical to that of the previous paragraphs. Namely, as |_w_|=_O(td_) and |_R_|=_O(ntd_), this yields an algorithm for UOV in time \(O((nt^2d^2)^{1-\epsilon})=O(n^{(1+2\alpha)(1-\epsilon)}\mathsf{poly}(d))\). Choosing \(\alpha:=\epsilon/2\) we obtain an algorithm for UOV that runs in time \(O(n^{(1+\epsilon)(1-\epsilon)}\mathsf{poly}(d))=O(n^{1+\alpha-(\alpha+\epsilon^2)}\mathsf{poly}(d))\) which violates UOVH.

### Constant-Site Alphabet.

Reducing the alphabet size to a constant is very similar to the case of the max-variant for the supersequence relation. Let \(\Sigma':=\{0,1,\$,\#\}\) and define a function \(\delta\) as before by \(\delta(1):=10\) and \(\delta(0):=0\). We define \(Z':=0^d\$^{d+1}\), \(F'(v):=(\Pi_{j\in[d]}\delta(\neg v[j]))\$^{d+1}\), and \(G'(u):=\left(\Pi_{j\in[d]}\delta(u[j])\right)\$^{\|u\|_0}\). Again \(Z'\unknown_\mathsf{sub}F'(v)\) but now \(\mathsf{MinSub}(F'(v),Z')=|Z'|=2d+1\). Next, \(G'(u)\unknown_\mathsf{sub}F'(v)\Longleftrightarrow v\perp u\), so if \(v\perp u\) we have \(\mathsf{MinSub}(F'(v),G'(u))=|G'(u)|=2d\).

We define \(Y',w'\) and \(R'\) as before, but now using the new expressions \(Z',G'\) and \(F'\). Then, \(\mathsf{MinSub}(F'(v),Y')=2d+1-\unknown[\exists_{i\in[n]}v\perp u_i]\) and finally \(\mathsf{MinSub}(w',R')=t(2d+2)-|\{i:\exists_{k\in[n]}v_i\perp u_k\}|\) so \(\mathsf{MinSub}(w',R')<t(2d+2)\) iff there exists \((u,v)\in U\times V\) such that \(u\perp v\). Further analysis of the reduction and its running time follows as in the case of the max-variant of the supersequence relation, which concludes the proof.

## 8 Conclusion and Future Work

Let us start with a brief summary of the key messages of our results. Firstly, for all our considered relations \(\unknown\), the \(\unknown\)-matching problem and its quantitative variants are in _O_(|_w|m_) - the (conditionally optimal) complexity for conventional regex matching. Hence, this generalises standard regex matching and the longest common subsequence/shortest common supersequence problems. Moreover, as a surprising and unexpected special case, the non-quantitative \(\unknown\)-matching problem for the subsequence and supersequence relation can be solved in linear time _O_(|_w_|+_m_); for all other problems, the running time of _O_(|_w|m_) is optimal in the sense that \(O((|w|m)^{1-\epsilon})\) cannot be achieved for any \(\epsilon>0\) assuming SETH. Finally, the intuitively much more difficult task of checking whether _all_ strings \(u\unknown w\) match the regex, i.e., the universal problem variants, leads to a more diverse picture ranging from cases that can still be solved efficiently (e.g., _O_(|_w|m_) or _O_(|_w_|<sup>2</sup>_m_) for the prefix and infix relation, respectively) to intractable cases.

With respect to the linear time solvable cases of subsequence and supersequence matching, it might be worthwhile to investigate whether our linear time algorithms can be used as components within other useful string matching algorithms. For example, in big data scenarios where quadratic running times are unrealistic, it might be possible to approximate reasonable string analysis tasks by only performing subsequence or supersequence matching. Let us also point out that none of our upper bounds rely on heavy algorithmic machinery or data structures and therefore our asymptotic running times do not hide huge constant factors. Hence, we believe that our algorithms have straightforward and practically relevant implementations (just like the classical state-set simulation does).

