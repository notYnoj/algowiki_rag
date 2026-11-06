We henceforth assume that \(\tau<|X|\). The grammar **G**<sup>+</sup> is constructed by adding new non-terminals to **G**. As for **G**_<sup>P</sup>_, we include as terminals all symbols _A_ of **G**<sup>+</sup> with \(|A|\le\tau\), and we add further symbols as non-terminals. For every symbol _A_ of **G** with \(|A|>\tau\), we introduce three new non-terminals:

• _L(A_) and _R(A_) to **G**<sup>+</sup>, satisfying \(|L(A)|\le\tau\) and \(|R(A)|\le\tau\),<tbc>

• _M(A_) to **G**_<sup>P</sup>_.

The productions for _L(A_), _R(A_), and _M(A_) are determined based on the production \(A\rightarrow B_LB_R\):

1. If \(|B_L|\le\tau\) and \(|B_R|\le\tau\), then \(M(A)\rightarrow\gamma\), \(L(A)\rightarrow B_L\), and \(R(A)\rightarrow B_R\).<tbc>

2. If \(|B_L|>\tau\) and \(|B_R|>\tau\), then \(M(A)\rightarrow M(B_L)R(B_L)L(B_R)M(B_R)\), \(L(A)\rightarrow L(B_L)\), and \(R(A)\rightarrow R(B_R)\).<tbc>

3. If \(|B_L|>\tau\) and \(|B_R|\le\tau\), then \(L(A)\rightarrow L(B_L)\) and:<tbc>

(a) \(R(A)\rightarrow R(B_L)B_R\) and \(M(A)\rightarrow M(B_L)\) if \(|R(B_L)|+|B_R|\le\tau\),<tbc>

(b) \(R(A)\rightarrow B_R\) and \(M(A)\rightarrow M(B_L)R(B_L)\) otherwise.<tbc>

4. If \(|B_L|\le\tau\) and \(|B_R|>\tau\), then \(R(A)\rightarrow R(B_R)\) and:<tbc>

(a) \(L(A)\rightarrow B_LL(B_R)\) and \(M(A)\rightarrow M(B_R)\) if \(|B_L|+|L(B_R)|\le\tau\),<tbc>

(b) \(L(A)\rightarrow B_L\) and \(M(A)\rightarrow L(B_R)M(B_R)\) otherwise.

Additionally, for the starting symbol _S_ of **G**, we add a starting symbol \(S^P\rightarrow L(S)M(S)R(S)\) to **G**_<sup>P</sup>_.

A simple inductive argument shows that every symbol _A_ of **G** with \(|A|>\tau\) satisfies

\(\mathrm{exp}_\mathbf{G}(A)=\mathrm{exp}_{\mathbf{G}^+}(L(A)\circ\mathrm{exp}_{\mathbf{G}^P}(M(A))\circ R(A)).\)

In particular, _P_=exp<sub>**G**_<sup>P</sup>_</sub>(_S<sup>P</sup>_) satisfies exp<sub>**G**<sup>+</sup></sub>(_P_)=exp<sub>**G**</sub>(_S_)=_X_.

It remains to prove that \(|P|<\frac{3}{\tau}|X|\). For this, we inductively show that every symbol _A_ of **G** with \(|A|>\tau\) satisfies \(|L(A)|+|R(A)|+\tau(|M(A)|+2)<3|A|\). To prove this claim, we analyze the cases based on the production \(A\rightarrow B_LB_R\).

1. If \(|B_L|\le\tau\) and \(|B_R|\le\tau\), then<tbc>

<tbc>\(|L(A)|+|R(A)|+\tau(|M(A)|+2)=|A|+2\tau<3|A|.\)<tbc>

2. If \(|B_L|>\tau\) and \(|B_R|>\tau\), then<tbc>

<tbc>\(|L(A)|+|R(A)|+\tau(|M(A)|+2)=|L(B_L)|+|R(B_R)|+\tau(|M(B_L)|+2+|M(B_R)|+2)<|L(B_L)|+|R(B_L)|+\tau(|M(B_L)|+2)+|L(B_R)|+\tau(|M(B_R)|+2)<3|B_L|+3|B_R|=3|A|.\)<tbc>

3. If \(|B_L|>\tau\), \(|B_R|\le\tau\), then<tbc>

• If \(|R(B_L)|+|B_R|\le\tau\), then<tbc>

<tbc>\(|L(A)|+|R(A)|+\tau(|M(A)|+2)=|L(B_L)|+|R(B_L)|+|B_R|+\tau(|M(B_L)|+2)<3|B_L|+|B_R|<3|A|.\)<tbc>

• Otherwise,<tbc>

<tbc>\(|L(A)|+|R(A)|+\tau(|M(A)|+2)=|L(B_L)|+|B_R|+\tau(|M(B_L)|+3)<|L(B_L)|+|B_R|+\tau(|M(B_L)|+2)+|R(B_L)|+|B_R|<3|B_L|+2|B_R|<3|A|.\)<tbc>

4. The case involving \(|B_L|\le\tau\) and \(|B_R|>\tau\) is symmetric to the previous one.

In particular, this claim holds for _A=S_, so \(|S^P|=|M(S)|+2<\frac{1}{\tau}(3|S|-|L(S)|-|R(S)|)<\frac{3}{\tau}|S|=\frac{3}{\tau}|X|\).

As for constructing the _DIST_ matrices, we use the original implementation from \[HLLW13\].

**Lemma 3.8** (\[HLLW13, Section 5\])**.** _Given straight-line programs_ **G**_<sub>X</sub> and_ **G**_<sub>Y</sub> and an integer_ \(\tau\ge 1\)_, in_ \(\widetilde{O}(|\mathbf{G}_X||\mathbf{G}_Y|\tau)\) _time one can construct a data structure that provides_ \(\widetilde{O}(1)\)_-time random access to the DIST_<sub>exp(_A<sub>X</sub>),_exp(_A<sub>Y</sub>_)</sub> _matrices for all symbols A<sub>X</sub> of_ **G**_<sub>X</sub> and A<sub>Y</sub> of_ **G**_<sub>Y</sub> satisfying_ \(|A_X|\le\tau\) _and_ \(|A_Y|\le\tau\).

Combining Lemmas 3.7 and 3.8, we complete our construction.

