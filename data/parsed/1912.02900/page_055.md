the algorithm.

## 6.5.1 Conflicting sets

Our algorithm uses the notion of conflicting point sets, defined as follows.

**Definition 6.14 (Conflicting Sets)** _Let Z and_ \(Z'\) _be sets of points. We say that Z and_ \(Z'\) _are_ conflicting _if there is a pair of points_ \(p\in Z\) _and_ \(p'\in Z'\)_, such that_ \((p,p')\) _is not satisfied in_ \(Z\cup Z'\)_. In other words, set_ \(Z\cup Z'\) _contains no point in_ \(\square_{p,p^\prime}\backslash\{p,p'\}\).

**Lemma 6.15** _Let Z and_ \(Z'\) _be two point sets, each of which is a satisfied set. Then the sets Z and_ \(Z'\) _are not conflicting if and only if_ \(Z\cup Z'\) _is satisfied._

**Proof:** Assume first that \(Z\cup Z'\) is satisfied. Then it is clear that for every pair \(p\in Z\), \(p'\in Z'\) of points, some point \(r\in Z\cup Z'\) lies in \(\square_{p,p^\prime}\backslash\{p,p'\}\)), so _Z_ and \(Z'\) are not conflicting.

Assume now that _Z_ and \(Z'\) are conflicting, and let \(p\in Z\) and \(p'\in Z'\) be the corresponding pair of points. Then \((p,p')\) is not satisfied in \(Z\cup Z'\), and so \(Z\cup Z'\) is not a satisfied set of points. \(\square\)

The following definition is central to our algorithm.

**Definition 6.16 (Top representation)** _Let Z be any set of points. A_ top representation _of Z, that we denote by_ top(_Z), is a subset_ \(Z'\subseteq Z\) _of points, obtained as follows: for every column C that contains points from Z, we add the topmost point of Z that lies on C to_ \(Z'\).

**Observation 6.17** _Let_ \(\mathrm{top}(Z)\subseteq Z\) _be the top representation of Z, and let R be a row lying strictly above all points in Z. Let Y be any set of points lying on row R. Then top(Z_) _is conflicting with Y if and only if Z is conflicting with Y ._

**Proof:** Assume that _Y_ is conflicting with _Z_, and let \(p\in Y\) , \(q\in Z\) be a pair of points, such that no point of \(Y\cup Z\) lies in \(\square_{p,q}\backslash\{p,q\}\). But then \(q\in\mathrm{top}(Z)\) must hold, and no point of \(\mathrm{top}(Z)\cup Y\) lies in \(\square_{p,q}\backslash\{p,q\}\), so top(_Z_) and _Y_ are conflicting.

Assume now that top(_Z_) and _Y_ are conflicting, and let \(p\in Y\) , \(q\in\mathrm{top}(Z)\) be a pair of points, such that no point of \(Y\cup\mathrm{top}(Z)\) lies in \(\square_{p,q}\backslash\{p,q\}\). But then no point of \(Y\cup Z\) lies in \(\square_{p,q}\backslash\{p,q\}\), and, since \(\mathrm{top}(Z)\subseteq Z\), sets top(_Z_) and _Y_ are conflicting. \(\square\)

## 6.5.2 The Algorithm

Let _X_ be the input point set, that is a semi-permutation. We denote by R={_R_<sub>1</sub>_,...,R<sub>m</sub>_} the set of all active rows for _X_, and we assume that they are indexed in their natural bottom-to-top order. We denote by C={_C_<sub>1</sub>_,...,C<sub>n</sub>_} the set of all active columns of _X_, and we assume that they are indexed in their natural left-to-right order. We also denote _X_={_p_<sub>1</sub>_,...,p<sub>m</sub>_}, where for all \(1\le i\le m\), _p<sub>i</sub>_ is the unique point of _X_ lying on row _R<sub>i</sub>_. For an index \(1\le t\le m\), we denote by \(\mathcal{R}_{\le t}=\{R_1,\dots,R_t\}\), and we denote by \(X_{\le t}=\{p_1,\dots,p_t\}\).

Note that, if _Y_ is a feasible solution to instance _X_, then for all \(1\le t\le m\), the set \(X_{\le t}\cup Y_{\le t}\) of points must be satisfied (here \(Y_{\le t}\) is the set of all points of _Y_ lying on rows of \(\mathcal{R}_{\le t}\).) Our dynamic programming-based algorithm constructs the optimal solution row-by-row, using this observation. We use height profiles, that we define next, as the "states" of the dynamic program.

