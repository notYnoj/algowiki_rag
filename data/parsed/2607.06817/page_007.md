`python instance\_solver.py palt 4 pmon 5 ref 13`

Its execution gives the following output:

`(False, None)`

This means that the corresponding SAT instance is unsatisfiable, implying \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})\unknown 13\). With these two executions in mind, we conclude that \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})=13\). \(\Diamond\)

Similar to the previous two `Python` files, the `number\_finder.py` module accepts two graphs _H_<sub>1</sub> and _H_<sub>2</sub> from the graph classes of interest, satisfying \(|H_1|,|H_2|\unknown 2\), together with a string indicating which type of Ramsey number is being considered. It then computes the considered Ramsey number by solving SAT instances via the `instance\_solver.py` module for sufficiently many values of _n_. The `number\_finder.py` module can be executed using the following syntax:

`python number\_finder.py \<class\_a\> \<a\> \<class\_b\> \<b\> \<problem\_type\> \[\<starting\_n\>\]`

The first five arguments are required and have the same meaning as in the previous two modules, while the `starting\_n` argument is optional. If this argument is not provided, then the script attempts to generate and solve a SAT instance for each integer _n_ starting from the trivial lower bound max{|_H_<sub>1</sub>|,|_H_<sub>2</sub>|}, until the first unsatisfiable SAT instance is encountered or a timeout is reached. If `starting\_n` is provided and exceeds max{|_H_<sub>1</sub>|,|_H_<sub>2</sub>|}, then it is treated as a nontrivial lower bound on the considered Ramsey number, so the script attempts to generate and solve SAT instances for each integer _n_ starting from `starting\_n`. The user must guarantee that the provided `starting\_n` is a valid lower bound; otherwise, the execution will yield an incorrect result.

The main function of the `number\_finder.py` module returns an ordered pair `(exact, number)`, as follows.

**(1)** If an unsatisfiable SAT instance is encountered for the first time, this means that the corresponding _n_ is equal to the considered Ramsey number. In this case, `exact` is set to `True`, while `number` is set to the computed value of the considered Ramsey number.

**(2)** If a timeout is reached, then the corresponding _n_ is a lower bound on the considered Ramsey number, and it is not known if equality holds. In this case, `exact` is set to `False`, while `number` is set to the obtained lower bound on the considered Ramsey number.

**Example 3.3.** The reflective Ramsey number \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})\) can be computed by executing the following command:

`python number\_finder.py palt 4 pmon 5 ref`

Upon execution, the script prints out the following output:

`palt 4 vs. pmon 5 // ref`

`Inspecting for n = 5... Satisfiable!`

`Inspecting for n = 6... Satisfiable!`

`Inspecting for n = 7... Satisfiable!`

`Inspecting for n = 8... Satisfiable!`

`Inspecting for n = 9... Satisfiable!`

`Inspecting for n = 10... Satisfiable!`

`Inspecting for n = 11... Satisfiable!`

`Inspecting for n = 12... Satisfiable!`

`Inspecting for n = 13... Unsatisfiable!`

`(True, 13)`

Therefore, \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})=13\). \(\Diamond\)

Finally, the `grid\_explorer.py` module computes Ramsey numbers of a selected type with arguments from two provided graph classes. Although this `Python` module is based on the `bash` scripts in the `src/sat\_solving` folder from \[5\], its logic is significantly optimized to remove redundancy and improve the efficiency of extensive computation. The module can be executed using the following syntax:

`python grid\_explorer.py \<class\_a\> \<class\_b\> \<problem\_type\>`

