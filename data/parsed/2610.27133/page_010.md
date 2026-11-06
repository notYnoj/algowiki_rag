<tbc>once, and, if _r\>_0, each color from _R_ is used exactly once on _Z_. This gives a panchromatic coloring of _H_ with \(\chi_P\) colors. In any panchromatic \(\chi_P\)-coloring of _H_, precisely the vertices in _S_ have unique colors, so \(\alpha\) is attained.

Now, we consider a bipanchromatic _k_-coloring of _H_. Assume that precisely \(s\le\alpha\) colors occur on _S_. Each of the other _k-s_ colors occurs in every _P<sub>i</sub>_, so at least _q_ times. Those also absent from _P_<sub>1</sub>\\_R_ must occur on _Z_, so they occur at least _q_+1 times. At most _m-r_ of the _k-s_ colors occur on _P_<sub>1</sub>\\_R_. Therefore<tbc>

\(|V|\ge 2s+q(k-s),|V|\ge 2s+(q+1)(k-s)-(m-r).\)

<tbc>Substituting \(s\le\alpha\), \(|V|=\alpha+qm+r\), and \(\chi_P=\alpha+m\) gives<tbc>

\(q(\chi_P-k)\ge\alpha-r,(q+1)(\chi_P-k)\ge\alpha.\)

<tbc>By the definition of _D_, it follows that

\(\chi_P-k\ge max\left\{\left\lceil\frac{\alpha}{q+1}\right\rceil,\left\lceil\frac{\alpha-r}{q}\right\rceil\right\}=D.\)

Thus every bipanchromatic coloring has at most \(\chi_P-D=L\) colors. Since also \(L\le\chi_B\) by Proposition 10, we obtain \(\chi_B=L\).

Therefore, at every feasible triple in this range, any universally valid lower bound using only \((|V|,\chi_P,\alpha)\) is at most _L_. Since _L_ is itself valid, it is the strongest such lower bound.

**Corollary 13** (Optimal ratio guarantees)**.** _For L, the factor_ 5/4 _in_ (8) _is attained. The constant_ 6/5 _in_ (9) _is asymptotically sharp as_ \(L\rightarrow\infty\)_. These are optimal constants from_ \(|V|,\chi_P,\alpha\).

_Proof._ For any \(n\in\mathbb{N}\), Proposition 7 describes a hypergraph whose parameters \((|V|,\chi_P,\alpha,\chi_B)\) are (12_n_-2,6_n,_3_n_+1,6_n_-1). Here we obtain _q_=3, _r_=0, _D=n_+1, and _L_=5_n_-1, so

\(\frac{\chi_B}{L}=\frac{6n-1}{5n-1}=\frac{6}{5}+\frac{1}{5(5n-1)}.\)

This is 5/4 at _n_=1 and tends to 6/5 as \(n\rightarrow\infty\). Proposition 12 confirms optimality.

## AI Assistance

ChatGPT was used to assist with proof development. All AI-assisted arguments were reviewed and revised by the authors, who take full responsibility for the final manuscript.

## References

