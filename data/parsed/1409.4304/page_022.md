<tbc>but (2) tells us that this chain is limited in length by _m_. Also, (1) again tells us that the number of steps it takes to generate the coalition which is used for the deletion is limited by _m_ as well. The only remaining issue is to argue why additional deletion of coalitions during this procedure does not create problems. Now if such a coalition was part of S<sub>0</sub> it does not create any additional costs. If it was part of some deletion chain, its cost was already accounted towards the coalition of S<sub>0</sub> which had to be deleted. In all other cases, the creation of this coalition was of no use in the first place, that is, it would not be part of the truncated sequence I<sup>∗</sup>. Hence, overall we have a sequence of length at most \(|\mathcal{S}_0|\cdot m^2+|\mathcal{S}^*|\cdot m\in O(m^2n)\) steps.

## A.5 Proof of Theorem 3

The proof is done via reduction from 3Sat . We will use the same idea and central construction for all cases and only adapt the structure of the clause- gadgets to the specific settings. Each clause gadget will have the property that one particular vertex _x<sub>C</sub>_ has be matched to a vertex of the central construction at some (arbitrary) point during the dynamics and has to be left single again. Otherwise the clause gadget cannot be transformed into the state it has in the desired final matching.

We first outline the universal proof approach including only this one particular vertex _x<sub>C</sub>_ per clause _C_ (and the central construction). We show that it is NP-hard to decide whether there is a sequence of improvement steps such that each of the clause vertices gets matched and dropped at least once. Afterwards, for every setting we will give the exact clause gadget and explain why it is necessary to match _x<sub>C</sub>_ to some vertex outside the clause gadget to reach the final state.

Given a 3Sat formula with _k_ variables _x_<sub>1</sub>_,...,x<sub>k</sub>_ and _l_ clauses _C_<sub>1</sub>_,...,C<sub>l</sub>_, where clause _C<sub>j</sub>_ contains the literals _l_<sub>1_,j_</sub>_,l_<sub>2_,j_</sub> and _l_<sub>3_,j_</sub>, for our central construction we have

Further \(E=E_1\cup E_2\cup E_3\) with _E_<sub>1</sub>={_u<sub>x<sub>i</sub></sub>,w<sub>x<sub>i</sub></sub>_},{_u<sub>x<sub>i</sub></sub>,w<sub>x<sub>i</sub></sub>_}|_i_=1_...k_}, _E_<sub>2</sub>={_u<sub>x<sub>i</sub></sub>,w<sub>x<sub>i</sub></sub>_},{_u<sub>x<sub>i</sub></sub>,w<sub>x<sub>i</sub></sub>_}|_i_=1_...k_}, and _E_<sub>3</sub>={{_x<sub>C<sub>j</sub></sub>,w<sub>l<sub>i,j</sub></sub>_}|_j_=1_...l,i_=1_..._3}, and benefits in  1.

For a small example see Figure 2. In the case of locally and socially stable matching we will have social links between all vertices of _U_ and _W_ to make sure that all edges of _E_ are available for matching at all times. In the case of friendship matching we set all \(\alpha\) to 0 to ensure that utility is also perceived utility.

We start from _M_<sub>0</sub>=_E_<sub>2</sub> and want to reach _M_<sup>∗</sup>=_E_<sub>1</sub> which also is the only stable state of this graph. This transformation is always possible, but we now<tbc>

U = {u<sub>x<sub>i</sub></sub>|i=1...k} U {u<sub>x<sub>i</sub></sub>|i=1...k} U {x<sub>C<sub>j</sub></sub>|j=1...l},
W = {w<sub>x<sub>i</sub></sub>|i=1...k} U {w<sub>x<sub>i</sub></sub>|i=1...k}.

