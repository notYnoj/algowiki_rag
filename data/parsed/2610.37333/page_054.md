## Appendix A. The three `diff-soup` VSVO solvers

In this appendix, we compare the three native VSVO solvers of `diff-soup` on each benchmark problem of Section 4. Figure A.15 shows that the three solvers generally exhibit similar performance at matched error, with no significant leader. For this reason, we adopt `JIDA` for the main text results, as it is generally the most robust stiff implicit integration algorithm and handles the most general problem form.

