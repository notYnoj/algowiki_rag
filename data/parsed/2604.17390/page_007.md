<tbc>Masking the image, both at initialization and at each training step in either of the two training procedures, plays a crucial role in preserving color and structural information during the learning phase. In Figure 3, the mask is shown on the initial input, which is particularly important for maintaining contrast, luminance and<tbc>

AvgPool 3
Conv4_1
Conv4_2
Conv5_1
Conv5_2
Conv3_1
Conv4_3
Conv5_3
Conv3_3
Conv4_4
Conv5_4
Conv3_4
Conv2_1
Conv2_2
G4 Input
G5 Input
G3 Input
G2 Input
L2 Min
L3 Min
L4 Min
L5 Min
MSD
MSD
MSD
MSD
Input inscription
Conv1_1
G2 input - G2 Exemplar1
G2 input - G2 Exemplar1
G2 input - G2 Exemplar2
G2 input - G2 Exemplar2
G2 input - G2 Exemplar2
G2 input - G2 Exemplar2
G2 input - G2 Exemplar2
Mask of damaged part
G1 input - G1 Exemplar1
G2 input - G2 ExemplarN
G2 input - G2 ExemplarN
G2 input - G2 ExemplarN
G2 input - G2 ExemplarN
G1 input - G2 ExemplarN
G1 input - G1 ExemplarN
G1 Exemplar1
G2 Exemplar1
G4 Exemplar1
G3 Exemplar1
G5 Exemplar1
AvgPool 3
Conv4_1
Conv4_2
Conv5_1
Conv5_2
Conv3_1
Conv4_3
Conv4_4
Conv5_3
Conv5_4
Conv2_1
Conv3_3
Conv4_4
Conv5_4
Conv2_2
Conv1_1
Conv1_2
G1 ExemplarN
G2 ExemplarN
G5 ExemplarN
G3 ExemplarN
Conv4_1
Conv5_1
Conv5_2
Conv3_1
Conv4_3
Conv5_3
Conv3_4
Conv5_4
Conv3_3
Conv3_4
Conv2_2
Conv1_1
Conv1_2
Exemplar N inscription
Conv1_1

Fig. 3. Restoring Ancient Inscriptions: _G_ denotes the Gram matrix of feature maps in layer _l_, depending on the number of filters _F<sub>l</sub>_. The network structure is based on VGG19 [18], using AvgPooling instead of MaxPooling layers. Networks generated with PlotNeuralNet (https://github.com/Harislqbal88/PlotNeuralNet) and then modified.

