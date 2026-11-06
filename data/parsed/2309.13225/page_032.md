Phase 1 calls `dominatingSetAPASP` \(b=\tilde{O}(1)\) times. In each call, we call `BFS` on the graph (_V,F<sub>i</sub>_) from dominating set _C<sub>i</sub>_ in time \(\tilde{O}\left(\left|C_i||F_i\right|\right)=\tilde{O}\left(\frac{n}{t_i}2nt_i\right)=\tilde{O}\left(n^2\right)\). Then, we compute a `boundedMinPlus` on matrices of size at most \(\left|D_{l-\frac{l_0}{2}}\right|\times\left|C_i\right|\) and \(\left|C_i\right|\times\left|D_{l-\frac{l_0}{2}+1}\right|\). Since \(\left|C_i\right|=O(\left|C_b\right|)=\tilde{O}\left(\frac{n}{t_b}\right)=\tilde{O}\left(2^b\right)=\tilde{O}\left(n^{1-x}\right)\), all computations of `boundedMinPlus` require time at most,

\(\tilde{O}\left(n^{\omega\left(1-\frac{l_0}{2}x,1-x,1-\frac{l_0}{2}-1}{l-l_0}x\right)}\right)=\tilde{O}\left(n^{\omega\left(1-\frac{l_0}{2(l-l_0)}x,1-x,1-\frac{l_0-2}{2(l-l_0)}x\right)}\right)\)<br>
\(=\tilde{O}\left(n^{\omega\left(1-\frac{k-2}{2(l-k+2)}x,1-x,1-\frac{k-4}{2(l-k+2)}x\right)}\right)\)

To optimize, we use \[Bra\] and choose _x,l_ minimizing,

\(t_\mathrm{max}=\mathrm{max}\left(\omega\left(1-\frac{k-2}{2(l-k+2)}x,1-x,1-\frac{k-4}{2(l-k+2)}\right),2+\frac{x}{l-k+2},1.5+x\right)\)

Finally, note that `denseAPASP` requires \(\tilde{O}(n^{2+\frac{2}{3M-2}})\) time. Given our choice of _x,l_, we simply choose _M_ to be a large enough constant such that the running time of `denseAPASP` does not exceed \(2+\frac{2}{3M-2}\le T_\mathrm{max}\). We give a few example running times in Proposition C.4 and  1.

## 5 Additive Approximation via Monotone (min,+) Product

In the following section, we will use the fast monotone (min,+) product of Chi, Duan, Xie, and Zhang \[CDXZ22\] to the additive approximation framework of Dor et al. \[DHZ00\]. In particular, this will generalize the result of Deng et al. \[DKR<sup>+</sup>22\] to all distances. Whereas Deng et al. \[DKR<sup>+</sup>22\] use fast rectangular matrix multiplication for bounded difference matrices, we will require a more general fast rectangular matrix multiplication. To do so, let us begin by designing a fast algorithm for multiplying rectangular matrices, of which only one is monotone.

### 5.1 Rectangular Monotone (min,+) Product

Following the algorithm of \[CDXZ22\], we give a simple extension of their result for monotone matrices to rectangular monotone matrices. This result slightly extends the work of Durr \[Dür23\] to handle the most general case of rectangular matrices, which is required in our application.

**Theorem 5.1.** _Let A be a_ \(n^a\times n^b\) _integer matrix with non-negative entries bounded by_ \(O(n^\mu)\)_. Let B be a_ \(n^b\times n^c\) _row-monotone integer matrix with non-negative entries bounded by_ \(O(n^\mu)\)_. Then, there is an algorithm `MonotoneMinPlus` computing C=A∗B in time,_

\(\tilde{O}\left(n^\frac{(a+b+\mu)+\omega(a,b,c)}{2}\right)\)

Since the algorithm and proof remain largely unchanged, we only provide a sketch of the proof.

Let \(\alpha\in[0,1]\) be a parameter to be fixed, and let _p_ be a uniformly random prime chosen in \([40n^\alpha,80n^\alpha]\). We make the same simplifying assumption as in \[CDXZ22\]. By Lemma 3.4 of \[CDXZ22\], this assumption is justified.

