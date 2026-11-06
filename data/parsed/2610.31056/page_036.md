Input: \((a_1,a_2,\dots,a_n)\in[M]^n\); Parameters: \(p,q\in\Theta(M^{1/4})\) co-prime, \(s_0,s_1\in\mathbb{Z}_p\) and \(s_2\in\mathbb{Z}_q\)<br>
Output: A non-trivial integer collision or \(\perp\)<br>
Build two mod-p DP tables storing the sizes of the following sets \(\forall s\in\mathbb{Z}_p\) and \(\forall 1\le i\le n/2\)<br>
\(B_{i,s}^{(L)}:=\left\{\mathbf{u}\in\{0,1\}^i\left|\sum_{j=1}^ia_ju_j\equiv s\mathrm{mod}p\right\},\)<br>
\(B_{i,s}^{(R)}:=\left\{\mathbf{v}\in\{0,1\}^i\left|\sum_{j=1}^ia_{n/2+j}v_j\equiv s\mathrm{mod}p\right\}.\)<br>
Compute the bins \(B_{n/2,s_0}^{(L)}\) and \(B_{n/2,s_1}^{(R)}\) by backtracing the DP table; look for a collision in these sets; else continue.<br>
Construct the following set<br>
\(B_{s_0,s_1,s_2}:=\left\{\mathbf{u}||\mathbf{v}\left|\begin{array}{ c }
\mathbf{u}\in B_{n/2,s_0}^{(L)},\mathbf{v}\in B_{n/2,s_1}^{(R)}, \\
\mathbf{a}^{(L)}\cdot\mathbf{u}+\mathbf{a}^{(R)}\cdot\mathbf{v}\equiv s_2\mathrm{mod}q
\end{array}\right\}\)<br>
Look for a non-trivial integer collision in this list B<sub>s<sub>0</sub>,s<sub>1</sub>,s<sub>2</sub></sub>. If one is found, it outputs this collision; otherwise, it outputs \(\perp\).<br>
\(\text{ }\)<br>
where 0\<s\<pq. Recall that the input vector **a** is uniformly distributed over the set \[_M_\]<sup>n</sup>={1,2_,...,M}<sup>n</sup>_. Let us split all the random variables, _a<sub>i</sub>_, into the lower _pq_ bits and the remaining as follows<br>
\(a_i=a_i^{(pq)}+a_i^{(r)}\cdot pq,\)<br>
where \(a_i^{(pq)}\in[0,pq)\) and \(a_i^{(r)}=[0,r]\forall 1\le i\le n\).<br>
Now, we split the probability mass of the distribution of the random variable _a<sub>i</sub>_ into two cases. First, the inner rectangle, i.e. \(1\le a_i\le pqr\), and second the truncated slice, i.e. \(pqr<a_i\le M\). Let \(\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\) and \(\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\) be two disjoint exhaustive events that denote these two cases, respectively. Then, we have<br>
\(\mathbb{P}_{a_i}\left(\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\right)=\frac{s}{M},\mathbb{P}_{a_i}\left(\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)=1-\frac{s}{M}.\)<br>
Since s\<pq, we have \(s/M=\mathcal{O}\left(1/2^{n/2}\right)\). Let \(\mathsf{E}^{(\mathsf{T})}:=\vee_{i=1}^n\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\), then using union bound, we have<tbc>

\(\mathbb{P}_\mathbf{a}\left(\mathsf{E}^{(\mathsf{T})}\right)\le\frac{ns}{M}=\mathcal{O}\left(\frac{n}{2^{n/2}}\right).\)

<tbc>Hence, we have<tbc>

\(\mathbb{P}_\mathbf{a}\left(\mathsf{E}^{(\mathsf{U})}\right)\ge 1-\mathcal{O}\left(\frac{n}{2^n}\right).\)

**Algorithm 4:** Algorithm for Theorem 1.3.

