<tbc>matched in any stable matching by a gadget based on a small unsolvable instance. However, modelling the ties in the preferences is a bit more complicated in our case, and is done by the tie gadget described in Section 4.4.1.

We construct a 3-DSRI-ML instance \(\mathcal{I}'\) with a strictly ordered master poset from an instance I of Perfect-SMTI-ML as follows. For each man _m<sub>i</sub>_, we add an agent _a<sub>i</sub>_, and for each woman _w<sub>j</sub>_, we add an agent _b<sub>j</sub>_. For each man _m<sub>i</sub>_, and each woman _w<sub>j</sub>_ who is not tied with another woman in _m<sub>i</sub>_’s preference list, we add an agent _c<sub>i,j</sub>_. For each man _m<sub>i</sub>_, and each tie \(w_j\perp_mw_{j+1}\) in _m<sub>i</sub>_’s preference list, we add a tie gadget \(T_i^j\) (described in Section 4.4.1).

It remains to describe the preferences. For each man _m<sub>i</sub>_, we define a sublist A_<sub>i</sub>_ as follows. Process all woman _w<sub>j</sub>_ adjacent to _m<sub>i</sub>_ by increasing _j_. If the woman is not tied with another woman adjacent to _m<sub>i</sub>_, then add the 2-set {_a<sub>i</sub>,c<sub>i,j</sub>_}, followed by {_b<sub>j</sub>,c<sub>i,j</sub>_}. Otherwise, _w<sub>j</sub>_ is tied with _w_<sub>_j_+1</sub> in the preference list of _m<sub>i</sub>_. Then add the 2-sets \(\{a_i,c_{i,j}\}\succ_\mathrm{ML}\left\{a_i,c_{i,j+1}\right\}\succ_\mathrm{ML}\left\{a_i,c'_{i,j}\right\}\succ_\mathrm{ML}\left\{b_j,c_{i,j}\right\}\succ_\mathrm{ML}\left\{b_j,c_{i,j+1}\right\}\succ_\mathrm{ML}\left\{b_j,c'_{i,j}\right\}\) to A_<sub>i</sub>_ (see Section 4.4.1).

For each man _m<sub>i</sub>_, we add a cut-off gadget _I<sub>i</sub>_ (described in Section 4.4.2) for agent _a<sub>i</sub>_.

We start by showing that the preferences are indeed derived from a strictly ordered master poset of agents.

**Observation 4.31.** _The master poset_ \(\succ_\mathrm{ML}\) _is derived from a strict order._

_Proof._ First, we order the tie gadgets \(T_{i_1}^{j_1},T_{i_2}^{j_2},\dots,T_{i_r}^{j_r}\) such that \(i_\ell\le i_{\ell+1}\) and if \(i_\ell=i_{\ell+1}\), then \(j_\ell<j_{\ell+1}\). For each tie gadget \(T_i^j\), define the sublist \(\mathcal{D}_i^j\) via \(d_{i,j}^1\succ d_{i,j}^2\succ\cdots\succ d_{i,j}^8\). Furthermore, we define the sublist \(\mathcal{C}_i^j\) via \(c_{i,j}\succ c_{i,j+1}\succ c'_{i,j}\). For every _i_ and _j_ such that _m<sub>i</sub>_ does not tie _w<sub>j</sub>_ with another woman but _w<sub>j</sub>_ is contained in the preferences of _m<sub>i</sub>_, we define \(\mathcal{C}_i^j\) to be the sublist containing only _c<sub>i,j</sub>_. For every _i_ and _j_ such that _w<sub>j</sub>_ is not contained in the preferences of _m<sub>i</sub>_ or _m<sub>i</sub>_ ties _w<sub>j</sub>_ with _w_<sub>_j_-1</sub>, we define C to be an empty sublist. The master poset now looks as follows:

\(\mathcal{D}_{i_1}^{j_1}\succ\cdots\succ\mathcal{D}_{i_r}^{j_r}\succ a_1\succ a_2\succ\cdots\succ a_{|M|}\succ b_1\succ\cdots\succ b_{|W|}\)<br>
\(\succ\mathcal{C}_1^1\succ\mathcal{C}_2^1\succ\dots\mathcal{C}_{|U|}^1\succ\mathcal{C}_1^2\succ\cdots\succ\mathcal{C}_{|U|}^2\succ\mathcal{C}_1^3\succ\cdots\succ\mathcal{C}_{|U|}^{|W|}.\)

It is easy to verify that the preferences are indeed derived from this master poset.

Notably, the preferences of every agent are not only derived from the master poset of agents, but also from a master list of 2-sets (where again every agent can declare an arbitrary set of 2-sets to be unacceptable).

Having described the construction, we continue by showing that the corresponding reduction is indeed correct.

## 4.4.4 Proof of the forward direction

We first show that a perfect stable matching in the Perfect-SMTI-ML instance I implies a perfect stable matching in the constructed 3-DSRI-ML instance \(\mathcal{I}'\).

**Lemma 4.32.** _If the_ Perfect-SMTI-ML _instance_ I _admits a perfect stable matching M, then the_ 3-DSRI-ML _instance_ \(\mathcal{I}'\) _admits a stable matching._

_Proof._ We construct a stable matching \(M'\) as follows, starting with \(M'=\emptyset\). For every edge \((m_i,w_j)\in M\), we add the 3-set {_a<sub>i</sub>,b<sub>j</sub>,c<sub>i,j</sub>_} to \(M'\). If _w<sub>j</sub>_ is tied with woman _w_<sub>_j_-1</sub>, then we add the 3-sets \(\{c_{i,\ell},d_{i,j}^5,d_{i,j}^8\}\), \(\{d_{i,j}^2,d_{i,j}^3,d_{i,j}^7\}\), and \(\{d_{i,j}^1,d_{i,j}^4,d_{i,j}^6\}\). If _w<sub>j</sub>_ is tied with woman _w_<sub>_j_+1</sub>, then we add the 3-sets \(\{d_{i,\ell}^1,d_{i,\ell}^2,d_{i,\ell}^8\}\) and \(\{d_{i,\ell}^3,d_{i,\ell}^4,d_{i,\ell}^5\}\). For each tie gad get \(T_i^j\) between _m<sub>i</sub>_, _w<sub>j</sub>_ and _w_<sub>_j_+1</sub> such that \((m_i,w_j)\notin M\) and \((m_i,w_{j+1})\notin M\), we add the<tbc>

