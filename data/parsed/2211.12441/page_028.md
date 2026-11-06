_Proof._ By taking the majority vote of multiple independent runs and a standard analysis, e.g, based on Chernoff bounds, we have that \(\mathrm{RQ}_\varepsilon(\Pi)=O(\mathrm{log}(1/\varepsilon))\mathrm{RQ}_{1/3}(\Pi)\) for any \(\varepsilon\le 1/3\). Combining this with Lemma 39 and Proposition 41, we have:<tbc>

\(\mathrm{RQ}_{1/3}(\Pi)=\Omega\left(\frac{\mathrm{RQ}_\varepsilon(\Pi)}{\mathrm{log}(1/\varepsilon)}\right)=\Omega\left(\frac{\mathrm{Dist}\mathrm{Q}_{2\varepsilon}(\Pi)}{\mathrm{log}(1/\varepsilon)}\right)=\Omega\left(\frac{\mathrm{log}(g(s+1-4(n-1)\varepsilon)/n)}{\mathrm{log}(1/\varepsilon)}\right).\)

<tbc>Setting \(\varepsilon\) such that \(4n\varepsilon=s/2\) yields<tbc>

\(\mathrm{RQ}_{1/3}(\Pi)=\Omega\left(\frac{\mathrm{log}(g(s/2+1)/n)}{\mathrm{log}(8n/s)}\right).\)

<tbc>Picking \(g(x)=\Gamma(x+1)\) and using the fact that \(\Gamma(x)\ge\sqrt{2\pi x}\left(\frac{x}{e}\right)^x\), we obtain

\(\mathrm{RQ}_{1/3}(\Pi)=\Omega\left(\frac{(s/2)\mathrm{log}(s/(2e))-\mathrm{log}n}{\mathrm{log}(8n/s)}\right)=\Omega\left(\frac{s\mathrm{log}s}{\mathrm{log}(2n/s)}\right),\)

where the simplification can be verified by considering the cases of large _s_ (say \(s\ge\sqrt{n}\)) and small _s_ separately.

We can apply Lemma 42 to the sensitivity lower bounds of Lemma 21 and produce randomized lower bounds for inversion minimization on bounded-degree trees. Using Fact 25 we obtain:

**Theorem 43 (lower bound against bounded-error for inversion minimization on trees).** _Let T be a tree with_ \(\mathrm{deg}(T)\le k\)_. The query complexity of_ \(\Pi_T\) _for bounded-error randomized algorithms is_ \(\Omega(\frac{n\mathrm{log}(n/k)}{k\mathrm{log}(k)})\).

## 7 Connectivity Lemma

In this section we establish Lemma 16 and use it to present some of the known lower bounds in a unified framework. We actually prove the following somewhat stronger result.

**Lemma 44 (Strong Connectivity Lemma).** _Consider an algorithm A in the comparison-based model, color each vertex of the permutahedron with its execution trace under A, and let H denote the subgraph with the same vertex set but only containing the monochromatic edges. The number of distinct execution traces of A equals the number of connected components of H._

The Connectivity Lemma follows from Lemma 44 because the coloring with execution traces of an algorithm _A_ for \(\Pi\) is a refinement of the coloring with \(\Pi\). Note that the counterpart of Lemma 44 in the Boolean setting is trivial. This is because an execution trace in the Boolean setting is specified by values for a subset of the input bits, so the set of inputs that follow a particular execution trace form a subcube of the hypercube, the Boolean counterpart of the permutahedron. Subcubes are trivially connected inside the hypercube. In the comparison-query model, the sets of inputs that follow a particular execution trace can be more complicated, and their connectedness is no longer trivial but still holds.

_Proof of Lemma 44._ Two rankings \(\rho_1\) and \(\rho_2\) that have distinct execution traces under _A_ cannot be connected because any path between them needs to contain at least one bichromatic edge. For<tbc>

