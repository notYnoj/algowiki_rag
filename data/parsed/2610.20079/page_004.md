### The multiple-unicast conjecture.

Li and Li (2004) \[LL04\] conjectured that network coding cannot improve the achievable rates of independent multiple-unicast sessions over fractional routing in undirected networks. Subsequent work proved the conjecture in special cases with restrictions on network structure and terminal placement \[JVY06,HKL06,YLLW18,QT22\], and developed geometric and metric approaches \[XLWH14,LL25,LQLL26\] and frameworks based on relations among sessions \[LHWL26,LLFC26\]. Related routing results characterize when cut conditions suffice for multiflow in series-parallel networks \[CFW12\]. The conjecture also became closely connected to computational lower bounds. Adler, Harvey, Jain, Kleinberg, and Lehman (2006) \[AHJ<sup>+</sup>06\] first used it to prove conditional lower bounds in several computational models whose access patterns are independent of the input. Farhadi, Hajiaghayi, Larsen, and Shi (2019) \[FHLS19\] removed this access restriction for external-memory integer sorting: assuming the conjecture, any randomized sorting algorithm with error probability at most 1/3 and key length \(w=\Omega(logN)\) requires at least

\(\Omega\left(min\big\{N,\frac{N}{B}log_{2M/B}\frac{N}{B}\big\}\right)\)

expected I/Os. Under the same assumption, when \(B\ge logN\), this lower bound would match the classical comparison-sorting bound up to constant factors. Afshani, Freksen, Kamma, and Larsen (2019) \[AFKL19\] extended this connection to integer multiplication, obtaining conditional lower bounds for constant-degree Boolean circuits and further demonstrating the conjecture’s complexity- theoretic significance beyond communication problems.

The finite binary linear circuit in OpenAI’s integer-multiplication construction \[Ope26, Section 3\] also implies a counterexample to the multiple-unicast conjecture. This follows by applying the routing argument in Section 5.4 to its rational matrix labels, which gives a routing upper bound strictly below an achievable coding rate.

Recently, Zhang, Li, and Li (2026) \[ZLL26\] and Braverman and He (2026) \[BH26\] gave counterexamples to the multiple-unicast conjecture, proving that coding can achieve strictly higher throughput than fractional routing. The former construct a reversible communication process from a completion-time separation; the latter use finite geometry and polynomial evaluation to construct a coding scheme. These results establish the existence of a coding advantage, but refuting the conjecture does not by itself produce a faster sorting algorithm. We further study how such an advantage can reduce data movement in computation: the finite linear construction used here both yields a communication-rate separation and supports recursive address permutations, connecting network-coding constructions to I/O upper bounds for external-memory sorting.

## 3 Main Results

We write log for the base-2 logarithm and ln for the natural logarithm. For a positive integer _t_, let \[_t_\]={0_,...,t_-1}.

### 3.1 The external-memory model and sorting bound

Let _N,M,B,w_ be positive integers with \(N\ge 2\). The input consists of _N_ integers of _w_ bits stored on disk, where \(w=\Theta(logN)\). A storage unit of _w_ bits is called a _machine word_, and each input integer occupies one word. The algorithm must write the integers back to disk in nondecreasing order.

