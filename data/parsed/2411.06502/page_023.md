**Definition 4.2.** _Given a forest_ **F** _with pre-order v_<sub>1</sub>_,...,v_<sub>|**F**|</sub>_, we define_ \(\pi_\mathbf{F}:[1..|\mathbf{F}|]\rightarrow[1..|\mathbf{F}|+1]\) _as_ \(\pi_\mathbf{F}(i)=min\{j:j\ge i\text{\textit{and}}v_j\notin\mathsf{sub}(v_i)\}\)_. If no such j exists, then_ \(\pi_\mathbf{F}(i)=|\mathbf{F}|+1\).

In other words, \(\pi_\mathbf{F}(i)\) maps each node _v<sub>i</sub>_ to the next node that pre-order visits after leaving the subtree sub(_v<sub>i</sub>_) (see Figure 6 for an example).

**Definition 4.3** (See also \[Tou05, BCH<sup>+</sup>07, MTWZU09\])**.** _Given two forests_ **F**, \(\mathbf{F}'\) _with pre-orders v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> _and_ \(v'_1,\dots,v'_{|\mathbf{F}^\prime|}\)_, and given a weight function_ \(\mathsf{w}:D\rightarrow\mathbb{R}\) _such that_ \(\mathbf{F}\times\mathbf{F}'\subseteq D\)_, we define the_ alignment graph \(\tilde{\mathbf{G}}=(\tilde{V},\tilde{E})\mathsf{w}.\mathsf{r}.\mathsf{t}.(\mathsf{w},\mathbf{F},\mathbf{F}')\) _as the directed weighted acyclic graph with_

_Vertex set_ \(\tilde{V}=[1..(|\mathbf{F}|+1)]\times[1..(|\mathbf{F}'|+1)]\);

_Edge set_ \(\tilde{E}\) _such that_ \(\bar{e}=((u,u'),(w,w'))\in\tilde{E}\)_, if exactly one of the following holds:_

(a) \((w,w')=(u,u'+1)\),

(b) \((w,w')=(u+1,u')\)_, or_

(c) \((w,w')=(\pi_\mathbf{F}(u),\pi_{\mathbf{F}^\prime}(u'))\);

_Weight function_ \(\bar{\mathsf{w}}\) _such that_ \(\bar{\mathsf{w}}(\bar{e})=0\) _if_ \(\bar{e}\) _has the form_ (a) _or_ (b)_, and_ \(\bar{\mathsf{w}}(\bar{e})=\mathsf{sim}(\mathsf{sub}(v_u),\mathsf{sub}(v'_{u^\prime}))\) _if it has the form_ (c).

**Figure 6** The figure displays two forests \(\mathbf{F},\mathbf{F}'\), together with the two mappings \(\pi_\mathbf{F}:[1..5]\rightarrow[1..6]\) and \(\pi_{\mathbf{F}^\prime}:[1..5]\rightarrow[1..6]\) from Definition 4.2. On the right side the alignment graph \(\tilde{\mathbf{G}}\mathsf{w}.\mathsf{r}.\mathsf{t}.(\mathsf{w},\mathbf{F},\mathbf{F}')\) is depicted (weights are omitted) from Definition 4.3. The figure also illustrates \(\tilde{\mathbf{G}}[2..4][2..5]\) from Definition 4.4.

Figure 6 illustrates an example of an alignment graph. Notably, if **F** and \(\mathbf{F}'\) are forests containing single node trees, one obtains the alignment graph for string edit distance.

In the rest of Section 4, we slightly abuse notation, and for a forest **F** with pre-order _v_<sub>1</sub>_,...,v_<sub>|**F**|</sub>, we write l(_v_<sub>|**F**|+1</sub>)=2|**F**|+1.

**Definition 4.4.** _Let_ \(\tilde{\mathbf{G}}\) _be an alignment graph w.r.t_ \((\mathsf{w},\mathbf{F},\mathbf{F}')\) _where_ **F**, \(\mathbf{F}'\) _are two forests with pre-orders v_<sub>1</sub>_,...,v_<sub>|**F**|</sub> _and_ \(v'_1,\dots,v'_{|\mathbf{F}^\prime|}\)_. Given intervals_ \([i..j]\subseteq[1..(|\mathbf{F}|+1)]\), \([i'..j']\subseteq[1..(|\mathbf{F}'|+1)]\)_, we denote with_ \(\tilde{\mathbf{G}}[i..j][i'..j']\) _the alignment graph w.r.t._ \((\mathsf{w},\mathbf{F}[\mathsf{l}(v_i)..\mathsf{l}(v_j))\), \(\mathbf{F}'[\mathsf{l}(v'_{i^\prime})..\mathsf{l}(v'_{j^\prime}))\)).

Note that \(\tilde{\mathbf{G}}[i..j][i'..j']\) does not necessarily correspond to the subgraph of \(\tilde{\mathbf{G}}\) induced by the vertex set \([i..j]\times[i'..j']\), as there might exist \(z\in[i..j)\) such that \(v_z\notin\mathbf{F}[\mathsf{l}(v_i)..\mathsf{l}(v_j))\). However, we can still<tbc>

G
F
V1
6
πF
1
2
3
4
5
5
V2
V3
6
3
6
5
6
4
V5
4
4-5
F'
3
3
V1
V4
πF'
1
2
3
4
5
2
2
v' 2
v3
v5
4
3
4
6
6
2
3-4
1
1
2
3
4
5
6

