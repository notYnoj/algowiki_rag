<tbc>Since the vectors \(\mathbf{u}_{lk}^{(10)}\) and \(\mathbf{u}_{lk}^{(01)}\) do not overlap, and using equations (9), we can say these vectors satisfy the weight constraints of the Lemma 7.0.3, therefore we get the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{D}_{lk}^{(\mathsf{int})}\right)=\Omega\left(\frac{1}{np^4q^2r}\right).\) (11)

Using equations (10), (11), and the fact that \(|T|=\Theta(4^n)\), \(p,q=\Theta\left(M^{1/4}\right)\), and \(M=pqr=\Omega\left(2^n\right)\), we get the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathsf{int})}\right)\ge\sum_{i<j}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}^{(\mathsf{int})}\right)\)<br>
\(>\sum_{(\mathbf{u}_l,\mathbf{u}_k)\in\mathsf{T}}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{lk}^{(\mathsf{int})}\right)\)<br>
\(\ge\sum_{(\mathbf{u}_l,\mathbf{u}_k)\in\mathsf{T}}\mathbb{E}_\mathbf{a}\left(\mathcal{D}_{lk}^{(\mathsf{int})}\right)\)<br>
\(=\Omega\left(\frac{4^n}{np^4q^2r}\right)\)<br>
\(=\Omega\left(\frac{1}{n}\right).\)

**Remark 3.** _Recall that we assume M=pqr, and that the random vectors_ \(a_i^{(pq)}\) _and_ \(a_i^{(r)}\) _are independent and uniformly distributed over the sets_ \[1_,pq_\] _and_ \[0_,r_-1\]_, respectively. This assumption holds conditioned on the event that_ \(1\le a_i\le pqr\forall 1\le i\le n\)_, given M=pqr+s. Since the probability of this event is at least_ 1-_n/_2<sup>_n/_2</sup>_, incorporating this factor into the above calculation of the first moment does not change the asymptotic bound, and we obtain the same result. This argument is explained in detail in Section E.2._

This completes the proof of Lemma 7.0.2.

## 7.1.2 Second Moment

In the previous subsection, while analyzing the first moment of the random variable C<sup>(int)</sup>, we assumed that _a<sub>i</sub>_ are random integers chosen uniformly from the set \[1_,pqr_\]. We ignored the truncated slice when \(pqr<a_i\le pqr+s\), since the probability of this event is negligible, and we were interested in the lower bound of the first moment. Now, we need to compute an upper bound of the second moment of the random variable C<sup>(int)</sup>.

**Lemma 7.0.4.** _Let M and n be the same as defined in the problem **ACI-RESS**. Then the following holds for the Algorithm 4_<tbc>

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}^{(\mathsf{int})2}\right)=\mathcal{O}\left(1\right).\)

<tbc>_Proof._ Let us first define another random variable that denotes the number of non-trivial modular collisions in the final list _B_<sub>_s_<sub>0</sub>_,s_<sub>1</sub>_,s_<sub>2</sub></sub> as follows<tbc>

\(\mathcal{C}^{(\mathsf{pqr})}:=\left|\left\{\left(\mathbf{u}_i,\mathbf{u}_j\right)\left|\begin{array}{ c }
i<j,\mathbf{u}_i,\mathbf{u}_j\in B_{s_0,s_1,s_2}, \\
\mathbf{a}^{(r)}\cdot\mathbf{u}_i\equiv\mathbf{a}^{(r)}\cdot\mathbf{u}_jmodr.
\end{array}\right\}\right|.\)

