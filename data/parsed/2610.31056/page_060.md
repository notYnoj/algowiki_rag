**Joint Distribution of** \(a_i^{(pq)}\) **and** \(a_i^{(r)}\)**.**

\(\mathbb{P}_{a_i}\left(a_i^{(pq)}=x,a_i^{(r)}=y\right)\)<br>
\(=\left\{\begin{array}{ c c }
\frac{1}{M} & 1\le x\le pq,0\le y<r \\
\frac{1}{M} & 1\le x\le s,y=r \\
0 & y=r,x>s.
\end{array}\right.\)

## Dependence between \(a_i^{(pq)}\) and \(a_i^{(r)}\).

Let us first make the following observations after looking at the above distributions

1. If _s_=0, it is easy to observe that the two random variables \(a_i^{(pq)}\) and \(a_i^{(r)}\) are independent and uniformly distributed over the sets \[0_,pq_) and \[0_,r_) respectively.<tbc>

2. We also observe that the main dependence occurs when _y=r_, since in this case, residues can only take _s_ values rather than _pq_ values, where \(0\le s<pq\).

Keeping these observations in mind, we split the probability mass of the distribution of the random variable _a<sub>i</sub>_ into two cases. First, the inner rectangle, i.e. \(1\le a_i\le pqr\), and second the truncated slice, i.e. \(pqr<a_i\le M\). Let \(\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\) and \(\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\) be two disjoint exhaustive events that denote these two cases, respectively. Then, we have

\(\mathbb{P}_{a_i}\left(\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\right)=\frac{s}{M},\)<br>
\(\mathbb{P}_{a_i}\left(\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)=1-\frac{s}{M}.\)

Since \((s)/M<pq/M=\mathcal{O}\left(1/2^{n/2}\right)\), we can ignore this event and focus only on the event \(\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\). Let \(\mathsf{E}^{(\mathsf{T})}:=\vee_{i=1}^n\mathsf{E}_\mathsf{i}^{(\mathsf{T})}\), then using union bound, we have<tbc>

\(\mathbb{P}_{a_i}\left(\mathsf{E}^{(\mathsf{T})}\right)\le\frac{ns}{M}=\mathcal{O}\left(\frac{n}{2^n}\right).\)

<tbc>Hence, we have

\(\mathbb{P}_{a_i}\left(\mathsf{E}^{(\mathsf{U})}\right)\ge 1-\mathcal{O}\left(\frac{n}{2^n}\right).\)

**Proposition E.0.1.** _Let_ \(a_i\leftarrow^\$[M]\forall 1\le i\le n\)_, where M=r.pq+s. Then, we have the following distributions for all_ \(1\le i\le n\)

1. _For all_ \(0\le x<pq\)_, we have_<tbc>

<tbc>\(\mathbb{P}_{a_i}\left(a_i^{(pq)}=x\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)=\left\{\begin{array}{ c c }
\frac{r-1}{M} & x=0 \\
\frac{r}{M} & 0<x<pq
\end{array}\right..\)<tbc>

<tbc>_2. For all_ \(0\le y<r\)_, we have_<tbc>

<tbc>\(\mathbb{P}_{a_i}\left(a_i^{(r)}=y\big|\mathsf{E}_\mathsf{i}^{(\mathsf{U})}\right)=\left\{\begin{array}{ c c }
\frac{pq-1}{M} & y=0 \\
\frac{pq}{M} & 0<y<r
\end{array}\right..\)<tbc>

