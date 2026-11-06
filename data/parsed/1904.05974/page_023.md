We will now describe the preference lists of vertices in a negative clause _k_--the overall picture here (see Fig. 8) will be the _mirror image_ of a clause gadget with 2 positive literals. For a gadget \(D_k=\neg x\unknown\neg y\), we have:

\(u_k:d_x\succ v_ku'_k:dy\succ v'_k\)<br>
\(v_k:u_k\succ c_yv'_k:u'_k\succ t\)

We describe below the preference lists of the 4 vertices \(c_x,d_x,c'_x,d'_x\) that occur in the first literal gadget in the clause _D<sub>k</sub>_, which is \(\neg x\)’s (unique) gadget.

\(c_x:d_x\succ\underline{b_{x,i}}\succ\underline{b_{x,j}}\succ\cdots\succ\underline{b_{x,\ell}}\succ d'_x\succ sc'_x:d'_x\succ d_x\)<br>
\(d_x:c'_x\succ u_k\succ c_xd'_x:\underline{a'_{x,i}}\succ\underline{a'_{x,j}}\succ\cdots\succ\underline{a'_{x,\ell}}\succ c_x\succ c'_x\)

The underlined vertices \(b_{x,i},b_{x,j},\dots,b_{x,\ell}\) in _c<sub>x</sub>_’s preference list are the _b_-vertices in the _x_-gadgets in various clauses. The order among these vertices in _c<sub>x</sub>_’s preference list is not important. Similarly, \(a'_{x,i},a'_{x,j},\dots,a'_{x,\ell}\) in \(d'_x\)’s preference list are the \(a'\)-vertices in the gadgets of _x_ that occur in various clauses and the order among these is not important.

We describe next the preference lists of the 4 vertices \(c_y,d_y,c'_y,d'_y\) that occur in the second literal gadget in _D<sub>k</sub>_, which is \(\neg y\)’s (unique) gadget.

\(c_y:v_k\succ dy\succ\underline{b_{y,i^\prime}}\succ\underline{b_{y,j^\prime}}\succ\cdots\succ\underline{b_{y,\ell^\prime}}\succ d'_yc'_y:d'_y\succ dy\)<br>
\(dy:c'_y\succ u'_k\succ c_yd'_y:\underline{a'_{y,i^\prime}}\succ\underline{a'_{y,j^\prime}}\succ\cdots\succ\underline{a'_{y,\ell^\prime}}\succ c_y\succ c'_y\)

**Edge Costs.** For each edge _e_ in \(G_\psi\), we will set \(\mathsf{cost}(e)\in\{0,1\}\).

Cx
dx
uk
Vk
Cy
dy
uk
V'k
S
t
d'x
C'x
d'y
C'y

Vel
ar
br
u'el
S
cr
dr
uk
b'r
a'r
d'r
C'r

**Fig.8.** A clause gadget corresponding to a negative clause \(D_k=\neg x\unknown\neg y\): every negative clause has only 2 literals.

**Fig.9.** A gadget corresponding to a positive literal (left) and to a negative literal (right) of a variable _r_. We use \(c_r,d_r,c'_r,d'_r\) to denote the 4 vertices in the negative gadget of _r_ (there is a unique clause with \(\neg r\)). For the sake of convenience, we use \(a_r,b_r,a'_r,b'_r\) to denote the 4 vertices in the positive gadget of _r_ in the \(\ell\)-th clause. Dashed edges have cost 1 and solid edges have cost 0.

