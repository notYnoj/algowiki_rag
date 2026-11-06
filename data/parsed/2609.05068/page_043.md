## A.4 Proof of Lemma 2.4

_Proof._ The reasoning is identical to the proof of Lemma 2.3. We apply the inequality \(\frac{1}{1-\epsilon}\ge 1+e\) (valid for _e\<_1, with a strict inequality when \(e\neq 0\) and equality for _e_=0) to the delays of the arcs forming the 2-hop paths.

Consider the path \(s\rightarrow v_j\rightarrow t\). The delay of the first arc is \(d_{(s,v_j)}=\frac{1}{c_{(s,v_j)}-y_{(s,v_j)}}=\frac{1}{2-(1+\epsilon_j)}\). This gives \(d_{(s,v_j)}>1+\epsilon_j\) if \(j\in Q_J\), and _d_<sub>(_s,v<sub>j</sub>_)</sub>=1 otherwise. For the second arc, applying the same inequality gives:

\(d_{(v_j,t)}=\frac{1}{c_{(v_j,t)}-y_{(v_j,t)}}=\frac{1}{\frac{W}{m}+2-y_{(v_j,t)}}\ge 1+y_{(v_j,t)}-\left(\frac{W}{m}+1\right).\)

Because commodity _k_<sub>2</sub> must respect the maximum delay constraint \(d_2=2\ge d_{(s,v_j)}+d_{(v_j,t)}\) on this path, we get:

• For \(j\in Q_J\), the strict inequality on the first arc implies \(2>1+\epsilon_j+1+y_{(v_j,t)}-\left(\frac{W}{m}+1\right)\), which leads to \(y_{(v_j,t)}<\frac{W}{m}+1-\epsilon_j\).<tbc>

• For \(j\in J\backslash Q_J\), the equality on the first arc implies \(2\ge 1+1+y_{(v_j,t)}-\left(\frac{W}{m}+1\right)\), leading to \(y_{(v_j,t)}\le\frac{W}{m}+1\).

The same reasoning applies to the path \(s\rightarrow v_j^N\rightarrow t\). The delay of the first arc \(d_{(s,v_j^N)}=\frac{1}{c_{(s,v_j^N)}-y_{(s,v_j^N)}}=\frac{1}{2-(1+\epsilon'_j)}\) is strictly greater than \(1+\epsilon'_j\) for \(j\in Q'_J\) and equals 1 if \(j\in J\backslash Q'_J\). The delay of the second arc satisfies:

\(d_{(v_j^N,t)}=\frac{1}{c_{(v_j^N,t)}-y_{(v_j^N,t)}}=\frac{1}{W\frac{(n+1)(n-3)}{n}+2-y_{(v_j^N,t)}}\ge 1+y_{(v_j^N,t)}-\left(W\frac{(n+1)(n-3)}{n}+1\right).\)

Enforcing the maximum delay of 2 across the entire path guarantees that \(y_{(v_j^N,t)}<W\frac{(n+1)(n-3)}{n}+1-\epsilon'_j\) for any \(j\in Q'_J\), and less than or equal to \(W\frac{(n+1)(n-3)}{n}+1\) otherwise.

