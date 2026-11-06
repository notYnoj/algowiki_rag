Note that with the input of the SASED instance \((\mathbf{F},\mathbf{F}')\), and the outputs of the SASED instances \((\mathbf{F},\mathbf{L}(\mathbf{F}'))\) and \((\mathbf{F},\mathbf{R}(\mathbf{F}'))\), we have collected all inputs for SED between \((\mathbf{F},\mathbf{F}')\), so we can run the SED algorithm to finish the algorithm in \(\mathcal{O}(f(n)g(n'))\) time.

The running time \(\mathsf{T}(n,n')\) of the algorithm can be formulated as the following formula:

\(\mathsf{T}(n,n')=2\mathsf{T}(n,n'/2)+\mathcal{O}(f(n)g(n')),\)

which can be upper bounded by \(\mathsf{T}(n,n')=\mathcal{O}(f(n)g(n')\mathrm{log}n')\).

Now we proceed to show the reduction from All-Subtrees-TED to SED.

**Lemma 6.4.** _Suppose there exists an algorithm for SED on two forests_ \(\mathbf{H},\mathbf{H}'\) _running in time_ \(\mathsf{T}_{SED}(m,m')=\mathcal{O}(f(m)g(m'))\)_, where_ \(m=|\mathbf{H}|,m'=|\mathbf{H}'|\) _and_ \(f(m)=\Omega(m),g(m')=\Omega(m')\) _are some functions. Then, there is an algorithm for All-Subtrees-TED on two forests_ \(\mathbf{F},\mathbf{F}'\) _running in time_ \(\mathcal{O}(f(n)g(n')\mathrm{log}^2\mathrm{max}(n',n))\)_, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\).

**Proof.** In the base case, if _n=_0 or \(n'=0\), we can simply return an empty set.

In general, given \(\mathbf{F},\mathbf{F}'\), we use Proposition 6.1 and Definition 6.2 to prepare **S**,**L**(**F**),**R**(**F**), \(\mathbf{S}',\mathbf{L}(\mathbf{F}'),\mathbf{R}(\mathbf{F}')\). We recursively solve All-Subtrees-TED in 4 instances \((\mathbf{L}(\mathbf{F}),\mathbf{L}(\mathbf{F}')),(\mathbf{L}(\mathbf{F}),\mathbf{R}(\mathbf{F}')),(\mathbf{R}(\mathbf{F}),\mathbf{L}(\mathbf{F}')),(\mathbf{R}(\mathbf{F}),\mathbf{R}(\mathbf{F}'))\).

Next, we apply Lemma 6.3 on inputs \((\mathbf{F},\mathbf{L}(\mathbf{F}')),(\mathbf{F},\mathbf{R}(\mathbf{F}')),(\mathbf{F}',\mathbf{L}(\mathbf{F})),(\mathbf{F}',\mathbf{R}(\mathbf{F}))\). Note that applying Lemma 6.3 on the first two instances clearly takes time \(\mathcal{O}(f(n)g(n')\mathrm{log}n')\). Applying Lemma 6.3 directly on the last two instances would take time \(\mathcal{O}(f(n')g(n)\mathrm{log}n)\). However, notice that by symmetry, if there exists a SED algorithm with running time \(\mathcal{O}(f(m)g(m'))\), there is also a SED algorithm with running time \(\mathcal{O}(g(m)f(m'))\) by swapping the two input forests. Applying Lemma 6.3 on the last two instances assuming the existence of a SED algorithm with running time \(\mathcal{O}(g(m)f(m'))\) gives us a running time \(\mathcal{O}(f(n)g(n')\mathrm{log}n)\). Hence, the overall running time of applying Lemma 6.3 is \(\mathcal{O}(f(n)g(n')\mathrm{logmax}(n',n))\).

Finally, at this point we have collected all required inputs for SED on input \((\mathbf{F},\mathbf{F}')\), so we can apply the assume SED algorithm in time \(\mathcal{O}(f(n)g(n'))\).

Let \(\mathsf{T}(n,n')\) be the running time of this algorithm, then it can be written as

\(\mathsf{T}(n,n')=4\mathsf{T}(n/2,n'/2)+\mathcal{O}(f(n)g(n')\mathrm{logmax}(n',n)),\)

which can be upper bounded by \(\mathsf{T}(n,n')=\mathcal{O}(f(n)g(n')\mathrm{log}^2\mathrm{max}(n',n))\).

Indeed, Lemma 2.1 follows directly from Lemma 6.4.

**Lemma 2.1.** _Suppose there exists an algorithm for SED on two forests_ \(\mathbf{H},\mathbf{H}'\) _running in time_ \(\mathsf{T}_{SED}(m,m')=\mathcal{O}(f(m)g(m'))\)_, where_ \(m=|\mathbf{H}|,m'=|\mathbf{H}'|\) _and_ \(f(m)=\Omega(m),g(m')=\Omega(m')\) _are some functions. Then, there is an algorithm for TED on two forests_ \(\mathbf{F},\mathbf{F}'\) _running in time_ \(\mathcal{O}(f(n)g(n')\mathrm{log}^2\mathrm{max}(n',n))\)_, where_ \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\).

**Proof.** We attach new roots _v_ and \(v'\) to the two forests **F** and \(\mathbf{F}'\) in the TED instance, resulting in the trees **T** and \(\mathbf{T}'\) (if the forests are already trees, the new root becomes the parent of the original root). We set weight such that we enforce that the two roots are both deleted. This ensures that \(\mathrm{sim}(\mathbf{F},\mathbf{F}')=\mathrm{sim}(\mathbf{T},\mathbf{T}')=\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\), which can be computed using Lemma 6.4.

As corollaries, we obtain the following results on tree edit distances, by applying Lemma 2.1 to Theorem 5.18 or Theorem 2.2.

**Main Theorem 1.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be forests of size_ \(n=|\mathbf{F}|,m=|\mathbf{F}'|\) _with_ \(n\ge m\)_. Then, there is an algorithm computing Tree Edit Distance between_ \(\mathbf{F},\mathbf{F}'\) _in time_ \(\tilde{\mathcal{O}}\left((n/m)^{1+o(1)}\cdot\left(\mathsf{T}_{MUL}(m)+m^{2+o(1)}\right)\right)\).

