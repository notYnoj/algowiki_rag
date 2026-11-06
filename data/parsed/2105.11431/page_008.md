<tbc>of each type. Therefore, if one chooses a diagonal uniformly at random the probability that it is unoccupied is approximately 1/2. If we fix (_r,c_) and choose \((x,y)\in Q(T)\) uniformly at random, we might imagine that the (four) diagonals containing (_r,y_) and (_x,c_) are distributed uniformly at random, which would imply that with constant probability they are unoccupied.

One approach to proving Lemma 4.3 is to track |B<sub>_Q(t_)</sub>(_r,c_)| for each \((r,c)\in[n]^2\) and each \(0\le t\le T\). This would give a precise count of |B<sub>_Q(t_)</sub>(_r,c_)| but at the cost of significant technical work. We take a different tack, giving a shorter proof at the expense of a suboptimal \(\beta\). We show that already at an early stage of the process w.h.p. there are \(\Omega(n)\) absorbers for each position. Furthermore, each of these absorbers is guaranteed to be present in _Q(T_). We begin by identifying a combinatorial property that ensures an absorber survives throughout the random greedy process.

We will need the following notation: Let \((r,c)\in[n]^2\). Let \(\ell_1^\mathrm{tor}(r,c):=\{(x,y)\in[n]^2:r+c=x+y\mathrm{mod}n\},\ell_2^\mathrm{tor}(r,c):=\{(x,y)\in[n]^2:r-c=x-y\mathrm{mod}n\}\) be the two toroidal diagonals incident to (_r,c_), and let \(\ell_1(r,c)\subseteq\ell_1^\mathrm{tor}(r,c),\ell_2(r,c)\subseteq\ell_2^\mathrm{tor}(r,c)\) be the two non-toroidal diagonals incident to (_r,c_). For _i_=1,2 we also define \(\ell_i^\mathrm{far}(r,c):=\ell_i^\mathrm{tor}(r,c)\backslash\ell_i(r,c)\).

**Definition 4.4.** Let \(Q\subseteq[n]^2\) be a partial _n_-queens configuration. Let \((r,c)\in[n]^2\). An absorber \((x,y)\in\mathcal{B}_Q(r,c)\) is **safe** if the four toroidal diagonals containing (_r,y_) and (_x,c_) are all occupied by _Q_. Equivalently, \((x,y)\in\mathcal{B}_Q(r,c)\) is safe if there exist \(a_1\in\ell_1^\mathrm{far}(r,y),a_2\in\ell_2^\mathrm{far}(r,y),b_1\in\ell_1^\mathrm{far}(x,c),b_2\in\ell_2^\mathrm{far}(x,c)\) such that \(a_1,a_2,b_1,b_2\in Q\). (see Figure 1).

More generally, if \(R\subseteq[n]^2\) (i.e., _R_ is not necessarily a partial queens configurations) and \((r,c)\in[n]^2\), we say that \((x,y)\in R\) is a safe absorber for (_r,c_) if (_x,y_) does not share a diagonal with (_r,c_), there exist \(a_1\in\ell_1^\mathrm{far}(r,y),a_2\in\ell_2^\mathrm{far}(r,y),b_1\in\ell_1^\mathrm{far}(x,c),b_2\in\ell_2^\mathrm{far}(x,c)\) such that \((x,y),a_1,a_2,b_1,b_2\in R\) and no other element of _R_ shares a line with any of \((x,y),a_1,a_2,b_1,b_2\in R\).

We denote the set of safe absorbers for (_r,c_) in _R_ by S_<sub>R</sub>(r,c_).

The crucial property of safe absorbers is the following.

_Observation_ 4.5. Let \(Q_1\subseteq Q_2\subseteq[n]^2\) be partial toroidal _n_-queens configurations. Then, for every \((r,c)\in[n]^2\), it holds that \(\mathcal{S}_{Q_1}(r,c)\subseteq\mathcal{S}_{Q_2}(r,c)\).

_Proof._ Since _Q_<sub>2</sub> is a partial toroidal _n_-queens configuration, every toroidal diagonal contains at most a single queen. Since \(Q_1\subseteq Q_2\), if a toroidal diagonal is occupied in _Q_<sub>1</sub> then it will contain no additional queens in _Q_<sub>2</sub>.

Let \((r,c)\in[n]^2\) and suppose \((x,y)\in\mathcal{S}_{Q_1}(r,c)\). Then, by definition, the toroidal diagonals incident to (_r,y_) and (_x,c_) are occupied in _Q_<sub>1</sub>, while the (non-toroidal) diagonals incident with these positions are unoccupied. Hence, this remains so in _Q_<sub>2</sub> as well, implying \((x,y)\in\mathcal{S}_{Q_2}(r,c)\). □

In order to prove Lemma 4.3 we will show that for some \(0\le t\le T\), _Q(t_) contains \(\Omega(n)\) safe absorbers for every \((r,c)\in[n]^2\). In order to gain a heuristic understanding we consider the situation in a random binomial subset of \[_n_\]<sup>2</sup>. This calculation will also be used in the proof of Lemma 4.3.

