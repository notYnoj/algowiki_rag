We can therefore restrict our attention to the generic _i_-th iteration of the for loop. From Theorem 4.10 we have that each invocation of NoisySearch on _S_<sub>_i_-1</sub> takes time _O_(log|_S_<sub>_i_-1</sub>|)=_O_(log_n_), leading to a total search time of _O_(|_T<sub>i</sub>_|log_n_). Then, the insertion trivially takes _O_(|_S_<sub>_i_-1</sub>|+|_T<sub>i</sub>_|)=_O_(|_S<sub>i</sub>_|) time. Furthermore, by Theorem 5.20, \(\mathtt{BasketSort}(S_i,\gamma\cdot\beta_\mathrm{max}\cdot\mathrm{ln}n)\) requires _O_(|_S<sub>i</sub>_|log_n_) time (recall that both \(\gamma\) and \(\beta_\mathrm{max}\) are constants depending only on _p_ and _q_). To sum up, since \(|T_i|\le 2^{i-1}\lceil\sqrt{n}\rceil\) and \(|S_i|\le\sum_{j=0}^i|T_j|=O(2^i\sqrt{n})\) for _i_=1_,...,k_, the _i_-th iteration takes time _O_(|_T<sub>i</sub>_|log_n_+|_S<sub>i</sub>_|+|_S<sub>i</sub>_|log_n_)=_O_(|_S<sub>i</sub>_|log_n_)=_O_(2<sup>_i_</sup>\(\sqrt{n}\mathrm{log}n\)), and thus the total running time of Algorithm 1 is \(O(n\mathrm{log}n)+O\left(\left(\sqrt{n}\mathrm{log}n\right)\cdot\sum_{i=1}^k2^i\right)=O(n\mathrm{log}n+2^k\sqrt{n}\mathrm{log}n)=O(n\mathrm{log}n)\), where we used \(2^k<2^{1+\frac{1}{2}\mathrm{log}n}=2\sqrt{n}\). □

We now analyze the maximum and the total dislocation of the returned sequence. We start by upper bounding the maximum dislocation resulting from the batch insertion and, to this aim, we consider a thought experiment involving urns and randomly drawn balls.

Lemma 3.2. _Consider an urn containing N balls,_ \(M\ge\frac{N}{2}\) _of which are white while the others are black. The balls are iteratively drawn from the urn without replacement until the urn is empty. Let_ \(\ell\) _be an integer that satisfies_ \(8\mathrm{log}N\le\ell\le\frac{M}{432}\)_. If_ \(M\ge 64\)_, the probability that there exists some contiguous subsequence of at least_ \(54\ell\) _drawn balls containing_ \(\ell\) _or fewer white balls is at most N_<sup>-6</sup>.

Proof. Let _b<sub>i</sub>_ denote the _i_-th drawn ball. We consider the sequence of drawn balls and we prove an upper bound the probability that, given any position \(i\le\left\lceil\frac{N}{2}\right\rceil\), at most \(\ell\) balls in \(b_i,\dots,b_{i+54\ell-1}\) are white. The same bound immediately holds for sequences stating from any position \(i>\left\lceil\frac{N}{2}\right\rceil\) since we can apply similar arguments by considering the sequence of drawn balls in reverse order. We distinguish two cases.

If \(i\le\frac{M}{4}\) then, for any integer \(0\le j\le\frac{M}{4}\) , the probability that _b_<sub>_i+j_</sub> is white (regardless of the colors of the other balls in _b_<sub>0</sub>_,...,b_<sub>_i+\lfloor M/4\rfloor_</sub>) is at least \(\frac{M-M/2}{N}\ge\frac{M/2}{2M}=\frac{1}{4}>\frac{1}{10}\).

If \(\frac{M}{4}<i\le\left\lceil\frac{N}{2}\right\rceil\), then let _X_ be the number of white balls in {_b_<sub>1</sub>_,...,b_<sub>_i_-1</sub>}. Since _X_ is distributed as a hypergeometric random variable of parameters _N_, _M_, and _i_-1 we have that \(\mathbb{E}[X]=\frac{(i-1)M}{N}\le\frac{M}{2}\) .

By using the tail bound (see, e.g., \[30\]) \(\mathrm{Pr}(X\ge\mathbb{E}[X]+t(i-1))\le e^{-2t^2(i-1)}\) for \(t\ge 0\), we obtain:

\(\mathrm{Pr}\left(X\ge\frac{3M}{4}\right)=\mathrm{Pr}\left(X\ge\frac{M}{2}+\frac{M}{4}\right)\le\mathrm{Pr}\left(X\ge\mathbb{E}[X]+\frac{M}{4(i-1)}\cdot(i-1)\right)\)<br>
\(\le e^{-2\frac{M^2}{16(i-1)^2}(i-1)}=e^{-\frac{M^2}{16(i-1)}}\le e^{-\frac{M}{16}}\le e^{-4}<\frac{1}{50},\)

where we used \(i-1\le\frac{N}{2}\le M\) and \(M\ge 64\).

Consider now the case \(X<\frac{3M}{4}\) , which happens with probability at least \(\frac{49}{50}\). In this case, for any integer \(j\le\frac{M}{8}\) , the probability that _b_<sub>_i+j_</sub> is white, regardless of the specific colors of the other balls in \(b_1,\dots,b_{i+\lfloor\frac{M}{8}\rfloor}\), is at least: \(\frac{M-(\frac{3M}{4}+\frac{M}{8})}{N}\ge\frac{M/8}{2M}=\frac{1}{8}\). Using the union bound on the events \(X\ge\frac{3M}{4}\) and "_b_<sub>_i+j_</sub> is black", we have that _b_<sub>_i+j_</sub> is white with probability at least \(1-\frac{7}{8}-\frac{1}{50}>\frac{1}{10}\).

Therefore, using \(54\ell\le\frac{M}{8}\) , we have that, in both the first case and the second case, the probability that at most \(\ell\) balls in \(b_i,\dots,b_{i+54\ell-1}\) are white is at most:<tbc>

\(\sum_{j=0}^\ell\left(\frac{54\ell}{j}\right)\left(\frac{1}{10}\right)^j\left(\frac{9}{10}\right)^{54\ell-j}\le(\ell+1)\left(\frac{54\ell}{\ell}\right)\left(\frac{9}{10}\right)^{54\ell}\le(\ell+1)\left(\frac{54e\ell}{\ell}\right)^\ell\left(\frac{9}{10}\right)^{54\ell}\)<br>
\(\le(\ell+1)\left(54e\left(\frac{9}{10}\right)^{54}\right)^\ell<\frac{\ell+1}{2^\ell},\)

