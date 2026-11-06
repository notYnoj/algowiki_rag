To complete the construction, let _k_=|_U_|, meaning that we are aiming for a perfect matching with minimum number of blocking pairs. Let \(\beta=h+\genfrac(){pt}{2}{h}{2}\). The statement follows from the following claims.

**Claim 1.** _If G admits a clique of size h, then there exists a perfect matching with at most_ \(\beta\) _blocking pairs._

_Proof._ Let _K_ be a size-_h_ clique and let \(E'\) be the induced edges in _G_\[_K_\]. Without loss of generality, assume that _K_={_v_<sub>1</sub>_,...,v<sub>h</sub>_} and \(E'=\{e_1,\dots,e_{\genfrac(){pt}{2}{h}{2}}\}\). We construct a matching _M_ as follows.

(1) Match the agents in \(\{\hat{u}_1,\dots,\hat{u}_k\}\cup\{t_1,\dots,t_h\}\) according to a perfect stable matching of _I_ restricted to \(\{\hat{u}_1,\dots,\hat{u}_k\}\cup\{t_1,\dots,t_h\}\); since the acceptability graph of the restricted to these agents is complete, we can find such a matching in polynomial time with Gale-Shapley algorithm \[11\]. Do the same for the set \(\{s_1,\dots,s_k\}\cup\{w_1,\dots,w_k\}\). For every \(v_j\in K\), let \(M(u_j)=\hat{w}_j\).<tbc>

(2) For each vertex \(v_i\notin K\), let \(M(\hat{u}_i)=\hat{w}_i\), and _M(u<sub>i</sub>_)=_w<sub>i</sub>_.<tbc>

(3) Match the agents in \(\{\hat{t}_1,\dots,\hat{t}_{\genfrac(){pt}{2}{h}{2}}\}\cup\{x_1,\dots,x_{\genfrac(){pt}{2}{h}{2}}\}\) according to a perfect stable matching of _I_ restricted to \(\{\hat{t}_1,\dots,\hat{t}_{\genfrac(){pt}{2}{h}{2}}\}\cup\{x_1,\dots,x_{\genfrac(){pt}{2}{h}{2}}\}\); since the acceptability graph of the restricted to these agents is complete, we can find such a matching in polynomial time using the Gale-Shapley algorithm \[11\]. Do the same for the set \(\{\hat{s}_1,\dots,\hat{s}_{\genfrac(){pt}{2}{h}{2}}\}\cup\{y_1,\dots,y_{\genfrac(){pt}{2}{h}{2}}\}\). For each edge \(e_z\in E'\) and each incident vertex _v<sub>i</sub>_, and each \(r\in[L]\), let \(M(\pi_{e_z}^{u_i}[r])=\theta_{e_z}^{u_i}[r]\) and \(M(\hat{\pi}_{e_z}^{u_i}[r])=\hat{\theta}_{e_z}^{u_i}[r]\).<tbc>

(4) For each edge \(e\notin E'\) and each incident vertex _v<sub>i</sub>_, and each \(r\in[L]\), do the following. Let _M(x<sub>e</sub>_)=_y<sub>e</sub>_, \(M(\pi_e^{u_i}[r])=\hat{\theta}_e^{u_i}[r]\) and \(M(\hat{\pi}_e^{u_i}[r])=\theta_e^{u_i}[r]\).

It remains to show that _M_ induces at most \(\beta\) blocking pairs. Let us consider every agent from _U_.

- No vertex selector agent can be involved in a blocking pair since they only prefer a vertex agent with lower index, but _M_ restricted to the vertex selectors and vertex agents is stable by construction.<tbc>

- Similarly, no edge selector agent can be involved in a blocking pair.<tbc>

- Let \(v_i\notin K\) be an arbitrary non-clique vertex. Agent \(\hat{u}_i\) is already matched with his most preferred agent. Agent _u<sub>i</sub>_ prefers \(\hat{w}_i\) to his partner _w<sub>i</sub>_, but agent \(\hat{w}_i\) is matched with his most preferred agent; see (2). Agent _u<sub>i</sub>_ also prefers each agent \(\theta_e^{u_i}[r]\) to his partner _w<sub>i</sub>_. But each \(\theta_e^{u_i}[r]\) is matched with his most preferred agent \(\hat{\pi}_e^{u_i}[r]\) since no edge incident to _v<sub>i</sub>_ is in \(E'\); see (4).<tbc>

- Let \(e\notin E'\) be an arbitrary non-clique edge. Agent _x<sub>e</sub>_ is already matched with his most preferred agent _y<sub>e</sub>_.<tbc>

- Let \(e\notin E'\) be an arbitrary non-clique edge and let \(r\in[L],v_i\in e\). Agent \(\pi_e^{u_i}[r]\) prefers _y<sub>e</sub>_ to his partner, but agent _y<sub>e</sub>_ is already matched with his most preferred partner _x<sub>e</sub>_; see (4). Agent \(\pi_e^{u_i}[r]\) also prefers \(\theta_e^{u_i}[r]\) to his partner, but \(\theta_e^{u_i}[r]\) is already matched with his most preferred partner. Agent \(\hat{\pi}_e^{u_i}[r]\) prefers \(\hat{\theta}_e^{u_i}[r]\) to his partner, but \(\hat{\theta}_e^{u_i}[r]\) is already matched with his most preferred partner.<tbc>

- Let \(v_i\in K\) be an arbitrary clique vertex. Agent _u<sub>i</sub>_ is matched to his most preferred agent. Agent \(\hat{u}_i\) forms with \(\hat{w}_i\) a blocking pair. He does not form with any vertex selector agent a blocking pair by reasoning analogously the first case.<tbc>

- Let \(e\in E'\) be an arbitrary clique edge. Agent _x<sub>e</sub>_ forms with _y<sub>e</sub>_ a blocking pair. He does not form with any edge selector agent a blocking pair. For each incident vertex _v<sub>i</sub>_ of _e_ (i.e., \(v_i\in K\)) and each \(r\in[L]\), both edge agents \(\pi_e^{u_i}[r]\) and \(\hat{\pi}_e^{u_i}[r]\) are already matched with their most preferred agents, respectively. So they will not form with anyone a blocking pair.

Summarizing, all but the last two cases yield blocking pairs. The last two cases give _h_ and \(\genfrac(){pt}{2}{h}{2}\) blocking pairs, respectively. Hence, \(\beta=h+\genfrac(){pt}{2}{h}{2}\), as desired. (end of Claim 3) \(\diamond\)

Before we continue with the backward direction, let us observe the following.

**Claim 2.** _Let M be a perfect matching of the reduced instance. Then, for each edge_ \(e\in E\)_, it holds that M(y<sub>e</sub>_)=_x<sub>e</sub> or_ \(M(y_e)=\hat{s}_z\) _for some_ \(z\in[\genfrac(){pt}{2}{h}{2}]\).

_Proof._ Since _M_ is perfect, by the preferences of the edge selectors, we know that there are exactly \(\genfrac(){pt}{2}{h}{2}\) edge-agents from _U_ that are each matched with some edge selector \(\hat{t}_z\) from _W_. The remaining \(\hat{m}-\genfrac(){pt}{2}{h}{2}\) edge-agents _x<sub>e</sub>_ must be matched with their only available partner _y<sub>e</sub>_. This leaves \(\genfrac(){pt}{2}{h}{2}\) edge-agents from _W_ that are to be matched with some edge selector agents from _U_, as desired. (end of Claim 2) \(\diamond\)

**Claim 3.** _If G does not admit a clique of size h, then every perfect matching induces at least_ \(L>F(\beta)\cdot\beta\) _blocking pairs._

