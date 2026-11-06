**Algorithm 2** Function to modify forest represented by Link-Cut structure.

function TryAdd(LC,u,v)<br>
   \(uRoot\leftarrow LC.\text{FindRoot}(u)\)<br>
   \(vRoot\leftarrow LC.\text{FindRoot}(v)\)<br>
   if \(uRoot\neq vRoot\) then<br>
   LC.evert(u)<br>
   LC.link(u, v)<br>
   return null<br>
   else<br>
   \(p\leftarrow LC.\text{parent}(u)\)<br>
   LC.cut(u)<br>
   LC.link(u, v)<br>
   return (u, p)<br>
   end if<br>
end function

**Algorithm 3** Handling edge addition in a sparse certificate.

procedure HandleAddition(e)<br>
   \((u,v)\leftarrow endpoints(e)\triangleright 1\). Define endpoints of edge e<br>
   \(result\leftarrow TryAdd(LC_1,u,v)\)<br>
   if \(result\neq\text{null then}\)<br>
   \((x,y)\leftarrow endpoints(result)\)<br>
   \(i\leftarrow 2\)<br>
   while \(i\le k\) do<br>
   \(result\leftarrow TryAdd(LC_i,x,y)\)<br>
   if result=null then break<br>
   else<br>
   \((x,y)\leftarrow endpoints(result)\)<br>
   \(i\leftarrow i+1\)<br>
   end if<br>
   end while<br>
end if<br>
end procedure

F1
F2
F3
V1
V2
V3
V1
V2
V3
V1
V2
V3
{v1, v4}
V4
V5
V6
V4
V5
V6
V4
V5
V6
inserted edge
displaced edge
absorbed edge

Figure 1: HandleAddition({_v_<sub>4</sub>_,v_<sub>6</sub>}): edge {_v_<sub>4</sub>_,v_<sub>6</sub>} displaces {_v_<sub>1</sub>_,v_<sub>4</sub>} from _F_<sub>1</sub>; edge {_v_<sub>1</sub>_,v_<sub>4</sub>} is absorbed into _F_<sub>2</sub>. _F_<sub>3</sub> remains unchanged.

