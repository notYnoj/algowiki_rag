Following the same reasoning as the other cases, we get:

\(d_{s\rightarrow v_j^N\rightarrow t}\ge\frac{1}{1-\frac{3}{5n}}+\frac{1}{1+\frac{(n+1)(n-3)}{4n^3}-\frac{3}{5n}}\)<br>
\(\ge(1+\frac{3}{5n})+(1-\frac{(n+1)(n-3)}{4n^3}+\frac{3}{5n})=2+2\frac{3}{5n}-\frac{(n+1)(n-3)}{4n^3}\)<br>
\(>2.\)

Therefore, commodity _k_<sub>2</sub> cannot route more than \(1+\delta\) on any of these paths. Since the total load is _n_+2_m_, it must use each path in \(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in I}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in I}\).

## A.3 Proof of Lemma 2.3

_Proof._ Let us consider the delay of arc (_u<sub>i</sub>,t_). Using the inequality \(\frac{1}{1-e}\ge 1+e\) for _e\<_1 (with a strict inequality if \(e\neq 0\) and equality if _e_=0), we get:

\(d_{(u_i,t)}=\frac{1}{c_{(u_i,t)}-y_{(u_i,t)}}=\frac{1}{2-(1+\epsilon_i)}=\frac{1}{1-\epsilon_i}\Longrightarrow d_{(u_i,t)}>1+\epsilon_i\text{if}\epsilon_i\neq 0\text{(i.e., if}i\in Q_I\text{)}d_{(u_i,t)}=1\text{if}\epsilon_i=0\text{(i.e., if}i\in I\backslash\text{)}\)

Using the same inequality on the delay of the arc (_s,u<sub>i</sub>_) we get:

\(d_{(s,u_i)}=\frac{1}{c_{(s,u_i)}-y_{(s,u_i)}}=\frac{1}{mw_i+(m-1)W+2-y_{(s,u_i)}}\ge 1+y_{(s,u_i)}-(mw_i+(m-1)W+1).\)

Because commodity _k_<sub>2</sub> must use the path \(s\rightarrow u_i\rightarrow t\), the total delay of this path is less than or equal to _d_<sub>2</sub>=2. Therefore:

• if \(i\in Q_I\): \(d_2=2\ge d_{(s,u_i)}+d_{(u_i,t)}>1+\epsilon_i+1+y_{(s,u_i)}-(mw_i+(m-1)W+1)\) which implies that:<tbc>

<tbc>\(y_{(s,u_i)}<mw_i+(m-1)W+1-\epsilon_i\forall i\in Q_I.\)<tbc>

• if \(i\in I\backslash Q_I\), we have _d_<sub>(_u<sub>i</sub>,t_)</sub>=1 and therefore \(d_{(s,u_i)}\le 1\), which leads to:<tbc>

<tbc>\(y_{(s,u_i)}\le mw_i+(m-1)W+1\forall i\in I\backslash Q_I.\)<tbc>

