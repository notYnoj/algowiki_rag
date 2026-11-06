• For commodity _k<sub>H</sub>_: for every triplet \(j\in J\) and object \(i\in I\backslash T_j\), the path \(s\rightarrow u_i\rightarrow v_j\rightarrow v_j^1\rightarrow\cdots\rightarrow v_j^N\rightarrow t\) is used with a load equal to _w<sub>i</sub>+W_.<tbc>

• For commodity _k_<sub>2</sub>: each path in \(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}\) is used with a load equal to 1.

One can verify that each commodity sends the required load: \(\sum_{i\in I}w_i=W=b_L\) for commodity _k<sub>L</sub>_, \(\sum_{j\in J}\sum_{i\in I\backslash T_j}(w_i+W)=m\left(W-\frac{W}{m}+(n-3)W\right)=mW(n-2-\frac{1}{m})=(m-1)(n+1)W=b_H\) for commodity _k<sub>H</sub>_ and 2_m+n_=5_m=b_<sub>2</sub> for commodity _k_<sub>2</sub>.

The delay of each arc is given by:

• \(d_{(u_i,v_j)}=\frac{1}{(w_i+2W)-w_i}=\frac{1}{2W}\) if \(i\in T_j\);<tbc>

• \(d_{(u_i,v_j)}=\frac{1}{(w_i+2W)-(w_i+W)}=\frac{1}{W}\) if \(i\notin T_j\);<tbc>

• the delay of all other arcs is exactly equal to 1.

It is easy to verify that the delay constraints are satisfied (with equality) for all paths used by all commodities.

Let us now suppose that this DCMCF instance admits a solution with \(\gamma\ge 1\). We will prove that the corresponding 3-Partition instance is of True type. For this purpose, we will prove that commodities _k_<sub>2</sub>, _k<sub>L</sub>_ and _k<sub>H</sub>_ are necessarily routed as described in the proof of Proposition 2.1, which allows us to infer the feasibility of the 3-Partition instance.

Since the proof is relatively long, we will only show the intermediate lemmas below: all proofs can be found in the Appendix section at the end of the paper.

Let us first prove that commodity _k_<sub>2</sub> must follow a specific set of paths:

**Lemma 2.1.** _Commodity k_<sub>2</sub> _must necessarily follow paths in_

\(\{s\rightarrow u_i\rightarrow t\}_{i\in I}\cup\{s\rightarrow v_j\rightarrow t\}_{j\in J}\cup\{s\rightarrow v_j^N\rightarrow t\}_{j\in J}.\)

The proof of this lemma is presented in Appendix A.1. It relies on the fact that the minimum delay of a given arc \(a\in A\) is \(\frac{1}{c_a}\): we can show that,<tbc>

