of _A_ and _B_ are obtained from the condensed representations of \(A'\) and \(B'\) similarly to the conversion of _A_<sup>∗</sup> into \(A'\). Note that _A_ and _B_ are Monge matrices due to Observation 3.3. The whole compression procedure takes \(\mathcal{O}(p^*+q^*+r^*+\delta(A^*)+\delta(B^*))\) time.

We now describe how to obtain the condensed representation of \(C^*:=A^*\otimes B'\) from the condensed representation of \(C:=A\otimes B=A'\otimes B'\). This constitutes one half of the decompression algorithm. Note that \(C_{i,k}=C_{f(i),k}^*\) for every \(i\in[0..p)\) and \(k\in[0..r)\). In particular, the topmost row of _C_<sup>∗</sup> coincides with the topmost row of _C_.

Consider some \(i\in[0..p^*-1)\) with \(\delta_{i,\cdot}(A^*)=0\). For every \(j\in[0..q)\), we have

\(A_{i+1,j}^*=A_{i,j}^*+(A_{i+1,0}^*-A_{i,0}^*)-\delta^\Sigma(A^*[i..i+1][0..j])=A_{i,j}^*+(A_{i+1,0}^*-A_{i,0}^*)\)

due to Observation 3.1. Therefore, for every \(k\in[0..r)\), we have

\(C_{i+1,k}^*=min\{A_{i+1,j}^*+B'_{j,k}|j\in[0..q)\}\)<br>
\(=min\{A_{i,j}^*+(A_{i+1,0}^*-A_{i,0}^*)+B'_{j,k}|j\in[0..q)\}\)<br>
\(=min\{A_{i,j}^*+B'_{j,k}|j\in[0..q)\}+(A_{i+1,0}^*-A_{i,0}^*)\)<br>
\(=C_{i,k}^*+(A_{i+1,0}^*-A_{i,0}^*).\)

In particular, we may use this equality to compute the values in the leftmost column of _C_<sup>∗</sup>: for \(i\in[0..p)\), we have \(C_{f(i),0}^*=C_{i,0}\) and \(C_{i^\prime,0}^*=C_{f(i),0}^*+(A_{i^\prime,0}^*-A_{f(i),0}^*)\) for \(i'\in(f(i)..f(i+1))\). Furthermore, for \(i'\in[f(i)..f(i+1)-1)\), we have \(\delta_{i^\prime,\cdot}(C^*)=0\). Finally,

\(C_{f(i+1)-1,k}^{*\square}=C_{f(i),k}^{*\square}+C_{f(i)+1,k}^{*\square}+\cdots+C_{f(i+1)-1,k}^{*\square}\)<br>
\(=\delta^\Sigma(C^*[f(i)..f(i+1)][k..k+1])\)<br>
\(=C_{f(i),k+1}^*+C_{f(i+1),k}^*-C_{f(i),k}^*-C_{f(i+1),k+1}^*\)<br>
\(=C_{i,k+1}+C_{i+1,k}-C_{i,k}-C_{i+1,k+1}\)<br>
\(=C_{i,k}^\square\)

for every \(k\in[0..r-1)\) due to the definition of _C_ and Observation 3.1. Therefore, the set \(core(C^*)=\{(i,k,C_{i,k}^{*\square})|i\in[0..p^*-1),k\in[0..r-1),C_{i,k}^{*\square}\neq 0\}=\{(f(i+1)-1,k,C_{i,k}^{\square})|(i,k,C_{i,k}^{\square})\in core(C)\}\) can be computed in time \(\mathcal{O}(\delta(C))=\mathcal{O}(\delta(A)+\delta(B))=\mathcal{O}(\delta(A^*)+\delta(B^*))\), where \(\delta(C)\le 2\cdot(\delta(A)+\delta(B))\) due to Theorem 1.1. The whole procedure takes \(\mathcal{O}(p^*+r+\delta(A^*)+\delta(B^*))\) time.

We showed how to decompress \(A\otimes B=A'\otimes B'\) into \(A^*\otimes B'\). The decompression of \(A^*\otimes B'\) into \(A^*\otimes B^*\) can be done symmetrically in time \(\mathcal{O}(p^*+r^*+\delta(A^*)+\delta(B^*))\). \(\blacktriangleleft\)

\(\blacktriangleright\) **Theorem 1.2.** _There is a (deterministic) algorithm that, given the condensed representations of an_ \(n_1\times n_2\) _Monge matrix M_<sub>1</sub> _and an_ \(n_2\times n_3\) _Monge matrix M_<sub>2</sub>_, in time_ \(\mathcal{O}(n_1+n_2+n_3+(\delta(M_1)+\delta(M_2))log(1+\delta(M_1)+\delta(M_2)))\) _computes the condensed representation of_ \(M_1\otimes M_2\).

**Proof.** We now formally describe the recursive procedure `Multiply` that is run for a \(p^*\times q^*\) matrix _A_<sup>∗</sup> and a \(q^*\times r^*\) matrix _B_<sup>∗</sup>. Consult Algorithm 1 for the pseudocode.

We first apply the `Compress` algorithm of Lemma 4.6 to obtain the condensed representations of a Monge matrix _A_ of size \(p\times q\) with \(p\le\delta(A^*)+1=\delta(A)+1\) and \(q\le\delta(A^*)+\delta(B^*)+1\) and a Monge matrix _B_ of size \(q\times r\) with \(r\le\delta(B^*)+1=\delta(B)+1\). We then compute the condensed representation of \(C:=A\otimes B\), and finally we use the `Decompress` algorithm of Lemma 4.6 to obtain the condensed representation of \(A^*\otimes B^*\).

