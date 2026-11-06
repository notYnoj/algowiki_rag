## 2.1 Termination Verification by CEGIS

Our method follows the usual workflow of termination verification by CEGIS. It works as follows: given a program, we encode the termination problem into a constraint solving problem, and then use the CEGIS architecture to solve the constraint solving problem.

### Encoding the termination problem.

The first step of our method is to encode the termination problem as the set C of constraints.

**Example 1.** As a running example, consider the following C program.

`while(x != 0) { if(x < 0) { x++; } else { x--; }`

The termination problem is encoded as the following constraints.

\(x<0\wedge x'=x+1\Longrightarrow R(x,x')\) (2)

\(\neg(x<0)\wedge x'=x-1\Longrightarrow R(x,x').\) (3)

Here, _R_ is a predicate variable representing a well-founded relation, and term variables \(x,x'\) are universally quantified implicitly.

The set C of constraints claims that the transition relation for the given program is subsumed by a well-founded relation. So, verifying termination is now rephrased as the existence of a solution for C. Note that we omitted constraints for invariants for simplicity in this example (see Sect. 3 for the full encoding).

### Constraint solving by CEGIS.

The next step is to solve C by CEGIS.

In the CEGIS architecture, a synthesizer and a validator iteratively exchange a set E of examples and a candidate solution \(R(x,x')\) for C. At the moment, we present a rough sketch of CEGIS, leaving the details of our implementation to Sect. 2.2.

**Example 2.** Fig. 3 shows how the CEGIS architecture solves the set C of constraints shown in (2) and (3). Fig. 3 consists of three pairs of interactions (i)-(vi) between a synthesizer and a validator.

(i) The synthesizer takes \(\mathcal{E}=\emptyset\) as a set of examples and returns a candidate solution \(R(x,x')=\perp\) synthesized from E. In general, candidate solutions are required to satisfy all constraints in E, but the requirement is vacuously true in this case.

synthesizer validator (i) E = = = (ii) (iii) = x x' ^ x 2 0 (iv) = (R(1,0), R(-2, -1)) (v) (vi)

Fig.3: An example of CEGIS iterations

