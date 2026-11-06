steps with word size \(w=\Theta(log(n+t))\) is simulated using \(\mathcal{O}(t\cdot w^2)=\mathcal{O}(tlog^2(n+t))\) tokens, dropping to \(\mathcal{O}(t\cdot w)=\mathcal{O}(tlog(n+t))\) for multiplication-free instruction sets. The latter matches the \(\Omega(tw)\) lower bound for discrete CoT exactly, the former up to a single _w_ factor.<tbc>

(ii) **Fixed-width transformers with continuous CoT (§5).** A fixed-width, log-precision transformer augmented with continuous CoT--where each reasoning step is a real-valued vector rather than a discrete token--simulates any Word RAM program with \(\mathcal{O}(t\cdot\kappa(w))\) decoding steps, where \(\kappa(w)\) is the TM cost of executing one instruction.<tbc>

(iii) **Hybrid transformer--RNN models (§6).** A fixed-width transformer augmented with a single linear RNN layer simulates any Word RAM program at the same \(\mathcal{O}(t\cdot\kappa(w))\) cost with _explicit_ CoT, showing that recurrence is a natural and practical substitute for the width or continuity extensions of (i) and (ii).

## 2 Preliminaries

### 2.1 The Word RAM Computational Model

There are several different variants of Word RAMs in the literature with different instruction set details, ranging from C-like Word RAMs (Hagerup, 1998; Thorup, 1996; Morin, 2013) to the weaker multiplication-free basic instruction set of Brodnik et al. (1997). While classical literature has often explored various _minimal_, assembly-like instruction sets under which the model is Turing-complete, our goal here is different: we would like to argue that transformers and hybrid models, when equipped with CoT, can directly simulate programs even when they are written in a much higher-level language, such as "textbook algorithms" or simple Python programs, with only a log or log-square overhead. Note that this is a stronger claim than simulating a minimal instruction set with instructions like `load`, `store`, `increment`, etc., with a log or log-square overhead. Keeping this overhead small is important; after all, every Word RAM program can be converted to a Turing machine if one disregards the overhead (which, in general, would be quadratic), and then simulated using standard transformers with CoT via known constructions (Pérez et al., 2021; Merrill and Sabharwal, 2024).

**Syntax.** To this end, we define the following grammar for specifying Word RAM programs. Let _n_ be the input length, _k_ as the maximum number of variables (realized as registers) allowed in the Word RAM program, and `c1, ..., cm` as the fixed constants (independent of _n_) allowed in the program.

\(\text{Line}\rightarrow\text{Var =Expr\unknown haltExpr}\rightarrow\text{Input\unknown Const\unknown Var\unknown Expr OpExpr\unknown UnOpExpr\unknown Expr\unknown}\text{Cond\unknown elseExpr Cond}\rightarrow\text{Bool\unknown Expr CompExpr\unknown CondBoolOp Cond\unknown}\neg\text{Cond Var}\rightarrow\text{Reg\unknown Mem\unknown pcMem}\rightarrow\text{mem\[Expr\]Input}\rightarrow\text{inp\[Expr\]Reg}\rightarrow\text{r1\unknown r2\unknown ...\unknown rkOp}\rightarrow+|-|\times|\div|mod|\checkmark|\gg|\&||\oplus\text{BoolOp}\rightarrow\wedge|\vee\text{UnOp}\rightarrow\neg\text{Comp}\rightarrow<|\le|=|\neq|\ge|>\text{Const}\rightarrow\text{n\unknown c1\unknown c2\unknown ...\unknown cm}\)

The above grammar allows nesting of expressions (e.g., `mem\[mem\[mem\[7\]\]\]`) as well as composition of logical operators over conditionals via the Cond rule. We require that the nesting depth of every expression and condition be bounded by a constant independent of _n_. This is what makes each line<tbc>

\begin{tabular}{ccccccc}
Setting & Precision & Width & Attention & Uniform? & Overhead/step & Result \\
Polylog-width (§3) & fixed & O(log<sup>2</sup>_n_) & rightmost UHAT & no & O(_w_<sup>2</sup>) & Thm. 1 \\
Continuous CoT (§5) & O(log_n_) & fixed & averaging hard & yes & \(\mathcal{O}(\kappa(w))\) & Thm. 3 \\
Hybrid (§6) & O(log_n_) & fixed & averaging hard + RNN & yes & \(\mathcal{O}(\kappa(w))\) & Thm. 4 \\
\end{tabular}

1: The three transformer settings in which we simulate Word RAMs and their trade-offs. Overheads are per simulated RAM step (CoT tokens per instruction); \(w=\Theta(log(n+t))\) is the word size and \(\kappa(w)\) is the TM cost of one instruction. The polylog-width overhead drops to O(_w_) for multiplication-free instruction sets; for the fixed-width settings, \(\kappa(w)=\mathcal{O}(w)\) (simple-arithmetic) or O(_w_<sup>2</sup>) (full-arithmetic) flat instructions.

