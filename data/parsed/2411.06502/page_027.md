of times we apply transition of type I and II, respectively. If the diameter of \(\bar{G}\) is at most D, then we note that the running time is in fact bounded by \(\mathcal{O}((t_\mathrm{I}+t_\mathrm{II})\cdot\mathsf{T}_{\mathrm{MonMUL}}(m,m,m,\mathrm{D}))\). To bound _t_<sub>I</sub>+_t_<sub>II</sub>, we report here the argumentation from Section 4.2.2. of \[Mao22\].

For every transition of type I, we merge two forests each of size no less than \(\Delta/3\), yielding \(t_\mathrm{I}=\mathcal{O}(|\mathbf{F}|/\Delta)\).

Now, for _t_<sub>II</sub>, let us decompose it into \(t_\mathrm{II}=t_\mathrm{II}^{(1)}+t_\mathrm{II}^{(2)}\), where \(t_\mathrm{II}^{(1)}\) denotes the number of transitions of type II where **H**_<sub>s</sub>_ contains fewer than two trees or either |**L**<sub>**H**_<sub>s</sub>_</sub>| or |**R**<sub>**H**_<sub>s</sub>_</sub>| is less than \(\Delta/3\), and \(t_\mathrm{II}^{(2)}\) represents the number of transitions of type II where **H**_<sub>s</sub>_ contains at least two trees and both |**L**<sub>**H**_<sub>s</sub>_</sub>| and |**R**<sub>**H**_<sub>s</sub>_</sub>| are no less than \(\Delta/3\). For \(t_\mathrm{II}^{(1)}\), we have \(|\mathbf{H}\backslash\mathbf{H}_s|>\Delta/3\), as otherwise, we would have not halted the removal process. Since **H**\\**H**_<sub>s</sub>_ are disjoint across different type II transitions, we have \(t_\mathrm{II}^{(1)}=\mathcal{O}(|\mathbf{F}|/\Delta)\). Regarding \(t_\mathrm{II}^{(2)}\), observe that the subsequent transition will be of type I, so \(t_\mathrm{II}^{(2)}\le t_\mathrm{I}=\mathcal{O}(|\mathbf{F}|/\Delta)\).

**Corollary 4.9.** _There is an algorithm that solves in time_ \(\mathcal{O}(\mathsf{T}_{\mathrm{MUL}}(m)+m^{2+o(1)})\) _a_ \((\mathrm{w},\mathbf{F},\mathbf{F}')\)_-BBD instance of size m._

_Furthermore, if the BBD instance has diameter_ D_, the algorithm runs in time_ \(\mathcal{O}(\mathsf{T}_{\mathrm{MonMUL}}(m,m,m,\mathrm{D})+m^{2+o(1)}g(D))\)_, where_ \(\mathsf{T}_{\mathrm{MonMUL}}(m,m,m,\mathrm{D})=\mathcal{O}(f(m)g(\mathrm{D}))\) _for some functions f,g._

**Proof.** We apply Lemma 4.8 recursively with threshold \(\Delta=m/\alpha\) for some constant \(\alpha\ge 1\) to be determined later. For small enough instances any algorithm computing shortest paths in a directed acyclic graph will do. Thereby, we obtain an algorithm for the FED Problem where the running time is described by the recurrence

\(\mathsf{T}(m)\le c_1\cdot(m/\Delta)^2\cdot\mathsf{T}(\Delta)+c_2\cdot(m/\Delta)^2\cdot\mathsf{T}_{\mathrm{MUL}}(m)+c_3\cdot m^2\)<br>
\(=c_1\alpha^2\cdot\mathsf{T}(m/\alpha)+c_2\alpha^2\cdot\mathsf{T}_{\mathrm{MUL}}(m)+c_3\cdot m^2\)

where _c_<sub>1</sub>_,c_<sub>2</sub>_,c_<sub>3</sub>, are the constants hidden in the number of problems we recurse on (parameter _k_ in Lemma 4.8), in the time needed to solve the \((\mathrm{w},\mathbf{H},\mathbf{F}')\)-BBD instance, and the time needed to find the _k_ pairs of subforests, respectively. Now, for any \(\varepsilon>0\), we can choose a sufficiently large constant \(\alpha\) such that

\(\mathrm{log}_\alpha(c_1\alpha^2)=\mathrm{log}_\alpha c_1+2<2+\varepsilon\)

and still \(c_2\alpha^2=\mathcal{O}(1)\). By applying the Master theorem, we conclude that \(\mathsf{T}(m)=\mathcal{O}(\mathsf{T}_{\mathrm{MUL}}(m)+m^{2+o(1)})\).

If the diameter is at most D, we instead have the recurrence,

\(\mathsf{T}(m)=c_1\alpha^2\cdot\mathsf{T}(m/\alpha)+c_2\alpha^2\cdot\mathsf{T}_{\mathrm{MonMUL}}(m,m,m,\mathrm{D})+c_3\cdot m^2\)<br>
\(=c_1\alpha^2\cdot\mathsf{T}(m/\alpha)+O(f(m)g(\mathrm{D})).\)

By the master theorem, we can choose a sufficiently large constant \(\alpha\) such that \(\mathrm{log}_\alpha(c_1\alpha^2)<2+\varepsilon\) for any \(\varepsilon\). By applying the Master theorem, we conclude that \(\mathsf{T}(m)=\mathcal{O}((f(m)+m^{2+o(1)})g(D))=\mathcal{O}(\mathsf{T}_{\mathrm{MonMUL}}(m,m,m,\mathrm{D})+m^{2+o(1)}g(D))\).

**Main Theorem 4.** _Suppose there exists an algorithm computing the min-plus product of two_ \(m\times m\) _matrices in time_ T<sub>MUL</sub>(_m). Then, there is an algorithm for FED running in time_ O(T<sub>MUL</sub>(n_)+_n_<sup>2+_o_(1)</sup>)_, where_ \(n=\mathrm{max}(|\mathbf{F}|,|\mathbf{F}'|)\).

**Proof.** We use Corollary 4.9 on the weight function defined in Lemma 4.5. Note that when the FED instance is unweighted, the BBD instance has diameter at most O(_n_). In particular, we have \(\mathsf{T}_{\mathrm{MonMUL}}(n,n,n,\mathcal{O}(n))=\mathcal{O}(\mathsf{T}_{\mathrm{MonMUL}}(n))\).

