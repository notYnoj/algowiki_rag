## B Analyzing entropy flow in Batcher’s sorting network: overwriting model with binary inputs

Here we show that in the overwriting model, the expected heat dissipation of Batcher’s sorting network is _O(n_), matching our bound for our thermodynamic circuit model. We first describe useful heat functions for our analysis, then use these to bound the expected heat dissipation for layers 1 through log_n_ of Batcher’s network, and finish with a recurrence to bound the total heat dissipation. This proof is very similar to the one for our standard circuit model (i.e. Theorem 5.2).

### The overwriting model and its heat functions

In the overwriting model, we view a circuit as a DAG where every node represents a gate and edges indicate input dependence. Unlike in our standard circuit model, the gates in the overwriting model retain their output values in a persistent storage between runs and are not required to erase their inputs. As such, the old output to every gate must be _overwritten_ by a new value during each run of the circuit. For this section, we will be assuming that inputs to our overwriting circuit are independently and identically distributed and will use \(\tilde{Q}\) to denote heat functions for circuits in the overwriting model. If a gate in the overwriting model computes a function \(f:D\rightarrow R\), then it is actually computing the function _h(x,y_)=(_x,f(x_)) for every \(x\in D,y\in R\). As such, the possible heat functions for this gate is given by functions \(\tilde{Q}:D\times R\rightarrow\mathbb{R}_{\ge 0}\) and the validity criteria matches that of Definition 2.21 when the function being computed is _h_.

Since our inputs are independently and identically distributed, there is a significantly simpler expression for the optimal heat function given by Lemma 3.1. Let D be the marginal induced distribution over inputs to our gate (including the output from the previous run), D_<sub>D</sub>_ be the marginal distribution over new input \(x\in D\), and D_<sub>R</sub>_ be the marginal distribution over the old output \(y\in R\). Then, since D is independently and identically distribution, we have that \(\mathcal{D}=\mathcal{D}_D\otimes\mathcal{D}_R\). Thus the optimal heat function for our gate is given by:

\(\tilde{Q}(x,y)=log\frac{Pr_{x,y\sim h(\mathcal{D})}[(x,f(x))]}{Pr_{x,y\sim\mathcal{D}}[x,y]}=log\frac{Pr_{x\sim\mathcal{D}_D}[x]}{Pr_{x\sim\mathcal{D}_D}[x]Pr_{y\sim\mathcal{D}_R}[y]}=log\frac{1}{Pr_{y\sim\mathcal{D}_R}[y]}.\)

So the optimal heat function for gates run on independently identically distributed inputs in the overwriting model is equivalent to the optimal heat function for erasing the value of _f(x_). Thus we will be specifying heat functions in the overwriting model whose only inputs are the values that are about to be overwritten.

### Batcher’s odd-even mergesort on bits

Rather than use the optimal heat function for every gate, in our analysis, we’ll use the three heat functions (parameterized by \(\varepsilon\)) shown in the following table:

In the table, preceding the column for each heat function \(\tilde{Q}_\varepsilon^{(b,b^\prime)}\), are the probabilities for which that function is optimal. For example. \(\tilde{Q}_\varepsilon^{(0,0)}\) is optimal when \((y'_1,y'_2)=(0,0)\) with probability \(1-\varepsilon\),<tbc>

\begin{tabular}{cccccccc}
_x_<sub>1</sub>_,x_<sub>2</sub> & \(y'_1,y'_2\) & Pr & \(\tilde{Q}_\varepsilon^{(0,0)}\) & Pr & \(\tilde{Q}_\varepsilon^{(0,1)}\) & Pr & \(\tilde{Q}_\varepsilon^{(1,1)}\) \\
0,0 & 0,0 & \(1-\varepsilon\) & \(log_2(1/(1-\varepsilon))\) & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) \\
0,1 or 1,0 & 0,1 & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) & \(1-\varepsilon\) & \(log_2(1/(1-\varepsilon))\) & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) \\
1,1 & 1,1 & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) & \(\varepsilon/2\) & \(log_2(2/\varepsilon)\) & \(1-\varepsilon\) & \(log_2(1/(1-\varepsilon))\) \\
\end{tabular}

