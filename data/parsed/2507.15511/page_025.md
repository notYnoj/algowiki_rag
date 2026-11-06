**Algorithm 8** KeyOf\((b,s',e')\)

**Require:** Half index _b_; real sum \(s'\); mask \(e'\)

1: **if AliasingEnabled then**

2: \(\chi\leftarrow e'[i_1^{(b)}]\)

3: \(\tilde{s}\leftarrow s'-\chi\cdot\left(x_1^{(b)}-x_0^{(b)}\right)\)

4: **return** \((\tilde{s},\chi)\)

5: **else**

6: **return** \(s'\)

**Algorithm 9** InsertOrImprove\((\mathtt{key},e',b)\) (suppression-on-overwrite)

**Require:** Key \(=s'\) (no alias) or \((\tilde{s},\chi)\) (alias); mask \(e'\); half _b_

1: \(\mathtt{Memo}\leftarrow\mathtt{Memo}_b;\mathtt{Rep}\leftarrow\mathtt{Rep}_b\)

2: **if** \(\mathtt{key}\notin\mathtt{Memo}\) **then**

3: \(\mathtt{Memo}[\mathtt{key}]\leftarrow e'\)

4: \(\mathtt{Rep}[\mathtt{key}]\leftarrow\mathtt{State}(\cdot)\triangleright\) bound representative to new state lazily

5: **return true** \(\triangleright\) new canonical representative

6: **else if** IsLexicographicallySmaller\((e',\mathtt{Memo}[\mathtt{key}])\) **then**

7: /\* suppress old representative so it never extends further \*/

8: **if** \(\mathtt{Rep}[\mathtt{key}]\neq\mathtt{nil}\) **then** \(\mathtt{Rep}[\mathtt{key}].\mathtt{doNotExtend}\leftarrow\mathtt{true}\)

9: \(\mathtt{Memo}[\mathtt{key}]\leftarrow e'\)

10: \(\mathtt{Rep}[\mathtt{key}]\leftarrow\mathtt{State}(\cdot)\)

11: **return true** \(\triangleright\) canonical representative updated

12: **else**

13: **return false**

## Notes on Modularity.

• **Enumeration Logic.** DoubleMIM-IC-SubsetSum drives interleaved enumeration; ProcessExtension encapsulates "generate, deduplicate, (optionally) gate by CNF, then check".<tbc>

• **Deduplication.** InsertOrImprove implements the lex-minimal canonicalization with _suppression-on-overwrite_, ensuring each canonical key is expanded at most once.<tbc>

• **Aliasing Hooks.** KeyOf provides a single switch for aliased vs. true sums; the CNF gate is the call to Expandable\((\cdot)\) (Appendix E).<tbc>

• **Solution Checks.** The real-time checks defer to Algorithms 10 and 11.

## B.3 Time and Space Bounds

Let \(U_i:=|\Sigma(\ell_i)|\) and \(\widehat{U}:=\mathrm{max}(U_0,U_1)\).

### Without Aliasing.

By Theorems 1 and 2, enumerating each half in isolation costs \(O(U_i\cdot(n/2)^2)\) deterministically, and \(O(U_i\cdot(n/2))\) in expectation for the randomized variant. In the interleaved solver, every cross-half probe and canonical comparison can be _injectively charged_ to a unique successor attempt on the dominant side (the half with \(U_i=\widehat{U}\)) due to suppression-on-overwrite. Hence<tbc>

\(T_\mathrm{det}(n)=O\big(\widehat{U}\cdot n^2\big),\mathbb{E}\big[T_\mathrm{rand}(n)\big]=O\big(\widehat{U}\cdot n\big),\)

