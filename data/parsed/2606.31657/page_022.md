Multiplying by the blocklength _n=tk_ converts the normalized Hamming metric to the unnormalized one used in the sensitivity definition, so the resulting Max Cut instance witnesses worst-case sensitivity at least

\(\frac{t}{d}\left(1-\frac{2(t+k)\varepsilon}{\kappa}\right)-\frac{1}{d}.\) (5)

The expression inside the parentheses is positive whenever \(\varepsilon\le\kappa/(2(t+k))\). Since any algorithm has sensitivity at most _n_, the range \(\varepsilon<1/n\) is already covered by the \(\Omega(n)\) lower bound for bipartite 2-coloring \[45\]; we therefore focus on \(1/n\le\varepsilon\le\kappa/(8\sqrt{n})\).

Fix an even integer<tbc>

\(t:=2\left\lfloor\frac{\kappa}{16\varepsilon}\right\rfloor,\)

<tbc>so that \(\kappa/(8\varepsilon)-2\le t\le\kappa/(8\varepsilon)\), and let \(k:=\lceil n/t\rceil\). If _t_ does not divide _n_, pad with at most _t_ dummy constraints so that the blocklength becomes \(tk\in[n,n+t]\); since \(t\le(\kappa/8)n\) when \(\varepsilon\ge 1/n\), this increases _n_ by at most a constant factor, and we continue to denote the new blocklength by _n_ (the upper bound \(\varepsilon\le\kappa/(8\sqrt{n})\) may shrink by an absolute constant, which we absorb into the choice of 8). For sufficiently large _n_ (say \(n\ge 16\)) the assumption \(\varepsilon\le\kappa/(8\sqrt{n})\) gives \(\varepsilon\le\kappa/32\) and \(n\varepsilon^2\le\kappa^2/64\), whence<tbc>

\(t\varepsilon\le\frac{\kappa}{8}\text{and}k\varepsilon\le\varepsilon+\frac{n\varepsilon^2}{\kappa/8-2\varepsilon}\le\frac{\kappa}{32}+\frac{\kappa^2/64}{\kappa/16}=\frac{9\kappa}{32}.\)

<tbc>Consequently \((t+k)\varepsilon\le 13\kappa/32\), so \(2(t+k)\varepsilon/\kappa\le 13/16\) and the parenthetical term in (5) is at least 3/16. Substituting into (5) yields

\(\mathsf{Sens}(\mathcal{A},\mathcal{I}_C(m))\ge\frac{3t}{16d}-\frac{1}{d}\ge\frac{1}{d}\left(\frac{3\kappa}{128}\cdot\frac{1}{\varepsilon}-\frac{11}{8}\right)=\Omega\left(\frac{1}{\varepsilon}\right),\)

because \(\varepsilon\le\kappa/(8\sqrt{n})\) tends to 0 with growing blocklength, so the term proportional to \(1/\varepsilon\) dominates the constant. Thus, for every sufficiently large _n_ and every \(1/n\le\varepsilon\le\kappa/(8\sqrt{n})\), we obtain a satisfiable bipartite Max Cut instance on which any \((1-\varepsilon)\)-approximation algorithm has sensitivity \(\Omega(1/\varepsilon)\). This completes the proof.

## 5 Maximum _k_-Coverage

We show how the sensitivity lower bound for Max E3SAT implies a matching bound for the maximum _k_-coverage problem when algorithms achieve near-perfect coverage on perfectly coverable instances.

In the maximum _k_-coverage problem, an instance _I_=(_U,_F) has a universe _U_ and a family \(\mathcal{F}\subseteq 2^U\). Outputs are _k_-subfamilies \(\mathcal{S}\subseteq\mathcal{F}\) encoded by their indicator vectors \(\unknown_\mathcal{S}\in\{0,1\}^\mathcal{F}\), and we measure distances with the Hamming metric \(d_\mathrm{H}(\unknown_\mathcal{S},\unknown_{\mathcal{S}^\prime})=|\mathcal{S}\triangle\mathcal{S}'|\). Two instances are neighbors if they differ only in the incidence vector of a single element \(e\in U\): equivalently, we delete _e_ and insert a fresh element whose membership across F can be chosen arbitrarily.

### 5.1 Max E3SAT

In Max E3SAT, an instance \(\Phi=(V,\{0,1\},\mathcal{C})\) consists of variables _V_ and 3-CNF clauses C={_C_<sub>1</sub>_,...,C<sub>m</sub>_}. The output space is {0,1}_<sup>V</sup>_ equipped with the Hamming metric _d_<sub>H</sub>. Combining the standard reduction from Max E3SAT to Max E3LIN2 with a swapping variant of Theorems 1.1 and 1.2 (obtained by adapting its proof to replace clause deletions with clause replacements) yields the following consequence.

