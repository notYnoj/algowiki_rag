_Proof of Claim 37._ We use structural induction to prove a somewhat stronger claim, namely that

\(\sum_v\sqrt{\frac{n_{v,1}n_{v,2}}{n_{v,1}+n_{v,2}}}\le c'n-d'\sqrt{n}\) (16)

for some constants \(c'\) and \(d'\) to be determined. As the base case we consider binary trees _T_ with at most two leaves. In this case, the left-hand side of (16) is zero and the right-hand side is non-negative provided \(c'\ge d'\), so (16) holds.

For the inductive step, the case where the root of _T_ has degree 1 immediately follows from the inductive hypothesis for the subtree _T<sub>u</sub>_ rooted by the child _u_ of the root of _T_. The remaining case is where the root of _T_ has degree 2. Let _u_<sub>1</sub> and _u_<sub>2</sub> be the two children for the root, _n_<sub>1</sub>=|L(_T_<sub>_u_<sub>1</sub></sub>)|, and _n_<sub>2</sub>=|L(_T_<sub>_u_<sub>2</sub></sub>)|. The sum on the left-hand side of (16) has three contributions: \(\sqrt{\frac{n_1n_2}{n_1+n_2}}\) from the root, and the contributions from _T_<sub>_u_<sub>1</sub></sub> and _T_<sub>_u_<sub>2</sub></sub>, to which we can individually apply the inductive hypothesis. This gives us an upper bound of<tbc>

\(\sqrt{\frac{n_1n_2}{n_1+n_2}}+(c'n_1-d'\sqrt{n_1})+(c'n_2-d'\sqrt{n_2})=\sqrt{\frac{n_1n_2}{n_1+n_2}}+c'(n_1+n_2)-d'(\sqrt{n_1}+\sqrt{n_2}),\)

<tbc>which we want to upper bound by<tbc>

\(c'n-d'\sqrt{n}=c'(n_1+n_2)-d'\sqrt{n_1+n_2}.\)

<tbc>Writing \(n_1=\alpha n\) for some \(\alpha\in[0,1]\) and rearranging terms, the upper bound holds if and only if<tbc>

\(\sqrt{\alpha(1-\alpha)}\le d'(\sqrt{\alpha}+\sqrt{1-\alpha}-1).\)

<tbc>We claim that the upper bound holds for \(d'=(\sqrt{2}+1)/2\). Let

\(F(\alpha)\doteq d'(\sqrt{\alpha}+\sqrt{1-\alpha}-1)-\sqrt{\alpha(1-\alpha)}.\)

It suffices to show that \(F(\alpha)\ge 0\). Since _F_ is continuous on \[0,1\], it attains a minimum on \[0,1\]. On (0,1), _F_ is differentiable. It can be verified that \(F'\) has a unique zero in (0,1/2), which needs to be a maximum as _F_ is increasing at \(\alpha=0\). By the symmetry \(F(\alpha)=F(1-\alpha)\), it follows that the minimum of _F_ on \[0,1\] is attained at the midpoint \(\alpha=1/2\) or at one of the endpoint \(\alpha=0\) or \(\alpha=1\). At all three points \(F(\alpha)=0\). We conclude that (16) holds for any constants \(d'\ge(\sqrt{2}+1)/2\) and \(c'\ge d'\).

## 6 Sensitivity Approach for Bounded Error

In this section, we apply the sensitivity approach to obtain lower bounds on the query complexity of problems in the comparison-query model against randomized algorithms with bounded error. We derive a generic result that query lower bounds against deterministic algorithms that are based on the Sensitivity Lemma, also hold against bounded-error randomized algorithms with a small loss in strength. The approach works particularly well when we have linear lower bounds on the average sensitivity, in which case there is only a constant-factor loss in the strength of the query lower bound. Among others, this applies to the \(\Omega(nlogn)\) query lower bound for inversion minimization on trees of bounded degree.

