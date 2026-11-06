Generalizing Brooks’ theorem via Partial Coloring is Hard Classically and Locally

**Abstract**

We investigate the classical and distributed complexity of _k-partial c-coloring_ where _c=k_, a natural generalization of Brooks’ theorem where each vertex should be colored from the palette {1_,...,c_}={1_,...,k_} such that it must have at least min{_k,_deg(_v_)} neighbors colored differently. Das, Fraigniaud, and Rosén [OPODIS 2023] showed that the problem of _k_-partial (_k_+1)-coloring admits efficient centralized and distributed algorithms and posed an open problem about the status of the distributed complexity of _k_-partial _k_-coloring. We show that the problem becomes significantly harder when the number of colors is reduced from _k_+1 to _k_ for every constant \(k\ge 3\).

In the classical setting, we prove that deciding whether a graph admits a _k_-partial _k_-coloring is NP-complete for every constant \(k\ge 3\), revealing a sharp contrast with the linear-time solvable (_k_+1)-color case. For the distributed LOCAL model, we establish an \(\Omega(n)\)-round lower bound for computing _k_-partial _k_-colorings, even when the graph is guaranteed to be _k_-partial _k_-colorable. This demonstrates an exponential separation from the \(O(log^2k\cdot logn)\)-round algorithms known for (_k_+1)-colorings.

Our results leverage novel structural characterizations of "hard instances" where partial coloring reduces to proper coloring, and we construct intricate graph gadgets to prove lower bounds via indistinguishability arguments.

<sup>∗</sup>Department of Algebra, Faculty of Mathematics and Physics, Charles University. Email: `jan.bok@matfyz.cuni.cz`. Website: `https://janbok.github.io`. ORCID id: `https://orcid.org/ 0000-0002-7973-1361`. Supported by the European Union (ERC, POCOCOP, 101071674). Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them. <sup>†</sup>Department of Computer Science, Aalto University. Email: `avinandan.das@aalto.fi`. This work was supported in part by the Research Council of Finland, Grant 363558. <sup>‡</sup>MTA–HUN-REN RI Lendület "Momentum" Arithmetic Combinatorics Research Group, HUN-REN Alfréd Rényi Institute of Mathematics, Budapest, Hungary. Email: `gujgicza@renyi.hu`. Website: `https://cs.bme.hu/\protect\ unhbox\voidb@x\protect\penalty\@M\{\}}gujgicza/`. Supported by the Lendület "Momentum" program of the Hungarian Academy of Sciences (MTA). <sup>§</sup>Department of Applied Mathematics, Faculty of Mathematics and Physics, Charles University. Department of Algebra, Faculty of Mathematics and Physics, Charles University. Email: `jedlickova@kam.mff.cuni.cz`. ORCID id: `https://orcid.org/0000-0001-9518-6386`. Supported by the research grants PRIMUS/24/SCI/008, UNCE/24/SCI/022 of Charles University, and SVV–2025–260822.

Jan Bok<sup>∗</sup> Avinandan Das<sup>†</sup> Anna Gujgiczer<sup>‡</sup> Nikola Jedličková§

arXiv:2508.16308v1 [cs.DC] 22 Aug 2025

