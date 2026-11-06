_Proof of Lemma 17._

(i) Follows from \(1\le\mathtt{depth}_R(x)\le n\) and \(\phi(x)\ge-\mathtt{depth}_R(x)\) for all \(x\in V(T)\).<tbc>

(ii) Immediate by summing (i).<tbc>

(iii) Follows as the minimum in \(\phi(x)\) is taken over a larger set.<tbc>

(iv) Suppose there are two nodes _x_<sub>1</sub>_,x_<sub>2</sub> of minimum depth in _R_. Then they have a proper least common ancestor _x_ in _R_ and since _x_ separates _x_<sub>1</sub>_,x_<sub>2</sub> in _S_, we have \(x\in A\).

_Proof of Lemma 16._<br>
Both phases consist of ZIG, ZIG-ZIG, and ZIG-ZAG steps, as defined in Algorithm 3.

We bound the _increases_ in node potential due to these elementary steps, denoted \(\Delta\phi\), then sum up the individual increases, multiplied by _d_ to get a bound on the total increase in potential. We refer to node names as in Algorithm 3 and Figure 5. By \(\phi\) and \(\phi'\) we denote respectively, the potential before and after the elementary step. By _N<sub>x</sub>_ and \(N'_x\) we denote the set of nodes in the subtree rooted at _x_ before, resp. after the elementary step.

**ZIG:** Only nodes _p_ and _x_ change potential.

\(\Delta\phi=\phi'(p)+\phi'(x)-\phi(p)-\phi(x)\)<br>
\(\le 2(\phi'(x)-\phi(x))\triangleright\text{by Lemma 17(iii)}\)<br>
\(\le 3(\phi'(x)-\phi(x)).\triangleright\text{since}\phi'(x)\ge\phi(x)\)

**ZIG-ZIG:** Only nodes _g_, _p_, and _x_ change potential.<br>
Lemma 17(iv) implies that there is a unique node \(y\in N'_x\) with minimum depth in _R_. Since \(N_x\cap N'_g=\emptyset\) and \(N_x\cup N'_g\subseteq N'_x\), either \(y\notin N_x\), which implies \(\phi'(x)\ge\phi(x)+1\), or \(x\notin N'_g\), which implies \(\phi'(x)\ge\phi'(g)+1\). Thus, \(\phi(x)+\phi'(g)+1\le 2\phi'(x)\). It follows that:

\(\Delta\phi=\phi'(g)+\phi'(p)+\phi'(x)-\phi(g)-\phi(p)-\phi(x)\)<br>
\(=\phi'(g)+\phi'(p)-\phi(p)-\phi(x)\triangleright\text{since}\phi'(x)=\phi(g)\)<br>
\(\le(2\phi'(x)-\phi(x)-1)+\phi'(p)-\phi(p)-\phi(x)\triangleright\text{by Lemma 17(iv)}\)<br>
\(\le 3(\phi'(x)-\phi(x))-1.\triangleright\text{by Lemma 17(iii)}\)

**ZIG-ZAG:** Only nodes _g_, _p_, and _x_ change potential.<br>
Since \(N'_g\cap N'_p=\emptyset\) and \(N'_g\cup N'_p\subseteq N'_x\), by Lemma 17(iv), we have either \(\phi'(x)\ge\phi'(g)+1\), or \(\phi'(x)\ge\phi'(p)+1\), so \(\phi'(g)+\phi'(p)+1\le 2\phi'(x)\). It follows that:

\(\Delta\phi=\phi'(g)+\phi'(p)+\phi'(x)-\phi(g)-\phi(p)-\phi(x)\)<br>
\(=\phi'(g)+\phi'(p)-\phi(p)-\phi(x)\triangleright\text{since}\phi'(x)=\phi(g)\)<br>
\(\le\phi'(g)+\phi'(p)-\phi(p)-\phi(x)+(2\phi'(x)-\phi'(g)-\phi'(p)-1)\triangleright\text{by Lemma 17(iv)}\)<br>
\(\le 2(\phi'(x)-\phi(x))-1\triangleright\text{by Lemma 17(iii)}\)<br>
\(\le 3(\phi'(x)-\phi(x))-1.\triangleright\text{since}\phi'(x)\ge\phi(x)\)

Observe that the potential-increases due to the elementary steps telescope within the splaying operation, yielding an increase of \(3(\phi'(x)-\phi(x))-z\), where \(\phi'(\cdot)\) and \(\phi(\cdot)\) denote the node potentials before and after the splaying and _z_ is the number of ZIG-ZIG and ZIG-ZAG operations.

