Each person takes one of three states, "free", "engaged", and "semi-engaged". Initially, all the persons are free. At lines 5, 10, and 14, man _m_ proposes to woman _w_. Basically, the procedure is exactly the same as that of MGS. If _w_ is free, then we let \(M:=M\cup\{(m,w)\}\) and both _m_ and _w_ be engaged (we say _w accepts m_). If _w_ is engaged to \(m'\) (i.e., \((m',w)\in M\)) and if \(m\succ_wm'\), then we let \(M:=M\cup\{(m,w)\}\backslash\{(m',w)\}\), _m_ be engaged, and \(m'\) be free. We also delete _w_ from \(m'\)’s preference list (we say _w accepts m_ and _rejects_ \(m'\)). If _w_ is engaged to \(m'\) and \(m'\succ_wm\), then we delete _w_ from _m_’s preference list (we say _w rejects m_).

**Algorithm 4** Király’s New Algorithm (NA) \[7\]

1: Let \(M:=\emptyset\) and all people be free.

2: **while** there is a free man whose preference list is non-empty **do**

3: Among those men, let _m_ be the one with the smallest index.

4: **if** the top of _m_’s current preference list consists of only one woman _w_ **then**

5: Let _m_ propose to _w_.

6: **end if**

7: **if** the top of _m_’s current preference list is a tie **then**

8: **if** all women in the tie are engaged **then**

9: Among those women, let _w_ be the one with the smallest index.

10: Let _m_ propose to _w_.

11: **end if**

12: **if** there is a free woman in the tie **then**

13: Among those free women, let _w_ be the one with the smallest index.

14: Let _m_ propose to _w_.

15: **end if**

16: **end if**

17: **end while**

18: Output _M_.

There is an exception in the acceptance/rejection rule of a woman, when she receives the first and second proposals. This is actually the key for guaranteeing 1.5-approximation, but this rule is not used in the subsequent counter-example so we omit it here. Readers may consult to the original papers for the full description of the algorithm.

It is already proved that the (original) Király’s algorithm always outputs a stable matching and it is a 1.5-approximate solution, and it is not hard to see that the same results hold for the above NA for MAX SMTI-1TM. However, as the example in Figures 5 and 6 shows, it is not a man-strategy-proof mechanism.

If NA is applied to the true preference lists in Figure 5, the obtained matching is {(_m_<sub>2</sub>_,w_<sub>1</sub>),(_m_<sub>3</sub>_,w_<sub>3</sub>),(_m_<sub>4</sub>_,w_<sub>2</sub>)}. Suppose that _m_<sub>1</sub> flips the order of _w_<sub>1</sub> and _w_<sub>2</sub> (Figure 6). This time, NA outputs {(_m_<sub>1</sub>_,w_<sub>2</sub>),(_m_<sub>2</sub>_,w_<sub>3</sub>),(_m_<sub>4</sub>_,w_<sub>1</sub>)} and _m_<sub>1</sub> successfully obtains a partner _w_<sub>2</sub>. By<tbc>

\begin{tabular}{ccccccc}
_m_<sub>1</sub>: & _w_<sub>2</sub> & _w_<sub>1</sub> & _w_<sub>1</sub>: & _m_<sub>2</sub> & _m_<sub>4</sub> & _m_<sub>1</sub> \\
_m_<sub>2</sub>: & (_w_<sub>1</sub> & _w_<sub>3</sub>) & _w_<sub>2</sub>: & _m_<sub>4</sub> & _m_<sub>1</sub> & \\
_m_<sub>3</sub>: & _w_<sub>3</sub> & & _w_<sub>3</sub>: & _m_<sub>2</sub> & _m_<sub>3</sub> & \\
_m_<sub>4</sub>: & _w_<sub>1</sub> & _w_<sub>2</sub> & _w_<sub>4</sub>: & & & \\
\end{tabular}

Figure 5: A counter-example (true lists)

