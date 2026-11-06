## 7 Appendix

### 7.1 Python code for Thm. 4 (GBST algorithm of [11])

#!/usr/bin/env python3.4<br> import functools<br> memoize = functools.lru\_cache(maxsize=None)<br> def huang1984(weights):<br> "Returns cost as computed by Huang and Wong's GBST algorithm (1984)."<br> n = len(weights)<br> beta = {i+1 : weights[key] for i, key in enumerate(sorted(weights.keys()))}<br> def is\_legal(i, j, d): return 0 \<= i \<= j \<= n and 0 \<= d \<= j -i<br> @memoize<br> def p\_w\_t(i, j, d):<br> "Returns triple: (cost p[i,j,d], weight w[i,j,d], deleted keys for t[i,j,d])."<br> interval = set(range(i+1, j+1))<br> if d == j-i: # base case<br> return (0, 0, interval)<br> def candidates(): # Lemma 4 recurrence from Huang et al<br> for k in interval: # k = index of split key<br> for m in range(d+2): # m = num. deletions from left subtree<br> if is\_legal(i, k-1, m) and is\_legal(k-1, j, d-m+1):<br> cost\_l, weight\_l, deleted\_l = p\_w\_t(i, k-1, m)<br> cost\_r, weight\_r, deleted\_r = p\_w\_t(k-1, j, d-m+1)<br> deleted = deleted\_l .union( deleted\_r )<br> x = min(deleted, key = lambda h : beta[h])<br> weight = beta[x] + weight\_l + weight\_r<br> cost = weight + cost\_l + cost\_r<br> yield cost, weight, deleted -set([x])<br> return min(candidates())<br> cost, weight, keys = p\_w\_t(0, n, 0)<br> return cost<br> weights = dict(b4=20,<br> a3=20, v3=20,<br> a2=20, p2=20, t2=20, x2=20,<br> a1=20, d1=22, n1=20, q1=20, s1=20, u1=20, w1=20, y1=20,<br> b0=10, c0= 5, d0=10, e0=10, n0=10, p0=10, q0=10, r0=10,<br> s0=10, t0=10, u0=10, v0=10, w0=10, x0=10, y0=10, z0=10)<br> assert huang1984(weights) == 1763 # Both assertions pass. The first is used in our Thm. 4.<br> weights['d1'] += 0.99 # Increasing a weight cannot decrease the optimal cost, but<br> assert huang1984(weights) \< 1763 # in this case decreases the cost computed by the algorithm.

The extended abstract [2] is essentially the body of this paper minus the remainder of this appendix. The remainder of this appendix contains all proofs omitted from the extended abstract.

### 7.2 Proof of Lemmas 2-4 (in the proof of Spuler’s conjecture)

We prove some slightly stronger lemmas that imply Lemmas 2-4. Let _T_ be any irreducible, optimal 2wcst as in the proof of Lemma 1.

