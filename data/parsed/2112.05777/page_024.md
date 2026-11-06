### Experimental Setup II.

While in the previous experiment we have focused on allowing _M_<sub>2</sub> to be blocked by a "fixed" number of pairs (independent of |bp(_M_<sub>1</sub>,P<sub>2</sub>)|), we now want to explore the spectrum between allowing that _M_<sub>2</sub> is not blocked by any pairs and that _M_<sub>2</sub> is blocked by all pairs that block _M_<sub>1</sub> in P<sub>2</sub>, which allows to set _M_<sub>2</sub>:=_M_<sub>1</sub>. For this, we conducted the following experiment: For each of our three types of changes, we computed 200 instances with 50 men and 50 women having random preferences with a 0.1 fraction of all changes applied uniformly at random between P<sub>1</sub> and P<sub>2</sub>. Subsequently, for each \(i\in\{0,0.02,0.04,\dots,0.98,1\}\), we computed a matching _M_<sub>2</sub> with minimum symmetric difference with _M_<sub>1</sub> that is blocked by at most \(i\cdot|\mathrm{bp}(M_1,\mathcal{P}_2)|\) pairs in P<sub>2</sub>. Note that the results can be found in Figure 9. We also repeated this experiment with different fractions of changes between P<sub>1</sub> and P<sub>2</sub> producing very similar results.

### Evaluation II.

Examining Figure 9 confirms our observation from Figure 8 that the first _x_ blocking pairs that _M_<sub>2</sub> is allowed to admit have a higher impact than the second _x_ blocking pairs, as the symmetric difference between _M_<sub>1</sub> and _M_<sub>2</sub> decreases particularly quickly for smaller fractions (up to around 0.3). The reason why for Delete allowing for |bp(_M_<sub>1</sub>,P<sub>2</sub>)| many blocking pairs does not lead to a symmetric difference of zero is because the deleted agents are not part of any pair in _M_<sub>2</sub> and thus their edges from _M_<sub>1</sub> are always part of the symmetric difference.

## 7 Conclusion

This paper extends the study of adapting stable matchings in two-sided matching markets to change in various directions: We systematically analyzed how different types of changes relate to each other in theory and in practice, initiated the study of incremental versions of two further two-sided stable matching problems and investigated experimentally practical aspects of adapting stable matchings.

For future work, on the experimental side, it would be interesting to perform experiments with methods that are used in practice to deal with settings discussed in the paper on real-world data. Moreover, extending our experiments to STABLE ROOMMATES is a natural next step. Finally, it might also be interesting to investigate how the complexity of the considered problems changes if the first matching is not given to us, i.e., we are given two preference profiles and the task is to find a stable matching for each profile which are close to each other. Notably, Chen et al. \[2018, Theorem 4.6\] already proved that finding a matching that is stable in two different given preference profiles is NP-hard.

## Acknowledgments

NB was supported by the DFG project MaMu (NI 369/19) and by the DFG project ComSoc-MPMS (NI 369/22). KH was supported by the DFG Research Training Group 2434 "Facets of Complexity" and by the DFG project FPTinP (NI 369/16).

## References

