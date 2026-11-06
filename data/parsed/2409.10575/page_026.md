Input: - An instance I.<br>
- A matching M.<br>
- A tie-breaking strategy S.<br>
- A set of agents whose preference lists are altered Q<sub>a</sub>.<br>
- A base algorithm A.<br>
- The time threshold for obtaining stable matchings T.<br>
Output: A matching M.<br>
Function ObtainStableMatching(I,M,S,Q<sub>a</sub>):<br>
   \(X:=Q_a\) ; \(\triangleright X\) is the set of agents requiring examination<br>
   while (execution time \(\le T\) **and** \(X\neq\emptyset\)) do<br>
   v:= randomly pop one agent from X;<br>
   y<sub>worst</sub>:= the worst partner of v in M under S;<br>
   sort v’s tie-free preference list in ascending order;<br>
   for (each \(y\in v's\) tie-free preference list) do<br>
   if \((y\in M(v))\) then<br>
   continue;<br>
   else if (v is full **and** \(r_v^*(y)>r_v^*(y_{worst})\)) then<br>
break;<br>
   else if ((v,y) is a blocking pair under S) then<br>
   z<sub>worst</sub>:= the worst partner of y in M under S;<br>
   if (v is full **and** y<sub>worst</sub> is full) then<br>
\(X:=X\cup y_{worst}\)<br>
;<br>
   end<br>
   if (y is full **and** z<sub>worst</sub> is full) then<br>
\(X:=X\cup z_{worst}\)<br>
;<br>
   end<br>
   Remove BP (v,y) in M;<br>
   y<sub>worst</sub>:= the worst partner of v in M under S;<br>
   end<br>
   end<br>
   end<br>
   if \((X\neq\emptyset)\) then<br>
   M:= apply the base algorithm A to find a stable matching after<br>
breaking all the ties in the instance I using the tie-breaking strategy<br>
S;<br>
   end<br>
return M

**Algorithm 4:** Obtain stable matching

