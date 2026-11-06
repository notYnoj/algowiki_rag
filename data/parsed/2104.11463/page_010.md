### Encoding non-termination.

We can also encode a problem of non-termination verification to pwCSP via recurrent sets \[20\]. For simplicity, we explain the encoding for the case of only one program variable _x_. We consider a recurrent set _R_ satisfying the following conditions.

\(\iota(x)\Longrightarrow R(x)\) (5)

\(R(x)\Longrightarrow\exists x'.\tau(x,x')\wedge R(x')\) (6)

To remove \(\exists\) from (6), we use the following constraint that is equivalent to (6).

\(R(x)\Longrightarrow E(x,0)\) (7)

\(E(x,x')\Longrightarrow\big(\tau(x,x')\wedge R(x')\big)\)<br>
\(\vee\big(S(x',x'-1)\wedge E(x,x'-1)\big)\vee\big(S(x',x'+1)\wedge E(x,x'+1)\big)\) (8)

The intuition is as follows. Given _x_ in the recurrent set _R_, the relation \(E(x,x')\) searches for the value of \(\exists x'\) in (6). The search starts from \(x'=0\) in (7), and \(x'\) is nondeterministically incremented or decremented in (8). The well-founded relation _S_ asserts that the search finishes within finite steps. As a result, we obtain a pwCSP for non-termination defined by (C,R) where R={_S_} and C is given by (5), (7), and (the disjunctive normal form of) (8).

**Example 10.** Consider the following C program.

`while(x \> 0) { x = -2 \* x + 9; }`

The non-termination problem is encoded as the pwCSP (C,R) where R={_S_}, and C consists of

\(x>0\Longrightarrow R(x)R(x)\Longrightarrow E(x,0)\)<br>
\(E(x,x')\Longrightarrow x'=-2x+9\wedge R(x')\)<br>
\(\vee(S(x',x'-1)\wedge E(x,x'-1))\vee(S(x',x'+1)\wedge E(x,x'+1)).\)

The program is non-terminating when _x_=3. This is witnessed by a solution \(\sigma\) for (C,R), which is given by \(\sigma(R)(x):=x=3\), \(\sigma(E)(x,x'):=x=3\wedge 0\le x'\wedge x'\le 3\), and \(\sigma(S)(x',x''):=x''=x'+1\wedge x''\le 3\).

## 4 CounterExample-Guided Inductive Synthesis (CEGIS)

We explain how CounterExample-Guided Inductive Synthesis \[28\] (CEGIS for short) works for a given pwCSP (C,R) following \[30\]. Then, we add the extraction of positive/negative examples to the CEGIS architecture, which enables our decision tree-based synthesizer to use a simplified form of examples.

CEGIS proceeds through the iterative interaction between a synthesizer and a validator (Fig. 1), in which they exchange examples and candidate solutions.

**Definition 11.** A formula \(\phi\) is an _example_ of C if \(ftv(\phi)=\emptyset\) and \(\wedge\mathcal{C}\vDash\phi\) hold. Given a set E of examples of C, a predicate substitution \(\sigma\) is a _candidate solution_ for (C,R) that is consistent with E if \(\sigma\) is a solution for (E,R).

