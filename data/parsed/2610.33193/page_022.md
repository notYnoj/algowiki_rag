<tbc>produces garbage in addition to its output must erase that garbage before it can be run on a new input. Failing to do so causes real issues; if one extends Definition 2.21 to probabilistic gates, then there are valid heat functions where _Q(x_) may be negative. By using such gates, you can define circuits that appear to violate the second law of thermodynamics until you account for the increase in entropy in their mapping of inputs to outputs.

Much of the complexity associated with reuse/cycling can be simplified by thinking of the circuit as a cog in a larger machine that goes through cycles. Let’s consider a circuit computing a function \(f:\Sigma^n\rightarrow\Sigma^m\) with _W_ total wires. At the start of a cycle, all _W_ wires are initialized to zero. Then some upstream process writes a new input _x_ into the first _n_ wires of our circuit. The circuit will perform its computation in accordance with Definition 2.15, ending in a state where the first _m_ wires contain _f(x_) and all other wires are reset to zero. The value _f(x_) can then be swapped with _m_ fresh zeroes from the downstream process that takes _f(x_) as its input at no cost. Resetting these values is a task for the downstream process. Note that _f_ can be defined to keep a copy of its input. Thus the standard logically reversible mapping _f(x_)=(_x,h(x_)) is allowed in this model, but then _x_ is explicitly part of the output of _f_ and must be handled as such by downstream processes.

## 3 Deriving optimal heat functions

Now we show how to derive the optimal heat function for a known distribution over inputs. Recall that for a logically reversible operation, i.e., computing an injective function \(f:D\rightarrow R\), an optimal heat function is 0 on all inputs. In this case, no matter the input distribution D, since each input _x_ maps to its own unique output _f(x_), Pr<sub>_f_(D)</sub>\[_f(x_)\]=Pr<sub>D</sub>\[_x_\], thus \(log\left(Pr_{f(\mathcal{D})}[f(x)]/Pr_\mathcal{D}[x]\right)=0\). If _f_ is not injective, it remains the case that any input _x_ mapping to its own unique output _f(x_) has zero expected heat released on input _x_. "Colliding" inputs will release more heat the more inputs map to a single output (more precisely, the greater the total probability Pr<sub>_f_(D)</sub>\[_f(x_)\] of inputs _x_ sharing output _f(x_)): \(stilllog\left(Pr_{f(\mathcal{D})}[f(x)]/Pr_\mathcal{D}[x]\right)\) (now strictly positive) is the expected heat released.

**Lemma 3.1.** _Let f be an arbitrary function with domain D and_ D _be a distribution over D. Then any valid heat function for a gate computing f that minimizes the expected heat release on input distribution_ D _satisfies for all_ \(x\in D\):

\(Q(x)=\left\{\begin{array}{ c c }
log(Pr_{f(\mathcal{D})}[f(x)]/Pr_\mathcal{D}[x]) & \text{Pr}_\mathcal{D}[x]>0 \\
\infty & \text{Pr}_\mathcal{D}[x]=0,Pr_{f(\mathcal{D})}[f(x)]>0
\end{array}\right.\)

_on all x where_ \(f(x)\in supp(f(\mathcal{D}))\).<sup>27</sup> _On x where_ \(f(x)\unknown\in supp(f(\mathcal{D}))\)_, Q can behave arbitrarily so long as Q still satisfies Lemma 2.22 on these inputs._

Note that in the finite case, _Q(x_) is the log of the one divided by the probability that the input is _x_, conditional on the output being _f(x_). In other words, the optimal heat function is unique up to the choice of values for inputs with zero probability under the input distribution D and whose outputs also have zero probability under the output distribution _f_(D). While an earlier version of<tbc>

reversible computation; Bennett’s construction \[Ben73,  2\] for efficiently and reversibly computing the mapping \(x\mapsto f(x)\) for bijective _f_ requires both _f_ and _f_<sup>-1</sup> to be efficiently computable, ruling out one-way functions. <sup>27</sup>Note that equivalently \(log(Pr_{f(\mathcal{D})}[f(x)]/Pr_\mathcal{D}[x])=-logPr_\mathcal{D}[x]\) output is _f(x_)\].

