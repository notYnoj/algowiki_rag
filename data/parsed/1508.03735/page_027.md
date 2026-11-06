1. _(Feasibility) For each_ \(u_j\in U\), \(|\{i:\mu(a_i)=u_j\}|\le C_j\)<tbc>

2. _(No Blocking Pairs with Filled Seats) For each_ \(a_i\in A\)_, and each_ \(u_j\in U\) _such that_ \(\mu(a_i)\neq u_j\)_, either_ \(\mu(a_i)\succ_{a_i}u_j\) _or for every student_ \(a'_i\in\mu^{-1}(u_j)\), \(a'_i\succ_{u_j}a_i\).<tbc>

_3._ _(No Blocking Pairs with Empty Seats) For every_ \(u_j\in U\) _such that_ \(|\mu^{-1}(u_j)|<C_j\)_, and for every student_ \(a_i\in A\) _such that_ \(a_i\succ_{u_j}\emptyset\), \(\mu(a_i)\succ_{a_i}u_j\).

A simple way to specify a matching is to specify an admissions threshold for every school - i.e. a score admit(_j_) that represents the minimum score student the school is willing to accept. A set of admissions thresholds admit defines a matching \(\mu_\text{admit}\) in the natural way, in which every student enrolls in their most preferred school to which they have been admitted:

\(\mu_\text{admit}(i):=argmax_{\succ_{a_i}}\{u_j|\text{score}_{u_j}(a_i)\ge\text{admit}(j)\}.\)

A set of admission scores is stable and feasible if the matching it induces is stable and feasible.

Now we give a coordination protocol to coordinate students to select schools that form a stable matching. The protocol crucially relies on the Gale-Shapley deferred acceptance algorithm -- the coordinator will first simulate the dynamics of the deferred acceptance algorithm based on the student profiles, and obtains the stable matching along with the associated admission scores. Then it suffices for the planner to publish the list of admission scores so that all the students can coordinate on the stable matching. We present an score-based deferred acceptance algorithm in Algorithm 7.

**Algorithm 7** Deferred Acceptance (with Admission Scores) Stab(_D_)

**Input:** _n_ students’ data _D_ including their preferences over the schools and score profiles

**for** each school \(u_j\in U\)

admission score admit(_j_)=_n_; temporary enrolled students \(\text{temp}(j)=\emptyset\)

**for** each student \(s_i\in S\): let \(\mu(s_i)=\perp\)

**while** there is some under-rolled school \(u_{j^\prime}\) such that \(|\text{temp}(j')|<C_{j^\prime}\) and \(\text{admit}(j')>1\)

\(\text{admit}(j')\leftarrow\text{admit}(j')-1\)

**for** each student _s<sub>i</sub>_:

**if** \(\mu(s_i)\neq argmax_{\succ_{a_i}}\{u_j|\text{score}_{u_j}(a_i)\ge\text{admit}(j)\}\)

**then** \(\text{temp}(j)\leftarrow\text{temp}(j)\backslash\{a_i\}\)

\(\mu(a_i)=argmax_{\succ_{a_i}}\{u_j|\text{score}_{u_j}(a_i)\ge\text{admit}(j)\}\)

\(\text{temp}(\mu(a_i))\leftarrow\text{temp}(\mu(a_i))\cup\{a_i\}\)

**Output:** the final admission scores {admit(_j_)}

The following is a standard fact about the deferred acceptance algorithm.

**Claim 6.** _The final matching_ \(\mu\) _computed from_ Stab(_D_) _is a stable._

Consider the following coordination protocol: the coordinator will first run Stab and broadcast the set of admission scores, and then based on the score, each student will just enroll in the favorite school that she qualifies, that is

\(argmax_{\succ_{a_i}}\{u_j|\text{score}_{u_j}(a_i)\ge\text{admit}(j)\}.\)

Note that the set of admission scores can be encoded with at most _O(k_log(_n_)) bits.

**Theorem 8.** _There exists a coordination protocol with coordination complexity of O(k_log_n_) _that coordinates the students to coordinate on a stable matching._

