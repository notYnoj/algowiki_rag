(5.45), it follows that _u<sub>xx</sub>(x,y,t_) and _u<sub>yy</sub>(x,y,t_) are bounded above. Therefore, by WMT, _u<sub>xx</sub>(x,y,t_) and _u<sub>yy</sub>(x,y,t_) are indeed continuous functions.

In a similar manner, we can show the continuity of \(_G\mathcal{D}_t^{(\varrho)}u(x,y,t)\).

• Uniqueness of second-ISP

**Theorem 5.4** _A regular solution to second-ISP is uniquely determined under the assumptions of Theorem 5.3._

**Proof:** The uniqueness of _w(t_) has been previously established by means of the Banach fixed-point theorem. Now, we prove the uniqueness of _u(x,y,t_). Define

\(\overline{u}(x,y,t)=u(x,y,t)-v(x,y,t),\overline{w}(t)=w_1(t)-w_2(t).\)

Then, the function <o>_u_</o>(_x,y,t_) satisfies the following equation

\(_G\mathcal{D}_t^{(\varrho)}\overline{u}(x,y,t)=\overline{u_{xx}}(x,y,t)+\overline{u_{yy}}(x,y,t),(x,y,t)\in\Omega,\)

alongside the following boundary conditions

\(\overline{u}(0,y,t)=0,\overline{u_x}(1,y,t)-d\big(\overline{u_{xx}}(1,y,t)+\overline{u_{yy}}(1,y,t)\big)=0,\)<br>
\(y\in[0,1],t\in[0,T],d=const>0,\)<br>
\(\overline{u}(x,0,t)=0,\overline{u_y}(x,1,t)=0,x\in[0,1],t\in[0,T],\)

and the initial condition

\(\overline{u}(x,y,0)=0,y\in[0,1],x\in[0,1].\) (5.65)

Consider the further function

\(\overline{U_{j,k}}(t)=\int_0^1\int_0^1_{(1)}\overline{u}(x,y,t)X_{j,k}(x,y)dxdy.\) (5.66)

Applying \(_G\mathcal{D}_t^{(\varrho)}\) to both sides of Eq. (5.50), we have

\(_G\mathcal{D}_t^{(\varrho)}\overline{U_{j,k}}(t)=_G\mathcal{D}_t^{(\varrho)}\int_0^1\int_0^1_{(1)}\overline{u}(x,y,t)X_{j,k}(x,y)dxdy.\)

Due to Eq. (5.5), we obtain

\(\overline{U_{j,k}}(t)=\overline{U_{j,k}}(0)\mathbf{W}_{j,k}(t)+\overline{w}(t)f_{j,k}(t)*\mathbf{V}_{j,k}(t).\)

By applying the initial conditions (5.65), taking into account the uniqueness of <o>_w_</o>(_t_) and the completeness of _Y<sub>j,k</sub>(x,y_), we infer

\(\overline{U_{j,k}}(t)=0.\)

As a consequence, we deduce

\(u(x,y,t)=v(x,y,t).\)

