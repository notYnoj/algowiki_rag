<tbc>contributes to more output strings. Throughout, we fix the switching order _t_, an integer with \(0\le t\le m\). The boxes will collect the leaves of order at least _t_, i.e., the leaves that choose _P_<sub>0</sub> at most _m-t_ times, and a query will read the leaves of order below _t_ one by one (Section 4.3).

Before giving the formal definition, we describe the idea informally and give some examples. Consider an output string _w_ with inner set _Q_, and a leaf \(\tau\) of order at least _t_ contributing to _w_. To find the box of \(\tau\), we look at the levels of _Q_ one at a time, from the highest down, and we stop as soon as we have seen _t_ levels at which \(\tau\) chooses a term other than _P_<sub>0</sub>. The box of \(\tau\) then agrees with \(\tau\) everywhere, except that it has a star at every level of _Q_ below the level where we stopped. For instance, let _m_=4 and _t_=2 as in Figure 10, and suppose that \(\tau\) chooses the terms _P_<sub>12</sub>_,P_<sub>0</sub>_,P_<sub>31</sub>_,P_<sub>22</sub> at the four levels \(\ell_1<\ell_2<\ell_3<\ell_4\) of _Q_. We see _P_<sub>22</sub> at level \(\ell_4\) and _P_<sub>31</sub> at level \(\ell_3\), and we stop there, so the box of \(\tau\) is ∗∗_P_<sub>31</sub>_P_<sub>22</sub> (in the first row of the figure). This box contains \(\tau\) along with the 99 other leaves that differ from \(\tau\) only at the levels \(\ell_1\) and \(\ell_2\). Similarly, for a leaf that chooses the terms _P_<sub>0</sub>_,P_<sub>23</sub>_,P_<sub>0</sub>_,P_<sub>11</sub>, we stop at level \(\ell_2\), so its box is ∗_P_<sub>23</sub>_P_<sub>0</sub>_P_<sub>11</sub> (in the second row of the figure). Since a box has stars at the levels that we did not reach, it contains many leaves. Moreover, although we described the box of \(\tau\) in terms of _w_, the definition of a box below does not refer to an output string, and the same box serves many output strings.

A **_box_** is a cube \(\pi=\pi_1\cdots\pi_L\) such that (i) at most _m-t_ of its symbols are _P_<sub>0</sub> or stars, and (ii) every star is at a lower level than every _P_<sub>0</sub>. That is, the symbols _P_<sub>0</sub> and stars of a box, read in increasing order of the levels, are<tbc>

\(\underbrace{*\cdots*}_e\underbrace{P_0P_0\cdots P_0}_{f-e}\text{for some}0\le e\le f\le m-t,\)

<tbc>and its other _L-f_ symbols are among the nine terms _P<sub>ij</sub>_. A leaf of \(\pi\) chooses _P_<sub>0</sub> at the _f-e_ levels where \(\pi\) has _P_<sub>0</sub> and possibly at some of its _e_ star levels, and hence at most \(f\le m-t\)<tbc>

V
l1
l2
l3
l4
sets Z of its leaves leaves per box
{l1,l2}
*
*
Pij
Pij
Ø, {l1}, {l2}, {l1,l2}
102
{l1,l3}
*
Pij
Po
Pij
{l3}, {l1,l3}
10
{l1,l4}
*
Pij
Pij
Po
{l4}, {l1,l4}
10
{l2,l3}
Pij
Po
Po
Pij
{l2,l3}
1
{l2,l4}
Pij
Po
Pij
Po
{l2,l4}
1
{l3,l4}
Pij
Pij
Po
Po
{l3,l4}
1

Figure 10: The boxes of an output string _w_ for _m_=4 and _t_=2, drawn at the four levels \(\ell_1<\ell_2<\ell_3<\ell_4\) of its inner set _Q_ (at every other level, they have the term of the private leaf of _w_). Here _P<sub>ij</sub>_ stands for one of the nine terms other than _P_<sub>0</sub>, and ∗ for all ten terms. Each row is one of the six sets _V_ of _m-t_=2 levels and stands for the 9_<sup>t</sup>_=81 boxes of B_<sub>V</sub>_, one for each choice of the two terms _P<sub>ij</sub>_. Read from right to left, a row stops at its second _P<sub>ij</sub>_, and the levels to the left of it, those of _F<sub>V</sub>_, carry stars. On the right are the sets _Z_ of levels at which the leaves of such a box choose _P_<sub>0</sub>, and the number 10<sup>|_F<sub>V</sub>_|</sup> of its leaves. Every set _Z_ of at most two levels appears in exactly one row (Lemma 27), so these \(6\cdot 81=486=\alpha_2\) boxes contain each of the \(\alpha_2+\alpha_3+\alpha_4=9963\) leaves of order at least 2 contributing to _w_ exactly once.

