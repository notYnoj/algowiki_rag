When extracting a subsequence scanning _T_ from left to right, instead of keeping track of the segmentation number _h_, we memorize the score of a factorization that yields the subsequence. Once the score of a factorization of a prefix of _T_ reaches |_T_|-2_f_, any subsequence of the suffix may follow, so we do not have to compute the exact score any further. When the segmentation constraint _f_ is close to |_T|/_2, the upper bound |_T_|-2_f_ will be close to zero.

We remark that when the last segment is a suffix of _T_, i.e., \(T=v_0u_1\cdots v_{h-1}u_h\), we have \(\mathcal{S}(v_0,u_1,\dots,v_{h-1},u_h)=|T|-2h+1\). This appears that we need a higher score than the previous case, where the factorization ends with _v<sub>h</sub>_. But one also notices that, in this case, the score and the text length always have opposite parities. Therefore, if \(\mathcal{S}(v_0,u_1,\dots,v_{h-1},u_h)\ge|T|-2f\), then \(\mathcal{S}(v_0,u_1,\dots,v_{h-1},u_h)\ge|T|-2f+1\). Hence, we can use the same score threshold |_T_|-2_f_ for a factorization ending with the last segment _u<sub>h</sub>_ to judge whether the yielded subsequence is _f_-segmental.

Define<tbc>

\(\overline{SubSeq_{\ge\ell}}(T)=\{u_1\cdots u_h|T=v_0u_1\cdots v_{h-1}u_hv_h\text{for some}v_0\in\Sigma^*\text{and}u_1,v_1,\dots,u_h,v_h\in\Sigma^+\text{with}\mathcal{S}(v_0,u_1,\dots,u_h,v_h)\ge\ell\},\overline{SubSeq_{\ge\ell}}(T)=\{u_1\cdots u_h|T=v_0u_1\cdots v_{h-1}u_h\text{for some}v_0\in\Sigma^*\text{and}u_1,v_1,\dots,u_h\in\Sigma^+\text{with}\mathcal{S}(v_0,u_1,\dots,v_{h-1},u_h)\ge\ell\}.\)

<tbc>We remark that we disallow _u<sub>i</sub>_ and _v<sub>i</sub>_ with _i\>_0 to be empty in the definition above, differently from \(SubSeq^{\le h}\) and \(SufSeq^{\le h}\). In this way, the scores are always non-negative.

Depending on whether _f<sub>a</sub>_ is small or large, we use different types of dynamic programming tables. For \(X_1,X_2\in\{\mathrm{B},\mathrm{F},\overline{\mathrm{B}},\overline{\mathrm{F}}\}\), we consider the tables _L_<sub>_X_<sub>1</sub>_X_<sub>2</sub></sub>, which shall satisfy<tbc>

\(L_{X_1X_2}[i_1,i_2,p_1,p_2]=\mathrm{mxl}\big(S_1(T_1[1..i_1])\cap S_2(T_2[1..i_2])\big)\) (3)

<tbc>where

\(S_a=\left\{\begin{array}{ c c }
SubSeq^{\le p_a} & \text{if}X_a=\mathrm{B}, \\
\overline{SubSeq^{\le p_a}} & \text{if}X_a=\mathrm{F}, \\
\overline{SubSeq_{\ge p_a}} & \text{if}X_a=\overline{\mathrm{B}}, \\
\overline{SufSeq_{\ge p_a}} & \text{if}X_a=\overline{\mathrm{F}}
\end{array}\right.\)

for _a_=1,2. If _f<sub>a</sub>_ is small, say \(f_a\le n_a/4\), we are interested only in \(X_a\in\{\mathrm{B},\mathrm{F}\}\) with \(0\le i_a\le n_a\) and \(0\le p_a\le f_a\); if _f<sub>a</sub>_ is large, say _f<sub>a</sub>\>n<sub>a</sub>/_4, we are interested only in \(X_a\in\{\overline{\mathrm{B}},\overline{\mathrm{F}}\}\) with \(0\le i_a\le n_a\) and \(0\le p_a\le\mathrm{max}\{0,n_a-2f_a\}\). For example, if _f_<sub>1</sub> is small and _f_<sub>2</sub> is large, then we construct the four tables _L_<sub>B<o>B</o></sub>, _L_<sub>B<o>F</o></sub>, _L_<sub>F<o>B</o></sub>, _L_<sub>F<o>F</o></sub>. The answer will be found as the maximum of the (_n_<sub>1</sub>_,n_<sub>2</sub>_,f_<sub>1</sub>,max{0_,n_<sub>2</sub>-2_f_<sub>2</sub>})-entries of those tables. Hereafter, let _g<sub>a</sub>=f<sub>a</sub>_ if _f<sub>a</sub>_ is small, and _g<sub>a</sub>_=max{0_,n<sub>a</sub>_-2_f<sub>a</sub>_} if _f<sub>a</sub>_ is large. It remains to explain how to initialize and update those tables.

## Initialization.

For _i_<sub>1</sub>=0 or _i_<sub>2</sub>=0, let _L_<sub>_X_<sub>1</sub>_X_<sub>2</sub></sub>\[_i_<sub>1</sub>_,i_<sub>2</sub>_,p_<sub>1</sub>_,p_<sub>2</sub>\]=min{_q_<sub>1</sub>_,q_<sub>2</sub>} where<tbc>

\(q_a=\left\{\begin{array}{ c c }
0 & \text{if}X_a=\mathrm{B}\text{or}X_a=\mathrm{F}\wedge p_a>0\text{or}X_a=\overline{\mathrm{B}}\wedge p_a\le i_a, \\
-\infty & \text{otherwise}
\end{array}\right.\)

<tbc>for _a_=1,2. This is justified by the fact that for any \(p\ge 0\),

\(\lambda\in SubSeq^{\le p}(\lambda)\cap SufSeq^{\le 1+p}(\lambda)\cap\overline{SubSeq_{\ge p}}(T[1..p]),\)<br>
\(\lambda\notin SufSeq^{\le 0}(\lambda)\cup\overline{SufSeq_{\ge p}}(\lambda)\cup\overline{SubSeq_{\ge 1+p}}(T[1..p]).\)

