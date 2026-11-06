1. For every \(v\in V\) , set \(Q^0(v)\leftarrow[k]\); set \(P^0\leftarrow Q^0\) and \(F_0\leftarrow\varnothing\).<tbc>

2. **for** _t_=1,2_,...,T_ **do**<tbc>

3. If some \(v\in A\) has \(Q^{t-1}(v)=\varnothing\), or \(A\backslash F_{t-1}=\varnothing\), stop.<tbc>

4. Choose \(f_t\in A\backslash F_{t-1}\) maximizing _m_<sub>_Q_<sup>_t_-1</sup></sub>(_v_), breaking ties by the fixed order; set \(D_t\leftarrow m_{Q^{t-1}}(f_t)\).<tbc>

5. Form the cap palette _P<sup>t</sup>_ from _Q_<sup>_t_-1</sup> according to the rule below.<tbc>

6. If \(i_t\notin P^t(f_t)\), stop.<tbc>

7. Set \(F_t\leftarrow F_{t-1}\cup\{f_t\}\) and initially set \(Q^t(w)\leftarrow P^t(w)\) for every \(w\in V\) .<tbc>

8. Set \(Q^t(f_t)\leftarrow\{i_t\}\); for every \(u\in N_G(f_t)\), set \(Q^t(u)\leftarrow P^t(u)\backslash\{i_t\}\).<tbc>

9. **end for**<tbc>

10. **return** the generated pivots, thresholds, cap palettes, and palette systems.

<tbc>The cap update in step 5 is

\(P^t(w)=\left\{\begin{array}{ c c }
\varnothing, & Q^{t-1}(w)\neq\varnothing\text{and}m_{Q^{t-1}}(w)>D_t, \\
Q^{t-1}(w), & \text{otherwise.}
\end{array}\right.\)

In particular,

\(U(P^t)=\{w:Q^{t-1}(w)\neq\varnothing\text{and}m_{Q^{t-1}}(w)\le D_t\}.\) (6)

In step 5, all degrees and the threshold are computed from the palette system _Q_<sup>_t_-1</sup> before any cap or neighbor update.

## 6 Analysis of the trial coloring process

### 6.1 Process invariants

**Lemma 6.1.** _For every completed run:_

1. \(P^0\supseteq P^1\supseteq\cdots\) _, and every_ \(v\in U(P^t)\) _has a color_ \(i\in P^t(v)\) _with_ \(d_i^{P^t}(v)\le D_t\)_; moreover_ \(0\le D_t\le n\).<tbc>

_2._ _On every run completing T rounds,_<tbc>

\(\sum_{t=1}^TD_t\le kn.\) \(\text{(7)}\)

_3. If G_\[_A_\] _has a proper coloring_ \(\varphi:A\rightarrow[k]\)_, then, whenever round t is reached, the prescribed choice_ \(i_t=\varphi(f_t)\) _is legal. If_ \(|A|\ge T\)_, it completes T rounds and preserves_ \(\varphi(v)\) _in the palette of every_ \(v\in A\) _throughout; in particular_ \(A\subseteq U(P^t)\) _for all_ \(t\le T\).<tbc>

<tbc>_Proof._ For the first assertion, caps only empty entire palettes and never add labels. If \(v\in U(P^t)\), then \(m_{Q^{t-1}}(v)\le D_t\) by (6). Choose \(i^*\in Q^{t-1}(v)\) attaining this minimum. Since _v_ was not emptied, _P<sup>t</sup>(v_)=_Q_<sup>_t_-1</sup>(_v_), and hence

\(d_{i^*}^{P^t}(v)\le d_{i^*}^{Q^{t-1}}(v)=m_{Q^{t-1}}(v)\le D_t.\)

The bounds on _D<sub>t</sub>_ are immediate from its definition and \(|N_G(f_t)|\le n-1\).

For the second assertion, since \(i_t\in Q^{t-1}(f_t)\),<tbc>

\(d_{i_t}^{Q^{t-1}}(f_t)\ge D_t.\)

