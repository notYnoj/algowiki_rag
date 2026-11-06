In Appendix D, we give a simple proof of a result of Wolpert and Kolchinsky \[WK20\], who showed that the entropy production of applying a gate in a circuit is at least the drop in mutual information between the wires in this gate and the state of the remaining wires of the circuit. We reprove this result (Proposition D.1) in the language of heat functions showing that it is an immediate consequence of the locality of valid heat functions, i.e., the fact that heat functions reference a single gate independently of the correlation of its inputs to other gates in the circuit.

## 2 Preliminaries

We use log to denote log<sub>2</sub>, and fix \(2^{-\infty}=0,-\mathrm{log}0=\infty\), as well as \(z/0=\infty\) when _z\>_0. Let D be a distribution over domain _D_ and \(x\in D\). We use Pr<sub>D</sub>\[_x_\] to denote the probability that a random variable _X_∼D has value _x_ (i.e. Pr_<sub>X∼D</sub>_\[_X=x_\]). Let \(S\subseteq D\). We will also use D<sub>|_S_</sub> to denote the distribution D conditioned on the sample being in _S_. More formally, \(\mathrm{Pr}_{\mathcal{D}_{|S}}[x]=\mathrm{Pr}_{X\sim\mathcal{D}}[X=x|X\in S]\). When \(S\cap\mathrm{supp}(\mathcal{D})=\emptyset\), we say that D<sub>|_S_</sub> is undefined. We use E<sub>_x_∼D</sub>\[_f(x_)\] to denote \(\sum_{x\in\mathrm{supp}(\mathcal{D})}\mathrm{Pr}_\mathcal{D}[x]f(x)\).

**Definition 2.1.** _The_ Shannon entropy _of a distribution_ D _is given by_

\(\mathcal{S}(\mathcal{D})=-\mathbb{E}_{x\sim\mathcal{D}}\left[\mathrm{log}\mathrm{Pr}_\mathcal{D}[x]\right]=-\sum_{x\in\mathrm{supp}(\mathcal{D})}\mathrm{Pr}_\mathcal{D}[x]\mathrm{log}\mathrm{Pr}_\mathcal{D}[x].\)

We use _e<sub>i</sub>_ to refer to a vector with the value 1 in the _i_’th index and zero everywhere else. When thinking about function computation, we will often use _D_ to refer to the (finite sized) domain and _R_ to refer to the (finite sized) range. When needed, we will often specify \(D=\Sigma^n\) and \(R=\Sigma^m\) for some finite alphabet \(\Sigma\) containing an element 0. We use _x<sub>i</sub>_ to denote the _i_’th coordinate of _x_ and _f<sub>i</sub>_ to denote the function _i_’th coordinate function of _f_. For \(I\subseteq[n]\) we use _x<sub>I</sub>_ to denote the length-|_I_| vector consisting of _x_ restricted to its coordinates on indices in _I_, and \(\Sigma^I\) to denote the set of all such vectors.

In our model, gates apply a function _f_ to some subset _I_ of the _W_ total wires in the circuit. It is useful to extend this function _f_ to an \(f_\uparrow\) that acts on all _W_ wires of the circuit, but only modifies the wires in _I_ according to _f_, leaving the other wires unchanged. Thus we define the following extension of a function _f_.

**Definition 2.2** (lifting function \(f_\uparrow\))**.** _If_ \(f:\Sigma^I\rightarrow\Sigma^I\) _for some finite set_ \(I=i_1,\dots,i_k\subseteq[W]\)_, then we can define the function_ \(f_\uparrow:\Sigma^W\rightarrow\Sigma^W\) _as:_

\((f_\uparrow)_i(x)=\left\{\begin{array}{ c c }
f_i(x_I) & i\in I \\
x_i & i\unknown\in I.
\end{array}\right.\)

The following definition gives us clean notation for the distribution over states after applying a gate computing some function _f_.

**Definition 2.3** (induced output distribution)**.** _If_ \(f:D\rightarrow R\) _and_ D _is a distribution over D, then we use f_(D) _to denote the distribution over R produced by first sampling x_∼D _and then outputting f(x)._

