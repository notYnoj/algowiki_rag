<tbc>\(log(\sigma(x))\). Here, we have shown that the simplifications to the partial likelihood made by Kvamme et al. (2019) are equivalent to using the log-sigmoid ranking loss.

The key difference between ranking and partial likelihood losses comes when considering the assumption that it is reasonable to take a constant sample size of 1 (one pair in the risk set) in the partial likelihood. This effectively introduces the assumption that each pair (i, j) is independent of any other pair. However, this assumption seems puzzling given the inherent transitivity of ranking (if _i\>j_ and _j\>k_ then _i\>k_).

## A.2 DIFFERENTIABLE SORTING

Differentiable sorting takes a different approach to the previously discussed partial likelihood loss and will need modification to account for censoring. In order train models based on ordering information, differences between predicted and true orderings are backpropagated through a relaxed sorting algorithm. The idea was first introduced by (Grover et al., 2019), the key motivation being that sorting is a key step in many classical algorithms and machine learning methods (K-nearest neighbours), yet is non-differentiable. This means that direct supervision cannot be done on the outputs of algorithms that rely on sorting (Petersen, 2022).

Sorting algorithms require use of non-differentiable max and min operators. These are analogous to the non-differentiable indicator function that was discussed earlier in the c-index (Equation 7). Differentiable sorting methods similarly rely on approximating these operators with smooth alternatives.

Petersen et al. (2021) propose combining traditional sorting networks and differentiable sorting functions. Sorting networks are a family of sorting algorithms that consist of two basic components: wires and conditional swaps. Wires carry values to be compared at conditional swaps, if one value is bigger than the other then the values carried forward are swapped around. This allows construction of provably guaranteed sorting networks. Conditional swaps are exactly the min and max operators that ensure that with inputs {_a,b_} and outputs \(a^*\le b^*\), _a_<sup>∗</sup>=min(_a,b_) and _b_<sup>∗</sup>=max(_a,b_). Note that as _a_ approaches _b_, the point at which it becomes larger is discontinuous and hence non-differentiable. Just as previously shown in the ranking loss, such operations can be made differentiable using the logistic relaxation

\(min_\sigma(a,b)=a\cdot\sigma(b-a)+b\cdot\sigma(a-b)\text{and}max_\sigma(a,b)=a\cdot\sigma(a-b)+b\cdot\sigma(b-a).\) (9)

Note that if an inverse temperature parameter \(\beta>0\) is introduced such that \(\sigma:x\rightarrow\frac{1}{1+e^{-\beta x}}\), then as \(\beta\rightarrow\infty\) the functions tend to the exact min and max functions. Other relaxation of the step function can also be considered, Petersen et al. (2021) show that the Cauchy distribution preserves monotonicity which is desirable for optimization. Given this, we use the Cauchy distribution as our relaxation for all experiments, where \(\sigma:x\rightarrow\frac{1}{\pi}arctan(\beta x)+\frac{1}{2}\).

(a)
(b)

Figure 2: Example sorting networks of size 8; (a) Odd-Even, (b) Bitonic.

