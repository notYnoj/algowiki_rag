## APPENDIX H<br> UPPER BOUNDS FOR NON-ADAPTIVE SAMPLING

In this section, we present a theorem on the upper bounds for non-adaptive learning in the worst-case query model.

**Theorem H.1.** _One can design algorithm such that the worst-case query complexity is_

1) \(\mathcal{O}(\frac{K\mathrm{log}(K/\delta)}{1-H(p)})\) _for computing_ OR;<tbc>

2) \(\mathcal{O}(\frac{K^2\mathrm{log}(K/\delta)}{1-H(p)})\) _for computing_ MAX;<tbc>

3) \(\mathcal{O}(\frac{K\mathrm{log}(1/\delta)}{1-H(p)})\) _for computing_ SEARCH;<tbc>

_4)_ \(\mathcal{O}(\frac{K^2\mathrm{log}(K/\delta)}{1-H(p)})\) _for computing_ SORT;

The results for OR, MAX and SORT are based the simple algorithms of querying all possible elements equal number of times. And the analysis is a direct union bound argument. Here we only present the algorithm and analysis for SEARCH.

_Proof._ Assume that the target _X_ lies between _X<sub>l</sub>_ and _X_<sub>_l_+1</sub>. Consider the non-adaptive learning algorithm which compares _X_ with each element _X<sub>i</sub>_ for \(T_i=\lfloor T/K\rfloor=4\mathrm{log}(1/\delta)/(1-H(p))\) times.

Let _N<sub>i</sub>_ be the number of observations of 1 among _T<sub>i</sub>_ queries for element _X<sub>i</sub>_. Consider the following algorithm:<tbc>

\(\hat{l}=\mathrm{argmax}_{l\in[K]}\sum_{i=1}^lN_i+\sum_{i=l+1}^K(T_i-N_i).\)

<tbc>We show that with high probability, \(\hat{l}=l\). We have

\(\mathbb{P}(\hat{l}\neq l)\le\sum_{j\neq l}\mathbb{P}(\hat{l}=j)\)<br>
\(\le\sum_{j\neq l}\mathbb{P}\big(\sum_{i=1}^lN_i+\sum_{i=l+1}^K(T_i-N_i)-(\sum_{i=1}^jN_i+\sum_{i=j+1}^K(T_i-N_i))<0\big).\)

Now we bound the above probability for each _j_. Without loss of generality, we assume that _j\>l_. The above probability can be written as

\(\mathbb{P}\big(\sum_{i=1}^lN_i+\sum_{i=l+1}^K(T_i-N_i)<\sum_{i=1}^jN_i+\sum_{i=j+1}^K(T_i-N_i)\big)\)<br>
\(=\mathbb{P}\big(\sum_{i=l+1}^j(T_i-2N_i)<0\big)\)<br>
\(=\mathbb{P}\big(\sum_{i=l+1}^jN_i>\frac{1}{2}(j-l)\lfloor T/K\rfloor\big)\)

Note that \(\sum_{i=l+1}^jN_i\sim\mathsf{Bin}((j-l)\lfloor T/K\rfloor,p)\). Let \(n=\frac{1}{2}(j-l)\lfloor T/K\rfloor\). From Lemma A.6 we have

\(\mathbb{P}(\sum_{i=l+1}^jN_i\ge n/2)\le\big(\frac{e^\frac{1-2p}{2p}}{(1/2p)^{(1/2p)}}\big)^{np}=(2p\cdot\mathrm{exp}(1-2p))^{n/2}\)<br>
\(<\mathrm{exp}\big(\mathrm{log}(1/\delta)\cdot\frac{2(j-l)(1-2p+\mathrm{log}(2p))}{(1-2p)^2}\big)<\delta^{j-l}.\)

Now by summing over the probability for different \(j's\), we get

\(\mathbb{P}(\hat{l}\neq l)\le\sum_{j\neq l}\delta^{\lfloor j-l\rfloor}<\frac{2\delta}{1-\delta}.\)

Rescaling \(\delta\) finishes the proof.

