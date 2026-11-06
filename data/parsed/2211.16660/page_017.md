_Proof._ Let \(I_1\times J_1<I_2\times J_2<\cdots<I_{m_x^\prime}\times J_{m_x^\prime}\) be the ordered sequence of rectangles given by Lemma 5.10. By construction, for all \(i=1,\dots,m'_x\), we have (i) \(I_i\in\mathcal{I}_w\), (ii) every \(\gamma w\)-subinterval of _I<sub>i</sub>_ is \(\gamma\)-balanced, (iii) \(|J_i|\ge(1+0.9\beta)w\), and (iv) IsQType_<sub>w</sub>(y<sub>J<sub>i</sub></sub>_,GetPType_<sub>w</sub>(x<sub>I<sub>i</sub></sub>_))=true.

It follows that at loop iteration _i_=(end_I<sub>i</sub>)/w_ and \(j=(\text{end}J_i)/(\theta w)\) of Line 20, the interval _J_ exists (the interval _J=J<sub>i</sub>_ satisfies the requirement, so a minimal _J_ exists). Thus, CoveringAlgorithm certifies a rectangle \((I'_i\times J'_i,\frac{|I'_i|}{2}+\alpha w)\) where \(I'_i\), the output of Getl_<sub>w</sub>_, is a \(\gamma w\)-aligned subinterval of _I<sub>i</sub>_ and \(J'_i\) is a subinterval of _J<sub>i</sub>_ with length at least \((1+0.9\beta)w\).

We would like to build an ordered collection of certified rectangles containing these \((I'_i\times J'_i,\frac{|I'_i|}{2}+\alpha w)\), which embed more than half of each small interval \(I'_i\) into _y_. However, for each of these rectangles, \(J'_i\) is typically much longer than \(I'_i\), so using many of them is extremely wasteful of bits in _y_. To reduce this issue, we let \(t:=3/\beta\) and build an ordered collection using only every _t_-th rectangle from the preceding family.

Let \(m''_x\) be the largest multiple of _t_ less than \(m'_x\). For each _i_ that is a multiple of _t_, partition _I<sub>i</sub>_ into \(\tilde{I}_i^L<\tilde{I}_i^M<\tilde{I}_i^R\) where \(\tilde{I}_i^M:=I'_i\). For _i_ not a multiple of _t_, let \(\tilde{I}_i:=I_i\). For _i_ a multiple of _t_, let \(\tilde{J}_i^M:=J'_i\).

For _i_ a multiple of _t_, we claim there exist \(\theta w\)-aligned intervals \(\tilde{J}_{i-t}^R<\tilde{J}_{i-t+1}<\tilde{J}_{i-t+2}<\cdots<\tilde{J}_{i-1}<\tilde{J}_i^L\) such that

• \(\tilde{J}_i^L<\tilde{J}_i^M\).<tbc>

• \(|\tilde{J}_i^L|=|\tilde{I}_i^L|\).<tbc>

• \(|\tilde{J}_{i-\ell}|=|\tilde{I}_{i-\ell}|\) for \(\ell=1,\dots,t-1\).<tbc>

• \(|\tilde{J}_{i-t}^R|=|\tilde{I}_{i-t}^R|\) (we take \(\tilde{I}_0^R=\emptyset\)).<tbc>

• \(\tilde{J}_{i-t}^M<\tilde{J}_{i-t}^R\) (this is vacuously true if _i=t_)

<tbc>To see that such intervals exist, notice that interval \([\text{end}\tilde{J}_{i-t}^M,\text{start}\tilde{J}_i^M]=[\text{end}J'_{i-t},\text{start}J'_i]\) contains all intervals \(J'_{i-\ell}\) for \(\ell=1,\dots,t-1\). Since each \(J'_{i-\ell}\) has length at least \((1+0.9\beta)w\), we have

\(\text{start}J_i^M-\text{end}J_{i-t}^M\ge(t-1)(1+0.9\beta)w>(t+1)w\ge|\tilde{I}_i^L|+\sum_{\ell=1}^{t-1}|\tilde{I}_{i-\ell}|+|\tilde{I}_{i-t}^R|.\)

The last inequality holds as each term on the right is at most _w_. Thus we can construct the intervals greedily in order \(\tilde{J}_i^L,\tilde{J}_{i-1},\tilde{J}_{i-2},\dots,\tilde{J}_{i-t+1},\tilde{J}_{i-t}^R\) by setting end \(\tilde{J}_i^L=\text{start}\tilde{J}_i^M\), and then end \(\tilde{J}_{i-1}=\text{start}\tilde{J}_i^L\), and so on. They will be \(\theta w\)-aligned as all of the \(\tilde{I}\) intervals have lengths a multiple of \(\gamma w\), and thus a multiple of \(\theta w\).

By construction of these intervals, CoveringAlgorithm certifies the following rectangles for \(i\le m''_x\):

\((\tilde{I}_i^M\times\tilde{J}_i^M,\kappa_i^M)\text{where}\kappa_i^M:=\frac{|\tilde{I}_i^M|}{2}+\alpha w\text{if}t|i\)<br>
\((\tilde{I}_i^L\times\tilde{J}_i^L,\kappa_i^L)\text{where}\kappa_i^L:=\text{Trivial}(\tilde{I}_i^L,\tilde{J}_i^L)\text{if}t|i\)<br>
\((\tilde{I}_i^R\times\tilde{J}_i^R,\kappa_i^R)\text{where}\kappa_i^R:=\text{Trivial}(\tilde{I}_i^R,\tilde{J}_i^R)\text{if}t|i\)<br>
\((\tilde{I}_i\times\tilde{J}_i,\kappa_i)\text{where}\kappa_i:=\text{Trivial}(\tilde{I}_i,\tilde{J}_i)\text{if}t\nmid i\) (4)

The first collection of rectangles comes from the definition of \(\tilde{I}_i^M:=I'_i\) and \(\tilde{J}_i^M:=J'_i\). The rest of the rectangles come from the fact that we certify all \(\gamma w\)-aligned squares with the trivial algorithm in CoveringAlgorithm Line 11. Furthermore, the rectangles are increasing in _i_, with additionally \(\tilde{I}_i^L\times\tilde{J}_i^L<\tilde{I}_i^M\times\tilde{J}_i^M<\tilde{I}_i^R\times\tilde{J}_i^R\) for _i_ a multiple of _t_. Hence, the rectangles in (4) form an ordered collection of rectangles. By Lemma 2.1, we also have \(\kappa_i^L\ge(\frac{1}{2}-\gamma)|\tilde{I}_i^L|,\kappa_i^R\ge(\frac{1}{2}-\gamma)|\tilde{I}_i^R|\) for _i_ a multiple of _t_ and \(\kappa_i\ge(\frac{1}{2}-\gamma)|\tilde{I}_i|\) for all other _i_,<tbc>

