The total number of nodes in the character-based graph is |_V<sub>C</sub>_|=_l<sub>x</sub>d<sub>x</sub>+l<sub>y</sub>d<sub>y</sub>_. By the last two desiderata of definition of \(X',Y'\) that, each side of the character based-graph has approximately the same number of nodes:

\(l_xd_x,l_yd_y\approx_{(1\pm\epsilon^\prime)\text{-factor}}|V_C|/2.\) (2)

Similarly, we also have that:

\(max\{l_x,l_y\}min\{d_x,d_y\}\approx_{(1\pm\epsilon^\prime)\text{-factor}}|V_C|/2.\) (3)

The total number of edges in the character-based graph satisfies

\(|E_C|\le l_xl_ymin\{d_x,d_y\},\) (4)

and, by (2),

\(|E_C|\ge l_xl_y\lambda\sqrt{d_xd_y}\approx_{\sqrt{1\pm\epsilon^\prime}\text{-factor}}\sqrt{l_xl_y}\lambda|V_C|/2.\) (5)

By Blakley-Roy inequality (Lemma A.3), the number of walks of length 3 in the character-based graph is at least

\(\#3\text{-walks}\ge|V_C|\cdot\left(2\frac{|E_C|}{|V_C|}\right)^3\)<br>
\(\approx_{(1\pm\epsilon^\prime)^{1.5}\text{-factor}}\lambda^3(l_xl_y)^{1.5}|V_C|.\)

We are interested in the number of 3-walks that are not degenerate. Thus, we need to exclude such degenerate walks from the total count. The number of such walks is upper bounded by

\(\#\text{degenerate}3\text{-walks}\le(max\text{degree of}G_C)\cdot 4|E_C|\)<br>
\(\le max\{l_x,l_y\}\cdot 4(l_xl_ymin\{d_x,d_y\})\) (Eq. (4))<br>
\(\approx_{(1\pm\epsilon^\prime)\text{-factor}}2l_xl_y\cdot|V_C|\) (Eq. (3))

Therefore the ratio of the number of degenerate 3-walks and the total number of 3-walks is bounded

d a b d d
b d b d
d a b d d
b d b d
d a b c a b
d c c d
a b c a b
c d c c d
a b c a b
c d c c d

Figure 4: The graph on the left is an example of the string-based graph and the graph on the right is an example of the character-based graph.

