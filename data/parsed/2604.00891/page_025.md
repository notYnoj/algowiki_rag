We next analyze the running time and the number of oracle calls. Consider any recursive call of `red-portals`. By Lemma 6, this calls `red-portals` at most \(2\cdot 2^{22log^2(2\alpha_\pi d+3)}\le 2^{88log^2(d)}\) times and in each such call, the value of _y_ is increased by one. Hence, the number of recursive calls of `red-portals` corresponds to the number of vertices in a tree of depth 22log(_d_)-1 and degree 2<sup>88log<sup>2</sup>(_d_)</sup>. Hence, the number of oracle calls (calls of `solve-\(\pi\)-r` and the number of leaves in the tree) is at most

\(\big(2^{88log^2(d)}\big)^{(22log(d)-1+1)}\le 2^{88log^2(d)\cdot 22log(d)}\le 2^{2000log^3(d)}\)

and the number of recursive calls of `red-portals` (the number of internal vertices in the tree) is at most 2<sup>2000log<sup>3</sup>(_d_)</sup>-1.

It remains to analyze the running time of each recursive call. Note that each single line except for Line 2 can be executed in O(_n_<sup>2</sup>) time.

Line 2 takes \(2^{\mathcal{O}(log^2(\alpha_\pi d))}n^{1+o(1)}\subseteq 2^{\mathcal{O}(log^2(d))}n^2\) time by Lemma 6. Since \(|V'|\le n\) and \(d'=d\) for each recursive call, Requirements R2, R3, and R4 state that Line 2 each take \(\mathcal{O}(\gamma(d)n^\rho)\) time. Since the number of separators in S is at most \(2^{44log^2(2d\alpha_\pi+3)}\in 2^{\tilde{\mathcal{O}}(1)}\) and the number of possible pebble sets for \(((X_\mathrm{he}\cup Y_\mathrm{he},X_\mathrm{he}\cup Y_\mathrm{he},X_\mathrm{he}\cup Y_\mathrm{he}),x+2y)\) is by Lemma 8 at most

\(2^{40(200log^7(d))\alpha_\pi\sqrt{d}}\cdot\left(\begin{array}{ c }
60(200log^7(d))\alpha_\pi dlog(d) \\
20(200log^7(d))\alpha_\pi\sqrt{d}log(d)
\end{array}\right)\in 2^{\tilde{\mathcal{O}}(\sqrt{d})}\)<br>
\((\text{since}|X_\mathrm{he}\cup Y_\mathrm{he}|\le 40(200log^7(d))\alpha_\pi\sqrt{d}\text{and}|X_\mathrm{li}\cup Y_\mathrm{li}|\le 60(200log^7(d))\alpha_\pi dlog(d)),\)

we have that the running time for one recursive call is in \(2^{\tilde{\mathcal{O}}(\sqrt{d})}\gamma(d)n^{max(2,\rho)}\).

## 3.4 Main Algorithm

We are finally in a position to prove our main theorem by showing that `solve-\(\pi\)-r` solves \(\pi\)- Request. We start with a description of the algorithm and then proceed with the formal proof.

Following the intuition presented in the introduction, `solve-\(\pi\)-r` works by first checking whether we can solve the base case. If \(|V|\le 2^{7\alpha_\pi}\), then it can afford to brute-force the solution and if \(d\le 2^{7\alpha_\pi}\), then it calls `base-case`. It then checks whether (_B,x_) is measured for _d_ and \(\alpha_\pi\), that is, whether the size of _B_ and the value of _x_ are small enough to proceed or whether `red-portals` has to be called. If (_B,x_) is measured, then `solve-\(\pi\)-r` finds a cycle separator _C_ and guesses whether _C_ contains at most \(20\sqrt{d}log(d)\) vertices of the (unknown) solution _Z_ or more. In the first case, it solves the corresponding instances in the interior and exterior of _C_ and combines the results (Requirement R4 ensures that this can be done). Otherwise, it uses the fact that _C_ contains many vertices of the solution to reduce the value of _d_ as follows. Since _C_ contains at least \(20\sqrt{d}log(d)\) vertices of _Z_, both the strict interior and the strict exterior of _C_ contain at most \(|Z|-20\sqrt{d}log(d)\) vertices. Hence _C_ is \(\frac{|Z|-20\sqrt{d}log(d)}{|Z|}\) -balanced for the weight function that assigns weight 1/|_Z_| to each vertex in _Z_ and zero to all other vertices. Using Lemma 6, the algorithm computes a set of cycle separators where one of those is also \(\frac{|Z|-20\sqrt{d}log(d)}{|Z|}\) -balanced for the mentioned weight function and does not intersect the solution in more than \(17\sqrt{d}log(d)\) vertices. Thus, the algorithm applies Lemma 1 (which is permitted by Requirement R1) to compute a \(\lfloor d-3\sqrt{d}\rfloor\)-outerplanar subgraph \(G'\) of both the interior and the exterior of each computed cycle separator, solves the problem recursively, and combines the solutions; again Requirement R4 allows us to combine solutions. Intuitively, we make progress in each recursive call as we either reduce the number of vertices by a constant factor or reduce the parameter _d_ by roughly \(3\sqrt{d}\). We will prove that this is sufficient for the claimed running time and now proceed with the formal proof of Theorem 3, which we restate here for convenience.

