<tbc>h qr[15];<br>
15<br>
#To initialize the ancillas required for diagonal checks in |1\> state<br>
17 x qr[19];<br>
x qr[20];<br>
19 x qr[21];<br>
x qr[22];<br>
21 x qr[23];<br>
x qr[24];<br>
22 x qr[0];<br>
x qr[3];<br>
23 x qr[4];<br>
25 x qr[7];<br>
27 x qr[8];<br>
x qr[11];<br>
29 x qr[12];<br>
x qr[15];<br>
31<br>
#Preparing each of the 4 blocks in the 4-qubit W-state<br>
33 ccx qr[0],qr[3],qr[1];<br>
ccx qr[4],qr[7],qr[5];<br>
35 ccx qr[8],qr[11],qr[9];<br>
ccx qr[12],qr[15],qr[13];<br>
37 x qr[0];<br>
39 x qr[3];<br>
x qr[4];<br>
41 x qr[7];<br>
x qr[8];<br>
43 x qr[11];<br>
x qr[12];<br>
45 x qr[15];<br>
47 ccx qr[0],qr[3],qr[2];<br>
ccx qr[4],qr[7],qr[6];<br>
49 ccx qr[8],qr[11],qr[10];<br>
ccx qr[12],qr[15],qr[14];<br>
51 cx qr[2],qr[0];<br>
53 cx qr[2],qr[3];<br>
cx qr[6],qr[4];<br>
55 cx qr[6],qr[7];<br>
cx qr[10],qr[8];<br>
57 cx qr[10],qr[11];<br>
cx qr[14],qr[12];<br>
59 cx qr[14],qr[15];<br>
61<br>
#Circuit for performing column check (Fig. 1 Part I) using 3 ancillary qubits<br>
63 h qr[16];<br>
h qr[17];<br>
65 h qr[18];<br>
67 cu1(3.14159265358979) qr[16],qr[0];<br>
cul(3.14159265358979) qr[16],qr[4];<br>
cul(3.14159265358979) qr[16],qr[8];<br>
69 cu1(3.14159265358979) qr[16],qr[12];<br>
71 cu1(3.14159265358979) qr[17],qr[1];<br>
cul(3.14159265358979) qr[17],qr[5];<br>
73 cu1(3.14159265358979) qr[17],qr[9];<br>
cul(3.14159265358979) qr[17],qr[13];<br>
75 cu1(3.14159265358979) qr[18],qr[2];<br>
cul(3.14159265358979) qr[18],qr[6];<br>
77 cu1(3.14159265358979) qr[18],qr[10];<br>
cul(3.14159265358979) qr[18],qr[14];<br>
79 h qr[16];<br>
81 h qr[17];<br>
h qr[18];<tbc>

