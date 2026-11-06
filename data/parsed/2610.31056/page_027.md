In the remainder of this section, we give a proof of Lemma 6.0.1. We first define a collision- finding random variable, and then, by using second-moment-based concentration bounds, we obtain the desired result.

## Distribution of collisions in _B_<sub>_s_<sub>0</sub>_,s_<sub>1</sub>_,s_<sub>2</sub></sub>.

To analyze the distribution of collisions in the list _B_<sub>_s_<sub>0</sub>_,s_<sub>1</sub>_,s_<sub>2</sub></sub>, we first define a random variable C that denotes the number of non-trivial modular collisions in this list. Our filtering algorithm succeeds if the value of these variables is at least 1. Hence, to find the success probability of the algorithm, i.e., the fraction of instances for which the algorithm outputs a collision, we need to find the probability of the event C_\>_0. Formally, we define the random C over a random choice of **a** as follows<tbc>

\(\mathcal{C}:=\left|\left\{\left(\mathbf{u}_i,\mathbf{u}_j\right)\left|\begin{array}{ c c }
i<j, & \mathbf{u}_i,\mathbf{u}_j\in B_{s_0,s_1,s_2}, \\
\mathbf{a}^{(r)}\cdot\mathbf{u}_i\equiv\mathbf{a}^{(r)}\cdot\mathbf{u}_j & \mathrm{mod}r
\end{array}\right\}\right|,\)

<tbc>where \(\mathbf{a}^{(r)}:=\{a_i\mathrm{mod}r\}_{i=1}^n\). And, we have<tbc>

\(\mathbb{P}_\mathbf{a}\left(Algorithm3\text{succeeds}\right)=\mathbb{P}_\mathbf{a}\left(\mathcal{C}>0\right).\)

<tbc>Hence, now our problem reduces to analyzing this random variable C. For any input instance, we can compute the value of C by iterating through all the possible pairs of binary vectors, and considering whether the vectors (or the corresponding subset sum) pass through the filters of the algorithm and collide modulo _r_. We define the following set that contains all the possible binary vectors that can reach the final list _B_<sub>_s_<sub>0</sub>_,s_<sub>1</sub>_,s_<sub>2</sub></sub>.

\(\mathsf{A}:=\{\mathbf{u}\in\{0,1\}^n|\mathbf{u}^{(L)}\neq 0^{n/2},\mathbf{u}^{(R)}\neq 0^{n/2}\}.\)

Let’s assume that the elements of the set A are ordered in a lexicographical sense. Then let A={**u**<sub>1</sub>,**u**<sub>2</sub>_,..._**u**_<sub>N</sub>_}, where **u**_<sub>i</sub>\<_**u**_<sub>j</sub>_ for any \(1\le i<j\le N\) and _N_=(2<sup>_n/_2</sup>-1)<sup>2</sup>=2_<sup>n</sup>_-2<sup>_n/_2+1</sup>+1.

A binary vector **u**_<sub>i</sub>_ survives the filtering algorithm if it satisfies the following events

\(\mathsf{E}_{\mathsf{LS},p}^{(i)}:\mathbf{u}_i^{(L)}\cdot\mathbf{a}^{(p)(L)}\equiv s_0\mathrm{mod}p\text{(Left sum Mod}p)\)<br>
\(\mathsf{E}_{\mathsf{RS},p}^{(i)}:\mathbf{u}_i^{(R)}\cdot\mathbf{a}^{(p)(R)}\equiv s_1\mathrm{mod}p\text{(Right sum Mod}p)\)<br>
\(\mathsf{E}_{\mathsf{TS},q}^{(i)}:\mathbf{u}_i\cdot\mathbf{a}^{(q)}\equiv s_2\mathrm{mod}q\text{(Total sum Mod}q)\)

Now, for each pair of binary vectors **u**_<sub>i</sub>,_**u**_<sub>j</sub>_, we define the binary random variable and C_<sub>ij</sub>_, such that its value is 1 if and only if **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_ survive the filtering algorithm, i.e., the above three events occur for both the vectors **u**_<sub>i</sub>_ and **u**_<sub>j</sub>_, and they collide modulo _r_, i.e., the following event occurs<tbc>

\(\mathsf{E}_{\mathsf{col},r}^{(ij)}:\mathbf{u}_i\cdot\mathbf{a}^{(r)}\equiv\mathbf{u}_j\cdot\mathbf{a}^{(r)}\mathrm{mod}r.\)

<tbc>Now, we write the random variable C as a sum of the binary random variables C_<sub>ij</sub>_ as follows<tbc>

\(\mathcal{C}=\sum_{1\le i<j\le N}\mathcal{C}_{ij}.\)

<tbc>Then, using the linearity of expectation, we have the following

\(\mathbb{E}_\mathbf{a}\left(\mathcal{C}\right)=\sum_{i<j}\mathbb{E}_\mathbf{a}\left(\mathcal{C}_{ij}\right).\)

Using this equation, we compute the first and second moments of the random variable C to prove Lemma 6.0.1.

