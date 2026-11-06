<tbc>_stage of the algorithm. If r<sub>v</sub>\<b<sub>v</sub> the node is said to have_ polarity _"red smaller than blue", otherwise "blue smaller than red". If the algorithm finds an inversion x,y between b<sub>v</sub> and r<sub>v</sub>, then v has three children with the respective pivots_ (_b<sub>v</sub>,y),_ (_y,x),_ (_x,r<sub>v</sub>_) _or_ (_r<sub>v</sub>,y),_ (_y,x),_ (_x,b<sub>v</sub>). The polarity of the middle child is the opposite of the polarity of v, whereas the two outer children have the same polarity as v. See Figure 2. If the algorithm finishes the subproblem by completing verification and concludes that b<sub>v</sub> and r<sub>v</sub> are representing neighboring stripes of the output, then v is a leaf of the tree._

To analyse the refinement tree, it is convenient to work with a totally ordered list _L<sub>I</sub>_=(_x_<sub>0</sub>_,x_<sub>1</sub>_,...x_<sub>_n+m_-1</sub>) of all red and blue elements. In the case of bichromatic sorting, this total order is given by the sorted ordering.

**Definition 8.** _\[List subinstance, Stripe subinstance and subproblem\] Let_ \(r\in R\) _and_ \(b\in B\) _be two elements and let i,j be their indices in L<sub>I</sub>, i.e., x<sub>i</sub>=r and x<sub>j</sub>=b. Then, the instance I<sub>rb</sub> given by the list_ (_x<sub>i</sub>,...,x<sub>j</sub>_) _or_ (_x<sub>j</sub>,...,x<sub>i</sub>_) _is called the_ list subinstance _of L_<sub>I</sub> _defined by r and b. Let_ I _be an instance of bichromatic sorting and let x<sub>o</sub>,x<sub>p</sub>,x<sub>q</sub>,x<sub>r</sub> be four consecutive pivots on the backbone of InversionSort at some point in time. Then the_ stripe subinstance _of x<sub>p</sub> and x<sub>q</sub> consists of the stripes of x<sub>p</sub> and x<sub>q</sub> and all elements between x<sub>p</sub> and x<sub>q</sub>. The_ subproblem _consists of the two buckets of x<sub>p</sub> and x<sub>q</sub>, i.e., the elements of the color of x<sub>p</sub> between x<sub>o</sub> and x<sub>q</sub>, and the elements of the other color (that of x<sub>q</sub>) between x<sub>p</sub> and x<sub>r</sub>._

Observe that at any snapshot of the algorithm, any existing backbone corresponds to the in- order leaf traversal of some subtree of the refinement tree that includes the root.<sup>2</sup> This traversal consists of internal nodes and leafs of the complete refinement tree. See Figure 3.

## 4.1 Inversion Finding

We start with a central insight about the randomness of inversion finding that has important consequences for the depth of the refinement tree of InversionSort.

**Lemma 9** (Randomness in Inversion Finding)**.** _At any stage of the InversionSort, consider a successful inversion finding procedure, which finds an inversion y\<x between representatives u<sub>i</sub>\<y\<x\<u_<sub>_i_+1</sub>_. Say, w.l.o.g., that u<sub>i</sub> is red and u_<sub>_i_+1</sub> _is blue, and hence x is red and y is blue._

<sup>2</sup>This subtree is obtained by removing from the full refinement tree subtrees of those internal nodes that have not yet found inversions.

blue red
V
bv
v
V
blue red
red red
blue red
bo = bv
o
p
p
q
rq = rv
ro = rp
bp = bq
0
p
q

Figure 2: A parent node _v_ and its three children _o,p,q_ in the refinement tree. The pivots for the parent are (_b<sub>v</sub>,r<sub>v</sub>_), and since the parent is of type blue _\<_ red, the inversion found is of type red _\<_ blue. The left and right children have the same polarity as the parent, whereas the middle child gets opposite polarity.

