Now suppose that exactly one of _j<sub>x</sub>=j<sub>b</sub>_ and _j<sub>b</sub>=j<sub>y</sub>_ holds. By symmetry, suppose that it is the former, and thus _j<sub>x</sub>=j<sub>b</sub>\<j<sub>y</sub>_. Then we trivially have \(b\in S_{j_x}\). And on the other hand, consider any ancestor \(b'\) of _x_ which is higher than _b_ and satisfies \(x<b'\). Then \(b'\) would have to satisfy \(y<b'\) as well, and in particular \(j_y\le j_{b^\prime}\), so it could not lie in _S<sub>j<sub>x</sub></sub>_. Therefore _b_ is the highest ancestor of _x_ which lies in _S<sub>j<sub>x</sub></sub>_ and satisfies _x\<b_. So this is type 2.

From now on we can assume that _j<sub>x</sub>\<j<sub>b</sub>\<j<sub>y</sub>_, which means in particular that _j<sub>a</sub>\<j<sub>b</sub>\<j<sub>c</sub>_, that _S<sub>j<sub>b</sub></sub>_ is contained entirely in _b_’s subtree in T , and therefore _b_ is the highest member of _S<sub>j<sub>b</sub></sub>_ in T . Now, the lowest common ancestor of _S<sub>j<sub>a</sub></sub>_ (resp. _S<sub>j<sub>c</sub></sub>_) must be an ancestor of _a_ (resp. _c_) and therefore an ancestor of _b_, so by the properties of \(\widetilde{\mathcal{T}}\), _j<sub>a</sub>_ (resp. _j<sub>c</sub>_) is an ancestor of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\). Furthermore, any ancestor of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\) must be of the form _j<sub>z</sub>_ for some ancestor _z_ of _b_ in T , so since _a_ (resp. _c_) is the closest (in key value) ancestors of _b_ on its left (resp. right) side in T , _j<sub>a</sub>_ (resp. _j<sub>c</sub>_) must be the closest ancestor of _j<sub>b</sub>_ on its left (resp. right) side in \(\widetilde{\mathcal{T}}\).

Suppose that at least one of _j<sub>a</sub>=j<sub>x</sub>_ or _j<sub>y</sub>=j<sub>c</sub>_ holds. By symmetry suppose that it is the former. Then just by virtue of the fact that _j<sub>x</sub>=j<sub>a</sub>_, _j<sub>x</sub>_ is the closest ancestor of _j<sub>b</sub>_ on its left side in \(\widetilde{\mathcal{T}}\). So this is type 3.

Otherwise, we have _j<sub>a</sub>\<j<sub>x</sub>\<j<sub>b</sub>\<j<sub>y</sub>\<j<sub>c</sub>_. This implies that _S<sub>j<sub>x</sub></sub>_ lies entirely within _b_’s left subtree, and _S<sub>j<sub>y</sub></sub>_ lies entirely within _b_’s right subtree, thus _j<sub>x</sub>_ and _j<sub>y</sub>_ are descendants of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\). So this is type 4. \(\blacktriangleleft\)

## 3.1.4 Using the classification to prove Theorem 19

**Proof of Theorem 19.** Let T be any binary search tree over \(S_1\cup\cdots\cup S_l\), and let T_<sub>j</sub>_ and \(\widetilde{\mathcal{T}}\) be the corresponding trees defined in Definition 21 and Definition 22. We will show that

\(\mathsf{Alt}_\mathcal{T}(X)\le\mathsf{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)+\sum_j\mathsf{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)+O(m).\)

Let us use Claim 23: we charge type 1 alternations to \(\mathsf{Alt}_{\mathcal{T}_j}\big(X^{(j)}\big)\), type 4 alternations to \(\mathsf{Alt}_\widetilde{\mathcal{T}}\big(\widetilde{X}\big)\), and we show below that there are only _O(m_) alternations of types 2 and 3.

For type 2, this is because we can charge it uniquely to the access made to _x_ or _y_ (formally, we charge it to _t<sub>x</sub>_ or _t<sub>y</sub>_).

Let us take the first subcase: _b_ is the highest ancestor of _x_ such that \(b\in S_{j_x}\) and _x\<b_. _x_ can only have one highest ancestor with a given property, so it has only one highest "ancestor _b_ such that \(b\in S_{j_x}\) and _x\<b_". So this can apply to at most one of the alternations that occurred when accessing _x_, and thus we can charge it to _t<sub>x</sub>_.

Let us take the second subcase: _b_ is the highest ancestor of _y_ such that \(b\in S_{j_y}\) and _b\<y_. Again, _y_ can only have one highest "ancestor _b_ such that \(b\in S_{j_y}\) and _b\<y_". The access to _x_ is the first time that the preferred child switches back from _b_’s left child to _b_’s right child after accessing _y_. So this event is unique from the perspective of this particular access to _y_, and thus we can charge it to _t<sub>y</sub>_.

Finally, we will bound the total number of occurrences of type 3 alternations by charging them to _j<sub>b</sub>_, not uniquely but in a \(\frac{l}{m}\)-to-1 manner. Let us take the case where _j<sub>x</sub>_ is the closest ancestor of _j<sub>b</sub>_ in \(\widetilde{\mathcal{T}}\) such that _j<sub>x</sub>\<j<sub>b</sub>_ (the other case is analogous). Clearly, _j<sub>b</sub>_ determines _j<sub>x</sub>_ uniquely. And since _b_’s subtree contains _S<sub>j<sub>b</sub></sub>_ in its entirety, _j<sub>b</sub>_ determines _b_ uniquely too. So once you know _j<sub>b</sub>_, the only uncertainty left about this alternation is _which_ access within

