see that we can decide whether _H_ is 3-colorable. This is, by Theorem 12, a contradiction to the ETH once we bound the running time of the reduction, which we now do. **Running time.** Building _G_<sup>[_k_]</sup>, optionally computing a 4-sequence S of _G_<sup>[_k_]</sup>, and running A on _G_<sup>[_k_]</sup>,S takes time \(\mathcal{O}\left(2^{\mathcal{O}\left(\frac{N}{log^{c+1}N}\right)}+n^{\mathcal{O}(1)}\right)=2^{\mathcal{O}\left(\frac{N}{log^{c+1}N}\right)}=2^{o(N/log^cN)},\) as desired. **Case when _H_ is 3-colorable.** By Theorem 13, it holds that \(\chi(G)\le 3\). Therefore, \(\chi(G^{[k]})\le 3^k\), by giving color \((\nu(v_1),\dots,\nu(v_k))\) to each vertex \((v_1,\dots,v_k)\in V(G^{[k]})\) for a fixed proper 3-coloring \(\nu\) of _G_. **Case when _H_ has no 3-colorable induced subgraph on at least** \(\beta N\) **vertices.** We have \(\chi(G^{[k]})\ge\frac{|V(G^{[k]})|}{\alpha(G^{[k]})}=\frac{|V(G)|^k}{\alpha(G^{[k]})}\ge\frac{|V(G)|^k}{\alpha(G)^k}=\left(\frac{|V(G)|}{\alpha(G)}\right)^k.\) where the first inequality holds for any graph, and the second inequality uses Lemma 9. We set \(q:=(3N+3|E(H)|)\lceil log(3N)\rceil\le 3(\Delta+1)N\lceil log(3N)\rceil,\) since _H_ has maximum degree at most \(\Delta\). By Theorem 13, \(\alpha(G)\le\beta N+q\) and |_V(G_)|=3_N_+3_q_. Thus, \(\chi(G^{[k]})\ge\left(\frac{3N+3q}{\beta N+q}\right)^k=3^k\cdot\left(1+\frac{(1-\beta)N}{\beta N+q}\right)^k\ge 3^k\cdot\left(1+\frac{1-\beta}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\right)^k.\) **Approximation gap.** The previous paragraphs have established that the approximation gap for \(\chi(G^{[k]})\) is at least \(\frac{3^k\cdot(1+(1-\beta)/(\beta+3(\Delta+1)\lceil log(3N)\rceil))^k}{3^k}=\left(1+\frac{1-\beta}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\right)^k.\) Thus we just need to show that \(r:=n^{\gamma/(loglogn)^2}<\left(1+\frac{1-\beta}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\right)^k\) in order to conclude. \(\vartriangleright\) Claim 14. It holds that \(logr<klog\left(1+\frac{1-\beta}{\beta+3(\Delta+1)\lceil log(3N)\rceil}\right).\) Proof. We have \(logr=\frac{\gamma logn}{(loglogn)^2}\) and \(logn=klog|V(G)|=klog(3N+3q)\le klog(12(\Delta+1)N\lceil log(3N)\rceil)\le 2klog(12(\Delta+1)N),\) where the last inequality uses Item 4.

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

\(\begin{array}{ c } \text{\textit{Q}} \\ \text{\textit{Q}} \\ \text{\textit{Q}} \end{array}\)

