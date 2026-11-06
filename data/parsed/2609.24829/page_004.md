## 1.1 Our Results and Technical Overview

Our main result is an _O(p_)-pass parameter-free triangle counting algorithm in the random-order streaming model for any \(p\le\lceil loglog(n)\rceil\). That is, we prove the following.

**Theorem 1.1** (Main Result, informal)**.** _Let S be a stream of edges (in random order) representing a simple graph G with n vertices, m edges, and T triangles. Then there exists an O(p_) _pass algorithm that uses expected_ \(\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(\frac{m+T}{\sqrt{T}}\right)\right)\) _space, and with probability_ \(1-\delta-1/poly(n)\) _outputs_ \(\widehat{T}\)_, an approximation of T, with_

\(T\le\widehat{T}\le(1+\varepsilon)T+\widetilde{O}(n^{1/2^p}).\)

_The algorithm does not require any prior knowledge of T._

If _T\<m_, the space bound simplifies to \(\widetilde{O}\left(\delta^{-1}\varepsilon^{-3.5}\left(m/\sqrt{T}\right)\right)\). When \(p=\lceil loglog(n)\rceil\), a simple modification gives a \(1+\varepsilon\) approximation \(\widehat{T}\) to _T_, with no additive error.

### Mixed approximation bound.

We refer to the type of approximation result given as a _mixed approximation_ bound. More generally, we say that _X_ is an \((\alpha,\beta)\) approximation of _T_ if \(T\le X\le\alpha T+\beta\). Our main result is, therefore, an \((1+\varepsilon,\widetilde{O}(n^{1/2^p}))\) mixed approximation of _T_ with an _O(p_) pass parameter-free algorithm, and a \((1+\varepsilon,0)\) approximation in _O_(loglog(_n_)) passes.

### Verified triangle counting.

A key building block of our algorithm is a _verified_ triangle counting subroutine, which we develop by modifying the algorithm of McGregor and Vorotnikova \[MV20\]. All prior triangle counting algorithms take a parameter \(\tau\) intended to be a lower bound on _T_ and produce an estimate without any guarantee of correctness if \(\tau\) is not actually a lower bound. Our verified subroutine, by contrast, either outputs a \((1\pm\varepsilon)\) approximation of _T_ when \(T\ge\tau\), or outputs `FAIL` when \(T<\tau\) (with high probability). This verification property is crucial: it allows us to search over possible values of \(\tau\) across passes without fear of silently returning an incorrect estimate, as each invocation either certifies its own output or explicitly declares failure. We define this result in Section 3 with additional details in Section A.

### Stream segmentation and the one-pass result.

A naïve approach to parameter-free counting would geometrically decrease a guess \(\tau_i\) by a constant factor in each pass, starting from _m_<sup>3/2</sup>. This requires _O_(log_n_) passes, and reducing the pass count further by using a larger factor comes at a steep cost in space. To circumvent this, we observe that a randomly ordered stream of _m_ edges can be partitioned into _O_(log_n_) contiguous segments, each of which behaves statistically like an independent uniform sample of the edges. Provided the maximum per-edge triangle participation \(\Delta_e\) is not too large, each segment is _representative_: its triangle count is a \((1\pm\varepsilon)\) fraction of the expected value. This allows us to run _O_(log_n_) geometrically spaced guesses for \(\tau\) across the segments of a _single pass_, rather than across separate passes. The result is a one-pass algorithm that either produces a \((1\pm\varepsilon)\) approximation of _T_, or certifies that \(T=\widetilde{O}(n)\). We discuss this result in Section 3.3 with more details in the subsequent section.

### Heavy and light edges, _O(p_) pass and _O_(loglog_n_)-pass algorithms.

When designing sampling based _parametrized_ triangle counting algorithms, the parameter \(\tau\) is used to separate the edges in the graph to _heavy_ and _light_, where heavy roughly corresponds to edges participating in \(\sqrt{\tau}\) triangles. This separation, and the assumption that \(\tau\) is a good approximation of _T_, allow one to set sampling probabilities and approximate the triangles with or without heavy edges separately. We bypass the need for a parameter \(\tau\) by _adaptively_ setting a heaviness threshold \(\gamma\) according to the certificate provided by the verified algorithm in a previous pass. If the one-pass algorithm did not return an estimate, we have established that \(T=\widetilde{O}(n)\), allowing a<tbc>

