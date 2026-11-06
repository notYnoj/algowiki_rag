specified precision, use the full functions \(\beta(\lambda_\mathrm{bal}(\epsilon))\) and \(\sigma(\Xi(\lambda_\mathrm{bal}(\epsilon)))\) in Definition 26, evaluating \(\sigma\) from the full maxima in (131).

For a fixed tripartition set and correction family Q, the remaining triples J are determined by Definition 20. Choosing \(\lambda\) balances error for one assignment of exponents; choosing the relative exponents can increase the limiting fraction by reducing _h_. The following linear program determines the best such fraction for this fixed correction family.

**Proposition 2** (Choice of parameter exponents)**.** _Fix_ S _and the evaluated corrections_ Q_, and suppose the remaining triples_ J _admit a grading. The largest limiting fraction given by the normalized gradings is_ 1/(_h_<sub>∗</sub>+1)_, where_

\(h_*=\mathrm{min}h\text{\textit{subject to}}a_t,b_t\ge 0,c_t\ge-h,a_t+b_t+c_t=0(1\le t\le m),a_i+b_j+c_k\ge 1((i,j,k)\in\mathcal{J}).\text{(150)}\)

_The minimum is attained by rational exponents. At an optimum,_ min_<sub>t</sub>a<sub>t</sub>_=min_<sub>t</sub>b<sub>t</sub>_=0 _and_ min_<sub>t</sub>c<sub>t</sub>_=-_h_<sub>∗</sub>.

_Proof._ Subtracting min_<sub>t</sub>a<sub>t</sub>_ from every _a<sub>t</sub>_ and adding it to every _c<sub>t</sub>_ preserves all product degrees and the spectral-norm product. The same holds for _b<sub>t</sub>_. Thus we may impose \(a_t,b_t\ge 0\) with minima zero; then (110) reduces to _h_=-min_<sub>t</sub>c<sub>t</sub>_. The constraints on J ensure that every remaining degree is at least one.

At an optimum, a positive minimum of _a<sub>t</sub>_ or _b<sub>t</sub>_ could be removed as above to decrease _h_, and min_<sub>t</sub>c<sub>t</sub>\>-h_ would also allow _h_ to decrease. When \(\mathcal{J}\neq\emptyset\), the smallest degree among the remaining mixed products must be one: otherwise dividing all exponents and _h_ by that degree lowers the objective. Lemma 11 therefore identifies the largest limiting fraction with 1/(_h_<sub>∗</sub>+1). The linear program has rational coefficients and a bounded objective, so a feasible instance has a rational optimum. If \(\mathcal{J}=\emptyset\), zero exponents give _h_<sub>∗</sub>=0.

## 8 Computational search and comparisons

The numerical comparisons evaluate multiplication counts as the matrix dimension, number of independent products, and required fraction of retained accuracy vary. We compare explicit corrections with padding and weighting, both for the same tripartition set and for the number of products that can be accommodated.  3 summarizes the selected constructions. Appendices C and D give additional bounds, and Appendix F indexes the complete construction data and their figure appearances.

### 8.1 Parameters and search

A balanced family in _B<sub>N,N,N</sub>_ gives _p_=|S| independent products of dimension _q=n<sup>N</sup>_, with _d_=3_N_ aggregate indices. The local dimension _n_ determines the embedding overhead, while the family determines the correction counts and feasible parameter exponents. We evaluate the selected multiplication budget \(r=\rho_{\mathcal{S},\mathcal{Q}}(n)\) from (101), using all corrections in P(S) for exact constructions. For a reference algorithm with count _r_ref, its reduction factor is _r_ref_/r_. In particular, relative to classical multiplication we use

\(\xi(p,q,r)=\frac{pq^3}{r},\omega_\mathrm{eff}(p,q,r)=\frac{\mathrm{log}(r/p)}{\mathrm{log}q}.\) (151)

The plotted quantity is \(\xi\), with one curve for each family.

We compare exact constructions, approximations with limiting retained fraction \(\theta\ge 1/2,1/3,1/4\) of Definition 26, and unrestricted border rank. The value of \(\theta\) is computed from the smallest remaining degree and normalized height; Proposition 2 gives the linear program for fixed tripartitions and corrections. At fixed working precision, (144) compares the full approximation and round-off bound with the classical reference. We compute \(\sigma\) of Definition 24 from (131) and use the leading-term parameter rule (146). For _N_=2,3,4, we evaluate every integer \(n\ge 2\) with \(n^N\le 16000\). Markers denote the dimensions _q=n<sup>N</sup>_ at these integer values of _n_; connecting segments join the samples. The largest sampled dimensions are 15876, 15625, and 14641, respectively.

