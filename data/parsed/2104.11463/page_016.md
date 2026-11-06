<tbc>**Algorithm 2** Resolving Case 2.

function ResolveCase2(\(\mathcal{E}'^+\))<br>
  \(\widetilde{f}:=\) MakeAffineTemplate(k)<br>
   C:= GetConstraints(\(\widetilde{f},\mathcal{E}'^+\))<br>
  \(\rho:=\) GetModel(C)<br>
   if \(\rho\) is undefined then<br>
   h:= ChooseQualifier(E<sup>\('^+\)</sup>)<br>
   D\(_{\ge 0}:=\) ResolveCase2(\(\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})\ge 0\wedge h(\widetilde{v}')\ge 0\}\))<br>
   D\(_{<0}:=\) ResolveCase2(\(\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})<0\wedge h(\widetilde{v}')<0\}\))<br>
   return (if \(h(\widetilde{x})\ge 0\) then D\(_{\ge 0}\) else D\(_{<0}\))<br>
   else<br>
   return \(\widetilde{f}\)<br>
   end if<br>
end function<br>
function GetConstraints(D,E<sup>+</sup>)<br>
   return \(\{R_{\widetilde{f}_D}(\widetilde{v},\widetilde{v}')|(\widetilde{v},\widetilde{v}')\in\mathcal{E}^+\}\) where \(\widetilde{f}_D\) is the tuple of piecewise affine functions corresponding to D<br>
end function

**Algorithm 3** A criterion for eager qualifier selection.

function QualityMeasure(h,E<sup>\('^+\)</sup>)<br>
   E\(_{++}:=\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})\ge 0\wedge h(\widetilde{v})\ge 0\}\)<br>
   E\(_{+-}:=\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})\ge 0\wedge h(\widetilde{v})<0\}\)<br>
   E\(_{-+}:=\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})<0\wedge h(\widetilde{v})\ge 0\}\)<br>
   E\(_{--}:=\{(\widetilde{v},\widetilde{v}')\in\mathcal{E}'^+|h(\widetilde{v})<0\wedge h(\widetilde{v})<0\}\)<br>
  \(\widetilde{f}:=\) MakeAffineTemplate(k)<br>
   C\(_+:=\) GetConstraints(\(\widetilde{f},E_{++}\)) C<sub>-</sub>:= GetConstraints(\(\widetilde{f},E_{--}\))<br>
   N<sub>+</sub>:= MaxSmt(C<sub>+</sub>) N<sub>-</sub>:= MaxSmt(C<sub>-</sub>)<br>
   return N<sub>+</sub>+N<sub>-</sub>+(|E<sub>+-</sub>|+|E<sub>-+</sub>|)(1-entropy(|E<sub>+-</sub>|,|E<sub>-+</sub>|))<br>
end function

**Assumption 18.** If halfspace \(h(\widetilde{x})\ge 0\) is chosen in Line 6 of Algorithm 2, then there exist \(\widetilde{v},\widetilde{u}\in\underline{\mathcal{E}'^+}\) such that \(h(\widetilde{v})\ge 0\) and \(h(\widetilde{u})<0\).

We explain two strategies (eager and lazy) to choose halfspaces that can be used to implement ChooseQualifier. Both of them are guaranteed to terminate, and moreover, intended to yield simple decision trees.

## Eager strategy.

In the eager strategy, we eagerly generate a finite set _H_ of halfspaces from the set E<sup>+</sup> of all examples beforehand and choose the best one from _H_ with respect to a certain quality measure. To satisfy Assumption 18, _H_ are generated so that any two points \(\widetilde{u},\widetilde{v}\in\underline{\mathcal{E}^+}\) can be separated by some halfspace \((h(\widetilde{x})\ge 0)\in H\).

For example, we can use intervals \(H=\{\pm(x_i-a_i)\ge 0|i=1,\dots,n\wedge(a_1,\dots,a_n)\in\underline{\mathcal{E}^+}\}\) and octagons \(H=\{\pm(x_i-a_i)\pm(x_j-a_j)\ge 0|i\neq j\wedge(a_1,\dots,a_n)\in\underline{\mathcal{E}^+}\}\) where \(\widetilde{x}=(x_1,\dots,x_n)\). For any input \(\mathcal{E}'^+\subseteq\mathcal{E}^+\) of

