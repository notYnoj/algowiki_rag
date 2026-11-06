**Algorithm 1** Insertion with Counter Width Tapering

Require: Root of histogram tree, path p, index i, value Ensure: Counters updated along key path function ADDITEM(root, p, i, value) \(node\leftarrow\text{root}\) 3: if node is null then 4: return node 5: end if 6: node.counter=node.counter+value[i] 7: if \(p[i]\le 0\) then 8: if node.left is null then 9: node.left=NODEORTUPLE(i,value[i]) 10: end if 11: child=node.left 12: else 13: if node.right is null then 14: node.right=NODEORTUPLE(i,value[i]) 15: end if 16: child=node.right 17: end if 18: return ADDITEM(child, p, i+1, value) 19: end function

<tbc>of thread scheduling while increasing the risk of cache overflow and cache misses. Smaller batches have low risk of cache overflow hence they enable cache reuse at the cost of increased synchronization frequency when switching between batches. Optimal batch size is tuned empirically for the target device demonstrating latency improvements of over 10% as shown in Figure 7.

## D. Batch Counter Update

The cached histogram from a terminating batch is reused by the next batch to enable faster batch synchronization due to reduced memory transfer. This leads to a reduction in memory usage as the number of batches processed increases, as shown in Figure 8.

### 1) Counter Width Compression and Overflow:

Essential to overall performance is the compression scheme involving counter width tapering in Algorithm 1. The principle exploits the reduction of significant bits on a well-balanced tree as levels increase from root to leaf, determined by the logarithm of the sub-tree size at each node _w<sub>c,l</sub>=O_(\(\lceil log(n_l)\rceil\)), which over large _n_ reduces by one at each level with leaves having approximately less than an average of two significant bits for uniformly distributed keys following Algorithm 1 and Algorithm 2.

The local and global updates have complexity _O(log(n_)) as shown in  I.

## E. Histogram Read and Write Operations

Looking up the value at an index involves depth-first path traversal of the histogram from root to leaf node. Each node has a range of indices representing the leaves in its subtree. The child selected at each node is the one containing the desired index. Traversal stops when a matching leaf node is reached. The _getValue(index_) hash function has _O(min(p,log(n_))) bounded latency as shown in Algorithm 2.

**Algorithm 2** Retrieving Items from Histogram

Require: Root of histogram tree, index, defaultVal Ensure: Value at target index or defaultVal if not found function GETITEM(root, index, defaultVal) \(node\leftarrow\text{root}\) 3: if node is null then 4: return defaultVal 5: end if 6: if node.counter\(\le\) index then 7: child,val=node.left,node.value 8: return GETITEM(child, index, val) 9: else 10: child,val=node.right,node.value 11: index=index-node.counter 12: return GETITEM(child, index, val) 13: end if 14: end function

Determining the index of a value involves the following _O(p_) algorithm shown in Algorithm 3, a significant improvement on the _O(log(n_)) search latency of array data structures.

**Algorithm 3** Retrieving Indices from Histogram

Require: Root of histogram tree, value Ensure: Index of target value 1: function GETINDEX(root, value, defaultIdx) \(node\leftarrow\text{root}\) 3: if node is null then 4: return defaultIdx 5: end if 6: if node.cnt\(\le\) targetIndex then 7: child,idx=node.left,defaultIdx 8: else 9: child,idx=node.right,defaultIdx+node.cnt 10: end if 11: return GETINDEX(child, value, idx) 12: end function

## F. Bandwidth Efficiency

### 1) Computable Pointer Optimization:

The histogram nodes are optimized for bandwidth usage by employing a format that stores nodes without identifier information, achieved<tbc>

