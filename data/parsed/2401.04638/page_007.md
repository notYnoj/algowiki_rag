<tbc>derstanding restricted cases, such as, demands of single source (resp., destination), and single commodity, uniform capacities, and their combinations. We will first show approximation lower bounds and NP-hardness for uniform capacities in §IV-A, and then introduce some tractable restricted cases in \(\mathsection\)IV-B.

## A. Approximation Lower Bounds for Non-Segregated Routing

By Theorem 6, we show that the MCRN problem under non- segregated routing has an approximation lower bound \(\Omega\left(\frac{c_\mathrm{max}}{c_\mathrm{min}}\right)\) for both splittable and unsplittable flow, which is pessimistic since the value of \(\frac{c_\mathrm{max}}{c_\mathrm{min}}\) can be arbitrarily large. We remark that the lower bounds \(\Omega\left(\frac{c_\mathrm{max}}{c_\mathrm{min}}\right)\) still holds if each link has the same capacity on both directions, which can be derived by adapting the given proof.

**Theorem 6.** _When_ \(\tau\in\{SN,UN\}\)_, given demands D of a single source (resp., destination), the MCRN problem cannot be approximated better than_ \(\Omega\left(\frac{c_\mathrm{max}}{c_\mathrm{min}}\right)\) _unless P=NP._

_Proof:_ We give a proof for demands of a single destination, and the case of a single source can be shown symmetrically. We give a gap-producing reduction from a decision problem of vertex cover \(\Pi\) on 3-regular graphs to the MCRN problem \(\Pi'\). For an instance _I_=(_G<sub>U</sub>_=(_U,E<sub>U</sub>),k_) of \(\Pi\), where |_U_|=_n_, we will construct an instance \(I'\) of \(\Pi'\), illustrated in Fig. 2.

Let the constructed instance be \(I'=(G,\mathcal{E},c,D)\), where _G_=(_V,E_) is the static network, a set of reconfigurable links E, a capacity function \(c:\vec{E}\cup\vec{\mathcal{E}}\mapsto\{1,\epsilon\}\), s.t., _c_<sub>max</sub>=1 and \(c_\mathrm{min}=\epsilon\) (\(0<\epsilon\checkmark 1\)), and a demand matrix _D_.

The set of nodes _V_ in \(I'\) are constructed as follows:

\(\bullet\) For each vertex \(u_i\in U\) of _I_, where \(i\in\{1,\dots,n\}\), we construct a node \(v_i\in V_1\);<tbc>

\(\bullet\) For each \(i\in\{1,\dots,k\}\), we have a node \(a_i\in A\) ;<tbc>

\(\bullet\) For each edge \(\{u_i,u_j\}\in E_U\), we construct a node: \(v_{i,j}\in V_2\);<tbc>

\(\bullet\) Moreover, we have additional one node _t_, and let<tbc>

<tbc>\(V=A\cup V_1\cup V_2\cup\{t\}.\)<tbc>

<tbc>Static (bidirected) links _E_ and their capacities \(c:\vec{E}\mapsto\{1,\epsilon\}\) are constructed as follows:

\(\bullet\) For each edge \(\{u_i,u_j\}\in E_U\) of _I_, where \(i,j\in\{1,\dots,n\}\) and \(i\neq j\), we construct two static (bidirected)<tbc>

<tbc>links: \(\{v_i,v_{i,j}\}\in E_1\) and \(\{v_{i,j},v_j\}\in E_1\) with the capacities defined as:<tbc>

\(c\left((v_i,v_{i,j})\right)=\epsilon,c\left((v_j,v_{i,j})\right)=\epsilon,\)<br>
\(c\left((v_{i,j},v_i)\right)=1,\text{and}c\left((v_{i,j},v_j)\right)=1.\)

\(\bullet\) For each \(i\in\{1,\dots,k\}\), we have a static (bidirected) link \(\{a_i,t\}\in E_t\), s.t., _c_((_a<sub>i</sub>,t_))=1 and \(c\left((t,a_i)\right)=\epsilon\).<tbc>

\(\bullet\) Since the static network (_V,E_) is a connected graph, we construct a static link _e_<sup>∗</sup> connecting a node in _V_<sub>1</sub> to another node in _A_, e.g., _e_<sup>∗</sup>={_v_<sub>2</sub>_,a<sub>k</sub>_} in Fig. 2.<tbc>

\(\bullet\) Finally, let \(E=E_1\cup E_t\cup\{e^*\}\), where every static link has a capacity \(\epsilon\) on both directions unless otherwise specified.

For any two nodes in _V_ , there is a reconfigurable (bidirected) link in E. For each \(i\in\{1,\dots,n\}\) and \(j\in\{i,\dots,k\}\), there is one reconfigurable links \(\{v_i,a_j\}\in\mathcal{E}\) with capacities _c_((_v<sub>i</sub>,a<sub>j</sub>_))=1 and \(c\left((a_j,v_i)\right)=\epsilon\). For other reconfigurable links, they have a capacity \(\epsilon\) on both directions.

We complete the construction by giving demands _D_ as follows: for each edge \(\{u_i,u_j\}\in E_U\) of _I_, we have a node \(v_{i,j}\in V\) with a demand _D(v<sub>i,j</sub>,t_)=1/3.

Next, we show that, when \(\tau\in\{\mathrm{SN},\mathrm{UN}\}\), if _I_ has a vertex cover of size \(\le k\), then the minimized congestion \(\lambda\) of \(I'\) is at most 1; and if _I_ has a vertex cover of size _\>k_, then the minimized congestion \(\lambda\) of \(I'\) has \(\lambda\ge\frac{1}{12\epsilon}\) for \(\tau=\mathrm{SN}\) (resp., \(\lambda\ge\frac{1}{3\epsilon}\) for \(\tau=\mathrm{UN}\)).

Clearly, we need to find _k_ nodes in _V_<sub>1</sub> to connect _k_ nodes in _A_ by reconfigurable links (matching) _M_, s.t., each demand can be sent to _t_ without going through any directed link of the capacity \(\epsilon\).

First, if _G<sub>U</sub>_ has a vertex cover \(U'\subseteq U\) of size _k_, then for each \(u_i\in U'\), we add the corresponding reconfigurable link \(\{v_i,a_i\}\in\mathcal{E}\) into _M_. By this reconfiguration _M_, each node _v<sub>i,j</sub>_ can find a directed path to _t_, s.t., each directed link in this path has the capacity one, then \(\lambda\le 1\).

On the other hand, if _G<sub>U</sub>_ does not have a vertex cover of size \(\le k\), then for any _k_ vertices \(U'\subseteq U\), there exists an edge \(\{u_i,u_j\}\in E_U\), s.t., \(u_i\notin U'\) and \(u_j\notin U'\). Thus, the demand _D(v<sub>i,j</sub>,t_) cannot be sent on reconfigurable links incident on either _v<sub>i</sub>_ or _v<sub>j</sub>_. It has to find another node \(v_f\in V_1\), which has a reconfigurable link {_v<sub>f</sub>,a<sub>l</sub>_} included in a directed path (_v<sub>f</sub>,a<sub>l</sub>,t_), where \(a_l\in A\). W.L.O.G., we assume \(\{u_f,u_i\}\in E_U\). Then, any directed path from \(v_{i,j}\in V_1\) to \(v_f\in V_1\) must visit the directed link (_v<sub>i</sub>,v<sub>i,f</sub>_) that has the capacity \(\epsilon\). Thus, when \(\tau=\mathrm{SN}\) (resp., \(\tau=\mathrm{UN}\)), it implies \(\lambda\ge\frac{1}{12\epsilon}\) (resp., \(\lambda\ge\frac{1}{3\epsilon}\)), where _c_<sub>max</sub>=1 and \(c_\mathrm{max}=\epsilon\).

Therefore, the \(I'\) cannot be approximated within a ratio \(\frac{1}{12\epsilon}\), i.e., \(\Omega\left(\frac{c_\mathrm{max}}{c_\mathrm{min}}\right)\), unless _P=NP_. \(\blacksquare\)

After knowing the approximation lower bound \(\Omega\left(\frac{c_\mathrm{max}}{c_\mathrm{min}}\right)\) in Theorem 6, an immediate question is if the problem is tractable when _c_<sub>max</sub>=_c_<sub>min</sub>. Next, we will negate this conjecture by showing the NP-hardness for splittable (resp., unsplittable) and segregated routing even if it has a single source (resp., dest.) and uniform capacities.

V1
a1
Vi,1
a2
i
Vi
a2
Vi,n
Vi,2
Vn
V2
a1

Fig. 2. Illustration of our gap-producing reduction from the min-vertex cover problem to the MCRN problem in the non-segregated model. The figure shows an instance of the MCRN, where each green node _v_<sub>1</sub>_,v_<sub>2</sub>_,v<sub>i</sub>,...,v<sub>n</sub>_ corresponds to one vertex in the min-vertex cover instance.

