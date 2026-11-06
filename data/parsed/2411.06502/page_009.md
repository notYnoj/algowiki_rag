For the right subrectangle, we can directly recurse since its inputs are a subset of those for the full rectangle.

For the left subrectangle, we must compute its input before recursing on it. First, let us consider \(\text{sim}((x,x'),(y,y'))\) for all \((x,x')\), \((y,y')\in[a..r]\times b'\). These values corresponds to the case where both paths cross the upper border [_a..r_]\(\times b'\) in Figure 2. Note that these values are part of the input for the entire rectangle.

Similarly, when both paths cross the right border of the left subrectangle, i.e. \(r\times[a'..b']\), no work needs to be done, as we can obtain the inputs from the right subrectangle’s output.

Next, suppose the path in \(\text{sim}(L,L')\) crosses the upper border at \((x,b')\) for some \(x\in[a..r]\), and the path in \(\text{sim}(R,R')\) crosses the right border at \((r,y')\) for some \(y'\in[a'..b']\). Then, we can decompose the path in \(\text{sim}(R,R')\) into two parts (see Figure 2), as

\(\text{sim}((x,b'),(r,y'))=max_{(w,w^\prime)\in[[r..b]\times b^\prime)\cup(b\times[a^\prime..b^\prime])}\big\{\text{sim}(R[r..w),R'[y'..w'))+\text{sim}((x,b'),(w,w'))\big\}.\) (1)

In this maximization, the latter summands are part of the input for the full rectangle, and the former summands are border-to-border paths in an alignment graph which can be computed in time O(_m_<sup>2</sup>), where \(m=max(b-a,b'-a')\). Equation (1) can be computed concurrently for all such _x_ and \(y'\) via a max-plus product<sup>4</sup> in time O(T<sub>MUL</sub>(_m_)).

<sup>4</sup> In max-plus products, the minimum operator is replaced by a maximum. Note that min and max products are equivalent, as one can be transformed into the other by appropriately reversing the signs of the matrices. For the remainder of this paper, we treat them as equivalent.

(n + 1, n' + 1)
(r,b')
(b,b')
(x,b')
(w,w')
(r, y')
(a,a')
(r,a')
(1,1)

**Figure 2** The figure illustrates an instance of the recursive scheme used to solve TED on caterpillars. The inputs can be visualized as fixing the starting points of the two paths on the upper right border (in orange) of the rectangle, and we are determining the maximum value achievable from there onwards. We are required to compute the same values for the lower left border (in purple). The divide-et-impera scheme divides the rectangle vertically into two smaller ones, parameterized by the corners \((a,a'),(r,b')\) and \((r,a'),(b,b')\). The figure also demonstrates how to compute the inputs for the scheme on the left subrectangle for one specific case: one path leaves the upper border, and the other exits from the right border.

