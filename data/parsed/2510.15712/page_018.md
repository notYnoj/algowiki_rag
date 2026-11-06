the following 3-clauses to Group 1:

\(f\rightarrow(g_i^T\leftrightarrow g_{j,1}^T)\)<br> \(\neg f\rightarrow(g_i^B\leftrightarrow g_{j,1}^B)\) (The new Group 1)

and similarly for the second input _g_<sub>_j,_2</sub>; we call those clauses _wire clauses_ because they check whether the value in the circuit are consistent along the wires. Also, if the first input of the gate _g<sub>j</sub>_ is an input _x<sub>i</sub>_ to the circuit, we produce the clause

\(f\rightarrow(x_i^T\leftrightarrow g_{j,1}^T)\)<br> \(\neg f\rightarrow(x_i^B\leftrightarrow g_{j,1}^B)\) (The new Group 1)

These are also called wire clauses.

Finally, we replace the lowest-priority group, Group 4, which previously stated that all gates should be correct, including those in the inactive circuit, by wire clauses:

\(g_i^T\leftrightarrow g_{j,1}^T\)<br> \(g_i^B\leftrightarrow g_{j,1}^B\) (The new Group 4)

\(\blacktriangleright\) **Lemma 18.** _Suppose_ \(\alpha\) _is a local maximum, i.e., cannot be improved by a 1-flip or 2-flip. Then all clauses in groups 0, 1, 3, and 4 are satisfied._

**Proof.** A clause in Group 0 can always be satisfied by changing \(\alpha\) in one position, namely the output of the incorrect gate. Now suppose a clause in the new group 1 is violated, for concreteness \((f\rightarrow(g_i^T\leftrightarrow g_{j,1}^T))\), so _f_=1 (TOP is active) and \(\alpha(g_i^T)\neq\alpha(g_{j,1}^T)\) (the wire from gate \(g_i^T\) to gate \(g_j^T\) is inconsistent); we can satisfy this by flipping \(\alpha(g_{j,1}^T)\); this might violate gate \(g_j^T\) and thus a clause in Group 0, which has higher priority. However, we are allowed to flip up to _two_ variables: we flip \(g_{j,1}^T\) and, if need be, also \(g_j^T\). This keeps Group 0 satisfied; it might violate a wire clause for a wire leaving gate _j_; however, this is in Group 1 and has a lower priority due to the topological ordering of the circuit.

A clause in Group 3 requires that the output of the active circuit agree with the input of the inactive one; suppose one is violated, for concreteness \((f\rightarrow(z_j^T\leftrightarrow x_j^B))\), so _f_=1 (TOP is active). We will simply flip \(x_j^B\). The wires going from _x<sub>j</sub>_ to the gates into which it feeds will now be inconsistent; however, the corresponding wire clauses in Group 1 will be satisfied because _f_=1 (BOTTOM is inactive); some wire clauses of Group 4 will become violated, but that’s fine because they have lower priority than the clause in Group 3.

Finally, if a clause in Group 4 is violated, it must be in the inactive circuit (all wire clauses for the active circuit are satisfied due to Group 1); for concreteness, BOTTOM is inactive and \((g_i^B\leftrightarrow g_{j,1}^B)\) is violated. We flip \(g_{j,1}^B\) and, if need be, the output variable \(g_j^B\). Clauses in Group 0 are still satisfied because all gates are still correct; clauses in Group 1 are satisfied because we only fiddled in BOTTOM, which is inactive, so all its Group-1-clauses are satisfied anyway; Group 3 stays satisfied because outputs of the inactive circuit BOTTOM are not required to agree with the inputs of the active circuit TOP; in Group 4 further wire clauses involving _g<sub>j</sub><sup>B</sup>_ might become violated, but they have lower priority than the one we fixed. \(\blacktriangleleft\)

If Group 0, 1, 3, and 4 are satisfied, and the output of the inactive circuit is lexicographically larger than the output of the active circuit, we can still flip _f_ and one bit of \(\vec{o}\) to improve \(\alpha\), simply because the clauses of Group 2 are identical to the ones in the reduction to 4-SAT/2-FLIP. This concludes the proof of Theorem 17

