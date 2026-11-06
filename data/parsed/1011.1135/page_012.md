which is independently drawn from uniform distribution over [0,100]. The factor \(\beta\) denotes the _degree of correlation_ for students’ preferences.<sup>16</sup> The preference list _p<sub>s</sub>_ can therefore be deduced by comparing the value of \(g_s^c\) for different _c_, i.e., _s_ prefers _c_<sub>1</sub> to _c_<sub>2</sub> if \(g_s^{c_1}>g_s^{c_2}\).

The preference lists of colleges are generated as follows:

College _c_ evaluates each student _s_ by this formulae,

\(mrt_c(s)=(1-\alpha_c)\cdot f_s+\alpha_c\cdot h_c(r)\)

where _h<sub>c</sub>(r_)=110-10_r_ if _c_ is the _r_-th choice in _p<sub>s</sub>_. _f<sub>s</sub>_ is the exam score of student _s_, which is independently drawn from uniform distribution over [0,100]. We generate the reciprocating factor \(\alpha_c\) for each college _c_ by the following distribution:

\(\alpha_c=\left\{\begin{array}{ c c } 0 & prob=1/2 \\ 1 & prob=1/2 \end{array}\right.\)

The preference list _p<sub>c</sub>_ can then be inferred by comparing the value of _mrt<sub>c</sub>(s_) for different _s_. In case of ties, namely, _mrt<sub>c</sub>(s_<sub>1</sub>)=_mrt<sub>c</sub>(s_<sub>2</sub>), _s_<sub>1</sub> is favored over _s_<sub>2</sub> if _f_<sub>_s_<sub>1</sub></sub>_\>f_<sub>_s_<sub>2</sub></sub>.

## 5.2 Efficiency Results

After generating the reciprocating preference lists for both sides, the matching outcome can be obtained by applying the student-proposing DA algorithm. We then calculate the social welfare under the matching outcome.

In the simulation, we use \(\beta\in[0,1]\), with a step size of 0.01. For each particular \(\beta\), we repeat the process of preference generation for 1000 times and compute the average values of aggregate utility and social welfare. For comparison, we also calculate the average social welfare under pure GS mechanism, which can be easily implemented by just setting \(\alpha_c\equiv 0\) for each college _c_ in the distribution of reciprocating factors.<sup>17</sup>

<sup>16</sup> \(\beta\) can be also regarded as a signal implying how much information students may know about other students’ preferences. If \(\beta=1\), each student has complete information to others’ preferences since they share exactly the same opinion over colleges. If \(\beta=0\), each student has independent opinion over colleges and thus has no posterior knowledge on others’ preferences. In general, students’ individual opinion would be more or less be affected by the common social opinion and each of them would have partial knowledge to other students’ preferences. <sup>17</sup> Here in GS mechanism we let the true preferences of colleges be endogenized via students’ exam scores only, since this is how the admission authority evaluates the social welfare of DA in practice. (One such example is that schools’ welfare is measured by the average score of their admitted students in equation (1) of Chiu and Weng (2009).) Thus our simulation result can serve as a predictor for comparing the official evaluation results, if there are any, of DA and hybrid mechanism released by corresponding admission authorities. Nevertheless, if we accept that reciprocating preferences are the "true" preferences of colleges and regard submitting \(\alpha_c=0\) as certain manipulation to the true preferences, then our comparison of social welfare of DA and hybrid mechanism should have been based on the same (true) preferences of colleges. Since the latter kind of comparison is already fully covered by Property 5 theoretically, we feel that there would be no need to conduct further simulations on it (which would not produce any "surprising" results beyond theory).

