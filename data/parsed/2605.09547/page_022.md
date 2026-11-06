_t_+1. Combining this with Lemma 4.7, which states that the algorithm runs for \(\widetilde{O}(\sqrt{n})\) iterations, gives the theorem.

To show the claim for a single iteration, note that both players can simulate the above steaming algorithm. Specifically, as we assume both parties have access to the (_t_-1)-transcript, they can jointly simulate a single pass over the input of the streaming algorithm while communicating only \(\widetilde{O}(n)\) space. First player A iterates over all their edges and performs exactly the calculations of the streaming algorithm. By Lemma 4.18 a pass over the input uses only \(\widetilde{O}(n)\) additional space when having access to the (_t_-1)-transcript. So player B can continue simulating the current pass over the input after player A sends those additional \(\widetilde{O}(n)\) information. With this, the two parties jointly compute the new _t_-transcript, i.e., they now both have complete access to the _t_-transcript, giving us the theorem recursively.

## 5 Constructing the Gradient _g_

The main goal of this section is to prove the following theorem, which shows that we can construct exact gradient-like vectors with low space.

**Theorem 5.1.** _Given an_ \(\epsilon>0\), \(f:\mathbb{R}\rightarrow\mathbb{R}\)_, a directed weighted graph G_=(_V,E_) _given as stream, and implicit vectors_ \(v,\tau\in\mathbb{R}^E\) _satisfying_ \(n/m\le\tau\le 1\) _and_ \(-1\le v\le 1\) _such that for any given_ \(e\in E\) _we can query v<sub>e</sub> and_ \(\tau_e\) _in T time._

_Then we can construct an implicit representation of target vector_ \(g=(f(\text{round}_{\epsilon^\prime}(v))^{\text{b}(\text{round}_{1+\epsilon^\prime}\tau)}\)_. Our construction takes_ \(O(\epsilon'^{-2}logm)\) _space and O(mT_) _time._

_Given edge e, querying any entry g<sub>e</sub> takes T+O_(1) _time._

The proof will make use the following two lemmas from \[BLN<sup>+</sup>20\].

**Lemma 5.2** (\[BLN<sup>+</sup>20, Corollary 7.4\])**.** _Given_ \(h,v\in\mathbb{R}^k\) _we can compute in O(k_log_k_) _time_<tbc>

\(u=argmax_{\|vw\|_2+\|w\|_\infty\le 1}\langle h,w\rangle.\)

<tbc>Note that for \(v=Clog(4m/n)\cdot\sqrt{\tau}\) (where _C_ is some constant) we have \(\|vw\|_2=Clog(4m/n)\|w\|_\tau\) and thus \(\|vw\|_2+\|w\|_\infty=\|w\|_{\tau+\infty}\) by Definition 4.6. Thus we have

\(u=argmax_{\|vw\|_2+\|w\|_\infty\le 1}\langle h,w\rangle=h^{\text{b}(\tau)}.\)

Thus to get Theorem 5.1, we will use \(v=Clog(4m/n)\cdot\sqrt{\text{round}_{1+\epsilon^\prime}\tau}\) in Lemmas 5.2 and 5.3.

**Lemma 5.3** (\[BLN<sup>+</sup>20, Lemma 7.5\])**.** _Given_ \(\overline{h},\overline{v},\overline{f}\in\mathbb{R}^k\), \(h,v\in\mathbb{R}^n\)_, and a partition_ \(\cup_{i=1}^kI_i=[n]\)_, such that_

• \(h=\sum_{i=1}^k\overline{h_i}\cdot\mathbf{1}_{I_i}\),<tbc>

• \(v=\sum_{i=1}^k\overline{v_i}\cdot\mathbf{1}_{I_i}\)<tbc>

• \(\overline{f_i}=\sqrt{|I_i|}\)_, for all_ \(i\in[k]\) _(This is the square root of the frequency)_<tbc>

<tbc>_Let_ \(\overline{u}\in\mathbb{R}^k\) _be the maximizer of_<tbc>

\(\overline{u}:=argmax_{\overline{w}\in\mathbb{R}^k:\|(\overline{f}\overline{v})\overline{w}\|_2+\|\overline{w}\|_\infty\le 1}\langle\overline{hff},\overline{w}\rangle.\)

<tbc>_We can define_ \(u\in\mathbb{R}^n\) _via_ \(u=\sum_{i=1}^k\overline{u_i}\cdot\mathbf{1}_{I_i}\)_, then_<tbc>

\(\langle v,u\rangle=max_{w\in\mathbb{R}^n:\|vw\|_2+\|w\|_\infty\le 1}\langle h,w\rangle.\)

