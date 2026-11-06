Although our problem is defined on an unweighted graph, our algorithm constructs several auxiliary graphs that may contain weighted edges. We denote a weighted edge from s to t in such graphs by \[s,t\] and denote its weight by \(|[s,t]|\). The degree of an edge _e_=(s,t) is deg(_e_):=min{deg(_s),_deg(t)}. For two paths P and Q where P ends at the vertex where Q starts, we denote by \(P\odot Q\) the concatenation of P and Q.

Baswana and Kavitha \[BK06\] proposed an \(\tilde{\mathcal{O}}(m\sqrt{n}+n^2)\) time algorithm for 2-APSP. We can use this result to find 2-approximate shortest paths for pairs connected entirely by low-degree vertices (degree at most \(\tilde{\mathcal{O}}(\sqrt{n})\)). To achieve this, we construct a subgraph H of G containing only vertices with degree at most \(\tilde{\mathcal{O}}(\sqrt{n})\). Note that all low-degree paths from G are preserved in H. Since the maximum degree in H is \(\tilde{\mathcal{O}}(\sqrt{n})\), the number of edges in H is at most \(\tilde{\mathcal{O}}(n\sqrt{n})\). Applying the algorithm from \[BK06\] to H takes \(\tilde{\mathcal{O}}(n^2)\) overall time. We therefore assume the following for the rest of the paper.

**Assumption 3.1.** _The shortest_ st _path contains at least one vertex with degree_ \(\ge\tilde{\mathcal{O}}(\sqrt{n})\).

In our paper we use the algorithm of Gupta \[Gup25\]. We now introduce some notations from it.

**Definition 3.2** (Nested Vertex Sampling)**.** _Let_ A<sub>0</sub>=V_. Let_ A<sub>1</sub> _be the set of vertices sampled from_ A<sub>0</sub> _with probability_ \(\frac{1}{2^{2^\mathrm{i}}}\)_. For each_ \(2\le\mathrm{i}\le\mathrm{loglog}n-1\), A<sub>i</sub> _is sampled from_ A<sub>i-1</sub> _with probability_ \(\frac{1}{2^{2^{\mathrm{i}-1}}}\).

One can show that \(|A_\mathrm{i}|=\tilde{\mathcal{O}}(\frac{n}{2^{2^\mathrm{i}}})\) with high probability. We now move on to the other notations used in \[Gup25\].

**Definition 3.3** (Pivots, Balls and Clusters)**.** _For each_ \(s\in\mathsf{V}\)_, let_ pivot<sub>i</sub>(s) _denote the vertex in_ A<sub>i</sub> _closest to s in_ G_, breaking ties arbitrarily. Let_ ball<sub>i</sub>(s) _be the set of vertices strictly closer to s than_ pivot<sub>i</sub>(s)_. Formally,_

\(\mathrm{ball}_\mathrm{i}(s)=\{v|\mathrm{s}v|<|\mathrm{spivot}_\mathrm{i}(s)|\}\)

_For each_ \(v\in\mathsf{V}\)_, let_ cluster<sub>i</sub>(v) _be the set of vertices whose ball contains v. Formally,_

\(\mathrm{cluster}_\mathrm{i}(v)=\{s|v\in\mathrm{ball}_\mathrm{i}(s)\}\)

We now state the following lemma in \[Gup25\] which bounds the size of balls.

**Lemma 3.4** (\[Gup25\])**.** _For each_ \(0\le\mathrm{i}\le\mathrm{loglog}n-1\) _and each_ \(s\in\mathsf{V}\), \(|\mathrm{ball}_\mathrm{i}(s)|=\tilde{\mathcal{O}}(2^{2^\mathrm{i}})\) _with a high probability. Moreover, we can compute the following in_ \(\tilde{\mathcal{O}}(n^2)\) _time with a high probability:_

1. pivot<sub>i</sub>(s) _and its distance from s for all_ \(s\in\mathsf{V}\)_. So,_ est(s,pivot<sub>i</sub>(s))=|spivot<sub>i</sub>(s)|.<tbc>

_2._ ball<sub>i</sub>(s) _for all_ i _and_ \(s\in\mathsf{V}\)_. Moreover,_ est(s,v)=|sv| _for each_ \(v\in\mathrm{ball}_\mathrm{i}(s)\).

The above lemma bounds the number of vertices in ball<sub>i</sub>(s). Furthermore, for each i and s, we can efficiently compute pivot<sub>i</sub>(s) and ball<sub>i</sub>(s). Additionally, we can compute the length of the shortest path from s to each vertex in ball<sub>i</sub>(s).

The above lemma also allows us to compute clusters, but it does not bound their size. The work \[Gup25\] does not use clusters. In contrast, our algorithm uses clusters crucially and requires a bound on the cluster size. However, nested vertex sampling does not guarantee bounded cluster size. To address this issue, we adapt a result of Thorup and Zwick \[TZ01\].

**Lemma 3.5.** _Fix an integer_ \(\alpha\) _where_ \(1\le\alpha\le\mathrm{loglog}n-1\)_. There is a randomised algorithm that finds a set_ \(A_\alpha\) _such that with high probability_

1. \(|A_\alpha|=\tilde{\mathcal{O}}(\frac{n}{2^{2\alpha}})\)<tbc>

