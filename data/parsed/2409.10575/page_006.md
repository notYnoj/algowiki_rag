matching _M_ is a weakly stable _b_-matching if and only if it has no BPs. In this paper, since we are focusing exclusively on weakly stable matchings, we will refer to them simply as stable matchings.

The bipartite stable _b_-matching problem provides a robust framework for understanding and addressing the SMTI and HRT problems. Specifically, an SMTI problem corresponds to a bipartite stable _b_-matching problem where _U_ represents men, _W_ represents women, and \(b:V\rightarrow\{1\}\). An HRT problem corresponds to a bipartite stable _b_-matching problem where _U_ represents residents and _W_ represents hospitals. In this context, the function _b_ is defined such that _b(u_)=1 for all \(u\in U\) and _b(w_)=_C(w_) for all \(w\in W\), where _C(w_) is the quota of hospital _w_. We assume, without loss of generality, that \(\sum_{u\in U}b(u)=\sum_{w\in W}b(w)\) for both problems.

### 3.2 Sex equality cost

Sex equality cost is a popular measure for achieving equity in the SM problem. This metric quantifies the gap between the preferences obtained by the two sides, defined as:

\(d_{SM}(M)=\left|\sum_{(u,w)\in M}r_u(w)-\sum_{(u,w)\in M}r_w(u)\right|\)

where _u_ and _w_ represent a man and a woman, respectively.

In the SMTI problem, there may be several single men and women. We denote the set \(M_{paired}=\{(u,w)\in M|u\neq\varnothing,w\neq\varnothing\}\) as the set of matching pairs consisting of matched men and women. When calculating the sex equality cost for the SMTI problem, we focus on the matched pairs, disregarding the single individuals:

\(d_{SMTI}(M)=\left|\sum_{(u,w)\in M_{paired}}r_u(w)-\sum_{(u,w)\in M_{paired}}r_w(u)\right|\)

1 shows an SMTI instance with four men and four women and their respective preference lists. In the preference lists, for example, _m_<sub>1</sub>:(_w_<sub>1</sub>_w_<sub>3</sub>)_w_<sub>2</sub> means that man _m_<sub>1</sub> equally prefers women _w_<sub>1</sub> and _w_<sub>3</sub>, and strictly prefers both over woman _w_<sub>2</sub>. Consider a stable matching \(M=\{(m_1,w_1),(m_2,w_2),(m_3,\varnothing),(m_4,\varnothing),(w_3,\varnothing),(w_4,\varnothing)\}\). The corresponding _M<sub>paired</sub>_ is {(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>2</sub>)}. Then, the sex equality cost is calculated as follows:

\(d_{SMTI}(M)=\left|\left(r_{m_1}(w_1)+r_{m_2}(w_2)\right)-\left(r_{w_1}(m_1)+r_{w_2}(m_2)\right)\right|=\left|(1+2)-(1+1)\right|=1\)

A stable matching _M_ is considered to favor the _U_ side if \(\sum_{(u,w)\in M_{paired}}r_u(w)<\sum_{(u,w)\in M_{paired}}r_w(u)\). Conversely, _M_ is considered to favor the _W_ side if \(\sum_{(u,w)\in M_{paired}}r_u(w)>\sum_{(u,w)\in M_{paired}}r_w(u)\).

## 4 A local search algorithm for SMTI and HRT

In this section, we introduce a tie-breaking based local search algorithm, named TBLS, designed to address the MAX-SMTI and MAX-HRT problems, and its equity-focused<tbc>

