We remark that while the authors of \[6\] do not explicitly use the CONGEST model for computation, their algorithm can easily be implemented in this model.

The randomized variants of **ASM** require faster (randomized) subroutines for computing maximal and "almost maximal" matchings in a communication graph. In Appendix A, we describe how to modify an algorithm of Israeli and Itai \[8\] to give the necessary results.

## 3 Deterministic algorithm description

In this section, we describe in detail the almost stable matching algorithm, **ASM**. The main algorithm invokes the subroutine **QuantileMatch** which in turn calls **ProposalRound**. In Section 3.1 we introduce notation, and describe the internal state of each processor during the execution of **ASM**. Section 3.2 contains a description of the **ProposalRound** subroutine, while Section 3.3 describes the **QuantileMatch** subroutine. Finally, Section 3.4 describes **ASM**.

### 3.1 The state of a processor

In our algorithm, we assume that each player is represented by an independent processor. Each processor has a unique id and a gender (male or female) both of which are known to that processor. The only global information known to each processor is (an upper bound on) _n_, the total number of processors. At each step of the algorithm, we specify the state of each processor as well as any messages the processor might send or receive. The state of a player _v_ consists of:

• Quantized preferences _Q_<sub>1</sub>_,Q_<sub>2</sub>_,...,Q<sub>k</sub>_ where we denote \(Q=\bigcup Q_i\). Initially _Q_<sub>1</sub> is the set of _v_’s deg_v/k_ favorite men, _Q_<sub>2</sub> is her next favorite deg(_v)/k_, and so on. We call _Q<sub>i</sub>w_’s _**ith quantile**_. For \(m\in Q_i\), we write _q(m_)=_i_. If we wish to make explicit the player to whom the preferences belong, we may adorn these symbols with a superscript. For example, \(Q_i^v\) is _v_’s _i_th quantile. Throughout the execution of the algorithm, elements may be removed from _Q_ and the _Q<sub>i</sub>_s, but elements will never be added to any of these sets. We will always use _k_ to denote the number of quantiles for the players’ preferences.<tbc>

• A partner _p_ (possibly empty). The partner _p_ is _v_’s current partner in the matching _M_ our algorithm constructs. To emphasize that _p_ is player _v_’s partner, we will write _p(v_). The (partial) matching _M_ produced by the algorithm at any step is given by \(M=\{(p(w),w)|w\in X,p(w)\neq\varnothing\}\).

Additionally, subroutines of our algorithm will require each processor to store the following variables:

• A set _G_<sub>0</sub> of "neighbors" of the opposite sex which correspond to accepted proposals.<tbc>

• A partner _p_<sub>0</sub> in a matching found in the graph determined by _G_<sub>0</sub>.

Thus each player knows their preferences, partners (if any) as well as any of their accepted proposals from the current round (stored in _G_<sub>0</sub>). The men \(m\in Y\) hold the following additional information:

• A set _A_ of "active" potential mates, initially set to _Q_<sub>1</sub>.

### 3.2 The ProposalRound subroutine

At the heart of our algorithm is the **ProposalRound** subroutine (Algorithm 1). **ProposalRound** works in 5 steps which are described in Algorithm 1.

We observe that if each player _v_ takes _k_=deg_v_, then **ProposalRound** mimics the classical (extended) Gale-Shapley algorithm \[4, 5\]. In this case, each man proposes to his most favored woman that has not yet rejected him, and each woman rejects all but her most favored suitor.

