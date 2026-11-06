For all \(u,v\in V\) , count the number of \(w\in V\) such that _D_[_u,w_]+_D_[_w,v_]_\<D_[_u,r<sub>u,v</sub>_]+_D_[_r<sub>u,v</sub>,v_] using "Fredman’s trick meets dominance product". Specifically, iterate over all \(r\in R\) and count the number of \(w\in V\) with _D_[_u,w_]+_D_[_w,v_]_\<D_[_u,r_]+_D_[_r,v_]. To do so, construct _A_ and _B_ with _A_[_i,j_]:=_D_[_i,j_]-_D_[_i,r_] and _B_[_i,j_]:=_D_[_r,j_]-_D_[_i,j_].<sup>2</sup> Compute the dominance product Dom with Dom[_i,j_]=|{_k:A_[_i,k_]_\<B_[_k,j_]}|. By construction, we have

\(A[i,k]<B[k,j]\Leftrightarrow D[i,k]+D[k,j]<D[i,r]+D[r,j].\)

Output the set _U_ of pairs (_u,v_) for which the brute force and dominance product counts are different.

**Running time.** Since we are given _n_<sup>2</sup> subsets of size _q_ from a universe of size _n_, a uniformly random set of size O(_n_log_n/p_) hits all of them with non-zero probability by a standard argument (see, e.g., [4, Chapter 1]). Hence, the optimal hitting set also has size at most O(_n_log_n/p_). The greedy hitting set algorithm from Chapter 2 in [43] is a log_n_-approximation and runs in near-linear time. We get |_R_|=O(_n_log<sup>2</sup>_n/p_).

Computing the detours, the greedy hitting set, and the brute force counts takes time O(_n_<sup>2</sup>_q_). Yuster’s algorithm [46] computes dominance product in time \(\mathcal{O}(n^{4-r}+n^{\omega(1,r,1)+o(1)})\) for any _r_. Here \(\omega(a,b,c)\) is the rectangular matrix multiplication exponent such that it takes time \(n^{\omega(a,b,c)+o(1)}\) to multiply a \(n^a\times n^b\) with a \(n^b\times n^c\) matrix. With the optimal choice of _r_ and the best known algorithm for rectangular matrix multiplication [42, 10], computing one dominance product takes time O(_n_<sup>2.658</sup>). In total, this gives the claimed running time.

**Correctness.** First, consider \((u,v)\in V^2\backslash\mathrm{U}(G,C,p)\), so for all \(w\in V\backslash C[u,v]\), we have

\(|\{c\in C[u,v]:\mathrm{detour}_{D,u,v}(c)\le\mathrm{detour}_{D,u,v}(w)\}|\ge p.\)

Since _r<sub>u,v</sub>_ is within the _p_ elements of _C_[_u,v_] with minimum detour<sub>_D,u,v_</sub>, for all \(w\in V\backslash C[u,v]\), we have \(\mathrm{detour}_{D,u,v}(r_{u,v})\le\mathrm{detour}_{D,u,v}(w)\). So, both counts in the algorithm must be the same and \((u,v)\in V^2\backslash U\).

Furthermore, if both counts are the same notice that

\(min_{w\in C[u,v]}D[u,w]+D[w,v]=min_{w\in V}D[u,w]+D[w,v].\)

So, by Lemma 3, the condition holds for all \((u,v)\in V^2\backslash U\).

We note that it would be possible to further speed up the verification part by using a co-nondeterministic algorithm for dominance product from [12]. However, that algorithm would need additional information about the dominance product included in the certificate. This would require more complex predictions and introduce additional sources of error, while not significantly improving the result. The best running time one could reach this way is \(\tilde{\mathcal{O}}(n^{(6+\omega)/3})\), or O(_n_<sup>2.80</sup>) with the current bound on the matrix multiplication exponent [3].

Intuitively, for every distance entry _D_[_u,v_] that is wrong but successfully verified, there must be another wrong entry _D_[_u,w_] or _D_[_w,v_] that the computation relied on. This allows us later in the final algorithm to trust correctly verified entries until we discover such a witness with incorrect distance. This is formalized in the next lemma.

<sup>2</sup> If the term \(\infty-\infty\) arises in this computation, we replace it with \(+\infty\) if in _A_ and with \(-\infty\) if in _B_.

