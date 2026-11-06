Figure 13 shows the problem and the learned reconstruction. The training converges rapidly, reaching the noise level of the measurement within a few hundred steps in panel (f). The learned field recovers the heterogeneity of the<tbc>

(a)
(b)
true activity k/k
concentration c/cin over time
t= 1
t= 2
poison front
inert streak
0.0
0.5
1.0
1.5
2.0
k/k
(c)
(d)
breakthrough surface
across the streak, x = 2.77W
1.0
t= 8
1.0
0.5
0.5
z/W
k/kOed
truth learned
0.0
0.0
0.0
0.5
1.0
0.0
0.5
1.0
y/W
y/W
0.0
0.5
1.0
1.0
1.2
1.4
c/cin
(e)
x/W
truth
(f)
1
2.0
0.5
10-2
rel. L2 of k
1.5
0
0.05
1.0
0
600
1200
learned
k/k
MSE
10-3
1
0.5
y/W
10-4
0
0.0
0
1
2
3
4
0
400
800
1200
x/W (flow)
optimizer step

Figure 13: Recovery of a three-dimensional catalyst activity field from noisy concentration measurements in a packed bed reactor. (a) The true activity \(k/\bar{k}\), with the breakthrough surface of the poisoning front (dashed) and the axis of the low-activity streak (solid) marked. (b) The measured concentration _c/c_<sub>in</sub> at three snapshot times. (c) The breakthrough surface _x<sub>f</sub>(y,z_) of the poisoning front, as learned (color) and in the ground truth (contours). (d) The activity across the low-activity streak, normalized by the surrounding bed, as learned (solid) against the ground truth (dashed). (e) The true and the learned activity on an axial plane through the streak. (f) Mean squared error in _c_ against optimizer step, converging to the measurement noise floor (gray dashed), with the relative _L_<sup>2</sup> error of the activity in the inset.

