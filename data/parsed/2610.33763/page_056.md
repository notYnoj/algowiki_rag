## 5.1.3 Special cases

We examine specific cases of Eq. (5.5) based on the properties of \(\varrho(t)\).

_n_**-Tempered FDE:** Assume the following power-law memory kernel

\(\varrho(t)=\sum_{\xi=1}^n\frac{P_\xi}{\Gamma(1-\beta_\xi)}e^{-pt}t^{-\beta_\xi},\)

where \(0<\beta_n<\dots<\beta_2<\beta_1<1,D_\xi>0,\xi=1,2,\dots n\), and _p\>_0 represents the truncation parameter. Applying this kernel in (5.5), we derive the corresponding _n_-tempered FDE

\(\sum_{\xi=1}^nP_\xi\mathcal{D}_t^{\beta_{\xi,p}}u(x,y,t)=u_{xx}(x,y,t)+u_{yy}(x,y,t)+F(x,y,t),\) (5.9)

where \(\mathcal{D}_t^{\beta_{\xi,p}}\) denotes the tempered fractional derivative of order \(\beta_\xi\in(0,1)\) and _p\>_0.

Now, we present few special cases of Eq. (5.9) and Eq. (5.5):

**Case-I:** Setting _p_=0 in Eq. (5.9), we obtain the following multi-term FDE

\(\sum_{\xi=1}^nP_\xi_C\mathcal{D}_t^{\beta_\xi} u(x,y,t)=u_{xx}(x,y,t)+u_{yy}(x,y,t)+F(x,y,t),\) (5.10)

where \(0<\beta_n<\dots<\beta_2<\beta_1<1,P_\xi>0,\xi=1,2,\dots n\). \(_C\mathcal{D}_t^{\beta_\xi}\) represents the CFD of order \(\beta_\xi\in(0,1)\).

**Case-II:** Take _P_<sub>1</sub>=1_,P_<sub>2</sub>=_P_<sub>3</sub>=_...=P<sub>n</sub>_=0, and _p_=0 in Eq. (5.9), the following mono-FDE is obtained

\(_C\mathcal{D}_t^{\beta_1}u(x,y,t)=u_{xx}(x,y,t)+u_{yy}(x,y,t)+F(x,y,t),\) (5.11)

where \(0<\beta_1<1\).

**Case-III:** By choosing \(\beta_1=1,P_1=1,P_2=P_3=\dots=P_n=0,\) and _p_=0 in Eq. (5.9), we derive the SDE as follows

\(u_t(x,y,t)=u_{xx}(x,y,t)+u_{yy}(x,y,t)+F(x,y,t).\) (5.12)

## 5.1.4 Mathematical formulation of the ISPs

In connection with the system (5.5)-(5.8), we explore two ISPs, defining each and addressing their solutions.

**In the first-ISP**, the source term in Eq. (5.5) depends only on spatial variables, denoted as _F(x,y,t_)=_f(x,y_). The first-ISP is to determine both _f(x,y_) and _u(x,y,t_) simultaneously for the system (5.5)-(5.8), given an additional condition

\(u(x,y,T)=g(x,y),x\in[0,1]y\in[0,1].\) (5.13)

