**Algorithm 1** Dynamic-LOCAL algorithm for 3-coloring a bipartite graph. To update the coloring after an insertion, the appropriate update procedure, either NodeInsertion or EdgeInsertion, is called.

**Global state:** graph _G_=(_V,E_), potential \(\phi(v)\), coloring _c(v_)<br>
procedure FixAndClear(edge _e_=(_v,w_))<br>
   \(\triangleright\) _Ensure parity-consistency_ \(\triangleleft\)<br>
   if \(v\unknown_\mathrm{par}w\) then<br>
   \(\triangleright\) _Choose component that currently has lower peak potential_ \(\triangleleft\)<br>
   Find C<sub>v</sub> and C<sub>w</sub>, the connected components of the endpoints before insertion of e.<br>
   \(C_m\leftarrow\mathrm{argmin}_{C\in\{C_v,C_w\}}\mathrm{max}_{v\in C}\phi(v)\)<br>
   \(\triangleright\) _Increment potential by 3 to flip parity without changing the coloring_ \(\triangleleft\)<br>
   Increment \(\phi(v)\) of every node \(v\in C_m\) by 3<br>
   \(\triangleright\) _Clear state inside edit-area_ \(\triangleleft\)<br>
   \(D\leftarrow\frac{1}{2}(\mathrm{max}_{v\in V}\phi(v)+1)\)<br>
   for all nodes x with d<sub>G</sub>(x,v)\<D and d<sub>G</sub>(x,w)\<D do<br>
   \(\phi(x)\leftarrow\perp\)<br>
procedure BuildAround(level k)<br>
   for all nodes v with \(\phi(v)=\perp\) that have a neighbor w with \(\phi(w)=k\) do<br>
   \(\phi(v)\leftarrow k-1\)<br>
procedure ExpandBorders<br>
   \(\phi_\mathrm{max}\leftarrow\mathrm{max}_{v\in V}\phi(v)\)<br>
   for \(k=\phi_\mathrm{max},\dots,1\) do<br>
BuildAround(k)<br>
procedure TwoColoring(representative node v<sub>r</sub>)<br>
   \(v\leftarrow\) arbitrary node with \(\phi(v)\neq\perp\) that is reachable from v<sub>r</sub><br>
   if no such v exists then<br>
   \(\phi(v_r)\leftarrow 0\)<br>
   \(v\leftarrow v_r\)<br>
   while any node w with \(\phi(w)=\perp\) is reachable from v do<br>
   \(\phi(w)\leftarrow\mathrm{mod}(\phi(v)+d(v,w),2)\)<br>
procedure EdgeInsertion(edge e=(v,w))<br>
   \(\triangleright\) _Fix potential parity mismatch between newly connected components and erase area_<br>
to allow fixing the coloring_ \(\triangleleft\)<br>
FixAndClear(e)<br>
   \(\triangleright\) _Fill back lines of potential until_ \(\phi=0\) _is reached_ \(\triangleleft\)<br>
ExpandBorders<br>
   \(\triangleright\) _Complete coloring of edit-area with 2-coloring_ \(\triangleleft\)<br>
TwoColoring(v)<br>
   \(\triangleright\) _Obtain the coloring from the potential_ \(\triangleleft\)<br>
   for all \(v\in V\) do<br>
   \(\triangleright\) _Coloring c(v_) _has changed only for nodes within edit area_ \(\triangleleft\)<br>
   \(c(v)\leftarrow\mathrm{mod}(\phi(v),3)\)<br>
procedure NodeInsertion(node v)<br>
   \(\triangleright\) _The inserted node v is always isolated_ \(\triangleleft\)<br>
   \(\phi(v)\leftarrow 0\)<br>
   \(c(v)\leftarrow 0\)

