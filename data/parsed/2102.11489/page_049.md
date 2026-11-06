to remain unsatisfied, it must receive at least _d/_2 rejections. This means that at most 32|_U|/_log<sup>4</sup>_m_ left vertices can remain unsatisfied.

**Fact 13.5.** _Suppose that_ \(n'\) _is sufficiently large. Then, after_ \(\mathsf{iter}:=\mathrm{log}n'/\mathrm{loglog}n'\) _iterations, all left vertices become satisfied._

_Proof._ We only need to make sure that \(\left(\frac{32}{\mathrm{log}^4m}\right)^\mathsf{iter}\cdot m<1\), that is,

\(\mathsf{iter}>\mathrm{log}m/\mathrm{log}\left(\frac{\mathrm{log}^4m}{32}\right)=\frac{\mathrm{log}m}{4\mathrm{loglog}m-5}.\)

Therefore, for sufficiently large _n_, it suffices to make sure that \(\mathsf{iter}>\frac{\mathrm{log}n'}{\mathrm{loglog}n'}\).

**Circuit implementation.** We now discuss how to implement the above meta algorithm in circuit.

• To determine whether each super-element is real or not, all super-elements in parallel run the counting circuit of Fact 6.3 and then call a comparator circuit of Fact 6.2. In total, this step takes _O(n_) generalized boolean gates and _O_(loglog_n_) depth.<tbc>

• To determine whether each chunk is sparse or dense, all chunks in parallel run the counting circuit of Fact 6.3 and then call a comparator circuit of Fact 6.2. In total, this step takes \(O(n')\) generalized boolean gates and _O_(log_d_)=_O_(loglog_n_) depth.<tbc>

• Next, we invoke the ProposeAcceptFinalize algorithm. In each iteration:<tbc>

– Every facility (i.e., right vertex) need to tally how many proposals it received, and decide whether it wants to send rejections or acceptance messages. For each facility, this requires a counting circuit of Fact 6.3, and a comparator circuit of Fact 6.2. Then, the decision can be propagated over a binary tree to all _d_ edges. Accounting for all facilities, this step in total requires \(O(n')\) generalized boolean gates and _O_(log_d_)=_O_(loglog_n_) depth.<tbc>

– Every factory (i.e., left vertex) needs to tally how many acceptance messages it has received, and decide if it wants to mark itself as satisfied. If it marks itself as satisfied, it will also mark all edges over which an acceptance message is received as being part of the matching _M_. This can be done in a similar fashion as how facilities tally their proposals, in total taking \(O(n')\) generalized boolean gates and _O_(loglog_n_) depth.<tbc>

Accounting for all \(\mathrm{log}n'/\mathrm{loglog}n'\) iterations, the total depth is at most _O_(log_n_), and the total number of generalized boolean gates is at most \(O(n')\cdot\mathrm{log}n'/\mathrm{loglog}n'=O(n)\).<tbc>

• Next, each dense chunk \(u\in L\) must send one real super-element over each of an arbitrary subset of \(\mathsf{load}(u)\le d/2\) edges outgoing from _u_ in the matching _M_. This can be accomplished by invoking an instance of **SlowDistr** (Corollary 13.2) for each chunk, such that in each dense chunk, each real super-element is sent over an edge in _M_. Thus, each chunk takes \(O(\lfloor d/2\rfloor\cdot(w\mathrm{log}n+\mathrm{log}\lfloor d/2\rfloor))=O(\lfloor d/2\rfloor\cdotw\mathrm{log}n)\) number of generalized boolean gates and \(O(\lfloor d/2\rfloor)\) total number of \((w\cdot\mathrm{log}n)\)-selector gates. Accounting for all chunks, the total number of generalized boolean gates is at most \(O(m\cdot\lfloor d/2\rfloor\cdot w\mathrm{log}n)=O(nw)\), the total number of \((w\cdot\mathrm{log}n)\)-selector gates is at most _O(n/_log_n_), and the depth is at most \(O(\mathrm{log}^2\lfloor d/2\rfloor)=O(\mathrm{log}n)\). Recall that each \((w\cdot\mathrm{log}n)\)-selector gate can be implemented as _O_(log_n_) number of _w_-selector gates, and using _O_(log_n_) generalized boolean gates to propagate the flag over a binary-tree of log_n_ leaves and depth loglog_n_.<tbc>

