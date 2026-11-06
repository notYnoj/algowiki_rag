## 3 General Procedure

The following is the general procedure for _N_ random variables of which we want the truncated _k_-th order statistic. Denote the unrestricted _N_-dimensional unit hypercube from which we will draw our original uniform sample as _C_=\[0,1\]_<sup>N</sup>_, and let points in this space have coordinates given by \((u_1,\cdots,u_N)\). Let the bound restricted hypercube be \(C'\) with points having coordinates \((u'_1,\cdots,u'_N)\). Our original bounds, _A_ and _B_, apply to the final _Y_ and not the uniform samples. By applying the CDFs, _a<sub>i</sub>=F<sub>X<sub>i</sub></sub>(A_) and _b<sub>i</sub>=F<sub>X<sub>i</sub></sub>(B_), we obtain the appropriate limits on \(u'_i\). Using these definitions, we can see that the restricted region \(C'\) from which we need to generate uniform samples can be written as:

\(C'=\left\{(u'_1,\cdots,u'_N):a_j<u'_j<b_j0<u'_j<1\text{for at least}k\text{of the}j\in\{1,\cdots,N\}\right\}\)

Our procedure divides _C_ and \(C'\) into the corresponding regions, _R<sub>s</sub>_ and \(R'_s\), and determines the mapping of points from _R<sub>s</sub>_ to \(R'_s\). After the mapping we can use ordinary inverse transform sampling to generate our draws from _Y_ .

### 3.1 Space Segmentation

Each draw must satisfy the constraint that at least _k_ of the _X<sub>i</sub>_ must be less _B_ in order for _Y_ to be less than _B_, and at least _N-k_+1 of them must be greater than _A_ in order for _Y_ to be greater than _A_. To accomplish the task, we enumerate all the possible combinations of allowed _X<sub>i</sub>_ orderings. To accomplish this, let us ease the notation of each _X<sub>i</sub>_ to be represented by its index _i_, and let \(I=\{1,\cdots,N\}\) as the set of all possible indices. Then, we can define two sets composed of subsets of _I_

\(S_A=\{s\in\mathcal{P}(I):|s|\ge N-k+1\}\)<br>
\(S_B=\{s\in\mathcal{P}(I):|s|\ge k\}\)

where P(_I_) is the power set of _I_. The first set, _S<sub>A</sub>_, is the list of possible combinations of the _X<sub>i</sub>_ which could fulfill the _A_ bound and likewise for _S<sub>B</sub>_. However, not every pair of \(s_A\in S_A\) and \(s_B\in S_B\) is a valid combination. For instance, if _N_=4_,k_=3 and we have two sets _s<sub>A</sub>_={1,2}_,s<sub>B</sub>_={1,2,4}, then we see that \(3\notin s_A\) and \(3\notin s_B\). This means that _X_<sub>3</sub>_\<A_ and _X_<sub>3</sub>_\>B_ but since _A\<B_, then we have a contradiction. In order to avoid such problems, we must impose two restrictions on the pair: \(s_A\cup s_B=I\) so that no index is omitted and \(s_A\cap s_B\neq\emptyset\) so that there is a value satisfying the bounds to be our _k_-th order statistic. We<tbc>

