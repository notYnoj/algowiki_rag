_Every time we enter or leave a node, we attach the node to the end of the sequence (do not attach the virtual root). We use_ **F**[_i_] _to denote the i-th node in such sequence._

Observe that bi-order traversal of rev(**F**) corresponds to the reversed bi-order traversal of **F**.

**Definition 3.3** (\[Mao22, Definition 2.4\])**.** _For_ \(1\le\ell\le r\le 2|\mathbf{F}|+1\)_, consider bi-order traversal_ **F**[1],**F**[2]_,...,_**F**[2|**F**] _of_ **F**_. We use_ \(\mathbf{F}[\ell..r\mathbf{r})\) _to denote the forest obtained by removing from_ **F** _all nodes that appear at least once in_ **F**[1],**F**[2]_,...,_**F**[\(\ell-1\)] _or_ **F**[_r_],**F**[_r_+1]_,...,_**F**[2|**F**] _, and we call such forest a_ subforest of **F**.

Consider the bi-order traversal sequence of a forest **F**. For a node \(v\in\mathbf{F}\), we define l(_v_) as the first index where _v_ appears in the bi-order traversal sequence, and r(_v_) as one plus the second index where _v_ appears. By these definitions, \(\mathbf{F}[\ell..r\mathbf{r})\) contains _v_ if and only if \(\ell\le\mathrm{l}(v)\) and \(\mathrm{r}(v)\le r\). Additionally, **F**[l(_v).._r(_v_)) corresponds to sub(_v_). Note that \(\mathbf{F}[\ell..r\mathbf{r})\) and \(\mathbf{F}[\ell'..r'\mathbf{r})\) may represent the same forest for distinct pairs \((\ell,r)\) and \((\ell',r')\).

**Definition 3.4** (\[Mao22, Definition 2.5\])**.** _For a forest_ **F**_, we say subforest_ \(\mathbf{F}'\) _of_ **F** _is a_ synchronous subforest of **F** _if there exists a node_ \(v\in\mathbf{F}\) _that is either a node in_ **F** _or the virtual root of_ **F**_, and such that_ \(\mathbf{F}'\) _is the union of subtrees of subsequent children of v._

**Anchors and anchor sets.** A key point in working with a similarity of the form \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) between two subforests **F**[_x...y_] and \(\mathbf{F}'[x'..y'\mathbf{)}\) in bi-order traversal is realizing that the following inequality holds for all \((z,z')\in[x..y]\times[x'..y']\):

\(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\ge\mathrm{sim}(\mathbf{F}[x..z\mathbf{)},\mathbf{F}'[x'..z'\mathbf{)})+\mathrm{sim}(\mathbf{F}[z..y\mathbf{)},\mathbf{F}'[z'..y'\mathbf{)}).\)

An _anchor_, is a pair \((z,z')\) where such last inequality holds with equality.

**Definition 3.5** (Anchors and anchor sets)**.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be two forests, and let_ \(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)}\) _be two subforests. We say that_ \((z,z')\in[1..(2|\mathbf{F}|+1)]\times[1..(2|\mathbf{F}'|+1)]\) is an anchor of \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) _if_ \(x\le z\le y\)_, and_ \(x'\le z'\le y'\) _and_

\(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})=\mathrm{sim}(\mathbf{F}[x..z\mathbf{)},\mathbf{F}'[x..z'\mathbf{)})+\mathrm{sim}(\mathbf{F}[z..y\mathbf{)},\mathbf{F}'[z'..y\mathbf{)}).\)

_Further, we say_ \(\mathrm{B}\subseteq[1..(2|\mathbf{F}|+1)]\times[1..(2|\mathbf{F}'|+1)]\) is an anchor set of \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) _if there exists_ \((z,z')\in\mathrm{B}\) _such that_ \((z,z')\) _is an anchor of_ \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\).

We note that we use the concept of anchor sets, defined as subsets of \[1_.._(2|**F**|+1)\]\times[1..(2|\mathbf{F}'|+1)]\), not only for similarities of the form \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) but also for other subforests where the same bi-order indexing applies, such as \(\mathrm{sim}(\mathbf{F}[x..z\mathbf{)}+\mathbf{F}[z..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\).

We extend the concept of anchors to _paired anchors_.

**Definition 3.6** (Paired anchors and anchor sets)**.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be two forests, and let_ \(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)}\) _be two subforests. We say that_ \((z,z'),(w,w')\in[1..(2|\mathbf{F}|+1)]\times[1..(2|\mathbf{F}'|+1)]\) are paired anchors of \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) _if_ \(x\le z\le w\le y\)_, and_ \(x'\le z'\le w'\le y'\) _and_

\(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})=\mathrm{sim}(\mathbf{F}[x..z\mathbf{)},\mathbf{F}'[x..z'\mathbf{)})\)<br> \(+\mathrm{sim}(\mathbf{F}[z..w\mathbf{)},\mathbf{F}'[z'..w'\mathbf{)})+\mathrm{sim}(\mathbf{F}[w..y\mathbf{)},\mathbf{F}'[w'..y'\mathbf{)}).\)

_Further, we say_ \(\mathrm{B},\mathrm{B}'\subseteq[1..(2|\mathbf{F}|+1)]\times[1..(2|\mathbf{F}'|+1)]\) are paired anchor sets of \(\mathrm{sim}(\mathbf{F}[x..y\mathbf{)},\mathbf{F}'[x'..y'\mathbf{)})\) _if there are_ \((z,z)\in\mathrm{B}\) _and_ \((w,w')\in\mathrm{B}'\) _such that_ \((z,z')\) _and_ \((w,w')\) _are paired anchors._

