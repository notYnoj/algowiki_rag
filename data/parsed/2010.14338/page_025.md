Combining this lemma with Theorem 21 gives the following result.

**Corollary 25.** _There is an O_(loglog_n)-approximation algorithm for_ MinGMConn _with complete k-partite demands._

## G Geometric Demands

In this section, we consider restricted demands that are defined implicitly by geometry. We present improved approximation algorithms for these instances. First, we start with some definition.

**Definition 26.** Let (_P,D_) be an input to MinGMConn. The input demand _D_ is _uniform_ in _P_ if, for every pair \(p,q\in P\), we have a demand \((p,q)\in D\).

The following theorem was proved in Harmon’s thesis \[16\].

**Theorem 27.** _There is a Greedy algorithm that, on input_ (_P,D_) _with uniform demand, produces a feasible solution of cost at most_ \(2\cdot\mathsf{OPT}(P,D)\).

**Definition 28.** Let (_P,D_) be an input to MinGMConn. The input demand _D_ is called _disk demand_ if, for each point \(p\in P\), there exists a radius _r<sub>p</sub>_ such that, \((p,q)\in D\) if and only if \(||p-q||_1\le r_p+r_q\).

In other words, the disk demands are the demands that are defined by an intersection graph of disks. A special case that is of interest to us is the following:

**Definition 29.** We say that the input demand _D_ is a _unit-disk demand_, if there exists a real number _r_ such that \((p,q)\in D\) if and only if \(|p-q|_1\le r\).

We will use the following lemma in our algorithms to bound the cost.

**Lemma 30.** _For any input such that the demand graph_ (_P,D_) _is connected,_ \(\mathsf{OPT}(P,D)\ge|P|-1\).

_Proof._ Let _X_ be the set of points added by an optimal solution. Notice that the Manhattan graph _G<sub>P</sub>_ has |_P_| singleton components. However, the Manhattan graph \(G_{X\cup P}\) contains a single component. Removing one point from any Manhattan graph can only break one component into at most two smaller components; more formally, for any point set \(Y\subseteq\mathbb{R}^2\) and \(p\in Y\) , we have that the number of components in _G_<sub>_Y-p_</sub> and that in _G<sub>Y</sub>_ differs by at most one. Therefore, we must have that \(|X|\ge|P|-1\).

### G.1 Algorithms for Unit-Disk Demand

Here we present an _O_(1)-approximation algorithm. We assume without loss of generality that _D_ is connected; if not, we could apply the same arguments to each connected component separately.

The algorithm has two steps. First, we draw an arbitrary grid G where the space between consecutive horizontal and vertical grid lines is exactly _r/_2; so each grid-cell is an (_r/_2)-by-(_r/_2) cell. Assume that no input points lie on any cell boundaries. Let C be a set of grid cells _C_ such that _C_ contains some input point, that is, \(C\cap P\neq\emptyset\). For each grid cell \(C\in\mathcal{C}\), define the points \(P_C=P\cap C\) inside the cell and _D<sub>C</sub>_ be the induced demands on the points _P<sub>C</sub>_. Observe that for any two points _p,q_ in the same cell _C_, we have \(||p-q||_1\le r\), so a demand \((p,q)\in D_C\). This means that (_P<sub>C</sub>,D<sub>C</sub>_) is in fact an instance with uniform demand. We make the following simple observations.

