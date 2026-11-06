Consider the columns in C in their natural left-to-right order, and define C_<sub>left</sub>_ to be the first 2_<sup>i</sup>_ columns and C_<sub>right</sub>_=C\\C_<sub>left</sub>_. Denote R={_R_<sub>1</sub>_,...,R_<sub>2_i_+1</sub>}, where the rows are indexed in their natural bottom to top order, and let R_<sub>even</sub>_={_R_<sub>2</sub>_,R_<sub>4</sub>_,...,R_<sub>2_i_+1</sub>} and R_<sub>odd</sub>_={_R_<sub>1</sub>_,R_<sub>3</sub>_,...,R_<sub>2_i_+1-1</sub>} be the sets of all even-indexed and all odd-indexed rows, respectively. Notice that |C_<sub>left</sub>_|=|C_<sub>right</sub>_|=|R_<sub>even</sub>_|=|R_<sub>odd</sub>_|=2_<sup>i</sup>_. The instance BRS(_i_+1,R,C) is defined to be \(\mathsf{BRS}(i,\mathcal{R}_{odd},\mathcal{C}_{left})\cup\mathsf{BRS}(i,\mathcal{R}_{even},\mathcal{C}_{right})\).

For _n_=2_<sup>i</sup>_, we denote by BRS(_n_) the instance BRS(_i,_C,R), where C contains all columns with integral _x_-coordinates from 1 to _n_, and R contains all rows with integral _y_-coordinates from 1 to _n_; see Figure 4 for an illustration.

It is well-known that, if _X_ is a bit-reversal sequence on _n_ points, then \(\mathsf{OPT}(X)\ge\Omega(nlogn)\).

**Claim 4.3** _Let X_=BRS(_i,_C,R)_, for any_ \(i\ge 0\) _and any sets_ C _and_ R _of columns and rows, respectively, with_ |R|=|C|=2_<sup>i</sup>. Then_ |_X_|=2_<sup>i</sup>, and_ \(\mathsf{OPT}(X)\ge\frac{\mathsf{WB}(X)}{2}\ge\frac{|X|(log|X|-2)+1}{2}\) .

The original proof by Wilber \[Wil89\] was given in the BST tree view. We provide a geometric proof here for completeness.

**Proof:** In order to prove the claim, it is sufficient to show that \(\mathsf{WB}(X)\ge|X|(log|X|-2)+1\). We consider a balanced cut sequence \(\sigma\) that always cuts a given strip into two sub-strips containing the same number of active columns. Notice that these cuts follow the inductive construction of the instance, in the reverse order. We will prove by induction that, for any \(i\ge 1\), if _X_=BRS(_i,_C,R), for any sets C and R of columns and rows, respectively, with |R|=|C|=2_<sup>i</sup>_, then \(\mathsf{WB}_\sigma(X)\ge 2^i\cdot(i-2)+1\).

The base case, when _i_=0, is obvious since the Wilber bound is always non-negative.

We now consider some integer _i\>_0, and we let _X_=BRS(_i,_C,R), for some sets C and R of columns and rows, respectively, with |R|=|C|=2_<sup>i</sup>_.

BRS(1)
BRS(2)
BRS(3)

Figure 4: Bit reversal sequences BRS(_i_) for _i_=1,2,3. The sequence BRS(_i_) is constructed by composing two copies of BRS(_i_-1). The left copy is shown in gray, while the right copy is in black. The active rows and columns of the left copies are shown as dotted lines.

