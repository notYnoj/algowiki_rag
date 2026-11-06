Recall that we picked _p_<sub>1</sub>=1 and \(p_{\ell+1}=p_\ell|A|/s\), and thus<tbc>

\(p_{k+1}=\frac{|A|^k}{s^k}.\)

<tbc>Moreover, we picked _Y_<sub>1</sub>=_X_ and \(Y_2,\dots,Y_{k+1}\subseteq\pm A\). In combination, we get<tbc>

\(\mathrm{Pop}\left(X,X,\underbrace{\pm A,\dots,\pm A}_{k\mathrm{times}};\frac{|A|^k}{s^k}\right)\neq\emptyset.\)

<tbc>By two applications of Observation 3.2 it further follows that<tbc>

\(\mathrm{Pop}^k\left(\pm A;\frac{|A|^k}{|X|^2s^k}\right)\neq\emptyset.\)

<tbc>But note that<tbc>

\(\frac{|A|^k}{|X|^2s^k}\ge\frac{|A|^k}{n^{2-2\rho}|A|^\epsilon}\ge\frac{|A|^k}{|A|^{2-2\rho+2\epsilon}|A|^\epsilon}=|A|^{k-2+2\rho-3\epsilon}=|A|^{k-1-c}=p,\)

<tbc>where we used that \(|X|\le n^{1-\rho}\) and that \(n\le|A|^{1+\epsilon}\) as asserted in step 2. Hence,

\(\mathrm{Pop}^k(\pm A;p)\neq\emptyset,\)

which contradicts step 1.

### Running Time.

The running time of step 1 is dominated by the calls to Theorem 3.5, running in time \(\widetilde{O}(|A|^{1+c+\epsilon})=\widetilde{O}(|A|^{2-2\rho+4\epsilon})\) for each call, and in total \(\widetilde{O}(|A|^{2-2\rho+5\epsilon})\) over all \(\widetilde{O}(|A|^\epsilon)\) calls. Step 2 runs in time \(O(n^{2-\delta_0})\) for some constant \(\delta_0=\delta_0(\epsilon)>0\). Finally, focus on step 3. For \(1\le\ell\le k\), the \(\ell\)-th iteration is dominated by the call to Lemma 4.7. In the odd case, this takes time

\(\widetilde{O}\left(\frac{s|X||Y_1|\dots|Y_\ell|}{p_\ell}+|A||X|+\frac{|B||Y_1|\dots|Y_\ell|}{p_\ell}+\frac{|A||B|}{s}\right)\)<br>
\(=\widetilde{O}\left(\frac{s^\ell|X|^2|A|^{\ell-1}}{|A|^{\ell-1}}+|A||X|+\frac{s^{\ell-1}|B||X||A|^{\ell-1}}{|A|^{\ell-1}}+\frac{|A||B|}{s}\right)\)<br>
\(=\widetilde{O}\left(n^{2-2\rho+\epsilon\ell/k}+n^{2-\rho}+n^{2-\rho+\epsilon(\ell-1)/k}+n^{2-\epsilon/k}\right),\)

and the running time of the even case can be bounded analogously. Note that the fourth term can be bounded by \(O(n^{2-\delta_1})\) for some constant \(\delta_1=\delta_1(\rho,\epsilon)>0\). This leaves the first three terms, and the time complexity of step 1, which are crudely bounded by \(\widetilde{O}(n^{2-\rho+5\epsilon})\). If necessary, decrease \(\epsilon\) further so that \(\epsilon<\rho/10\). Then let \(\delta=\mathrm{min}(\delta_0,\delta_1,\rho/2)\), and the proof is complete.

## 4.2 Low-Doubling Containment for All Sets

Next, we demonstrate that low-doubling containment for one set can be extended to low-doubling containment for all three sets:

