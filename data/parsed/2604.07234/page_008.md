<tbc>the null and planted variants of the Random Subsequence Model as a structural hypothesis testing problem. For each ambient string \(x\in\{0,1\}^N\), we define an _x-good set_

\(\mathcal{G}(x)\subseteq\{0,1\}^M\)

of strings that are "well-aligned" to _x_ so that we obtain the following distinguishing property.

\(\bullet\) For (_X,Y_) drawn from the planted model, \(Y\in\mathcal{G}(X)\) with probability \(1-e^{-\Omega(N)}\).<tbc>

\(\bullet\) For \((X',Y)\) drawn from the null model, \(Y\notin\mathcal{G}(X')\) with probability \(1-e^{-\Omega(N)}\).

The strict inequality of (1.8) is then obtained by showing that for typical _x_, only an exponentially small fraction of its length-_M_ subsequences belong to G(_x_). The strict inequality of (1.6) essentially comes from combining this null estimate with the size-bias relation between the null and planted laws.

To define G(_x_), we partition _x_ into _B=B(N_):=_N/b_ contiguous blocks _x_<sup>(1)</sup>_,...,x_<sup>(_B_)</sup> of length _b_, where _b_ is large but fixed. If _Y_ is a planted subsequence of _x_, then the embedding induces a decomposition<tbc>

\(Y=\big(Y^{(1)},\dots,Y^{(B)}\big),\)

<tbc>where _Y_ <sup>(_i_)</sup> is the portion of _Y_ contributed by the block _x_<sup>(_i_)</sup>. For a typical block of _x_, the sign of the block sum in _Y_ <sup>(_i_)</sup> is more likely than not to agree with that of _x_<sup>(_i_)</sup>, and the strength of this bias is captured by the random-walk displacement \(\Delta(Y^{(i)})\). This leads to the _local alignment A_loc(_x_<sup>(_i_)</sup>_,y_<sup>(_i_)</sup>), which rewards agreement of block majorities while weighting it by the size of the displacement. Taking the supremum of the resulting average local alignment over _induced near-equipartitions_ of _y_, thought of as the collection of typical block structures of _Y_ drawn from the planted model, yields the _induced total alignment T_ind(_x,y_). Section 3.2 shows that for every typical _x_, with probability \(1-e^{-\Omega(N)}\), a planted subsequence _Y_ satisfies

\(T_\text{ind}(x,Y)\ge\frac{1}{2}+\beta^\star(\alpha),\)

where \(\beta^\star(\alpha)>0\) is an appropriate constant. This is the _regular alignment property_ that defines G(_x_).

0.40
0.35
0.30
0.25
0.20
value
0.15
0.10
0.05
strict-weak polymer exact solution random subsequence null model simulation
0.00
0.0
0.1
0.2
0.3
0.4
0.5
a = M/N

Figure 2. The blue curve is the exact solution (1.9) for _a_=1_,b_=1/2, and the orange curve is obtained by numerically solving (1.4) for the null Random Subsequence Model, _N_=10,000. The plot is in the interval \(\alpha\in[0,1/2]\) because, outside of that range, we

have _Z<sub>X,Y</sub>_=0 with high probability for the null Random Subsequence Model.

