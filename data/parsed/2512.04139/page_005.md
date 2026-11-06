Finally, the algorithm filters out any positions that fall outside the boundaries of the board, ensuring that both row and column indices lie within the range 0 to _n_-1. Then the resulting set of invalid positions is returned and used to restrict future queen placements, effectively reducing the size of the search space. Since the algorithm performs checks across rows, columns, and diagonals in a single pass, its overall time complexity is _O(n_<sup>2</sup>).

**Algorithm 1** Invalid Points Calculation

Require: n, i, j (Board size and queen position)<br> Ensure: Set of invalid positions for a queen placed at (i,j)<br> Initialize points \(\leftarrow\emptyset\)<br> for x=0 to n-1 do<br>   Add (x,j) to points \(\triangleright\) Mark all positions in column j<br>   Add (i,x) to points \(\triangleright\) Mark all positions in row i<br>   Add (x,i+j-x) to points \(\triangleright\) Mark negative diagonal<br>   Add (x,x-i+j) to points \(\triangleright\) Mark positive diagonal<br>   end for<br> Remove (i,j) from points \(\triangleright\) Remove the queen’s position<br> Filter points to retain only (p,q) where \(0\le p,q<n\) return points

## 3.2. Function: Las Vegas Algorithm

The Las Vegas Algorithm, 2 solves the N-Queens problem by randomly placing queens on an _n_ x _n_ chessboard while making sure that no two queens can attack each other.

