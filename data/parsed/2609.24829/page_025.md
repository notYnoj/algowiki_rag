## A Verified Triangle Counting

### A.1 Algorithm

Recall our notation: For an edge _e_ and a set of edges _F_, let \(t_e^F\) be the number of triangles in \(\{e\}\cup F\) that include _e_. Let \(t_e:=t_e^E\) where _E_ is the edge set of the graph, \(\Delta_e(G)=\Delta_e=max_et_e\).

In this section, we prove Theorem 3.1.

**Theorem 3.1.** _There exists a single-pass algorithm_ A _which takes one pass over a randomly ordered stream and parameter_ \(\tau\) _such that a) the algorithm uses_ \(s(m,\tau)=\widetilde{O}(\varepsilon^{-2}\delta^{-1}(m/\sqrt{\tau}+T/\sqrt{\tau}))\) _space in expectation, and b) with probability at least_ \(1-\delta-1/poly(n)\):

• _If_ \(T\ge\tau\)_, the output is a_ \((1\pm\varepsilon)\)_-approximation of T._<tbc>

• _If_ \(T<\tau\)_, the output is a_ \((1\pm\varepsilon)\)_-approximation of T or `FAIL`._

_Note that the algorithm has no a priori information about T._

During a single pass, the algorithm collects the various sets of edges. The role of these is as follows: The set _P_ will likely include most of the heavy edges, i.e., edges involved in many triangles. Sets \(E_0,E_1,\dots,E_{log\sqrt{\tau}-1}\) will be used to construct _P_. Together _P_ and \(E_\sqrt{\tau}\) will be used to estimate the number of triangles that include heavy edges. Another set _S_ will be used to estimate the number of triangles that don’t share an edge with many other triangles, i.e., triangles consisting of three light edges.

• **Finding Potentially Heavy Edges:** For \(i=0,1,\dots,log\sqrt{\tau}\), let _V<sub>i</sub>_ be a subset of vertices where each vertex is sampled with probability \(p_i:=min\{1,10\delta^{-1}\varepsilon^{-2}(logn)/2^i\}\). Let _E<sub>i</sub>_ be defined as the set of edges incident to _V<sub>i</sub>_ amongst the first _q<sub>i</sub>m_ elements of the stream, where \(q_i:=2^i/\sqrt{\tau}\). During a pass over the stream, store the following set of edges:<tbc>

<tbc>\(P:=\{e\in E:\text{position of}e\text{in stream is}>q_im\text{and}t_e^{E_i}\ge 1\text{for some}i\}\)<tbc>

• **Colorful Sampling:** Independently assign one of \(C:=\delta\varepsilon^2\sqrt{\tau}/7\) "colors" chosen uniformly at random to each node of the graph. During a pass over the stream, collect all edges whose endpoints are monochromatic. Call this set _S_.<tbc>

• **Post-Processing:** Let \(O=E_{log(\sqrt{\tau})}\) and \(p=p_{log(\sqrt{\tau})}\).<tbc>

<tbc>\(oracle(e)=\left\{\begin{array}{ c c }
\mathbb{L} & \text{if}t_e^O<p\sqrt{\tau} \\
\mathbb{H} & \text{otherwise}
\end{array}\right.\)<tbc>

