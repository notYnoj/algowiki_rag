<tbc>O(_n_log_n_) RAM steps on a TM therefore costs up to O(_n_<sup>2</sup>log_n_) steps, and on a single-tape TM sorting provably requires \(\Omega(n^2/logn)\) steps (Hennie, 1965). This overhead is not a quirk of the analysis--it reflects a fundamental mismatch between TMs and algorithms that rely on random memory access or word-level arithmetic. This paper asks: can CoT transformers efficiently simulate algorithms as written in textbooks? We answer affirmatively.

The natural model for describing textbook algorithms efficiently and concisely is the **Word RAM**. A Word RAM program stores data in a random-access memory (RAM) partitioned into _words_ of \(w=\Theta(log(n+t))\) bits--wide enough to address any of the O(_n+t_) cells the program may touch during a _t_-step execution--and it executes a program one instruction at a time, where each instruction runs in O(1) steps. Its primitive operations--memory reads and writes, integer arithmetic, bitwise operations, and comparisons--correspond directly to the operations of modern programming languages and the algorithms textbooks describe. Thus, the standard complexity bounds practitioners know about correspond naturally to the algorithms expressed in the Word RAM model. For example, sorting takes O(_n_log_n_) Word RAM steps and Dijkstra’s algorithm takes O(_E+V_log_V_).

Existing CoT expressivity results establish computational universality by simulating Turing machines (Pérez et al., 2021; Merrill and Sabharwal, 2024). These constructions, however, operate entirely at the TM-instruction level: each CoT token encodes one tape symbol, and each decoding step simulates one TM transition. Routing a Word RAM program of _t_ steps through this construction therefore costs O(_t_<sup>2</sup>) CoT tokens: a Word RAM on a TM already incurs an O(_t_<sup>2</sup>) blowup,<sup>1</sup> and the CoT spends one token per TM step. What is missing is a direct simulation at the Word RAM-instruction level--one that would let CoT transformers execute textbook algorithms at close to their textbook complexity.

We close this gap with direct Word RAM simulations for decoder-only CoT transformers in three settings. _(i)_ First, finite-precision transformers of polylogarithmic width using rightmost-unique hard attention--an interpretable and pedagogical construction emitting O(_w_<sup>2</sup>) tokens per Word RAM instruction, hence O(_tw_<sup>2</sup>)=O(_t_log<sup>2</sup>(_n+t_)) tokens overall, with the per-instruction overhead dropping to O(_w_) for multiplication-free instruction sets. This is essentially tight for discrete CoT: just as a Python program hard-coding a _p_-bit integer must write \(\Omega(p)\) characters, any CoT transcript representing a _w_-bit word must emit \(\Omega(w)\) tokens from a fixed alphabet, giving an \(\Omega(tw)=\Omega(tlog(n+t))\) lower bound. Our Word RAM simulation matches this bound up to one logarithmic factor in general and exactly when multiplication is excluded--already far below the \(\Omega(t^2)\) of TM-based CoT simulations. _(ii)_ Second, _fixed-width_ transformers with _continuous CoT_--which reasons with hidden vectors in place of discrete tokens. These models can invoke a TM oracle for each Word RAM instruction, generalizing the finite-precision setting. _(iii)_ Third, _hybrid_ models--transformers augmented with a linear RNN layer--which can implement the same simulation with _explicit_ CoT. For an instruction set whose individual operations run in time \(\kappa(w)\) on a TM, the latter two constructions take \(\mathcal{O}(t\kappa(w))\) CoT steps, generalizing the results to arbitrary instruction sets. This recovers the same poly-logarithmic overhead as the first setting: for the flat instruction sets we consider, \(\kappa(w)=\mathcal{O}(w)\) when multiplication, division, and modulo are excluded and O(_w_<sup>2</sup>) otherwise, so \(\mathcal{O}(t\kappa(w))\) is O(_t_log(_n+t_)) or O(_t_log<sup>2</sup>(_n+t_)) accordingly.

## Contributions.

In summary, we prove that CoT transformers can directly simulate Word RAM algorithms with only poly-logarithmic overhead per instruction, matching an information-theoretic lower bound for discrete CoT up to a single logarithmic factor. Specifically, as summarized in Tab. 1:

(i) **Polylogarithmic-width transformers (§3).** Fixed-precision transformers of log<sup>2</sup>(_n+t_) width with rightmost-unique hard attention can simulate Word RAM programs. A Word RAM running _t_<tbc>

<sup>1</sup>In general, each random-access step forces the TM to scan a tape region of length O(_t_) to reach the addressed cell.

RAM step s
RAM step s+1
0110 1001 1010
mem
# a1
# v1
mem
# a
# v
1011 0010 0101
mem
# a1
# v1
TM-oracle scratch

Figure 1: **Schematic of the CoT transcript simulating a Word RAM program.** Within each slot, the model may emit TM-oracle scratch tokens--intermediate computations used to carry out the instruction--before committing the resulting memory updates as a list of address--value pairs.

