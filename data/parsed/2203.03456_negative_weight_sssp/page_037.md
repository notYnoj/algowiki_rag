**Lemma D.3.** _For any i,_ \(Pr_{R_1,\dots,R_i}[X_i|I_i]\le pw(u,v)\)_. (Recall that p_=min{1,40log(_n)/D}.)_

We first show that Lemma D.3 completes the proof:

_Proof of Lemma 6.9 given Lemma D.3._ By Observation D.1 and (13) we have<sup>24</sup>

\(Pr[(u,v)\in E^{boundary}]=\sum_{i\ge 0}Pr_{R_1,\dots,R_i}[I_i\wedge X_i]=\sum_{i\ge 0}Pr[I_i]\cdot Pr[X_i|I_i]\)<br>
\(\le pw(u,v)\cdot\sum_{i\ge 0}Pr[I_i]\le pw(u,v)=O(log(n)\cdot w(u,v)/D).\)

To prove Lemma D.3 we use the following claim, which is the crux of the analysis. The claim allows us to fix the first _i_-1 random variables _R_<sub>1</sub>_,...,R_<sub>_i_-1</sub> and only treat _R<sub>i</sub>_ as random.

**Claim D.4.** _Fix any instantiations of the first i_-1 _random variables R_<sub>1</sub>=_r_<sub>1</sub>_,...,R_<sub>_i_-1</sub>=_r_<sub>_i_-1</sub> _such that the resulting graph G<sub>i</sub>=G(r_<sub>1</sub>_,...,r_<sub>_i_-1</sub>) _contains both u and v. Then,_ \(Pr_{R_i}[X_i|I_i]\le pw(u,v)\).

_Proof of Lemma D.3 assuming Claim D.4._ Applying the law of total probability (13) over all possible instantiations _r_<sub>1</sub>_,...,r_<sub>_i_-1</sub> of _R_<sub>1</sub>_,...,R_<sub>_i_-1</sub> we have

\(Pr_{R_1,\dots,R_i}[X_i|I_i]=\sum_{r_1,\dots,r_{i-1}}Pr_{R_i}[X_i|I_i\wedge R_1=r_1\wedge\dots\wedge R_{i-1}=r_{i-1}]\cdot Pr[R_1=r_1\wedge\dots\wedge R_{i-1}=r_{i-1}]\) (14)

To bound the above, we consider two cases. If _R_<sub>1</sub>=_r_<sub>1</sub>_,...,R_<sub>_i_-1</sub>=_r_<sub>_i_-1</sub> are such that _G<sub>i</sub>=G(r_<sub>1</sub>_,...,r_<sub>_i_-1</sub>) does not contain _u_ or does not contain _v_ then by definition _I<sub>i</sub>_ is false, so \(Pr_{R_i}[X_i|I_i\wedge R_1=r_1\wedge\dots\wedge R_{i-1}=r_{i-1}]=0\). (Here we are using Assumption D.2.) The second case is that _G<sub>i</sub>=G(r_<sub>1</sub>_,...,r_<sub>_i_-1</sub>) contains both _u_ and _v_, in which case we can apply Claim D.4. Thus, in either case, we have

\(Pr_{R_i}[X_i|I_i\wedge R_1=r_1\wedge\dots\wedge R_{i-1}=r_{i-1}]\le pw(u,v)\) (15)

Combining (14) and (15) we have

\(Pr_{R_1,\dots,R_i}[X_i|I_i]\le pw(u,v)\sum_{r_1,\dots,r_{i-1}}Pr[R_1=r_1\wedge\dots\wedge R_{i-1}=r_{i-1}]=pw(u,v).\)

All that remains is to prove Claim D.4.

_Proof of Claim D.4._ Recall that in this claim we have a fixed graph _G<sub>i</sub>_ that contains both _u_ and _v_ and that the only randomness now comes from _R<sub>i</sub>_∼Geo(_p_). Note also that the LDD algorithm (Algorithm 3) is removing vertices and edges from the graph _G_ over time, and that by when the algorithm reaches _s<sub>i</sub>_, the remaining graph _G_ that it is working on is by definition _G=G<sub>i</sub>_.

For the rest of this proof, we will assume that the algorithm grows an out-ball \(\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,R_i)\); the case for an in-ball is exactly analogous. We thus have:

\(Pr[X_i|I_i]=Pr[v\notin\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,R_i))|u\in\mathrm{Ball}_\mathrm{G}^\mathrm{out}(s_i,R_i))\)<br>
\(=Pr[R_i<\mathrm{dist}_G(s,v)|R_i\ge\mathrm{dist}_G(s,u)]\)<br>
\(\le Pr[R_i<\mathrm{dist}_G(s,u)+w(u,v)|R_i\ge\mathrm{dist}_G(s,u)]\)

<sup>24</sup>Here we use Assumption D.2; otherwise, some of the sums must be over all _i_ such that Pr\[_I<sub>i</sub>_\]_\>_0.

