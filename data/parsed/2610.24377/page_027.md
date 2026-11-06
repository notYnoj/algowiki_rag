toggle between having \(a:=(\tau_i)_{i\in[N]}\) or \(c:=(\tau_i+v_i)_{i\in[N]}\) in the catalytic tape.<sup>17</sup> In particular, we have read-access (and therefore XOR-access) to these values.

Allocate 2_Nb_ registers over Z/2_<sup>k</sup>_Z (for a _k_ discussed shortly). Add the _j_th bit of _a_ and _c_ onto _R_<sub>2_j_</sub> and _R_<sub>2_j_+1</sub> respectively for all _j_ using Lemma A.1, while only running A a constant number of times. (We can XOR the value of _a_ all at once onto any place in the catalytic tape. We can similarly do this for _c_ by toggling.) There exists an _NC_<sup>1</sup> circuit which given two values \(a_i,c_i\in\mathcal{K}\) finds _c<sub>i</sub>-a<sub>i</sub>_ over K. Let _k_ be the value needed for the power-of-two registers used in Theorem 1.1 for our circuit. Using Theorem 1.1, evaluate _N_ instances of this circuit in parallel in time \(O(T+N\cdot poly(b))\) and \(O(logb)\le O(S)\) additional space. As the output of the circuit evaluation will be in a bitwise XOR form, we can XOR the value \((c_i-a_i)_{i\in[N]}=(v_i)_{i\in[N]}\) onto a desired block.

**XOR-output to modular output.** We observe it is possible to go from XOR output to modular ring output with only a poly(_b_) overhead as well. This follows from first applying Lemma A.1 to add an XOR- access bit into a corresponding register in K (_Nb_ registers total); then, for each output ring register (_N_ total), accumulate the sum of the _k_th least significant bit register multiplied by 2_<sup>k</sup>_ over all _k_. (Do this in parallel over all output registers to maintain only a polylog(_m_) overhead.)

**Modulo _m_ output to modulo _a_ output.** We additionally observe that we can convert from an algorithm which adds values to registers mod _m_ to an algorithm which subsequently takes the remainder mod some other value.

**Lemma A.3** (MOD _m_ to MOD _a_)**.** Let _m,a_ be positive integers where 1_\<a\<m_, and \(v\in\mathbb{Z}^N\) be a vector where each entry has magnitude at most _a_ for all \(i\in[N]\). Assume there exists an algorithm adding vector _v_ onto catalytic tape registers over Z_/m_Z in time _T_, clean space _S_, and catalytic space _C_. There exists an algorithm running in time _T_polylog(_m_), clean space _O(S_), and catalytic space _O(C+N_polylog(_m_)) which instead adds _v_ over Z_/a_Z.

_Proof._ First, convert the added output over Z_/m_Z registers to XOR form by Lemma A.2. Then, convert to Z_/a_Z register form by the previous XOR to modular register output remark.

<sup>17</sup>To revert from \((\tau_i+v_i)_{i\in[N]}\) to \((\tau_i)_{i\in[N]}\) simply negate all the _N_ registers, run A, and negate all the registers again. This is a standard trick to get the inverse (i.e. subtract).

