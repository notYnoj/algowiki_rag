## A Expander Graphs and Spectral Expansion

**Lemma A.1** (Expander mixing lemma for bipartite graphs \[Hae95\])**.** _Let_ \(G=(L\cup R,E)\) _be a d-regular bipartite graph such that_ |_L_|=|_R_|=_n. Then, for all sets_ \(S\subseteq L\) _and_ \(T\subseteq R\)_, it holds that_

\(\left|e(S,T)-\frac{d}{n}\cdot|S|\cdot|T|\right|\le\lambda_2(G)\cdot d\cdot\sqrt{|S|\cdot|T|},\)

_where_ \(\lambda_2(G)\) _is defined as the second largest eigenvalue of the normalized adjacency matrix A of G. In other words, A is the adjacency matrix of G multiplied by_ 1_/d; let_ \(\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_{2n}\) _be the eigenvalues of A, then_ \(\lambda_2(G):=\lambda_2\)_. The eigenvalue_ \(\lambda_2(G)\in(1/d,1)\) _is also called the spectral expansion of the bipartite graph G._

## B Summary and Improvement of Koucký and Král \[KK21\]

Koucký and Kràl show a circuit that sorts _n_ integers each is _k_-bit (without payload), taking circuit size _O(nk_<sup>2</sup>) and depth _O_(log_n+k_log_k_). In this section, we improve the circuit depth to _O_(log_n+k_) (with the same circuit size).

If \(k=\Omega(logn)\), then the standard AKS sorting network \[AKS83\] is applied to _n_ integers directly: recall that the depth of AKS is _O(k_+log_n_) using the pipelining technique in Fact 15.5 while the circuit size is still _O(kn_log_n_).

For \(k\le 0.1\cdot logn\), Koucký and Kràl takes a counting approach as below (for readability, integer rounding is omitted).

