imply efficient algorithms for determining optimal thermodynamic parameters are unlikely to exist in general. Nevertheless we can analyze fixed families of circuits to derive bounds in these fixed cases. We first warm up by analyzing two simple implementations of an _n_-ary AND function: a balanced tree (depth log_n_), and a linear chain of (depth _n_), of 2-input AND gates (Section 5.1). We then study the Batcher even-odd sorting networks, analyzing first the Boolean case (Section 5.2) then the case where each wire carries a whole integer (Section 5.2.2).

For all of these results, the upper and lower bounds we show on entropy production are for EP<sub>C</sub> (i.e. they assume that the input distribution is sampled independently from the outside world). This assumption is perhaps stronger than it looks. Since EP measures the total increase in entropy of the universe, this is essentially saying the inputs, which presumably came from somewhere in the universe, are distributed independently of the state of the rest of the universe. Nevertheless, upper bounds on EP<sub>C</sub> which are smaller than Q are still worth studying. When \(\mathsf{EP}_\mathcal{C}\checkmark\mathsf{Q}\) we know that most of the released heat is offsetting the drop in entropy of the marginal input distribution. When EP<sub>C</sub>=0 we know that no circuit could compute the same mapping of inputs to outputs while releasing less expected heat.

## 5.1 Warm-up: entropy-depth tradeoff for computing AND

We note that the circuits we consider in this example are compatible with the overwriting model. Thus the bounds we show here apply equally well to that model of computation under the assumption that inputs to the circuit across runs are independently distributed.

Assume that the input is drawn from the uniform distribution _U<sub>n</sub>_ over {0,1}_<sup>n</sup>_ and say that you want to cleanly compute the function \(\mathsf{AND}(x_1,\dots,x_n)=(x_1\wedge\dots\wedge x_n)\) where _n_ is a power of two using only and gates of the form \(\wedge(x_1,x_2,z)=(x_1,x_2,x_1\wedge x_2)\) and erasure gates _E(x_)=0. Per Lemma 3.1 we know that the optimal heat functions for each of these gates depend on their distributions over inputs. Since \(\wedge(x_1,x_2,z)\) leaves inputs _x_<sub>1</sub>_,x_<sub>2</sub> untouched and it overwrites _z_ with a deterministic function only of _x_<sub>1</sub>_,x_<sub>2</sub>, when inputs _x_<sub>1</sub>_,x_<sub>2</sub> are independently distributed from _z_, the optimal heat function for this gate only depends on the marginal probability distribution over _z_. We can see this as follows for such a product input distribution \(\mathcal{D}=\mathcal{D}_{x_1,x_2}\otimes\mathcal{D}_z\):<tbc>

\(Q_\wedge(x_1,x_2,z)=\mathrm{log}\left(\frac{\mathrm{Pr}_{\wedge(\mathcal{D})}[(x_1,x_2,x_1\wedge x_2)]}{\mathrm{Pr}_\mathcal{D}[(x_1,x_2,z)]}\right)=\mathrm{log}\left(\frac{\mathrm{Pr}_{\mathcal{D}_{x_1,x_2}}[(x_1,x_2)]}{\mathrm{Pr}_{\mathcal{D}_{x_1,x_2}}[(x_1,x_2)]\mathrm{Pr}_{\mathcal{D}_z}[z]}\right)=\mathrm{log}\left(\frac{1}{\mathrm{Pr}_{\mathcal{D}_z}[z]}\right)\)

<tbc>Similarly, per Lemma 3.1, the optimal heat function for _E_ on input distribution D is given by:

\(Q_E(x)=\mathrm{log}\left(\frac{1}{\mathrm{Pr}_\mathcal{D}[x]}\right)\)

Importantly we also have that the expected heat release of these gates is given by E<sub>_x_∼D</sub>\[_Q<sub>E</sub>(x_)\]=H<sub>2</sub>(Pr<sub>D</sub>\[0\])=H<sub>2</sub>(Pr<sub>D</sub>\[1\]).

With these optimal heat functions in mind, we will now analyze the local entropy production of two different fixed Boolean circuits computing \(\mathsf{AND}(x_1,\dots,x_n)=(x_1\wedge\dots\wedge x_n)\) using these gates.

The first we consider is the binary tree composed of \(\wedge(x_1,x_2,z)\) gates on pairs of inputs _x_<sub>1</sub>_,x_<sub>2</sub> and an initially zeroed wire _z_. After executing each of these gates, we apply _E(x_) gates on the wires containing the values of _x_<sub>1</sub> and _x_<sub>2</sub>. Since each \(\wedge(x_1,x_2,z)\) gate in this circuit is run with _z_=0, they can all be implemented with the heat function \(Q_\wedge(x_1,x_2,0)=0,Q_\wedge(x_1,x_2,1)=\infty\) and have an expected heat release of zero. Thus it is only necessary to keep track of the expected heat release<tbc>

