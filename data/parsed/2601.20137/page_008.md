**Algorithm 4** Procedure for handling edge deletion operations.

procedure HandleDeletion(e)<br>
   \((u,v)\leftarrow\) endpoints(e)<br>
   \(G\leftarrow G\backslash\{e\}\)<br>
   \(flow\leftarrow\) DinicMaxFlow(G,u,v)<br>
   if \(flow\ge k\) then<br>
   return<br>
   else if flow=k-1 then<br>
   \(G_f\leftarrow\) Residual Graph from Dinic’s execution on G<br>
   \(S\leftarrow\{w\in V|w\text{is reachable from}u\text{in}G_f\}\)<br>
   \(T\leftarrow\{w\in V|v\text{is reachable from}w\text{in}G_f\}\)<br>
   if \(S=\{u\}\wedge T=\{v\}\) then<br>
   \(u'\leftarrow\) arbitrarily chosen vertex in G<br>
   \(G\leftarrow G\cup\{\{u,u'\},\{u',v\}\}\)<br>
   else<br>
   \(u'\leftarrow\) arbitrarily chosen vertex from S<br>
   \(v'\leftarrow\) arbitrarily chosen vertex from T<br>
   \(G\leftarrow G\cup\{u',v'\}\)<br>
   end if<br>
   end if<br>
end procedure

V3
V1
V2
V4

V3
S
V1
V2
T
V4

V3
V1
V2
V4

V2
V3
V1
V4
V6
V5

T = {v2}
V2
V3
V2
V3
S = {v1}
V1
V4
V6
V5

V2
V3
V1
V4
V6
V5

(a) \(G'=G\backslash\{v_1,v_2\}\)

(b) Residual graph _G<sub>f</sub>_

(c) Augmented graph \(G''\)

Figure 2: HandleDeletion({_v_<sub>1</sub>_,v_<sub>2</sub>}): single augmenting edge (\(|T|\ge 2\)).

(a) \(G'=G\backslash\{v_1,v_2\}\)

(b) Residual graph _G<sub>f</sub>_

(c) Augmented graph \(G''\)

Figure 3: HandleDeletion({_v_<sub>1</sub>_,v_<sub>2</sub>}): two augmenting edges (|_S_|=|_T_|=1).

