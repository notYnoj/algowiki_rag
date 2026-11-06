<tbc>index sets. Consider \(\bar{u}\in I^\perp\) and \(\bar{v}\in I^\top\) for some \((I^\perp,I^\top)\in\{I_\ell^\perp,I_s^\perp,I_r^\perp\}\times\{I_\ell^\top,I_s^\top,I_r^\top\}\). In order to calculate \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})\), we perform a case distinction on \(I^\perp\) and \(I^\top\).

If \(I^\perp=I_s^\perp\) and \(I^\top=I_\ell^\top\), or \(I^\perp=I_r^\perp\) and \(I^\top\in\{I_\ell^\top,I_s^\top\}\), \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})=-\infty\), as \(\bar{v}\) is not reachable from \(\bar{u}\).

If \(I^\perp=I_\ell^\perp,I^\top=I_\ell^\top\), then we can get \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})\) from the output of the \((\mathrm{w},\mathbf{F}_\ell,\mathbf{F}')\)-BBD instance.

If \(I^\perp=I_s^\perp,I^\top=I_s^\top\), then we can get \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})\) from the output of the \((\mathrm{w},\mathbf{F}_s,\mathbf{F}')\)-BBD instance.

If \(I^\perp=I_r^\perp,I^\top=I_r^\top\), then we can get \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{u},\bar{v})\) from the output of the \((\mathrm{w},\mathbf{F}_r,\mathbf{F}')\)-BBD instance.

If \(I^\perp=I_\ell^\perp,I^\top=I_s^\top\), observe that for any \(i\in[1..(n^\prime+1)]\left\{\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{w})+\mathrm{dist}_\tilde{\mathbf{G}}(\bar{w},\bar{u})\right\}\).<br>
Similarly to Lemma 4.6, we can rewrite the computation of \(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{u})\) for all such \(\bar{u}\) and \(\bar{v}\) using a max-plus product. This time, we use the output of the \((\mathrm{w},\mathbf{F}_\ell,\mathbf{F}')\)-BBD instance and the output of the \((\mathrm{w},\mathbf{F}_s,\mathbf{F}')\)-BBD instance to compute the entries of the matrices since \(\tilde{\mathbf{G}}[1..i_s][1..(n'+1)]=\tilde{\mathbf{G}}_\ell\) and \(\tilde{\mathbf{G}}[i_s..i_r][1..(n'+1)]=\tilde{\mathbf{G}}_s\).<br>
If the diameter is at most D, we note that following similar arguments as Lemma 4.6, the matrix multiplication requires time O(T<sub>MonMUL</sub>(_m,m,m,_D)).

If \(I^\perp=I_s^\perp,I^\top=I_r^\top\), observe that for \(i\in[i_s..i_r]\), we have \(\pi_\mathbf{F}(i)\le i_r\) because **F**_<sub>s</sub>_ is a synchronous subforest of _s_. Hence, a path in \(\tilde{\mathbf{G}}\) that goes from \(\bar{u}\) to \(\bar{v}\) must pass through a node in \(i_r\times[1..n'+1]\), and we can write<tbc>

\(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{u})=\mathrm{max}_{\bar{w}\in i_r\times[1..n^\prime+1]}\left\{\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{w})+\mathrm{dist}_\tilde{\mathbf{G}}(\bar{w},\bar{u})\right\}.\)

<tbc>Similarly to the previous case, these computations can be performed using a max-plus product, where entries are take from the output of the \((\mathrm{w},\mathbf{F}_s,\mathbf{F}')\)-BBD instance and the output of the \((\mathrm{w},\mathbf{F}_r,\mathbf{F}')\)-BBD instance.<br>
As above, if the diameter is at most D, the matrix multiplication requires time O(T<sub>MonMUL</sub>(_m,m,m,_D)).<br>
If \(I^\perp=I_\ell^\perp,I^\top=I_r^\top\), we use again that either \(\pi_\mathbf{F}(i)\le i_s\) or \(\pi_\mathbf{F}(i)\ge i_r>i_s+n_s\) for \(i\in[1..i_s]\), and that \(\mathbf{F}(i)\le i_r\) for \(i\in[i_s..i_r]\). Consequently, any path from \(\bar{u}\) to \(\bar{v}\) either stays entirely in \(\tilde{\mathbf{G}}_{\backslash s}\), or passes through a node in \(i_s\times[1..(n'+1)]\) and a node in \(i_r\times[1..(n'+1)]\). Therefore, we obtain<tbc>

\(\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{u})=\mathrm{max}\big\{\mathrm{dist}_{\tilde{\mathbf{G}}_{\backslash s}}(\bar{v},\bar{u}),\mathrm{max}_{\bar{w}\in i_s\times[1..(n'+1)]\bar{z}\in i_r\times[1..(n'+1)]}\big\{\mathrm{dist}_\tilde{\mathbf{G}}(\bar{v},\bar{w})+\mathrm{dist}_\tilde{\mathbf{G}}(\bar{w},\bar{z})+\mathrm{dist}_\tilde{\mathbf{G}}(\bar{z},\bar{u})\big\}\big\}.\)

<tbc>These computation can be done by taking the maximum between outputs of the \((\mathrm{w},\mathbf{F}_{\backslash s},\mathbf{F}')\)-BBD instance, and a max-plus product between three matrices. The entries of these matrices can be retrieved from outputs of the other three FED instance at our disposal.<br>
As above, if the diameter is at most D, the matrix multiplication requires time O(T<sub>MonMUL</sub>(_m,m,m,_D)).<br>
This concludes the proof of Lemma 4.7.

## 4.5 Computing spine mapping similarities

In this (sub)section we prove a lemma that will turn out to be useful in a special case appearing in Section 5. We prove it here, since in order to solve it we need to solve a BBD instance, similar to the \((\mathrm{w},\mathbf{F}_{\backslash s},\mathbf{F}')\)-BBD instance appearing in Lemma 4.7.

