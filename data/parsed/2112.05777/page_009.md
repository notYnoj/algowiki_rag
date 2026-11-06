an original man in _M_<sub>2</sub>, as each original women only prefers original man to agents from the penalizing component in P<sub>2</sub>.

The preferences of the agents in P<sub>1</sub> are as follows. For every \(i\in[n]\), man _m<sub>i</sub>_ has the preferences of \(m'_i\) where each woman \(w'_j\) is replaced by _w<sub>j</sub>_. For every \(i\in[t]\), woman _w<sub>i</sub>_ has the preferences of \(w'_i\) where every man \(m'_j\) is replaced by _m<sub>j</sub>_ and additionally \(m_i^\star\succ\widetilde{m}_1^1\succ\cdots\succ\widetilde{m}_{b+1}^1\) is appended at the end of the preferences of _w<sub>i</sub>_. For every \(i\in[t+1,n]\), woman _w<sub>i</sub>_ has the preferences of \(w'_i\) where every man \(m'_j\) is replaced by _m<sub>j</sub>_ and additionally \(\widetilde{m}_1^1\succ\cdots\succ\widetilde{m}_{b+1}^1\) is appended at the end of the preferences of _w<sub>i</sub>_. The preferences of all other agents are as follows:

\(m_i^\star:w_i,i\in[t];\)<br>
\(\widetilde{m}_i^1:w_1\succ\cdots\succ w_n\succ\widetilde{w}_i^1,i\in[b+1];\)<br>
\(\widetilde{w}_i^{k+1}:\widetilde{m}_i^{k+1},i\in[b+1].\)<br>
\(\widetilde{m}_i^j:\widetilde{w}_1^{j-1}\succ\cdots\succ\widetilde{w}_{b+1}^{j-1}\succ\widetilde{w}_i^j,i\in[b+1],j\in[2,k+1];\)<br>
\(\widetilde{w}_i^j:\widetilde{m}_i^j\succ\widetilde{m}_1^{j+1}\succ\cdots\succ\widetilde{m}_{b+1}^{j+1},i\in[b+1],j\in[k];\)

The preferences of all agents are the same in P<sub>2</sub> as in P<sub>1</sub> except for the women _w_<sub>1</sub>_,...,w<sub>t</sub>_ who all swap down the catch man in their preferences to the last place, i.e., the preferences of _w<sub>i</sub>_ in P<sub>2</sub> arise from the preferences of \(w'_i\) by replacing every man \(m'_j\) by _m<sub>j</sub>_ and appending \(\widetilde{m}_1^1\succ\cdots\succ\widetilde{m}_{b+1}^1\succ m_i^\star\) at the end. Thus, it holds that \(|\mathcal{P}_1\oplus\mathcal{P}_2|=t\cdot(b+1)\). Lastly, we set the matching _M_<sub>1</sub> to:

\(M_1=\{\{m_i,w_j\}|\{m'_i,w'_j\}\in N\}\cup\{\{m_i^\star,w_i\}|i\in[t]\}\cup\{\{\widetilde{m}_i^j,\widetilde{w}_i^j\}|i\in[b+1],j\in[k+1]\}.\)

The matching _M_<sub>1</sub> is stable in P<sub>1</sub>, as _N_ is stable in \(\mathcal{I}'\), each original woman is matched to her catch man which they prefer to all men from the penalizing component, all catch men are matched to their top choice, and the agents in the penalizing component are matched in a stable way.

We now prove that the construction described above is indeed a correct parameterized reduction from LOCAL SEARCH ASM parameterized by _q+t+z_ to IASM parameterized by \(k+b+|\mathcal{P}_1\oplus\mathcal{P}_2|\). The reduction clearly runs in polynomial time and \(k+b+|\mathcal{P}_1\oplus\mathcal{P}_2|=z+q+t+t\cdot(z+1)\), that is, the new parameter combination only depends on the old one. It remains to prove the correctness of the reduction:

\((\Rightarrow):\) Given a matching _N_<sup>∗</sup> of size |_N_|+_t_ with at most _z_ blocking pairs in \(\mathcal{I}'\) and with \(|N\triangle N^*|\le q\), we set matching _M_<sub>2</sub> to be the following:

\(M_2:=\{\{m_i,w_j\}|\{m'_i,w'_j\}\in N^*\}\cup\{\{\widetilde{m}_i^j,\widetilde{w}_i^j\}|i\in[b+1],j\in[k+1]\}\)

Each original woman is matched to an original man and thereby to a man they prefer to their catch man and all men from the penalizing component. As the agents in the penalizing component are matched in a stable way, this implies that all blocking pairs need to involve two original agents and thus that the number of blocking pairs for _M_<sub>2</sub> and _N_<sup>∗</sup> is the same and thus at most _b_. It remains to examine the symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub>. That is \(M_1\triangle M_2=N\triangle N^*\cup\{\{m_i^\star,w_i\}|i\in[t]\}\). Thus, it holds that \(|M_1\triangle M_2|\le q+t\).

\((\Leftarrow):\) Assume that we are given a solution _M_<sub>2</sub> to the constructed IASM instance. We claim that _M_<sub>2</sub> cannot contain a pair involving an original woman and a man from the penalizing component. To prove this, observe that for all \(j\in[k]\) it cannot be the case that there is a woman \(\widetilde{w}_{i^*}^j\) in layer _j_ who is not matched to \(\widetilde{m}_{i^*}^j\) and each man \(\widetilde{m}_i^{j+1}\) is matched to \(\widetilde{w}_i^{j+1}\) for all \(i\in[b+1]\). For the sake of contradiction, assume that this situation occurs. As \(\widetilde{w}_{i^*}^j\) is not matched to \(\widetilde{m}_{i^*}^j\) and also not matched to one of \(\widetilde{m}_1^{j+1},\dots,\widetilde{m}_{b+1}^{j+1}\), she needs to be unmatched. Thus, all _b_+1 men \(\widetilde{m}_1^{j+1},\dots,\widetilde{m}_{b+1}^{j+1}\) form a blocking pair with \(\widetilde{w}_{i^*}^j\) contradicting that _M_<sub>2</sub> admits only at most _b_ blocking pairs. It follows that if a man in some layer _j_ is matched differently in _M_<sub>1</sub> and _M_<sub>2</sub>, then also a man in layer _j_+1 is matched<tbc>

