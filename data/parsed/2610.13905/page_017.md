_2. There exists_ \(y\in\mathbb{C}(\varepsilon)^m\) _such that_ \(y^TA=b^T\) _and_ \(y\notin\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\).<tbc>

<tbc>_Then there exists a Laurent-polynomial solution_ \(y'\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^m\) _such that_ \((y')^TA=b^T\), \(y'\notin\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\)_, and every nonzero entry of_ \(y'\) _has exponent support contained in_<tbc>

\(I=[\mathrm{min}\left\{0,B_--\alpha-k\right\},\mathrm{max}\left\{B_+-\alpha-k+H+(\rho-1)(\beta-\alpha),\rho(\beta-\alpha)\right\}].\)

<tbc>_Proof._ We start by noting \(\mathrm{rank}_{\mathbb{C}(\varepsilon)}(A_0)=\rho\) and \(A=\varepsilon^\alpha A_0\). Hence, if _y<sup>T</sup>A=b<sup>T</sup>_ then _z<sup>T</sup>A_<sub>0</sub>=_b<sup>T</sup>_ for \(z=\varepsilon^\alpha y\in\mathbb{C}(\varepsilon)^m\). With this in mind, let _I<sub>i</sub>_ and _J<sub>i</sub>_ collect, respectively, the row and column indices corresponding to the minor _N<sub>i</sub>_ of _A_<sub>0</sub>. If adj(_N<sub>i</sub>_) is the adjugate of _N<sub>i</sub>_, then we have \(\mathrm{adj}(N_i)N_i=\Delta_i(\varepsilon)I_\rho\) and therefore<tbc>

\(b_i^T\mathrm{adj}(N_i)N_i=\Delta_i(\varepsilon)b_i^T,\) (3.6)

<tbc>where \(b_i=b\big|_{J_i}\in\mathbb{C}(\varepsilon)^\rho\) is the vector obtained by restricting _b_ to the indices in _J<sub>i</sub>_. Define now \(u_i^T=b_i^T\mathrm{adj}(N_i)\) and let \(\tilde{u}_i\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^m\) such that<tbc>

\(\tilde{u}_i\big|_{I_i}=u_i\text{and}\tilde{u}_i\big|_{I_i^C}=0.\) (3.7)

<tbc>In this case<tbc>

\(\tilde{u}_i^TA_0\big|_{J_i}=u_i^TN_i=\Delta_i(\varepsilon)b_i^T=\left(\Delta_i(\varepsilon)b\big|_{J_i}\right)^T.\) (3.8)

<tbc>Now since _N<sub>i</sub>_ is a full rank minor of _A_<sub>0</sub> and \(\mathrm{rank}_{\mathbb{C}(\varepsilon)}(A_0)=\rho\), we can express each column of _A_<sub>0</sub> as a linear combination of the columns with indices in _J<sub>i</sub>_. Letting \(A_0(:,r)=\sum_{u\in J_i}\lambda_u(\varepsilon)A_0(:,u)\) for some \(\lambda_u(\varepsilon)\in\mathbb{C}(\varepsilon)\) and recalling _z<sup>T</sup>A_<sub>0</sub>=_b<sup>T</sup>_, we have

\(\tilde{u}_i^TA_0(:,r)=\tilde{u}_i^T\left(\sum_{u\in J_i}\lambda_u(\varepsilon)A_0(:,u)\right)=\sum_{u\in J_i}\lambda_u(\varepsilon)(\tilde{u}_i^TA_0(:,u))=\sum_{u\in J_i}\lambda_u(\varepsilon)\Delta_i(\varepsilon)b_u=\Delta_i(\varepsilon)\sum_{u\in J_i}\lambda_u(\varepsilon)(z^TA_0(:,u))=\Delta_i(\varepsilon)z^T\left(\sum_{u\in J_i}\lambda_u(\varepsilon)A_0(:,u)\right)=\Delta_i(\varepsilon)z^TA_0(:,r)=\Delta_i(\varepsilon)b_r,\text{(3.9)}\)

where _b<sub>r</sub>_ is the _r_-th entry of _b_. Hence, \(\tilde{u}_i^TA_0=\Delta_i(\varepsilon)b^T\). Suppose now<tbc>

\(y'=\frac{1}{c\varepsilon^{k+\alpha}}\sum_ih_i(\varepsilon)\tilde{u}_i,\) (3.10)

<tbc>which we note has Laurent-polynomial entries by construction. Combining (3.9) with \(\sum_ih_i(\varepsilon)\Delta_i(\varepsilon)=c\varepsilon^k\) and \(A=\varepsilon^\alpha A_0\), it is easy to see that \((y')^TA=b^T\), as desired. Moreover, since the degree of any entry in adj(_N<sub>i</sub>_) is at most \((\beta-\alpha)(\rho-1)\), the exponent support for entries of \(y'\) is a subset of<tbc>

\(I=[B_--\alpha-k,B_+-\alpha-k+H+(\beta-\alpha)(\rho-1)].\) (3.11)

<tbc>It remains to show that \(y'\) does not belong to the span of _S_ in \(\mathbb{C}(\varepsilon)^m\). To do this, let \(v_1,\dots v_{m-\rho}\in\mathbb{C}[\varepsilon,\varepsilon^{-1}]^m\) be a basis for the _left_ null space of _A_. By construction, \(y'-y\) belongs to this space and hence can be written as a linear combination of \(v_1,\dots,v_{m-\rho}\). Suppose now that \(y'\in\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\). Since \(y\notin\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\) we must have \(y'-y\notin\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\) and therefore \(v_j\notin\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\) for at least one _j_. But in this case, we can simply replace \(y'\) by \(y'+v_j\), which satisfies<tbc>

\((y'+v_j)^TA=(y')^TA+v_j^TA=b^T+0=b^T\) (3.12)

<tbc>and does not belong to \(\mathrm{span}_{\mathbb{C}(\varepsilon)}(S)\). To verify that this will not destroy the structure of \(y'\), we next show that \(v_1,\dots,v_{m-\rho}\) can be constructed to have Laurent polynomial entries. We start by noting that _A_ and _A_<sub>0</sub> have the same left null spaces over \(\mathbb{C}(\varepsilon)\), so it suffices to construct a basis for _A_<sub>0</sub>. Let _I<sub>i</sub>_ and _J<sub>i</sub>_ again correspond to the row/column indices of the minor _N<sub>i</sub>_ of _A_<sub>0</sub>. Since the columns of _N<sub>i</sub>_ are linearly independent, we have<tbc>

\(q^TA_0=0\Longleftrightarrow q^TA_0(:,J_i)=0\) (3.13)

