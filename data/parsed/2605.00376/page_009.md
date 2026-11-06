**Theorem 4.1.** _Let_ C _be an MDS array code over_ \(\mathbb{F}_2^b\) _with parameters_ \([m+k,k,m+1]\)_, where_ \(m\ge 4\) _and k,b are positive integers, and let H be its parity-check matrix given in (3.2). Then Algorithm 2 corrects up to two symbol errors with unknown locations._

**Proof.** Since _n=m+k_, symbol errors in the received vector **v**=\[**v**<sub>1</sub>_,...,_**v**_<sub>n</sub>_\] may affect either the _k_ information symbols or the _m_ parity symbols. All such cases are considered below.

• **_Case 1: One or two errors in parity symbols_**. If one or two errors occur in parity symbols, then _m_-1 or _m_-2 syndromes are zero, respectively. If the errors occur at positions _k+j_<sub>1</sub> and _k+j_<sub>2</sub>, then the nonzero syndromes are **s**<sub>_j_<sub>1</sub></sub> and **s**<sub>_j_<sub>2</sub></sub>, respectively.<tbc>

<tbc>So, the magnitudes of the errors are given by<tbc>

\(\mathbf{e}_{k+j_1}=\mathbf{s}_{j_1}\text{and}\mathbf{e}_{k+j_2}=\mathbf{s}_{j_2}.\) \(\text{(4.11)}\)

• **_Case 2: One error in an information symbol._** Suppose that a single error occurred in an information symbol at position _l_<sub>1</sub>. Then, by (4.2), the syndromes are given by<tbc>

\(\mathbf{s}_i^T=A_{il_1}\mathbf{e}_{l_1}^T,\) \(\text{(4.12)}\)

for all _i_=1_,...,m_. Replacing in (4.3), we have \(y_i^T=0\), for all _i_=1_,...,m_, because<tbc>

\(\mathbf{e}_{l_1}^T=A_{1l_1}^{-1}\mathbf{s}_1^T=A_{2l_1}^{-1}=\dots=A_{ml_1}^{-1}\mathbf{s}_m^T,\) \(\text{(4.13)}\)

and the magnitude of the error is obtained using any equality from Equation (4.13).<tbc>

• **_Case 3: One error in an information symbol and one error in a parity symbol._** Assume that the error in the information symbol occurred at position _l_<sub>1</sub> and, without loss of generality, that the error in the parity symbol occurred at position _k_+1. Then, by (4.2), the syndromes are given by<tbc>

\(\mathbf{s}_1^T=A_{1l_1}\mathbf{e}_{l_1}^T+\mathbf{e}_{k+1}\text{and}\mathbf{s}_i^T=A_{il_1}\mathbf{e}_{l_1}^T,\) \(\text{(4.14)}\)

for all _i_=2_,...,m_. In this case, we will have \(\mathbf{y}_1,\mathbf{y}_2\neq\mathbf{0}\), since **s**<sub>1</sub> is involved in the computation of these vectors, and **y**<sub>3</sub>=_..._=**y**_<sub>m</sub>_=0. The magnitude of the error in the information symbol is obtained from any syndrome equation with _i_=2_,...,m_, namely,<tbc>

\(\mathbf{e}_{l_1}^T=A_{il_1}^{-1}\mathbf{s}_i^T.\) \(\text{(4.15)}\)

Substituting this value into the first syndrome equation, the magnitude of the error in the parity symbol is given by<tbc>

\(\mathbf{e}_{k+1}=\mathbf{s}_1^T-A_{1l_1}\mathbf{e}_{l_1}^T.\) \(\text{(4.16)}\)

• **_Case 4: Two errors in information symbols_**. Suppose now that the two errors in the information symbols are at positions _l_<sub>1</sub> and _l_<sub>2</sub>. By (4.2), the syndromes are calculated by<tbc>

\(\mathbf{s}_i^T=A_{il_1}\mathbf{e}_{l_1}^T+A_{il_2}\mathbf{e}_{l_2}^T,\) \(\text{(4.17)}\)

for _i_=1_,...,m_. Without loss of generality, suppose _l_<sub>1</sub>=1. Replacing (4.17) into the vectors **y**_<sub>i</sub>_ given by (4.3), then \(\mathbf{y}_i^T\neq 0\), for all _i_=1_,...,m_. Fixing **y**<sub>2</sub> we have<tbc>

\(\mathbf{y}_2^T=\mathbf{s}_2^T+A_{2l_1}A_{1l_1}^{-1}\mathbf{s}_1^T=(A_{2l_1}\mathbf{e}_{l_1}^T+A_{2l_2}\mathbf{e}_{l_2}^T)+A_{2l_1}A_{1l_1}^{-1}(A_{1l_1}\mathbf{e}_{l_1}^T+A_{1l_2}\mathbf{e}_{l_2}^T)=A_{2l_1}\mathbf{e}_{l_1}^T+A_{2l_2}\mathbf{e}_{l_2}^T+A_{2l_1}A_{1l_1}^{-1}A_{1l_1}\mathbf{e}_{l_1}^T+A_{2l_1}A_{1l_1}^{-1}A_{1l_2}\mathbf{e}_{l_2}^T=A_{2l_2}\mathbf{e}_{l_2}^T+A_{2l_1}A_{1l_1}^{-1}A_{1l_2}\mathbf{e}_{l_2}^T=(A_{2l_2}+A_{2l_1}A_{1l_1}^{-1}A_{1l_2})\mathbf{e}_{l_2}^T.\text{(4.18)}\)

Since \(A_{ij}=C^{\sigma(i,j)}\), then<tbc>

\(\mathbf{y}_2^T=(C^{\sigma(2,l_2)}+C^{\sigma(2,l_1)-\sigma(1,l_1)+\sigma(1,l_2)})\mathbf{e}_{l_2}^T.\) \(\text{(4.19)}\)

