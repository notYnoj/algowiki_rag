_Proof._ Consider the instance _I_<sub>1</sub> given in Fig. 1, where _m_<sub>3</sub>’s preference list is empty. It is straightforward to verify that _I_<sub>1</sub> has two stable matchings _M_<sub>1</sub>={(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>2</sub>)} and _M_<sub>2</sub>={(_m_<sub>1</sub>_,w_<sub>2</sub>),(_m_<sub>2</sub>_,w_<sub>3</sub>)}, both of which are of maximum size. Hence any stable mechanism must output either _M_<sub>1</sub> or _M_<sub>2</sub>.

First, consider an arbitrary \((2-\epsilon)\)-approximate-stable mechanism _S_ for MAX SMTI that outputs _M_<sub>1</sub> on _I_<sub>1</sub>. Let \(I'_1\) be the instance obtained from _I_<sub>1</sub> by deleting _w_<sub>1</sub> from _m_<sub>1</sub>’s preference list. Then since _M_<sub>2</sub> is still a stable matching for \(I'_1\) and _S_ is a \((2-\epsilon)\)-approximate-stable mechanism, _S_ must output a stable matching of size 2. But since _M_<sub>2</sub> is now the only stable matching of size 2, _S_ outputs _M_<sub>2</sub> on \(I'_1\). Thus _m_<sub>1</sub> can obtain a better partner by manipulating his preference list. Next, consider a \((2-\epsilon)\)-approximate-stable mechanism _S_ that outputs _M_<sub>2</sub> on _I_<sub>1</sub>. Then let \(I''_1\) be the instance obtained from _I_<sub>1</sub> by deleting _w_<sub>3</sub> from _m_<sub>2</sub>’s preference list. By a similar argument, _S_ must output _M_<sub>1</sub> on \(I''_1\) and hence _m_<sub>2</sub> can obtain a better partner by manipulation. We have shown that, for any \((2-\epsilon)\)-approximate-stable mechanism _S_, some man has a successful strategy in _I_<sub>1</sub> and hence _S_ is not a man-strategy-proof mechanism.

Next we use the instance _I_<sub>2</sub> given in Fig. 2, which is symmetric to _I_<sub>1</sub>. By the same argument as above, we can show that for any \((2-\epsilon)\)-approximate-stable mechanism _S_, some woman has a successful strategy in _I_<sub>2</sub> and hence _S_ is not a woman-strategy-proof mechanism.

Therefore, we have shown that any \((2-\epsilon)\)-approximate-stable mechanism is neither a man- strategy-proof mechanism nor a woman-strategy-proof mechanism.

## 3 Results for MAX SMTI-1TM

Recall that, in a MAX SMTI-1TM instance, ties can appear in men’s lists only. Since _I_<sub>2</sub> in the proof of Lemma 2.2 is a MAX SMTI-1TM instance, the second half of the proof applies also to MAX SMTI-1TM. Consequently, together with Lemma 2.1, we have Corollary 1.3.

We then move to man-strategy-proofness and give a proof for Theorem 1.4. We start with the negative part:

**Lemma 3.1** _For any positive_ \(\epsilon\)_, there is no man-strategy-proof_ \((1.5-\epsilon)\)_-approximate-stable mechanism for MAX SMTI-1TM._

_Proof._ The proof goes like that of Lemma 2.2. Consider the instance _I_<sub>3</sub> in Fig. 3. _I_<sub>3</sub> has four matchings of size 3, namely, _M_<sub>3</sub>={(_m_<sub>1</sub>_,w_<sub>1</sub>),(_m_<sub>2</sub>_,w_<sub>2</sub>),(_m_<sub>3</sub>_,w_<sub>3</sub>)},<tbc>

\begin{tabular}{ccccc}
_m_<sub>1</sub>: & _w_<sub>2</sub> & _w_<sub>1</sub> & _w_<sub>1</sub>: & _m_<sub>1</sub> \\
_m_<sub>2</sub>: & _w_<sub>2</sub> & _w_<sub>3</sub> & _w_<sub>2</sub>: & (_m_<sub>1</sub> _m_<sub>2</sub>) \\
_m_<sub>3</sub>: & & & _w_<sub>3</sub>: & _m_<sub>2</sub> \\
\end{tabular}

\begin{tabular}{ccccc}
_m_<sub>1</sub>: & _w_<sub>1</sub> & _w_<sub>1</sub>: & _m_<sub>2</sub> & _m_<sub>1</sub> \\
_m_<sub>2</sub>: & (_w_<sub>1</sub> _w_<sub>2</sub>) & _w_<sub>2</sub>: & _m_<sub>2</sub> & _m_<sub>3</sub> \\
_m_<sub>3</sub>: & _w_<sub>2</sub> & _w_<sub>3</sub>: & & \\
\end{tabular}

Figure 1: A MAX SMTI instance _I_<sub>1</sub>

Figure 2: A MAX SMTI instance _I_<sub>2</sub>

