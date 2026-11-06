### 3.4 Blind pick and the equivalent blind-pick size

A blind pick selects _s_ designs uniformly at random without comparing them. Its selected set contains a design of the good-enough set with probability

\(B(n,r,s)=1-\frac{\genfrac(){pt}{2}{n-r}{s}}{\genfrac(){pt}{2}{n}{s}},\) (3)

the blind-pick alignment probability at alignment level one \[2, 3\]. When a second stage identifies the best of the _s_ designs exactly, as in the two-stage use of OO \[2\], that design is good enough with the same probability. For _r_=1, _B(n,_1_,s_)=_s/n_.

For \(1\le r\le n\) and with \(\genfrac(){pt}{2}{a}{b}=\Gamma(a+1)/\big(\Gamma(b+1)\Gamma(a-b+1)\big)\), the ratio in (3) extends to real _s_ in \[0_,n-r_+1\], with _B(n,r,n-r_+1)=1. The logarithmic derivative of the ratio in _s_ is \(\psi(n-r-s+1)-\psi(n-s+1)<0\), where \(\psi\) is the digamma function, so _B(n,r,s_) increases strictly in _s_ from 0 to 1.

**Definition 3.** For \(1\le r\le n\), the equivalent blind-pick size of a value \(P\in[0,1]\) is the unique \(s_\mathrm{eq}(n,r)\in[0,n-r+1]\) with _B(n,r,s_<sub>eq</sub>)=_P_. We write \(s_\mathrm{eq}^Q(n,r)\) for _P=Q<sub>q</sub>(n,r_) and \(s_\mathrm{eq}^C(n,r)\) for _P=C<sub>q</sub>(n,r_). For _r_=1, \(s_\mathrm{eq}^Q(n,1)=nQ_q(n,1)\). We leave the dependence on _P_ and, for the classical and quantum values, on _q_ implicit in this notation.

Using equivalent blind-pick sizes follows the OO practice of comparing selection rules by the selected-set size needed for a given alignment probability \[2\].

### Scope.

Comparisons are exact, meaning noiseless, and the oracle is coherent, so the algorithm may query superpositions of pairs. The budget counts oracle calls. Exact comparisons model problems in which each design is evaluated deterministically but at high cost, such as a unit commitment evaluated against a fixed set of scenarios. Whether such an evaluation can be queried coherently, and at what cost, is the question of Section 8.3. When performance is observed only through noisy simulation, an exact comparison cannot be implemented directly \[9\]. Section 8.2 discusses extensions to that setting.

The choice of cost unit also affects the interpretation. In a model that charges evaluated designs, a blind pick followed by keeping the best is the natural rule. With comparisons as the cost unit, Theorem 1 below shows that _q_ comparisons attain exactly the alignment probability of _q_+1 evaluated designs, although the comparisons can involve up to 2_q_ designs. The results of this paper count comparison queries and make no claim about running time. If a coherent comparison is built from an oracle that evaluates one design, computing and uncomputing both evaluations uses four evaluation calls, and four evaluated designs already contain the best design with probability 4_/n_. The one-comparison gain of Sections 6 and 7 is therefore a gain per comparison and not per evaluation. The order of growth discussed in Section 8.1 does not change under this unit, because _q_ comparisons then cost 4_q_ evaluations while the quantum equivalent blind-pick size grows quadratically in _q_. The gate cost of an oracle call requires a further cost model, as discussed in Section 8.3.

## 4 The classical optimum

The blind-pick formula gives the success probability of a knockout on a random subset with one more design than the comparison budget. We first show that no adaptive comparison<tbc>

