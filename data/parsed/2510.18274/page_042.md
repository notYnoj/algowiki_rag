Let us first argue the correctness. In Step 2, if \(\hat{f}\le 0.99\Delta\), we then know that \(\nu(G)\le\Delta\); hence, simply outputting \(H=\emptyset\) is correct.

Otherwise, we must have \(\hat{f}\ge 0.99\Delta\). In Step 4, we compute _f_. Similar to before, if \(f\le(1-\lambda)\Delta\), we then know that \(\nu(G)\le\Delta\); hence, simply outputting \(H=\emptyset\) is correct.

Otherwise, we must have \(f\ge(1-\lambda)\Delta\). We also know that \(\nu(G)\ge\frac{f}{1+\lambda}\). Together with the fact that \(\frac{f}{1+\lambda}\ge\frac{\lambda f}{10}\), the premises of Corollary C.2 are met. As a result the output _H_ via Step 6 must satisfy:

\(\nu(H)\ge\frac{f}{1+\lambda}-\frac{\lambda f}{10}=\nu(G)-\left[\nu(G)-\left(\frac{1}{1+\lambda}-\frac{\lambda}{10}\right)\cdot f\right]\)<br>
\(\ge\nu(G)-\left(\frac{1}{1-\lambda}-\frac{1}{1+\lambda}+\frac{\lambda}{10}\right)\cdot f(\nu(G)\le\frac{f}{1-\lambda})\)<br>
\(\ge\nu(G)-10\lambda f(\lambda\le\frac{1}{10})\)<br>
\(\ge\nu(G)-\frac{\Delta}{2}\cdot\frac{f}{\hat{f}}(\lambda=\frac{\Delta}{20\hat{f}})\)<br>
\(\ge\nu(G)-\Delta\)

where the last inequality follows the facts that \(f\le(1+\lambda)\nu(G)\le 1.1\nu(G)\) and \(0.99\nu(G)\le\hat{f}\). Hence, our protocol does compute _H_ with a guarantee that \(\nu(H)\ge\nu(G)-\Delta\).

Finally, the protocol communicates \(\widetilde{O}(n)\) bits in Step 1, \(\widetilde{O}\left(\frac{n}{\lambda^2}\right)\) bits in Step 4, and \(\widetilde{O}\left(\frac{n\sqrt{f}}{\sqrt{\lambda}}\right)\) bits in Step 6. Using the fact that \(f\le(1+\lambda)\nu(G)\le 1.1\nu(G)\) and \(\lambda=\frac{\Delta}{20\hat{f}}\ge\frac{\Delta}{20(1.01)\cdot\nu(G)}\), the total communication is bounded by

\(\widetilde{O}\left(\frac{n\cdot\nu(G)}{\sqrt{\Delta}}+\frac{n\cdot\nu(G)^2}{\Delta^2}\right)\)

bits, as desired.

## Setting up the proof of Claim C.1.

Our task only remains to Claim C.1. We assume its setting: let \(f,k,k'\) be such that \(k'<k\le f\) with a promise that \(\nu(G)\ge f\), and also given for free is \(H\unknown G\) with \(\nu(H)\ge f-k\). We wish to obtain \(H^\text{after}\unknown G\) with \(\nu(H^\text{after})\ge f-k'\). Our protocol proceeds in a similar fashion as sketched in Section 3 barring changes in the notions of witness: we shall now consider a witness with respect to the residual graph instead of actual graph _H_.

Specifically, let _F_ be a flow subgraph of _H_ with size \(\nu(F)=f-k\) that is fixed throughout the protocol. For any graph G containing _F_ as a subgraph, we define a set of _residual witness_ of G with respect to _F_, denoted W_<sub>F</sub>_(G), with an invariant that \(\nu(\mathcal{G})\ge f-k'\) if and only if \(\mathcal{W}_F(\mathcal{G})=\emptyset\). The protocol starts with \(H_1\leftarrow H\). In each round _i_=1,2_,..._, the players compute a private edge \(e_i\in G\backslash H_i\) that reduces the number of witnesses by a fraction of \(\gamma\); that is, _e<sub>i</sub>_ be such that \(|\mathcal{W}_F(H_i\cup e_i)|\le(1-\gamma)\cdot|\mathcal{W}_F(H_i)|\), exchange such edge, and then set \(H_{i+1}\leftarrow H_i\cup e_i\). The protocol terminates at the first round _T_ where \(\mathcal{W}_F(H_T)=\emptyset\), ensuring that the final graph _H_after:=_H<sub>T</sub>_ has \(\nu(H^\text{after})\ge f-k'\) via our invariant. Since the protocol communicates _T_ edges in total, our goal is to ensure that a small \(T=\widetilde{O}\left(nf\cdot\frac{\sqrt{k}}{k'}\right)\) suffices for termination.

## Organization.

In Section C.1, we apply an inexpensive pre-processing step to _H_, ensuring that all of its vertices is actually reachable from the terminal _s_. In Section C.2, we formally define _residual witnesses_ and prove their corresponding useful properties. Section C.3 establishes an upper bound on the starting number of residual witnesses of _H_. Finally, Section C.4 integrates these results, yielding a protocol that satisfies Claim C.1.

