<tbc>#Circuit for performing diagonal check (Fig. 1 Part II) using 6 ancillary qubits<br>
<sup>85</sup> #Evaluating f(Q1,Q2), value of which is stored in qr[19]<br>
<sup>87</sup> ccx qr[0],qr[5],qr[19];<br>
ccx qr[1],qr[4],qr[19];<br>
ccx qr[1],qr[6],qr[19];<br>
ccx qr[2],qr[5],qr[19];<br>
ccx qr[2],qr[7],qr[19];<br>
ccx qr[3],qr[6],qr[19];<br>
<sup>83</sup> #Evaluating f(Q1,Q3), value of which is stored in qr[20]<br>
<sup>95</sup> ccx qr[0],qr[10],qr[20];<br>
ccx qr[1],qr[11],qr[20];<br>
ccx qr[2],qr[8],qr[20];<br>
ccx qr[3],qr[9],qr[20];<br>
<sup>99</sup> #Evaluating f(Q1,Q4), value of which is stored in qr[21]<br>
<sup>101</sup> ccx qr[0],qr[15],qr[21];<br>
ccx qr[3],qr[12],qr[21];<br>
<sup>103</sup> #Evaluating f(Q2,Q3), value of which is stored in qr[22]<br>
<sup>105</sup> ccx qr[4],qr[9],qr[22];<br>
ccx qr[5],qr[8],qr[22];<br>
ccx qr[5],qr[10],qr[22];<br>
ccx qr[6],qr[9],qr[22];<br>
ccx qr[6],qr[11],qr[22];<br>
ccx qr[7],qr[10],qr[22];<br>
<sup>111</sup> #Evaluating f(Q2,Q4), value of which is stored in qr[23]<br>
<sup>113</sup> ccx qr[4],qr[14],qr[23];<br>
ccx qr[5],qr[15],qr[23];<br>
ccx qr[6],qr[12],qr[23];<br>
ccx qr[7],qr[13],qr[23];<br>
<sup>114</sup> #Evaluating f(Q3,Q4), value of which is stored in qr[24]<br>
<sup>115</sup> ccx qr[8],qr[13],qr[24];<br>
ccx qr[9],qr[12],qr[24];<br>
ccx qr[9],qr[14],qr[24];<br>
ccx qr[10],qr[13],qr[24];<br>
ccx qr[10],qr[15],qr[24];<br>
ccx qr[11],qr[14],qr[24];<br>
<sup>125</sup> #Performing measurement on all qubits<br>
<sup>127</sup> measure qr[0] -\> cr[24];<br>
measure qr[1] -\> cr[23];<br>
measure qr[2] -\> cr[22];<br>
measure qr[3] -\> cr[21];<br>
measure qr[4] -\> cr[20];<br>
measure qr[5] -\> cr[19];<br>
measure qr[6] -\> cr[18];<br>
measure qr[7] -\> cr[17];<br>
measure qr[8] -\> cr[16];<br>
measure qr[9] -\> cr[15];<br>
measure qr[10] -\> cr[14];<br>
measure qr[11] -\> cr[13];<br>
measure qr[12] -\> cr[12];<br>
measure qr[13] -\> cr[11];<br>
measure qr[14] -\> cr[10];<br>
measure qr[15] -\> cr[9];<br>
measure qr[16] -\> cr[8];<br>
measure qr[17] -\> cr[7];<br>
measure qr[18] -\> cr[6];<br>
measure qr[19] -\> cr[5];<br>
measure qr[20] -\> cr[4];<br>
measure qr[21] -\> cr[3];<br>
measure qr[22] -\> cr[2];<br>
measure qr[23] -\> cr[1];<br>
measure qr[24] -\> cr[0];<tbc>

