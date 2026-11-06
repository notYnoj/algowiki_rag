<tbc>_M_<sub>4</sub>={(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>2</sub>),(_m_<sub>3</sub>_,w_<sub>4</sub>)}, _M_<sub>5</sub>={(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>3</sub>),(_m_<sub>3</sub>_,w_<sub>4</sub>)}, and _M_<sub>6</sub>={(_m_<sub>1</sub>_,w_<sub>2</sub>),(_m_<sub>2</sub>_,w_<sub>3</sub>),(_m_<sub>3</sub>_,w_<sub>4</sub>)}. Among them, _M_<sub>3</sub> and _M_<sub>6</sub> are stable (_M_<sub>4</sub> is blocked by (_m_<sub>3</sub>_,w_<sub>3</sub>) and _M_<sub>5</sub> is blocked by (_m_<sub>1</sub>_,w_<sub>2</sub>)). Hence any \((1.5-\epsilon)\)-approximate-stable mechanism outputs either _M_<sub>3</sub> or _M_<sub>6</sub>, since a stable matching of size 2 is not a \((1.5-\epsilon)\)-approximate solution.

Consider an arbitrary \((1.5-\epsilon)\)-approximate-stable mechanism _S_ for MAX SMTI-1TM, and suppose that _S_ outputs _M_<sub>3</sub> on _I_<sub>3</sub>. Then if _m_<sub>1</sub> deletes _w_<sub>1</sub> from the list, _M_<sub>6</sub> is the unique maximum stable matching (of size 3); hence _S_ must output _M_<sub>6</sub> and so _m_<sub>1</sub> can obtain a better partner _w_<sub>2</sub>. Similarly, if _S_ outputs _M_<sub>6</sub> on _I_<sub>3</sub>, _m_<sub>3</sub> can force _S_ to output _M_<sub>3</sub> by deleting _w_<sub>4</sub> from the list. In either case, some man has a successful strategy in _I_<sub>3</sub> and hence _S_ is not a man-strategy-proof mechanism.

Finally, we give a proof for the positive part, which is the main result of this paper.

**Lemma 3.2** _There exists a man-strategy-proof_ 1.5_-approximate-stable mechanism for MAX SMTI-1TM._

_Proof._ We give Algorithm 1 and show that it is a man-strategy-proof 1.5-approximate-stable mechanism by three subsequent lemmas (Lemmas 3.3-3.5). Algorithm 1 first translates an SMTI-1TM instance _I_ to an SMI instance \(I'\) using Algorithm 2, then applies MGS to \(I'\) and obtains a matching \(M'\), and finally constructs a matching _M_ of _I_ from \(M'\). It is worth noting that a man _b<sub>j</sub>_ created at Step 2 of Algorithm 2 corresponds to a woman (not a man) of _I_. As will be seen later, _b<sub>j</sub>_ is definitely matched with _s<sub>j</sub>_ or _t<sub>j</sub>_ in \(M'\), and the other woman (i.e., either _s<sub>j</sub>_ or _t<sub>j</sub>_ who is not matched with _b<sub>j</sub>_) plays a role of woman _w<sub>j</sub>_ of _I_: If she is single in \(M'\), then _w<sub>j</sub>_ is single in _M_. If she is matched with _a<sub>i</sub>_ in \(M'\), then _w<sub>j</sub>_ is matched with _m<sub>i</sub>_ in _M_.

**Algorithm 1** An algorithm for MAX SMTI-1TM

**Input:** An instance _I_ for MAX SMTI-1TM.

**Output:** A matching _M_ for _I_.

1: Construct an SMI instance \(I'\) from _I_ using Algorithm 2.

2: Apply MGS to \(I'\) and obtain a matching \(M'\).

3: Let \(M:=\{(m_i,w_j)|(a_i,s_j)\in M'\vee(a_i,t_j)\in M'\}\) and output _M_.

Now we start formal proofs for the correctness.

**Lemma 3.3** _Algorithm 1 always outputs a stable matching._

_Proof._ Let _M_ be the output of Algorithm 1 and \(M'\) be the matching obtained at Step 2 of Algorithm 1. We first show that _M_ is a matching. Since \(M'\) is a matching, _a<sub>i</sub>_ appears at most once in \(M'\), so _m<sub>i</sub>_ appears at most once in _M_. Observe that _b<sub>j</sub>_ is matched in \(M'\), as otherwise<tbc>

\begin{tabular}{ccccc}
_m_<sub>1</sub>: & _w_<sub>2</sub> & _w_<sub>1</sub> & _w_<sub>1</sub>: & _m_<sub>1</sub> \\
_m_<sub>2</sub>: & (_w_<sub>2</sub> & _w_<sub>3</sub>) & _w_<sub>2</sub>: & _m_<sub>2</sub> & _m_<sub>1</sub> \\
_m_<sub>3</sub>: & _w_<sub>3</sub> & _w_<sub>4</sub> & _w_<sub>3</sub>: & _m_<sub>2</sub> & _m_<sub>3</sub> \\
_m_<sub>4</sub>: & & & _w_<sub>4</sub>: & _m_<sub>3</sub> \\
\end{tabular}

Figure 3: A MAX SMTI-1TM instance _I_<sub>3</sub>

