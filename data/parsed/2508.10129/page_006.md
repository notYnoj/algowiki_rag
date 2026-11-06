## Agents.

We create two disjoint sets of agents, _U_ and _W_.

- For every \(z\in[h]\), we create two vertex selector agents _s<sub>z</sub>_ and _t<sub>z</sub>_, and add them to _U_ and _W_, respectively.<tbc>

- For every \(p\in[\genfrac(){pt}{2}{h}{2}]\), we create two edge selector agents \(\hat{s}_p\) and \(\hat{t}_p\), and add them to _U_ and _W_, respectively.<tbc>

**-** For every vertex \(v_i\in V\) , we create four vertex-agents _u<sub>i</sub>_, \(\hat{u}_i\), _w<sub>i</sub>_, and \(\hat{w}_i\), and add the first two to _U_, and the last two to _W_.<tbc>

**-** For every edge \(e\in E\), we do the following. We create two edge-agents _x<sub>e</sub>_ and _y<sub>e</sub>_, and add them to _U_ and _W_, respectively. Additionally, let _v<sub>i</sub>_ and _v<sub>j</sub>_ denote the two endpoints of _e_, then, we create 8 groups of edge agents \(\pi_e^{u_i}[r]\), \(1\pi_e^{u_j}[r]\), \(\hat{\pi}_e^{u_i}[r]\), \(\hat{\pi}_e^{u_j}[r]\), \(\theta_e^{u_i}[r]\), \(\theta_e^{u_j}[r]\), \(\hat{\theta}_e^{u_i}[r]\), \(\hat{\theta}_e^{u_j}[r]\), for \(r\in[L]\). We add the first four groups to _U_ and the last four groups to _W_. Note that these edge agents’ preference orders will enforce that matching two adjacent vertices to the selector agents will induce too many blocking pairs (at least _L_).

Summarizing, \(U:=\{s_z|z\in[h]\}\cup\{\hat{s}_p|p\in[\genfrac(){pt}{2}{h}{2}]\}\cup\{u_i,\hat{u}_i|v_i\in V\}\cup\{x_e|e\in E\}\cup\{\pi_e^{u_i}[r],\pi_e^{u_j}[r],\hat{\pi}_e^{u_i}[r],\hat{\pi}_e^{u_i}[r]|e\in E\) with \(e=\{v_i,v_j\},r\in[L]\}\) and \(W:=\{t_z|z\in[h]\}\cup\{\hat{t}_p|p\in[\genfrac(){pt}{2}{h}{2}]\}\cup\{w_i,\hat{w}_i|v_i\in V\}\cup\{y_e|e\in E\}\cup\{\theta_e^{u_i}[r],\theta_e^{u_j}[r],\hat{\theta}_e^{u_i}[r],\hat{\theta}_e^{u_j}[r]|e\in E\) with \(e=\{v_i,v_j\},r\in[L]\}\). In total, we have created \(2(h+\genfrac(){pt}{2}{h}{2}+2\hat{n}+\hat{m}+4\hat{m}\cdot L)\) agents.

## Agents’ preference orders.

For a given subset _Q_ of agents, let \(\langle Q\rangle\) denote an arbitrary but fixed linear order of the elements in _Q_.

The preference orders of the agents are as follows, where \(z\in[h]\), \(p\in[\genfrac(){pt}{2}{h}{2}]\), \(r\in[L]\), \(e\in E\) with _e_={_v<sub>i</sub>,v<sub>j</sub>_}, \(\Theta(v_i):=\{\theta_{e^\prime}^{u_i}[r']|v_i\in e'\) for some \(e'\in E\wedge r'\in[L]\}\), and \(\Pi(e):=\{\pi_e^{u_i}[r'],\pi_e^{u_j}[r']|r'\in[L]\}\).

\(s_z:\langle\{w_i|v_i\in V\}\rangle,t_z:\langle\{\hat{u}_i|v_i\in V\}\rangle,\)<br>
\(\hat{s}_z:\langle\{y_e|e\in E\}\rangle,\hat{t}_z:\langle\{x_e|e\in E\}\rangle,\)<br>
\(u_i:\hat{w}_i\succ\langle\Theta(v_i)\rangle\succ w_i,w_i:u_i\succ s_1\succ\cdots\succ s_h,\)<br>
\(\hat{u}_i:\hat{w}_i\succ t_1\succ\cdots\succ t_h,\hat{w}_i:\hat{u}_i\succ u_i,\)<br>
\(x_e:y_e\succ\hat{t}_1\succ\cdots\succ\hat{t}_{\genfrac(){pt}{2}{h}{2}},y_e:x_e\succ\langle\Pi(e)\rangle\succ\hat{s}_1\succ\cdots\succ\hat{s}_{\genfrac(){pt}{2}{h}{2}},\)<br>
\(\pi_e^{u_i}[r]:\theta_e^{u_i}[r]\succ y_e\succ\hat{\theta}_e^{u_i}[r],\theta_e^{u_i}[r]:\hat{\pi}_e^{u_i}[r]\succ u_i\succ\pi_e^{u_i}[r],\)<br>
\(\hat{\pi}_e^{u_i}[r]:\hat{\theta}_e^{u_i}[r]\succ\theta_e^{u_i}[r],\hat{\theta}_e^{u_i}[r]:\pi_e^{u_i}[r]\succ\hat{\pi}_e^{u_i}[r],\)<br>
\(\hat{\pi}_e^{u_j}[r]:\hat{\theta}_e^{u_j}[r]\succ\theta_e^{u_j}[r],\hat{\theta}_e^{u_j}[r]:\pi_e^{u_j}[r]\succ\hat{\pi}_e^{u_j}[r],\)<br>
\(\pi_e^{u_j}[r]:\theta_e^{u_j}[r]\succ y_e\succ\hat{\theta}_e^{u_j}[r],\theta_e^{u_j}[r]:\hat{\pi}_e^{u_j}[r]\succ u_j\succ\pi_e^{u_j}[r].\)

