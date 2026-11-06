**Theorem 2.** Max-SMTI _admits an_ FPT-AS _with respect to the number_ \(\tau\) _agents with ties._

_Proof._ Let _I_ be an instance of Max-SMTI, \(\tau\) be the number of agents with ties, and \(\varepsilon\in[0,1)\) the approximation ratio we desire. As mentioned before, by the results of Király \[19\] and McDermid \[25\], we can assume without loss of generality that \(\varepsilon\ge\frac{2}{3}\). Further, let _M_<sup>∗</sup> be a maximum-size matching of the acceptability graph for _I_. We first observe the following relation between every stable matching and the size of _M_<sup>∗</sup>.

**Claim 4.** _For every stable matching of I, we have that_ \(|M^*|\le|M|+\tau\).

_Proof._ Consider the symmetric difference \(M^*\Delta M\). Each connected component in the symmetric difference is either a path and a cycle. Every cycle and even-length path component matches the same number of agents in both _M_ and _M_<sup>∗</sup>. Thus every component where _M_<sup>∗</sup> matches more agents must be an odd-length path. Moreover, each of these components matches precisely one extra pair.

Assume, towards a contradiction, that there are more odd-length paths than agents with ties. Then there must be some odd-length path component where no agent has a tie in his preference list.

Let (_v_<sub>1</sub>_,...,v<sub>t</sub>_) be such a path, where _t_ is even. In _M_<sup>∗</sup>, the pairs {_a_<sub>1</sub>_,a_<sub>2</sub>}_,...,_{_a_<sub>_t_-1</sub>_,a<sub>t</sub>_} are matched, whereas in _M_, the pairs {_a_<sub>2</sub>_,a_<sub>3</sub>}_,...,_{_a_<sub>_t_-2</sub>_,a_<sub>_t_-1</sub>} are matched, and _a_<sub>1</sub>_,a<sub>t</sub>_ are unmatched. Since _M_ is stable, it cannot be blocked by {_a_<sub>1</sub>_,a_<sub>2</sub>}. As _a_<sub>1</sub> is unmatched in _M_, it must be that \(a_2:a_3\succ a_1\). Since _M_<sup>∗</sup> is stable, it cannot be blocked by {_a_<sub>2</sub>_,a_<sub>3</sub>}, and we must have that \(a_3:a_4\succ a_2\). By repeating this argument, we obtain that \(a_{t-1}:a_t\succ a_{t-2}\). But then {_a_<sub>_t_-1</sub>_,a<sub>t</sub>_} blocks _M_, a contradiction. (end of Claim 4) \(\diamond\)

Let _M_ be a stable matching with \(|M|\ge\frac{2}{3}|M^*|\). Note that we can find _M_ in polynomial time by using for instance the algorithm of McDermid \[25\]. We proceed in two cases:

**Case 1:** \(|M|<\frac{\varepsilon\cdot\tau}{1-\varepsilon}\) . Then, \(|M^*|\le\frac{3}{2}|M|<\frac{3\varepsilon\cdot\tau}{2(1-\varepsilon)}\) . Since Max-SMTI has a size-_O(k_<sup>2</sup>) problem kernel \[2\] where _k_ is the target size of a stable matching in the natural parameterization of Max-SMTI, and _k_ is bounded by |_M_<sup>∗</sup>|, we can solve _I_ exactly in FPT-time with respect to \(\tau+\varepsilon\). Adil et al. \[2\] also provide an FPT-algorithm with running time _k_<sup>_O(k_)</sup>+_n_<sup>_O_(1)</sup>. Applying it, we obtain our FPT-algorithm with running time \(\frac{3\varepsilon\cdot\tau}{2(1-\varepsilon)}^{O(\frac{3\varepsilon\cdot\tau}{2(1-\varepsilon)})}+|I|^{O(1)}\).

**Case 2:** \(|M|\ge\frac{\varepsilon\cdot\tau}{1-\varepsilon}\) . Combining with Claim 4, \(|M^*|\le|M|+\frac{(1-\varepsilon)}{\varepsilon}\cdot|M|=\frac{|M|}{\varepsilon}\) . Thus, |_M_| is an \(\varepsilon\)- approximation.

As both cases lead to a \(\varepsilon\)-approximation in FPT-time, this concludes the proof.

## 5 Conclusion

In this manuscript, we have explored the fixed-parameter approximability of three problems in the field of stable matchings. Our goal is to highlight the potential of fixed-parameter approximability in the field of matching under preferences and computational social choice more generally. This technique can be used to solve problems that resist both polynomial-time approximation and FPT-algorithms. Using this technique more widely in the field of matchings and computational social choice is an open question. Of course, as we have in Theorem 1 and Corollary 1, some problems resist even this. Finding suitable parameters is part of the challenge.

## References

