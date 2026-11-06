**Lemma 4.10.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be forests, let_ \(\mathbf{S}\subseteq\mathbf{F}\) _be a spine, and let_ \(q\in\mathbf{S}\).<br>
_Then, we can calculate the function_ \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) _for all_ \((x,x')\in\mathrm{B}^\perp(1,1,\mathrm{l}(q),2|\mathbf{F}'|+1)\) _and_ \((y,y')\in\mathrm{B}^\top(\mathrm{r}(q),1,2|\mathbf{F}|+1,2|\mathbf{F}'|+1)\)_, where:_

\(\blacksquare\) \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) _if there exists_ \(t\in\mathbf{S}\) _is such that t\<q and_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) _aligns_ sub(_t_) _to any subtree of_ \(\mathbf{F}'\)_, and_

\(\blacksquare\) \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\le\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) _otherwise._<br>
_This computation takes time_ \(\mathcal{O}(\mathsf{T}_{MUL}(m_q)+m_q^{2+o(1)})\)_, where_ \(m_q=\mathrm{max}(|\mathbf{F}\backslash\mathrm{sub}(q)|,|\mathbf{F}'|)\)_, and requires as input the values_ \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) _for all_ \(v\in\mathbf{F}\backslash\mathrm{sub}(q)\), \(v'\in\mathbf{F}'\).

_In the unweighted setting, the computation takes time_ \(\mathcal{O}(\mathsf{T}_{MonMUL}(m_q,m_q,m_q,\mathrm{D})+m_q^{2+o(1)}g(\mathrm{D}))\) _where_ \(\mathrm{D}=\mathrm{max}(|\mathbf{F}|,|\mathbf{F}'|)\) _and_ \(\mathsf{T}_{MonMUL}(m,m,m,\mathrm{D})=f(m)g(\mathrm{D})\).

**Proof.** Let \(n=|\mathbf{F}|,n'=|\mathbf{F}'|\), and _n<sub>q</sub>_=|sub(_q_)|. Further, let _v_<sub>1</sub>_,...,v<sub>n</sub>_ and \(v'_1,\dots,v'_{n^\prime}\) be the pre-orders of **F** and \(\mathbf{F}'\), respectively, and let _i<sub>q</sub>_ be such that _v_<sub>_i<sub>q</sub>_</sub>_,...,v_<sub>_i<sub>q</sub>+n<sub>q</sub>_</sub> is the pre-order of sub(_q_).

Consider the alignment graph \(\bar{\mathbf{G}}\) w.r.t. \((\mathrm{w}_{\mathbf{F},\mathbf{F}^\prime},\mathbf{F},\mathbf{F}')\). Define the alignment graph \(\bar{\mathbf{G}}_{\backslash q}\), as the alignment graph obtained from \(\bar{\mathbf{G}}\) by removing from all nodes (and their incident edges) of the set \([i_q..(i_q+n_q)]\times[1..(n'+1)]\), and by adding an edge from (_x,i<sub>q</sub>_-1) to (_x,i<sub>q</sub>+n<sub>q</sub>_+1) of cost 0 for all \(x\in[1..(n'+1)]\). Note, the construction of \(\bar{\mathbf{G}}_{\backslash q}\) is possible as it requires to know the values \(\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\) for all \(v\in\mathbf{F}\backslash\mathrm{sub}(q)\), \(v'\in\mathbf{F}\).

We claim that solving BBD on \(\bar{\mathbf{G}}_{\backslash q}\) in time \(\mathcal{O}(\mathsf{T}_{MUL}(m_q)+m_q^{2+o(1)})\), leads to the desired func tion. In the unweighted setting, Corollary 4.9 shows that BBD can instead by computed in time \(\mathcal{O}(\mathsf{T}_{MonMUL}(m_q,m_q,\mathrm{D})+m_q^{2+o(1)}g(\mathrm{D}))\). For \((x,x')\in\mathrm{B}^\perp(1,1,\mathrm{l}(q),2|\mathbf{F}'|+1)\) and \((y,y')\in\mathrm{B}^\top(\mathrm{r}(q),1,2|\mathbf{F}|+1,2|\mathbf{F}'|+1)\), we define \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) to be the longest path from (_x,y_) to \((x',y')\) in \(\bar{\mathbf{G}}_{\backslash q}\) (in this proof we index nodes in \(\bar{\mathbf{G}}_{\backslash q}\) w.r.t. their original indices in \(\bar{\mathbf{G}}\)).

To see that the definition serves our purpose, consider arbitrary \((x,x')\in\mathrm{B}^\perp(1,1,\mathrm{l}(q),2|\mathbf{F}'|+1)\) and \((y,y')\in\mathrm{B}^\top(\mathrm{r}(q),1,2|\mathbf{F}|+1,2|\mathbf{F}'|+1)\). Whenever the longest path from \((x,x')\) to \((y,y')\) takes an outgoing edge from a node \((i,i')\) of the form (c), where _v<sub>i</sub>=s_ for some \(t\in S\) such that _t\<q_, then \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) aligns sub(_t_) to \(\mathrm{sub}(v'_{i^\prime})\). Note, all such outgoing edges start from a node in the set \([1..(i_q-1)]\times[1..(n'+1)]\) and arrive to a node in the set \([(i_q+n_q+1)..(n+1)]\times[1..(n'+1)]\). Consequently, such longest path survives in \(\bar{\mathbf{G}}_{\backslash q}\), and we conclude \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\ge\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

On the other hand, for any \((x,x')\in\mathrm{B}^\perp(1,1,\mathrm{l}(q),2|\mathbf{F}'|+1)\) and \((y,y')\in\mathrm{B}^\top(\mathrm{r}(q),1,2|\mathbf{F}|+1,2|\mathbf{F}'|+1)\), observe that the longest path between (_x,y_) to \((x',y')\) in \(\bar{\mathbf{G}}_{\backslash q}\) is no longer than the one between (_x,y_) to \((x',y')\) in \(\bar{\mathbf{G}}\). We conclude, \(\mathrm{sim}_q(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\le\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

## 4.6 Forest Edit Distance on Unbalanced Instances

In this section, we consider instances where one forest **F** is significantly larger than the other \(\mathbf{F}'\). Without loss of generality, assume \(n\ge n'\). We show that we can solve a restricted versions of the BBD problem more efficiently.

**Left-Right Border-to-Border Distances (LRBBD)**<br>
**Input:** two forests **F**, \(\mathbf{F}'\) of size \(|\mathbf{F}|=n,|\mathbf{F}'|=n'\), and a weight function \(\mathrm{w}:D\rightarrow\mathbb{R}\) such that \(D\subseteq\mathbf{F}\times\mathbf{F}'\).<br>
**Output:** \(\mathrm{dist}_\bar{\mathbf{G}}(\bar{u},\bar{w})\) for all \(\bar{u}\in 1\times[1..n'+1]\) and \(\bar{w}\in\mathrm{B}^\top(1,1,n+1,n'+1)\), where \(\bar{\mathbf{G}}\) is the alignment graph w.r.t. \((\mathrm{w},\mathbf{F},\mathbf{F}')\).

We say \((n,n')\) is the size of the LRBBD instance. We will solve the unbalanced LRBBD instance by decomposing the larger forest into forests of size at most \(n'\) using Mao’s decomposition algorithm

