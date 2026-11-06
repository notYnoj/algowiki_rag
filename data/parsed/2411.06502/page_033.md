**Proof.** We apply Lemma 4.8 recursively with threshold \(\Delta=n/\alpha\) for some constant \(\alpha\ge 1\) on forest **F**. As before, for small enough instances when \(n=O(n')\) we can simply apply our algorithm for BBD and compute the output in \(\mathcal{O}(\mathsf{T}_\mathsf{MUL}(n'))\) time. Thereby, we obtain an algorithm for the LRBBD Problem where the running time is described by the formula

\(\mathsf{T}(n,n')=\mathcal{O}\left(\frac{n}{\Delta}\right)\mathsf{T}(\Delta,n')+\mathcal{O}\left(\frac{n^2}{\Delta n'}\mathsf{T}_\mathsf{MUL}(n')\right).\)

Note that the recurrence terminates at \(\mathsf{T}(n',n')=\mathcal{O}\left(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}\right)\). By our choice of \(\Delta\), there exists a constant _C_ such that

\(\mathsf{T}(n,n')\le(C\alpha)\mathsf{T}(n/\alpha,n')+\left(C\alpha\frac{n}{n'}\right)\mathsf{T}_\mathsf{MUL}(n').\)

We choose a constant alpha such that \(log_\alpha(C\alpha)<1+\varepsilon\) for arbitrarily small \(\varepsilon>0\) so that \(\mathsf{T}(n,n')=(n/n')^{1+o(1)}\cdot\left(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)}\right)\).

When the diameter is at most \(\mathcal{O}(n')\), we instead have the recurrence for some constant _C_,

\(\mathsf{T}(n,n')\le(C\alpha)\mathsf{T}(n/\alpha,n')+\left(C\alpha\frac{n}{n'}\right)\mathsf{T}_\mathsf{MonMUL}(n').\)

again with the recurrence terminating at \(\mathsf{T}(n',n')=\mathcal{O}(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}g(n'))\). As before, we choose a constant \(\alpha\) such that the time can be bounded by \(\mathsf{T}(n,n')=(n/n')^{1+o(1)}\cdot\left(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\).

Finally, to conclude, we give an algorithm computing certain outputs of the FED problem efficiently, defined as the UFED problem.

Using an identical proof to Main Theorem 4, we obtain the following result on UFED, noting that the paths in the LRBBD instance correspond to the desired outputs. In particular, in an LRBBD instance we compute all distances in the BBD instance except those originating from the bottom border. Then,

**Theorem 4.15.** _There is an algorithm for UFED running in time_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_\mathsf{MUL}(n')+n'^{2+o(1)}\right)\) _where_ \(|\mathbf{F}|=n\), \(|\mathbf{F}'|=n'\) _and_ \(n\ge n'\).

**Theorem 2.3.** _There is an algorithm for unweighted UFED running in time_ \((n/n')^{1+o(1)}\cdot\left(\mathsf{T}_\mathsf{MonMUL}(n')+n'^{2+o(1)}g(n')\right)\) _where n_=|**F**|, \(n'=|\mathbf{F}'|\), \(n\ge n'\) _and_ \(\mathsf{T}_\mathsf{MonMUL}(n',n',n',\mathsf{D})=\mathcal{O}(f(n')g(\mathsf{D}))\) _for some functions f, g._

Since the proofs are essentially identical, we give both here.

**Proof.** We apply Corollary 4.14 to the generalized alignment graph. We consider the three outputs separately.

For Output (1), we obtain the desired similarity value by the distance from \((1,x')\) to \((n+1,y')\).

Unbalanced Forest Edit Distance (UFED) Input: Two forests F and F' and sim(sub(v),sub(v')) for all (v, v') ∈ F × F'. Output: The following values: (1) sim(F, F'[ x'.. y' )) for all x', y' ∈ [1..(2|F'|+1)], and (2) sim(F[1.. y ), F'[ x'..(2|F'|+1))) for all y ∈ [1..(2|F|+1)], x' ∈ [1..(2|F'|+1)]. (3) sim(F[ x..2|F|+1), F'[1.. y' )) for all x ∈ [1..(2|F|+1)], y' ∈ [1..(2|F'|+1)].

