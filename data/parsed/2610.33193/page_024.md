<tbc>requires computing probabilities induced by the circuit. Nonetheless, we view this as an overall strength of the heat function framework.

## 4.1 PP-complete language for optimizing heat functions

We start with the language L<sub>_Q_-min</sub> that we will prove PP-complete.

**Definition 4.1.** L<sub>_Q_-min</sub> _is a set of tuples_ (C_,g,x,a,b_) _where_ C _is a Boolean circuit, g is a gate in that circuit, x is a potential input to that gate, and q=a/b is a positive rational number. We say that_ \((\mathcal{C},g,x,a,b)\in\mathcal{L}_{Q-\mathrm{min}}\) _if, when_ C _receives the uniform distribution over inputs, there exists some valid heat function Q for gate g that minimizes the expected heat release on its induced marginal input distribution such that_ \(Q(x)\ge\mathrm{log}q\).

We note that our choice to express threshold _q=a/b_ as a rational number whose log corresponds to the optimal expected released heat is for simplicity but is not actually needed. Per Lemma 3.1 the optimal value of _q_ is always the ratio of two integer valued fractions whose numerators are at most 2_<sup>n</sup>_ and whose denominators are both exactly 2_<sup>n</sup>_. Thus we can safely round up any _q_ obtain a rational \(q'\) that is the ratio of two \(\le n+1\) bit integers \(a'\) and \(b'\) without changing membership in L<sub>_Q_-min</sub>.

To show that L<sub>_Q_-min</sub> is PP-hard, we will reduce from the following PP-hard problem \[AW22\].<sup>29</sup>

**Proposition 4.2** (\[AW22\])**.** _Let_ L<sub>SAT/2</sub> _be the subset of_ SAT _instances that evaluate to_ 1 _on at least half of all inputs. Deciding membership in_ L<sub>SAT/2</sub> _is_ PP_-hard._

**Lemma 4.3.** L<sub>_Q_-min</sub> _is_ PP_-hard._

_Proof._ We prove this by Karp reduction from L<sub>SAT/2</sub>. Given a Boolean circuit C, assume its output is the first wire. We modify C by appending a single-wire gate _g_ that erases its input to the first wire at the end of the circuit and call our new circuit \(\mathcal{C}'\). Observe that, due to Lemma 3.1, the optimal heat function for the added gate _g_ releases at least 1 expected heat on input 0 precisely when the probability of that input is at most 1/2. Thus, \((\mathcal{C}',g,0,2,1)\in\mathcal{L}_{Q-\mathrm{min}}\) precisely when \(\mathcal{C}\in\mathcal{L}_{\mathrm{SAT}/2}\).

Next we show that this language is in PP.

**Lemma 4.4.** \(\mathcal{L}_{Q-\mathrm{min}}\in\mathsf{PP}\).

_Proof._ Consider input (C_,g,x,a,b_). Let D be the marginal distribution over inputs to gate _g_ when C receives the uniform distribution over inputs, _f_ be the function computed by gate _g_, _y=f(x_), and _q=a/b_. The value \(q\le 1\) asks if the optimal heat function releases at least 0 expected heat on input _x_. Since such a condition is trivially satisfied by the definition of heat functions, we can automatically accept such inputs. Now we assume that \(a\ge b\). By Lemma 3.1, we know that deciding if \((\mathcal{C},g,x,a,b)\in\mathcal{L}_{Q-\mathrm{min}}\) is equivalent to deciding if \(q=a/b\le\mathrm{Pr}_{f(\mathcal{D})}[y]/\mathrm{Pr}_\mathcal{D}[x]\). We will now construct a non deterministic program that accepts with probability at least 1/2 exactly when<tbc>

<sup>29</sup>A version of this problem where ‘at least’ is replaced with ‘more than’ was proven to be PP-hard in \[Gil74\]. That paper also uses the convention that PP algorithms must accept with probability strictly larger than 1/2 on yes instances. In \[AW22\] the authors show how to convert between these definitions of PP.

