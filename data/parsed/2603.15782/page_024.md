_Proof._ We need to show that \(N\bullet X\le-\alpha\). Using eq. (17) and the fact that \((v_1,\dots,v_n)\approx_{\gamma,\tau}(\tilde{v}_1,\dots,\tilde{v}_n)\), we conclude that for any \(p\in P\) we have

\(\sum_{j=1}^{\ell(p)}\|v_{p_j}-v_{p_{j-1}}\|^2\le\|v_{p_{\ell(p)}}-v_{p_0}\|^2-\frac{1}{2}\Delta T_p\bullet X\le-\frac{1}{2}\Delta\)

(using the same argument as in the proof of Theorem 22). Therefore, \(N\bullet X\le|P|\cdot\frac{2\alpha}{|P|\Delta}\cdot(-\frac{1}{2}\Delta)=-\alpha\), as desired.

By construction, matrix _N_ has at most \(O(|P|\cdot K)\le O(n\sqrt{logn})\) non-zero entries. Graphs _F_ and _D_ have maximum degree at most 2_K_, and hence \(\|N\|\le\frac{2\alpha}{|P|\Delta}(\|\mathcal{L}(F)\|+\|\mathcal{L}(D)\|)\le\frac{2\alpha}{n^{1-\Theta(\varepsilon)}\Delta}(2K+2K)\le\frac{\alpha\cdot\text{polylog}(n)}{n^{1-\Theta(\varepsilon)}}\) .

### 7.2 Wrap-up: proof of the second oracle bound

We now collect the complexity, width, and sparsity bounds for the second implementation of the reduced oracle.

**Lemma 26.** _Let_ \(\varepsilon\in[\Theta(1/logn),\Theta(1)]\)_. The oracle described above runs in_ \(O(n^{O(\varepsilon)}\cdot T_\text{maxflow}(m,m)\cdot\text{polylog}(n))\) _time and produces either a_ \(\Theta(1)\)_-balanced element cut of cost_ \(O(\alpha\sqrt{logn/\varepsilon})\) _or a valid feedback matrix with spectral norm_ \(O(\alpha\sqrt{logn}/(n^{1-\Theta(\varepsilon)}\sqrt{\varepsilon}))\)_, with probability at least_ \(1-n^{-\Theta(1)}\)_. Moreover, every feedback matrix has_ \(O(m\sqrt{logn})\) _non-zero entries._

_Proof._ Choose parameters \(\Delta=\sqrt{\varepsilon/logn}\) and \(\mu\in[\mu_0,2\mu_0]\), where \(\mu_0=6\alpha/(c'n\Delta)\), as described above. The value \(\mu\) can be chosen as a ratio _p/q_ of two polynomially-bounded integers: since \(\mu_0\ge c''/n\) for an appropriate constant \(c''>0\), take \(p=\lceil(2n/c'')\mu_0\rceil\) and \(q=\lfloor 2n/c''\rfloor\). Multiplying all finite capacities by 2_q_ makes them polynomially-bounded integers, including the capacities _w(x)/_2; after computing a flow, scale it back by 2_q_.

The oracle repeatedly runs Algorithm 4. If it terminates at line 2, Lemma 12(a) gives a \(\Theta(1)\)-balanced element cut of cost at most \(2c'n\mu=O(\alpha\sqrt{logn/\varepsilon})\). If it terminates at line 3, Lemma 22 gives a valid feedback matrix with spectral norm \(O(\mu)=O(\alpha\sqrt{logn}/(n\sqrt{\varepsilon}))\) and _O(m_) non-zero entries. Otherwise, Lemma 25 gives a valid feedback matrix with spectral norm \(\alpha n^{-1+\Theta(\varepsilon)}\text{polylog}(n)\) and \(O(n\sqrt{logn})\) non-zero entries. Since \(m=\Omega(n)\), these alternatives satisfy the width and sparsity bounds in the statement.

Each call to Algorithm 4 makes one maximum-flow call and otherwise takes _O(m_polylog(_n_)) time. The chaining procedure uses \(n^{O(\varepsilon)}\) such calls per trial. A trial succeeds with probability at least \(n^{-O(\varepsilon)}\) by the reverse Markov inequality, so running \(n^{O(\varepsilon)}logn\) independent trials in lockstep gives a valid answer with probability at least \(1-n^{-\Theta(1)}\). The total runtime is therefore \(O(n^{O(\varepsilon)}\cdot T_\text{maxflow}(m,m)\cdot\text{polylog}(n))\).

Taking \(\tau=\Theta(1)\) sufficiently small and \(\gamma=\Theta(\Delta/(K+1))=\Theta(1/logn)\) meets the hypotheses of Lemmas 22 and 25. This also gives the common parameter bounds in Theorem 11.

## 8 Acknowledgments

LLM assistance was used to derive Theorem 5 as a fast algorithm (particularly, GPT 6-Astra and Opus 5.5). However, the ideas that underly the approximation itself were human-devised, based on the "edge-wise non-expansive" line embeddings originally used in \[42, Section 3\]. LLMs were not used to derive any other results in this work.

All AI-assisted mathematical arguments were verified by the authors, who significantly revised and simplified them. The authors take full responsibility for the correctness and content of the manuscript.

