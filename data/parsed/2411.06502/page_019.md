Observe that a set B is an anchor set of \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\) if and only if

\(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{max}_{(z,z^\prime)\in\mathrm{B}:x\le z\le y,x^\prime\le z^\prime\le y^\prime}\big\{\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x..z'))+\mathrm{sim}(\mathbf{F}[z..y),\mathbf{F}'[z'..y'))\big\}.\)

Moreover, for sets B and \(\mathrm{B}'\) are paired anchor sets holds

\(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{max}_{(z,z^\prime)\in\mathrm{B}:x\le z\le y,x^\prime\le z^\prime\le y^\prime}\big\{\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))\)<br> \(+\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))\)<br> \(+\mathrm{sim}(\mathbf{F}[w..y),\mathbf{F}'[w'..y'))\big\}.\)

In previous works, such as \[Mao22, Equation (9)\], it was observed that when **F** consists of more than one tree, there exists an anchor set with a simple representation. More specifically, if we can write **F**=**F**<sub>I</sub>+**F**<sub>r</sub> for two forests **F**<sub>I</sub>,**F**<sub>r</sub>, then \((2|\mathbf{F}_\mathrm{I}|+1)\times[1..(2|\mathbf{F}'|+1)]\) is an anchor set of \(\mathrm{sim}(\mathbf{F},\mathbf{F}')\). We rephrase this observation for subforests as follows.

**Proposition 3.7.** _Suppose that for two subforests_ \(\mathbf{F}[x..y),\mathbf{F}'[x'..y')\) _and some_ \(z\in[x..y]\)_, we have that_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))=\mathrm{sim}(\mathbf{F}[x..z)+\mathbf{F}[z..y),\mathbf{F}'[x'..y'))\) _holds. Then,_ \(z\times[1..(2|\mathbf{F}'|+1)]\) _is an anchor set of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

Next, we prove Proposition 3.8 that allows us to transform anchor sets.

**Proposition 3.8.** _Let_ \((z,z')\) _be an anchor of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\)_. Suppose_ B _is an anchor set of_ \(\mathrm{sim}(\mathbf{F}[z..y),\mathbf{F}'[z'..y'))\)_. Then, the two following hold:_

(**i)** _For any anchor set_ A _such that_ \((z,z')\in\mathrm{A}\)_, we have that_ A _and_ B _are paired anchor set._

**(ii)** B _is also anchor set of_ \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\).

**Proof.** From the assumptions on B, there exists \((w,w')\in\mathrm{B}\) such that \(\mathrm{sim}(\mathbf{F}[z..y),\mathbf{F}'[z'..y'))=\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))+\mathrm{sim}(\mathbf{F}[w..y),\mathbf{F}'[w'..y'))\). Combining this with the anchor assumption on \((z,z')\), we have

\(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\)<br> \(=\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))+\mathrm{sim}(\mathbf{F}[z..y),\mathbf{F}'[z'..y'))\)<br> \(=\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))+\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))+\mathrm{sim}(\mathbf{F}[w..y),\mathbf{F}'[w'..y')).\)

This shows (i). To prove (ii), it suffices to show that \(\mathrm{sim}(\mathbf{F}[x..w),\mathbf{F}'[x'..w'))=\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))+\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))\), which would imply that \((w,w')\) is an anchor of \(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\). To this end, observe that \(\mathrm{sim}(\mathbf{F}[x..w),\mathbf{F}'[x'..w'))>\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))+\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))\) would imply

\(\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y'))\)<br> \(=\mathrm{sim}(\mathbf{F}[x..z),\mathbf{F}'[x'..z'))+\mathrm{sim}(\mathbf{F}[z..w),\mathbf{F}'[z'..w'))+\mathrm{sim}(\mathbf{F}[w..y),\mathbf{F}'[w'..y'))\)<br> \(<\mathrm{sim}(\mathbf{F}[x..w),\mathbf{F}'[x'..w'))+\mathrm{sim}(\mathbf{F}[w..y),\mathbf{F}'[w'..y'))\)<br> \(\le\mathrm{sim}(\mathbf{F}[x..y),\mathbf{F}'[x'..y')),\)

a contradiction.

Using Proposition 3.8 we can transform the anchor set from Proposition 3.7 as follows.

