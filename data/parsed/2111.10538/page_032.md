**Algorithm 3** lcs-cmp data structure

data structure lcs-cmp<br>
members<br>
  \(\text{opt}_{a,1},\cdots,\text{opt}_{a,s}\)<br>
   \(Y_{a,1},\cdots,Y_{a,s}\)<br>
   \(\widetilde{\lambda}\in(0,1)\)<br>
   end members<br>
procedure Initial\((w_a,\{w_i\}_{i\in[s]},\widetilde{\lambda})\triangleright\) Lemma 3.22<br>
   for \(i\in[s]\) do<br>
   compute opt<sub>a,i</sub>, a fixed (e.g. lexicographically smallest) LCS between w<sub>a</sub> and w<sub>i</sub><br>
   end for<br>
   for \(i\in[s]\) do<br>
   \(Y_{a,i}\leftarrow\emptyset\)<br>
   \(w'_a\leftarrow w_a\)<br>
   while \(\text{LCS}(w'_a,w_i)\ge|w_a|\widetilde{\lambda}/2\) do<br>
   \(Y_{a,i}\leftarrow Y_{a,i}\cup\) characters in the LCS of \(w'_a\) and w<sub>i</sub><br>
   \(w'_a\leftarrow w'_a\backslash\) characters in the LCS of \(w'_a\) and w<sub>i</sub><br>
   end while<br>
   end for<br>
   return \(\{\text{opt}_{a,i}\}_{i\in[s]},\{Y_{a,i}\}_{i\in[s]}\)<br>
end procedure<br>
procedure Query(w<sub>i</sub>,w<sub>j</sub>) \(\triangleright\) Lemma 3.23<br>
   if \(|\text{opt}_{a,i}\cap Y_{a,j}|>\widetilde{\lambda}|w_a|/2\) then<br>
   return<br>
accept<br>
   else<br>
   return<br>
reject<br>
   end if<br>
end procedure<br>
end data structure

**Lemma 3.23** (Query)**.** _For any_ \((i,j)\in[s]\times[s]\)_, the_ Query _of data structure_ lcs-cmp _(Algorithm 3) runs in time O_(|_w<sub>a</sub>_|) _with the following properties:_

1. _If_ \(\text{lcs}_{w_a}(w_i,w_j)\ge\widetilde{\lambda}|w_a|\)_, then it outputs accept._<tbc>

_2._ _If_ \(\text{lcs}_{w_a}(w_i,w_j)<\widetilde{\lambda}^2|w_a|/4\)_, then it outputs reject._

_Proof._ Our algorithm takes the intersection of the characters that contribute to opt<sub>a,i</sub> with Y<sub>a,j</sub>. As explained earlier, if \(\text{lcs}_{w_a}(w_i,w_j)\ge\widetilde{\lambda}|w_a|\) then at least half of these characters belong to Y<sub>a,j</sub> and thus the intersection of one of the common subsequences contributing to Y<sub>a,j</sub> with opt<sub>a,i</sub> is at least \(\widetilde{\lambda}^2|w_a|/4\). Indeed, this can only happen if \(\text{lcs}_{w_a}(w_i,w_j)\ge\widetilde{\lambda}^2|w_a|/4\) in the first place. Otherwise we certainly output reject.

