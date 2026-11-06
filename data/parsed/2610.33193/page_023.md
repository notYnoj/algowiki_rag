this proof appeared in \[Kor25\], it contained some bugs. Here we give a corrected proof of optimality and uniqueness up to the behavior of _Q_ on such inputs.

_Proof._ Picking _Q_ as in the statement of Lemma 3.1 exactly satisfies the best possible bound of:

\(\mathcal{L}_f(\mathcal{D})=\mathbb{E}_{x\sim\mathcal{D}}[Q(x)].\) (2)

To see that this choice is valid, we show that _Q_ satisfies Lemma 2.22. For every \(y\in\mathrm{supp}(f(\mathcal{D}))\) we have:

\(\sum_{x\in f^{-1}(y)}2^{-Q(x)}=\sum_{x\in f^{-1}(y)}\mathrm{Pr}_\mathcal{D}[x]\big/\mathrm{Pr}_{f(\mathcal{D})}[y]=1.\)

And for every \(y\unknown\in\mathrm{supp}(f(\mathcal{D}))\) the only constraint we place on _Q_ is that this quantity is at most 1.

Next we show that any heat function that minimizes the heat release on D must satisfy Lemma 3.1. Let _Q_<sup>∗</sup> be some other valid heat function that minimizes the expected heat release on input distribution D. Then per Lemma 2.22 for every \(y,\sum_{x\in f^{-1}(y)}2^{-Q^*(x)}\le 1\). Moreover if \(\sum_{x\in f^{-1}(y)}2^{-Q^*(x)}<1\) for some \(y\in\mathrm{supp}(f(\mathcal{D}))\) then there must be some \(x\in\mathrm{supp}(\mathcal{D}_{|f^{-1}(y)})\) where _Q_<sup>∗</sup>(_x_) could have been smaller while remaining valid, and therefore _Q_<sup>∗</sup> could not have been optimal. Thus we can assume that for every \(y\in\mathrm{supp}(f(\mathcal{D}))\):<tbc>

\(\sum_{x\in f^{-1}(y)}2^{-Q^*(x)}=1.\)

<tbc>This means that we can define the conditional Gibbs distribution \(\mathrm{Pr}_{(\mathcal{G}_{Q^*})_{|f^{-1}(y)}}[x]=2^{-Q^*(x)}\) for every \(y\in\mathrm{supp}(f(\mathcal{D}))\). Since _Q_<sup>∗</sup> is valid we know that for every \(y\in\mathrm{supp}(f(\mathcal{D}))\):<tbc>

\(\mathbb{E}_{x\sim(\mathcal{G}_{Q^*})_{|f^{-1}(y)}}[Q^*(x)]-\mathcal{S}((\mathcal{G}_{Q^*})_{|f^{-1}(y)})\ge 0.\)

<tbc>And since _Q_<sup>∗</sup> is a valid heat function that minimizes the heat release on the distribution D we know that for every \(y\in\mathrm{supp}(f(\mathcal{D}))\),<tbc>

\(\mathbb{E}_{x\sim\mathcal{D}_{|f^{-1}(y)}}[Q^*(x)]-\mathcal{S}(\mathcal{D}_{|f^{-1}(y)})=0,\)

<tbc>as Definition 2.21 requires that this expression be non-negative for every \(y\in\mathrm{supp}(f(\mathcal{D}))\) and we need the average of these terms to be 0 to match Eq. (2). But by Lemma 2.12, we know that this implies that for every _y_ where D<sub>|_f_<sup>-1</sup>(_y_)</sub> is defined, D<sub>|_f_<sup>-1</sup>(_y_)</sub>=(G<sub>_Q_<sup>∗</sup></sub>)<sub>|_f_<sup>-1</sup>(_y_)</sub> and hence for every _x_ where \(f(x)\in\mathrm{supp}(f(\mathcal{D}))\),

\(2^{-Q^*(x)}=\mathrm{Pr}_\mathcal{D}[x]\big/\mathrm{Pr}_{f(\mathcal{D})}[f(x)]=2^{-Q(x)}.\)

For _x_ where Pr<sub>_f_(D)</sub>\[_f(x_)\]=0 then both _Q(x_) and _Q_<sup>∗</sup>(_x_) can take on arbitrary non-negative values without affecting the optimality of the heat function, so long as it remains valid.

## 4 The complexity of optimizing heat functions in a given circuit

Here we show that computing optimal heat functions for gates in a fixed circuit is PP-hard.<sup>28</sup> In light of Lemma 3.1, this hardness result is hardly surprising: computing an optimal heat function<tbc>

<sup>28</sup>See \[AB09, Chapter 9\] for a discussion of the complexity class PP. Briefly, it is the class of decision problems/languages L for which yes-instances _x_, that like NP problems, have a polynomial-length _k_=poly(|_x_|) witness \(w\in\{0,1\}^k\), furthermore have at least _half_ of all \(w\in\{0,1\}^k\) as witnesses; see for example the language L<sub>SAT/2</sub> below. A probabilistic characterization (PP actually stands for "probabilistic polynomial-time") is that there is a randomized polynomial-time algorithm for L that answers ‘yes’ on input _x_ with probability at least 1/2 if and only if \(x\in\mathcal{L}\).

