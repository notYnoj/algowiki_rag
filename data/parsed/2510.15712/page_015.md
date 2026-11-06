\(\blacktriangleright\) **Lemma 11.** _In_ \(\alpha\)_, all gate variables in the active circuit are correct, i.e. their output matches what an actual_ NAND _would do for the current values of the inputs._

**Proof.** Suppose not, so there is a gate variable \(g_j^T\neq\mathrm{NAND}(y_1^T,y_2^T)\), where \(y_1^T,y_2^T\) are the variables feeding into gate _g<sub>j</sub>_ (either earlier gates or input variables). Changing the value of \(g_j^T\) leaves clauses in group 0 unaffected; in group 1 we satisfy an additional clause of \(f\rightarrow(g_j^T\leftrightarrow\mathrm{NAND}(y_1^T,y_2^T))\) (4.1) belonging to gate _j_ in TOP while not violating any gate coming before _j_; we might violate lower-priority clauses. The total satisfied weight improves and \(\alpha\) was not a local optimum. \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 12.** _Suppose_ \(\alpha(s_i^B)=1\) _for some shadow variable_ \(s_i^B\)_. Then all gate variables in_ BOTTOM _are correct._

**Proof.** Otherwise, if some gate variable \(g_j^B\) were incorrect, we could simply change \(\alpha(s_i^B)\) to 0; this would not affect groups 0 and 1; in group 1b the currently violated clause \(s_i^B\rightarrow(g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B)\) (4.10) would become satisfied, and no additional clause in group 1b would become violated, so this would improve the satisfied weight, and \(\alpha\) would not be a local optimum. \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 13.** _In_ \(\alpha\)_, all gate variables in the inactive circuit are correct._

**Proof.** If some \(\alpha(s_i^B)=1\) this follows from Lemma 12. So we can assume (\*) that \(\alpha(s_i^B)=0\) for all shadow variables. For the sake of contradiction, suppose some gate variable \(g_j^B\) is incorrect: \(g_j^B\neq\mathrm{NAND}(y_1^B,y_2^B)\). What happens when we flip \(g_j^B\)? Clauses in group 0 are unaffected; clauses in group 1 concerning the bottom circuit are of the form \(\neg f\rightarrow(g_{j^\prime}^B\leftrightarrow\mathrm{NAND}(y_3^B,y_4^B))\) (4.2) and thus are and stay satisfied by \(\alpha(f)=1\). Group 1b stays satisfied because all shadow variables are 0 (in TOP by Lemma 10; in BOTTOM by assumption (\*)). If \(g_j^B\) is a value output variable \(v_i^B\) then group 2 contains \(\neg f\rightarrow(o_i\le v_i^B)\vee s_i^T\) (4.6); if \(g_j^B\) is a best-neighbor output variable \(z_{j^\prime}^B\) then group 3 contains clause \(\neg f\rightarrow(z_{j^\prime}^B=x_{j^\prime}^T)\) (4.3); both are and stay satisfied by \(\alpha(f)=1\). In group 4, changing the value of \(g_j^B\) will satisfy all of \(g_j^B\leftrightarrow\mathrm{NAND}(y_1^B,y_2^B)\), of which at least one was previously violated, and violate only lower-priority clauses, due to the clauses being ranked by the topological order on the gates. Thus, we improve the total weight, meaning that \(\alpha\) was not a local optimum. \(\blacktriangleleft\)

Let us summarize: all shadow variables in TOP are 0, and all gates are correctly evaluated. Formally: \(\alpha(\mathbf{z}^T)=C_N(\alpha(\mathbf{x}^T))\); \(\alpha(\mathbf{v}^T)=C_V(\alpha(\mathbf{x}^T))\); \(\alpha(\mathbf{z}^B)=C_N(\alpha(\mathbf{x}^B))\); \(\alpha(\mathbf{v}^B)=C_V(\alpha(\mathbf{x}^B))\). Next, we show that BOTTOM’s input is equal to TOP’s output.

\(\blacktriangleright\) **Lemma 14.** _If_ \(\alpha(s_i^B)=1\) _then_ \(\alpha(\mathbf{x}^B)=\alpha(\mathbf{z}^T)\).

**Proof.** If not, then \(\alpha(x_j^B)\neq\alpha(z_j^T)\) for some \(1\le j\le n\). Then clause \((s_i^B\wedge f)\rightarrow(z_j^T=x_j^B)\) (4.9) from group 1b is violated. If we change \(s_i^B\) to 0 we satisfy it and do not violate any other clause of group 1b since \(s_i^B\) only occurs negatively here; group 0 does not contain \(s_i^B\) at all. \(\blacktriangleleft\)

\(\blacktriangleright\) **Lemma 15.** \(\alpha(\mathbf{x}^B)=\alpha(\mathbf{z}^T)\).

**Proof.** If some \(s_i^B\) is set to one, this follows from Lemma 14. So we can assume that all shadow variables are 0. For the sake of contradiction, suppose there is some \(1\le j\le n\) with \(\alpha(z_j^T)\neq\alpha(x_j^B)\). We distinguish three cases.

**Case 0:** \(\alpha(\mathbf{x}^B)\) and \(\alpha(\mathbf{x}^T)\) are equal. Let us change the value of \(x_j^B\). Group 0 stays satisfied because now exactly one input bit differs; group 1 stays satisfied because \(\alpha(f)=1\);

