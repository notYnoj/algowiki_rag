<tbc>Section 4.3 presents the subroutine `ObtainStableMatching`, Section 4.4 outlines two modifications for developing TBLS-E, an equity-focused variant of TBLS.

Input: - An instance I.<br>
- A small probability p<sub>d</sub>.<br>
- A base algorithm A.<br>
- The maximum number of iterations max.iters.<br>
- Two integer k<sub>u</sub> and k<sub>w</sub>.<br>
- The time threshold for obtaining stable matchings T.<br>
Output: - A matching M.<br>
- A tie-breaking strategy S.<br>
Function Main(I):<br>
   S:= arbitrarily break all the ties in the instance I;<br>
   M:= apply the base algorithm A to find a stable matching after<br>
breaking all the ties in the instance I using the tie-breaking strategy S;<br>
   S<sub>best</sub>:=S;<br>
   M<sub>best</sub>:=M;<br>
   iter:=0;<br>
   while \((iter\le max.iters)\) do<br>
   S,Q<sub>a</sub>:=`RefineTieBreakingStrategy(I,M,S)`;<br>
   M:=`ObtainStableMatching(I,M,S,Q<sub>a</sub>)`;<br>
   if \((E(M,I)\ge E(M_{best},I))\) then<br>
   S<sub>best</sub>:=S;<br>
   M<sub>best</sub>:=M;<br>
   end<br>
   iter:=iter+1;<br>
   end<br>
return M<sub>best</sub>,S<sub>best</sub>

## 4.1 Evaluation function

The evaluation function is defined by two criteria. The primary criterion is to maximize the matching size. Subsequently, among matchings of identical size, the secondary criterion gives priority to freeing up agents with longer preference lists, as these agents have a higher likelihood of being matched later to increase the matching size. Therefore, we define the evaluation function as follows:<tbc>

\(maxE(M,L)=\text{size}(M)\times bigM+\sum_{v\in F_M}|L_v|\times\big(b(v)-|M(v)|\big)\)

**Algorithm 1:** A Tie-breaking based Local Search Algorithm

