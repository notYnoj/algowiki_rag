## A.2.2 A connected-flow enumerator

Let _A<sub>w,t</sub>(G_) count nonzero flows whose connected support has _w_ edges and _w-t_ vertices. The next bound keeps the excess _t_ explicit.

**Lemma 5.** _For_ \(w\le n/4\)_, set a=w/n and_

\(L_w=w\sqrt{\frac{2qw}{n-w}}.\) (135)

_Then_

\(\mathbb{E}[\mathbf{1}_{\mathcal{A}_n}A_{w,t}]\le\frac{qD}{D-1}(D-1)^we^{(4a+\xi_n)w}\frac{L_w^{2t}}{(2t)!}.\) (136)

_Proof._ Put _s=w-t_. A connected support has flow-space dimension _w-s_+1=_t_+1, so it supports at most _q_<sup>_t_+1</sup> flows. For degrees \(d_1,\dots,d_s\ge 2\) with sum 2_w_, pairing half-edges bounds the number of simple realizations by \((2w-1)!!/\prod_id_i!\). Coefficientwise,

\(\sum_{d\ge 2}\frac{z^d}{d!}\unknown\frac{z^2}{2}e^z,\) (137)

so summing over these degree sequences costs at most

\((2w-1)!!2^{-s}\frac{s^{2t}}{(2t)!}.\) (138)

Apply Lemma 3, including its connected port-labelling bound, to obtain

\(\mathbb{E}[\mathbf{1}_{\mathcal{A}_n}A_{w,t}]\le q^{t+1}D(D-1)^{w-1}\frac{e^{\xi_nw}}{(n-2w)^w}\genfrac(){pt}{2}{n}{w-t}(2w-1)!!2^{-(w-t)}\frac{(w-t)^{2t}}{(2t)!}.\) (139)

We applied the colouring bound only to connected supports; subsequently allowing all pairings merely overcounts them. Now use

\(\frac{\genfrac(){pt}{2}{n}{w-t}}{\genfrac(){pt}{2}{n}{w}}\le\left(\frac{w}{n-w}\right)^t,\frac{\genfrac(){pt}{2}{n}{w}(2w-1)!!2^{-w}}{n^w}\le 1,-\mathrm{log}(1-2a)\le 4a.\) (140)

These inequalities turn (139) into (136).

## A.2.3 The reliability criterion

Write \(R=(D-1)B_\Theta(p)\) and define

\(u=Dp,K=2qu^2,a_*=\frac{4K^{2/3}}{q},\Psi(a)=4a+\sqrt{\frac{2qa}{1-a}},b_0=\frac{1+\mathrm{log}8}{2}.\) (141)

**Proposition 1.** _For fixed p\>_0_, recovery is reliable if_

\(u<\frac{1}{8},a_*\le\frac{1}{4},\mathrm{log}R+\Psi(a_*)<0,\mathrm{log}R+8u+b_0K^{1/3}<0.\) (142)

