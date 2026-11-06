**Algorithm 2** Las Vegas Algorithm for _n_-Queens Problem

Require: n (Size of the board)<br>
Ensure: An \(n\times n\) matrix with queens placed<br>
Define function `create\_boolean\_array`(n)<br>
Return an \(n\times n\) matrix of ones<br>
Define function `las\_vegas`(n)<br>
\(a\leftarrow\) True<br>
while a is True do<br>
   Initialize \(result\leftarrow\) create a boolean array of size \(n\times n\)<br>
   Initialize \(valid\text{\_}space\leftarrow\) list of all indices in \(n\times n\)<br>
   for i=0 to n-1 do<br>
   Select random q\_pos from valid\_space and remove it<br>
   Compute \(x=\lfloor q\text{\_}pos/n\rfloor\), y=q\_pos mod n<br>
   Compute attack positions using `invalid\_points`(n,x,y)<br>
   for each (p,q) in attack positions do<br>
   Set \(result[p,q]\leftarrow 0\)<br>
   Remove corresponding index from valid\_space<br>
   end for<br>
   if valid\_space is empty then<br>
   if i\>n-2 then<br>
\(a\leftarrow\)<br>
False<br>
   end if<br>
   break<br>
   end if<br>
   end for<br>
end whilereturn result

It begins with a board where all positions are marked as valid, and a one dimensional list is created containing every possible position on the board. Then, the algorithm randomly picks one valid position from this list and places a queen there. After placing a queen on the board, it uses the Invalid Points Algorithm, 1 to find all positions that become unsafe because of that queen. These unsafe positions are marked on the board and also removed from the list of valid positions.

If the algorithm runs out of valid positions before placing all n queens, it starts over and tries again. This process continues until queens are successfully placed in all rows without conflicts. Once a valid arrangement is found, the algorithm returns the completed board along with the number of attempts it took. Since the solution depends on how many retries are needed, the overall time complexity is \(O(p\cdot n^2)\), where _p_ is the number of attempts before a solution is found.<br>
Now we present the working example of the algorithm for the case of N=4<br>
First we initialize a board with all position as valid,(V)<tbc>

\begin{tabular}{ccccc}
V & V & V & V \\
V & V & V & V \\
V & V & V & V \\
V & V & V & V \\
\end{tabular}

1: Initialize a board with all position as valid.

