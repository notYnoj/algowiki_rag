_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathsf{D})=\mathcal{O}(f(n')g(\mathsf{D}))\).

**Lemma 5.14.** _Suppose we are given an_ \((s,s',q,q')\)_-UDISED instance of size m, and let_ \(r\in\mathbf{S}\) _be such that s\<r\<q. Then, we can reduce the_ \((s,s',q,q')\)_-UDISED instance to the_ \((s,s',r,q')\)_-UDISED and_ \((r,s',q,q')\)_-UDISED instances in time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MUL}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathsf{D})=\mathcal{O}(f(n')g(\mathsf{D}))\).

We now give an algorithm for the UDISED problem.

**Lemma 5.15.** _There exists an algorithm_ A<sub>_UDISED_</sub> _solving UDISED which runs in time_ \((m/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}\right)\) _on instances of size_ \((m,n')\).

_Furthermore, if the UDISED instance is unweighted, then the algorithm only requires time_ \((m/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathsf{D})=\mathcal{O}(f(n')g(\mathsf{D}))\).

**Proof.** It suffices to apply recursively (the simplified version of) Lemma 5.4 with threshold \(\Delta(m)=m/\alpha\) for a constant \(\alpha\ge 1\) to be determined later. In particular, we decompose only the larger tree **F**.

If \(m=\mathcal{O}(n')\), we simply apply Lemma 5.12 to the instance. Otherwise, we proceed to construct a set \(I\subseteq\mathbf{S}\times\mathbf{S}\) using Algorithm 2 with threshold \(\Delta\) yielding a sequence of spine nodes \(s=r_1<r_2<\cdots<r_d=q\). The algorithm guarantees for each \(i\in[1..d)\), either \((r_i,s',r_{i+1},q')\)-UDISED has size at most \((\Delta,n')\) or _r<sub>i</sub>_ immediately precedes _r_<sub>_i_+1</sub>. To complete the reduction we recursively solve \((r_i,s',r_{i+1},q')\)-UDISED instances, which requires total time \(\mathcal{O}(d\mathsf{T}(\Delta,n'))\) in the former case and \((m/n')^{1+o(1)}\cdot\mathsf{T}_{MUL}(n')\) in the latter case, since the combined size of the instances in the latter case is at most \((m,n')\). Note that there are at most _d_ instances to recombine, and thus recombining the instances require \(\mathcal{O}(d(m/n')^{1+o(1)}\cdot\mathsf{T}_{MUL}(n'))\).

Thus, we obtain the following recurrence by using \(d\le 3m/\Delta\) so that for some constant _C_,

\(\mathsf{T}(m)=\mathcal{O}(3m/\Delta\mathsf{T}(\Delta,n')+(m/n')^{1+o(1)}\cdot(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}))\)<br> \(\le 3C\alpha\mathsf{T}(m/\alpha,n')+(m/n')^{1+o(1)}\cdot(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}).\)

For any \(\varepsilon>0\), we can choose a sufficiently large constant \(\alpha\) such that \(log_\alpha(3C\alpha)<1+\varepsilon\). Similarly as in Corollary 4.14 we conclude that \(\mathsf{T}(m,n')=(m/n')^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(n')+n'^{2+o(1)}\right)\).

In the unweighted setting, we instead have the recurrence

\(\mathsf{T}(m)=\mathcal{O}(3m/\Delta\mathsf{T}(\Delta,n')+(m/n')^{1+o(1)}\cdot(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n')))\)

which yields the desired result.

It remains to prove the necessary lemmas.

## 5.5.1 Handling the Recursive Case

We begin with the recursive case where we patch together two sub-problems.

**Lemma 5.14.** _Suppose we are given an_ \((s,s',q,q')\)_-UDISED instance of size m, and let_ \(r\in\mathbf{S}\) _be such that s\<r\<q. Then, we can reduce the_ \((s,s',q,q')\)_-UDISED instance to the_ \((s,s',r,q')\)_-UDISED and_ \((r,s',q,q')\)_-UDISED instances in time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MUL}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathsf{D})=\mathcal{O}(f(n')g(\mathsf{D}))\).

