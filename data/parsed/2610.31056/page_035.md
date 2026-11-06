#### Tail Upper Bound.

Hence, the expected size of all three lists is \(\mathcal{O}\left(M^{1/4}\right)\). Using Markov’s inequality, we can say the following

\(\mathbb{P}_{\mathbf{a}^{(L)}}\left(\left|B_{n/2,s_0}^{(L)}\right|\ge poly(n)M^{1/4}\right)\le\frac{\mathbb{E}_{\mathbf{a}^{(L)}}\left(\left|B_{n/2,s_0}^{(L)}\right|\right)}{poly(n)M^{1/4}}\)<br>
\(=\mathcal{O}\left(\frac{1}{poly(n)}\right).\)

Similarly, we have

\(\mathbb{P}_{\mathbf{a}^{(R)}}\left(\left|B_{n/2,s_1}^{(R)}\right|\ge poly(n)M^{1/4}\right)=\mathcal{O}\left(\frac{1}{poly(n)}\right),\)<br>
\(\mathbb{P}_\mathbf{a}\left(\left|B_{s_0,s_1,s_2}\right|\ge poly(n)M^{1/4}\right)=\mathcal{O}\left(\frac{1}{poly(n)}\right).\)

This completes the proof.

**Remark 2.** _Combining the above tail bound for the running time and the success probability of the algorithm, we can claim that the filtering algorithm for_ \(\Omega(1)\) _fraction of instances will have running time_ O_<sup>⋆</sup>_(2<sup>_n/_4</sup>) _and the final list will have a collision._

## 7 Integer average-case: Proof of Theorem 1.3

In this section, we present the proof of Theorem 1.3. Firstly, recall the definition of the **ACI-RESS** problem.

#### Average-Case Integer Restricted Equal Subset Sum (ACI-RESS).

Given two integers _M_ and _n_ divisible by 4 as input, such that \(M\le 2^n\).

Choose _n_ integers _a_<sub>1</sub>_,a_<sub>2</sub>_,...,a<sub>n</sub>_ uniformly randomly from \[_M_\] and the task is to find a non- trivial integer collision, i.e., two _distinct_ sets \(\mathbf{u},\mathbf{v}\in\{0,1\}^n\) such that **a.u**=**a.v**, where . denotes the standard dot product.

Similar to the Modular case, w.l.o.g. we can assume that \(M=\Theta(2^n)\). The algorithm for solving **ACI-RESS** will remain the same as in the modular case. The inputs will have a different structure as mentioned in Algorithm 4. We give Algorithm 4 for Theorem 1.3, for completeness.

In the modular case, we observed that the sum of random variables modulo _p_, _q_, and _r_ is uniformly distributed over their corresponding supports, and to obtain a collision modulo _M=pqr_, one must additionally ensure collision in the residual _r_-part, after which the Chinese Remainder Theorem yields a collision modulo _M_. In the integer setting, agreement modulo _pq_ remains the same as in the modular setting. Still, after that, one must additionally understand carry propagation from the sum of mod-_pq_ variables and the collision over the remaining high-order bits. This is the bottleneck in analyzing the integer case.

#### Unstructured M.

Firstly, we divide _M_ by the product of the integers _p_ and _q_ (the parameters of the algorithm <sup>15</sup>). Let _r_ and _s_ be the quotient and remainder of the division as mentioned below

\(M=r\cdot pq+s,\)

<sup>15</sup>Parameters _p_ and _q_ are chosen such that \(\lfloor M/pq\rfloor\) is co-prime to _p_ and _q_ both.

