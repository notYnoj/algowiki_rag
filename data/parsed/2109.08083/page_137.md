<tbc>affect these particular parity constraints.) On the other hand, in place of our random greedy cover step, over the two iterations for which we need to consider the parity constraints, it is also possible to simultaneously use a (deterministic) greedy strategy to cover any vertices remaining outside _I_<sub>_t_<sub>0</sub></sub> after removing \(M_H^o\), so whilst an additional step is required to consider parity, we combine it with a greedy cover strategy which is more straightforward than that of Step 3 in Plan 6.34. To obtain _w_<sub>0</sub> from _w<sub>H</sub>_ follows a similar but simpler strategy to that in Plan 6.34. Before proceeding with the details for these steps we make one final note that, due to the nature of wrap-around edges, our management of parity issues is slightly different moving from _H_ to _H_<sub>0</sub> than from _H_<sub>0</sub> to _H_<sub>1</sub> and hence we describe the steps one by one. The reason for the difference will become clear as we detail the strategy.

**6.5.1.** _H_ **to** _H_<sub>0</sub>**.** We assign a weighting _w<sub>H</sub>_ to _H_, which is an almost-perfect fractional matching:

Definition 6.64 (_w<sub>H</sub>_, \((H^o,w_H^o)\)). We set \(w_H(e)=\frac{1}{D}\) for every \(e\in H\), where \((1-\alpha_G)np_\mathrm{gr}^3\le D=\mathrm{max}_{v\in V(H)}d_H(v)\le(1+\alpha_G)np_\mathrm{gr}^3\). Then \(\mathrm{max}_{v\in V(H)}d_{w_H,H}(v)=\mathrm{max}_{v\in V(H)}\sum_{e\unknown v}w_H(e)=1\) and \(d_{w_H,H}(v)\ge\frac{1-\alpha_G}{1+\alpha_G}\ge 1-2\alpha_G\) for every \(v\in V(H)\). We also define \((H^o,w_H^o)\) to be the weighted hypergraph where \(V(H^o):=\{v\in V(H):\exists e\in H,e\cap V(\mathcal{T})\backslash I_{t_0}\neq\emptyset\}\), _E(H<sup>o</sup>_)=_E(H_\[_V(H<sup>o</sup>_)\])\\_E(H_\[_I_<sub>_t_<sub>0</sub></sub>\]), and \(w_H^o=w_H|_{e\in H^o}\).

Proposition 6.65. _Given_ (_H,w<sub>H</sub>_) _and_ \((H^o,w_H^o)\) _as above we have that:_

(_i)_ \(w_H(E_H(v,I_{t_0}))\ge\frac{1}{3}-O(\alpha_G)\) _for every_ \(v\in V(H)\),<tbc>

(_ii)_ \(d_{w_H^o}(v)=1\pm 2\alpha_G\) _for every_ \(v\in V(H)\backslash V(H[I_{t_0}])\),<tbc>

_(iii)_ \(d_{w_H,H}(v)=d_{w_H^o}(v)+w_H(E_H(v,I_{t_0}))=1\pm 2\alpha_G\) _for every_ \(v\in V(H[I_{t_0}])\),<tbc>

_(iv)_ \(1-d_{w_H^o}(v)=(1\pm 6.1\alpha_G)w_H(E_H(v,I_{t_0}))\) _for every_ \(v\in V(H[I_{t_0}])\)

Proof. By Fact 3.30(i) we have that \(|E_\mathcal{T}(v,I_{t_0})|\ge\frac{n}{3}-2\) for all \(v\in V(\mathcal{T})\), where _n_=2_t_<sub>0</sub>+1. Thus by Theorem 3.28(ii), and the definition of _w<sub>H</sub>_, (i) follows. It is straightforward to see that (ii) and (iii) follow from the fact that \(1-2\alpha_G\le d_{w_H,H}(v)\le 1\) combined with the definitions. We deduce (iv) from (iii) and (i). For \(v\in V(H[I_{t_0}])\),

\(1-d_{w_H^o}(v)=w_H(E_H(v,I_{t_0}))\pm 2\alpha_G\)<br>
\(=w_H(E_H(v,I_{t_0}))\left(1\pm\frac{2\alpha_G}{1/3-O(\alpha_G)}\right)=(1\pm 6.1\alpha_G)w_H(E_H(v,I_{t_0})).\)

□

We start the process by running Theorem 6.2 on \((H^o,w_H^o)\), to obtain \(M_H^o\).

Proposition 6.66. _There exists a matching_ \(M_H^o\) _in_ \((H^o,w_H^o)\) _such that letting_ \(H^c:=H[V(H)\backslash V(M_H^o)]\)_, we have that_

(_i)_ _every_ T _-valid subset_ \(S\subseteq I_{t_0}\) _satisfies_<tbc>

<tbc>\(|V(H^c[S])|=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V(H[S])}(1-d_{w_H^o}(v)),\)<tbc>

<tbc>_and for any vertex allowable function_ \(p_S(v):V(H)\rightarrow\mathbb{R}_{\ge 0}\) _for_ \((H,w_H,t_0,\eta)\) _such that_ \(p_S(v)=f_S(v)\unknown_{v\in V(H[S])}\),<tbc>

<tbc>\(\sum_{v\in V(H^c[S])}p_S(v)=(1\pm O(t_0^{-\epsilon}))\sum_{v\in V(H[S])}p_S(v)(1-d_{w_H^o}(v)),\)

