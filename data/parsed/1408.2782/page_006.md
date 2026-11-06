**Algorithm 1 ProposalRound**(_Q,k,A_)

**Step 1:** Each man _m_ proposes to all women in _A<sup>m</sup>_ by sending each \(w\in A\) the message PROPOSE.

**Step 2:** Each women _w_ receiving proposals responds with the message ACCEPT to all proposals from her most preferred quantile \(Q_i^w\) from which at least one man proposed in Step 1.

**Step 3:** Let _G_<sub>0</sub> denote the bipartite graph _G_<sub>0</sub> of accepted proposals from Step 2. The players compute a maximal matching _M_<sub>0</sub> in _G_<sub>0</sub>, using **MaximalMatching**(_G_<sub>0</sub>), storing their match in _G_<sub>0</sub> as _p_<sub>0</sub>.

**Step 4:** Each woman _w_ matched in _M_<sub>0</sub> sends REJECT to all men \(m\in Q^w\) in a lesser or equal quantile to her partner _p_<sub>0</sub>(_w_) in _M_<sub>0</sub> other than _p_<sub>0</sub>(_w_). She then removes all of these men from _Q<sup>w</sup>_ and the corresponding \(Q_i^w\). The matched women then set \(p\leftarrow p_0\), so the partial matching _M_ now contains the edge (_p_<sub>0</sub>(_w),w_). Any man _m_ matched in _M_<sub>0</sub> sets \(p\leftarrow p_0\) and sets \(A\leftarrow\varnothing\).

**Step 5:** The men remove all _w_ from whom they received the message REJECT from their preferences _Q_, the various _Q<sub>i</sub>_ and _A_. If a man _m_ receives a rejection from his match _p(m_) from a previous round, he sets \(p\leftarrow\varnothing\).

Computing a maximal matching is trivial, as the accepted proposals already form a matching. The general case has one crucial feature in common with the Gale-Shapley algorithm, which follows immediately from the description of **ProposalRound**.

**Lemma 3.1** (Monotonicity)**.** Once a woman _w_ has \(p(w)\neq\varnothing\) in some execution of **ProposalRound**, she is guaranteed to always have \(p(w)\neq\varnothing\) after each subsequent execution of **ProposalRound**. Further, once matched, she will only accept proposals from men in a strictly higher quantile than her current match, _p(w_).

## 3.3 The QuantileMatch subroutine

Here we describe the **QuantileMatch** subroutine (Algorithm 2), which simply iterates **ProposalRound** until each man _m_ has either been rejected by all women in _A<sup>m</sup>_ or is matched with some woman in _A<sup>m</sup>_. In either case, \(A^m=\varnothing\) when **QuantileMatch** terminates. We will argue that _k_ (the number of quantiles) iterations suffice.

**Algorithm 2 QuantileMatch**(_Q,k_)

\(i\leftarrow min\{i|Q_i\neq\varnothing\}\cup\{k\}\) (male only)

**if** \(p=\varnothing\) **then**

\(A\leftarrow Q_i\) (male only)

**end if**

**for** \(i\leftarrow 1\) to _k_ **do**

**ProposalRound**(_Q,k,A_)

**end for**

**Lemma 3.2** (**QuantileMatch** guarantee)**.** At the termination of **QuantileMatch**(_Q,k_) every man _m_ satisfies \(A^m=\varnothing\). In particular, each man who had \(A^m\neq\varnothing\) before the first iteration of the loop in **QuantileMatch** has either been rejected by all women in _A<sup>m</sup>_ or is matched with some woman in _A<sup>m</sup>_.

