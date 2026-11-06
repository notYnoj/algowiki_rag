Since we are only interested in computing the lower bound of the expectation and the event E<sup>(U)</sup> has almost the entire probability mass, it makes sense to consider events conditioned on the event E<sup>(U)</sup>. In particular, for the remainder of the proof, we assume that _M=pqr_, and the random variables \(\{a_i^{(pq)}\}_{i=1}^n\) and \(\{a_i^{(r)}\}_{i=1}^n\) are independent and distributed uniformly on the integer sets \[1_,pq_\] and \[0_,r_-1\] respectively.

## 7.1 Success Probability

**Lemma 7.0.1.** _Let M and n be the same as defined in the above problem **ACI-RESS**. Then the following holds for the Algorithm 4_<tbc>

\(\mathbb{P}_\mathbf{a}\left[Algorithm4succeeds\right]=\Omega\left(\frac{1}{n^2}\right).\)

<tbc>In the remainder of the section, we give a proof of Lemma 7.0.1. Recall the following set from the modular case

\(\mathbf{A}=\{\mathbf{u}\in\{0,1\}^n|\mathbf{u}^{(L)}\neq 0^{n/2},\mathbf{u}^{(R)}\neq 0^{n/2}\}.\)

The elements of the set A are ordered in a lexicographical sense, and A={**u**<sub>1</sub>,**u**<sub>2</sub>_,..._**u**_<sub>N</sub>_}, where **u**_<sub>i</sub>\<_**u**_<sub>j</sub>_ for any \(1\le i<j\le N\) and _N_=(2<sup>_n/_2</sup>-1)<sup>2</sup>=2_<sup>n</sup>_-2<sup>_n/_2+1</sup>+1.

The following random variable over a random choice of **a** denotes the number of integer collisions that survive the filtering algorithm. To be more precise, we have

\(\mathcal{C}^{(\mathrm{int})}:=\left|\left\{\left(\mathbf{u}_i,\mathbf{u}_j\right)\right|\begin{array}{ c }
i<j,\mathbf{u}_i,\mathbf{u}_j\in B_{s_0,s_1,s_2}, \\
\left|\frac{\mathbf{a}\cdot\mathbf{u}_i}{pq}\right|=\left|\frac{\mathbf{a}\cdot\mathbf{u}_j}{pq}\right|
\end{array}\right\}\right|.\)

Our filtering algorithm succeeds for an instance of the problem **ACI-RESS** if the value of this non- negative random variable is at least 1. Hence, similar to the modular case, analyzing the random variable C<sup>(int)</sup> will give us the success probability of the Algorithm 4.

For any input instance **a**, we can compute the value of C<sup>(int)</sup> by iterating through all the possible pairs of binary vectors from the set A, and considering whether the vectors pass through the filters of the algorithm and collide over integers. Hence, we define a binary random variable \(\mathcal{C}_{ij}^{(\mathrm{int})}\forall 1\le i<j\le N\) such that its value is 1 if and only if **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ pass through all the filters of the algorithm, and they collide over integers. To analyze this random variable \(\mathcal{C}_{ij}^{(\mathrm{int})}\), we first define the following random variables that will denote different sums of the input random variables. Let us fix a binary vector \(\mathbf{u}_i\in\mathbf{A}\) with Hamming weight _w<sub>i</sub>_, and define

\(S_{\mathsf{TS},i}:=\mathbf{a}\cdot\mathbf{u}_i\) (Total sum over integers)<br>
\(S_{\mathsf{TS},pq,i}:=\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\) (Total sum lower _pq_ bits over integers)<br>
\(S_{\mathsf{TS},i}^{(pq)}:=\mathbf{a}^{(pq)}\cdot\mathbf{u}_i\mathrm{mod}pq\) (Mod _pq_ bits of the Total sum _S_<sub>TS_,pq,i_</sub>)<br>
\(S_{\mathsf{C},pq,i}:=\left|\frac{\mathbf{a}^{(pq)}.\mathbf{u}_i}{pq}\right]=\frac{\mathbf{a}^{(pq)}.\mathbf{u}_i-(\mathbf{a}^{(pq)}.\mathbf{u}_i\mathrm{mod}pq)}{pq}\) (Carry bits from _S_<sub>TS_,pq,i_</sub>)<br>
\(S_{\mathsf{TS},r,i}:=\mathbf{a}^{(r)}\cdot\mathbf{u}_i\) (Remaining bits of the Total sum _S_<sub>TS_,i_</sub>)<br>
\(S_{\mathsf{LS},i}^{(p)}:=\mathbf{a}^{(p)(L)}\cdot\mathbf{u}_i^{(L)}\mathrm{mod}p\) (Left sum Mod _p_)<br>
\(S_{\mathsf{RS},i}^{(p)}:=\mathbf{a}^{(p)(R)}\cdot\mathbf{u}_i^{(R)}\mathrm{mod}p\) (Right sum Mod _p_)

