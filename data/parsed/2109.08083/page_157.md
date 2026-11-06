Similarly, when _n_ is even and 3|_n_, to satisfy (d) and (e) in Lemma 3.18 reduces to showing that

\(\frac{n^2}{3}+\frac{n}{2}+\frac{1}{6}+\frac{n}{12}+\frac{1}{6}\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in\mathbb{Z},\)

which is equivalent to showing that

\(2+n+2\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in 12\mathbb{Z}.\)

When _n_ is even and 3 \(\unknown n\) satisfying (d) and (e) in Lemma 3.18 reduces to showing that

\(\frac{n^2}{3}+\frac{n}{2}+\frac{1}{6}+\frac{3n}{4}+\frac{1}{2}\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in\mathbb{Z},\)

and since in this case we have \(n^2\equiv 1\) mod 3, this is equivalent to showing that

\(2+n+2\sum_{i\in[3]}(a_i+b_i+c_i-d_i)\in 4\mathbb{Z}.\)

These conditions are all satisfied by the constraints on _a<sub>i</sub>,b<sub>i</sub>,c<sub>i</sub>,d<sub>i</sub>_ given in the proof of Theorem 1.3.

We could, of course, give explicit collections for the 12 queens taken out and chosen to attack toroidally (but not classically), but the general description above shows that there are many choices for every _n_ sufficiently large.

## 7.2. Concluding remarks

Theorem 1.2, our main result, asymptotically answers an open question of Pólya [49] from 1918, as well as settling conjectures of Rivin, Vardi and Zimmerman [50] and Luria [39]. The proof of Theorem 1.2 uses the upper bounds of Luria [39] and the lower bound is our main contribution. Recall that previously there was no known non-trivial lower bound for all \(n\equiv 1,5\) mod 6 and the best lower bound for some _n_ was due to Luria [39] using very different methods. Together with Theorem 1.3 and the upper bounds of Luria both for the toroidal and classical case, we completely settle Conjecture 1.1, but we also recall that the classical case of the conjecture has been independently settled by the recent lower bound of Luria and Simkin [40] matching our lower bound in Theorem 1.3. One difference in our results, other than the vastly different strategies, is that whilst their lower bound obtains ‘almost-toroidal’ _n_-queens configurations in the sense that there are at most _o(n_) toroidal attacks for each classical configuration, our result produces the same count for an even stronger structure where we obtain the same lower bound, but counting only those configurations where at most some constant \(C\le 12\) toroidal attacks occur for each classical configuration counted. We note that the three pairs of toroidal attacks on the _X+Y_ diagonal and three pairs of toroidal attacks on the _X-Y_ diagonal used in the proof of Theorem 1.3 is not necessarily best possible for all _n_, but does indeed work for all _n_. For example, when _n_ is even and 3 \(\unknown n\), our constructions in the proof of Theorem 1.3 work taking only _i_=1 and disregarding _i_=2,3 so that we then have only one pair attacking toroidally along the _X+Y_ diagonal and only one pair attacking toroidally along the _X-Y_ diagonal.

