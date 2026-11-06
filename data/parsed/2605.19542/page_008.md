<tbc>_Proof._ Without loss of generality, we can assume that |_A_|=1. If |_B_|=1, then the desired inequality holds trivially (although it is possible that \(A\dot{+}B=\emptyset\)). Now we consider the case \(|B|\ge 2\). We write _A_={_a_<sub>0</sub>} and |_B_|=_k_. We can find _k_-1 distinct elements _b_<sub>1</sub>_,...,b_<sub>_k_-1</sub> in _B_ such that \(b_i\neq a_0\) for \(1\le i\le k-1\).

Note that \(a_0+b_1,\dots,a_0+b_{k-1}\in A\dot{+}B\). Thus, \(|A\dot{+}B|\ge k-1=|A|+|B|-2=min\{p,|A|+|B|-2\}\). The proof of this lemma is finished.

□

Now we are able to prove the Main Theorem. If \(|A|+|B|-2\ge p+1\), we claim that there exist nonempty subsets \(A'\subset A\) and \(B'\subset B\) such that \(|A'|+|B'|-2=p\) and \(|A'|\neq|B'|\).

Suppose that |_A_|+|_B_|-2=_p+d_ with \(d\ge 1\). We write \(d_1=\lfloor d/2\rfloor\) and \(d_2=\lceil d/2\rceil\). Clearly, _d_<sub>1</sub>+_d_<sub>2</sub>=_d_. Without loss of generality, we assume that |_A|\<|B_|. We choose _d_<sub>2</sub> elements \(a'_1,\dots,a'_{d_2}\) in _A_ and _d_<sub>1</sub> elements \(b'_1,\dots,b'_{d_1}\) in _B_. Let \(A'=A\backslash\{a'_1,\dots,a'_{d_2}\}\) and \(B'=B\backslash\{b'_1,\dots,b'_{d_1}\}\). From \(|A|+|B|-2=p+d\), we can see that \(|A|\ge d+2\ge d_2+2\). Thus, \(A'\) is nonempty and \(|A'|=|A|-d_2\). Similarly, \(B'\) is nonempty and \(|B'|=|B|-d_1\). We have \(|A'|<|B'|\) since |_A|\<|B_| and \(d_2\ge d_1\). It is easy to check that \(|A'|+|B'|-2=|A|-d_2+|B|-d_1-2=|A|+|B|-2-d=p\). Therefore, the above claim is true.

Now it suffices to prove the Main Theorem in the case \(|A|+|B|-2\le p\), since if \(|A|+|B|-2\ge p+1\) then \(|A\dot{+}B|\ge|A'\dot{+}B'|\ge min\{p,|A'|+|B'|-2\}=p=min\{p,|A|+|B|-2\}\).

From now on, we assume that \(|A|+|B|-2\le p\). Let _A_={_a_<sub>1</sub>_,...,a<sub>m</sub>_} and _B_={_b_<sub>1</sub>_,...,b<sub>k</sub>_}. We have \(m+k\le p+2\). In view of Lemma 4.3, we can assume that \(m\ge 2\) and \(k\ge 2\). Let _C=A_\(\dot{+}B=\{c_1,\dots,c_t\}\). By Lemma 2.2, there exists a nonzero sequence _w_<sub>1</sub>(_a_<sub>1</sub>)_,...,w_<sub>1</sub>(_a<sub>m</sub>_) such that

\(e_A(w_1)=|A|-1=m-1.\) (4.7)

Also, there exists a nonzero sequence _w_<sub>2</sub>(_b_<sub>1</sub>)_,...,w_<sub>2</sub>(_b<sub>k</sub>_) such that

\(e_B(w_2)=|B|-1=k-1.\) (4.8)

Recalling the definitions of \(\alpha_i:=\alpha_i(A,w_1)\) and \(\beta_i:=\beta_i(B,w_2)\), we conclude from (4.7) and (4.8) that \(\alpha_i=0\) for \(0\le i\le m-2\), \(\alpha_{m-1}\neq 0\), \(\beta_i=0\) for \(0\le i\le k-2\) and \(\beta_{k-1}\neq 0\).

Applying Lemma 4.2 with _r=m_-2 and _s=k_-2, we obtain

\(\gamma_{m+k-3}=\big(C_{m+k-3}^{m-2}-C_{m+k-3}^{k-2}\big)\alpha_{m-1}\beta_{k-1}.\)

