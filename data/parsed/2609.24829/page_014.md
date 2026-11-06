## 4.1.1 Correctness of termination at round _i_.

For a given \(i\le p\), the passes 3_i_-1,3_i,_3_i_+1 are collectively called a _round_. The successful execution of round _i_ depends on three random events:

1. The probability that the oracle constructed correctly distinguished `H` and `L` edges.<tbc>

2. _Condition on the oracle’s success_, the probability that the segments of _S_<sup>L</sup> are representative of _S_<sup>L</sup>, the light edges in the stream.<tbc>

3. Conditioned on the above two events, the probability that the execution of A on a segment \(S_j^\mathrm{L}\) succeeds.

To make the second event precise, note that the classification of edges is a function of the sampled vertex set and the edge set alone, and in particular is independent of the ordering of the stream. Hence, conditioned on the oracle, _S_<sup>L</sup> is a uniformly random-order stream of the _m_<sub>L</sub> light edges. Let \(T_j^\mathrm{L}\) denote the number of triangles in \(S_j^\mathrm{L}\). We say that \(S_j^\mathrm{L}\) is _representative_ if

\(|T_j^\mathrm{L}-t^{-3}T_\mathrm{L}|\le\varepsilon t^{-3}\mathrm{max}(T_\mathrm{L},U_i).\)

On the success event of Lemma 4.2, every light edge satisfies \(t_e\le 2n^{1/2^i}\), so Lemma 4.1 applies to the light subgraph with \(\eta=2n^{1/2^i}\) and threshold _U<sub>i</sub>_, and each segment is representative with probability at least 1-1_/n_<sup>4</sup>. The probabilistic analyses of the next lemmas all follow from the same line of reasoning, captured by the following:

**Lemma 4.3** (Successful executions of A in round _i_)**.** Let M_<sub>i</sub>_ be the event that in round _i_, the execution of A on all segments of _S_<sup>L</sup> was successful. Then \(\mathrm{Pr}\left[\mathcal{M}_i\right]\ge 1-\delta-1/\mathrm{poly}(n)\).

_Proof._ For a given _i_, let E_<sub>i,oracle</sub>_ be the event that 4.2 holds at round _i_, and let E_<sub>i,j,rep</sub>_ be the event that the segment \(S_j^\mathrm{L}\) is representative of _S_<sup>L</sup> in round _i_. Let \(\mathcal{E}_{i,rep}=\cap_{j\in[t]}\mathcal{E}_{i,j,rep}\). By the union bound and 4.1,<tbc>

\(\mathrm{Pr}\left[\mathcal{E}_{i,rep}|\mathcal{E}_{i,\mathrm{oracle}}\right]\ge 1-1/n^3\)

<tbc>Let M_<sub>i,j</sub>_ be the event that in round _i_ the execution of A on the segment \(S_j^\mathrm{L}\) was successful, and let \(\mathcal{M}_i=\cap_{i\in[t]}\mathcal{M}_{i,j}\). By the union bound,<tbc>

\(\mathrm{Pr}\left[\mathcal{M}_i|\mathcal{E}_{i,rep},\mathcal{E}_{i,\mathrm{oracle}}\right]\mathrm{Pr}\left[\cap_{j\in[t]}\mathcal{M}_{i,j}|\mathcal{E}_{i,rep},\mathcal{E}_\mathrm{oracle}\right]\ge 1-t\delta-1/\mathrm{poly}(n)=1-O(\mathrm{log}(n)\delta)-1/\mathrm{poly}(n).\)

<tbc>Consequently,

\(\mathrm{Pr}\left[\mathcal{M}_i\right]\ge\mathrm{Pr}\left[\mathcal{M}_i|\mathcal{E}_{i,rep},\mathcal{E}_{i,\mathrm{oracle}}\right]\cdot\mathrm{Pr}\left[\mathcal{E}_{i,rep},\mathcal{E}_{i,\mathrm{oracle}}\right]\)<br>
\(=\mathrm{Pr}\left[\mathcal{M}_i|\mathcal{E}_{i,rep},\mathcal{E}_{i,\mathrm{oracle}}\right]\cdot\mathrm{Pr}\left[\mathcal{E}_{i,rep}|\mathcal{E}_{i,\mathrm{oracle}}\right]\cdot\mathrm{Pr}\left[\mathcal{E}_{i,\mathrm{oracle}}\right]\)<br>
\(\ge(1-O(\mathrm{log}(n)\delta)-1/\mathrm{poly}(n))(1-1/n^3)(1-1/n^2)\)<br>
\(=1-O(\mathrm{log}(n)\delta)-1/\mathrm{poly}(n).\)

Rescaling \(\delta\) shows the desired result.

**Lemma 4.4** (Heavy Triangles Estimation)**.** With probability 1-1_/n_<sup>3</sup>, at round _i_, \(\widehat{T_\mathrm{H}}\in(1\pm\varepsilon)T_\mathrm{H}\).

