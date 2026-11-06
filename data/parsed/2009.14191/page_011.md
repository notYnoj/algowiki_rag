## 3.2.3 Proof of the backward direction

Now, we show how to construct a solution to the 1-in-3 Positive 3-Occurrence-SAT instance I from a stable matching. First, we identify small subsets \(A'\) of agents such that \(\mathcal{I}'\) restricted to the agents from \(A'\) does not admit a stable matching, implying that at least one agent of \(A'\) must be matched to at least one vertex outside \(A'\).

**Lemma 3.3.** _For any_ \(i\in[n]\) _and_ \(k\in[3]\)_, the subinstance_ \(\mathcal{I}_i^k\) _of_ \(\mathcal{I}'\)_, which results from_ \(\mathcal{I}'\) _by deleting all but the agents_ \(x_i^k\) _and_ \(\{z_i^{k,p}:p\in[6]\}\)_, does not admit a stable matching._

_Proof._ Assume for the sake of contradiction that there exists a stable matching _M_. Note that deleting \(z_i^{k,6}\) from \(\mathcal{I}_i^k\) results in an instance identical to the instance I<sub>instable</sub> (this can be seen by renaming agent \(x_i^k\) to _a_, agent \(z_i^{k,p}\) to _b_, agent \(z_i^{k,2}\) to _c_, agent \(z_i^{k,3}\) to _d_, agent \(z_i^{k,4}\) to _e_, and agent \(z_i^{k,5}\) to _f_). Thus, Observation 3.1 implies that _M_ matches agent \(z_i^{k,6}\) to a 2-set {_x,y_}. As all 2-sets containing \(z_i^{k,6}\) appear on the end of the preference lists, _x_ and _y_ together with any unmatched agent form a blocking 3-set, a contradiction to the stability of _M_.

We now show that the two agents _c<sub>j</sub>_ and _d<sub>j</sub>_ created for clause _C<sub>j</sub>_ have to be matched to an agent corresponding to a literal in this clause; indeed, we will later see that this literal satisfies the clause _C<sub>j</sub>_ in the found solution.

**Lemma 3.4.** _In any stable matching M and for each_ \(j\in[m]\)_, there is an_ \(\ell\in[3]\) _such that_ \(\{c_j,d_j,y_j^\ell\}\in M\).

_Proof._ We prove the lemma by induction on _j_.

**Base case:** If _M_ does not contain the 2-set \(\{c_1,d_1,y_1^\ell\}\) for all \(\ell\in[3]\), then \(\{c_1,d_1,y_1^\ell\}\) is a blocking 2-set for every \(\ell\in[3]\).

**Induction step:** By the induction hypothesis, no agent _c<sub>p</sub>_ or _d<sub>p</sub>_ for _p\<j_ is matched to _c<sub>j</sub>_, _d<sub>j</sub>_, or some \(y_j^\ell\). Hence, neither _c<sub>j</sub>_ nor _d<sub>j</sub>_ nor \(y_j^\ell\) is matched to a 2-set which comes before A_<sub>j</sub>_ in the master list. Thus, if _M_ does not contain \(\{c_j,d_j,y_j^\ell\}\) for all \(\ell\in[3]\), then \(\{c_j,d_j,y_j^\ell\}\) is a blocking 3-set for every \(\ell\in[3]\), contradicting the stability of _M_.

We now want to show that for any \(i\in[n]\), a stable matching contains either \(\{x_i^1,x_i^2,x_i^3\}\) or matches \(x_i^k\) to 2-sets of the form {_c<sub>j</sub>,d<sub>j</sub>_}. In order to do so, we first show that for any \(i\in[n]\) and \(k\in[3]\), agents \(z_i^{k,1},\dots,z_i^{k,6}\) are matched to two 3-sets in any stable matching _M_ unless at least one agent \(z_i^{k,p}\) is matched to a 2-set containing an agent _c<sub>j</sub>_, _d<sub>j</sub>_, \(x_{i^\prime}^{k^\prime}\), or \(z_{i^\prime}^{k^\prime,q}\) for some \(j\in[m]\), \((i',k')\in[n]\times[3]\) with \(i'<i\) or \(i'=i\) and \(k'\le k\), and \(q\in[6]\).

**Lemma 3.5.** _Let M be any stable matching, and let_ \(i\in[n]\) _and_ \(k\in[3]\)_. Let_ \(X:=\{c_j,d_j:j\in[m]\}\cup\{x_{i^\prime}^{k^\prime},z_{i^\prime}^{k^\prime,q}:i'<i,k'\in[3],q\in[6]\}\cup\{x_i^{k^\prime},z_i^{k^\prime,q}:k'\le k,q\in[6]\}\)_, and let_ \(Z_i^k:=\{z_i^{k,p}:p\in[6]\}\)_. If no agent_ \(z_i^{k,p}\) _is matched to a 2-set containing an agent from X, then M contains two 3-sets t_<sub>1</sub> _and t_<sub>2</sub> _which are subsets of_ \(Z_i^k\).

_Proof._ Note that every 2-set before \(\mathcal{B}_i^k\) in the master list contains an agent from _X_. List \(\mathcal{B}_i^k\) contains all 2-sets \(\{z_i^{k,p},z_i^{k,q}\}\) for \(p,q\in[6]\) with \(p\neq q\) (as well as some 2-sets containing \(x_i^k\in X\)). Now assume for a contradiction that the lemma does not hold, i.e., there exists some \(z\in Z\) which is not matched to a 2-set \(\{z',z''\}\) with \(z',z''\in Z_i^k\). Then there exist three such agents \(z_1,z_2,z_3\in Z_i^k\). Hence, _z_<sub>1</sub>_,z_<sub>2</sub>, and _z_<sub>3</sub> are matched to 2-sets which appear after \(\mathcal{B}_i^k\) in the master list. Consequently, {_z_<sub>1</sub>_,z_<sub>2</sub>_,z_<sub>3</sub>} is a blocking 3-set, contradicting the stability of _M_.

