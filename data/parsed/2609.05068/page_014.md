Let us now characterize the routing of commodity _k<sub>L</sub>_.

**Lemma 2.6.** _Commodity k<sub>L</sub> must follow paths in_ \(\{s\rightarrow u_i\rightarrow v_j\rightarrow t\}_{i\in I,j\in J}\).

The proof of this lemma, given in Appendix A.6, simply relies on the fact that all other paths are either saturated by commodity _k_<sub>2</sub> or violate the delay limit _d<sub>L</sub>_.

**Lemma 2.7.** _The load of commodity k<sub>L</sub> over each arc in_ \(\{(v_j,t)\}_{j\in J}\) _is exactly_ \(\frac{W}{m}\) .

The proof of this lemma can be found in Appendix A.7 ; it directly results from the load of arc (_v<sub>j</sub>,t_) given in Equation (8).

Let us now consider commodity _k<sub>H</sub>_.

**Lemma 2.8.** _The load of commodity k<sub>H</sub> over each arc in_ \(\{(v_j,v_j^1)\}_{j\in J}\cup\{(v_j^l,v_j^{l+1})\}_{j\in J,I\in[1,N-1]}\cup\{(v_j^N,t)\}_{j\in J}\) _is exactly_ \(W\frac{(n+1)(n-3)}{n}\) _, and the delay on each arc is equal to_ 1.

The proof of this lemma, which results from Equation (9), is given in Appendix A.8.

The results presented above fix the flow on each arc entering vertices _u<sub>i</sub>_ for \(i\in I\) and exiting vertices _v<sub>j</sub>_ for \(j\in J\) if the concurrent throughput \(\gamma\) is greater than 1. We will now study the arcs (_u<sub>i</sub>,v<sub>j</sub>_) to describe how the paths followed by commodity _k<sub>L</sub>_ allow the construction of a 3-Partition of the original problem. The next lemma allows us to associate each object \(i\in I\) with a unique part \(j\in J\) in the original 3-Partition problem:

**Lemma 2.9.** _For every_ \(i\in I\)_, commodity k<sub>L</sub> is carried by a single arc exiting vertex u<sub>i</sub>, and the load of k<sub>L</sub> on this arc is exactly w<sub>i</sub>. This arc does not carry commodity k<sub>H</sub>._

This lemma is proved in Appendix A.9; this proof relies on the upper bound of the delays of arcs (_u<sub>i</sub>,v<sub>j</sub>_) if commodities _k<sub>L</sub>_ and _k<sub>H</sub>_ cross them, and on the total flow exiting the nodes _u<sub>i</sub>_ -- obtained by flow conservation and Equation (7).

**Lemma 2.10.** _For every_ \(j\in J\)_, commodity k<sub>L</sub> is carried by exactly_ 3 _arcs entering vertex v<sub>j</sub>._

