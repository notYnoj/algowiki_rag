<tbc>Assume that \(\gamma\le|\mathrm{TRUECLOSE}(\mathrm{p}_\mathrm{s})|\le 2\gamma\) where \(\gamma\in\{\mathrm{n}^{0.875},2\mathrm{n}^{0.875},2^2\mathrm{n}^{0.875},\dots\}\). In Algorithm 4, we sample a set \(\mathrm{L}_\gamma\) of size \(\tilde{\mathrm{O}}(\frac{\mathrm{n}}{\gamma})\). With high probability at least one vertex of \(\mathrm{L}_\gamma\) lies in TRUECLOSE(p<sub>s</sub>). Without loss of generality, let this vertex be z. In UPDATEFROM(z), our algorithm computes the shortest path from z to every other vertex in \(\mathrm{G}(\gamma)\). We want \(\mathrm{G}(\gamma)\) to contain both the shortest path p<sub>s</sub>z and the st path (See Figure 4). This condition ensures a good approximation of the st distance when we use the distance product. We now prove this property.

**Lemma 4.7.** \(\mathrm{G}(\gamma)\) _contains the_ p<sub>s</sub>z _path._

_Proof._ Recall that \(|\mathrm{TRUECLOSE}(\mathrm{p}_\mathrm{s})|\le 2\gamma\) and that TRUECLOSE(p<sub>s</sub>) contains all vertices within distance 2c+1 from p<sub>s</sub>. Hence, every vertex at distance strictly less than 2c+1 from p<sub>s</sub> has degree at most \(2\gamma\), since its degree is bounded by |TRUECLOSE(p<sub>s</sub>)|. Therefore, every vertex on the p<sub>s</sub>z path, except possibly z, has degree at most \(2\gamma\). In the construction of \(\mathrm{G}(\gamma)\), we add all edges whose degree is at most \(\tilde{\mathrm{O}}(\gamma)\). Thus, \(\mathrm{G}(\gamma)\) contains the entire p<sub>s</sub>z path.

**Lemma 4.8.** \(\mathrm{G}(\gamma)\) _contains the_ st _path._

_Proof._ We show that sp<sub>s</sub>, p<sub>s</sub>p<sub>t</sub> and p<sub>t</sub>t lie in \(\mathrm{G}(\gamma)\). This will imply that st lies in \(\mathrm{G}(\gamma)\).

1. p<sub>s</sub>p<sub>t</sub> lies in \(\mathrm{G}(\gamma)\)<tbc>

<tbc>By Theorem 4.4, \(|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|\le\mathrm{c}\). By Theorem 2.1, \(\mathrm{est}(\mathrm{p}_\mathrm{s},\mathrm{p}_\mathrm{t})\le 2|\mathrm{p}_\mathrm{s}\mathrm{p}_\mathrm{t}|+1\le 2\mathrm{c}+1\), so \(\mathrm{p}_\mathrm{t}\in\mathrm{ESTIMATEDCLOSE}(\mathrm{p}_\mathrm{s})\). Using Theorem 4.6, we obtain \(\mathrm{p}_\mathrm{t}\in\mathrm{TRUECLOSE}(\mathrm{p}_\mathrm{s})\).<tbc>

<tbc>Each vertex on the p<sub>s</sub>p<sub>t</sub> path, except possibly p<sub>t</sub>, has degree at most \(2\gamma\), since otherwise \(|\mathrm{TRUECLOSE}(\mathrm{p}_\mathrm{s})|\ge 2\gamma\). Thus, the degree of every edge on the p<sub>s</sub>p<sub>t</sub> path is at most \(\tilde{\mathrm{O}}(\gamma)\) and the entire path lies in \(\mathrm{G}(\gamma)\).<tbc>

2. sp<sub>s</sub> and p<sub>t</sub>t lie in \(\mathrm{G}(\gamma)\)<tbc>

<tbc>Using Theorem 3.9, every edge on the sp<sub>s</sub> and tp<sub>t</sub> paths has degree at most \(\tilde{\mathrm{O}}(2^{2^\alpha})=\tilde{\mathrm{O}}(2^{2^{\mathrm{loglog}\mathrm{n}-4}})=\tilde{\mathrm{O}}(\mathrm{n}^{0.0625})<\tilde{\mathrm{O}}(\mathrm{n}^{0.875})\le\tilde{\mathrm{O}}(\gamma)\). Hence, the paths sp<sub>s</sub> and tp<sub>t</sub> also lie in \(\mathrm{G}(\gamma)\).

Thus, the entire st path lies in \(\mathrm{G}(\gamma)\).

Since we compute the shortest path from z to all other vertices in \(\mathrm{G}(\gamma)\), we obtain a good estimate of est(s,z) and est(z,t) after completing \(\mathrm{UPDATEFROM}(z,\gamma)\). We prove the following.

**Lemma 4.9.** \(\mathrm{est}(\mathrm{s},\mathrm{z})\le|\mathrm{sp}_\mathrm{s}|+2\mathrm{c}+1\) _and_ \(\mathrm{est}(\mathrm{z},\mathrm{t})\le|\mathrm{p}_\mathrm{st}|+2\mathrm{c}+1\) _after executing_ \(\mathrm{UPDATEFROM}(z,\gamma)\).

TRUECLOSE(ps)
z
distance = 2c + 1
s
ps
Pt
t

Figure 4: The figure illustrates the scenario discussed in this section. The vertex p<sub>t</sub> lies in TRUECLOSE(p<sub>s</sub>). Moreover, there exists a sampled vertex \(z\in\mathrm{L}_\gamma\) that also lies in TRUECLOSE(p<sub>s</sub>).

