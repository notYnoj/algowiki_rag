[VW18] Virginia Vassilevska Williams and R. Ryan Williams. "Subcubic Equivalences Between Path, Matrix, and Triangle Problems". In: _J. ACM_ 65.5 (2018), 27:1–27:38. doi: `10.1145/3186893`. url: `https://doi.org/10.1145/3186893`.

[Weg87] Ingo Wegener. _The Complexity of Boolean Functions_. Wiley-Teubner Series in Computer Science. Chichester and Stuttgart: John Wiley & Sons and B. G. Teubner, 1987. isbn: 0-471- 91555-6.

[Wil25] R. Ryan Williams. "Simulating Time with Square-Root Space". In: _Proceedings of the 57th Annual ACM Symposium on Theory of Computing_. S ’25. Prague, Czechia: Association for Computing Machinery, 2025, pp. 13–23. isbn: 9798400715105. doi: `10.1145/3717823. 3718225`. url: `https://doi.org/10.1145/3717823.3718225`.

[Yes84] Yaacov Yesha. "Time-Space Tradeoffs for Matrix Multiplication and the Discrete Fourier Transform on any General Sequential Random-Access Computer". In: _J. Comput. Syst. Sci._ 29.2 (1984), pp. 183–197. doi: `10.1016/0022-0000(84)90029-1`. url: `https://doi.org/ 10.1016/0022-0000(84)90029-1`.

## A Quickly converting between registers over different moduli

For the remaining part of this appendix, we will fix an arbitrary modular ring K=Z_/m_Z representable in \(b:=\lceil logm\rceil\) bits. (We further assume \(O(logb)\le S\) for space _S_ algorithms.) We show that we can efficiently convert between catalytic algorithms which compute the output by adding it into _N_ registers over a modular ring Z_/m_Z and those which bitwise XOR the _N_-element output into dirty space (represented as _N_ concatenated _b_-bit blocks), and consequently registers over different moduli.

In the proofs below we will assume that all the _b_-bit dirty space chunks for any modular ring register represent a valid value in K (this is not always true when _m_ is not a power of two). We can use pre- processing and post-processing from the scheme of \[CDKMR26, Appendix A\] to assume this WLOG with only a poly(_b_)=polylog(_m_) time multiplicative overhead.

First, we use a simple helper lemma.

**Lemma A.1.** Assume there exists an algorithm which XORs a value \(v\in\{0,1\}^M\) onto a catalytic tape in time _T_, clean space _S_, and catalytic space _C_. Then, there exists an algorithm which adds \(v_i\in\{0,1\}\) to register _R<sub>i</sub>_ over K in the catalytic tape using time \(T\cdot\mathsf{polylog}(m)\), clean space _O(S_), and catalytic space _O(C_).

_Proof._ Allocate _M_ registers _R<sub>i</sub>_ over K in the catalytic tape. First, XOR the _i_th bit of the dirty space input section into the least significant bit (LSB) of _R<sub>i</sub>_ for all _i_. Run the catalytic algorithm XORing _v_ onto this chunk. XOR the _i_th bit into the LSB of _R<sub>i</sub>_ again. This procedure keeps _R<sub>i</sub>_ the same if _v<sub>i</sub>_=0 and adds \(\pm 1\) otherwise. In order to remove the negative sign, square the value added to each _R<sub>i</sub>_ by using \[BCKLS14\] transparent multiplication over K. Run these programs in parallel so only _O_(1) calls to the above \((0,\pm 1)\) procedure are used.

We can now show register modular ring output implies XOR output.

**Lemma A.2** (MOD _m_ to XOR)**.** Assume there exists an algorithm A adding vector \(v\in\mathcal{K}^N\) onto catalytic tape registers in time _T_, clean space _S_, and catalytic space _C_. Then, there exists an algorithm which bitwise XORs _v_ onto a block of catalytic tape in time \(T\cdot\mathsf{polylog}(m)\), clean space _O(S_), and catalytic space _O(C_).

_Proof._ Suppose the _Nb_-bit output dirty space block algorithm A uses is initialized to \(\tau\in\{0,1\}^{Nb}\). Let \(\tau_i\in\{0,1\}^b\) represent the initial _b_-bit value at register _R<sub>i</sub>_. Observe that by running A appropriately, we can<tbc>

