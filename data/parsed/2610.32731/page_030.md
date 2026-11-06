If _F_ has only one root, we know that this root is the minimum. Thus, we can remove it, yielding an equivalent instance \((F',k-1)\). Repeat this until the forest has more than one root, or _k_=0. If \(k\ge 1\), run WSHSparseForestSelect2. The number of comparisons will be still bounded by O(OPTlogOPT), and the running time overhead due to preprocessing is only O(_k_). We have thus shown theorem 3.

### Acknowledgments.

The author did not use generative AI tools in any capacity for this paper. Many thanks to the anonymous reviewers for their suggestions.

## References

