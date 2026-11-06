Consider an optimization problem with input space I, output space O, and evaluation map \(e:\mathcal{I}\times\mathcal{O}\rightarrow[0,1]\). A deterministic \((1-\varepsilon)\)-approximation algorithm \(\mathcal{A}:\mathcal{I}\rightarrow\mathcal{O}\) satisfies \(e(x,\mathcal{A}(x))\in[1-\varepsilon,1]\) for every _x_. Attaching the input to the output, \(\tilde{\mathcal{A}}(x)=(x,\mathcal{A}(x))\), yields the diagram

\(\mathcal{I}-\rightarrow^\tilde{\mathcal{A}}\mathcal{I}\times\mathcal{O}-\rightarrow^e[1-\varepsilon,1].\)

The sensitivity of A is the maximum, over neighboring inputs \(x\sim x'\), of the distance between \(\tilde{\mathcal{A}}(x)\) and \(\tilde{\mathcal{A}}(x')\) inside \(\mathcal{I}\times\mathcal{O}\). To derive a lower bound we therefore search for neighboring inputs that force any \((1-\varepsilon)\)-approximation algorithm to output points that are well separated for at least two inputs in \(\mathcal{I}\times\mathcal{O}\), mirroring the coding-theoretic requirement that distinct messages map to distant codewords.

Now replace the algorithm by a systematic LTC _C_ with an encoder _f_. Let _n_ be the block length, _k_ be the message length, \(\delta\) be the relative distance, and _T_ be the tester with detection probability \(\kappa\). Then, define _e(x_)=**Pr**\[_T_ accepts _x_\]. Every codeword _f(m_) for a message _m_ satisfies _e(m,f(m_))=1, so we obtain the analogous diagram

\(\Sigma^k-\rightarrow^f\Sigma^k\times\Sigma^{n-k}-\rightarrow^e\{1\}.\)

Because the code has relative distance \(\delta\), distinct messages map to codewords whose relative Hamming distance is at least \(\delta\), mirroring the separation requirement for optimization algorithms.

To reason about approximate outputs we invoke strong testability. Think of _f_ as an exact algorithm that always attains the optimum 1 of _e_. If another encoder B satisfies \(e(m,\mathcal{B}(m))\ge 1-\varepsilon\), strong testability guarantees that \(\tilde{\mathcal{B}}(m)\) lies within distance \(\varepsilon/\kappa\) of some codeword. Consequently we get the diagram

\(\Sigma^k-\rightarrow^\tilde{\mathcal{B}}\Sigma^k\times\Sigma^{n-k}-\rightarrow^e[1-\varepsilon,1].\)

The distance between the codewords of neighboring messages \(m\sim m'\) therefore forces a comparable separation between \(\tilde{\mathcal{B}}(m)\) and \(\tilde{\mathcal{B}}(m')\), yielding the desired sensitivity lower bound.

The systematic nature of the code is crucial: it embeds the message directly into the codeword, so the tester _T_ enforces consistency between input and output rather than merely checking membership in the code.

## Any approximate encoder has high sensitivity.

With this analogy in place we outline how to prove the sensitivity lower bound for approximation algorithms on the induced CSP, thereby establishing Theorem 1.1. Fix a randomized \((1-\varepsilon)\)-approximation algorithm A for MaxCSP(_C_). Given a message _m_, we construct a CSP instance I_<sub>C</sub>(m_) that is satisfiable exactly by the codeword for _m_, and strong testability ensures that the output of \(\tilde{\mathcal{A}}\) on I_<sub>C</sub>(m_) lies within Hamming distance \(\varepsilon/\kappa\) of that codeword. Hence we may view \(\tilde{\mathcal{A}}\) as an approximate encoder that attempts to extend _m_. To force large sensitivity we must find neighboring messages \(m\sim m'\) whose outputs fall into balls centred at different codewords. To this end we introduce the nearest-message decoder \(\sigma:\Sigma^n\rightarrow\Sigma^k\) and show that for some \(m\sim m'\) the values \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\sigma\circ\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\) differ with constant probability; by the code’s relative distance this forces \(\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\) to have large earth mover’s distance.

However, it is not enough to focus on a single pair \(m\sim m'\): the encoder \(\tilde{\mathcal{A}}\) might always output the codeword for _m_, achieving zero sensitivity while staying nearly optimal for _m_ and \(m'\). Instead we average over all such pairs. For any approximate encoder \(\tilde{\mathcal{A}}\) we define a functional _L_ that averages the earth mover’s distance between \(\tilde{\mathcal{A}}(\mathcal{I}_C(m))\) and \(\tilde{\mathcal{A}}(\mathcal{I}_C(m'))\) across all \(m\sim m'\). This functional lower bounds the worst-case sensitivity and, more strongly, the average sensitivity under uniformly random constraint deletions.

