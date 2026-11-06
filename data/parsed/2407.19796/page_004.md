We show the following theorem using Corollary 1.

**Theorem 2.** _Neither SegE nor MinSegE over an alphabet of size three can be solved in_ \(O((|T||P|)^{1-\epsilon})\) _time for any_ \(\epsilon>0\)_, unless SETH fails._

_Proof._ Since MinSegE is an optimization version of SegE, it suffices to show the hardness of SegE. Let _T_ and _P_ be instance strings of Episode Matching over {0,1} with |_T_|=_n_ and \(|P|=m\in\Theta(n)\). Define two strings over {0,1,$} by

\(T'=(\$0)^{2n-2}\$^2T[1]\$^2T[2]\$^2\cdots\$^2T[n]\$^2(0\$)^{2n-2},\)<br>
\(P'=\$^{2n}P\$^{2n}\)

(see Example 1 below). Clearly \(|T'|,|P'|\in\Theta(n)\). By Corollary 1, it is enough to show that _T_ has a factor of length _h_ subsuming _P_ as a subsequence if and only if \(P'\in SubSeq^{\le f}(T')\) where _f_=3_n+m+h_-4.

Suppose \(P\in SubSeq(T[i..j])\) where _j-i_+1=_h_. Then, \(\$^2P\$^2\) is an _m_-segmental subsequence of \(S=\$^2T[i]\$^2\cdots\$^2T[j]\$^2\) in \(T'\), where the first and the last segments have length three and the others consist of single characters. Outside _S_, \(T'\) has _n-h_ occurrences of \(\$^2\), to which one can align \(\$^2\) in the prefix and the suffix \(\$^{2n-2}\) of \(P'\). This gives _n-h_ segments. Each of the remaining (4_n_-4)-2(_n-h_)=2(_n+h_-2) occurrences of \(\$\) in \(P'\) is aligned with those in the prefix (\(\$0\))<sup>2_n_-2</sup> and the suffix (0\(\$\))<sup>2_n_-2</sup> of \(T'\). In total, we have \(P'\in SubSeq^{\le f}(T')\) for \(f=m+(n-h)+2(n+h-2)=3n+m+h-4\).

Suppose \(P'\in SubSeq^{\le f}(T')\). Since _P_ is preceded by 2_n_ occurrences of \(\$\) in \(P'\), _P_\[1\] cannot be aligned to any occurrence of 0 in the prefix (\(\$0\))<sup>2_n_-2</sup> of \(T'\), which has only 2_n_-2 occurrences of \(\$\). Similarly _P_\[_m_\] cannot be aligned to any 0 in the suffix (0\(\$\))<sup>2_n_-2</sup> of \(T'\). So, there must be _i_ and _j_ such that _P_\[1\] and _P_\[_m_\] are aligned at _T_\[_i_\] and _T_\[_j_\], respectively. Obviously, \(P\in SubSeq(T[i..j])\). That is, _T_ has a factor of length _j-i_+1 that subsumes _P_ as a subsequence. Here, we require _m_ segments to align _P_ with \(T[i]\$^2\cdots\$^2T[j]\) in \(T'\). Let us consider how \(\$\)’s in \(P'\) can be aligned with \(T'\). They cannot be aligned with any of the occurrences of \(\$^2\) between _T_\[_i_\] and _T_\[_j_\]. The occurrence of \(\$^2\) immediately before and after _P_ can be put into the segments of _P_\[1\] and _P_\[_m_\], respectively. This does not require additional segments. Now \(T'\) has _n-j+i_-1 occurrences of \(\$^2\). To make the segmentation number as low as possible, we must make each segment as long as possible. Thus, we should align as many occurrences of \(\$\) in \(P'\) as possible with those _n-j+i_-1 occurrences of \(\$^2\), which gives _n-j+i_-1 segments, and this leaves 4_n_-4-2(_n-j+i_-1) occurrences of \(\$\) in \(P'\). Those remaining occurrences each will constitute single segments. Thus, in total, we have _m_+4_n_-4-(_n-j+i_-1)=_m_+3_n+j-i_-3 segments at minimum. Since this number is at most _f_=3_n+m+h_-4, the length of _T_\[_i..j_\] is bounded by \(j-i+1\le f-(m+3n-4)=h\).

**Example 1.** _Consider T_=0101 _of length n_=4 _and P_=00 _of length m_=2_, where P is a subsequence of the factor T_\[1..3\] _of length h_=3 _of T. The proof of Theorem 2 constructs_

\(T'=(\$0)^6\$\$0\$\$1\$\$0\$\$1\$\$(0\$)^6,\)<br>
\(P'=\$^800\$^8.\)

_which can be aligned as_

