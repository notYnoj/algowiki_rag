### Step 2b: Reconstruction of a Lattice Vector.

The reduction runs the PESS algorithm on this instance, and converts the returned unequal sets (_X,Y_) into a lattice vector by computing \(\mathbf{v}^{(\tilde{\lambda}_n)}:=\sum_{i\in X}\mathbf{x}^{(i)}-\sum_{j\in Y}\mathbf{x}^{(j)}\). If the PESS algorithm fails to find a solution, the reduction treats this as returning \((\emptyset,\emptyset)\). In this case, the corresponding candidate vector is **0** and is discarded at the final output stage.

### Step 3: Final vector.

After constructing the vectors \(\mathbf{v}^{(\tilde{\lambda}_n)}\) for \(\tilde{\lambda}_n\in[2^{\lceil log(\|\mathbf{D}\|)\rceil},2^{\lceil log(\|\mathbf{D}\|)\rceil-1},\dots,2^{\lfloor log(\|\mathbf{D}\|-log(B)\rfloor)}]\), the reduction returns the shortest non-zero vector among them.

We present the full pseudocode of the reduction in Algorithm 2.

Input: A lattice basis B=\[b<sub>1</sub>,...,b<sub>n</sub>\], parameters N:=N(n) and B:=B(n)<br>
Output: A lattice vector \(\mathbf{v}\in\mathcal{L}(\mathbf{B})\)<br>
Perform the lattice reduction algorithm in Theorem 5.1 to obtain D. Set W:=8BN<sup>3</sup>.<br>
Sample x<sup>(1)</sup>,...,x<sup>(N)</sup> using the algorithm in Theorem 5.2 on D with \(s=4\pi\sqrt{n}N\|\mathbf{D}\|_2\).<br>
Sample n primes r<sub>1</sub>,...,r<sub>n</sub> independently and uniformly from \[N<sup>3</sup>\].<br>
Sample n integers s<sub>1</sub>,...,s<sub>n</sub> independently and uniformly from \[N<sup>2</sup>\].<br>
for \(\tilde{\lambda}_n=2^{\lceil log(\|\mathbf{D}\|_2)\rceil},\dots,2^{\lfloor log(\|\mathbf{D}\|_2)-log(B)\rfloor}\) do<br>
   Set a<sub>i</sub>=f(x<sup>(i)</sup>) for all \(i\in[N]\) Obtain X,Y by running the PESS algorithm on the input (a<sub>1</sub>,...,a<sub>N</sub>).<br>
   Set \(\mathbf{v}^{(\tilde{\lambda}_n)}:=\sum_{i\in X}\mathbf{x}^{(i)}-\sum_{j\in Y}\mathbf{x}^{(j)}\).<br>
end<br>
Output the shortest non-zero vector among the candidates \(\left\{\mathbf{v}^{(\tilde{\lambda}_n)}\right\}_{\tilde{\lambda}_n}\).

## 5.2 Correctness

We prove correctness by analyzing a modified version of the reduction. Recall that the reduction sets \(s:=4\pi\sqrt{n}N\|\mathbf{D}\|_2\). By Theorem 5.2, the actual sampling procedure used by the reduction produces vectors whose joint distribution is negligibly close to that of _N_ independent samples from D<sub>L,_s_</sub>. Thus, it suffices to analyze an idealized version of the reduction in which (**x**<sup>(1)</sup>,...,**x**<sup>(_N_)</sup>) are sampled independently from D<sub>L,_s_</sub>. This discrepancy between the actual and idealized samplers contributes only a negligible additive error to the overall failure probability.

We now introduce a modified idealized reduction that differs only in its sampling step. First, sample \(\mathbf{x}^{\prime(1)},\dots,\mathbf{x}^{\prime(N)}\) independently from D<sub>L,_s_</sub>. Then, for each \(i\in[N]\), sample an independent uniform bit \(\tau_i\in\{0,1\}\) and define

\(\mathbf{x}^{(i)}:=\left\{\begin{array}{ c c }
\mathbf{x}^{\prime(i)}+\mathbf{v}^* & \text{if}\tau_i=1, \\
\mathbf{x}^{\prime(i)} & \text{if}\tau_i=0,
\end{array}\right.\)

where **v**<sup>∗</sup> is a fixed shortest nonzero vector of L. All subsequent steps of the reduction remain unchanged.

This modified sampling procedure is not efficient, since it requires knowledge of **v**<sup>∗</sup>. However, efficiency is irrelevant for the present argument, as we use the modified reduction only for the correctness analysis. Since \(\|\mathbf{v}^*\|_2=\lambda_1(\mathcal{L})\le\lambda_n(\mathcal{L})\le\tilde{\lambda}_n\), Lemma A.2.1 implies that<tbc>

\(\Delta(\mathcal{D}_{\mathcal{L},s},\mathcal{D}_{\mathcal{L},s}+\mathbf{v}^*)\le\mathcal{O}((NB)^{-1}),\)

**Algorithm 2:** Reduction behind Theorem 1.2.

