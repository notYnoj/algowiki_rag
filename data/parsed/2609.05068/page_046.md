Summing over all _m_ arcs confirms that the total volume routed matches the demand _b<sub>L</sub>=W_.

## A.8 Proof of Lemma 2.8

_Proof._ Equation (9) establishes that the total load on each arc \((v_j^N,t)\) is \(W\frac{(n+1)(n-3)}{n}+1\). Knowing that 1 unit of flow is already routed by commodity _k_<sub>2</sub> on each arc \((v_j^N,t)\), the remaining flow on these arcs must belong to commodity _k<sub>H</sub>_. Thus, the load of _k<sub>H</sub>_ on each arc \((v_j^N,t)\) is \(W\frac{(n+1)(n-3)}{n}\) .

By the conservation of flow, because commodity _k<sub>H</sub>_ only enters _t_ through these arcs and must cross the entire arc chain to reach them, this result extends to all arcs in the chain: the entry arcs \(\{(v_j,v_j^1)\}_{j\in J}\), the internal arcs \(\{(v_j^l,v_j^{l+1})\}_{j\in J,l\in[1,N-1]}\), and the exit arcs \(\{(v_j^N,t)\}_{j\in J}\). Finally, substituting these loads back into the delay functions confirms that the delay on each of these arcs is exactly 1.

## A.9 Proof of Lemma 2.9

_Proof._ From Lemma 2.1, commodity _k_<sub>2</sub> never crosses the arcs (_u<sub>i</sub>,v<sub>j</sub>_). These arcs are therefore exclusively used by commodities _k<sub>L</sub>_ and _k<sub>H</sub>_. From Lemma 2.5, we know that the delays of the entry and exit arcs are _d_<sub>(_s,u<sub>i</sub>_)</sub>=1 and _d_<sub>(_v<sub>j</sub>,t_)</sub>=1.

Lemma 2.8 establishes that the total delay of the sub-path \(v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\) used by commodity _k<sub>H</sub>_ is _N_+1. Because the maximum delay limit for commodity _k<sub>H</sub>_ is \(d_H=N+2+\frac{1}{W}\), any arc (_u<sub>i</sub>,v<sub>j</sub>_) traversed by _k<sub>H</sub>_ must satisfy:

\(d_{(s,u_i)}+d_{(u_i,v_j)}+(N+1)\le d_H\Longrightarrow 1+d_{(u_i,v_j)}+N+1\le N+2+\frac{1}{W}\Longrightarrow d_{(u_i,v_j)}\le\frac{1}{W}.\)

Since \(d_{(u_i,v_j)}=\frac{1}{c_{(u_i,v_j)}-y_{(u_i,v_j)}}=\frac{1}{w_i+2W-y_{(u_i,v_j)}}\), this delay constraint imposes the upper bound on the load \(y_{(u_i,v_j)}\le w_i+W\) for any arc (_u<sub>i</sub>,v<sub>j</sub>_) traversed by _k<sub>H</sub>_.

