## Appendix: A Worked Example of the Fingerprint-Container and Palette Algorithms

**Fingerprint and Container Generation** ( \[7, 19\]).<br>
**Input:** A graph _H_=(_V,E_), an independent set \(I\subseteq V\) , and a fixed vertex order for tie-breaking.<br>
**Output:** Fingerprints _F_<sub>1</sub>_,...,F_<sub>|_I_|</sub> and containers _C_<sub>1</sub>_,...,C_<sub>|_I_|</sub>.<tbc>

1. \(F_0\leftarrow\varnothing\); \(C_0\leftarrow V\) .<tbc>

2. **for** _t_=1,2_,...,|I_| **do**<tbc>

3. Choose \(f_t\in I\backslash F_{t-1}\) with maximum degree in _H_\[_C_<sub>_t_-1</sub>\], breaking ties by the fixed order.<tbc>

4. \(X_t\leftarrow\{w\in C_{t-1}:deg_{H[C_{t-1}]}(w)>deg_{H[C_{t-1}]}(f_t)\}\).<tbc>

5. \(Y_t\leftarrow N_H(f_t)\cap C_{t-1}\).<tbc>

6. \(F_t\leftarrow F_{t-1}\cup\{f_t\}\).<tbc>

7. \(C_t\leftarrow C_{t-1}\backslash(X_t\cup Y_t)\).<tbc>

8. **end for**<tbc>

9. **return** (_F_<sub>1</sub>_,C_<sub>1</sub>)_,...,(F_<sub>|_I_|</sub>_,C_<sub>|_I_|</sub>).

We give a concrete example illustrating both the fingerprint-container algorithm of \[7, 19\] and our palette algorithm. The example is a 3-coloring instance on a graph _G_. Here _k_=3: the auxiliary graph is the triplicate construction _H=K_<sub>3</sub>∗_G_, where each vertex _u_ of the original bipartite graph _G_ is replicated into three copies _u_<sub>1</sub>_,u_<sub>2</sub>_,u_<sub>3</sub> forming a triangle. The original graph _G_ has vertex set \(\{a,b,c,v,x,y\}\cup\{w,r,s,t\}\) and edge set

\(E(G)=\{vw,vr,vs,vt,yr,ys,xr,wa,wb,wc\}.\)

**Figure 1** and **Figure 2** show the base graph _G_ together with the resulting graph _H_ obtained by the triplicate construction.

We first illustrate the first two rounds of our palette process on this graph. Let _A_={_v,x,y_}, and fix the total order so that _x_ precedes _y_. Initially every palette is \[3\], so the first pivot is _f_<sub>1</sub>=_v_, whose degree in _G_ is larger than those of _x_ and _y_. Choose any prescribed color \(i_1\in[3]\) for _v_. In the update from _P_<sup>1</sup> to _Q_<sup>1</sup>, color _i_<sub>1</sub> is deleted from the palettes of _w,r,s,t_. At the start of round 2, both _x_ and _y_ have minimum palette-degree 0 (consider color _i_<sub>1</sub>). Thus the tie-breaking order selects _f_<sub>2</sub>=_x_ and _D_<sub>2</sub>=0. In forming _P_<sup>2</sup>, the vertices _w,r,s_ have positive minimum palette-degree (respectively 3,2,1), so their palettes are emptied. In particular, _P_<sup>2</sup>(_x_)=\[3\], so the second prescribed color _i_<sub>2</sub> may be any of 1,2,3.

a
b
c
v
x
y
w
r
s
t

Figure 1: The original bipartite graph _G_.

