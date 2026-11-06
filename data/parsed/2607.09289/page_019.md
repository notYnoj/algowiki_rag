Thus, in every case, the numerator is \(\Theta^*(2^{H(\beta)n})\). Therefore, the good split occurs with probability \(\Theta^*(1)\), and in particular with probability at least 1/poly(_n_). This completes the proof.

We now turn to the time and space complexity analysis of Algorithm 4.

**Theorem 5.12.** _Let_ \(\ell'\) _be the minimum solution ratio. For every constant_ \(\alpha>0\)_, there is a Monte Carlo algorithm for ESS that uses_ \(O^*(2^{\alpha n})\) _space and runs in_ \(O^*(2^{\tau_\mathrm{sbu}(\ell^\prime,\alpha)n})\) _time, where_ \(\tau_\mathrm{sbu}(\ell',\alpha)\) _is defined by_

\(\tau_\mathrm{sbu}(\ell',\alpha)=\left(1-\frac{\mathrm{min}\left\{\frac{4\alpha}{H(\ell')+\ell^\prime},1\right\}}{2}\right)(H(\ell')+\ell').\) (12)

_Proof._ If \((H(\ell')+\ell')/4\le\alpha\), then by Lemma 3.9, the algorithm uses \(O^*(2^{\frac{n}{4}(H(\ell^\prime)+\ell^\prime)})\le O^*(2^{\alpha n})\) space and runs in \(O^*(2^{\frac{n}{2}(H(\ell^\prime)+\ell^\prime)})\) time. This is consistent with the definition of \(\tau_\mathrm{sbu}(\ell',\alpha)\), since \(\mathrm{min}\left\{\frac{4\alpha}{H(\ell^\prime)+\ell^\prime},1\right\}=1\) in this case. Thus, it remains to consider the case \((H(\ell')+\ell')/4>\alpha\).

By Lemma 5.11, repeating the algorithm poly(_n_) times amplifies to a constant the probability that<tbc>

\(|(A\cup B)\cap S_1|=\lfloor\beta\ell\rfloor\text{and}|(A\cup B)\cap S_2|=\ell-\lfloor\beta\ell\rfloor,\)

<tbc>where \(A,B\subseteq S\) are a minimum solution. When this good split occurs, Line 2 of Algorithm 4 eventually considers \(X_2=A\cap S_2\) and \(Y_2=B\cap S_2\), since it enumerates all subsets \(X_2,Y_2\subseteq S_2\) such that \(X_2\cap Y_2=\emptyset\) and \(|X_2|+|Y_2|=\ell-\lfloor\beta\ell\rfloor\). This enumeration takes

\(O\left(\genfrac(){pt}{2}{n-\lfloor\beta n\rfloor}{\ell-\lfloor\beta\ell\rfloor}2^{\ell-\lfloor\beta\ell\rfloor}\right)=O^*(2^{(H(\ell^\prime)+\ell^\prime)(1-\beta)n})\)

time and polynomial space, since the algorithm stores only one candidate pair (_X_<sub>2</sub>_,Y_<sub>2</sub>) at a time, and \(\genfrac(){pt}{2}{n-\lfloor\beta n\rfloor}{\ell-\lfloor\beta\ell\rfloor}=O^*(2^{H(\ell^\prime)(1-\beta)n})\). To see this binomial-coefficient bound, if \(n-\lfloor\beta n\rfloor=O(1)\), then the binomial coefficient is polynomially bounded. Otherwise, we have \(\left|\frac{\ell-\lfloor\beta\ell\rfloor}{n-\lfloor\beta n\rfloor}-\ell'\right|\le O\left(\frac{1}{(1-\beta)n}\right)\), and the claim follows from Fact 2.2.

For each generated pair _X_<sub>2</sub>_,Y_<sub>2</sub>, we apply Lemma 5.10 to _S_<sub>1</sub> with target integer \(\kappa=\sum(Y_2)-\sum(X_2)\). When the good split occurs and the enumeration reaches \(X_2=A\cap S_2\) and \(Y_2=B\cap S_2\), the subsets \(A\cap S_1\) and \(B\cap S_1\) form a minimum solution to this Target ESS instance, with minimum solution size \(|A\cap S_1|+|B\cap S_1|=\lfloor\beta\ell\rfloor\). Thus, applying Lemma 5.10 with this minimum solution size parameter, we find, with constant probability, subsets \(X_1,Y_1\subseteq S_1\) such that \(\sum(X_1)-\sum(Y_1)=\sum(Y_2)-\sum(X_2)\) in

\(O^*\left(2^{\frac{\lfloor\beta n\rfloor}{2}\left(H\left(\frac{\lfloor\beta\ell\rfloor}{\lfloor\beta n\rfloor}\right)+\frac{\lfloor\beta\ell\rfloor}{\lfloor\beta n\rfloor}\right)}\right)=O^*\left(2^{\frac{\beta}{2}(H(\ell^\prime)+\ell^\prime)n}\right)\)

time. The equality follows from \(\left|\frac{\lfloor\beta\ell\rfloor}{\lfloor\beta n\rfloor}-\ell'\right|\le O(1/n)\) and Fact 2.2, since \(\beta\) is lower-bounded by a constant \(\alpha>0\). Then \(\sum(X_1)+\sum(X_2)=\sum(Y_1)+\sum(Y_2)\). Since _S_<sub>1</sub> and _S_<sub>2</sub> are disjoint, we also have \(X_1\cap X_2=\emptyset\) and \(Y_1\cap Y_2=\emptyset\). Thus, \((X_1\cup X_2,Y_1\cup Y_2)\) is a valid ESS solution.

The overall time complexity is

\(O^*(2^{(H(\ell^\prime)+\ell^\prime)(1-\beta)n})\cdot O^*\left(2^{\frac{\beta}{2}(H(\ell^\prime)+\ell^\prime)n}\right)=O^*(2^{(1-\frac{\beta}{2})(H(\ell^\prime)+\ell^\prime)n}).\)

In this case, we have \(\beta=\frac{4\alpha}{H(\ell^\prime)+\ell^\prime}<1\). Thus, the above bound is consistent with the definition of \(\tau_\mathrm{sbu}(\ell',\alpha)\). This completes the proof.

