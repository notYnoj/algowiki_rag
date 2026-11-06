_Proof._ Without loss of generality, assume \(a_x\ge 0\) for all _x_ (otherwise, replace _a<sub>x</sub>_ with |_a<sub>x</sub>_|). We define a probability distribution _P_ over the indices \(x\in[n]\) where \(p_x=a_x/\|A\|_1\). Let _U_ denote the uniform distribution over \[_n_\], i.e., _u<sub>x</sub>_=1_/n_.

Recall that the Kullback-Leibler (KL) divergence between _P_ and _U_ is defined as:

\(D(P\|U)=\sum_{x=1}^np_xln\left(\frac{p_x}{1/n}\right).\)

We view the recursive partitioning of _A_ as a tree T of depth _S_. For any recursion interval \(I\in\mathcal{T}\) (a node in the tree), let \(\sigma(I):=\sum_{x\in I}p_x\) be the total probability mass in that interval. For a scale-_s_ interval _I_ (where _s\<S_), let its _M_ sub-intervals on scale _s_+1 be _I_<sub>1</sub>_,...,I<sub>M</sub>_. We define the _local distribution_ at _I_ as the vector \(q_I\in\mathbb{R}^M\) where the _k_-th component is \(q_I(k)=\sigma(I_k)/\sigma(I)\). Note that if the mass were distributed uniformly, this local distribution would be _u_<sub>local</sub>=(1_/M,...,_1_/M_).

By the chain rule for KL divergence, the total divergence \(D(P\|U)\) decomposes into the sum of local divergences weighted by the mass of the parent intervals:

\(D(P\|U)=\sum_{s\in[S]}\sum_{I\in s}\sigma(I)\cdot D(q_I\|u_\mathrm{local}).\) (35)

Now, consider the mean deviation term TD_<sub>M</sub>(A<sub>I</sub>_) for a specific interval _I_. Substituting \(A_{\Sigma I_k}:=\|A\|_1\cdot\sigma(I_k)\), we have:

\(\mathrm{TD}_M(A_I)=\sum_{k=1}^M\left|A_{\Sigma I_k}-\frac{1}{M}A_{\Sigma I}\right|\)<br>
\(=\|A\|_1\sum_{k=1}^M\left|\sigma(I_k)-\frac{\sigma(I)}{M}\right|\)<br>
\(=\|A\|_1\cdot\sigma(I)\sum_{k=1}^M\left|\frac{\sigma(I_k)}{\sigma(I)}-\frac{1}{M}\right|\)<br>
\(=\|A\|_1\cdot\sigma(I)\sum_{k=1}^M\left|q_I(k)-\frac{1}{M}\right|.\)

The summation term \(\sum|q_I(k)-1/M|\) is exactly twice the Total Variation distance between the local distribution _q<sub>I</sub>_ and the uniform distribution _u_<sub>local</sub>. Using Pinsker’s inequality (\(2\mathrm{TV}(P,Q)^2\le D(P\|Q)\)), we bound this term:

\(\sum_{k=1}^M\left|q_I(k)-\frac{1}{M}\right|=2\mathrm{TV}(q_I,u_\mathrm{local})\le\sqrt{2D(q_I\|u_\mathrm{local})}.\)

Therefore, the contribution of interval _I_ to the total deviation is bounded by:

\(\mathrm{TD}_M(A_I)\le\|A\|_1\cdot\sigma(I)\sqrt{2D(q_I\|u_\mathrm{local})}.\)

Let _C<sub>s</sub>_ be the sum of deviations on a scale _s_. Summing over all intervals _I_ on scale _s_:

\(C_s=\sum_{I\in s}\mathrm{TD}_M(A_I)\le\|A\|_1\sum_I\sigma(I)\sqrt{2D(q_I\|u_\mathrm{local})}.\)

