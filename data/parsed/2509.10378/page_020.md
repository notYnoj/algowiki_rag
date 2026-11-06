<tbc>loss scale. These small differences among models are further diminished when applying the trained models in the PCG solve process. Therefore, given the negligible sensitivity to hyperparameter choice, we adopt the settings listed above for all experiments.

## B Impact of the number of random vectors

To ensure that the training process remains matrix-free, we rely on projections of the linear operators onto random vectors, as described in Section 3. The number of such vectors, denoted by _K_, influences both the training dynamics and the resulting model performance. Using _K_=128 as the baseline, we experiment with _K_=16,32,64,128,256 to train the model (\(\mathcal{N}_{L8}^\text{FCN}\)) and evaluate its performance on the validation set. For fair comparison, the validation loss is consistently computed with _K_=128 across all experiments, and the training terminates when hitting the same early stopping criterion. Using the same early stopping criterion, Figure 10 shows the offset validation loss from these models. The curves show that increasing the number of random vectors leads to lower validation loss, despite the minuscule difference (relative to the absolute loss values). Since using more random vectors slows down the training, with the minimal performance difference, we use a intermediate value _K_=128 for training.

FNO
FCN
35
train loss val loss
30
train loss val loss
30
25
22
Loss
20
18
16
15
14
0
200
400
600
800
1000
1200
1400
1600
0
500
1000
1500
2000
2500
Epoch
Epoch
(a)
FNO
L=16
(b)
FNO
L=16

256
7
4
0.327
swish
102
0.0109
13.79
223
9
127
7
0.0408
swish
13.81
200
5.5
3.25
0.246
79.8
0.00822
13.78
168
7
99.2
5.5
0.0307
softplus
13.8
softplus
144
4
2.5
0.164
57.5
0.00848
13.77
Validation Loss
112
5
71.5
4
0.0205
signoid
relu
13.77
88
2.5
1.75
0.0818
35.2
0.00275
13.76
57.2
3
43.8
2.5
0.0103
relu
13.76
32
1
0
prelu
13
1.26e-05
2
16
0:000113
prelu
batch size
model
n-block
activation
batch size
hidden channel
hidden channel
activation
batch size
kernel size
n-layers
activation
(a)
FNO
L16
(b)
FNO
L16

Fig. 8. Training dynamics of the FNO and FCN for _L_=16 cases. Both models converge smoothly, and the validation losses closely track the training losses.

Fig. 9. Parallel-coordinate plots of hyperparameters for the proposed \(\mathcal{N}_{L16}^\text{FNO}\) and \(\mathcal{N}_{L16}^\text{FCN}\) models. Using validation loss as the objective, darker blue lines indicate trials with lower validation loss.

