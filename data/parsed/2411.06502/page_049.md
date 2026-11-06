If **F**[_x...y_]=sub(_s_) and _s_ is mapped to any node contained in \(\mathsf{sub}(q')\), then \(\mathsf{sim}(\mathsf{sub}(s),\mathbf{F}[x'..y'))=\) sim(sub(_s_),sub(_q_<sup>∗</sup>)). Observe that \(\mathsf{sim}(\mathsf{sub}(s),\mathsf{sub}(q'))\) is already at our disposal as input of the \((s,s',q,q')\)-DISED instance.

If **F**[_x...y_]=sub(_s_) and _s_ is mapped to any node contained in \(\mathbf{F}'[x'..l(q'))\), then we have that \(\mathsf{sim}(\mathsf{sub}(s),\mathbf{F}'[x'..y'))=\mathsf{sim}(\mathsf{sub}(s),\mathsf{sub}(v'))\) for some \(v'\in\mathbf{F}'[x'..l(q'))\) and \(v'\notin\mathbf{S}'\). Note, all these values are already at our disposal in the SED Problem.

Lastly, if **F**[_x...y_]=sub(_s_) and _s_ is mapped to any node contained in \(\mathbf{F}'[\mathsf{r}(q')..y')\), then we can apply reverse symmetry obtaining the previous case.

## 5.5 Spine Edit Distance on Unbalanced Instances

In this section, we give an algorithm for Spine Edit Distance on unbalanced instances, where one tree, say **F** is significantly larger than \(\mathbf{F}'\). In the following assume |**F**|=_n_, \(|\mathbf{F}'|=n'\), and \(n\ge n'\). For the smaller tree \(\mathbf{F}'\), we let \(r'\) denote its root (i.e. top-most node of the spine) and \(b'\) denote the bottom-most node of the spine. In this setting, we compute a slightly restricted version of the divide et impera scheme for Spine Edit Distance.

On unbalanced instances, we will only decompose the larger graph **F**, so that we only handle \((s,s',q,q')\)-UDISED instances with \(s'=r'\) and \(q'=b'\). Given such an instance, we define its _size_ as \((m,n')\) where

\(m=|\mathsf{sub}(s)\backslash\mathsf{sub}(q)|.\)

In the following (sub)section, we present a divide-et-impera algorithm A<sub>UDISED</sub> solving UDISED. The three lemmas, the proof of which we defer for now, that motivate such an approach are the following.

**Lemma 5.12.** _Consider an_ \((s,s',q,q')\)_-UDISED instance of size_ \((m,n')\) _such that_ \(m=\mathcal{O}(n')\)_. Then, we can solve the_ \((s,s',q,q')\)_-UDISED instance in time_ \(\mathcal{O}(\mathsf{T}_{MUL}(n')+n'^{2+o(1)})\).

_Furthermore, if the UDISED instance is unweighted, the algorithm requires time_ \(\mathcal{O}(\mathsf{T}_{MonMUL}(n')+n'^{2+o(1)}g(n'))\) _where_ \(\mathsf{T}_{MonMUL}(n',n',n',\mathrm{D})=\mathcal{O}(f(n')g(\mathrm{D}))\).

**Lemma 5.13.** _Consider an_ \((s,s',q,q')\)_-UDISED instance of size_ \((m,n')\) _such that s immediately precedes q. Then, we can solve the_ \((s,s',q,q')\)_-UDISED instance in time_ \((m/n')^{1+o(1)}\cdot(\mathsf{T}_{MUL}(n')+n'^{2+o(1)})\).

