• **Bypass arcs:** Three sets of arcs with a constant capacity of 2 are added to control delays: (_u<sub>i</sub>,t_) for all \(i\in I\) (green dashed), (_s,v<sub>j</sub>_) for all \(j\in J\) (orange dashed), and \((s,v_j^N)\) for all \(j\in J\) (yellow dashed).

We define three commodities sharing the same source _s_ and destination _t_. The structure and purpose of each commodity are summarized below:

• **Commodity** _k<sub>L</sub>_ **(Light and Fast):** Size _b<sub>L</sub>=W_, maximum delay \(d_L=2+\frac{1}{2W}\).<br>
We will prove that it must be carried exclusively through paths of the form \(s\rightarrow u_i\rightarrow v_j\rightarrow t\), effectively building the solution to the 3-Partition problem.<tbc>

• **Commodity** _k<sub>H</sub>_ **(Heavy and Slow):** Size \(b_H=(m-1)(n+1)W\), maximum delay \(d_H=N+2+\frac{1}{W}\).<br>
This commodity will use all paths crossing the partition arcs (_u<sub>i</sub>,v<sub>j</sub>_) that are not used by _k<sub>L</sub>_. This creates high delays on these arcs, forcing _k<sub>L</sub>_ to define a partition of the objects set _I_.<tbc>

• **Commodity** _k_<sub>2</sub> **(Delay calibration):** Size _b_<sub>2</sub>=5_m_, maximum delay _d_<sub>2</sub>=2.<br>
We will show that this tight delay limit forces the commodity to use only 2-hop paths (formed by the bypass arcs) and to maintain a load of exactly 1 on each of these paths. This sets the delay and load on the crossed links.

**Proposition 2.1.** _If the 3-Partition instance with weights_ \(\{w_i\}_{i\in I}\) _is feasible, then the related DCMCF instance described above admits a feasible solution with_ \(\gamma=1\).

_Proof._ Assuming that the 3-Partition instance is feasible, each vertex _v<sub>j</sub>_ is assigned to a single triplet _T<sub>j</sub>_. We can build a multi-commodity flow using the following paths:

• For commodity _k<sub>L</sub>_: for every triplet \(j\in J\) and object \(i\in T_j\), the path \(s\rightarrow u_i\rightarrow v_j\rightarrow t\) is used with a load equal to _w<sub>i</sub>_.<tbc>

