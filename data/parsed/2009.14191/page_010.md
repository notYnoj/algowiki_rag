## 3.2.2 Proof of the forward direction

We show how to construct a stable matching from a solution to a 1-in-3 Positive 3-Occurrence- SAT instance.

**Lemma 3.2.** _Let_ \(f:\{x_i\}\rightarrow\{\mathtt{true},\mathtt{false}\}\) _be a solution to the_ 1-in-3 Positive 3-Occurrence- SAT _instance_ I_. Then_ \(\mathcal{I}'\) _admits a stable matching._

_Proof._ We construct a stable matching _M_ as follows. We start with \(M=\emptyset\).

Denote by \(S:=\{i\in[n]:f(x_i)=\mathtt{true}\}\) the set of indices such that the corresponding variables are set to `true` by truth assignment _f_.

For a clause _c<sub>j</sub>_, let \(y_j^{\ell_j}\) be the the variable in _c<sub>j</sub>_ set to `true` by _f_. For each \(j\in[m]\), we add the 3-set \(\{c_j,d_j,y_j^{\ell_j}\}\) to _M_. For all \(i\in[n]\backslash S\), we add the 3-set \(\{x_i^1,x_i^2,x_i^3\}\) to _M_. Finally, for each pair \((i,k)\in[n]\times[3]\), we add the 3-sets \(\{z_i^{k,1},z_i^{k,2},z_i^{k,3}\}\) and \(\{z_i^{k,4},z_i^{k,5},z_i^{k,6}\}\).

Since _f_ assigns exactly one true variable to each clause, _M_ is indeed a matching. It remains to show that _M_ is stable. We do so by showing for each agent that it is not contained in a blocking 3-set.

**Claim 1.** _For all_ \(j\le m\)_, neither c<sub>j</sub> nor d<sub>j</sub> is contained in a blocking 3-set._

### Proof of Claim:

We prove the claim by induction on _j_. For _j_=0, there is nothing to show, as there are no agents _c_<sub>0</sub> or _d_<sub>0</sub>.

For the induction step, first note that we can ignore all 2-sets containing an agent _c<sub>p</sub>_ or _d<sub>p</sub>_ for some _p\<j_, as we already know that they are not contained in a blocking 3-set. Thus, we consider the sublist \(\mathrm{ML}'\) of ML arising by deleting all such 2-sets. The first 2-set of \(\mathrm{ML}'\) is {_c<sub>j</sub>,d<sub>j</sub>_}. Let \(y_j^{\ell_j}=x_i^k\) such that \(\{c_j,d_j,y_j^\ell\}\in M\). The variable \(y_j^{\ell_j}\) is not contained in any blocking 3-set, as it is matched to the first 2-set of sublist \(\mathrm{ML}'\). If _c<sub>j</sub>_ is contained in a blocking 3-set, then the blocking 3-set is \(\{c_j,y_j^p,d_j\}\) for some \(p<\ell_j\), as \(\{y_j^p,d_j\}\) for \(p<\ell_j\) are the only 2-sets _c<sub>j</sub>_ prefers to \(\{y_j^\ell,d_j\}\). However, _d<sub>j</sub>_ does not prefer \(\{y_j^p,c_j\}\) to \(\{y_j^\ell,c_j\}\), and thus, \(\{c_j,y_j^p,d_j\}\) is not a blocking 3-set. By symmetric arguments, _d<sub>j</sub>_ also cannot be contained in a blocking 3-set.

**Claim 2.** _No agent_ \(x_i^k\) _or_ \(z_i^{k,p}\) _for_ \(i\le n\), \(k\in[3]\) _and_ \(p\in[6]\) _is contained in a blocking 3-set._

### Proof of Claim:

We prove the claim by induction on _i_. For _i_=0, there is nothing to show.

Note that all 2-sets from \(\bigcup_{\ell\in[m]}\mathcal{A}_\ell\) contain an agent of the type \(c_\ell\) or \(d_\ell\), and thus, no blocking 3-set contains a 2-set from \(\bigcup_{\ell\in[m]}\mathcal{A}_\ell\) by Claim 1. Furthermore, by the induction hypothesis, no 2-set from C_<sub>q</sub>_ for _q\<i_ can be contained in a blocking 3-set. Thus, it is enough to consider the sublist ML_<sub>i</sub>_ of the master list arising through the deletion of A_<sub>j</sub>_ for all \(j\in[m]\) and C_<sub>q</sub>_ for _q\<i_.

If _x<sub>i</sub>_ is set to `true`, then all agents \(x_i^k\) are matched better than any 2-set from ML_<sub>i</sub>_, and thus, cannot be part of a blocking 3-set. Otherwise, all of \(x_i^1\), \(x_i^2\), and \(x_i^3\) are matched to the first 2-set not containing itselfes in ML_<sub>i</sub>_, and thus are not contained in a blocking 3-set.

Considering the sublist \(\mathrm{ML}'_i\) arising from ML_<sub>i</sub>_ by deleting all 2-sets containing an agent \(x_i^k\), one can check that the first 15 sets of two agents of this sublist only consider agents of \(z_i^{k,p}\) for \(p\in[6]\), and all agents \(z_i^{k,p}\) are matched to one of these 15 sets of size two. Thus, any blocking 2-set containing an agents \(z_i^{k,p}\) consists only of agents from \(\{z_i^{k,q}:q\in[6]\}\). By enumerating all 20 such 3-sets, one easily verifies that none of them is blocking.

Since the set _A_ of agents in \(\mathcal{I}'\) is \(\{c_j,d_j:j\in[m]\}\cup\{x_i^k,z_i^{k,p}:i\in[n],k\in[3],p\in[6]\}\), the lemma now directly follows from Claims 1 and 2.

