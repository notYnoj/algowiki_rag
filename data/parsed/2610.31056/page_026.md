Choose _n_ elements _a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_ uniformly randomly from Z_<sub>M</sub>_ and the task is to find a non-trivial collision modulo _M_, i.e., find two _distinct_ sets \(\mathbf{u},\mathbf{v}\in\{0,1\}^n\) and \((\mathbf{u},\mathbf{v})\neq(0^n,0^n)\) such that \(\mathbf{a}.\mathbf{u}\equiv\mathbf{a}.\mathbf{v}modM\), where . denotes the standard dot product.

**Discussion on the modulus** _M_**.** Let _M\<_2_<sup>n</sup>_, then we define \(n':=\lceil log(M)\rceil\). And, we only consider any \(n'\) elements from the list {_a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_}. Then, our problem reduces to a problem with input modulus _M_ and integer \(n'\), where we can observe that \(2^{n^\prime-1}<M\le 2^{n^\prime}\).

Here, we first introduce the Filtering Algorithm 3, which, on average, solves **ACM-RESS** problem.

Input: \((a_1,a_2,\dots,a_n)\in\mathbb{Z}_M^n\); Parameters: \(s_0,s_1\in\mathbb{Z}_p\) and \(s_2\in\mathbb{Z}_q\)<br>
Output: A non-trivial modular collision or \(\perp\)<br>
Build two mod-p DP tables storing the sizes of the following sets \(\forall s\in\mathbb{Z}_p\) and \(1\le i\le n/2\)<br>
\(B_{i,s}^{(L)}:=\left\{\mathbf{u}\in\{0,1\}^i\middle|\sum_{j=1}^ia_ju_j\equiv smodp\right\},\)<br>
\(B_{i,s}^{(R)}:=\left\{\mathbf{v}\in\{0,1\}^i\middle|\sum_{j=1}^ia_{n/2+j}v_j\equiv smodp\right\}.\)<br>
Compute the bins \(B_{n/2,s_0}^{(L)}\) and \(B_{n/2,s_1}^{(R)}\) by backtracing the DP table; look for a collision in these sets, else continue.<br>
Construct the following set<br>
\(B_{s_0,s_1,s_2}:=\left\{\mathbf{u}||\mathbf{v}\in\{0,1\}^n\middle|\mathbf{u}\in B_{n/2,s_0}^{(L)},\mathbf{v}\in B_{n/2,s_1}^{(R)},\mathbf{a}^{(L)}\cdot\mathbf{u}+\mathbf{a}^{(R)}\cdot\mathbf{v}\equiv s_2modq,\right\}\)<br>
Look for a non-trivial collision in this list B<sub>s<sub>0</sub>,s<sub>1</sub>,s<sub>2</sub></sub>. If one is found, it outputs this collision; otherwise, it outputs \(\perp\).

**Observation.** Using **CRT** (Chinese Remainder Theorem), we can say that every input _a<sub>i</sub>_ can be split into three independent random variables \(a_i^{(p)},a_i^{(q)}\), and \(a_i^{(r)}\), which are images of the CRT isomorphism. Then, we can first observe that the filtering Algorithm 3 only depends on the random vectors \(\mathbf{a}^{(p)}:=(a_1^{(p)},a_2^{(p)},\dots,a_n^{(p)})\) and \(\mathbf{a}^{(q)}:=(a_1^{(q)},a_2^{(q)},\dots,a_n^{(q)})\).

## 6.1 Success Probability

The filtering algorithm succeeds when it outputs a desired collision for the input instance. We are interested in computing a lower bound of the fraction of all the input instances for which the algorithm succeeds. The following theorem gives us the success probability of Algorithm 3.

**Lemma 6.0.1.** _Let M,n,p, and q be the same as defined in the above problem **ACM-RESS**. Then the following holds for the Algorithm 3_

\(\mathbb{P}_\mathbf{a}\left(Algorithm3\text{\textit{succeeds}}\right)=\Omega\left(1\right).\)

**Algorithm 3:** Algorithm for Theorem 1.4.

