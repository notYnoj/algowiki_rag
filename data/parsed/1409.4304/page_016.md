## A Omitted Proofs

### A.1 Proof of Proposition 1

In \[16, Theorem 3\] we have shown that such instances and starting states exist for locally stable matching, when agents are allowed to match with partners at a hop distance of at most \(\ell=3\) in \((V,L\cup M)\). This scenario can be embedded into the context of coalition formation games with constraints, where we violate only the above mentioned precondition in the generation rules. Note that the violation is minimal in the sense that we increase from one to at most two sets in the precondition.

Given an instance of locally stable matching with graph _G_=(_V,E_), (social) links _L_, correlated preferences based on edge benefits _b(e_), we define the parameters of the framework as follows. The set of agents is _N=V_ , the set of possible coalitions is C=_E_. The coalitions that can always be generated are the ones connected by at most 3 links, i.e., \(\mathcal{C}_g=E\cap\{\{u,v\}|dist_L(u,v)\le 3\}\). The benefit or coalition weight is obviously given by _w=b_. For the generation rules, we have \(T=T_1\cup T_2\cup T_3\), where

\(T_1=\{(\{\{u,v\}\},\{u,v'\})|\{u,v\},\{u,v'\}\in E,\{v,v'\}\in L\}\)<br>
\(T_2=\{(\{\{u,v\}\},\{u',v'\})|\{u,v\},\{u',v'\}\in E,\{u',v\},\{u,v'\}\in L\}\)<br>
\(T_3=\{(\{\{u',v\},\{u,v'\}\},\{u,v\})|\{u,v\},\{u,v'\},\{u',v\}\in E,\{u',v'\}\in L\}\)

Here _T_<sub>1</sub> captures accessible pairs with 2 hops composed of one matching edge and one link, _T_<sub>2</sub> captures accessible pairs within distance of 3 hops composed of one matching edge and two links, and _T_<sub>3</sub> captures accessible pairs within distance of 3 hops composed of two matching edges and one link. The latter generation rules are obviously using two coalitions as precondition. The domination rules implement only the necessary preference-based improvement of coalitions _D=D<sub>w</sub>_. \(\sqcap\sqcup\)

### A.2 Proof of Proposition 2

We will attach a sequence of gadgets that imply a unique exponential improvement sequence. We use a gadget of size 9 and a starting state with the property that to create coalition _C_<sub>6_,i_</sub> of gadget _i_ we twice need to generate _C_<sub>1_,i_</sub>. Further the gadget will not reach a stable state unless _C_<sub>6_,i_</sub> exists. Using this property we will connect _k_ such gadgets by allowing a creation rule {{_C_<sub>1_,i_+1</sub>}_,C_<sub>6_,i_</sub>} and identifying 0<sub>_i_+1</sub> with 8_<sub>i</sub>_. Then to create _C_<sub>_k,_6</sub> (without which the graph would not be stable) _C_<sub>1,1</sub> has to be created at least 2_<sup>k</sup>_ times.<br>
Now for gadget _i_ we have _N<sub>i</sub>_={0_<sub>i</sub>,...,_8_<sub>i</sub>_}, C_<sub>i</sub>_={_C_<sub>1_,i_</sub>_,...,C_<sub>6_,i_</sub>} with _C_<sub>1_,i_</sub>={0_<sub>i</sub>,_1_<sub>i</sub>,_2_<sub>i</sub>_}, _C_<sub>2_,i_</sub>={1_<sub>i</sub>,_3_<sub>i</sub>_}, _C_<sub>3_,i_</sub>={3_<sub>i</sub>,_4_<sub>i</sub>,_5_<sub>i</sub>_}, _C_<sub>4_,i_</sub>={4_<sub>i</sub>,_6_<sub>i</sub>_}, _C_<sub>5_,i_</sub>={2_<sub>i</sub>,_6_<sub>i</sub>,_7_<sub>i</sub>_}, _C_<sub>6_,i_</sub>={5_<sub>i</sub>,_7_<sub>i</sub>,_8_<sub>i</sub>_}, weights _w(C_<sub>1_,i_</sub>)=_x<sub>i</sub>_+1, _w(C_<sub>2_,i_</sub>)=_x<sub>i</sub>_+2, _w(C_<sub>3_,i_</sub>)=_x<sub>i</sub>_+4, _w(C_<sub>4_,i_</sub>)=_x<sub>i</sub>_+3, _w(C_<sub>5_,i_</sub>)=_x<sub>i</sub>_+2 and _w(C_<sub>6_,i_</sub>)=_x<sub>i</sub>_+5 with _x<sub>i</sub>_=5(_i_-1), and

