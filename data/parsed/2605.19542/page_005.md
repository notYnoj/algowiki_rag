<tbc>Our proof of the Main Theorem, presented in the next section, uses only the elementary linear algebraic tools established in Section 2. This gives a more accessible proof of the Erd ́os-Heilbronn theorem, avoiding the advanced combinatorial and algebraic machinery used in prior arguments.

## 4. Proof of the Main Theorem

In this section, we give the complete proof of the Main Theorem using the linear algebraic tools from Section 2. We split the proof into several auxiliary lemmas, followed by the final argument for the main result.

Let _A_={_a_<sub>1</sub>_,...,a<sub>m</sub>_} and _B_={_b_<sub>1</sub>_,...,b<sub>k</sub>_} be subsets of Z_/p_Z. Let _w_<sub>1</sub>(_a_<sub>1</sub>)_,...,w_<sub>1</sub>(_a<sub>m</sub>_) and _w_<sub>2</sub>(_b_<sub>1</sub>)_,...,w_<sub>2</sub>(_b<sub>k</sub>_) be two sequences in Z_/p_Z. For nonnegative integer _i_, we introduce

\(\alpha_i:=\alpha_i(A,w_1)=\sum_{j=1}^mw_1(a_j)a_j^i\) (4.5)

and

\(\beta_i:=\beta_i(B,w_2)=\sum_{j=1}^kw_2(b_j)b_j^i.\) (4.6)

Let \(C=A\dot{+}B\), and suppose that _C_={_c_<sub>1</sub>_,...,c<sub>t</sub>_}. For \(c_j\in C\), we define<tbc>

\(w(c_j)=\sum_{a\in A,b\in Ba+b=c_j}w_1(a)w_2(b)(a-b).\)

<tbc>Then we introduce

\(\gamma_i:=\gamma_i(C,w)=\sum_{j=1}^tw(c_j)c_j^i.\)

**Lemma 4.1.** _Let A,B,C and_ \(\alpha_i,\beta_i,\gamma_i\) _be as above. Then_

\(\gamma_n=\sum_{i=0}^nC_n^i\alpha_{i+1}\beta_{n-i}-\sum_{i=0}^nC_n^i\alpha_i\beta_{n+1-i}.\)

