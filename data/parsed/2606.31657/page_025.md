## 6 A Boolean-Function View of Randomized Algorithms for Satisfiable Max E3SAT

In this section we recast the instability results from Sections 3.3 and 5.1 in the language of Boolean functions. We study randomized algorithms that, given a satisfiable Max E3SAT formula, output an assignment satisfying almost all clauses in expectation. Our hard instances are not arbitrary unrelated formulas: they form an explicit local subcube inside the ordinary SAT input space, indexed by messages \(m\in\{0,1\}^k\). All formulas in the family share the same variables and the same ordered clause skeleton, and flipping one bit of _m_ changes only _O_(1) clause signs. Once the algorithm’s random seed is fixed, each output bit becomes an ordinary Boolean function of _m_. Its influence is the sum, over all message coordinates, of the probability that flipping that coordinate changes the output bit. The main conclusion is that, on this explicit satisfiable family, these output bits cannot all have small influence: averaged over the random seed, the sum of their influences is necessarily large. This viewpoint is what later yields the junta, pseudo-junta, decision-tree, and bounded-depth circuit corollaries.

We say that a randomized algorithm _A_ is _one-sided_ \((1-\eta)\)-approximate for Max E3SAT if _A_ is defined on every 3-CNF formula and, for every satisfiable input formula \(\Phi\),<tbc>

\(\mathbb{E}_{a\sim A(\Phi)}\big[\#\text{clauses of}\Phi\text{satisfied by}a\big]\ge(1-\eta)|\Phi|.\)

<tbc>Equivalently, if _R_ denotes the internal random seed of _A_, then

\(\mathbb{E}_R\big[\#\text{clauses of}\Phi\text{satisfied by}A(\Phi;R)\big]\ge(1-\eta)|\Phi|\)

for every satisfiable \(\Phi\). No guarantee is required on unsatisfiable inputs. When _A_ happens to be deterministic, the seed _R_ is trivial and all of the statements below reduce to the deterministic version.

### The standard formula encoding.

Fix integers _n_ and _M_, and regard a 3-CNF formula on variable set \[_n_\] with exactly _M_ clauses as an ordered list<tbc>

\(\Phi=(C_1,\dots,C_M).\)

<tbc>Write each clause in the canonical order of its three variable indices, and encode each literal by the binary representation of its variable index in \[_n_\] together with one sign bit indicating whether it is negated. Let

\(\text{Enc}_{n,M}(\Phi)\in\{0,1\}^N,N:=M\big(3\lceil log_2n\rceil+3\big),\)

denote the concatenation of the _M_ clause encodings. Throughout this section, when we write \(A(\Phi)\) for such a randomized algorithm _A_, we mean the output distribution \(A(\text{Enc}_{n,M}(\Phi))\) under this standard clause-by-clause encoding. Thus the ambient input space is the completely ordinary bit representation of 3-CNF formulas; the parameter \(m\in\{0,1\}^k\) used below merely indexes an explicit hard subfamily inside that ambient space.

### 6.1 From Instability to Influence

We begin with the randomized E3LIN2 instability statement supplied by the LTC framework.

