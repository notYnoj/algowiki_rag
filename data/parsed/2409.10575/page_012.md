adjustment (_w_<sub>3</sub>_,m_<sub>1</sub>), the refined tie-breaking strategy _S_<sub>3</sub> assigns \(r_{m_1}^*(w_1)>r_{m_1}^*(w_3)\). Consequently, the stable matching _M_<sub>3</sub>={(_m_<sub>1</sub>_,w_<sub>3</sub>),(_m_<sub>2</sub>_,w_<sub>4</sub>),(_m_<sub>3</sub>_,w_<sub>1</sub>),(_m_<sub>4</sub>_,w_<sub>2</sub>)} results in a perfect matching with a size of four.

## 4.3 Obtaining a stable matching

Following the refinement of the tie-breaking strategy, it is necessary to obtain a corresponding stable matching to assess the efficacy of the current strategy. As the preference lists of only a subset of agents are modified during the refinement process, most matching pairs from the previous stable matching can be retained. Rather than reconstructing a stable matching from scratch using the base algorithm, eliminating BPs from the existing matching is generally more efficient. Moreover, rather than re-evaluating the entire set of agents, only a specific subset of agents needs to be examined to identify and eliminate potential BPs. Therefore, we design a BP removal process to effectively identify and eliminate UBPs. However, this process may become trapped in an endless cycle while attempting to obtain a stable matching by removing BPs (Tamura 1993). A time threshold _T_ is established for the BP removal process. If the duration of this process exceeds this threshold, the base algorithm is applied to ensure a stable matching is achieved. The function to obtain a stable matching is described in Algorithm 4. The rest of this section will focus on the BP removal process, where only a specific set of agents is required for examination.

**Proposition 1.** _Given a tie-breaking strategy S_<sub>1</sub> _and its corresponding stable matching M_<sub>1</sub>_. If, after refining the tie-breaking strategy from S_<sub>1</sub> _to S_<sub>2</sub>_, there exist no BPs for the agents in set Q<sub>a</sub> within the current matching M_<sub>1</sub>_, then M_<sub>1</sub> _is also a stable matching corresponding to S_<sub>2</sub>.

_Proof._ Assume, for contradiction, that _M_<sub>1</sub> is not stable under _S_<sub>2</sub>. Then, there exists a BP (_u,w_) under _S_<sub>2</sub>. We consider two cases:

(i). \(u\in Q_a\) **or** \(w\in Q_a\) : Given the conditions, no BPs exist for the agents in _Q<sub>a</sub>_ within _M_<sub>1</sub> under _S_<sub>2</sub>. Thus, this scenario is not possible.<tbc>

(ii). \(u\notin Q_a\) **and** \(w\notin Q_a\) : Since _M_<sub>1</sub> was stable under _S_<sub>1</sub>, and the only change from _S_<sub>1</sub> to _S_<sub>2</sub> involves the agents in _Q<sub>a</sub>_, the stability conditions for agents outside _Q<sub>a</sub>_ remain unaffected. Thus, a BP under _S_<sub>2</sub> for agents not in _Q<sub>a</sub>_ cannot exist.

As both scenarios lead to contradictions, the initial assumption that _M_<sub>1</sub> is not stable under _S_<sub>2</sub> must be incorrect. Therefore, _M_<sub>1</sub> is a stable matching under _S_<sub>2</sub> provided that no BPs exist for the agents in set _Q<sub>a</sub>_.

Given a matching _M_, to remove a BP (_u,w_), we follow these steps. First, if _u_ is full, we disconnect _u_ from its worst partner in _M_. Similarly, if _w_ is full, we disconnect _w_ from its worst partner in _M_. Then, we connect _u_ and _w_.

**Proposition 2.** _Let M_<sub>1</sub> _be a matching with a set B_<sub>1</sub> _of BPs. Removing a BP_ \((u,w)\in B_1\) _results in a new matching M_<sub>2</sub> _and a new set B_<sub>2</sub> _of BPs. Let_ \(w'\) _and_ \(u'\) _be the agents disconnected from u and w, respectively, during this removal process. If no agent is disconnected from u, then_ \(w'\) _is undefined; similarly, if no agent is disconnected from_<tbc>

