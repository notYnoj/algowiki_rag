**sub** d {<br>
($xs, $ys, $xe, $ye, $th) = @_;<br>
$xs += $col; $ys += $row;<br>
$xe += $col; $ye += $row;<br>
$xs \*= $xscale; $ys \*= $yscale;<br>
$xe \*= $xscale; $ye \*= $yscale;<br>
**push** @xs, $xs; **push** @ys, $ys;<br>
**push** @xe, $xe; **push** @ye, $ye;<br>
**push** @th, $th;<br>
}<br>
**sub** gron {<br>
**print** "\<svg\_width=\\"700\\"\_height=\\"900\\"\_viewPort=\\"0\_0\_700\_900\\"\\n";<br>
**print** "\_version=\\"1.1\\"\_xmlns=\\"http://www.w3.org/2000/svg\\"\>\\n";<br>
# \<rect x=0 y=0 width=200 height=320 fill="linen"/\><br>
}<br>
**sub** merge {<br>
**for** ($i=0; $i\<=$#xs; $i++) {<br>
**for** ($j=$0; $j\<=$#xs; $j++) {<br>
**if** ( ($i != $j) && ($xe[$i] == $xs[$j]) && ($ye[$i] == $ys[$j]) &&<br>
( (($xs[$i] == $xe[$i]) && ($xe[$i] == $xs[$j]) && ($xs[$j] == $xe[$j])) ||<br>
(($ys[$i] == $ye[$i]) && ($ye[$i] == $ys[$j]) && ($ys[$j] == $ye[$j])) ) ) {<br>
# update ith entry <br>
$xe[$i] = $xe[$j];<br>
$ye[$i] = $ye[$j];<br>
# delete jth entry <br>
$xs[$j] = $xs[$#xs];<br>
$ys[$j] = $ys[$#ys];<br>
$xe[$j] = $xe[$#xe];<br>
$ye[$j] = $ye[$#ye];<br>
$th[$j] = $th[$#th];<br>
**pop** @xs; **pop** @ys; **pop** @xe; **pop** @ye, **pop** @th;<br>
**return** $#xs+1;<br>
}<br>
}<br>
return 0;<br>
}<br>
**sub** groff {<br>
# compact the vector list<br>
**while** (merge()) { }<tbc>

