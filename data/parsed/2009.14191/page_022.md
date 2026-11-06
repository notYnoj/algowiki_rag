is not matched solely to agents from CO<sub>_a<sub>j</sub>_</sub>, then it forms a blocking 3-set together with any two other agents of CO<sub>_a<sub>j</sub>_</sub> which are not matched solely to agents from CO<sub>_a<sub>j</sub>_</sub>. Therefore, no agent from CO<sub>_a<sub>i</sub>_</sub> including _a<sub>i</sub>_ is matched to a 2-set which it prefers to any 2-set consisting of agents from CO<sub>_a<sub>i</sub>_</sub>. By Lemma 3.3, it follows that there is a blocking 3-set in \(\{a_i\}\cup\{z_{a_i}^r:r\in[5]\}\), contradicting the stability of _M_. Thus, \(M(a)\unknown_ap\) holds for all \(a\in\{a_1,\dots,a_s\}\).

It remains to show that _M_ is stable in I<sub>0</sub>. First note that the above argument shows that _M<sub>s</sub>_ matches every agent \(z_{a_j}^r\) from cut-off gadget CO<sub>_a<sub>j</sub>_</sub> to a 2-set consisting solely of agents from CO<sub>_a<sub>j</sub>_</sub>. Thus, every agent \(a\in A\) is matched the same in _M<sub>s</sub>_ and _M_. Hence, any blocking 3-set for _M_ is also a blocking 3-set for _M<sub>s</sub>_, and thus, _M_ is stable.

Having shown that the cut-off gadgets have the desired effect, we now show how we can model the selection of one vertex being part of the independent set.

**Vertex-Selection Gadget.** A vertex-selection gadget has 6_n_ agents _a<sub>p</sub>_, \(b_p(p\in[n])\), _c<sub>q</sub>_, \(\bar{c}_q(q\in[n-1])\), _d<sub>r</sub>_, and \(\bar{d}_r(r\in[n+1])\). The intuitive idea is the following. The agents _a<sub>p</sub>_ and _b<sub>p</sub>_ want to be matched to 2-sets \(\{c_q,\bar{c}_{q^\prime}\}\). As _c<sub>q</sub>_ prefers \(\{a_p,\bar{c}_{q^\prime}\}\) to \(\{b_{p^\prime},\bar{c}_{q^\prime}\}\) while \(\bar{c}_{q^\prime}\) prefers \(\{b_{p^\prime},c_q\}\) to {_a<sub>p</sub>,c<sub>q</sub>_}, we can match the _n_-1 sets of size two of the form {_c<sub>q</sub>,<o>c</o><sub>q</sub>_} to the agents \(\{a_p:p<\ell\}\cup\{b_p:p<n+1-\ell\}\) for any \(\ell\in[n]\), corresponding to selecting the vertex \(v_\ell\) to be part of the independent set. The agents \(\{a_p:p\ge\ell\}\cup\{b_p:p\ge n+1-\ell\}\) are then matched to the 2-sets \(\{d_r,\bar{d}_r\}\), and can form blocking 3-sets with the edge gadgets (which are described later).

Formally, the preferences look as follows.

\(a_p:\{\{c_q,\bar{c}_{q^\prime}\}:q,q'\in[n-1]\}\succ\{\{d_r,\bar{d}_{r^\prime}\}:r,r'\in[n+1]\}\succ\mathrm{CO}_{a_p},\)<br>
\(b_p:\{\{c_q,\bar{c}_{q^\prime}\}:q,q'\in[n-1]\}\succ\{\{d_r,\bar{d}_{r^\prime}\}:r,r'\in[n+1]\}\succ\mathrm{CO}_{b_p},\)<br>
\(c_q:\{\{a_1,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\succ\{\{a_2,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\succ\cdots\succ\{\{a_n,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\)<br>
\(\succ\{\{b_1,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\succ\{\{b_2,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\succ\cdots\succ\{\{b_k,\bar{c}_{q^\prime}\}:q'\in[n-1]\}\)<br>
\(\succ\mathrm{CO}_{c_q},\)<br>
\(\bar{c}_q:\{\{b_1,c_{q^\prime}\}:q'\in[n-1]\}\succ\{\{b_2,c_{q^\prime}\}:q'\in[n-1]\}\succ\cdots\succ\{\{b_n,c_{q^\prime}\}:q'\in[n-1]\}\)<br>
\(\succ\{\{a_1,c_{q^\prime}\}:q'\in[n-1]\}\succ\{\{a_2,c_{q^\prime}\}:q'\in[n-1]\}\succ\cdots\succ\{\{a_n,c_{q^\prime}\}:q'\in[n-1]\}\)<br>
\(\succ\mathrm{CO}_{\bar{c}_q},\)<br>
\(d_r:\{\{a_1,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\succ\{\{a_2,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\succ\cdots\succ\{\{a_n,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\)<br>
\(\succ\{\{b_1,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\succ\{\{b_2,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\succ\cdots\succ\{\{b_n,\bar{d}_{r^\prime}\}:r'\in[n+1]\}\)<br>
\(\succ\mathrm{CO}_{d_r},\)<br>
\(\bar{d}_r:\{\{b_1,d_{r^\prime}\}:r'\in[n-1]\}\succ\{\{b_2,d_{r^\prime}\}:r'\in[n-1]\}\succ\cdots\succ\{\{b_n,d_{r^\prime}\}:r'\in[n-1]\}\)<br>
\(\succ\{\{a_1,d_{r^\prime}\}:r'\in[n+1]\}\succ\{\{a_2,d_{r^\prime}\}:r'\in[n+1]\}\succ\cdots\succ\{\{a_n,d_{r^\prime}\}:r'\in[n+1]\}\)<br>
\(\succ\mathrm{CO}_{\bar{d}_r}.\)

In the master poset, we have \(x_p\succ x_q\) for _p\<q_ for all \(x\in\{a,b,c,\bar{c},d,\bar{d}\}\) as well as \(x_i\perp y_j\) for all \(x\neq y\). See Figure 1 for an example of the 3-sets {_v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>} such that {_v_<sub>1</sub>_,v_<sub>2</sub>_,v_<sub>3</sub>}\\{_v<sub>p</sub>_} is before the cut-off gadget of _v<sub>p</sub>_ in the preferences of _v<sub>p</sub>_ for all \(p\in[3]\).

**Lemma 4.8.** _Let_ I _be a_ MDSR-Poset_-instance containing a vertex-selection gadget such that every agent v in the vertex-selection gadget except for_ \(\{a_i,b_i:i\in[3n'+1]\}\) _prefers all 2-sets consisting of two agents in the vertex-selection gadget to a 2-set containing an agent outside the vertex-selection gadget._

