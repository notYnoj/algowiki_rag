We now construct a mapping \(\hat{\mu}:\mathcal{A}\rightarrow\mathcal{B}\cup\{\perp\}\) that will have low cost. \(\hat{\mu}\) may not be monotone. Finally, we will convert \(\hat{\mu}\) into a monotone mapping \(\mu\) by negligibly increasing the cost, thus overall getting a good mapping. For each \(a\in\mathcal{A}\), if \(a\cap A'=\varnothing\), then set \(\hat{\mu}(a)=\perp\). For each window \(a\in\mathcal{A}\) which nontrivially intersects \(A'\), let _i<sub>a</sub>_ be the first index of \(\mu'(a\cap A')\). Similarly, let _j<sub>a</sub>_ be the last index of \(\mu'(a\cap A')\). Note that _i_<sub>_a._next</sub>_\>j.a_ for all _a_ with \(\hat{\mu}(a)\neq\perp\) .

Let _k<sub>a</sub>_ denote the number of indices of _a_ that are deleted and \(\ell_a\) denote the number of indices of _a_ that are substituted. Let _m<sub>a</sub>_ denote the number of indices in _B_ between _i<sub>a</sub>_ and _j<sub>a</sub>_ that are not mapped from any indices of _A_ in \(a\cap A'\) by \(\hat{\mu}\). Then, it must hold that if \((j_a-i_a+1)\ge d\) then \(m_a\ge[(j_a-i_a+1)-d]+k_a\). If (_j<sub>a</sub>-i<sub>a</sub>_+1)_\<d_ then \(k_a\ge[d-(j_a-i_a+1)]+m_a\).

When \((j_a-i_a+1)\ge d\), if \(\frac{(1+\epsilon)^{j-1}}{d}\le[(j_a-i_a+1)-d]<\frac{(1+\epsilon)^j}{d}\) (note that such a _j_ always exists). Set \(\hat{\mu}(a)\) to be the right-most interval in \(\mathcal{H}^\tau\), \(\tau=\frac{(1+\epsilon)^{j-1}}{d}\) , that contains \(\mu'(A[i])\). In that case, the length of the interval \(\hat{\mu}(a)\) is \(d+(1+\epsilon)^{j-1}\).

On the other hand, if (_j<sub>a</sub>-i<sub>a</sub>_+1)_\<d_ and \(\frac{(1+\epsilon)^{j-1}}{d}\le[d-(j_a-i_a+1)]<\frac{(1+\epsilon)^j}{d}\) (note that such a _j_ always exists). Set \(\hat{\mu}(a)\) to be the right-most interval in \(\mathsf{L}^\tau\) that contains \(\mu'(A[i])\). In that case, the length of the interval \(\hat{\mu}(a)\) is \(d-(1+\epsilon)^{j-1}\).

Note that \((i_a-s(\hat{\mu}(a)))\le\epsilon\tau d\). We get

\(\mathrm{ED}(a,\hat{\mu}(a))\le\underbrace{m_a+k_a+l_a}_\text{True edits}+\underbrace{\epsilon(1+\epsilon)^{j-1}}_\text{Due to error in length estimation}+\underbrace{2(s(\mu(a))-i_a)}_\text{Shift due to the choice of grid points}\)<br>
\(\le(1+3\epsilon)\tau d.\)

Now note that, for all \(a\in\mathcal{A}\), _j<sub>a</sub>\<i_<sub>_a._next</sub>. Let \(r_a=(i_a-s(\mu(a)))\). Thus, we have \(|e(\hat{\mu}(a))-s(\hat{\mu}(a.\text{next}))|\le|r_a-r_{a.\text{next}}|+M(j_a,i_{a.\text{next}})\) where _M(j<sub>a</sub>,i_<sub>_a._next</sub>) are the number of symbols of _B_ in between _j<sub>a</sub>_ and _i_<sub>_a._next</sub>. Note that, in ED(_A,B_), all these symbols, _M(j<sub>a</sub>,i_<sub>_a._next</sub>), are deleted from _B_ or equivalently inserted in _A_. If \(r_a\ge r_{a.\text{next}}\) then we charge |_r<sub>a</sub>-r_<sub>_a._next</sub>| to _a_. Else, we charge it to _a._next. Note that when |_r<sub>a</sub>-r_<sub>_a._next</sub>| is charged to _a_ then \(|r_a-r_{a.\text{next}}|\le r_a\le\epsilon(m_a+k_a+l_a)\).

Hence we obtain

\(\mathrm{ED}(\hat{\mu})=\sum_{a\in\mathcal{A}}\mathrm{ED}(a,\hat{\mu}(a))+\sum_{i=1}^n\big|\#\{a\text{s.t.}i\in\hat{\mu}(a)\}-1\big|\)<br>
\(\le(1+3\epsilon)\mathrm{ED}(A,B)+\sum_{a,\hat{\mu}(a)\neq\perp} 4r_a\)<br>
\(\le(1+7\epsilon)\mathrm{ED}(A,B)\)

It is possible that \(\hat{\mu}\) may not be monotone. In particular, this can happen if _r_<sub>_a._next</sub>_\>r<sub>a</sub>_ so that \(s(\hat{\mu}(a.\text{next}))\) comes before \(s(\hat{\mu}(a))\). In this situation, we simple set \(\mu(a)=\perp\) by paying at most _r_<sub>_a._next</sub>. In more details, we start with \(\mu=\hat{\mu}\). We iterate over \(a\in cA\) in increasing order of _s(a_), whenever we encounter a window _a_ such that \(s(\hat{\mu}(a))<s(\hat{\mu}(a.\text{prev}))\), we find all \(a'\) with \(s(a')<s(a)\) but \(s(\hat{\mu}(a))<s(\hat{\mu}(a'))\), we set \(\mu(a')=\perp\) by paying an extra edit cost of _r<sub>a</sub>_.

Thus

\(\mathrm{ED}(\mu)\le\mathrm{ED}(\hat{\mu})+\sum_{a,\hat{\mu}(a)\neq\perp} r_a\le(1+8\epsilon)\mathrm{ED}(A,B).\)

This completes the proof.

