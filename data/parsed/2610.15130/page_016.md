<tbc>that lie in the true top-\(\beta L\) yet are absent from the returned list. Each such point costs at most 1_/k_ of recall, so

\(\mathbb{E}[\mathrm{recall}]\ge\mathbb{E}[\mathrm{min}(X_q,k)]/k-\delta_\mathrm{ann}(L).\) (5)

The argument (5) bounds the _shortfall_ and says nothing about recall exceeding the frontier-mass value, so the inequality is one-sided. One-sided suffices because Theorem 8 adds \(\delta_\mathrm{ann}(L)\) to an upper bound on loss, and \(\delta_\mathrm{ann}\) is measurable against the archived brute-force neighbour lists. The object is a truncated mean rather than a success probability, the distinction that separates parts (i)-(iv) below.

_(i) Envelope._ The map \(u\mapsto\mathrm{min}(u,k)\) is concave, so by Jensen and \(\mathbb{E}X=\beta L\sigma_\mathrm{loc}\),

\(\mathbb{E}[\mathrm{min}(X,k)]/k\le\mathrm{min}(1,\beta L\sigma_\mathrm{loc}/k).\) (6)

No assumption on the law of _X_ beyond its mean is used, so (6) holds for arbitrarily correlated predicates. Recall \(\rightarrow 1\) therefore requires \(\beta L\sigma_\mathrm{loc}\ge k\), i.e. \(L=\Omega(k/\sigma_\mathrm{loc})\), and with (ii) the recovery scale is \(\Theta(k/\sigma_\mathrm{loc})\).

_(ii) Exact form under homogeneity._ Under Assumption 6, \(X\sim\mathrm{Binom}(\beta L,\sigma_\mathrm{loc})\). For a non-negative integer variable \(\mathbb{E}[\mathrm{min}(X,k)]=\sum_{i=1}^k\mathrm{Pr}[X\ge i]\), hence<tbc>

\(h=\frac{1}{k}\sum_{i=1}^k\mathrm{Pr}[\mathrm{Binom}(\beta L,\sigma_\mathrm{loc})\ge i].\) (7)

<tbc>Every summand is \(\ge\mathrm{Pr}[X\ge k]\), so \(h\ge h_\mathrm{tail}=\mathrm{Pr}[X\ge k]\). The single-term tail is a valid lower bound on recall but only the smallest of _k_ terms, and is loose by orders of magnitude at \(\beta L\sigma_\mathrm{loc}\checkmark k\) (§ V-C,  SIII). Combining with (6),

\(h_\mathrm{tail}\le h\le\mathrm{min}(1,\beta L\sigma_\mathrm{loc}/k).\) (8)

At the limits \(h\rightarrow 1\) when \(\beta L\sigma_\mathrm{loc}\gg k\) (all _k_ tail terms saturate) and \(h\rightarrow\beta L\sigma_\mathrm{loc}/k\) when \(\beta L\sigma_\mathrm{loc}\checkmark k\) (the truncation is inactive, \(\mathbb{E}[\mathrm{min}(X,k)]\rightarrow\mathbb{E}X\)), the latter being the unit- slope regime that calibrates \(\beta=1\).

_(iii) Query average._ A tenant’s recall is<br>
\(\bar{h}_\tau=\mathbb{E}_{q|\tau}[h(\sigma_\mathrm{loc}(q),L,k)]\), from (ii) applied per query and averaged. Put \(\gamma(p)=\mathbb{E}[\mathrm{min}(\mathrm{Binom}(n,p),k)]\) with \(n=\beta L\). Differentiating the binomial expectation twice in _p_ gives \(\gamma''(p)=n(n-1)\mathbb{E}[\Delta^2\phi(\mathrm{Binom}(n-2,p))]\), where \(\phi(j)=\mathrm{min}(j,k)\) and \(\Delta^2\phi(j)=\phi(j+2)-2\phi(j+1)+\phi(j)\le 0\) by concavity of \(\phi\), so \(\gamma\) is concave on \[0,1\]. By Jensen,

\(\bar{h}_\tau=\mathbb{E}_q[\gamma(\sigma_\mathrm{loc}(q))]/k\le\gamma(\mathbb{E}_q[\sigma_\mathrm{loc}(q)])/k=h(\bar{\sigma}_\mathrm{loc}^{(\tau)},L,k).\) (9)

Substituting a tenant’s mean local density therefore over- predicts its recall, and the gap is governed by the dispersion of \(\sigma_\mathrm{loc}\) across the tenant’s queries. The gap is one-signed and vanishes wherever \(\gamma\) is affine, in the unsaturated regime \(\gamma(p)\rightarrow np\) (linear) and the saturated regime \(\gamma\rightarrow k\) (constant), so it peaks in the knee, matching § V-C. Because \(\bar{h}_\tau\) is computable from the per-query \(\sigma_\mathrm{loc}\) the sweep already produces, it is a quantitative prediction (§ VII).

_(iv) Ordering._ Every summand of (ii) is \(\ge\mathrm{Pr}[X\ge k]\) and, by (6), \(\gamma(p)/k\le\mathrm{min}(1,np/k)\); combining with (iii),

\(h_\mathrm{tail}\le\bar{h}_\tau\le h(\bar{\sigma}_\mathrm{loc},L,k)\le\mathrm{min}(1,\beta L\bar{\sigma}_\mathrm{loc}/k).\) (10)

The tail _h_<sub>tail</sub> lower-bounds recall unconditionally and the envelope upper-bounds it unconditionally.

### C. Multi-tenant extension (Theorem 8)

By Assumption 5 the staleness/degradation term is filter- and tenant-independent, so it applies per tenant with \(N_\tau^\mathrm{stale}\) in place of the global insert count; the scheduler’s max-staleness ceiling caps \(N_\tau^\mathrm{stale}\le\lambda_\mathrm{ins}^{(\tau)}(S_\tau+W)\) for a trigger window _W_, a scheduler invariant and the ceiling-test granularity of § IV-C. The filtered term is the query-averaged Lemma 7(ii)-(iii) on the fixed graph. Additivity follows from a union bound. Fix a ground-truth item _y_ for query _q_; let _A_ be the event that _y_ is a pending mutation neither integrated into _G<sub>t</sub>_ nor served by the cache, and _B_ the event that _y_ is absent from the post-filtered frontier of the converged graph. The item is missed only on \(A\cup B\), so

\(\mathbb{E}[1-R_q]\le\mathrm{Pr}[A]+\mathrm{Pr}[B],\) (11)

and averaging over _y_, _q_ and taking the supremum over _t_ gives the displayed inequality, with slack \(\mathrm{Pr}[A\cap B]\) from items that are both stale and out-of-frontier. Parameter disjointness makes the two terms separately _estimable_. Deletes and migration add a \(\lambda_\mathrm{del}\)-dependent term \(g_0^\mathrm{del}\) to the M2 hub-perturbation floor. The high-probability form extends by a union bound over |T| tenants, since the _R_-cap bounded influence survives the union. Evaluating a tenant’s filtered term at its mean local density rather than the query average \(\bar{h}_\tau\) replaces the bound with the estimate of Lemma 7(iii); the assumption-free fallback is Lemma 7(i), giving a necessary-_L_ condition per tenant.

## II. SUPPLEMENTARY TABLES

Three tables back the proofs and the evaluation.  SI gives the per-merge degradation _g(c,N_<sub>0</sub>) that underlies the missing-edge count (1) and the horizon sum (2).  SII tracks the horizon assembly that makes the additive bound (3) conservative, reporting realized cumulative loss against the additive prediction.  SIII compares the frontier-mass model _h_ of (7) against measured recall on the collapsed curve, alongside the single-term tail _h_<sub>tail</sub> and the envelope (6).

## III. EXTERNAL COMPARISONS

On single-tenant streaming, recall@10 is 99.29/99.15/99.02 over res 20/40/60K against PipeANN’s 99.94, at unmatched parameters (ours _R_=32_/L_=75/beam4 vs. PipeANN _R_=64_/L_=100/beam32). Tail latency is _p_<sub>99</sub>≈45 ms against PipeANN’s 3.1-6.1 ms, the regime the<tbc>

<sup>†</sup> at or below the 0.02 pp floor set by 2-decimal reporting of _R_<sub>scratch</sub>; excluded from all fits. This floor coincides with the \(c/N\le 0.02\) regime, so the fitted per-merge law is quoted for _c/N\>_0.02.

\begin{tabular}{cccccc}
_c_ & _c/N_<sub>0</sub> & _R_<sub>scratch</sub> & _R_<sub>merge</sub> & _g_ (pp) & cap _c/(N_<sub>0</sub>+_c_) \\
1,000 & 0.01 & 99.71 & 99.722 & ≈0.00<sup>†</sup> & 0.0099 \\
2,000 & 0.02 & 99.73 & 99.711 & 0.019<sup>†</sup> & 0.0196 \\
5,000 & 0.05 & 99.72 & 99.633 & 0.087 & 0.0476 \\
10,000 & 0.10 & 99.73 & 99.534 & 0.196 & 0.0909 \\
20,000 & 0.20 & 99.70 & 99.340 & 0.360 & 0.1667 \\
40,000 & 0.40 & 99.62 & 98.500 & 1.120 & 0.2857 \\
80,000 & 0.80 & 99.53 & 96.494 & 3.036 & 0.4444 \\
\end{tabular}

TABLE SI

PER-MERGE DEGRADATION AT _N_<sub>0</sub>=100K, _L_=75, RECALL@10, 10K QUERIES, CACHE-EMPTY TIER-0B. ROWS BELOW THE 0.02 PP REPORTING FLOOR ARE EXCLUDED FROM THE FIT.

