**Proposition 3.9.** _Consider two subforests_ \(\mathbf{F}[x..y),\mathbf{F}'[x'..y')\)_, and suppose there exist_ \(v\in\mathbf{F}[x..y)\) _and_ \(v'\in\mathbf{F}'[x'..y')\) _such that_

\(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v')))+\mathbf{F}'[\mathrm{l}(v')..y')).\)

_Then, we have that_

\(\mathrm{B}^\top(1,1,\mathrm{l}(v),\mathrm{l}(v'))=(\mathrm{l}(v)\times[1..\mathrm{l}(v')])\cup([1..\mathrm{l}(v)]\times\mathrm{l}(v'))\)

_is an anchor set of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

**Proof.** By Proposition 3.7, the set \(\mathrm{B}:=\mathrm{l}(v)\times[1..(2|\mathbf{F}'|+1)]\) serves as an anchor set for \(\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v'))+\mathbf{F}'[\mathrm{l}(v')..y'))\).

Suppose there exists an anchor \((z,z')\) contained in the subset \(\mathrm{B}':=\mathrm{l}(v)\times[\mathrm{l}(v')..(2|\mathbf{F}'|+1)]\subseteq\mathrm{B}\). For any such \((z,z')\), note that, by Proposition 3.7, the set \(\mathrm{B}'':=[1..\mathrm{l}(v)]\times\mathrm{l}(v')\) is an anchor set for \(\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..\mathrm{l}(v'))+\mathbf{F}'[\mathrm{l}(v')..z'))\). By Proposition 3.8(ii), we get that \(\mathrm{B}''\) is also an anchor set for \(\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v'))+\mathbf{F}'[\mathrm{l}(v')..y'))\).

Now, we perform a case distinction on whether there is an anchor \((z,z')\in\mathrm{B}\) of \(\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v')))+\mathbf{F}'[\mathrm{l}(v')..y'))\) contained in the subset \(\mathrm{B}'\) or not. In any case, \((\mathrm{B}\backslash\mathrm{B}')\cup\mathrm{B}''=(\mathrm{l}(v)\times[1..\mathrm{l}(v')])\cup([1..\mathrm{l}(v)]\times\mathrm{l}(v'))\) is an anchor set of \(\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v')))+\mathbf{F}'[\mathrm{l}(v')..y'))\). By the assumption, \((\mathrm{B}\backslash\mathrm{B}')\cup\mathrm{B}''\) is also an anchor set of \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

For certain of forms of similarities we can also find paired anchor sets.

**Proposition 3.10.** _Let_ \(\mathbf{F},\mathbf{F}'\) _be two forests, and let_ \(\mathbf{F}[x..y),\mathbf{F}'[x'..y')\) _be two subforests. Then, the two following hold:_

(**i)** _For any_ \(v\in\mathbf{F}[x..y)\) _such that_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..y'))\)_, we have that_ \(\mathrm{l}(v)\times[1..(2|\mathbf{F}'|+1)]\) _and_ \(\mathrm{r}(v)\times[1..(2|\mathbf{F}'|+1)]\) _are paired anchors sets of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).<tbc>

(**ii)** _For any_ \(v\in\mathbf{F}[x..y)\) _and_ \(v'\in\mathbf{F}'[x'..y')\) _such that_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[x..\mathrm{l}(v))+\mathbf{F}[\mathrm{l}(v)..y),\mathbf{F}'[x'..\mathrm{l}(v'))+\mathbf{F}'[\mathrm{l}(v')..y'))+\mathbf{F}'[\mathrm{l}(v')..y'))\)_, we have that_ \(\mathrm{B}^\top(1,1,\mathrm{l}(v),\mathrm{l}(v'))\) _and_ \(\mathrm{B}^\perp(\mathrm{r}(v),\mathrm{r}(v'),2|\mathbf{F}|+1,2|\mathbf{F}'|+1)\) _are paired anchors sets of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

**Proof.** We first prove (i). By Proposition 3.7, we have that \(\mathrm{l}(v)\times[1..(2|\mathbf{F}'|+1)]\) is an anchor set of \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\). Observe that **F**\[l(_v)..y_)=sub(_v_)+**F**\[r(_v)..y_)\]. Thus, by Proposition 3.7, for every \((z,z')\in\mathrm{l}(v)\times[1..(2|\mathbf{F}'|+1)]\), we have that \(\mathrm{r}(v)\times[1..(2|\mathbf{F}'|+1)]\) is an anchor set of \(\mathrm{sim}(\mathbf{F}[z..y),\mathbf{F}'[z'..y'))\). To conclude the proof of (i) we use Proposition 3.8(i).

We prove (ii) in a similar manner. By Proposition 3.9, the set \(\mathrm{B}^\top(1,1,\mathrm{l}(v),\mathrm{l}(v'))\) serves as an anchor set for \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\). For each \((z,z')\in\mathrm{B}^\top(1,1,\mathrm{l}(v),\mathrm{l}(v'))\), we have **F**\[_z..y_)=**F**\[_z.._r(_v_))+**F**\[r(_v)..y_)\] and \(\mathbf{F}[z'..y')=\mathbf{F}[z'..\mathrm{r}(v'))+\mathbf{F}[\mathrm{r}(v')..y')\). Thus, we can once again apply Proposition 3.9, using a symmetric equivalent that uses r(_v_) instead of l(_v_), and subsequently apply Proposition 3.8(i).

**Aligned Subtrees.** Next, we introduced what means for two subtrees to be _aligned_ by a similarity.

**Definition 3.11.** _Given two forests_ \(\mathbf{F},\mathbf{F}'\) _and nodes_ \(v\in\mathbf{F},v'\in\mathbf{F}'\)_, we say_ \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\) _aligns_ sub(_v_) _to_ \(\mathrm{sub}(v')\) _if_

\(\mathrm{sim}(\mathbf{F},\mathbf{F}')=\mathrm{sim}(\mathbf{F}[1..\mathrm{l}(v)),\mathbf{F}'[1..\mathrm{l}(v')))+\mathrm{sim}(\mathrm{sub}(v),\mathrm{sub}(v'))\)<br>
\(+\mathrm{sim}(\mathbf{F}[\mathrm{r}(v)..(2|\mathbf{F}|+1)),\mathbf{F}'[\mathrm{r}(v')..(2|\mathbf{F}'|+1))).\)

In other words, \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\) aligns sub(_v_) to \(\mathrm{sub}(v')\), if \(\{(\mathrm{l}(v),\mathrm{l}(v))\},\{(\mathrm{r}(v),\mathrm{r}(v'))\}\) are paired anchor sets.

