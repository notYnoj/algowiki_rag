The first module, `sat\_problem\_generator.py`, is essentially the `src/sat\_solving/cnf\_generator.py` script from \[5\], with small modifications made to provide a suitable API for the other modules. The other three modules are implemented from scratch and their core logic is based on the `bash` scripts in the `src/sat\_solving` folder from \[5\]. Our full source code is available at \[12\], together with supplementary data, including the computed Ramsey numbers, the Kissat output files and all the 2-edge-colorings yielding the lower bounds.

The `sat\_problem\_generator.py` script accepts two graphs _H_<sub>1</sub> and _H_<sub>2</sub> from the graph classes of interest, together with \(n\in\mathbb{N}\) and a string indicating which type of Ramsey number is being considered. It then generates the corresponding SAT problem encoding the search for a 2-edge-coloring of _K<sub>n</sub>_ containing no forbidden embeddings. The generated SAT instance is printed out in the standard DIMACS CNF format, with the Boolean variables _x_<sub>{_u,v_}</sub> arranged in ascending order first by min{_u,v_}, and then by max{_u,v_}, i.e., as

\(x_{\{0,1\}},x_{\{0,2\}},\dots,x_{\{0,n-1\}},x_{\{1,2\}},x_{\{1,3\}},\dots,x_{\{1,n-1\}},x_{\{2,3\}},x_{\{2,4\}},\dots,x_{\{2,n-1\}},\dots,x_{\{n-2,n-1\}}.\)

The script is executed with six required arguments using the following syntax:

`python sat\_problem\_generator.py \<class\_a\> \<a\> \<class\_b\> \<b\> \<problem\_type\> \<n\>`

Here, `class\_a` and `class\_b` are strings from the set {pmon, palt, cmon, ssc, k, mnest} that specify the graph classes of _H_<sub>1</sub> and _H_<sub>2</sub>, respectively, while `a` and `b` determine |_H_<sub>1</sub>| and |_H_<sub>2</sub>|. Furthermore, `problem\_type` is a string from the set {ord, ref, cyc, dih} indicating which of the four supported types of Ramsey numbers (ordered, reflective, cyclic and dihedral) is being considered, while `n` represents _n_.

**Example 3.1.** Consider the following command:

`python sat\_problem\_generator.py palt 4 pmon 5 ref 12`

This command prints out the DIMACS CNF representation of the SAT instance that encodes the search for a 2-edge-coloring of _K_<sub>12</sub> containing no forbidden embeddings in the context of the reflective Ramsey number \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})\). \(\unknown\)

The `instance\_solver.py` module solves a SAT instance encoding the search for a 2-edge-coloring of _K<sub>n</sub>_ containing no forbidden embeddings. It accepts the same arguments as the `sat\_problem\_generator.py` script, which is immediately invoked to generate an output DIMACS CNF file representing the generated SAT problem. Afterwards, the Kissat SAT solver is used on the output file in order to solve the generated SAT instance. Both of these steps have a time limit, and the execution is aborted in case of a timeout. Additionally, if the Kissat executable is not present, an auxiliary `bash` script from \[5\] is used to obtain it automatically. To avoid trivial cases where the Ramsey number is identically one, both argument graphs are required to have at least two vertices.

The main function of the `instance\_solver.py` module returns an ordered pair `(status, graph)`, as follows.

**(1)** If a timeout is reached, then both `status` and `graph` are set to `None`. In this case, it is not known whether the SAT instance has a solution.

**(2)** If the SAT instance is deemed unsatisfiable, then `status` is set to `False`, while `graph` is set to `None`.

**(3)** If the SAT instance is deemed satisfiable, then `status` is set to `True`, while `graph` is set to the `graph6` \[18, 19\] string representation of the solution found to the SAT instance. Here, the presence of an edge indicates that its color in _K<sub>n</sub>_ is 2, i.e., that the corresponding Boolean variable is `True`.

In addition, the `instance\_solver.py` module saves the Kissat outputs to separate files in the `kissat\_output` folder and, in the case of satisfiable instances, saves the `graph6` string representations of the corresponding solutions to separate files in the `parsed\_graphs` folder.

**Example 3.2.** Consider the following command:

`python instance\_solver.py palt 4 pmon 5 ref 12`

This command gives the following output:

`(True, ’KCrffr{^f}^{’)`

Therefore, the corresponding SAT instance is satisfiable, with the solution given as a `graph6` string. Hence, \(R_\mathrm{ref}(P_4^\mathrm{alt},P_5^\mathrm{mon})\unknown 13\). Now, consider the following command:

