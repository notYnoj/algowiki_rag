A code snippet appendix A.1 is written in C++ describing the structure of compressed l-mer and the method of calculating hamming distance.

### 3.3.2 Motif Finding

After compressing the input sequences we need to find the motifs in them. For these we’ve modified the TraverStringRef algorithm by using the compressed l-mers. Then we have followed the steps of Algorithm TraverStringRef to find out the motifs.

### 3.3.3 Parallel Implementation of qpMS-Sigma

The Algorithm qpMS-Sigma can easily implement in parallel by traversing several search trees in parallel. Similar to the idea of parallelism mentioned in Algorithm TraverStringRef [24] we can divide the problem into (_m-l_+1) subproblem where each subproblem explores different search trees.

## 3.4 Space and Runtime Complexity

Here the space complexity of our algorithm is \(O(nml(log[\Sigma])/w)\). Here _w_ is the size of the integers that contain the compressed input sequences as well as the _l_-mers. For DNA sequences \(log|\Sigma|=2\). So the space complexity becomes _O(nml/w_).

The worst case time complexity is similar to TraverStringRef \(O((n-q+1)^2nm^2(m+logn)n_B(l,d))\). However, finding the hamming distance between two _l_-mers take about constant time for DNA sequence. Normally bitwise operations are a little faster than the other arithmetic operations. So, practically our algorithm runs a little faster than the former.

## 3.5 Experimental Results

We have compared the runtime of Algorithm qpMS-Sigma in the challenging states with the other well known algorithms. The proposed algorithm is implemented in C++ (using GNU C++ compiler). We have run the experiment on Ubuntu 14.04 (64 bit) operating system. The machine configuration is Intel®CoreTMi3-4005U CPU @ 1.70GHz × 4, 4GB RAM.

The test dataset was generated in computational experiment of Algorithm TraverStringRef [24].

