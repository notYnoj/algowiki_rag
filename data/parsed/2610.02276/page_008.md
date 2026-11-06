<tbc>A targeted check of the structural proof was also run on all 434 nonisomorphic trees of orders three through eleven. In the one-pendant-leaf branch, 1103 paired maximal-independent-set comparisons had the strict fibre-probability direction predicted by theorem 4.4. These finite checks are corroborative only; section 4 is the proof for arbitrary finite trees.

## 8 Lean formalisation and Palomar registration

The frozen A+B theorem package has been formalised in Lean. The Stage-5 verification baseline used Lean 4.34.1 and Mathlib commit

`d13f23b723b8a846827a245b89c10fc7d3f11612`.

The final Theorem A declarations are

`GreedyUniformity.tree\_greedyLawEqUniform\_iff\_isK1OrK2`

`GreedyUniformity.tree\_bias\_eq\_zero\_iff\_isK1OrK2`.

The mixed-spider package contains the maximal-independent-set count, the centre and non- centre probability formulas, the tuned exact bias identity and positivity theorem, and the two asymptotic Big-O statements stated above.

For Palomar packaging, Stage 6 migrated the project to Lean 4.35.0-rc3 and Mathlib commit

`c55e6e786f49471c72fbddbec5415808896aec1e`.

This was a compatibility migration and did not strengthen or alter the frozen theorem statements. The package was registered as

`PALOMAR-2026-10-01-000003`, version 1,

with trust level _high_. The immutable registered source commit is

`1733c29a5165148d71a2f0bd1ed2dcd7c35309ce`.

The public registry entry is

`https://palomar-registry.org/entry.html?id=PALOMAR-2026-10-01-000003&version=1`.

The project source is available at

`https://github.com/jfairfaxball-348/Greedy-Uniformity-on-Trees`.

All nine intended final theorem declarations--two for Theorem A and seven mixed-spider checkpoints--are included in the registered comparator surface. The permitted axiom reports for these declarations are exactly

\[`propext`, `Classical.choice`, `Quot.sound`\],

and there are no project-specific mathematical axioms in the final theorem package.

These records should be interpreted narrowly. Lean checks the formal derivations against the specified foundations and dependencies, and Palomar records/verifies the packaged formal statements under its tooling. Neither constitutes peer review, a literature-priority determination, or a certificate that no stronger theorem is known.

\begin{tabular}{cccc}
_k_ & _l_ & |_V_| & _b(T_) \\
2 & 2 & 7 & 1/30 \\
3 & 5 & 12 & 7/576 \\
4 & 12 & 21 & 41/13260 \\
6 & 58 & 71 & 18353/78602160 \\
10 & 1014 & 1035 & 22598757953479/19219192053894201600 \\
\end{tabular}

1: Selected exact biases for _T_<sub>_k,_2_k-k_</sub>.

