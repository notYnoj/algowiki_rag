<tbc>containing \(w'\), there also exists a MWIS without \(w'\). Therefore, we can find the MWISs of the graph without \(w'\) and check whether any of the neighbours is included to decide whether there is also a MWIS containing \(w'\). So when \(w'\) has weight less than or equal to 0, this reduces the graph size by a further vertex and potentially multiple edges. Crucially, in doing this reduction, we may also expose further vertices, which allows us to continue to reduce the graph.

This concept can be extended further: consider a vertex of degree 2, _v_, connected to a pair of vertices that are also connected to each other, _w_<sub>1</sub>_,w_<sub>2</sub>. Then, we can apply similar principle to the degree 1 case. The vertex _v_ can only be in a MWIS if neither _w_<sub>1</sub> nor _w_<sub>2</sub> is in it, and crucially as _w_<sub>1</sub>_,w_<sub>2</sub> conflicts, only one of them can be in a putative MWIS at a time. As a result, in this case we case remove _v_ from the graph and dropping the weight of both \(w'_1,w'_2\) by \(\omega_G(v)\), knowing that as only at most one of the vertices can be in the MWIS and so we would never want to remove _v_ twice.

These two methods form part of a larger series of reductions, which are sometimes collectively known as "kernelisation routines" \[10\]. We limit our attention here to the two described above due to the complexity of verifying the reduction requirements for more complex reductions, and their limited expected utility. As mentioned above, each of these reductions will expose new vertices that may newly satisfy the conditions for reduction, whether it be Cherry’s original reduction or the new ones we have developed. Therefore, instead of having these reductions as a stand-alone subroutine embedded into the algorithm, we embed it directly<tbc>

1.
1
1
2
2
V
1
0
1
w
w'
+v if w' not in MWIS
1
2
2.
3.
1
1
1
2
2
+v if w' not in MWIS
+v if w' not in MWIS

Figure 6: An example of the effects of the reduction process on the MWIS algorithm on a simple complement graph. The target vertex is _v_, which is connected to _w_. In step 1, we remove _v_ and decrease the weight of \(w'\). In step 2, as \(w'\) has weight 0, we remove it to deal with in postprocessing. In this case, as it is connected to both the remaining vertices, it cannot be in any MWIS. In step 3, we find the MWIS in the reduced graph, which is simply the vertex of weight 2. This is then combined with _v_ which we had removed in the beginning to give the sole MWIS for this complement graph.

