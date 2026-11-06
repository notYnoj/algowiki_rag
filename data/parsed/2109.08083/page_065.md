<tbc>for every vertex \(v\in V(0)\). Thus we would guess that \(Q(i)\approx(1\pm b)n^2p^4\), and \(d_v(i)\approx(1\pm b)np^3\) for every \(v\in V(i)\).

We’ll show that, in fact, for every \(0\le i\le(1-n^{-\alpha_\mathrm{gr}})n\), where \(\alpha_\mathrm{gr}:=10^{-25}\) we have that

\(Q(i)=n^2p^4\pm e_q\text{and}d_v(i)=np^3\pm e_d\)

for every \(v\in V(i)\), where

\(e_q=2(1-4\mathrm{log}p)bn^2\text{and}e_d=2(1-4\mathrm{log}p)b^{2/3}n.\)

Note that we chose such errors with no attempt to optimise the process, and instead choose them to be sufficient for the process to complete to reach _H_ as per Theorem 3.28.

Additionally we consider our secondary random variables which are of three types: the number of vertices remaining in a particular subset \(S\subseteq V(\mathcal{T})\), the number of edges containing a fixed vertex _v_, with subset-style conditions on the ‘types’ of edge to be counted (‘degree-type conditions’), and the number of zero- sum configurations of specific ‘types’ for a fixed edge _e_. (Note that our degree- type conditions would include the actual degree _d<sub>v</sub>(i_) already considered in the primary random variables but since _d<sub>v</sub>(i_) plays a more crucial role in tracking this process than the other degree-type properties we use the different notation for clarity and since we require a tighter error bound.) We write _V<sub>S</sub>(i_) to denote the random variable tracking |_V(T<sub>i</sub>[S_])|, _E<sub>v,S</sub>(i_) to denote the random variable tracking |_E<sub>T<sub>i</sub></sub>(v,S_)| where _S_ represents any of the subsets of _V_(T) which are considered in degree-type conditions in Theorem 3.28, and _Z_<sub>A</sub>(_i_) to denote the random variables tracking zero-sum configurations, where A describes both the fixed edge for which we are tracking configurations as well as all details of the type of configuration being tracked. By assumption, we have that \(V_S(0)=(1\pm b)|S|\), \(E_{v,S}(0)=(1\pm b)|E_\mathcal{T}(v,S)|\), and _Z_<sub>A</sub>(0)=_Z_<sub>A</sub>(T<sup>-_A_<sup>∗</sup></sup>), where \(Z_\mathcal{A}(\mathcal{T}^{-A^*})=(1\pm b)Z_\mathcal{A}(\mathcal{T})\) if A considers configurations containing a fixed bad edge _e_ (with positive sign), or a fixed edge of type \((\alpha,\beta,0)\) with \(\alpha\neq 0\) (with negative sign). If A considers configurations containing a fixed edge of type (0,1,3) with positive sign, or containing a fixed bad edge and at least two bad edges in total with positive sign, we are only interested in tracking _Z_<sub>A</sub> if \(Z_\mathcal{A}(\mathcal{T}^{-A^*})=\Omega(k_it_1n^{-12\alpha_\mathrm{gr}})\). Similarly, if A considers configurations containing a fixed edge of type (0,1,3) or (0,0,4) with negative sign, we are only interested in tracking _Z_<sub>A</sub> if \(Z_\mathcal{A}(\mathcal{T}^{-A^*})=\Omega(k_ij_in^{-12\alpha_\mathrm{gr}})\). As in the case for the primary variables, we define<tbc>

\(e_{E_{v,S}}=2b^{1/3}|E_\mathcal{T}(v,S)|,e_{V_S}=2b^{1/3}|S|,\text{and}e_{Z_\mathcal{A}}=2b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|,\)

<tbc>and we’ll show that whp for every \(0\le i\le(1-n^{-\alpha_\mathrm{gr}})n\) we have that<tbc>

\(E_{v,S}(i)=|E_\mathcal{T}(v,S)|p^3\pm e_{E_{v,S}},\)<br>
\(V_S(i)=|S|p\pm e_{V_S},\)

<tbc>and

\(Z_\mathcal{A}(i)=|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}\pm e_{Z_\mathcal{A}},\)

where the last holds only for A discussed above. Note that for all other A of concern in Theorem 3.28, the statements regarding them are already true, since we can only lose configurations through the random greedy edge removal process. Note additionally that whilst the error terms for the primary variables change with _i_ (since they are dependent on _p_), the error terms for the secondary variables remain

