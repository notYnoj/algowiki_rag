**Lemma 4.7.** _Let T be any tree in_ \(G_\Phi\) _rooted at c_<sub>0</sub>_, and let_ \(\varsigma\in[q]^{\mathrm{vbl}(T)}\) _be a partial assignment. Given the witness tree of the execution log being T and the witness assignment being_ \(\varsigma\)_, a run of Algorithm 2 from_ \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing)\) _is fully determined, except for the random choices made in Line 2._

_Proof._ For each \(c\in V(T)\), define var(_c_) as the set of variables within vbl(_c_), excluding all variables within \(\mathrm{vbl}(c')\) for any \(c'\in V(T)\) such that \(\mathrm{dep}(c')<\mathrm{dep}(c)\) in _T_ and \(\mathrm{vbl}(c')\cap\mathrm{vbl}(c)\neq\emptyset\). Note that var(_c_) is determined by the witness tree _T_.

Then, the random choices in Line 6 (and Line 13) can be determined by checking whether \(c^O\in V(T)\) and vbl(_c_)=var(_c<sup>O</sup>_) for the pinned constraint \(c\in\mathcal{C}^*\) picked in Line 5 (and Line 12). Recall that _c<sup>O</sup>_ denotes the original unpinned constraint from C corresponding to _c_.

The random assignments generated in Lines 10 and 17 are recorded by the witness assignment \(\varsigma\), and thus can be fully recovered from \(\varsigma\).

Therefore, a run of Algorithm 2 from \(\mathrm{Couple}(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing)\) can be deterministically simulated, except for the random assignments generated in Line 2. □

## 4.3. Analysis of the coupling.

In this subsection, we utilize the witness tree and witness assignment defined previously to prove Theorem 4.1.

The following definition describes a random process to simulate Algorithm 2 using both the witness tree and witness assignment, employing the principle of deferred decisions.

**Definition 4.8** (_M_-truncated process for simulating Algorithm 2 with explicitly identified randomness)**.** Let \(\mathfrak{X}\sim\mu_{\mathcal{C}\backslash\{c_0\}}\) and \(\mathfrak{Y}\sim\mu_\mathcal{C}\) be drawn independently beforehand. Define the random process

\(P^\mathrm{cp}=\{(\mathcal{E}_t,\mathcal{F}_t,\sigma_t,\tau_t,T_t,\varsigma_t)\}_{t\ge 0}\)

starting from the initial state \((\mathcal{E}_0,\mathcal{F}_0,\sigma_0,\tau_0,T_t,\varsigma_t)=(\mathcal{C}\backslash\{c_0\},\mathcal{C},\varnothing,\varnothing,\emptyset,\varnothing)\) as follows:

(1) If \(\mathcal{E}_t^{\sigma_t}=\mathcal{F}_t^{\tau_t}\) or |_V(T<sub>t</sub>_)|=_M_, the process stops, and \((\mathcal{E}_t,\mathcal{F}_t,\sigma_t,\tau_t,T_t,\varsigma_t)\) is the outcome.<tbc>

(2) Otherwise, if \(\mathcal{F}_t^{\tau_t}\nsubseteq\mathcal{E}_t^{\sigma_t}\), let _c_ be the smallest pinned constraint in \(\mathcal{F}_t^{\tau_t}\backslash\mathcal{E}_t^{\sigma_t}\). We then set \((\mathcal{E}_{t+1},\mathcal{F}_{t+1},\sigma_{t+1},\tau_{t+1},T_{t+1},\varsigma_{t+1})\) as<tbc>

<tbc>\(\left\{\begin{array}{ c c }
(\mathcal{E}_t\cup\{c\},\mathcal{F}_t,\sigma_t,\tau_t,T_t,\varsigma_t) & \text{if}c\text{is satisfied by}\mathfrak{X}; \\
\left(\mathcal{E}_t,\mathcal{F}_t,\sigma_t\wedge\mathfrak{X}_{\mathrm{vbl}(c)},\tau_t\wedge\mathfrak{Y}_{\mathrm{vbl}(c)},T_t\oplus c^O,\varsigma_t\wedge\mathfrak{Y}_{\mathrm{vbl}(c)}\right) & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>Here, \(c^O\in\mathcal{C}\) denotes the original unpinned version of _c_, and \(T_t\oplus c^O\) is given in Definition 4.4.<tbc>

(3) Otherwise, if \(\mathcal{F}_t^{\tau_t}\subseteq\mathcal{E}_t^{\sigma_t}\), let _c_ be the smallest pinned constraint in \(\mathcal{E}_t^{\sigma_t}\backslash\mathcal{F}_t^{\tau_t}\). We then set \((\mathcal{E}_{t+1},\mathcal{F}_{t+1},\sigma_{t+1},\tau_{t+1},T_{t+1},\varsigma_{t+1})\) as<tbc>

<tbc>\(\left\{\begin{array}{ c c }
(\mathcal{E}_t,\mathcal{F}_t\cup\{c\},\sigma_t,\tau_t,T_t,\varsigma_t) & \text{if}c\text{is satisfied by}\mathfrak{Y}; \\
\left(\mathcal{E}_t,\mathcal{F}_t,\sigma_t\wedge\mathfrak{X}_{\mathrm{vbl}(c)},\tau_t\wedge\mathfrak{Y}_{\mathrm{vbl}(c)},T_t\oplus c^O,\varsigma_t\wedge\mathfrak{X}_{\mathrm{vbl}(c)}\right) & \text{otherwise.}
\end{array}\right.\)<tbc>

<tbc>Let \(\mu^\mathrm{cp}\) denote the distribution of the outcome \((\mathcal{E}^\mathrm{cp},\mathcal{F}^\mathrm{cp},\sigma^\mathrm{cp},\tau^\mathrm{cp},T^\mathrm{cp},\varsigma^\mathrm{cp})\) of this process, and let \(\mathcal{L}^\mathrm{cp}=\mathrm{supp}(\mu^\mathrm{cp})\) be its support. Let V<sup>cp</sup> denote the set of all possible \((\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\) such that

\(\mathbf{Pr}\left[(\mathcal{E},\mathcal{F},\sigma,\tau,T,\varsigma)\in P^\mathrm{cp}\right]>0.\)

**Remark 4.9** (distinctions between Algorithm 2 and Definition 4.8)**.** We note two main distinctions between Algorithm 2 and Definition 4.8, specifically regarding truncation and the explicitly identified randomness using the principle of deferred decisions. Both aspects are beneficial for our analyses of the coupling and algorithmic applications.

\(\bullet\) In Definition 4.8, the process is truncated once the size of the witness tree reaches the threshold _M_, whereas Algorithm 2 does not incorporate such truncation.<tbc>

\(\bullet\) In Definition 4.8, all randomness utilized by the process _P_<sup>cp</sup> is identified with the two pre- generated random assignments \(\mathfrak{X}\sim\mu_{\mathcal{C}\backslash c_0}\) and \(\mathfrak{Y}\sim\mu_\mathcal{C}\). In contrast, Algorithm 2 generates random choices at the moment they are needed. However, by the principle of deferred decisions, Definition 4.8 still faithfully simulates Algorithm 2 (truncated when the size of the witness tree reaches _M_). Thus, properties we proved for Algorithm 2 (specifically Proposition 4.5 and Lemma 4.7) also hold for the random process constructed in Definition 4.8.<tbc>

