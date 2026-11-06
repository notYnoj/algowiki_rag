## 5.2 Matrix Labels

For a rational subspace \(U\subseteq\mathcal{H}\), let _P<sub>U</sub>_ be its orthogonal projection, and let _I<sub>m</sub>_ be the identity matrix on H. Positive definiteness gives \(\mathcal{H}=U\oplus U^\perp\), and row reduction gives rational coefficients. If \(U\subseteq V\) , then

\(P_V-P_U=P_{V\cap U^\perp},\mathrm{rank}(P_V-P_U)=\mathrm{dim}V-\mathrm{dim}U.\) (7)

For every gate, input vertex, and output vertex _u_, write _M<sub>u</sub>_ for the projection onto its assigned subspace. At a gate all operands have the same assigned subspace. Wire segments of data and auxiliary registers join consecutive labels; a temporary copy has its own wire path, beginning at the copy gate and ending after its last addition to a target register. No source or sink is added for this path.

**Lemma 5.3** (Full-rank differences between source and sink matrices)**.** For every session, the difference between its sink and source matrices has full rank:

\(\mathrm{rank}_\mathbb{Q}(M_{t_{\sigma(i)}}-M_{s_i})=m.\) (8)

The sum of ranks over all wire segments, including those of temporary copies, is

\(S=6v^3(m-1)+3v^2Rm+9v^2c=12,508,242,237<Wm.\) (9)

_Proof._ A data pair has source labels _P<sub>U<sub>a</sub></sub>,_0 and terminal labels _I<sub>m</sub>,I<sub>m</sub>-P<sub>U<sub>a</sub></sub>_ on the physical _X,Y_ paths. Because _X_ exits on _Y_ , its session difference is _I<sub>m</sub>_-2_P<sub>U<sub>a</sub></sub>_. This matrix is invertible: (_I<sub>m</sub>_-2_P<sub>U<sub>a</sub></sub>_)<sup>2</sup>=_I<sub>m</sub>_. The other data session and every auxiliary-register session have difference _I<sub>m</sub>_. Thus all session differences have rank _m_, although they need not be the same matrix.

Each data path is nested and grows by _m_-1 dimensions; there are 6_v_<sup>3</sup> such paths. Each of the 3_v_<sup>2</sup>_R_ auxiliary-register paths grows from zero to dimension _m_. Finally, there are 9_v_<sup>2</sup> local invocations, each with copy cost _c_=63. Equation (7) gives the stated sum. Copying and XOR updates performed at a common subspace add only zero-rank segments. Their temporary nature does not remove any charged conversion.

## 5.3 A Strict Saving in Total Rank

Every data pair saves two units relative to two full increases of _m_ dimensions. The temporary copies contribute _c_ per local invocation. Reusing auxiliary registers reduces their number of independent inputs, while their subspace labels still grow by inclusion. Consequently

\(W=3v^2(2v+R),Wm-S=3v^2(2v-3c)=1,219,779,\eta:=1-\frac{S}{Wm}=\frac{33}{338432}>0.\) (10)

The strict inequality is the elementary comparison 2_v_=222_\>_3_c_=189.

**Corollary 5.4** (Fixed parameters for the recursion)**.** Take _m_=512, _W_=24,432,543, _S_=12,508,242,237, \(\varepsilon=1.5\times 10^{-5}\), and \(\tau=1-\varepsilon\). The circuit permutes the input bits and has the matrix-label properties proved above, and

\(\eta=\frac{33}{338432},\frac{S}{W}<m^\tau.\) (11)

_Proof._ Appendix B proves \(\varepsilon\mathrm{ln}m<\eta\) by rational comparisons. Since 1-_x\<e_<sup>-_x_</sup> for _x\>_0, \(S/W=m(1-\eta)<m\mathrm{exp}(-\varepsilon\mathrm{ln}m)=m^{1-\varepsilon}\).

