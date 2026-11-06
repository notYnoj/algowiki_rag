(C4) permutations of the legs: if \(T\triangleleft S\), then \(\pi\cdot T\triangleleft\pi\cdot S\) for every permutation \(\pi\in\mathfrak{S}_3\) of the three legs.

Finding the optimal combination of the degeneration ingredients given these combination rules seems a daunting task! Not only do we have an infinite family of degeneration ingredients (parametrised by the several parameters _a,b,t,m_), we may also need to use large _n_ to obtain our target degenerations \(\langle n,n,n\rangle\triangleleft\langle r\rangle\) for which log_r/_log_n_ is small.

Let us first illustrate what sort of combination strategies we may want to do, and then let Strassen’s asymptotic spectrum duality come to the rescue to turn this into a tractable optimisation problem (with a clean analysis, optimal objective value and "dual certificate").

## 1.2 Understanding how the ingredients can be combined

Let us try to combine the degeneration ingredients according to the combination rules to start understanding them, including the role of catalysts and asymptotics.

### 1.2.1 From P_<sub>a,b</sub>_ to partial direct sum of \(\langle 1,1,n\rangle\) and permutations

Fix an integer \(a\ge 2\). By ingredient (D1), we have \(\langle 2a-1\rangle\triangleleft\mathsf{P}_{a,a}\). Tensoring both sides with \(\langle 1,1,n\rangle\) gives

\(\langle 2a-1\rangle\otimes\langle 1,1,n\rangle\triangleleft\mathsf{P}_{a,a}\otimes\langle 1,1,n\rangle\cong\mathsf{P}_{a,a}\oplus_1\cdots\oplus_1\mathsf{P}_{a,a},\) (1.1)

the partial direct sum of _n_ copies of P_<sub>a,a</sub>_.

Ingredients (D3) and (D4) are degenerations that act only on the second and third legs, so they can be applied to some of the summands of a partial direct sum while the other summands stay as they are. With ingredient (D3), the second parameter branches out: two summands P_<sub>a,b</sub>_ become P<sub>_a,b_+1</sub> and P<sub>_a,b_-1</sub>. For example, ingredient (D3) with _b=a_, applied to two of the summands, continues (1.1):<tbc>

\(\mathsf{P}_{a,a}\oplus_1\mathsf{P}_{a,a}\oplus_1\mathsf{P}_{a,a}\oplus_1\cdots\oplus_1\mathsf{P}_{a,a}\triangleleft\mathsf{P}_{a,a+1}\oplus_1\mathsf{P}_{a,a-1}\oplus_1\mathsf{P}_{a,a}\oplus_1\cdots\oplus_1\mathsf{P}_{a,a}.\)

<tbc>With ingredient (D4), a summand P<sub>_a,_3_b+a_-1</sub> with a large second parameter 3_b+a_-1 becomes three summands with second parameter _b_, one of them with its second and third legs exchanged. In this way one can reach summands with second parameter 1, which are matrix multiplication tensors, since \(\mathsf{P}_{a,1}\cong\langle a,1,1\rangle\) and \((23)\cdot\mathsf{P}_{a,1}\cong\langle 1,a,1\rangle\). For example, a summand P<sub>_a,a_+2</sub>, which three applications of ingredient (D3) produce from four copies of P_<sub>a,a</sub>_, becomes three matrix multiplication tensors by ingredient (D4) with _b_=1:

\(\mathsf{P}_{a,a+2}\triangleleft\mathsf{P}_{a,1}\oplus_1((23)\cdot\mathsf{P}_{a,1})\oplus_1\mathsf{P}_{a,1}\cong\langle a,1,1\rangle\oplus_1\langle 1,a,1\rangle\oplus_1\langle a,1,1\rangle.\)

All in all, we see that after (1.1), applying (D3) and (D4) will let us produce certain partial direct sums of matrix multiplication tensors.

### 1.2.2 From partial direct sums to \(\langle n,n,n\rangle\) via symmetrisation and powering

Suppose that in the above manner the _n_ copies of P_<sub>a,a</sub>_ of (1.1) become a partial direct sum that contains _s_ copies of \(\langle a,1,1\rangle\) and _t_ copies of \(\langle 1,a,1\rangle\). (Note that here we have not yet specified explicitly what _s_ and _t_ can be; applying the above ideas cleverly will have to optimise this; We will discuss this via an example in a moment.) The partial direct sum of the _s_ copies of \(\langle a,1,1\rangle\) is \(\langle a,1,1\rangle\otimes\langle 1,1,s\rangle\cong\langle a,1,s\rangle\), and likewise the partial direct sum of the _t_ copies of \(\langle 1,a,1\rangle\) is \(\langle 1,a,t\rangle\). Together with (1.1), this gives<tbc>

\(\langle 2a-1\rangle\otimes\langle 1,1,n\rangle\triangleleft\langle a,1,s\rangle\oplus_1\langle 1,a,t\rangle.\) (1.2)

