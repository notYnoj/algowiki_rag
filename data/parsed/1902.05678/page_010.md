<tbc>having the following properties: _I_ and _J_ differ in only _m<sub>i</sub>_’s preference list, and _m<sub>i</sub>_ prefers _M<sub>J</sub>_ to _M<sub>I</sub>_, where _M<sub>I</sub>_ and _M<sub>J</sub>_ are the outputs of Algorithm 1 for _I_ and _J_, respectively. Then either (i) \(M_J(m_i)\succ_{m_i}M_I(m_i)\) in _I_, or (ii) _m<sub>i</sub>_ is single in _M<sub>I</sub>_ and _M<sub>J</sub>(m<sub>i</sub>_) is acceptable to _m<sub>i</sub>_ in _I_.

Let \(I'\) and \(J'\) be the SMI-instances constructed by Algorithm 2. Since _I_ and _J_ differ in only _m<sub>i</sub>_’s preference list, \(I'\) and \(J'\) differ in only _a<sub>i</sub>_’s preference list. Let \(M_{I^\prime}\) and \(M_{J^\prime}\), respectively, be the outputs of MGS applied to \(I'\) and \(J'\). In case of (i), we have that \(M_{J^\prime}(a_i)\succ_{a_i}M_{I^\prime}(a_i)\) in \(I'\), due to Algorithm 2 and Step 3 of Algorithm 1. In case of (ii), _a<sub>i</sub>_ is single in \(M_{I^\prime}\) because _m<sub>i</sub>_ is single in _M<sub>I</sub>_, and \(M_{J^\prime}(a_i)\) is acceptable to _a<sub>i</sub>_ in \(I'\) because _M<sub>J</sub>(m<sub>i</sub>_) is acceptable to _m<sub>i</sub>_ in _I_. This implies that _a<sub>i</sub>_ has a successful strategy in \(I'\), contradicting to the man-strategy-proofness of MGS for SMI \[4\].

By Lemmas 3.3, 3.4, and 3.5, we can conclude that Algorithm 1 is a man-strategy-proof 1.5-approximate-stable mechanism for MAX SMTI-1TM.

## References

