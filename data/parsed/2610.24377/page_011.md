subroutine call, except for a single global counter that lets the machine know which step of the algorithm to perform. This means that the total clean space usage will be log(# steps), for the counter, plus \(\mathrm{max}_\ell\)(clean space overhead at the \(\ell\)th layer of recursion).

Our algorithm \(A_{\ell+1}\) proceeds as follows (erasing the clean space in between each step):

i) For each gate _g_ on layer \(\ell+1\) of the circuit, determine \(i_g=\sum_{g^\prime|g^\prime\text{is an input gate to}g}R_{g^\prime}\mathrm{mod}f_g\), and set \(R_g\leftarrow R_g-R_g^{(i_g)}\mathrm{mod}w\).<tbc>

ii) Run _A_.<tbc>

iii) For each gate _g_ on layer \(\ell+1\), determine \(j_g=\sum_{g^\prime|g^\prime\text{is an input gate to}g}R_{g^\prime}\mathrm{mod}f_g\). Now, for every value _t_ such that _g_ would output 1 if exactly _t_ inputs were 1, set \(R_g^{j_g-t}\leftarrow R_g^{j_g-t}+1\mathrm{mod}w\).<tbc>

iv) Run _A_ in reverse.<tbc>

v) Once more, for each gate _g_ on layer \(\ell+1\), determine \(i_g=\sum_{g^\prime|g^\prime\text{is an input gate to}g}R_{g^\prime}\mathrm{mod}f_g\). This time, set \(R_g\leftarrow R_g+R_g^{(i_g)}\mathrm{mod}w\).

We claim this will result in every gate on the \(\ell+1\)st layer being computed. Observe that the values of _i<sub>g</sub>_ computed in steps i) and v) will be identical, and that the value of _j<sub>g</sub>_ computed in step iii) will be equal to _i<sub>g</sub>_+(# of 1s among input wires to _g_)mod_f<sub>g</sub>_. So, step iii) will increment \(R_g^{i_g}\) by 1 if and only if the number of 1s among inputs to _g_ would make _g_ output 1. Otherwise, \(R_g^{i_g}\) will remain unchanged. Since we subtract off from _R<sub>g</sub>_ the initial value of \(R_g^{i_g}\), and then add back in the final value of \(R_g^{i_g}\), this procedure will result in _g_ being computed.

Observe also that each step can be computed with low space overhead (we simply do memory lookups and compute running sums), and that this sequence of operations is reversible (every step either performs some linear operations, based on the indices specified by some registers that remain constant, or else consists of calling _A_). To bound the runtime, observe that \(A_{\ell+1}\) makes two recursive calls to \(A_\ell\), and then for each gate performs a number of register lookups and additions proportional to that gate’s fan-in, meaning at most _O(w_) total such operations. So, the overall runtime is at most \(\widetilde{O}\left(w2^d\right)\).

## 3.2 Application: Integer Multiplication

The ability to quickly evaluate low-depth circuits of symmetric gates is in fact a very useful algorithmic tool. Observe that Theorem 1.1 gives an algorithm with runtime near-linear in the circuit size whenever _d=o_(log_w_). We use this fact here to directly obtain near-linear-time catalytic logspace algorithms for several fundamental problems.

First, we observe that this gives us a near-linear-time algorithm for evaluating any NC<sup>1</sup> circuit:

**Lemma 3.1.** Given a fan-in 2 boolean circuit of size _S_ and depth _O_(log(_S_)), there exists a catalytic algorithm which computes the circuit’s output using _O_(log(_S_)) clean workspace and _S_<sup>1+_O_(1/loglog(_S_))</sup> time.

_Proof._ We observe that any such circuit can be easily converted into a SYM circuit of depth log(_S)/_loglog(_S_) and size _S_<sup>1+_O_(1/loglog(_S_))</sup>. That is, we show how to replace loglog(_S)/_100 layers of fan-in-2 gates with _O_(1) layers of arbitrary fan-in SYM gates. Observe that an output at the end of those loglog(_S)/_100 layers can only depend on at most 2<sup>loglog(_S)/_100</sup>=log(_S_)<sup>1/100</sup> inputs. We can build a constant-depth SYM circuit which checks whether those inputs equal each of the 2<sup>log(_S_)</sup><sup>1/100</sup> possible settings, and returns the correct value for each. This requires 2<sup>_O_(log(_S_)<sup>1/100</sup>)</sup> wires. So, using 2<sup>_O_(log(_S_)<sup>1/100</sup>)</sup> wires for each gate of the original circuit, we can replace every loglog(_S)/_100 layers of the original circuit with circuits of this form. The overall statement holds by plugging that resulting circuit into Theorem 1.1.

From this, we immediately get fast catalytic algorithms for any problems for which we know small NC<sup>1</sup> circuits. For instance:

