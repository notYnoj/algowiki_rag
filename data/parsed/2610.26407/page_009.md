<tbc>where \(z_i(t,\Delta_i):=\mu_i(t)+(q(t)-\mu_i(t))/c_i(t,\Delta_i)\). Choosing the batch that minimizes (6) is thus equivalent to

\(min_{\Delta\in\mathbb{Z}_{\ge 0}^I}\sum_{i=1}^I\ell_{i,t}(\Delta_i)\text{s.t.}\sum_{i=1}^I\Delta_i=B_t,\) (8)

which is the per-round surrogate program. Conceptually, allocating according to (8) sends samples to the items whose posterior has substantial mass on both sides of the top-_k_ threshold _q(t_), weighted by the distance of that mass from _q(t_). These are the items whose membership in the top-_k_ set is uncertain and whose misclassification, if it occurs, could be costly.

## 3.2. Relation to OCBA-style objectives

Before analyzing how to solve (8), we discuss how its structure differs from static objectives in the OCBA literature for EOC. These objectives often use an upper bound on EOC based on a sum of losses associated with pairwise misorderings. For example, for top-1 EOC with Gaussian samples, He et al. (2007) use<tbc>

\(\mathrm{EOC}(\mathcal{H}_t)\le\sum_{i\neq i_{(1)}}\mathbb{E}_t[(\theta_i-\theta_{i_{(1)}})^+].\)

<tbc>Gao and Chen (2015) give the following bound on top-_k frequentist_ EOC:

\(\mathrm{EOC}\le\sum_{j=1}^k\sum_{i\notin\{i_{(1)},\dots,i_{(j)}\}}\sum_{n=1}^j(\mu_{i_{(n)}}(t)-\mu_i(t))\Phi\left(-\frac{\mu_{i_{(n)}}(t)-\mu_i(t)}{\sqrt{v_{i_{(n)}}(t)+v_i(t)}}\right),\)

where \(\Phi\) is the standard normal CDF, and _i_<sub>(1)</sub>_,...,i_<sub>(_I_)</sub> order the items by their current posterior means. Their static objective is then based on driving this bound down. The potential issue with using such a bound is that the candidate top-_k_ items {_i_<sub>(1)</sub>_,...,i_<sub>(_k_)</sub>} are in far more terms in the sum than the non-top-_k_ items. For instance, when _k_=1, _i_<sub>(1)</sub> is in all _I_-1 terms, while all other items are only in one term. Thus, an objective based on such a bound may over-count the benefit of sampling the top items. Our bound avoids these pairwise terms by comparing each item to the same threshold _q(t_), resulting in a single term for each item regardless of whether or not it is in \(S_k(\mu(t))\). Figure 2 shows the distribution of sample allocation across items for our method, called TEAk, and the method of Gao and Chen (2015), called EOC-m. EOC-m systematically allocates more samples to items in the top-_k_, even items far above the top-_k_ boundary, which is likely one of the main factors driving our method’s improvement over EOC-m, which we demonstrate in §5.

## 3.3. Batch allocation algorithm

Although (8) is an integer program, its separability across items allows us to solve it efficiently by dynamic programming and, in some cases, using a greedy procedure. Both are standard techniques. The main technical result of this subsection is Proposition 2(ii)–(iii), which gives conditions on the posterior distributions under which the greedy procedure is optimal.

The dynamic programming procedure in Algorithm 1 has two phases. First, we compute \(\ell_{i,t}(d)\) for every item _i_ and candidate allocation _d_=0_,...,B<sub>t</sub>_. Second, for each _r_=1_,...,I_ and _b_=0_,...,B<sub>t</sub>_, we solve the<tbc>

