## A A Coordination Protocol For Many-to-One Stable Matchings

Finally, we present a coordination protocol for the many-to-one stable matchings problem, which is relatively straightforward. A many-to-one stable matching problem consists of _k_ schools _U_={_u_<sub>1</sub>_,...,u<sub>k</sub>_}, each with capacity _C<sub>j</sub>_ and _n_ students _S_={_s_<sub>1</sub>_,...,s<sub>n</sub>_}. Every student _i_ has a strict preference ordering \(\succ_i\) over all the schools, and each school _j_ has a strict preference ordering \(\succ_j\) over the students. It will be useful for us to think of a school _u_’s ordering over students _A_ as assigning a unique _score_ \(\mathsf{score}_u(s)\in\{1,\dots,n\}\) to every student, in descending order (for example, these could be student scores on an entrance exam). Therefore, each student’s private data is \(D_i=(\succ_i,\{\mathsf{score}_u(s)\}_u)\). We recall the standard notion of stability in a many-to-one matching.

**Definition 9.** _A matching_ \(\mu:S\rightarrow U\cup\emptyset\) _is_ feasible _and_ stable _if:_

