**Algorithm 1** TRM4CO: one recursion step, inference with depth _D_ and width _K_, and training. Problem-specific hooks are listed in  4, and the rest is shared between MIS and TSP.

Require: core \(f_\theta\), head \(g_\theta\), prefix tokens _p_, initial states _y_<sub>0</sub>_,z_<sub>0</sub><br>
Require: hooks Emb, Dec, c, Solved, and wrapper W of  4<br>
procedure STEP(y,z,e,A) \(\triangleright\) Eq. (1), with Eq. (2) inside \(f_\theta\)<br>
   for i=1,...,H do \(\triangleright\) cycles 1...H-1 without gradient<br>
   for l=1,...,L do<br>
   \(z\leftarrow f_\theta(z+y+e;A)\)<br>
   end for<br>
   \(y\leftarrow f_\theta(z+y;A)\)<br>
   end for<br>
   return y,z<br>
end procedure

procedure SOLVE(x; D,K,\(\sigma\)) \(\triangleright\) inference; x may be a batch of instances<br>
   \(e\leftarrow[p;\mathrm{Emb}(x)]\)<br>
   \(A\leftarrow\) adjacency of x (MIS) or 0 (TSP)<br>
   \((y^{(j)},z^{(j)})\leftarrow(y_0,z_0)\) for j=1,...,K<br>
   \(s^\star\leftarrow\) none<br>
   for t=1,...,D do \(\triangleright\) depth<br>
   for j=1,...,K in one batched forward pass do \(\triangleright\) width<br>
   \(z^{(j)}\leftarrow z^{(j)}+\sigma\xi\) with \(\xi\sim\mathcal{N}(0,I)\)<br>
   \((y^{(j)},z^{(j)})\leftarrow\mathrm{STEP}(y^{(j)},z^{(j)},e,A)\)<br>
   \(s\leftarrow\mathrm{Dec}(g_\theta(y^{(j)}),x)\)<br>
   if s<sup>⋆</sup> is none or c(s) improves on c(s<sup>⋆</sup>) then<br>
   \(s^\star\leftarrow s\)<br>
   end if<br>
   end for<br>
   end for<br>
   return s<sup>⋆</sup><br>
end procedure

procedure TRAIN(\(\{(x_i,\ell_i)\}\); D,T) \(\triangleright\) deep supervision with problem-specific halting<br>
   fill B batch slots with augmented instances, each with e, A, (y<sub>0</sub>,z<sub>0</sub>), and t=0<br>
   loop<br>
   \((y,z)\leftarrow\mathrm{STEP}(y,z,e,A)\) on all slots<br>
   \(t\leftarrow t+1\)<br>
   \(\mathcal{L}\leftarrow\mathrm{CE}(g_\theta(y),\ell)\)<br>
   update \(\theta\) with \(\nabla_\theta\mathcal{L}\)<br>
   detach (y,z)<br>
   for each slot with \(\mathrm{Solved}(g_\theta(y),\ell,x)\) or t=D do<br>
   refill the slot with a new augmented instance<br>
   end for<br>
   if T epochs have passed since the last relabel pass then<br>
   \(\ell_i\leftarrow\) the better of \(\ell_i\) and W(x<sub>i</sub>) for all \(i\triangleright\) self-relabel<br>
   end if<br>
   end loop<br>
end procedure

for selection. As in TRM, a random minimum step count is imposed on a small fraction of training instances so that later steps keep receiving a gradient. The loss is the stablemax cross-entropy of Jolicoeur-Martineau (2025). Body weights are trained with Muon (Jordan et al., 2024), heads and biases with AdamW, and prefix tokens with sign-SGD. An exponential moving average of the weights is maintained. Training uses _D_=16 for TSP and 32 for MIS, _P_=16 prefix tokens, _H_=3 cycles of _L_=6 latent updates, and a 12-step random-walk positional encoding for MIS ( 5). The TSP solved check compares predicted successors with the canonical (counterclockwise) label because decoding a tour would cost _n_ sequential steps per training step. The 2-opt repair may be<tbc>

