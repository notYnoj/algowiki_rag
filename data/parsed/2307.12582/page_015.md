## A Proof of Lemma 2.2

Lemma 2.2. _Let_ **g** _be a maximal prefix solution to Bounted Knapsack. Let_ \(W_1\cup\cdots\cup W_k\) _be a partition of the set W. For_ \(j\in\{1,\dots,k\}\)_, let U<sub>j</sub> be an upper bound for_ \(\Delta(\mathcal{I}^{W_j})\)_. Then Bounded Knapsack can be solved in_ \(\widetilde{O}(n+k\sum_{j=1}^k|W_j|\cdot U_j)\) _time._

_Proof._ Without loss of generality, assume that \(U_1\le\dots\le U_k\). We construct an optimal solution **x** from **g**, which can be interpreted as **x**=**g**-**x**<sup>-</sup>+**x**<sup>+</sup>. Here **x**<sup>-</sup> stands for the copies in **g** but not in **x**, which must be copies in I_<sub>\<b</sub>_. Likewise, **x**<sup>+</sup> stands for copies in **x** but not in **g**, which must be copies in \(\mathcal{I}_{\unknown b}\). It is obvious that \(\Delta(\mathcal{I}_{<b})=\sum_{j=1}^k\Delta(\mathcal{I}_{<b}^{W_j})\le k\cdot U_k\) and \(\Delta(\mathcal{I}_{\unknown b})\le k\cdot U_k\).

From now on we shall use the bold symbol **_x_** to represent a sequence. We shall compute 3 sequences:

• \(\mathbf{x}^-=\langle x_0^-,\dots,x_{k\cdot U_k}^-\rangle\), where \(x_{t^\prime}^-\) is the minimum total profit of copies in I_<sub>\<b</sub>_ whose total weight is exactly \(t'\);<tbc>

• \(\mathbf{x}^+=\langle x_0^+,\dots,x_{k\cdot U_k}^+\rangle\), where \(x_{t^\prime}^+\) is the maximum total profit of copies in \(\mathcal{I}_{\unknown b}\) whose total weight is exactly \(t'\).<tbc>

• \(\mathbf{x}_\unknown^+=\langle x_{\unknown 0}^+,\dots,x_{\unknown k\cdot U_k}^+\rangle\), where \(x_{\unknown t^\prime}^+\) means the maximum value we can obtain by choosing copies from \(\mathcal{I}_{\unknown b}\) whose total weight does not exceed \(t'\). To simply the writing up, we let \(x_{\unknown k\cdot U_k+h}^+=x_{\unknown k\cdot U_k}^+\) for all \(1\le h\le\Delta\), where \(\Delta=t-\sum_{i\in\mathcal{I}}w_ig_i\).

Suppose we have computed the above three sequences, then Knapsack can be solved as follows: For every \(t'\in\{0,\dots,k\cdot U_k\}\), we compute \(y_{t^\prime}=\sum_{i\in\mathcal{I}}v_ig_i-x_{t^\prime}^-+x_{\unknown(t^\prime+\Delta)}^+\), and select \(max_{t^\prime} y_{t^\prime}\).

It remains to compute the three sequences. We show that, \(\mathbf{x}^+=\langle x_0^+,\dots,x_{k\cdot U_k}^+\rangle\) can be computed in \(\widetilde{O}(n+k\sum_{j=1}^k|W_j|U_j)\) time. The computation of **_x_**<sup>-</sup> is similar. Moreover, once we have computed **_x_**<sup>+</sup>, \(\mathbf{x}_\unknown^+\) can be computed in a straightforward way using that \(x_{\unknown t^\prime}^+=max_{1\le h\le t^\prime} x_h^+\).

Now we describe our algorithm for computing \(\mathbf{x}^+=\langle x_0^+,\dots,x_{k\cdot U_k}^+\rangle\). Towards this, we use the fast structured (min,+)-convolution as a basic operation. The (max,+)-convolution \(\mathbf{a}\oplus\mathbf{b}\) between two sequence **_a_** and **_b_** is a sequence _c_<sub>0</sub>_,...,c_<sub>_n+m_</sub> such that for any _i_,

\(c_i=max_{0\le j\le i}(a_j+b_{i-j}).\)

Let \(\mathbf{s}^w=\langle s_0^w,\dots,s_{U_j}^w\rangle\), where \(s_{t^\prime}^w\) denotes the optimal objective value of copies in \(\mathcal{I}_{\unknown b}^w\) whose total weight is exactly \(t'\). Note that copies in \(\mathcal{I}_{\unknown b}^w\) have the same weight _w_. Hence, \(s_{t^\prime}^w\) equals the total profit of the _i_ most valuable copies in \(\mathcal{I}_{\unknown b}^w\) when \(t'=i\cdot w\) for some _i_, or equals \(-\infty\) otherwise.

Given **_s_**_<sup>w</sup>_, **_x_**<sup>+</sup> can be computed by iteratively convolving **_s_**_<sup>w</sup>_, see Algorithm 1. Due to the special structure of **_s_**_<sup>w</sup>_, a single convolution step \(\mathbf{x}^+\oplus\mathbf{s}^w\) can be performed in linear time by SMAWK algorithm \[2\] (also see Lemma 2.2 in \[26\]). As \(\Delta(\mathcal{I}_{\unknown b}^{W_1\cup\dots\cup W_{k^\prime}})\le\sum_{j=1}^{k^\prime} U_j\le k'\cdot U_{k^\prime}\), we can truncate **_x_**<sup>+</sup> after the \(k'\cdot U_{k^\prime}\)-th entry when we compute the weights in \(W_{k^\prime}\). We can compute **_x_**<sup>+</sup> in time: \(\widetilde{O}(n+\sum_{j=1}^kj\cdot|W_j|\cdot U_j)\le\widetilde{O}(n+k\sum_{j=1}^k|W_j|U_j)\). \(\square\)

**Algorithm 1** The Algorithm to Compute **_x_**<sup>+</sup>

1: sort _W_<sub>1</sub>_,...,W<sub>k</sub>_ that \(U_1\le\dots\le U_k\)<br>
2: **_x_**<sup>+</sup>:= empty sequence<br>
3: for j=1,...,k do<br>
4: for \(w\in W_j\) do<br>
5: \(\mathbf{s}^w:=\) the sequence of maximum value get from \(\mathcal{I}_{\unknown b}^w\)<br>
6: \(\mathbf{x}^+:=\mathbf{x}^+\oplus\mathbf{s}^w\triangleright\) using SMAWK algorithm<br>
7: Truncate **_x_**<sup>+</sup> after the \(j\cdot U_j\)-th entry<br>
8: return **_x_**<sup>+</sup>

## B Proof of Lemma 3.2

Lemma 3.2. _Let w be a positive integer. Let A and B be two multisets of integers from_ {1_,...,w_} _such that_<tbc>

