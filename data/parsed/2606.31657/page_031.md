The strength of Corollary 6.5 is that it turns Corollary 6.3 into a black-box lower-bound principle: _any_ coordinatewise representation class whose seedwise realizations have sublinear total influence is automatically ruled out on linearly many output coordinates on average over the seed. The next three subsections record concrete instantiations.

## 6.3 Anti-Junta and Anti-Pseudo-Junta Consequences

Recall that a Boolean function on {0,1}_<sup>k</sup>_ is a _K-junta_ if it depends on at most _K_ input coordinates. We also use Hatami’s notion of a _K-pseudo-junta_ \[28\], which generalizes juntas by allowing the relevant coordinates to vary with the input in a structured way. We will not need the full formal definition here; the only property used below is that every _K_-pseudo-junta has total influence at most 2_K_.

**Corollary 6.6** (On average over the seed, linearly many outputs are far from juntas and pseudo-juntas)**.** _There exist constants_ \(\gamma,\delta>0\) _such that the following holds for all sufficiently large k._

1. _For every_ \(K\le\gamma k\)_, one has_<tbc>

<tbc>\(\mathbb{E}_R\left[\left|\{v\in[n]:\mathrm{dist}(f_{v,R},\{K\text{\textit{-juntas}}\})\ge\delta\}\right|\right]\ge\delta n.\)<tbc>

_2._ _For every_ \(K\le\gamma k\)_, one has_

<tbc>\(\mathbb{E}_R\left[\left|\{v\in[n]:\mathrm{dist}(f_{v,R},\{K\text{\textit{-pseudo-juntas}}\})\ge\delta\}\right|\right]\ge\delta n.\)

_Proof._ Let \(\alpha_0,\gamma_0\) be the constants from Corollary 6.4. Every _K_-junta satisfies \(\mathrm{Inf}(g)\le K\) \[16\], and every _K_-pseudo-junta satisfies \(\mathrm{Inf}(g)\le 2K\) by Hatami’s proposition on pseudo-juntas \[28\]. Thus both claims follow from Corollary 6.5 by taking \(\delta:=\mathrm{min}\{\alpha_0/4,\gamma_0\}\) and shrinking the displayed constant \(\gamma\) by an absolute factor if needed so that both _K_ and 2_K_ are at most \(\alpha_0k/2\).

The point of Corollary 6.6 is that the randomized task of finding near-satisfying assignments for an explicit satisfiable Max E3SAT family forces averaged non-junta structure: linearly many output coordinates stay a constant distance away from every small junta and every small pseudo-junta on average over the internal randomness.

## 6.4 Decision Trees and Local Dependence

For a Boolean function \(f:\{0,1\}^k\rightarrow\{0,1\}\), let _D(f_) denote its deterministic decision-tree depth, that is, the minimum worst-case number of input bits that must be queried in order to determine _f(m_).

**Corollary 6.7** (On average over the seed, linearly many outputs have linear decision-tree depth)**.** _There exist constants_ \(\alpha,\gamma>0\) _such that_

\(\mathbb{E}_R\left[\left|\{v\in[n]:D(f_{v,R})\ge\alpha k\}\right|\right]\ge\gamma n,\)

_Equivalently, averaged over the internal randomness of the algorithm, linearly many output coordinates cannot be computed by reading o(k_) _message bits._

