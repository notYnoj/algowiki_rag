We finally argue that any witness of \((A'_s*B'_t)[k^*]\) is also a witness of (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\]. Let _i_ be a witness of \((A'_s*B'_t)[k^*]\). Let _j=k_<sup>∗</sup>-_i_. By definition, there exist \(i'\ge i\) and \(j'\ge j\) such that<tbc>

\((A'_s*B'_t)[k^*]=A_s[i']+B_t[j'].\)

<tbc>Suppose that \(i'+j'>k^*\). Then<tbc>

\(\phi(i^*,A[i^*])+\phi(j^*,B[j^*])<\phi(i',A[i'])+\phi(j',B[j']),\)

<tbc>and thus by the same reasoning as above,<tbc>

\(A_s[i^*]+B_t[j^*]<A_s[i']+B_t[j'].\)

<tbc>But then we reach the contradiction that<tbc>

\((A'_s*B'_t)[k^*]\le A'_s[i^*]+B'_t[j^*]\le A_s[i^*]+B_t[j^*]<A_s[i']+B_t[j']=(A'_s*B'_t)[k^*],\)

<tbc>and must have \(i'+j'=k^*\) instead. Combined with \(i'\ge i\), \(j'\ge j\) and _i+j=k_<sup>∗</sup>, we conclude that \(i=i'\) and \(j=j'\). Recall that we initially picked _i_ as an arbitrary witness of \((A'_s*B'_t)[k^*]\). We have thus argued that

\((A'_s*B'_t)[k^*]=min_{i+j=k^*}(A_s[i]+B_t[j]),\)

and so the witnesses of \((A'_s*B'_t)[k^*]\) and (_A<sub>s</sub>∗B<sub>t</sub>_)\[_k_<sup>∗</sup>\] are identical.

## Running Time.

Initially, we call Lemma 5.3 to reduce from one given instance to \(O(n^\epsilon)\) listing instances, each provided with a low-doubling container. Lemma 5.3 runs in time \(O(n^{2-\delta})\) for some constant \(\delta=\delta(\rho,\epsilon)>0\). For each instance we call the algorithm implied by Hypothesis 1.7 on the container set \(\phi(H)\). This set has size \(N=O(n^{2-2\rho})\) and doubling \(K=O(n^\epsilon)\), and so this takes time \(O(n^{2-2\rho+O(\epsilon)})\). We then apply Lemma 5.9 in time<tbc>

\(|Y-\phi(H)||S|(logu)^{O(1)}=NK^{2c+2}(logu)^{O(1)}=n^{2-2\rho+O(\epsilon)}(logu)^{O(1)}.\)

<tbc>Then we reduce each listing instance (with threshold \(t=O(n^{2\rho})\)) further to \(\widetilde{O}(n^{2\rho})\) plain Min Plus Convolution subinstances by Lemma 2.14. This leaves us with \(\widetilde{O}(n^{2\rho+\epsilon})\) instances that the main part of the algorithm treats. For each pair of shifts \(s,t\in S\) we construct the sequences _A<sub>s</sub>,B<sub>t</sub>_ and \(A'_s,B'_t\) in linear time. Assuming the premise of Lemma 5.8, by Lemma 5.6 we can compute their convolution in time \(O(n^{2-\epsilon_0})\) for some \(\epsilon_0>0\). The total time is

\(\big(n^{2-\delta}+n^{2-2\rho+O(\epsilon)}+n^{2\rho+\epsilon+2-\epsilon_0}\big)(logu)^{O(1)}.\)

This becomes subquadratic for, say, \(\rho=\epsilon_0/8\) and by choosing \(0<\epsilon\le\epsilon_0/2\) sufficiently small so that the \(O(\epsilon)\) term becomes at most \(\rho\).

