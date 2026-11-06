Input: Input set S and minimum solution size \(\ell\)<br>
Output: An ESS solution for S if one exists; otherwise, NO<br>
Space bound: \(O^*(2^{\alpha n})\)<br>
Let \(\ell'=\ell/n\). If \(\frac{1}{4}(H(\ell')+\ell')\le\alpha\), then apply Lemma 3.9 to the whole input set S and return its output. Otherwise, set \(\beta=\frac{4\alpha}{H(\ell^\prime)+\ell^\prime}<1\). Randomly split the input set S into two disjoint sets \(S_1,S_2\subseteq S\) such that \(|S_1|=\lfloor\beta n\rfloor\), and \(|S_2|=n-\lfloor\beta n\rfloor\).<br>
Generate the triples (c,X<sub>2</sub>,Y<sub>2</sub>) one by one, where \(X_2,Y_2\subseteq S_2\), \(X_2\cap Y_2=\emptyset\), \(|X_2|+|Y_2|=\ell-\lfloor\beta\ell\rfloor\), and \(c=\sum(X_2)-\sum(Y_2)\). We do not store all such triples simultaneously; instead, each generated triple is processed immediately. For each generated triple (c,X<sub>2</sub>,Y<sub>2</sub>), apply Lemma 5.10 to the input set S<sub>1</sub> with target integer \(\kappa=-c\) and minimum solution size parameter \(\lfloor\beta\ell\rfloor\). If Lemma 5.10 finds subsets \(X_1,Y_1\subseteq S_1\) such that \(\sum(X_1)-\sum(Y_1)=-c\), then return \((X_1\cup X_2\), \(Y_1\cup Y_2)\).<br>
Return NO.

**Lemma 5.10** (\[25, Appendix E of the full version\])**.** _The_ Target Equal-Subset-Sum (Target ESS) Problem _is defined as follows. Given an input set S of n integers and a target integer_ \(\kappa\)_, the task is to find two distinct subsets_ \(A,B\subseteq S\) _such that_ \(\sum(A)-\sum(B)=\kappa\)_, or to report that no such pair of subsets exists. If such subset pairs exist, let_ \(\ell\) _denote the minimum value of_ |A|+|B| _over all pairs of distinct subsets_ \(A,B\subseteq S\) _satisfying_ \(\sum(A)-\sum(B)=\kappa\)_. We define a minimum solution of the Target ESS instance to be a pair_ (_A,B_) _attaining this minimum, and let_ \(\ell'=\ell/n\) _denote the minimum solution ratio of the Target ESS instance. Then, for any Target ESS instance_ \((S,\kappa)\) _with minimum solution ratio_ \(\ell'\)_, there is a Monte Carlo algorithm that solves the_ Target ESS Problem _in_ \(O^*(2^{\frac{n}{2}(H(\ell^\prime)+\ell^\prime)})\) _time and_ \(O^*(2^{\frac{n}{4}(H(\ell^\prime)+\ell^\prime)})\) _space._

Algorithm 4 relies on the assumption that S<sub>1</sub> contains roughly a \(\beta\)-fraction of the elements of a minimum solution, just as it contains a \(\beta\)-fraction of the input set. We show that such a split occurs with probability at least \(\Omega(1/\text{poly}(n))\).

**Lemma 5.11.** _Let_ \(A,B\subseteq S\) _be a minimum solution with_ \(|A\cup B|=\ell\)_. Then_ \(|(A\cup B)\cap S_1|=\lfloor\beta\ell\rfloor\) _and_ \(|(A\cup B)\cap S_2|=\ell-\lfloor\beta\ell\rfloor\) _hold with probability at least_ \(\Omega(1/\text{poly}(n))\).

_Proof._ The probability that such a good split occurs is \(\frac{\genfrac(){pt}{2}{\ell}{\lfloor\beta\ell\rfloor}\genfrac(){pt}{2}{n-\ell}{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}}{\genfrac(){pt}{2}{n}{\lfloor\beta n\rfloor}}\) . The denominator satisfies \(\genfrac(){pt}{2}{n}{\lfloor\beta n\rfloor}=\Theta^*(2^{H(\beta)n})\), since \(\left|\frac{\lfloor\beta n\rfloor}{n}-\beta\right|\le O(1/n)\), together with Fact 2.2.

We show that the numerator is also \(\Theta^*(2^{H(\beta)n})\). If \(\ell=O(1)\), then \(\genfrac(){pt}{2}{\ell}{\lfloor\beta\ell\rfloor}\) is polynomially bounded, and \(\genfrac(){pt}{2}{n-\ell}{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}=\Theta^*(2^{H(\beta)n})\), since \(\left|\frac{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}{n-\ell}-\beta\right|\le O(1/n)\), together with Fact 2.2. Similarly, if \(\ell=n-O(1)\), then \(\genfrac(){pt}{2}{n-\ell}{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}\) is polynomially bounded, and \(\genfrac(){pt}{2}{\ell}{\lfloor\beta\ell\rfloor}=\Theta^*(2^{H(\beta)n})\), since \(\left|\frac{\lfloor\beta\ell\rfloor}{\ell}-\beta\right|\le O(1/n)\), together with Fact 2.2. Otherwise, we have

\(\genfrac(){pt}{2}{\ell}{\lfloor\beta\ell\rfloor}\genfrac(){pt}{2}{n-\ell}{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}=\Theta^*(2^{H(\frac{\lfloor\beta\ell\rfloor}{\ell})\ell})\Theta^*(2^{H(\frac{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}{n-\ell})(n-\ell)})\)<br>
\(=\Theta^*(2^{H(\beta)\ell})\Theta^*(2^{H(\beta)(n-\ell)})=\Theta^*(2^{H(\beta)n}).\)

The second equality follows from \(\left|\frac{\lfloor\beta\ell\rfloor}{\ell}-\beta\right|\le O(1/\ell)\) and \(\left|\frac{\lfloor\beta n\rfloor-\lfloor\beta\ell\rfloor}{n-\ell}-\beta\right|\le O(1/(n-\ell))\), together with Fact 2.2.

**Algorithm 4:** SpaceBoundedUnbalancedESS

