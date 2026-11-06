Item 2 of Definition 3.8 for entry _q_\[_z<sup>⋆</sup>_\] and the _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((\widetilde{A}',\widetilde{B}')\), and hence contradicts the assumption that _q_\[\] (with hints _S_<sup>+</sup>\[\]_,S_<sup>-</sup>\[\]) is a hinted-\((J_{\le j-1}^+\cup J_{\le j-1}^-)\)-optimal DP table.

This finishes the proof that \(r[\hat{i}]=q[z'']+\sum_{w\in\mathcal{W}_1}Q_w(y_w)\), meaning that _r_\[-_L<sub>j</sub>..L<sub>j</sub>_\] is indeed an \((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal DP table.

For the rest of the proof, without loss of generality we assume \((x[\hat{i}],z[\hat{i}])=(y,z'')\) (since we could have started the proof with the _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\) which would produce a **_y_** that coincides with \(x[\hat{i}]\)).

## New hints for hinted-optimality.

Now we describe how to compute new hint arrays _T_<sup>+</sup>\[-_L<sub>j</sub>..L<sub>j</sub>_\], _T_<sup>-</sup>\[-_L<sub>j</sub>..L<sub>j</sub>_\] to annotate to the DP table _r_\[-_L<sub>j</sub>..L<sub>j</sub>_\].

We will crucially use Item 3 of Lemma 3.7, which states that for every _I_<sub>W<sub>1</sub></sub>-optimal partial solution \((A',B')\),

\(|\{w\in\mathcal{W}_1:I_{\{w\}}\cap J_j^+\subseteq A'\text{and}I_{\{w\}}\cap J_{j+1}^+\neq\varnothing\}|\le b_{j+1}.\) (18)

Given the solutions (**_x_**\[_i_\]_,z_\[_i_\]) returned by Theorem 3.11 (where each **_x_**\[_i_\] encodes an item subset of \(J_j^+\)), we do the following for every \(-L_j\le i\le L_j\):

• Define hints<tbc>

\(T^-[i]:=S^-\big[z[i]\big],\)<br>
\(T^+[i]:=\{w\in\mathcal{W}_1:|I_{\{w\}}\cap J_j^+|=x[i]_w\text{and}I_{\{w\}}\cap J_{j+1}^+\neq\varnothing\}.\)

• If |_T_<sup>+</sup>\[_i_\]|_\>b_<sub>_j_+1</sub>, then we remove entry _r_\[_i_\] from the DP table by setting \(r[i]=-\infty\), and leave _T_<sup>-</sup>\[_i_\]_,T_<sup>+</sup>\[_i_\] undefined.

This clearly satisfies the requirement of hint size: the positive hint size is \(|T^+[i]|\le b_{j+1}\), and the negative hint size is \(|T^-[i]|=\big|S^-\big[z[i]\big]\big|\le b_j\). From Eq. (18), we also know that we did not remove the entry \(r[\hat{i}]\) corresponding to our \((J_{\le j}^+\cup J_{\le j-1}^-)\)-optimal solution \((\widehat{A}'',B'')\) defined earlier (this is because \(|I_{\{w\}}\cap J_j^+|=x[\hat{i}]_w=y_w\) would imply \(I_{\{w\}}\cap J_j^+\subseteq Y\subseteq A'\)).

Finally we show that \(T^+[\hat{i}]\) and \(T^-[\hat{i}]\) satisfy Item 2 of Definition 3.8 for the DP table entry \(r[\hat{i}]\). Suppose for contradiction that there is an _I_<sub>W<sub>1</sub></sub>-optimal partial solution (_A_<sup>∗</sup>_,B_<sup>∗</sup>) whose restriction \((\widehat{A}^{**},B^{**})\) where \(\widehat{A}^{**}:=A^*\cap J_{\le j}^+,B^{**}:=B^*\cap J_{\le j-1}^-\) has weight \(W(\widehat{A}^{**})-W(B^{**})=\hat{i}\), such that either \(A^*\backslash J_{\le j}^+\unknown\subseteq I_{T^+[\hat{i}]}\) or \(B^*\backslash J_{\le j-1}^-\unknown\subseteq I_{T^-[\hat{i}]}\). Recall that \((A''\cup Y,B'')\) (where \(A''\subseteq J_{\le j-1}^+,Y\subseteq J_j^+,B''\subseteq J_{\le j-1}^-\)) has the same weight \(\hat{i}\) and profit \(r[\hat{i}]\) as \((\widehat{A}^{**},B^{**})\) does, so

\((\widetilde{A}^*,\widetilde{B}^*):=\big((A''\cup Y)\cup(A^*\backslash\widehat{A}^{**}),B''\cup(B^*\backslash B^{**})\big)\) (19)

is also an _I_<sub>W<sub>1</sub></sub>-optimal partial solution with the same weight and profit as (_A_<sup>∗</sup>_,B_<sup>∗</sup>). Now consider two cases:

• Case \(A^*\backslash J_{\le j}^+\unknown\subseteq I_{T^+[\hat{i}]}\):<tbc>

<tbc>Let \(a\in A^*\backslash J_{\le j}^+\) and \(a\notin I_{T^+[\hat{i}]}\). By \(a\notin I_{T^+[\hat{i}]}\) and the definition of \(T^+[\hat{i}]\), we know either \(|I_{\{w_a\}}\cap J_j^+|>x[\hat{i}]_{w_a}\) or \(I_{\{w_a\}}\cap J_{j+1}^+=\varnothing\). The latter is impossible given the existence of<tbc>

