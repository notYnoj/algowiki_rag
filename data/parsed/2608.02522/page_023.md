on _M_ in the lemma, we then have \(\mathbf{u}_s^\top\mathbf{u}_s=\frac{1}{\left\|M\right\|}\mathbf{b}_s^\top\mathbf{b}_s=\frac{M_{s,s}}{\left\|M\right\|}=\frac{1}{\left\|M\right\|}\) for every \(s\in S\). Furthermore, by definition of _C_, we have<tbc>

\(\sum_{s\in S}\mathbf{u}_s\mathbf{u}_s^\top+\sum_{i=1}^k\mathbf{u}_i\mathbf{u}_i^\top=\frac{1}{\left\|M\right\|}\sum_{s\in S}\mathbf{b}_s\mathbf{b}_s^\top+C=\frac{1}{\left\|M\right\|}BB^\top+C=I_S.\)

<tbc>We are therefore now in the position to apply Theorem 4.6 to the collection of vectors \(\{\mathbf{u}_s|s\in S\}\cup\{\mathbf{u}_i|i\in[k]\}\) with the parameters \(\delta:=\frac{1}{\left\|M\right\|}\) and _r_:=_q_. This yields a partition of the index-set<sup>5</sup> \(S\cup[k]\) into _q_ disjoint (possibly empty) sets \(T'_1,\dots,T'_q\), such that<tbc>

\(\left\|\sum_{s\in S\cap T_j^\prime}\mathbf{u}_s\mathbf{u}_s^\top+\sum_{i\in[k]\cap T_j^\prime}\mathbf{u}_i\mathbf{u}_i^\top\right\|\le\left(\frac{1}{\sqrt{q}}+\sqrt{\delta}\right)^2\)

<tbc>for every \(j\in[q]\). Set \(T_j:=T'_j\cap S\) for every \(j\in[q]\), such that \(S=T_1\sqcup\cdots\sqcup T_q\). Note that since the matrices \(\sum_{s\in T_j}\mathbf{u}_s\mathbf{u}_s^\top=\sum_{s\in S\cap T_j^\prime}\mathbf{u}_s\mathbf{u}_s^\top\) and \(\sum_{i\in[k]\cap T_j^\prime}\mathbf{u}_i\mathbf{u}_i^\top\) are both clearly positive semidefinite for every \(j\in[q]\), the fourth linear algebra fact stated before the proof of the lemma now implies that<tbc>

\(\left\|\sum_{s\in T_j}\mathbf{u}_s\mathbf{u}_s^\top\right\|\le\left(\frac{1}{\sqrt{q}}+\sqrt{\delta}\right)^2\)

<tbc>for every \(j\in[q]\). Finally, recalling that \(\mathbf{u}_s=\frac{1}{\sqrt{\left\|M\right\|}}\mathbf{b}_s\) for every \(s\in S\) and that \(\delta=\frac{1}{\left\|M\right\|}\), this implies that

\(\left\|\sum_{s\in T_j}\mathbf{b}_s\mathbf{b}_s^\top\right\|\le\left\|M\right\|\cdot\left(\frac{1}{\sqrt{q}}+\frac{1}{\sqrt{\left\|M\right\|}}\right)^2=\left(\sqrt{\frac{\left\|M\right\|}{q}}+1\right)^2\)

for every \(j\in[q]\).

Finally, for every fixed \(j\in[q]\), note that we can write \(\sum_{s\in T_j}\mathbf{b}_s\mathbf{b}_s^\top\) as \(B_jB_j^\top\), where \(B_j\in\mathbb{R}^{S\times S}\) is defined as the matrix whose column indexed by \(s\in S\) equals **b**_<sub>s</sub>_ if \(s\in T_j\), and has zero-entries otherwise. By the third linear algebra fact stated before the proof, \(B_jB_j^\top\) further has the same non-zero (i.e., positive) eigenvalues as \(B_j^\top B_j\). The latter matrix is easily verified to equal _M<sub>T<sub>j</sub></sub>_, by virtue of _M_ being the Gram matrix of the \((\mathbf{b}_s)_{s\in S}\). Hence, it follows that

\(\left\|M_{T_j}\right\|=\left\|B_j^\top B_j\right\|=\lambda_\mathrm{max}(B_j^\top B_j)=\lambda_\mathrm{max}(B_jB_j^\top)=\left\|B_jB_j^\top\right\|\le\left(\sqrt{\frac{\left\|M\right\|}{q}}+1\right)^2\)

for every \(j\in[q]\). This shows that the partition \(S=T_1\sqcup\cdots\sqcup T_q\) of _S_ satisfies the property required by the lemma statement, and concludes the proof. \(\square\)

We are now ready for the proof of Lemma 4.5. As explained before, with this proof we then also conclude the proof of Theorem 1.6.

<sup>5</sup>W.I.o.g., we assume here that _S_ is disjoint from \[_k_\].

