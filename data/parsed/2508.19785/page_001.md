# An Optimal Sorting Algorithm for Persistent Random Comparison Faults

BARBARA GEISSMANN, FHNW University of Applied Sciences and Arts Northwestern Switzerland, Switzerland

STEFANO LEUCCI<sup>∗</sup>, University of L’Aquila, Italy

CHIH-HUNG LIU<sup>∗</sup>, National Taiwan University, Taiwan

PAOLO PENNA, IOG, Switzerland

We consider the problem of sorting _n_ elements subject to persistent random comparison errors. In this problem, each comparison between two elements can be wrong with some fixed (small) probability _p_, and comparing the same pair of elements multiple times always yields the same result. Sorting perfectly in this model is impossible, and the objective is to minimize the dislocation of each element in the output sequence, that is, the difference between its position in the sequence and its true rank.

In this paper, we present the first _O(n_log_n_)-time sorting algorithm that guarantees both _O_(log_n_) maximum dislocation and _O(n_) total dislocation with high probability when \(p<\frac{1}{4}\). This settles the time complexity sorting with persistent comparison errors in the given range of _p_ and shows that comparison errors do not increase its computational difficulty. Indeed, \(\Omega(nlogn)\) time is necessary to archive a maximum dislocation of _O_(log_n_) (even without comparison errors). Moreover, we further prove that no algorithm can guarantee a maximum dislocation of _o_(log_n_) with high probability, nor a total dislocation of _o(n_) in expectation.

To develop our sorting algorithm, we solve two related sub-problems in the persistent error comparisons model, which might be of independent interest. More precisely, we that _O_(log_n_) time suffices to find a position in which to insert a new element _x_ in an almost-sorted sequence _S_ of _n_ elements having dislocation at most \(d=\Omega(logn)\), so that the dislocation of _x_ in the resulting sequence is _O(d_) with high probability (which can be equivalently thought as the problem of estimating the rank of _x_ in _S_). We also show that the maximum (resp. total) dislocation of an approximately sorted sequence _S_ of _n_ elements can be lowered to _O_(log_n_) (reps. _O(n_)) in _O(nd_) time, with high probability, where _d_ is an upper bound on the maximum dislocation of _S_.

<sup>∗</sup>Corresponding author. Authors’ Contact Information: Barbara Geissmann, barbara.geissmann@fhnw.ch, FHNW University of Applied Sciences and Arts Northwestern Switzerland, Windisch, Switzerland; Stefano Leucci, stefano.leucci@univaq.it, University of L’Aquila, L’Aquila, Italy; Chih-Hung Liu, chliu@ntu.edu.tw, National Taiwan University, Taipei, Taiwan; Paolo Penna, paolo.penna@ iohk.io, IOG, Zurich, Switzerland.

