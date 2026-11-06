### AI statement

Various AI models were used throughout this project, but all work done by AI was supervised and carefully checked by the authors, who take responsibility for the correctness of all claims.

## Disclaimer

This paper was prepared for informational purposes by the Global Technology Applied Research center of JPMorgan Chase & Co. This paper is not a product of the Research Department of JPMorgan Chase & Co. or its affiliates. Neither JPMorgan Chase & Co. nor any of its affiliates makes any explicit or implied representation or warranty and none of them accept any liability in connection with this paper, including, without limitation, with respect to the completeness, accuracy, or reliability of the information contained herein and the potential legal, compliance, tax, or accounting effects thereof. This document is not intended as investment research or investment advice, or as a recommendation, offer, or solicitation for the purchase or sale of any security, financial instrument, financial product or service, or to be used in any way for evaluating the merits of participating in any transaction.

## Appendix A Proofs of the Maximum-Likelihood bounds

We prove Theorems 4 and 5 for the Linial-Simkin ensemble. Fix \(D\ge 3\), _q_, \(c\in(0,1)\), and the channel during the _n_-limit. Write _g=g(n_).

Let E_<sub>n</sub>_ be the event of successful completion of all _D_-2 matching rounds in Definition 4. Thus Pr(E_<sub>n</sub>_)=1-_o_(1) by \[LS20\]. We may randomize the initial Hamilton cycle _H_ and its direction: this randomizes labels without changing graph-invariant decoding probabilities. Unless explicitly conditioned, probabilities refer to the unconditioned process. A failed run contributes zero to a count requiring a completed graph; conditioning on E_<sub>n</sub>_ is imposed at the end. The published graph- construction and process estimates are cited below; the matching, planting, and coding arguments are additional arguments of this manuscript.

### A.1 Dense matching rounds and prescribed subgraphs

For a given Hamilton cycle _H_ on _V_=\[_n_\], fixed target degree \(D\in\unknown\), a target girth \(g:\unknown\rightarrow\unknown\) with \(g(n)\le n\) and even \(n\in\unknown\), \[LS20\] define their (_H,g,D)-high-girth process_ as a graph sequence (_G_<sub>0</sub>_,G_<sub>1</sub>_,..._) that begins with _G_<sub>0</sub>=_H_ and where _G_<sub>_t_+1</sub> is constructed from _G<sub>t</sub>_ as follows: If _G<sub>t</sub>_=(_V,E<sub>t</sub>_) is _D_-regular, then _G_<sub>_t_+1</sub>=_G<sub>t</sub>_. Otherwise, let _H<sub>t</sub>_=(_W<sub>t</sub>,_A_<sub>t</sub>_) where

\(W_t:=\{u\in V|d_{G_t}(u)=min_{v\in V}d_{G_t}(v)\}\) (97)

is the set of _unsaturated_ vertices and

\(\mathscr{A}_t:=\{\{u,v\}\subset W_t|\delta_{G_t}(u,v)\ge g(n)-1\}\) (98)

is the set of _available_ edges. If \(\mathscr{A}_t=\emptyset\), then _G_<sub>_t_+1</sub>=_G<sub>t</sub>_. Otherwise, \(E_{t+1}=E_t\cup\{e_{t+1}\}\) where _e_<sub>_t_+1</sub> is chosen uniformly at random from A_<sub>t</sub>_. The process _freezes_ at time _t_ if _G<sub>t</sub>=G_<sub>_t_+1</sub> and _saturates_ at time _t_ if _G<sub>t</sub>_ is _D_-regular. As shown in \[LS20, Theorem 1.1\], if \(D\ge 3\) and _g(n_)=_c_log<sub>_D_-1</sub>(_n_) for a fixed \(c\in(0,1)\), then the (_H,g,D_)-high-girth process saturates _w.h.p_. (with high probability,<tbc>

