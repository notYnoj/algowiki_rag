<tbc>executable in O(1) Word RAM steps. We also consider a simplified version of this grammar that doesn’t allow nesting. This is obtained by changing the grammar expansion rules for Expr and Cond to not be recursive, as follows:

We call a Word RAM program **flat** if it uses only the flat grammar above. We further distinguish two flat instruction classes by which operators from Op appear: **full-arithmetic** flat programs may use any operator from Op, while **simple-arithmetic** flat programs restrict Op to \(\{+,-,\checkmark,\gg,\&,|,\oplus\}\), i.e., it excludes \(\times\), \(\div\), mod.

**Semantics.** A specific Word RAM machine is specified by a finite-length program of the form above, with the standard semantics when executed on a string \(x\in\Sigma^*\). In more detail, the machine has three memory arrays: a read-only one `inp` that contains the input **_x_**, `mem` is a standard read-write tape initialized to all zeros, and `out` is an output tape that can only be written to, where written values are stored \(\mathrm{mod}|\Sigma|\). The machine state also specifies the value of the program counter `pc` and finite registers `r1`_,...,_`rk`, which all start as 0. When an instruction is run, `pc` is incremented, unless it is otherwise assigned by the instruction (e.g., `pc`=`r2`+1). The program runs until `halt` is executed, at which point the contents of `out` is deemed the output. When considering language recognition, we say that a Word RAM accepts a string iff `out`\[0\]=1.

Without loss of generality, we can view the program counter `pc` and each register `ri` as stored in memory via \(\mathtt{pc}\unknown\mathtt{mem}[0]\) and \(\mathtt{ri}\unknown\mathtt{mem}[-i]\), with `mem` being 1-indexed for standard memory.

## 2.2 Transformers and Related Models

**Transformers.** We defer a definition of the standard transformers model to §A.1. The depth of our transformer will be _fixed_, i.e., O(1), w.r.t. sequence length _n_ and CoT runtime _t_=O(_n<sup>c</sup>_). Regarding precision and width of our transformers, we consider two possibilities motivated by a bifurcation in the transformer expressivity literature (Strobl et al., 2024; Svete et al., 2026):

1. Fixed precision and polylogarithmic, i.e., O(log_<sup>k</sup>n_) width. Because width grows with _n_ and _t_, this model is not fully uniform, meaning new parameters are introduced on longer inputs and CoTs. We use rightmost-unique hard attention transformers ( UHATS) (cf. Strobl et al., 2024).<tbc>

2. Logarithmic, i.e., O(log_n_), precision and fixed width. We further enforce in this model that the parameters are fully uniform. We use averaging hard attention (cf. Strobl et al., 2024).

**Linear RNNs and Hybrid Models.** Next, we define linear RNN layers. There are many existing linear RNN architectures with complex parameterizations that all meet the following general form for different choices of _A<sub>t</sub>_, _b<sub>t</sub>_, and _c<sub>t</sub>_ (Merrill et al., 2026): _S_<sub>_t_+1</sub>=_A<sub>t</sub>S<sub>t</sub>+b<sub>t</sub>_ and \(h_t=c_t^\top S_t\) We will assume for simplicity that _A<sub>t</sub>_, _b<sub>t</sub>_, and _c<sub>t</sub>_ are all parameterized as projections of the input vector to the RNN layer at step _t_. RNNs can be fit into a transformer architecture by using the head input to compute _A<sub>t</sub>,b<sub>t</sub>_, and _c<sub>t</sub>_ and then defining _h<sub>t</sub>_ as the head output. The sublayer output from a multihead RNN layer would then be passed through layer-norm in the standard way. A _hybrid model_ is an architecture that mixes attention heads with linear RNN heads.

**CoT.** Finally, we say that a transformer _T_ computes a function _f_ within CoT budget _t(n_) if, after feeding **_x_** through _T_ and allowing at most _t_(|_w_|) autoregressive steps sampled greedily (potentially terminating early), the generated tokens end with the suffix =_f(w_)$, where = is an output delimiter and $ is the end-of-string symbol. Continuous CoT is defined analogously except that final logits of the transformer are passed as a "soft token" to the next step rather than a token decoded from them.

## 2.3 Layernorm Hash Representation

In the log-precision model, we will represent values _v_ using their layer-norm hash \(\phi(v)\), which is a unit-norm vector in R<sup>4</sup> defined as follows (Merrill and Sabharwal, 2024):

\(\phi(v)\equiv\phi(v,1):=\mathrm{layernorm}(v,1,-v,-1)=\frac{(v,1,-v,-1)}{\sqrt{2v^2+2}}.\) (1)

\begin{tabular}{ccc}
FlatExpr & \(\rightarrow\) & Input | Const | Var \\
Expr & \(\rightarrow\) & FlatExpr | FlatExpr Op FlatExpr | UnOp FlatExpr | FlatExpr `if` Cond `else` FlatExpr \\
Cond & \(\rightarrow\) & Bool | FlatExpr Comp FlatExpr \\
\end{tabular}

