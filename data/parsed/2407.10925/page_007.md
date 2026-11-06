_x_ is iterated in sequential order, _L_<sub>0,0</sub> first accesses values sequentially within \([0,\dots,2^{2\ell-1})\) and writes out values sequentially within \([0,\dots,2^{2\ell-3})\), and then accesses values sequentially within \((2^{2\ell-1},\dots,0]\) and writes out values sequentially within \((2^{2\ell-2},\dots,2^{2\ell-3}]\).

### 3.4.2 _L_<sub>0,1</sub> and its Recursion _L_<sub>0,1</sub> iterates over string pairs whose first bits do not match. It calculates the second case (_h(a_)=0_,h(b_)=1) from _F_<sub>0</sub> (see (2.9)). This can be accomplished by another simple procedure.

Algorithm 3.2.<br> **Input:** _x_, an interleaved _a_, _b_ string pair<br> **Output:** The new recurrence value for index _x_

