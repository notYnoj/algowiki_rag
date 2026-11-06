Data: s and <o>s</o>.<br>
Result: A \(\sqrt{n}\) approximate solution for LCS.<br>
\(s^*\leftarrow\) an empty string;<br>
for \(i\in[1,n]\) do<br>
   \(p\leftarrow\) a random variable which is equal to 1 with probability \(1/\sqrt{n}\) and 0 otherwise ;<br>
   if p=1 then<br>
add<br>
_s<sub>i</sub>_<br>
to<br>
the<br>
end<br>
of<br>
_s_<br>
<sup>∗</sup><br>
;<br>
   \(T^*\leftarrow\) a \([0,\dots,|s^*|]\times[0,\dots,|s^*|]\) array initially containing \(\infty\);<br>
   for \(i\leftarrow 0\) to |s<sup>∗</sup>| do<br>
\(T^*[i][0]\leftarrow 0\);<br>
   for \(j\leftarrow 1\) to |s<sup>∗</sup>| do<br>
   for \(i\leftarrow 1\) to |s<sup>∗</sup>| do<br>
\(T^*[i][j]\leftarrow\mathrm{min}\{T^*[i-1][j],\mathrm{first}(\overline{s},T^*[i-1][j-1],s_i^*)\}\)<br>
;<br>
   \(mx\leftarrow|s^*|\);<br>
   while \(T^*[|s^*|][mx]=\infty\) do<br>
\(mx\leftarrow mx-1\)<br>
;<br>
return (<br>
_mx_<br>
);

In the rest of this section, we use the above definitions to demonstrate the ideas of our solution in an informal way. Based on the above definitions, we aim to design a linear time algorithm with approximation factor \(\overline{o}(\sqrt{n})\). Before we go further, we note a few points.

• We emphasize that the arguments we make in this section are not mathematically coherent and we may intentionally oversimplify some issues here in the hope that the reader grasps a more intuitive explanation of the ideas. Later in Sections 6, 7, and 8 we bring formal and detailed discussions to prove the approximation factor of our solution.<tbc>

• For simplicity, in the pseudocodes of the algorithms, we only report the solution size. However, it is easy to observe that in each case the actual solution can also be reported in linear time.<tbc>

• Anywhere we use the term w.h.p. we mean a probability whose difference with 1 is exponentially small (in terms of _n_).<tbc>

• It may be confusing how an exponent 0.497956 is obtained using the algorithms that we outline in this section. However, a patient reader can find a lot of technical hurdles in Sections 6, 7, and 8 that we skip or simplify in this section. By considering these technicalities, the upper bound on the exponent of the approximation factor would be equal to 0.497956.

As mentioned before, our solution consists of several algorithms that we run one by one. Each of the algorithms performs well on a class of inputs. At each step of our solution, we use the term _nontrivial_ instances to refer to the inputs that are not approximated within a factor of \(\overline{o}(\sqrt{n})\) by the algorithms that have been performed until that step. Therefore, initially, all the input instances are nontrivial.

**Algorithm 0:** a \(\sqrt{n}\) approximate solution for LCS.

