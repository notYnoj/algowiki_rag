\(\le\delta(u,w)+2(k-1-(k_0+1))+2+\delta(w,v)\)<br>
\(\le\delta(u,v)+2(\lfloor k/3\rfloor+1)\)

completing the proof.

_Proof._ (Time Complexity)

Recall that _k=O_(1) is a constant.

Phase 0 requires _O(m_) time, as `Decompose` requires _O(k(m+n_))-time.

We examine Phase 1. Constructing the Euler Tours and `BFS` trees require \(\tilde{O}(n^2)\)-time over all iterations, as \(|C_i||F_i|=\tilde{O}(n^2)\). The expensive step therefore is the (min,+) product, which we compute with an invocation to `MonotoneMinPlus`. By Theorem 5.1, this requires,<tbc>

\(\tilde{O}\left(n^\frac{(a+b+\mu)+\omega(a,b,c)}{2}\right)\)

<tbc>where we apply

\(a=1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x\)<br>
\(b=1-x\)<br>
\(c=1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\)<br>
\(\mu=1\)

since all distances in _G_ are bounded by _n_.

In Phase 2, each \(|D_j|=\tilde{O}\left(n^{1-(k-j)}\frac{x}{\lfloor k/3\rfloor+2}\right)\) and \(|E_j|\le O\left(n^{1+(k-j+1)}\frac{x}{\lfloor k/3\rfloor+2}\right)\). Therefore, each invocation of `Dijkstra` in Phase 2 requires time \(\tilde{O}\left(n^{2+\frac{x}{\lfloor k/3\rfloor+2}}\right)\).

Finally, we balance terms to optimize,

\(\frac{\left(3-\frac{2\lfloor k/3\rfloor+2}{\lfloor k/3\rfloor+2}x\right)+\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)}{2}=2+\frac{x}{\lfloor k/3\rfloor+2}\)

To get the exact expression, we plug in \(k=\frac{3\beta-2}{2}\) and in particular \(\lfloor k/3\rfloor=\frac{\beta}{2}-1\).

\(\frac{\left(3-\frac{2\beta}{\beta+2}x\right)+\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)}{2}=2+\frac{2x}{\beta+2}\)<br>
\(\left(3-\frac{2\beta}{\beta+2}x\right)+\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=4+\frac{4x}{\beta+2}\)<br>
\(\omega\left(1-\frac{\beta-2}{\beta+2}x,1-x,1-\frac{\beta-4}{\beta+2}x\right)=1+\frac{4+2\beta}{\beta+2}x\)

2 exhibits the running times for a few values of \(\beta\) utilizing \[Bra\].

In the following lemma, we show that every distance estimate produced is feasible. That is, each distance estimate can be attained by some path in _G_.

**Lemma 5.10.** _Algorithm 6 returns_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) .

