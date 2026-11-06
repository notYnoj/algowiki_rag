<tbc>**Case 1 (**\(p\cdot n_i\ge 1\)**):** In this case, _B<sub>X</sub>(i_) is rejected with probability \((1-p)^{n_i}\le(1-\frac{1}{n_i})^{n_i}\le\frac{1}{e}\). Thus, _B<sub>X</sub>(i_) is accepted as a promising bucket with probability at least \(1-\frac{1}{e}\in\Omega(1)\).

**Case 2 (**\(p\cdot n_i<1\)**):** Recall that, in this case, _B<sub>X</sub>(i_) is accepted with probability \(\frac{1-(1-p)^{n_i}}{p\cdot n_i}\) . We claim that this probability is at least \(1-\frac{1}{e}\). To see this, consider the function \(f(a,b)=\frac{1-(1-b)^{a/b}}{a}\) for \(a=p\cdot n_i<1\) and \(b=p\in(0,1)\). It can be verified that _f(a,b_) decreases monotonically with respect to _a_. To see this, the partial derivative of _f_ with respect to _a_ is computed as \(\frac{\partial f}{\partial a}=\frac{-\frac{a}{b}\cdot(1-b)^{a/b}\cdot log(1-b)+(1-b)^{a/b}-1}{a^2}\) . Thus, it suffices to consider the sign of the numerator of \(\frac{\partial f}{\partial a}\) . Let _c_=(1-_b_)<sup>1_/b_</sup> and define \(g(x)=-x\cdot c^x\cdot logc+c^x-1=c^x(1-xlogc)-1\). Clearly, _g_(0)=0 and \(g'(x)=-(logc)\cdot c^x+c^x\cdot logc\cdot(1-xlogc)=-x\cdot c^x\cdot(logc)^2<0\) for _x\>_0. This implies that _g(x)\<_0 for \(x\in(0,1)\) and hence, \(\frac{\partial f}{\partial a}<0\) for \(a\in(0,1)\). Thus, we have \(f(a,b)>1-(1-b)^{1/b}>1-\frac{1}{e}\in\Omega(1)\). As a result, _B<sub>X</sub>(i_) is accepted as a promising bucket with probability at least \(\Omega(1)\).

Combining the above two cases, Claim 1 holds. Moreover, our results on random variate generation in Section 3 imply that all the random variates used in Algorithm 4 can be generated in _O_(1) expected time. Putting all the above together, Theorem 4.8 follows. □

Theorem 4.8 implies that, as long as we can answer the PSS queries optimally on the next-level instances, we can answer the PSS query on _X_ optimally. Moreover, observe that the next-level item set size is at most log<sub>2</sub>_N_, logarithmic in the size of _X_. This motivates an idea of recursively applying the same bucket-grouping technique on next-level item set _Y<sub>j</sub>_ of each group _G<sub>X</sub>(j_). When the next-level instance is "small" enough, we use a _lookup table_ to answer the PSS queries on them optimally. While this idea looks natural, certain non-trivial technical challenges remain to be addressed. First, by Lemma 4.2, each recursion level increases the number of next-level instances by a factor of 3. Thus, the recursion cannot be so deep that it exceeds _O_(1) recursion levels. Otherwise, a super-constant factor would be introduced to the query time complexity. Second, having only _O_(1) recursion levels does not reduce the problem size to _O_(1). Thus, it is not trivial to design a lookup table with space consumption bounded by _O(N_). Third, the next-level instances are _dynamic_, depending on the query parameters \((\alpha,\beta)\). However, the lookup table is _static_. As a result, reducing the next-level instances to problems where the lookup table is applicable during the query time is a challenging task.

## 4.2 The Three-Level Sampling Hierarchy

Given a set _S_ of _n_ items, the three-level sampling hierarchy of _S_ is constructed as follows:

\(\bullet\) **Level-1**: Construct BG-Str(_S_);<tbc>

\(\bullet\) **Level-2**: For each group _G<sub>S</sub>(j_) in BG-Str(_S_):<tbc>

- construct BG-Str(_Y<sub>j</sub>_) on the next-level item set _Y<sub>j</sub>_ of _G<sub>S</sub>(j_);<tbc>

- denote each bucket with bucket index _i_ by _B<sub>Y<sub>j</sub></sub>(i_), and each group with group index _k_ by _G<sub>Y<sub>j</sub></sub>(k_);<tbc>

**-** denote the next-level item corresponding to bucket _B<sub>Y<sub>j</sub></sub>(i_) by _z<sub>i</sub>_ and the next-level item set of group _G<sub>Y<sub>j</sub></sub>(k_) by _Z<sub>k</sub>_.<tbc>

**-** **Level-3**: For each group _G<sub>Y<sub>j</sub></sub>(k_) in BG-Str(_Y<sub>j</sub>_),<tbc>

\* construct BG-Str(_Z<sub>k</sub>_) on the next level item set _Z<sub>k</sub>_ of _G<sub>Y<sub>j</sub></sub>(k_);<tbc>

\* denote each bucket with bucket index _i_ by _B<sub>Z<sub>k</sub></sub>(i_) and its corresponding next-level item by _v<sub>i</sub>_;<tbc>

\* denote the set of all the next-level items of the buckets by _V<sub>k</sub>_; the PSS instance on _Z<sub>k</sub>_ is called a _final-level instance_.

Lemma 4.9. _Given a set S of n items, the three-level sampling hierarchy can be constructed in O(n_) _time with O(n_) _space consumption._

