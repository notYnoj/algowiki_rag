1. If _n_ is odd, since<tbc>

\(\sigma(\mathcal{T}(n))=\left\{2n-2,n-3^{[3]},\dots,\frac{n-3^{[3]}}{2},\frac{n-7^{[2]}}{2},\frac{n-9^{[3]}}{2},\dots,-2^{[3]},-3^{[T(n-3)]}\right\}\)<br>
\(\text{and}\)<br>
\(\sigma(\mathcal{T}(n-1))=\left\{2n-4,n-4^{[3]},\dots,\frac{n-3^{[3]}}{2},\frac{n-5^{[2]}}{2},\frac{n-9^{[3]}}{2},\dots,-2^{[3]},-3^{[T(n-4)]}\right\},\)<br>
\(\text{we get}\)<br>
\(\sigma(G_{1,2})=\left\{2n-2,2n-4,n-3^{[3]},n-4^{[3]},\dots,\frac{n-3^{[6]}}{2},\frac{n-5^{[2]}}{2},\frac{n-7^{[2]}}{2},\right.\)<br>
\(\left.\frac{n-9^{[6]}}{2},\dots,-2^{[6]},-3^{[T(n-3)+T(n-4)]}\right\}.\) (42)

2. If _n_ is even, since<tbc>

\(\sigma(\mathcal{T}(n))=\left\{2n-2,n-3^{[3]},\dots,\frac{n-2}{2},\frac{n-4^{[2]}}{2},\frac{n-8^{[3]}}{2},\dots,-2^{[3]},-3^{[T(n-3)]}\right\}\)<br>
\(\text{and}\)<br>
\(\sigma(\mathcal{T}(n-1))=\left\{2n-4,n-4^{[3]},\dots,\frac{n-4^{[3]}}{2},\frac{n-8^{[2]}}{2},\frac{n-10^{[3]}}{2},\dots,-2^{[3]},-3^{[T(n-4)]}\right\},\)<br>
\(\text{we get}\)<br>
\(\sigma(G_{1,2})=\left\{2n-2,2n-4,n-3^{[3]},n-4^{[3]},\dots,\frac{n-2^{[3]}}{2},\frac{n-4^{[5]}}{2},\frac{n-8^{[5]}}{2},\right.\)<br>
\(\left.\frac{n-10^{[3]}}{2},\dots,-2^{[6]},-3^{[T(n-3)+T(n-4)]}\right\}.\) (43)

• **Spectrum of** \(G_3^1\)**.** The connected components of the graph \(G_3^1\) are the cliques _K_<sub>1</sub>, _K_<sub>2</sub>, ..., _K_<sub>_n_-1</sub>, _K<sub>n</sub>_, _K_<sub>_n_-1</sub>, ..., _K_<sub>2</sub>, _K_<sub>1</sub>, where the adjacency matrix of each clique appears as a diagonal square submatrix of \(A(G_3^1)\). Therefore,<tbc>

\(\sigma(G_3^1)=\{n-1,n-2^{[2]},\dots,1^{[2]},0^{[2]},-1^{[(n-1)^2]}\}.\) \(\text{(44)}\)

• **Spectrum of** \(G_{3,H}^2\) which is equal to the **spectrum of** \(G_{3,V}^2\)**.** Colouring the vertices of \(G_1\cong\mathcal{T}(n)\) and \(G_2\cong\mathcal{T}(n-1)\) as described in Theorem 4.2- (2b), the connected components \(G_{3,H}^2\) and \(G_{3,V}^2\) are formed by the remain ing edges of Q(_n_), that is, \(E(\mathcal{Q}(n))\unknown(E(G_{2,3})\cup E(G_3^1))\), which are edges between blue and red vertices. These remaining edges can be partitioned into the horizontal edges \((E(G_{3,H}^2))\) and vertical edges \((E(G_{3,V}^2))\). Then, the connected components of a graph \(G_{3,X}^2\), for each \(X\in\{H,V\}\), are the complete bipartite graphs _K<sub>i,n-i</sub>_ for each \(i\in\{1,2,\dots,n\}\). Therefore,<tbc>

\(\sigma(G_{3,X}^2)=\underbrace{\bigcup_{i=1}^n\sigma(K_{i,n-i})}_\text{with repetitions}\)<br>
\(=\bigcup_{i=1}^{n-1}\{\sqrt{(n-i)i},0^{[(n-1)^2+1]},-\sqrt{(n-i)i}\}.\) \(\text{(45)}\)

