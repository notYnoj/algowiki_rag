Since \(g=(i,i+2^{k_\ell})\) is central, we have that

\(3n/8-O(\sqrt{n})\le x_\mathrm{min}\le x_\mathrm{max}\le 5n/8+O(\sqrt{n}),\) (7)

and so both _x_<sub>min</sub> and _x_<sub>max</sub> are \(\Theta(n)\).

Observe that moving precisely \(2^{k_\ell}\) elements from _A_ to _B_ (or from _B_ to _A_) that are smaller than _x_<sub>min</sub> and moving \(2^{k_\ell}\) elements larger than _x_<sub>max</sub> back results in flipping the sets \(\mathcal{E}\cap[x_\mathrm{min},x_\mathrm{max}]\) and \(\mathcal{O}\cap[x_\mathrm{min},x_\mathrm{max}]\).<sup>33</sup> In particular such a change would swap the values of \(o_t(\ell-1)\) and \(e_{t+1}(\ell-1)\), as the even and the odd sets swapped their values in this interval and the moved elements made the number of elements smaller than _x_<sub>min</sub> now in E one more than the number of elements smaller than _x_<sub>min</sub> previously in O.<sup>34</sup> This swap would have the effect of replacing input (_x_<sub>1</sub>_,x_<sub>2</sub>) with (_x_<sub>2</sub>_,x_<sub>1</sub>) and vice versa.

Let \(\mathcal{A}_I^s\) be the (possibly empty) subset of equipartitions _A_ where \(I=[x_\mathrm{min},x_\mathrm{max}]\cap A\) and \(s=|[0,x_\mathrm{min})\cap A|\). Importantly, all equipartitions in \(\mathcal{A}_I^s\) result in _g_ receiving the same input. Then we can precisely characterize the size of these sets by:

\(|\mathcal{A}_I^s|=HG_{n/2-|I|}^{(n-x_\mathrm{max}+x_\mathrm{min}-1),x_\mathrm{min}\left[s\right]}\cdot\left(\begin{array}{ c }
n-x_\mathrm{max}+x_\mathrm{min}-1 \\
n/2-|I|
\end{array}\right)=\left(\begin{array}{ c }
x_\mathrm{min} \\
s
\end{array}\right)\left(\begin{array}{ c }
n-x_\mathrm{max}-1 \\
n/2-|I|-s
\end{array}\right).\) (8)

To see why the hypergeometric distribution applies, note that |_I_| elements of _A_ are already fixed, leaving _n/_2-|_I_| elements of _A_ that can be chosen from the set \[0_,n_-1\]-\[_x_<sub>min</sub>_,x_<sub>max</sub>\], which has size _n-x_<sub>max</sub>+_x_<sub>min</sub>-1. Mark the _x_<sub>min</sub> elements in the range \[0_,x_<sub>min</sub>-1\]; from these, _s_ must be chosen. The remaining _n/_2-|_I_|-_s_ items are chosen from the unmarked elements in the set \[_x_<sub>max</sub>+1_,n_-1\] which has size _n-x_<sub>max</sub>-1.

From Definition 5.10, the mean of this distribution is<tbc>

\(\frac{x_\mathrm{min}(n/2-|I|)}{n-(x_\mathrm{max}-x_\mathrm{min}+1)}.\)

<tbc>Since \(|I|\le x_\mathrm{max}-x_\mathrm{min}+1\le 2^{k_\ell+1}\le 2\sqrt{n}\), and since \(x_\mathrm{min}=\Theta(n)\), the mean and modes (which differ from the mean by at most 1) are \(x_\mathrm{min}/2\pm O(\sqrt{n})\). We denote the larger mode of this distribution by _s_<sup>∗</sup>, and so we have

\(s^*=x_\mathrm{min}/2\pm O(\sqrt{n})\) (9)

For any _s_ and _I_ where _g_ receives the input pair (_x_<sub>1</sub>_,x_<sub>2</sub>) we know that both \(\mathcal{A}_I^{s+2^{k_\ell}}\) and \(\mathcal{A}_I^{s-2^{k_\ell}}\) results in _g_ receiving the input pair (_x_<sub>2</sub>_,x_<sub>1</sub>). We will want to show that there is some constant \(\alpha>1\) such that for every choice of _s_ and _I_,

\(\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|+\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|\ge\left|\mathcal{A}_I^s\right|(2/\alpha).\) (10)

Since the hyper-geometric distribution is unimodal, i.e., strictly non-decreasing to _s_<sup>∗</sup>, the larger mode, and then strictly non-increasing after that point, for any \(s\le s^*-2^{k_\ell}\) we immediately have that \(\left|\mathcal{A}_I^s\right|\le\left|\mathcal{A}_I^{s+2^{k_\ell}}\right|\). Likewise for any \(s\ge s^*+2^{k_\ell}\) we immediately have that \(\left|\mathcal{A}_I^s\right|\le\left|\mathcal{A}_I^{s-2^{k_\ell}}\right|\).

<sup>33</sup>When shifting small elements from _B_ to _A_, each old _a<sub>j</sub>_ with a value in this interval becomes \(a_{j+2^{k_\ell}}\) and each old _b<sub>j</sub>_ with a value in this interval becomes \(b_{j-2^{k_\ell}}\). <sup>34</sup>As an illustrative example of this, consider \(\ell=0\) so E and O are just the even and odd indices respectively of _A_ and _B_ when sorted. Fix _A_={0,1,2,3} and _B_={4,5,6,7}. Then E={0,2,4,6} and O={1,3,5,7}. If we swap values 0 and 7 between _A_ and _B_, then we get \(A'=\{1,2,3,7\},B'=\{0,4,5,6\}\) and \(\mathcal{E}'=\{0,1,3,5\},\mathcal{O}'=\{2,4,6,7\}\). We have that \(e'_{t+1}=o_t\) and \(o'_t=e_{t+1}\) for \(t\in\{0,1,2\}\).

