\(v_i^z,f_i^{1,z}\) and \(f_i^{2,z}\) prefer all of \(f_i^{3,z},f_i^{4,z}\) and \(f_i^{5,z}\) to all of \(f_i^{6,z},f_i^{7,z}\) and \(f_i^{8,z}\), and so on. The lists look as follows:

\(f_i^{1,z}:f_i^{2,z}v_i^zf_i^{3,z}f_i^{4,z}f_i^{5,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}\)<br>
\(f_i^{2,z}:v_i^zf_i^{1,z}f_i^{3,z}f_i^{4,z}f_i^{5,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}\)<br>
and<br>
\(f_i^{3,z}:f_i^{4,z}f_i^{5,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}v_i^zf_i^{1,z}f_i^{2,z}\)<br>
\(f_i^{4,z}:f_i^{5,z}f_i^{3,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}v_i^zf_i^{1,z}f_i^{2,z}\)<br>
\(f_i^{5,z}:f_i^{3,z}f_i^{4,z}f_i^{6,z}f_i^{7,z}f_i^{8,z}v_i^zf_i^{1,z}f_i^{2,z}\)<br>
and<br>
\(f_i^{6,z}:f_i^{7,z}f_i^{8,z}v_i^zf_i^{1,z}f_i^{2,z}f_i^{3,z}f_i^{4,z}f_i^{5,z}\)<br>
\(f_i^{7,z}:f_i^{8,z}f_i^{6,z}v_i^zf_i^{1,z}f_i^{2,z}f_i^{3,z}f_i^{4,z}f_i^{5,z}\)<br>
\(f_i^{8,z}:f_i^{6,z}f_i^{7,z}v_i^zf_i^{1,z}f_i^{2,z}f_i^{3,z}f_i^{4,z}f_i^{5,z}\)

A visual example of the forcing gadget (without edge labels) is shown in Figure 5. This concludes the construction of the variable and forcing gadgets.

Finally, for each clause \(C_j=(C_j^1\vee C_j^2\vee C_j^3)\in C\), we construct a **clause gadget** _G<sub>C<sub>j</sub></sub>_ consisting of the three agents \(x_j^1,x_j^2,x_j^3\), respectively. These agents are connected to variable gadgets, but we do not consider these occurrences of variable gadgets to be part of the clause gadget (in contrast to the forcing gadgets being part of the variable gadgets). The preferences are constructed as follows:

\(x_j^1:x_j^2x_j^3v(x_j^1)\)<br>
\(x_j^2:x_j^3x_j^1v(x_j^2)\)<br>
\(x_j^3:x_j^1x_j^2v(x_j^3)\)

where \(v(x_j^s)\) will be specified below. This concludes the construction of the clause gadgets. The clause gadget construction is illustrated in Figure 6.

Now we link up the variable and clause gadgets as follows: for each unnegated literal \(C_j^d=V_i\), let \(v(x_j^d)=v_i^T\) and let \(x_1(v_i^T)=x_j^d\) if this is the first occurrence of this literal or \(x_2(v_i^T)=x_j^d\) if this is the second occurrence of this literal. Similarly, for each negated literal \(C_j^d=\bar{V}_i\), let \(v(x_j^d)=v_i^F\) and let \(x_1(v_i^F)=x_j^d\) if this is the first occurrence of this literal or \(x_2(v_i^F)=x_j^d\) if this is the second occurrence of this literal. Recall that by definition of (2,2)-e3-sat, there are<tbc>

P vz
i
2,z
1,z
fi
fi
8,z
3,z
fi
7,z
fi
4,z
fi
6,z
fi
fi

Figure 5: Illustration of the forcing gadget construction (edge labels omitted for clarity)

