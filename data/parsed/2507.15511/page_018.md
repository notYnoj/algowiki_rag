runtime. The results help explain why many real-world instances are easier, why SETH-based reductions can be structurally brittle, and how instance complexity can be made constructive.

### Algorithmic Advance.

IC-SubsetSum delivers a set of guarantees that advance the state of the art:

• **Certificate-sensitive runtime.** A deterministic worst-case bound of \(O(U\cdot n^2)\) and an expected randomized bound of \(O(U\cdot n)\), realizing a constructive link to Instance Complexity by tying performance to the certificate size _U_, which is discovered _online_ in an _anytime_ fashion.<tbc>

• **Worst-case improvement.** Via Controlled Aliasing under count-based canonical normalization (CNF) at the alias indices, a deterministic bound of \(O^*(2^{n/2-\varepsilon})\) with \(\varepsilon=log_2(\frac{4}{3})\approx 0.415\), improving on the classical _O_<sup>∗</sup>(2<sup>_n/_2</sup>) Horowitz-Sahni bound for all sufficiently large _n_.<tbc>

• **Real-time certificate generation.** Online construction of the constructive certificate, storing the lex-minimal witness for each \(\sigma\in\Sigma(S)\) without duplication.

Closing the gap between the deterministic and randomized bounds remains a key open challenge, as does the question of whether an \(\tilde{O}(U)\) runtime is achievable.<sup>1</sup>

## References

<sup>1</sup>May all your programs be short and quick (Fortnow \[For04\]) and may their runtimes reveal the structure within.

