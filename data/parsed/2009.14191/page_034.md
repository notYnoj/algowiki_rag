_Proof._ Agents \(z_2^{i,j}\) and \(z_3^{i,j}\) are matched to the first 2-sets in their preference lists and thus are not part of a blocking 3-set.

All 2-sets which \(z_1^{i,j}\) prefers to \(\{z_2^{i,j},z_3^{i,j}\}\) are of the form \(\{b_p^\ell,b_q^{\ell^\prime}\}\) for \(\ell=i,j\) or \(\ell=j,i\) and \(\ell'=i,j\) or \(\ell'=j,i\). We assume without loss of generality that \(p\le q\) and \(\ell=i,j\); the case _q\>p_ or \(\ell=j\) is symmetric. However, agent \(b_p^{i,j}\) is matched to \(\{c_p^{i,j},b_p^{j,i}\}\) if _p\<p<sub>i</sub>_, to \(\{x^{i,j},\overleftarrow{x}^{i,j}\}\) if _p=p<sub>i</sub>_, and to \(\{c_{p-1}^{i,j},b_p^{j,i}\}\) if _p\>p<sub>i</sub>_. In all cases, agent \(b_p^{i,j}\) prefers \(M(b_p^{i,j})\) to \(\{z_1^{i,j},b_q^{\ell^\prime}\}\), and thus, \(z_1^{i,j}\) is not part of a blocking 3-set.

Finally, we turn to the remaining agents from the incidence-checking gadgets.

**Lemma 4.21.** _For every_ \(i<j\in[k]\) _and each_ \(\ell\in[3m']\)_, agents_ \(b_\ell^{i,j}\), \(b_\ell^{j,i}\)_, and_ \(c_\ell^{i,j}\) _as well as_ \(b_{3m^\prime+1}^{i,j}\) _and_ \(b_{3m^\prime+1}^{j,i}\) _are not part of a blocking 3-set._

_Proof._ The argument is similar to the proof of Lemma 4.18.

We show that agents \(b_\ell^{i,j},b_\ell^{j,i}\), and \(c_\ell^{i,j}\) are not contained in a blocking 3-set via induction on _ki+j_. For _ki+j\<k_+1, there are no agents \(b_\ell^{i,j}\), \(b_\ell^{j,i}\), and \(c_\ell^{i,j}\), and thus, there is nothing to show. So fix an incidence-checking gadget _B<sup>i,j</sup>_ with \(ki+j\ge k+1\). A blocking 3-set cannot contain an agent from a vertex-selection gadget (by Lemmas 4.17 and 4.20), an agent from an incidence-checking gadget \(B^{i^\prime,j^\prime}\) with \(ki'+j'<ki+j\) (by the induction hypothesis), or an agent \(x^{i^\prime,j^\prime}\) or \(\overleftarrow{x}^{i^\prime,j^\prime}\) (by Lemma 4.19). Thus, every blocking 3-set only consists of agents \(b_\ell^{i,j},b_\ell^{j,i}\), or \(c_\ell^{i,j}\). However, the agent with minimal index does not prefer the 3-set to _M_, a contradiction. Therefore, no blocking 3-set contains an agent \(b_\ell^{i,j}\), \(b_\ell^{j,i}\), or \(c_\ell^{i,j}\).

Now, we can conclude the stability of _M_.

**Lemma 4.22.** _Matching M is stable._

_Proof._ By Lemmas 4.17 to 4.21, no agent outside a cut-off gadget is contained in a blocking 3-set. Thus, by Lemma 4.7, there is no blocking 3-set.

## 4.3.7 Proof of the backward direction

Finally, we show that if \(\mathcal{I}'\) admits a stable matching, then _G_ contains a clique of size _k_. We start by showing that every stable matching selects a vertex \(v_{p_i}^i\) in every vertex-selection gadget _S<sup>i</sup>_, meaning that it contains the 3-set \(\{s^i,\overleftarrow{s}^i,v_i^{p_i}\}\) for some \(p_i\in[3n'+1]\).

**Lemma 4.23.** _For_ \(i\in[k]\)_, every stable matching M contains a 3-set_ \(\{s^i,\overleftarrow{s}^i,v_{p_i}^i\}\) _for some_ \(p_i\in[3n'+1]\)_, and all other agents_ \(v_q^i\) _are matched to each other for_ \(q\neq p_i\).

_Proof._ Consider a stable matching _M_. We prove the statement by induction on _i_. For _i_=0, there is nothing to show. So fix _i\>_0. By the induction hypothesis, we know that no agent from a vertex-selection gadget \(S^{i^\prime}\) with \(i'<i\) is matched to a 2-set containing an agent from _S<sup>i</sup>_. Ignoring 2-sets containing an agent from \(S^{i^\prime}\) for \(i'<i\), agent \(v_p^i\) prefers most to be matched to \(\{v_q^i,v_{q^\prime}^i\}\) for \(q,q'\in[3n'+1]\), or to \(\{s^i,\overleftarrow{s}^i\}\). If no agent \(v_p^i\) is matched to \(\{s^i,\overleftarrow{s}^i\}\), then \(\{v_{3r-2}^i,v_{3r-1}^i,v_{3r}^i\}\in M\) for all \(r\in[n']\) by the same arguments as in the proof of Proposition 4.1 (as after ignoring also \(\{s^i,\overleftarrow{s}^i\}\), the beginning of the preferences is derived from the strict order \(v_1^i\succ v_2^i\succ\cdots\succ v_{3n^\prime+1}^i\)). The cut-off gadget for \(v_{3n^\prime+1}^i\) then implies that _M_ is not stable. Thus, there exists some \(p_i\in[3n'+1]\) such that \(\{v_{p_i}^i,s^i,\overleftarrow{s}^i\}\in M\). It follows that all other agents \(v_q^i\) are matched to each other for \(q\neq p_i\) by the same arguments as in the proof of Proposition 4.1.

**Lemma 4.24.** _For every stable matching M and every incidence-checking gadget B<sup>i,j</sup>, every 3-set t containing at least one agent from B<sup>i,j</sup> contains three agents from B<sup>i,j</sup>._

