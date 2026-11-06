## A The Man-Oriented Gale-Shapley Algorithm

During the course of the algorithm, each person takes one of two states "free" and "engaged". At the beginning, everyone is free and the matching _M_ is initialized to the empty set. At one step of the algorithm, an arbitrary free man _m_ proposes to the top woman _w_ in his current list. If _w_ is free, then _m_ and _w_ are provisionally matched and (_m,w_) is added to _M_. If _w_ is engaged and matched with \(m'\), then _w_ compares _m_ and \(m'\), takes the preferred one, and rejects the other. The rejected man deletes _w_ from the list and becomes (or keeps to be) free. When there is no free man, the matching _M_ is output. The pseudo-code is given in Algorithm 3.

**Algorithm 3** The man-oriented Gale-Shapley algorithm

1: Let \(M:=\emptyset\) and all people be free.

2: **while** there is a free man whose preference list is non-empty **do**

3: Let _m_ be any free man.

4: Let _w_ be the woman at the top of _m_’s (current) list.

5: **if** _w_ is free **then**

6: Let \(M:=M\cup\{(m,w)\}\), and _m_ and _w_ be engaged.

7: **end if**

8: **if** _w_ is engaged **then**

9: Let \(m'\) be _w_’s partner.

10: **if** _w_ prefers \(m'\) to _m_ **then**

11: Delet _w_ from _m_’s list.

12: **else**

13: Let \(M:=M\cup\{(m,w)\}\backslash\{(m',w)\}\).

14: Let \(m'\) be free and _m_ be engaged.

15: Delete _w_ from \(m'\)’s list.

16: **end if**

17: **end if**

18: **end while**

19: Output _M_.

## B Non-Strategy-Proofness of Existing 1.5-approximation Algorithms for MAX SMTI-1TM

Király \[7\] presented a 1.5-approximation algorithm for general MAX SMTI (i.e., ties can appear on both sides). We modify it in the following two respects.

1. Men’s proposals do not get into the 2nd round.

2. When there is arbitrarity, the person with the smallest index is prioritized.

Ideas behind these modifications are as follows: For item 1, since there is no ties in women’s preference lists, executing the 2nd round does not change the result. The role of item 2 is to make the algorithm deterministic, so that the output is a function of an input (as we did in the proof of Lemma 2.1). For completeness, we give a pseudo-code of the algorithm in Algorithm 4. This algorithm is called "New Algorithm" in \[7\], so we abbreviate it as NA here.

