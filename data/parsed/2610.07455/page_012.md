The two lower bounds therefore use the same structural principle. We first reduce exactly to the core and then recover the variable pinnings. For satisfiability, it is enough to restrict the satisfying assignments up to one common automorphism. For exact optimization, the restriction must additionally be strong enough that violating it is never profitable. The sparsification result uses the same core reduction to obtain the minimization characterization.

### 2.4 Relation to prior work

We first explain how our results extend the earlier work of Sharma and Velusamy [SV26a]. Here, a constraint language is a fixed finite set of relations over the same domain. They proved the satisfiability characterization in two settings. First, they considered every finite domain but allowed literals: when the domain is Z_<sub>q</sub>_, each occurrence of a variable _x_ in a constraint may be replaced by \(x+\lambda\) modulo _q_, for an arbitrary \(\lambda\in\mathbb{Z}_q\). In the Boolean setting, this is exactly the choice between _x_ and \(\neg x\). These shifts give the lower bound construction more freedom. For a fixed relation, a lower bound that uses nonzero shifts need not apply when all shifts are zero.

Their second result concerns positive Boolean CSPs, meaning Boolean CSPs without literals. They assume that the constraint language is not "constant-satisfiable". This means that there is no value \(c\in\{0,1\}\) for which assigning every variable the value _c_ satisfies every relation in the language. This is the general interesting case for positive Boolean CSPs, since otherwise every instance has the same constant satisfying assignment.

**Lemma 2.10** (Informal Lemmas A.2 and A.7)**.** _Reducing a language with literals to its core does not change its non-redundancy. Moreover, a Boolean constraint language is a core if and only if it is not constant-satisfiable._

Our core viewpoint uses these two facts to explain both earlier results. For the literal model, treat every shifted use of a relation as a separate relation. The resulting language is shift-closed, so the first part of the lemma shows that passing to its core does not change its non-redundancy. Our general core characterization therefore gives the earlier characterization for CSPs with literals. For the positive Boolean result, the only non-bijective maps on the Boolean domain are the two constant maps, which send both domain values to 0 or both to 1. The second part of the lemma therefore shows that the assumption of not being constant-satisfiable is exactly the assumption that the language is a core.

Our work then goes beyond both results by giving a characterization in the most general finite-domain setting. The precise statements and their proofs are given in Section A.

We also compare our exact-optimization result with the work of Kol, Paramonov, Saxena, and Yu [KPSY23]. Their general characterization is restricted to Boolean CSPs with literals and constants. Our result applies to arbitrary relations, requiring neither literals nor constants, giving a characterization in the more general CSP setting. However, their lower bound does extend to a constant number of passes. We view an extension of our result to the multi-pass setting as an exciting future direction.

## 3 Preliminaries

In this section, we state the definitions used in the rest of the paper.

