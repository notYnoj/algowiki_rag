<tbc>We specify an instance I of 2wcst as a tuple \(\mathcal{I}=(\mathcal{K}=\{K_1,\dots,K_n\},\mathcal{Q},\mathcal{C},\alpha,\beta)\). The set C of allowed comparison operators can be any subset of \(\{<,\le,=,\ge,>\}\). The set Q specifies the queries. A solution is an optimal 2wcst _T_ among those using operators in C and handling all queries in Q. This definition generalizes both standard 2wcst (let Q contain each key and a value between each pair of keys), and the successful-queries variant (take Q=K and \(\alpha\equiv 0\)). It further allows any query set Q between these two extremes, even allowing \(\mathcal{K}\unknown\subseteq\mathcal{Q}\). As usual, \(\beta_i\) is the probability that _v_ equals _K<sub>i</sub>_; \(\alpha_i\) is the probability that _v_ falls between keys _K<sub>i</sub>_ and _K_<sub>_i_+1</sub> (except \(\alpha_0=Pr[v<K_1]\) and \(\alpha_n=Pr[v>K_n]\)). <sup>4</sup>

To prove Thm. 1, we prove Spuler’s 1994 "maximum-likelihood" conjecture: _in any optimal_ 2wcst _tree, each equality comparison is to a key in_ K _of maximum likelihood, given the comparisons so far_ \[17, §6.4Conj.1\]. As Spuler observed, the conjecture implies an _O(n_<sup>5</sup>)-time algorithm; we reduce this to _O(n_<sup>4</sup>) using standard techniques and a new perturbation argument. Anderson et al. proved the conjecture for their special case \[1, Cor. 3\]. We were unable to extend their proof directly; our proof uses a different local-exchange argument.

We also give a fast additive-3 approximation algorithm:

**Theorem 2.** _Given any instance_ \(\mathcal{I}=(\mathcal{K},\mathcal{Q},\mathcal{C},\alpha,\beta)\) _of_ 2wcst_, one can compute a tree of cost at most the optimum plus 3, in O(n_log_n_) _time._

Comparable results were known for the successful-queries variant (Q=K) \[19,1\]. We approximately reduce the general case to that case.

_Binary split trees_ "split" each 3-way comparison in Knuth’s 3-way-comparison model into two 2-way comparisons within the same node: an equality comparison (which, by definition, must be to the maximum-likelihood key) and a "_\<_" comparison (to any key) \[16,6,12,15,9\]. The fastest algorithms to find an optimal binary split tree take _O(n_<sup>5</sup>)-time: from 1984 for the successful-queries-only variant (_Q=K_) \[12\]; from 1986 for the standard problem (_Q_ contains queries in all possible relations to the keys in _K_) \[9\]. We obtain a linear speedup: <sup>5</sup>

**Theorem 3.** _Given any instance_ \(\mathcal{I}=(\mathcal{K}=\{K_1,\dots,K_n\},\alpha,\beta)\) _of the standard binary split tree problem, an optimal tree can be computed in O(n_<sup>4</sup>) _time._ <sup>5</sup>

The proof uses our new perturbation argument (Sec. 3.1) to reduce to the case when all \(\beta_i\)’s are distinct, then applies a known algorithm \[9\]. <sup>5</sup> The perturbation argument can also be used to simplify Anderson et al.’s algorithm \[1\].

_Generalized binary split trees_ (gbsts) are binary split trees without the maximum- likelihood constraint. Huang and Wong \[11\] (1984) observe that relaxing this constraint allows cheaper trees -- the maximum-likelihood conjecture fails here -- and propose an algorithm to find optimal gbsts. We prove it incorrect!

<sup>4</sup> As defined here, a 2wcst _T_ must determine the relation of the query _v_ to every key in K. More generally, one could specify any partition P of Q, and only require _T_ to determine, if at all possible using keys in K, which set \(S\in\mathcal{P}\) contains _v_. For example, if P={K,Q\\K}, then _T_ would only need to determine whether \(v\in\mathcal{K}\). We note without proof that Thm. 1 extends to this more general formulation. <sup>5</sup> ERRATUM (MARCH 2021): SEE SECTIONS 0 AND 3.1.

