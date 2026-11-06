## B Other Results

### B.1 Hardness of Approximating DSG in Unweighted Graphs

In this section, we generalize the lower bound of Lemma 3.5 to unweighted graphs.

**Lemma B.1.** The randomized query complexity of a \((2-\delta)\)-approximation for DSG in simple graphs is \(\Omega(n\delta/logn)\), for any \(\delta>0\).

_Proof._ Reduction from DISJ_<sub>N</sub>(x,y_) on _N_ bits. Let \(t=2/\delta\). We will define a graph _G_ on _n=O(Nt_) vertices. For each index _i_, we construct a gadget with 3_t_-1 vertices across _a<sub>i</sub>,c<sub>i</sub>_, and three sets _B<sub>i</sub>,D<sub>i</sub>_, and _V<sub>i</sub>_ of _t_-1 vertices each. There is a star between _a<sub>i</sub>_ and _V<sub>i</sub>_ if _x<sub>i</sub>_=1, otherwise a star between _a<sub>i</sub>_ and _B<sub>i</sub>_. Similarly, there is a star between _c<sub>i</sub>_ and _V<sub>i</sub>_ if _y<sub>i</sub>_=1, otherwise a star between _c<sub>i</sub>_ and _D<sub>i</sub>_. If DISJ_<sub>N</sub>(x,y_), then \(\rho^*(G)=(t-1)/t\). Otherwise, let _i_ be an index where _x<sub>i</sub>=y<sub>i</sub>_. Then \(\rho^*(G)=\rho(\{a_i,c_i\}\cup V_i)=2(t-1)/(t+1)\).

Observe that the two players can simulate a cut query on _G_ with _O_(log_n_) bits of communication. Assume that they have an _f(n_)-query \((2-\delta)\)-approximation for DSG. The players can then solve DISJ_<sub>N</sub>(x,y_) by outputting `False` if they find a subgraph of density at least \(\frac{2(t-1)}{t+1}/\frac{2(t-1)}{t}=t/(t+1)>(t-1)/t\), and `True` otherwise. This gives an _O(f(n_)log(_n_)) bit communication protocol for this problem. However, the randomized communication complexity of DISJ is \(\Omega(N)=\Omega(n\delta)\) \[22\]. Thus, \(f(n)=\Omega(n\delta/logn)\), as claimed.

As a result, a \((2-\delta)\)-approximation for DSG any constant \(\delta=\Omega(1)\) requires \(\Omega(n/logn)\) queries.

### B.2 Deterministic \((2+\varepsilon)\)-Approximation for DSG

We observe that the streaming DSG algorithm of Bahmani et al. \[4\] can be implemented in the cut query model.

**Proposition 1.** Let _G_=(_V,E_) be a weighted graph. There is a deterministic algorithm that makes \(O(n/\varepsilon)\mathtt{cut}\) queries and returns a \((2+\varepsilon)\)-approximation to the densest subgraph of _G_.

_Proof._ We begin by giving the algorithm’s pseudocode, where we use the Cross primitive to learn induced degrees.

**Algorithm 3**

**Require:** \(\varepsilon>0\)<br>
\(S,S^*\leftarrow V\)<br>
while \(S\neq\emptyset\) do<br>
   for all \(v\in S\) do<br>
   \(deg_S(v)\leftarrow\mathrm{Cross}(\{v\},S\backslash\{v\})\triangleright 3|S|\) queries each pass<br>
   \(\rho(S)\leftarrow\left(\sum_{v\in S}deg_S(v)\right)/2|S|\)<br>
   if \(\rho(S)\ge\rho(S^*)\) then<br>
   \(S^*\leftarrow S\)<br>
   \(A(S)\leftarrow\{v\in S|deg_S(v)\le 2(1+\varepsilon)\rho(S)\}\)<br>
   \(S\leftarrow S\backslash A(S)\)<br>
return S<sup>∗</sup>

The approximation guarantee of Algorithm 3 follows directly from \[4, Lemma 3\]. To bound the query complexity, we appeal to the following property.

**Proposition 10** (\[4, Lemma 4\])**.** The cardinality of the remaining set _S_ decreases by a factor at least \(1/(1+\varepsilon)\) each pass.

