### 6.7 Summary

In the analysis, we have degenerated \(\otimes_{t=1}^{s^\prime} T_{i_t,j_t,k_t}^{\otimes A_{t,1}n_t}\big[\beta_{X,t}^{(1)},\beta_{Y,t}^{(1)},\beta_{Z,t}^{(1)},\varepsilon\big]\) into \(\ge N_\alpha\cdot M_0^{-1-o(1)}\) copies of a level-\((\ell-1)\) interface tensor T<sup>∗</sup> with parameter list

\(\big\{\big(A_{t,1}\cdot n_t\cdot\big(\alpha_t^{(1)}(i',j',k')+\alpha_t^{(1)}(i_t-i',j_t-j',k_t-k')\big),\)<br>
\(i',j',k',\beta_{X,t,i^\prime,j^\prime,k^\prime}^{(1)},\beta_{Y,t,i^\prime,j^\prime,k^\prime}^{(1)},\beta_{Z,t,i^\prime,j^\prime,k^\prime}^{(1)}\big)\big\}_{t\in[s^\prime],i^\prime+j^\prime+k^\prime=2^{\ell-1}}.\)

By plugging in the bounds of \(N_\alpha\) and _M_<sub>0</sub>, we see that the number of copies we obtained (in the first region) is

\(2^{min}\big\{\sum_{t\in[s^\prime]}A_{t,1}\cdot n_t\cdot\big(H(\gamma_{X,t}^{(1)})-P_{\alpha,t}^{(1)}\big),\sum_{t\in[s^\prime]}A_{t,1}\cdot n_t\cdot\big(H(\gamma_{Y,t}^{(1)})-P_{\alpha,t}^{(1)}\big),\sum_{t\in[s^\prime]}A_{t,1}\cdot n_t\cdot\big(H(\beta_{Z,t}^{(1)})-\lambda_{Z,t}^{(1)}\big)\big\}^{-o_{1/\varepsilon}(n)-o(n)}.\)

We conclude the proof by applying the same method to the second and third region, where for the second region we perform asymmetric hashing that shares _Y_ -variable blocks, and for the third region we perform asymmetric hashing that shares _X_-blocks, and taking the tensor product of these returned results.

## 7 Fixing Holes

In this section, we show (by generalizing a result by Duan \[Dua22\]) that we can degenerate a direct sum of some broken copies of an interface tensor into an unbroken copy of the same tensor as long as we only have a small fraction of holes in the _X_-, _Y_ -, _Z_-dimensions. Since our result of fixing holes in all _X_-, _Y_ -, _Z_-variables might be of independent interest, we present our result in a more general setting.

Let us first describe the setup of this section. We consider a partitioned tensor _T_ on variable sets _X_={_x_<sub>1</sub>_,...,x<sub>N<sub>X</sub></sub>_}, _Y_={_y_<sub>1</sub>_,...,y<sub>N<sub>Y</sub></sub>_}, _Z_={_z_<sub>1</sub>_,...,z<sub>N<sub>Z</sub></sub>_} of size |_X_|=_N<sub>X</sub>_, |_Y_|=_N<sub>Y</sub>_, |_Z_|=_N<sub>Z</sub>_ with partitions \(X=\sqcup_{i=1}^{M_X}X_i\), \(Y=\sqcup_{j=1}^{M_Y}Y_k\), \(Z=\sqcup_{k=1}^{M_Z}Z_k\) into equal-size parts |_X<sub>i</sub>_|=_m<sub>X</sub>_ for all \(i\in[M_X]\), |_Y<sub>j</sub>_|=_m<sub>Y</sub>_ for all \(j\in[M_Y]\), and |_Z<sub>k</sub>_|=_m<sub>Z</sub>_ for all \(k\in[M_K]\). (We use the notation _X<sub>i</sub>_ to represent both the part itself and the set of elements in this part.) Let \(\mathcal{P}_X=\{X_i|i\in[M_X]\}\) denote the set of parts in the partition of _X_, and similarly let P_<sub>Y</sub>,_P_<sub>Z</sub>_ denote the set of parts in the partition of _Y_ and _Z_ respectively. Note that by definition \(N_X=M_X\cdot m_X\), \(N_Y=M_Y\cdot m_Y\), \(N_Z=M_Z\cdot m_Z\) and |P_<sub>X</sub>_|=_M<sub>X</sub>_, |P_<sub>Y</sub>_|=_M<sub>Y</sub>_, |P_<sub>Z</sub>_|=_M<sub>Z</sub>_.

We consider the broken copies of _T_ where some of the _X_-, _Y_ - and _Z_-parts are missing which we call the _holes_. (Equivalently, the variables in a part are either all present or all missing.) More specifically, we say that _T_<sub>hole</sub> is _a broken copy of T with holes_ \(P_X^{(0)}\subseteq M_X\), \(P_Y^{(0)}\subseteq M_Y\), \(P_Z^{(0)}\subseteq M_Z\) when

\(T_\mathrm{hole}=T\big|_{X\backslash\sqcup_{X_t\in P_X^{(0)}}X_t,Y\backslash\sqcup_{Y_t\in P_Y^{(0)}Y_t,Z\backslash\sqcup_{Z_t\in P_Z^{(0)}}Z_t}}\) (24)

is obtained from _T_ via zeroing out the variables in the parts \(P_X^{(0)}\subseteq\mathcal{P}_X\), \(P_Y^{(0)}\subseteq\mathcal{P}_Y\), \(P_Z^{(0)}\subseteq\mathcal{P}_Z\). For simplicity, we define the notation

\(T\big|_{P_X,P_Y,P_Z}:=T\big|_{\sqcup_{X_t\in P_X}X_t,\sqcup_{Y_t\in P_YY_t},\sqcup_{Z_t\in P_ZZ_t}}\)

to represent the subtensor of _T_ over the set of parts _P<sub>X</sub>,P<sub>Y</sub>,P<sub>Z</sub>_. With this notation, Eq. (24) can be rewritten as

\(T_\mathrm{hole}=T\big|\big|_{\mathcal{P}_X\backslash P_X^{(0)},\mathcal{P}_Y\backslash P_Y^{(0)},\mathcal{P}_Z\backslash P_Z^{(0)}}.\)

