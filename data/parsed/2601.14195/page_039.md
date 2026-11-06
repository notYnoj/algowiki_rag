where the \(c(t_{i,\gamma}^{r,1})\) entry will be specified later. The construction is illustrated in Figure 12. \(G_{T_{i,\gamma}^r}\) only admits two perfect matchings:<tbc>

\(M_{i,\gamma,r}^1=\{\{t_{i,\gamma}^{r,1},t_{i,\gamma}^{r,2}\},\{t_{i,\gamma}^{r,3},t_{i,\gamma}^{r,4}\},\{t_{i,\gamma}^{r,5},t_{i,\gamma}^{r,6}\},\{t_{i,\gamma}^{r,7},t_{i,\gamma}^{r,8}\},\{t_{i,\gamma}^{r,9},t_{i,\gamma}^{r,10}\},\{t_{i,\gamma}^{r,11},t_{i,\gamma}^{r,12}\}\}\text{and}\)<br>
\(M_{i,\gamma,r}^2=\{\{t_{i,\gamma}^{r,1},t_{i,\gamma}^{r,12}\},\{t_{i,\gamma}^{r,2},t_{i,\gamma}^{r,3}\},\{t_{i,\gamma}^{r,4},t_{i,\gamma}^{r,5}\},\{t_{i,\gamma}^{r,6},t_{i,\gamma}^{r,7}\},\{t_{i,\gamma}^{r,8},t_{i,\gamma}^{r,9}\},\{t_{i,\gamma}^{r,10},t_{i,\gamma}^{r,11}\}\},\)

<tbc>where \(M_{i,\gamma,r}^1\) admits no blocking pairs within the gadget and \(M_{i,\gamma,r}^2\) admits the blocking pair \(\{t_{i,\gamma}^{r,5},t_{i,\gamma}^{r,6}\}\) within the gadget (not counting blocking pairs that may also involve \(c(t_{i,\gamma}^{r,1})\) or \(x_i^r\) entries).

We now connect the gadgets as follows. For each vertex gadget _G<sub>V<sub>i</sub></sub>_, we replace the entry \(c(x_i^r)\) in the preference list of \(x_i^r\) (from the previous construction in the proof of Theorem 4.4) with \(\gamma_*\) many entries \(t_\gamma(x_i^r)\) (for \(1\le\gamma\le\gamma_*\)). Specifically, let \(t_\gamma(x_i^r)=t_{i,\gamma}^{r,7}\). In the construction of \(G_{T_{i,\gamma}^r}\), we already included \(x_i^r\) as the second-ranked entry in the preference list of \(t_{i,\gamma}^{r,7}\). Thus, the edge that previously connected the variable gadget to the clause gadget was replaced by edges that now connect the variable gadget to the \(\gamma_*\) many connector gadgets.

For the links between connector gadgets and clause gadgets, let \(C_j^s\) correspond to the _s_th literal in \(C_j\in C\), which is either an unnegated or a negated occurrence of some variable _V<sub>i</sub>_. Replace each \(x(c_j^s)\) entry from the previous construction in the proof of Theorem 4.4 with \(\gamma_*\) many entries \(t_\gamma(c_j^s)\) (for \(1\le\gamma\le\gamma_*\)). Now, if processing _B_ from left to right, \(C_j^s\) is the

• first unnegated occurrence of _V<sub>i</sub>_, then let \(t_\gamma(c_j^s)=t_{i,\gamma}^{1,1}\) (for all \(1\le\gamma\le\gamma_*\)) and let \(c(t_{i,\gamma}^{1,1})=c_j^s\);<tbc>

• second unnegated occurrence of _V<sub>i</sub>_, then let \(t_\gamma(c_j^s)=t_{i,\gamma}^{2,1}\) (for all \(1\le\gamma\le\gamma_*\)) and let \(c(t_{i,\gamma}^{2,1})=c_j^s\);<tbc>

• first negated occurrence of _V<sub>i</sub>_, then let \(t_\gamma(c_j^s)=t_{i,\gamma}^{3,1}\) (for all \(1\le\gamma\le\gamma_*\)) and let \(c(t_{i,\gamma}^{3,1})=c_j^s\);<tbc>

• second negated occurrence of _V<sub>i</sub>_, then let \(t_\gamma(c_j^s)=t_{i,\gamma}^{4,1}\) (for all \(1\le\gamma\le\gamma_*\)) and let \(c(t_{i,\gamma}^{4,1})=c_j^s\).

Informally, we simply replace the communication edges between the vertex and the clause gadgets in the previous construction with \(\gamma_*\) occurrences of a connector gadget copy in this construction. Lastly, we leave the preference lists of all agents in _A<sub>r</sub>_ (if any exist) empty (essentially discarding them as they can never be matched). This is illustrated in Figure 13.

