**Theorem 2.** _Let P be an efficiently self-reducible problem,_ \(p:\mathbb{Z}_{\ge 0}\rightarrow\mathbb{Z}_{\ge 0}\) _be a non-decreasing and efficiently computable function, and Q be a problem that can be solved in time_ \(O(\beta^s)\)_, where_ \(\beta>1\) _is a constant. Then, if there exists a fine-grained reduction_ \((P,p(s))\le(Q,\gamma^s)\)_, for a constant_ \(\gamma>1\)_, then P can be solved in time_ \(p(s)^{1-\epsilon}\) _for some constant_ \(\epsilon>0\).

_Proof._ If we apply the reduction from an instance of the problem _P_ of size _a_, then all of the oracle calls made by reductions would be on instances of the problem _Q_ of size at most \(b=\frac{logp(a)}{log\gamma}\) . With this in mind, we are going to enumerate and solve all of the instances of the problem _Q_ of size up to \(\nu\), for some \(\nu\) to be determined later. This will take time \(O(2^\nu\beta^\nu=O((2\beta)^\nu)\). Then, we use self-reducibility of _P_ to reduce an instance of size _s_ to some number of instances of size at most \(p^{-1}(p(s)^\alpha)\) for some \(0<\alpha<1\) to be determined later. We apply the given reduction from _P_ to _Q_ to each of the new small instances. Whenever the reduction makes an oracle call, we can just take a peek into the lookup table. To do this, we will need to have

\(\nu\ge\frac{logp(p^{-1}(p(s)^\alpha))}{log\gamma}=\frac{logp(s)^\alpha}{log\gamma}=\frac{\alpha}{log\gamma}logp(s).\) (3)

On the other hand, we need<tbc>

\(O((2\beta)^\nu)\le p(s)^\frac{1}{2}.\)

<tbc>This gives us

\(\nu\le\frac{1}{2log2\beta}logp(s).\)

We can pick \(\nu=\frac{1}{2log2\beta}logp(s)\) and then choose \(\alpha>0\) to make the inequality (3) correct too.

Overall, we have a preprocessing that takes time _p(s_)<sup>1/2</sup> and a fine-grained reduction that solves all of the oracle calls in polynomial time. By the properties of fine-grained reduction this means that we will solve all the small instances of _P_ in time

\(O(p(s)^{1/2}+p(s)^{(1-\delta)})=O(p(s)^{1-\delta})\)

for some \(\delta>0\).

## References

