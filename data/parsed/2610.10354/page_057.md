### Step 2: Constructing **_H_** by the BSG Theorem.

In step 2 we first identify the index _j_ minimizing |_A_<sub>_j_+1</sub>|/|_A<sub>j</sub>_|. Since we have computed the sets _A_<sub>1</sub>_,...,A<sub>J</sub>_ explicitly, this can be done in linear time. Then we apply the BSG theorem (Theorem 2.3) to the set _A<sub>j</sub>_ to construct _H_. This runs in time \(\widetilde{O}(|A_j|K_j)\), for some _K<sub>j</sub>=O<sub>J</sub>(L_<sup>_O_(1_/J_)</sup>) as before. Again, recalling that \(|A_j|\le|B|/\alpha_j\) by Property (iii), this is within the claimed time budget.

### Step 3: Relating **_H_** to **_A_**.

The only data that we need to compute in this step is the shift _x_<sub>0</sub> satisfying Equation (13), i.e.,<tbc>

\(|A\cap(H+x_0)|\ge\frac{|A|}{K_0}.\)

<tbc>In fact, we settle for a slightly weaker condition. Namely, observe that this shift _x_<sub>0</sub> is equivalently an element of Pop(_A,-H_;|_A|/K_<sub>0</sub>). Hence, to find _x_<sub>0</sub> we may run Lemma 3.3 to compute a set sandwiched between Pop(_A,-H_;|_A|/K_<sub>0</sub>) and Pop(_A,-H_;|_A|/_2_K_<sub>0</sub>), and pick any element _x_<sub>0</sub> from that set. By definition, that element satisfies

\(|A\cap(H+x_0)|\ge\frac{|A|}{2K_0}.\)

We may increase _K_<sub>0</sub> to 2_K_<sub>0</sub> without any harm, and then _x_<sub>0</sub> is as claimed in Equation (13).

The running time is dominated by the call to Lemma 3.3 in time \(\widetilde{O}(|H|K_0)\). By Equation (10) and Property (iii) this is at most \(\widetilde{O}(|A_j|K_jK_0)=\widetilde{O}(|B|K_jK_0/\alpha_j)\), which is within the budget.

### Step 4: Relating **_H_** to **_B_**.

The final step only involves the construction of \(\Lambda\). Recall that \(\Lambda\) is constructed as a random subset of _B_, sampled with an appropriate rate _p_. We have argued that with constant probability, the size \(|B\cap(H+\Lambda)|\) is at least as large as claimed in Equation (15). The only modification in our algorithm is to amplify the success probability. That is, we sample \(R=\Theta(log|B|)\) sets \(\Lambda_1,\dots,\Lambda_R\), compute the sumsets \(H+\Lambda_1,\dots,H+\Lambda_R\) by brute-force, and report the set \(\Lambda_r\) maximizing \(|B\cap(H+\Lambda_r)|\). With high probability that choice satisfies Equation (15). Moreover, with high probability all sets \(\Lambda_1,\dots,\Lambda_R\) simultaneously satisfy the size bound from Equation (16),<tbc>

\(|\Lambda_1|,\dots,|\Lambda_R|\le O\left(\frac{K_j^2}{\alpha_j}\cdot\frac{|B|}{|H|}\right).\)

<tbc>The running time of step 4 is therefore bounded by

\(O\left(\sum_{r=1}^R(|B|+|H||\Lambda_r|)\right)=\widetilde{O}\left(\frac{K_j^2}{\alpha_j}\cdot|B|\right).\)

This is within the claimed time budget.

## Acknowledgements

We are very grateful for the detailed feedback of an anonymous reviewer, especially for suggesting a substantial simplification of the proof of Theorem 1.2.

C. J. is supported by the Miller Research Fellowship at the Miller Institute for Basic Research in Science, UC Berkeley. Y. X. is supported by NSF HDR TRIPODS Phase II grant 2217058 (EnCORE Institute).

