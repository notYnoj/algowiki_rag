**Theorem 5.** _Given strings T_<sub>1</sub> _and T_<sub>2</sub> _with_ \(|T_1|\le|T_2|\) _over a linearly sortable alphabet, and integer f, the problem SegLCS can be solved in_ \(O(f|T_2|(|T_1|-\ell+1))\) _time using_ \(O(\ell(|T_1|-\frac{\ell}{f}+1))\) _space, where_ \(\ell=\mathsf{slcs}(T_1,T_2,f)\).

The basic idea of our algorithm is to combine the ideas from Banerjee et al.’s algorithm \[1\] for the SegLCS problem and the method of Nakatsu et al. \[15\] for the (standard) LCS problem. Banerjee et al. \[1\] considered a function<sup>3</sup> _C_ such that _C(i,j,h_)=slcs(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\]_,h_) for \(1\le i\le n_1\), \(1\le j\le n_2\), and \(1\le h\le f\). They showed that _C_ can be computed by the following recurrence:

\(C(i,j,h)=max\{C(i,j-1,h),C(i-1,j,h),Z\},\)

where _Z=x+C(i-x,j-x,h_-1) and _x_=lcsuf(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\]). This recurrence provides an _O(fn_<sub>1</sub>_n_<sub>2</sub>)-time algorithm since lcsuf(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\]) can be computed in _O_(1) time after _O(n_<sub>1</sub>+_n_<sub>2</sub>)- time preprocessing by using a _lowest common ancestor_ query \[10\] on the _suffix tree_ \[19, 5\] of the reversal of _T_<sub>1</sub>_T_<sub>2</sub>. We further speed up the solution by combining Nakatsu et al.’s method.

Our algorithm maintains a three-dimensional table. Let _L(i,s,h_) be the length _j_ of the shortest prefix _T_<sub>2</sub>\[1_..j_\] of _T_<sub>2</sub> satisfying slcs(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\]_,h_)=_s_. If there are no such prefixes, let \(L(i,s,h)=\infty\). Then, we have

\(\mathsf{slcs}(T_1,T_2,f)=max\{s|L(i,s,f)\neq\infty\text{for some}i\}.\)

Our goal is to compute the table _L_ by dynamic programming, but as we will see later, we do not have to completely fill the table to obtain the value slcs(_T_<sub>1</sub>_,T_<sub>2</sub>_,f_).

We have the following inequalities by definition.

\(L(i,s,h)\le L(i-1,s,h)\) (1)

\(L(i,s,h)>L(i-1,s-1,h)\) (2)

Also, we obtain the following lemmas.

**Lemma 2.** _For any i,j,s, and h, if_ \(j\ge L(i-x,s-x,h-1)+x\) _holds where x_=lcsuf(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\])_, then_ \(L(i,s,h)\le j\) _holds._

_Proof._ Since \(j-x\ge L(i-x,s-x,h-1)\), _T_<sub>1</sub>\[1_..i-x_\] and _T_<sub>2</sub>\[1_..j-x_\] have (_h_-1)-SegCS of length _s-x_. Thus, _T_<sub>1</sub>\[1_..i_\] and _T_<sub>2</sub>\[1_..j_\] have _h_-SegCS of length _s_ since _x_=lcsuf(_T_<sub>1</sub>\[1_..i_\]_,T_<sub>2</sub>\[1_..j_\]). Therefore, \(L(i,s,h)\le j\) holds.

The next lemma states that, intuitively, a right-aligned embedding of a string into _S_ and _T_ can be transformed into another embedding while maximizing the length of the rightmost segment without increasing the segmentation size.

**Lemma 3.** _Suppose p_=(_u_<sub>1</sub>_,...,u<sub>h</sub>_) _is an h-segmentation of a string of length s_=|_u_<sub>1</sub>_...u<sub>h</sub>_| _such that p can be embedded to both of S and T and the last segment u<sub>h</sub> is a common suffix of S and T. Then, there is an h-segmentation_ \(p'=(u'_1,\dots,u'_h)\) _of a string of length s that can be embedded to both S and T such that_ \(|u'_h|=min\{\mathsf{lcsuf}(S,T),s\}\).

_Proof._ Let \(\ell=\mathsf{lcsuf}(S,T)\). If \(\ell\ge s\), then the _h_-segmentation \((\varepsilon,\dots,\varepsilon,S[|S|-s+1,|S|])\) of _S_\[|_S_|-_s_+1,|_S_|\]=_T_\[|_T_|-_s_+1.|_T_|\] has the desired property. If \(\ell<s\), let _j_ be the integer such that |_u_<sub>1</sub>_...u_<sub>_j_-1</sub>|_\<s_-\(\ell\le|u_1\dots u_j|\). Such _j_ always exists. Also, _j\<h_ holds since \(|u_h|\le\ell\). Let _v_ be the prefix of _u<sub>j</sub>_ such that \(|u_1\dots u_{j-1}v|=s-\ell\). Let \(u'_h=S[|S|-\ell+1,|S|]\). Then, the sequence of _h_ segments \((u_1,\dots,u_{j-1},v,\varepsilon,\dots,\varepsilon,u'_h)\) has the desired property.

<sup>3</sup>We remark that the definition of _C_ here is not strictly the same as the corresponding function CHAIN from \[1\] as _C_ focuses on prefixes of _T_<sub>1</sub> and _T_<sub>2</sub> while CHAIN focuses on suffixes of them.

