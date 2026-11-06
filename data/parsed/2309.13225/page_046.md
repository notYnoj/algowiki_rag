**Case 1:** deg(_P)\<s_<sub>_k_<sub>0</sub></sub> Since \(L(P,k)\subset\{k_0+1,\dots,k-1\}\), correctness holds as in Theorem 5.6.

**Case 2:** \(\mathrm{deg}(P)\ge s_{k_0}\) By assumption, there is a vertex \(w\in P\) with \(\mathrm{deg}(w)\ge s_{k_0+3}\). Then, with Lemma 5.17, we have that for all \(x\in P\),

\(\hat{\delta}_{k_0+3}(w^*,x)\le\delta(w,x)+5\)

The remaining proof follows as in Theorem 5.6.

_Proof._ (Time Complexity)

As the only modifications are in Phase 1, we examine only the complexity of this phase. Each \(|C_i|=\tilde{O}(\frac{n}{t_i})=\tilde{O}(2^i)\) Each graph _F<sub>i</sub>_ has _O(nt<sub>i</sub>_) edges. Thus, each `BFS` requires \(\tilde{O}(n^2)\)-time. Over _k_ iterations, this is again \(\tilde{O}(n^2)\)-time.

Now, \(|D_{k_0+2}|=\tilde{O}\left(\frac{n}{s_{k_0+2}}\right)=\tilde{O}\left(\frac{n}{s_{k-\lfloor k/3\rfloor}}\right)=\tilde{O}\left(n^{1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x}\right)\). Similarly, we can upper bound the size of _D_<sub>_k_<sub>0</sub>+3</sub> as \(|D_{k_0+3}|=\tilde{O}\left(\frac{n}{s_{k-(\lfloor k/3\rfloor-1)}}\right)=\tilde{O}\left(n^{1-\frac{\lfloor k/3-1\rfloor}{\lfloor k/3\rfloor+2}x}\right)\). Finally, \(|C_i|=\tilde{O}(2^l)=\tilde{O}(n^{1-x})\). Thus, each `BoundedMinPlus` requires time,

\(\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)\)

Recall that Phase 2 requires time \(\tilde{O}\left(n^{2+\frac{x}{\lfloor k/3\rfloor+2}}\right)\). Finally, we balance terms to optimize,

\(\omega\left(1-\frac{\lfloor k/3\rfloor}{\lfloor k/3\rfloor+2}x,1-x,1-\frac{\lfloor k/3\rfloor-1}{\lfloor k/3\rfloor+2}x\right)=2+\frac{x}{\lfloor k/3\rfloor+2}\)

To get the exact expression, we plug in \(k=\frac{3\beta-2}{2}\) and in particular \(\lfloor k/3\rfloor=\frac{\beta}{2}-1\).

In the following lemma, we show that every distance estimate produced is feasible. That is, each distance estimate can be attained by some path in _G_.

**Lemma 5.16.** _Algorithm 7 returns_ \(\hat{\delta}\) _such that_ \(\delta(u,v)\le\hat{\delta}(u,v)\) _for all_ \(u,v\in V\) .

_Proof._ This holds simply by observing that every distance estimate is produced by some path in the original graph _G_, as argued in Lemma 5.10.

We present the key lemma for correctness below. In particular, we prove that we have a good additive approximation after the (_k_<sub>0</sub>+3)-th iteration.

**Lemma 5.17.** _Let P be a shortest path between u,v. In Phase 2 of Algorithm 7, let w be a vertex of P in V_<sub>_k_<sub>0</sub>+3</sub>_. Then, for every vertex_ \(x\in P\)_, the_ (_k_<sub>0</sub>+3)_-th iteration of Phase 2 finds a path of length_ \(\delta(w,x)+5\) _from w_<sup>∗</sup> _to x._

_Proof._ Let _P<sub>w,x</sub>_ denote the sub-path of _P_ between _w_ and _x_.

**Case 1:** \(\mathrm{deg}(P_{w,x})\le s_{k_0}\) This is identical to Case 1 of Lemma 5.11.

