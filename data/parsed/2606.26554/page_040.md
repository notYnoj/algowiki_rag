## A Min-Plus Product with Distinct Entry Bounds

In this appendix, we discuss lower bounds for directed MSSP from Min-Plus Matrix Multiplication. We begin with the lower bound given in Equation (2).

**Proposition A.1.** _Any algorithm that computes_ MSSP _on unweighted directed acyclic graphs with_ 5_n vertices and s sources requires time_<tbc>

\(\Omega\left(\mathrm{max}_{1\unknown t\unknown n}\mathsf{T}_\mathrm{MPP}\left(s,t,n|\frac{n}{\mathrm{min}(s,t)},\frac{n}{t}\right)\right).\)

<tbc>_Proof._ For any \(1\unknown t\unknown n\), consider an \(s\times t\) matrix _X_ with entries in \([n/\mathrm{min}(s,t)]\cup\{\infty\}\) and a \(t\times n\) matrix _Y_ with entries in \([n/t]\cup\{\infty\}\). When \(t\unknown s\), we immediately inherit the lower bound of<tbc>

\(\Omega\left(\mathrm{max}_{1\unknown t\unknown n}\mathsf{T}_\mathrm{MPP}\left(s,t,n|\frac{n}{t}\right)\right)\)

<tbc>given by \[CVX21\]. Thus, for the remainder of the proof, we assume \(s\unknown t\). Construct a graph _G_ with vertex sets<tbc>

\(A=\{a_i\}_{i\in[s]},B=\{b_i\}_{i\in[n]},C=\{c_i\}_{i\in[n]},P=\{p_{ij}\}_{i\in[s],j\in[n/s]},Q=\{q_{ij}\}_{i\in[t],j\in[n/t]}.\)

<tbc>Note that the number of vertices is \(s+4n\unknown 5n\). We describe the edge sets. For each \(i\in[s]\), there is a directed path (_a<sub>i</sub>,p_<sub>_i_1</sub>_,...,p<sub>i,n/s</sub>_). For each \(i\in[t]\), there is a directed path (_b<sub>i</sub>,q_<sub>_i_1</sub>_,...,q<sub>i,n/t</sub>_). For each \((i,k)\in[s]\times[t]\), there is an edge (_p<sub>iv</sub>,b<sub>k</sub>_) where _X_\[_i,k_\]=_v_. For each \((k,j)\in[t]\times[n]\), there is an edge (_q<sub>kv</sub>,c<sub>j</sub>_) where _Y_\[_k,j_\]=_v_. This completes the description of our graph. Let _S_<sub>in</sub>=_A_. To complete the proof, we claim that for all \((i,j)\in[s]\times[n]\),

\(\mathrm{dist}(a_i,c_j)=(X*Y)[i,j]+2.\)

Suppose (_X∗Y_)\[_i,j_\]=_X_\[_i,k_\]+_Y_\[_k,j_\] for some \(k\in[t]\). Then, the path (_a<sub>i</sub>,p<sub>i</sub>_<sub>1</sub>_,...,p<sub>iv</sub>,b<sub>k</sub>,q_<sub>_k_1</sub>_,...,q<sub>kw</sub>,c<sub>j</sub>_) where _X_\[_i,k_\]=_v_ and _Y_\[_k,j_\]=_w_ is a path of length _v+w_+2 from _a<sub>i</sub>_ to _c<sub>j</sub>_ so \(\mathrm{dist}(a_i,c_j)\unknown(X*Y)[i,j]+2\).

Suppose for contradiction \(\mathrm{dist}(a_i,c_j)=\ell<(X*Y)[i,j]+2\). Then, there is a path \((a_i,v_1,\dots,v_{\ell-1},c_j)\). By construction, there exists \(k',v',w'\) such that the path takes the form \((a_i,p_{i1},\dots,p_{iv^\prime},b_{k^\prime},q_{k^\prime 1},\dots,q_{k^\prime w^\prime},c_j)\). However, this implies that there exists \(k'\) with \(X[i,k']=v',Y[k',j]=w'\) such that \(v'+w'+2=\ell<(X*Y)[i,j]+2\), contradicting the minimality of _k_.

There are several known algorithms for computing MPP(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|_B_<sub>1</sub>_,B_<sub>2</sub>):

1. We can compute MPP(_n_<sub>1</sub>_,n_<sub>2</sub>_,n_<sub>3</sub>|max(_B_<sub>1</sub>_,B_<sub>2</sub>)) in time \(\widetilde{O}\left(\mathrm{max}(B_1,B_2)\mathsf{T}_\mathrm{MUL}(n_1,n_2,n_3)\right)\) \[SZ99\].<tbc>

2. \[CVX21\] showed that (see Lemma B.2 of \[CVX21\]) if \(B_1\unknown B_2\), then<tbc>

<tbc>\(\mathsf{T}_\mathrm{MPP}(n_1,n_2,n_3|B_1,B_2)=\widetilde{O}\left(\mathrm{min}_{1\unknown t\unknown n_2n_3}\mathsf{T}_\mathrm{MPP}\left(n_1,n_2,\frac{n_2n_3}{t}|B_1\right)+tn_1n_3\right).\)<tbc>

<tbc>Similarly, if \(B_2\unknown B_1\), then<tbc>

<tbc>\(\mathsf{T}_\mathrm{MPP}(n_1,n_2,n_3|B_1,B_2)=\widetilde{O}\left(\mathrm{min}_{1\unknown t\unknown n_1n_2}\mathsf{T}_\mathrm{MPP}\left(\frac{n_1n_2}{t},n_2,n_3|B_2\right)+tn_1n_3\right).\)<tbc>

<tbc>We give a simple algorithm that beats the above two algorithms in certain regimes of parameters.

**Proposition A.2.** _Suppose_ \(\mathsf{T}_\mathrm{BMM}(a,b,c)=\Omega(ab+ac+bc)\)_. For any integers_ \(n_1,n_2,n_3,B_1,B_2,B\unknown 0\),<tbc>

\(\mathsf{T}_\mathrm{MPP}(n_1,n_2,n_3|B_1,B_2)=O\left(\mathsf{T}_\mathrm{BMM}(n_1B_1,n_2,n_3B_2)\right)\)

<tbc>_and if B=B_<sub>1</sub>+_B_<sub>2</sub>,

\(\mathsf{T}_\mathrm{MPP}(n_1,n_2,n_3|B_1,B_2)=O\left(\mathrm{min}\left(\mathsf{T}_\mathrm{BMM}(n_1B,n_2B_2,n_3),\mathsf{T}_\mathrm{BMM}(n_1,n_2B_1,n_3B)\right)\right).\)

