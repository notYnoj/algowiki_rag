**The Algorithm.** We are given a function cost on the edges of _G_. We set cost(_e_)=0 for every new edge _e_ in _G_<sup>∗</sup>, i.e., cost(_e_)=0 for all \(e\in\cup_{i=0}^kS_i\). All the _old_ edges in _G_<sup>∗</sup>, i.e., those in _E_, inherit their edge costs from _G_. For any matching _T_ in _G_<sup>∗</sup>, note that \(\text{cost}(T\cap E)=\text{cost}(T)\).

Our algorithm that proves Theorem 2 stated in Section 1 is summed up below.

1. Identify all unstable vertices in \(G=(A\cup B,E)\) by running Gale-Shapley algorithm.<tbc>

2. Determine the popular subgraph of _G_ by computing all popular edges in _G_ using \[11\].<tbc>

3. Augment the graph _G_ into the graph _G_<sup>∗</sup> by adding edges in \(\cup_{i=0}^kS_i\) as described earlier.<tbc>

4. Compute a min-cost extra-dominant matching _T_ in _G_<sup>∗</sup> by solving a linear program over F<sub>_G_<sup>∗</sup></sub>.<tbc>

5. Return \(T\cap E\).

It follows from Lemma 2 and Theorem 8 that \(\text{cost}(T)\le\text{opt}\) where opt is the cost of a min-cost popular matching in _G_. We know from Lemma 3 that \(T\cap E\) is a quasi-popular matching in _G_. Since \(\text{cost}(T\cap E)=\text{cost}(T)\le\text{opt}\), the correctness of our algorithm follows.

## 3.3 Proofs of Our Technical Lemmas

_Proof._ (of Lemma 2). Since _M_ is popular in _G_, it has a witness \(\unknown\in\{0,\pm 1\}^n\) such that \(\sum_u\alpha_u=0\) and \((I_M,\unknown)\) satisfies edge covering constraints as given in Theorem 5, where _I<sub>M</sub>_ is the incidence vector of _M_. For any non-trivial connected component _C<sub>i</sub>_ in the subgraph _G_<sub>0</sub>, it follows from Lemma 1 that either (i) \(\alpha_u=0\) for all \(u\in C_i\) or (ii) \(\alpha_u\in\{\pm 1\}\) for all \(u\in C_i\).

We will now define a witness \(\unknown\) that proves the popularity of _M_<sup>∗</sup> in _G_<sup>∗</sup>. For any non-trivial connected component _C<sub>i</sub>_ in _G_<sub>0</sub> do:

- if \(\alpha_u\in\{\pm 1\}\) for all \(u\in C_i\) then set \(\beta_u=\alpha_u\) for all \(u\in C_i\).<tbc>

**-** if \(\alpha_u=0\) for all \(u\in C_i\) then set \(\beta_a=-1\) for all \(a\in A\cap C_i\) and \(\beta_b=1\) for all \(b\in B\cap C_i\).

We will now set \(\beta\)-values for vertices that are unpopular in _G_. These vertices are outside \(\cup_{i=1}^kC_i\). We set \(\beta_b=1\) for all unpopular vertices \(b\in B\) and \(\beta_a=-1\) for all those unpopular vertices \(a\in A\) that have an edge incident to them in _S_<sub>0</sub>. For each unpopular vertex \(a\in A\) that does not appear in _S_<sub>0</sub> (so _a_ is unmatched in _M_<sup>∗</sup>), we set \(\beta_a=0\). Let us check that \(\unknown\) satisfies Theorem 5.

Observe first that \(\sum_{(a,b)\in S_0}(\beta_a+\beta_b)=0\). For each edge \((a,b)\in M\), we have \(\alpha_a+\alpha_b=\text{wt}_M(a,b)=0\) and it is easy to see from our assignment of \(\beta\)-values that \(\beta_a+\beta_b=\alpha_a+\alpha_b=0\). Thus \(\sum_{a\in A\cup B}\beta_u=0\).

_Edge-Covering Constraints._ We will now show that \(\beta_a+\beta_b\ge\text{wt}_{M^*}(a,b)\) for all edges (_a,b_) in _G_<sup>∗</sup> along with \(\beta_u\ge\text{wt}_{M^*}(u,u)\) for all vertices _u_, where the function wt<sub>_M_<sup>∗</sup></sub>(_e_) was defined in Section 2. The constraints \(\beta_u\ge\text{wt}_{M^*}(u,u)\) for all vertices _u_ are easy to see: either (i) \(\beta_u=-1\) which implies that _u_ is matched in _M_<sup>∗</sup> and so wt<sub>_M_<sup>∗</sup></sub>(_u,u_)=-1 or (ii) \(\beta_u\ge 0\ge\text{wt}_{M^*}(u,u)\).

We will now show edge covering constraints hold for all edges in _G_<sup>∗</sup>. It is easy to see that \(\beta_a+\beta_b\ge\text{wt}_{M^*}(a,b)\) for all the _new_ edges (_a,b_) in _G_<sup>∗</sup>, i.e., for all \((a,b)\in\cup_{i=0}^kS_i\). This is because either: (i) both _a_ and _b_ are matched in _M_, in which case wt<sub>_M_<sup>∗</sup></sub>(_a,b_)=-2 and \(\beta_a+\beta_b\ge-2\) holds, or (ii) both _a_ and _b_ are unmatched in _M_, in which case \((a,b)\in M^*\) and so \(\text{wt}_{M^*}(a,b)=0=\beta_a+\beta_b\) (recall that \(\beta_a=-1\) and \(\beta_b=1\) in this case).

We will now show that these constraints hold for all the old edges as well, i.e., for any \((a,b)\in E\). Note that \(\alpha_a+\alpha_b\ge\text{wt}_M(a,b)\) and also wt<sub>_M_<sup>∗</sup></sub>(_a,b_)=wt_<sub>M</sub>(a,b_) by construction. If \(\beta_a=\alpha_a\) then either \(\beta_b=\alpha_b\) or \(\beta_b=\alpha_b+1\), so \(\beta_a+\beta_b\ge\alpha_a+\alpha_b\ge\text{wt}_M(a,b)=\text{wt}_{M^*}(a,b)\) for such an edge (_a,b_). Else \(\beta_a=\alpha_a-1\).

We have two sub-cases here. In the first sub-case, \(\beta_b=\alpha_b+1\) and thus \(\beta_a+\beta_b=\alpha_a+\alpha_b\). Since wt<sub>_M_<sup>∗</sup></sub>(_a,b_)=wt_<sub>M</sub>(a,b_) for all \((a,b)\in E\), the statement follows. The other sub-case is \(\beta_b=\alpha_b\). So \(\alpha_b\in\{\pm 1\}\), while \(\alpha_a=0\), thus \(\alpha_a+\alpha_b\in\{\pm 1\}\). We have wt<sub>_M_<sup>∗</sup></sub>(_a,b_)=wt_<sub>M</sub>(a,b_)\(\le\alpha_a+\alpha_b\). Note that for any edge (_a,b_), the value \(\text{wt}_M(a,b)\in\{0,\pm 2\}\). Thus wt_<sub>M</sub>(a,b_) is an even number, so the constraint \(\text{wt}_M(a,b)\le\alpha_a+\alpha_b\) is _slack_ and we can tighten it to \(\text{wt}_M(a,b)\le\alpha_a+\alpha_b-1\). In other words, we have: \(\text{wt}_{M^*}(a,b)=\text{wt}_M(a,b)\le\)<tbc>

