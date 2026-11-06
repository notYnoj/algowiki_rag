<tbc>1)<sup>3</sup>-_p(i_)<sup>3</sup>)+_e<sub>d</sub>(i_+1)-_e<sub>d</sub>(i_), so that applying Taylor’s theorem, we have that \(\mathbb{E}'(\Delta d_v^-(i))\approx\mathbb{E}'(\Delta d_v(i))-\frac{12np^2}{|V(0)|}+\frac{e'_d}{|V(0)|}\). We give the full details below.

Dealing first with our primary variables, we could take the calculations for the supermartingales directly from Bennett and Bohman \[6\]. The submartingale details are not given since they are very similar. For completeness we show the submartingale conditions from scratch but emphasise that this is essentially repeating the details from \[6\] with different values for _e<sub>d</sub>_ and _e<sub>q</sub>_. Before proceeding, recall that _b=O(p<sub>A</sub>_)=_O(n_<sup>-10<sup>-7</sup></sup>) and

(5.1) \(1\ge p=\Omega(n^{-10^{-25}})\)

in the range for which we are interested in _p_.

Starting with \(d_v^-(i)\), we have that

\(\mathbb{E}'(\Delta d_v(i))=-\frac{1}{Q(i)}\sum_{e\in E_{T_i}(v,\mathcal{T})}\sum_{u\in e\backslash\{v\}}d_u(i)\pm O\left(\frac{d_v}{Q(i)}\right)\)<br>
\(\ge-\frac{3(np^3-e_d+b^{2/3}n)(np^3+e_d)}{Q(i)}.\)

Note that this does not take into account the contribution to the expected change that comes from the selection of an edge that itself contains _v_. Since we are not interested in the random variable once _v_ has left _V(i_) we may instead use the convention that whenever \(v\notin V(i+1)\) we take _d<sub>v</sub>(i_+1)=_d<sub>v</sub>(i_). This convention will follow through to the calculations for all random variables we are tracking. Then

\(\mathbb{E}'(\Delta d_v^-(i))\ge-\frac{3(np^3-e_d+b^{2/3}n)(np^3+e_d)}{Q(i)}+\frac{12np^2}{|V(0)|}+\frac{e'_d}{|V(0)|}\)<br>
\(+O\left(\frac{d_v}{Q}+\frac{np}{|V(0)|^2}+\frac{e''_d}{|V(0)|^2}\right)\)

Expanding, cancelling and regrouping terms we get that

\(\mathbb{E}'(\Delta d_v^-(i))\ge-\frac{12b^{2/3}n}{|V(0)|p}+\frac{e'_d}{|V(0)|}\)<br>
\(+O\left(\frac{(e_d-b^{2/3}n)e_d}{|V(0)|np^4}+\frac{e_q}{|V(0)|^2p^2}+\frac{d_v(i)}{Q(i)}+\frac{np}{|V(0)|^2}+\frac{e''_d}{|V(0)|^2}\right).\)

Noting that \(|V(0)|=\Theta(n)\) and \(Q(i)=\Theta(n^2p^4)\), we have that the terms carried in the ‘big-O’ are given by \(O\left(\frac{b^{4/3}(1-\mathrm{log}^2(p))}{p^4}+\frac{b(1-\mathrm{log}(p))}{p^2}+\frac{1}{np}+\frac{p}{n}+\frac{b^{2/3}}{np^2}\right)\). Then since \(\frac{e'_d}{|V(0)|}=\Theta\left(\frac{b^{2/3}}{p}\right)\) and \(p^3\gg b^{2/3}\mathrm{log}^2(n)\) by (5.1), we have that the ‘big-O’ terms are \(o\left(\frac{e'_d}{|V(0)|}\right)\). Furthermore, since \(e'_d=\frac{32b^{2/3}n}{p}\) , we have that

\(-\frac{12b^{2/3}n}{|V(0)|p}+\frac{e'_d}{|V(0)|}=\frac{20b^{2/3}n}{|V(0)|p},\)

so that \(-\frac{12b^{2/3}n}{|V(0)|p}+\frac{e'_d}{|V(0)|}=\Theta\left(\frac{e'_d}{|V(0)|}\right)\), and \(-\frac{12b^{2/3}n}{|V(0)|p}+\frac{e'_d}{|V(0)|}\ge 0\), which proves the trend hypothesis for \(d_v^-(i)\).

