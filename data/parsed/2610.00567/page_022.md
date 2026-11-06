## Verification procedure.

The function `verify_decomposition` checks whether a given sequence of bags is valid for parameters _p_ and _q_. Each bag must be (_p,q_)- spannable: after removing _p_ vertices, the remaining vertices are covered by the endpoints of _q_ edges. This is verified by enumerating all choices of removed vertices and testing edge coverage in the induced subgraph.

The procedure also checks that every comparability condition _i\<j_ is witnessed by some bag, and that the number of graph automorphisms preserving all such conditions is odd. Any violation causes the verification to fail with an explicit error.

Below is the table of all the possible 5 vertex simple connected graphs with their (p,q) tree decomposition, we can use the above code to verify each tree decomposition is a valid tree decomposition, can be spanned by at most p ver

# Comparability condition for (i, j) in conds: found = False for bag in bag_lists: if i in bag and j in bag: found = True break if not found: return False, f"Condition {i}<{j} not witnessed" # Automorphism parity condition count = 0 conds = [(str(i), str(j)) for (i, j) in conds] for sigma in G.automorphism_group(): ok = True for (i, j) in conds: if sigma(i) >= sigma(j): ok = False break if ok: count += 1 if count % 2 == 0: return False, f"Automorphism count even ({count})" return True, "OK" G = Graph([('4','3'), ('3','0'), ('0','4'), ('4','2'), ('4',' 1')]) T = "043-124" conditions = "1<2, 0<3" verify_decomposition(G, T, conditions, p=1, q=1)

