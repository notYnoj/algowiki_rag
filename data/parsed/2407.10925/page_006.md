<tbc>additionally describes how this independence can be relaxed slightly in order to reuse computations without sacrificing the ability to parallelize.

## 3.2 Indexing A pair of binary strings can be represented as a single 64-bit unsigned integer so long as their combined length does not exceed 64 characters and a consistent indexing scheme is identified. Given two strings _a_ and _b_, we choose to index them by interleaving their bits starting with _a_ and filling the remaining bits with zeros on the left. For instance, a pair of strings _a_=1011 and _b_=0010 is represented as 0...10001110. We say a 64-bit integer is an **_interleaved string pair_**, or simply a **_pair_**, if it represents two binary strings interleaved in this fashion.

This scheme has several desirable properties. Firstly, calculating **v<sub>2</sub>** can be done (in sequential order) by simply iterating through all integers from 0 to \(2^{2\ell}-1\), which we denote \([0,\dots,2^{2\ell})\). Secondly, we need not check whether the first bit of _a_ and _b_ match: we know ahead of time that pairs \([0,\dots,2^{2\ell-2})\) have the same first bit (0) for _a_ and _b_, pairs \([2^{2\ell-2},\dots,2^{2\ell-1}+2^{2\ell-2})\) have different first bits, and pairs \([2^{2\ell-1}+2^{2\ell-2},\dots,2^{2\ell})\) have the same first bit (1). Lastly, this indexing will allow us to determine a method of reading disk memory sequentially once arrays become too large to fit in RAM (Section 3.4).

## 3.3 Array Reductions and Symmetries

In the binary case, Lueker notes how it is not necessary to store arrays **v<sub>i</sub>**, for three consecutive integers _i_, in memory, as the recurrence can be simplified by storing only two arrays (that is, **v<sub>1</sub>**,**v<sub>2</sub>**) and iterating on those instead, with the bound calculation adjusted appropriately [20]. We also adopt this optimization. As Lueker also notes, one can further observe that since complementing both _a_ and _b_ does not impact the length of their longest common subsequence, we get that

\(\mathbf{v}_\mathbf{i}[(\overline{a},\overline{b})]=\mathbf{v}_\mathbf{i}[(a,b)],\)

where <o>_a_</o> represents the binary complement of _a_ [20]. With the indexing scheme defined in Section 3.2, for any two indices _i_ and _j_ such that

\(2^{2\ell-1}>i\ge 0\text{and}j=2^{2\ell}-1-i,\)

we have that

\(2^{2\ell}>j\ge 2^{2\ell-1}\text{and}(a_i,b_i)=(\overline{a_j},\overline{b_j}).\)

Thus, we need only iterate strings pairs represented by the integers \([0,\dots,2^{2\ell-1})\).

## 3.4 Sequential Memory Access As \(\ell\) grows, memory becomes a limiting factor far faster than computation time. For instance, at \(\ell=20\) with 4 bytes for each value stored in the vector, a naive implementation requires

\(2^{2\cdot 20}\cdot 4=4398046511104\text{bytes}\approx 4.4\text{TB}\)

per vector. Even if symmetry is fully exploited, this requires roughly a terabyte of memory per vector. With our resources, it is infeasible to store all of these values in RAM.

Accordingly, vectors must be read from and written to external (disk) memory. However, operating exclusively from external memory is also infeasible: we experienced over a 100x slow down when reading and writing values only from disk. File I/O time dwarfed the time taken to actually perform the computations for the recurrence, largely because memory accesses were non-sequential.

To alleviate this overhead, reading from and writing to disk must be done in large sequential blocks. As such, a recursive approach is taken to identify contiguous blocks of integers from \([0,\dots,2^{2\ell-1})\) whose accessed values also span a contiguous block of integers. This section outlines the approach taken and justifies why it is correct.

The function as implemented contains three primary loops: _L_<sub>0,0</sub>, _L_<sub>0,1</sub>, and _L_<sub>1,0</sub>. Each loop is valid only for a predetermined range of string pairs, but accepts a start parameter and end parameter to allow for subdivision of that range.

### 3.4.1 _L_<sub>0,0</sub>_L_<sub>0,0</sub> iterates over string pairs whose first bits match and calculates the new value in the recurrence according to the last case of _F_<sub>1</sub> (see (2.8)). For a particular _a,b_ string pair, with the interleaved indexing, this is accomplished by the following simple procedure:

Algorithm 3.1.<br> **Input:** _x_, an interleaved _a_, _b_ string pair<br> **Output:** The new recurrence value for index _x_

1: **function** SameFirstBit(_x_)<br> 2: Bitshift _x_ left by 2<br> 3: **return** \(1+\frac{1}{4}(\mathbf{v}_\mathbf{1}[x]+\mathbf{v}_\mathbf{1}[x+1]+\mathbf{v}_\mathbf{1}[x+2]+\mathbf{v}_\mathbf{1}[x+3])\)

Since _L_<sub>0,0</sub> iterates only within \([0,\dots,2^{2\ell-2})\), the first bit of _a_ and _b_ will always be 0. Thus, this procedure always accesses the values at 4_x_, 4_x_+1, 4_x_+2, and 4_x_+3. For \(x\ge 2^{2\ell-3}\), it will access pairs \(\ge 2^{2\ell-1}\), so we use (3.10) to transform the pairs back to their symmetric position within the vector. As a result, if

