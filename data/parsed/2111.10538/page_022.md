Using standard Chernoff bound, we have with probability 0.99,<tbc>

\(|V(\mathsf{NF}_\lambda)|\le 2\mathbb{E}[|V(\mathsf{NF}_\lambda)|]=k^{\gamma/4}/2.\)

<tbc>In the rest of this proof, we show that with probability 0.99,

\(|E(\mathsf{NF}_\lambda)|\ge k^{\gamma/2-\beta}/128,\)

and then the claim follows.

It is known that any graph can be made bipartite by removing at most half of its edges \[Wes01\]. Thus, for the sake of this proof, we only consider a bipartite subgraph of \(\mathsf{NG}_\lambda\) with parts P and Q that contains at least \(k^{2-\beta}/2\) edges. We refer to this graph by \(\widehat{\mathsf{NG}_\lambda}\). We consider a two-step construction of \(\widehat{\mathsf{NF}_\lambda}\) based on sampling in \(\widehat{\mathsf{NG}_\lambda}\), where we first only sub-sample the vertices on the P-side, and then also sub-sample the vertices on the Q-side. Let \(\widehat{\mathsf{NF}_\lambda}(\mathcal{P})\) denote the graph after subsampling only the P-side, and \(V(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}),\mathcal{P})\) denote the set of vertices in \(\widehat{\mathsf{NF}_\lambda}\) on the P-side.

The number of edges in \(\widehat{\mathsf{NF}_\lambda}(\mathcal{P})\) is the sum of degrees of surviving P-vertices, aka a sum of i.i.d. random variables bounded in \[0_,k_\]. It’s expectation is given by:<tbc>

\(\mathbb{E}[|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|]=p|E(\widehat{\mathsf{NG}_\lambda}(\mathcal{P}))|\ge k^{2-\beta}/2,\)

<tbc>and by Hoeffding’s inequality this sum concentrates around its expectation with high probability:

\(\mathrm{Pr}\left[|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|\le pk^{2-\beta}/4\right]\le\mathrm{Pr}\left[|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|\le\mathbb{E}[|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|]-pk^{2-\beta}/4\right]\)<br>
\(\le\mathrm{exp}\left(-\frac{2|\mathcal{P}|^2p^2k^{4-2\beta}/16}{|\mathcal{P}|k^2}\right)\)<br>
\(\le\mathrm{exp}\left(-\Theta\left(k^{\gamma/2-2\beta}\right)\right).\text{By}|P|\ge 1\)

By Chernoff bound,<tbc>

\(\mathrm{Pr}[|V(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}),\mathcal{P})|>2pk]\le[|V(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}),\mathcal{P})|>2p|\mathcal{P}|]\le\mathrm{exp}\left(-p|\mathcal{P}|/3\right)\le\mathrm{exp}(-\Theta(k^{\gamma/4-\beta})),\)

<tbc>where the last inequality is obtained by \(|\mathcal{P}|\le k\). We henceforth fix any realization of \(\widehat{\mathsf{NF}_\lambda}(\mathcal{P})\) conditioned on<tbc>

\(|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|\ge pk^{2-\beta}/4\text{and}|V(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}),\mathcal{P})|\le 2pk.\)

<tbc>We now consider the second step of the sub-sampling, which transforms \(\widehat{\mathsf{NF}_\lambda}(\mathcal{P})\) to \(\widehat{\mathsf{NF}_\lambda}\). The expected number of edges in \(\widehat{\mathsf{NF}_\lambda}\) satisfies:<tbc>

\(\mathbb{E}[|E(\widehat{\mathsf{NF}_\lambda})|]=p|E(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}))|\ge p^2k^{2-\beta}/4=k^{\gamma/2-\beta}/64.\)

<tbc>We now argue about concentration. Notice that the degree of each vertex in \(\widehat{\mathsf{NF}_\lambda}(\mathcal{Q})\) is at most the number of vertices on P-side in \(\widehat{\mathsf{NF}_\lambda}(\mathcal{P})\) is at most \(|V(\widehat{\mathsf{NF}_\lambda}(\mathcal{P}),\mathcal{P})|\le 2pk\). Therefore, by Hoeffding’s inequality,

\(\mathrm{Pr}\left[|E(\widehat{\mathsf{NF}_\lambda})|<k^{\gamma/2-\beta}/128\right]\le\mathrm{Pr}\left[|E(\widehat{\mathsf{NF}_\lambda})|<\mathbb{E}[|E(\widehat{\mathsf{NF}_\lambda})|]-k^{\gamma/2-\beta}/128\right]\)<br>
\(\le\mathrm{exp}\left(-\Theta\left(\frac{|\mathcal{Q}|^2k^{\gamma-2\beta}}{|\mathcal{Q}|p^2k^2}\right)\right)\)<br>
\(\le\mathrm{exp}\left(-\Theta\left(k^{\gamma/2-2\beta}\right)\right)\text{By}|Q|\ge 1.\)

By taking a union bound on the low probability events and the fact that \(E(\widehat{\mathsf{NF}_\lambda})\) is a subset of \(E(\mathsf{NF}_\lambda)\), we have \(|E(\mathsf{NF}_\lambda)|\ge k^{\gamma/2-\beta}/128\).

