## Acknowledgments and Methodology

### How the result was originally found and shared with the authors.

An Anthropic employee used an internal research model to investigate open problems in the theory of cryptography. One of them was about cryptographic constructions based on the average-case hardness of Zero-_k_-Clique [LLV19, AHY25]. Claude was tasked with verifying and improving the constructions, but instead developed this algorithm, first for the average case, then for the worst case. The session used 16M output tokens with no human input.

Anthropic shared the algorithm with the authors in September 2026 under a confidentiality agreement, offered compensation, and provided access to the public version of Claude.

### Shared algorithm.

The algorithm that was shared with the authors is essentially the algorithm in Section 2, although presented differently and with other numerical parameters. A different reduction from Exact Triangle to the problem of Section 2 was also shared, although the authors did not include it here, and instead used known reductions to All-Edges Sparse Triangle, which suffice and strengthen the connection. The authors derived the data structure version in Section 4 and its connection with Hinted OMv.

### Lean certification.

After the paper was completely written, Anthropic used an internal research model to certify this paper’s main results using the Lean 4 proof assistant with the Math- lib library. The formalization is available at `https://github.com/anthropics/formal-math/ tree/main/3sum-apsp`. The following are formalized there: Theorem 19 (Exact Triangle in _O(n_<sup>2.9983</sup>) time), Theorem 22 (3SUM in _O(n_<sup>1.9992</sup>) time, and the (min,+)-product and APSP in _O(n_<sup>2.99942</sup>) time), and the Zero-Weight case of Corollary 39 (Zero-Weight _k_-Clique in \(O(n^{k-0.0017\lfloor k/3\rfloor})\) time for every \(k\ge 3\)). All lemmas and prior results that these statements rely on are also formalized there.

### Further acknowledgments.

The authors used Claude to help with writing, figure creation, and checking mathematical details throughout this project. They have attempted to make the entire paper accessible and well-written, and take full responsibility for its contents.

The authors’ contribution to this publication was done in their individual capacities, not in connection with their duties or responsibilities to Columbia University or to MIT. Any opinions expressed in this work are opinions of the authors; they are not official positions or endorsements of Columbia University or of MIT, and do not represent the research of the authors at Columbia University or MIT.

## References

