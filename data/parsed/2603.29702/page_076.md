Since \(\sum_I\sigma(I)=1\), we can apply Jensen’s inequality (using the concavity of the square root function) to move the summation inside the square root:

\(C_s\le\|A\|_1\sqrt{\sum_I\sigma(I)\cdot 2D(q_I\|u_\text{local})}.\)

Let \(G_s:=\sum_{I\in s}\sigma(I)D(q_I\|u_\text{local})\) be the expected information gain on scale _s_. Then \(C_s\le\|A\|_1\sqrt{2G_s}\).

Finally, we sum over all scales \(s\in[S]\) to bound \(\includegraphics{}\text{TD}_{M,S}(A)\). Using the Cauchy-Schwarz inequality:<tbc>

\(\includegraphics{}\text{TD}_{M,S}(A)=\sum_{s=1}^SC_s\le\|A\|_1\sum_{s=1}^S\sqrt{2G_s}\le\|A\|_1\sqrt{S\sum_{s=1}^S2G_s}.\)

<tbc>From Eq. (35), we know \(\sum G_s=D(P\|U)\). Thus:<tbc>

\(\includegraphics{}\text{TD}_{M,S}(A)\le\|A\|_1\sqrt{2S\cdot D(P\|U)}.\)

<tbc>It remains to bound \(D(P\|U)\). We maximize \(\sum p_x\mathrm{ln}(np_x)\) subject to \(0\le p_x\le\|A\|_\infty/\|A\|_1\) and \(\sum p_x=1\). The divergence is maximized when the distribution is most concentrated (minimum entropy). Since \(p_x\le\|A\|_\infty/\|A\|_1\) for all _x_, we have:

\(D(P\|U)=\sum_xp_x\mathrm{ln}(np_x)\le\sum_xp_x\mathrm{ln}\left(n\frac{\|A\|_\infty}{\|A\|_1}\right)=\mathrm{ln}\left(\frac{n\|A\|_\infty}{\|A\|_1}\right).\)

Plugging this back into the tree deviation bound yields the lemma.

## C A Counter-Example to a Ratio-Free Version of Lemma 4.3

We provide an example showing that the \(\alpha\)-dependence of Lemma 4.3 is necessary, even for _M_=2: The authors are grateful to an anonymous reviewer for this construction.

**Lemma C.1.** _We can construct two sequences A_=(_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_) _and B_=(_b_<sub>1</sub>_,b_<sub>2</sub>_,...,b<sub>n</sub>_) _of non- negative real numbers where n_=2_<sup>S</sup>, such that_

\(\includegraphics{}\text{SD}_{2,S}(A,B)=\Omega\left(S\sum_xb_x\right).\) (36)

_Proof._ We let _B_={1,1_,...,_1} simply be the length-_n_ sequence of 1’s. We let _A_={1,2,2,4,2,4,4,8_,..._} be the sequence where<tbc>

\(a_i=2^\text{number of 1’s in the binary representation of}(i-1).\)

<tbc>Notice that for every recursion interval (_l,r_\], we have \(\frac{A_{\Sigma(l,(l+r)/2]}}{A_{\Sigma((l+r)/2,r]}}=\frac{1}{2}\). Therefore \(\frac{\text{TD}_2(A(l,r])}{A_{\Sigma(l,r]}}=1/3\). Since \(B_{\Sigma(l,r]}=r-l\), we have \(\text{SD}_2(A(l,r],B(l,r])=\frac{r-l}{3}\) . Thus

\(\includegraphics{}\text{SD}_{2,S}(A,B)=\sum_{s\in[S]}\sum_{(l,r]\in s}\text{SD}_M(A(l,r],B(l,r])=\sum_{s\in[S]}n/3=nS/3=S\sum_xb_x/3=\Omega\left(S\sum_xb_x\right).\)

