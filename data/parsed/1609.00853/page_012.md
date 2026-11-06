<tbc>generating function has many cancellable factors. This, too, is not predicted by Ehrhart theory; but as it is too systematic and elegant to be accidental, it presents another tantalizing question. Kotˇcešovec’s evidence, indeed, suggests that _u_<sub>Q</sub>(_q;n_) has a recurrence relation of length far less than its period (see Section 8.3). A proof of these conjectures seems to call for a new theoretical leap forward.

### 5.2. The semiqueen.

The _semiqueen_ Q<sup>21</sup> is the queen without one of its diagonal moves (think of it as having lost the left or right arm in battle). We gave formulas for _q_=2 and 3 in s III.4.1 and III.4.2. We also gave formulas for the initial coefficients \(\gamma_2\) and \(\gamma_3\) in s III.3.1 and III.3.2. For higher values of _q_ we refer to Kotˇcešovec’s heuristic counting formulas for \(q\le 6\) in \[12, 6th ed., pp. 732-733\].

Conjecture IV.5.8 states a conjectural upper bound for the quasipolynomial period of lcm\[_F_<sub>_q/_2</sub>\] when _q_ is even and lcm\[_F_<sub>(_q_+1)/2</sub>-1\] when _q_ is odd. Since we do not expect all denominators in \[_F_<sub>_q/_2</sub>\] or \[_F_<sub>(_q_+1)/2</sub>-1\] to appear, we do not expect this bound to be tight for large _q_, although it agrees with Kotˇcešovec’s formulas for \(q\le 6\).

### 5.3. The trident.

The _trident_ is the partial queen Q<sup>12</sup> that can advance and retreat but cannot move sideways. Our counting formulas for \(q\le 3\) in s III.4.1 and III.4.2 are the same as Kotˇcešovec’s heuristic ones \[12, pp. 730-731\], thereby confirming his. s III.3.1 and III.3.2 give the values of \(\gamma_2\) and \(\gamma_3\).

Conjecture IV.5.10 implies a conjectural upper bound for the period of the counting quasipolynomial for _q_ tridents of lcm\[2_F_<sub>_q/_2</sub>-1\] when _q_ is even and lcm\[_F_<sub>(_q_+3)/2</sub>-1\] when _q_ is odd. Again, this should not be considered tight. However, Kotˇcešovec’s heuristic approach did yield a period of 6 when _q_=4, which is our upper bound.

### 5.4. The anassa.

The _anassa_ (Kotˇcešovec’s "semi-rook + semi-bishop") is the partial queen Q<sup>11</sup>, with one horizontal or vertical and one diagonal move. It is the fourth and final piece known to have period 1, i.e., whose counting function _u_<sub>Q<sup>11</sup></sub>(_q;n_) is a polynomial for all _q_.

Kotˇcešovec noticed in his results that (_n)<sub>q</sub>_ is a factor of _u_<sub>Q<sup>11</sup></sub>(_q;n_) for _q_ up to 8. For instance,

\(u_{\mathbb{Q}^{11}}(6;n)=\frac{(n)_6}{6!}\big(n^6-10n^5+45n^4-\frac{1093}{9}n^3+\frac{634}{3}n^2-\frac{14033}{63}n+\frac{2278}{21}\big).\)

We would like an explanation for this.

Kotˇcešovec also presents a formula for the number of ways to place _n_ nonattacking anassas on an \(n\times n\) board:

\(u_{\mathbb{Q}^{11}}(n;n)=\sum_{k=1}^n\genfrac(){pt}{2}{n+1}{k}\frac{k!}{2^k}S(n,k).\)

## 6. Preparation for the Nightrider

