<tbc>differently in _M_<sub>1</sub> and _M_<sub>2</sub>. Let us assume now that there exists a pair in _M_<sub>2</sub> consisting of an original woman and a man \(\widetilde{m}_i^1\) for some \(i\in[b+1]\). Using our above observation this, however, implies that at least one man from each of the _k_ layers of the penalizing component is matched differently in _M_<sub>1</sub> and _M_<sub>2</sub>, contradicting that \(|M_1\triangle M_2|\le k\). Hence, no original woman can be matched to a man from the penalizing component in _M_<sub>2</sub>. From this it also follows that no original woman _w<sub>i</sub>_ can be unmatched or matched to a catch man in _M_<sub>2</sub>, as otherwise _w<sub>i</sub>_ forms blocking pairs with all _b_+1 men from the first layer of the penalizing component. Hence, all original women need to be matched to an original man in _M_<sub>2</sub>. This implies that the matching _N_<sup>∗</sup> defined as the matching _M_<sub>2</sub> restricted to original agents is a perfect matching of these agents which admits at most _z=b_ blocking pairs with \(|N\triangle N^*|\le q\), as \(|M_1\triangle M_2|=|N\triangle N^*|+|\{\{m_i^\star,w_i\}\}|i\in[t]\}|\).

On the positive side, we provide XP-algorithms for all three single parameters:

**Proposition 1.** IASM _is in XP when parameterized by any of k or b or_ \(|\mathcal{P}_1\oplus\mathcal{P}_2|\).

_Proof._ We give a separate proof for each parameter.

### Parameter _k_.

For the allowed size _k_ of the symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub>, we guess the set _F_ up to _k_ edges in \(M_1\triangle M_2\) and check whether \(M_1\triangle F\) is a stable matching.

### Parameter _b_.

For the number _b_ of blocking pairs _M_<sub>2</sub> is allowed to admit, we start by guessing the blocking pairs. For each guessed blocking pair {_m,w_}, we modify the preferences of _m_ in P<sub>2</sub> by deleting _w_ from his preferences and from Ac(_m_). Similarly to the polynomial-time algorithm for ISM, we now compute a maximum-weight stable matching _M_ for P<sub>2</sub>, where we set the weight of an edge to be 2 if it is contained in _M_<sub>1</sub>, and 0 otherwise. If the weight weight(_M_) of _M_ is at least |_M_<sub>1</sub>|+|_M_|-_k_, then we have \(|M\triangle M_1|=|M|+|M_1|-2|M\cap M_1|=|M|+|M_1|-\text{weight}(M)\le|M|+|M_1|-(|M_1|+|M|-k)=k\), so _M_ is a solution to the ISM instance. Otherwise, there is no matching _M_<sub>2</sub> with exactly the guessed set of blocking pairs and \(|M_1\cap M_2|\le k\) (note that due to the the Rural Hospitals Theorem all stable matchings after the deletion of the blocking pairs have the same size).

### Parameter \(|\mathcal{P}_1\oplus\mathcal{P}_2|\).

Note that each swap in some agent’s preferences can only create a single blocking pair for the initial matching _M_<sub>1</sub>. Thus, if \(|\mathcal{P}_1\oplus\mathcal{P}_2|\le b\), then we can simply set _M_<sub>2</sub>:=_M_<sub>1</sub>. Otherwise, we use the XP-algorithm for the number _b_ of blocking pairs.

We finally remark that while the XP-algorithm for the parameter _k_ also works for IASM-T, IASM- T is NP-hard even for _b_=0 and \(|\mathcal{P}_1\oplus\mathcal{P}_2|=1\) (as Bredereck et al. \[2020\] proved that ISM-T is NP-hard for \(|\mathcal{P}_1\oplus\mathcal{P}_2|=1\)).

## 5 Incremental Hospital Residents

We start our study of the incremental variant of HOSPITAL RESIDENTS by observing that one can reduce IHR to the polynomial-time solvable WEIGHTED STABLE MARRIAGE problem \[Feder, 1992\]; this yields:

**Proposition 2.** IHR _is solvable in_ \(\mathcal{O}(n^{2.5}\cdot m^{1.5})\) _time, where n is the number of residents and m is the number of hospitals._

_Proof._ Let \(\mathcal{I}=(A=R\cup H,\mathcal{P}_1,\mathcal{P}_2,M_1,k)\) be the given instance of IHR. We reduce the problem to an instance of WEIGHTED STABLE MARRIAGE where given an SM instance \((U\cup W,\mathcal{P})\), a weight<tbc>

