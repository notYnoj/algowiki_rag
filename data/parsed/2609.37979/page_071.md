\(\chi_\infty^G(z)=D\): for \(u\in V_1\), take \(z=\sigma(r_C)\); for \(u\in V_2\), use Neighborhood Preservation. Since \(\sigma\) wins from _r<sub>C</sub>_ with energy _H(C_), we have \(h(r_C)+w(u,v)\ge h(z)\) and therefore \(w(u,v)\ge H(D)-H(C)\).

Now fix any initial vertex _v_<sub>0</sub> and energy \(E_0\ge h(v_0)\), and consider any resulting infinite walk \(\pi=v_0v_1v_2\dots\) consistent with \(\widehat{\sigma}\). Applying the preceding inequality to each edge (_v<sub>k</sub>,v_<sub>_k_+1</sub>) yields a telescoping sum

\(E_k=E_0+\sum_{j=0}^{k-1}w(v_j,v_{j+1})\ge H(\chi_\infty^G(v_k))\ge 0\text{for all}k\ge 0.\)

Hence \(\widehat{\sigma}\) is optimal from every starting vertex and has the required consistency property. The construction of \(\widehat{\sigma}\) takes linear time.

## A.2 More Games on Graphs

We have shown in Section 7 that Energy Game can be solved efficiently in the Isomorphic-Priors model using the 1-WL algorithm. In the following, we extend them to more general games.

**Definition A.1** (Value-determined Game)**.** An instance of Value-determined Game is defined by a tuple \(G=(V,E,V_1,V_2,V_r,\delta,w,v_0,W,p)\), where

• (_V,E_) is a finite directed graph with no terminal states,<tbc>

• (_V_<sub>1</sub>_,V_<sub>2</sub>_,V<sub>r</sub>_) is a partition of _V_ , where Player 1 controls _V_<sub>1</sub>, Player 2 controls _V_<sub>2</sub>, and _V<sub>r</sub>_ are random nodes,<tbc>

• \(\delta\) is a transition probability function for random nodes: for each \(u\in V_r\), \(\delta(u)\) is a probability distribution over \(Succ(u)=\{v|(u,v)\in E\}\).<tbc>

• \(w:V\rightarrow\Sigma\) is a label function.<tbc>

• _v_<sub>0</sub> is the designated initial vertex.<tbc>

• \(W\subseteq\Sigma^\omega\) is the Borel objective for Player 1.<tbc>

• \(p\in[0,1]\) is a probability threshold.

A play \(\pi=v_0v_1v_2\dots\) is formed by moving a token: at step \(k\ge 0\), if \(v_k\in V_i,i\in\{1,2\}\), Player _i_ chooses an outgoing edge \((v_k,v_{k+1})\in E\) and moves the token to _v_<sub>_k_+1</sub>; if \(v_k\in V_r\), then the arena samples a node _v_<sub>_k_+1</sub> from \(\delta(v_k)\), and moves the token to _v_<sub>_k_+1</sub>. We slightly abuse the label function by denoting \(w(\pi):=w(v_0)w(v_1)w(v_2)\dots\). We denote \(\pi(\sigma,\tau)\) as the (randomized) play where Player 1 uses strategy \(\sigma\) and Player 2 uses strategy \(\tau\). We say

• Player 1 wins the game from _v_<sub>0</sub> if \(sup_\sigma inf_\tau Pr(w(\pi(\sigma,\tau))\in W)\ge p\),<tbc>

• Player 2 wins the game from _v_<sub>0</sub> if \(inf_\tau sup_\sigma Pr(w(\pi(\sigma,\tau))\in W)<p\).

The game is value-determined, if \(sup_\sigma inf_\tau Pr(w(\pi(\sigma,\tau))\in W)=inf_\tau sup_\sigma Pr(w(\pi(\sigma,\tau))\in W)\), which means that exactly one of the Players wins. For a value-determined game _G_, we define _OPT(G_)=YES if Player 1 wins from _v_<sub>0</sub>, and _OPT(G_)=NO otherwise.

We view a value-determined game as an attributed directed graph in the sense of Section 5. All instance-specific information can be encoded using vertex and edge attributes. In particular, the threshold _p_, which is a global parameter of the instance, can be encoded by including _p_ in the attribute of every vertex. We regard the Borel objective _W_ as a fixed global parameter. Thus, Value-determined Game fits the model of 5.

