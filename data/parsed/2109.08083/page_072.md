\(\mathbb{E}'(\Delta E_{v,S}^-(i))\ge-\frac{3(|E_\mathcal{T}(v,S)|p^3-e_{E_{v,S}}+b^{1/3}|E_\mathcal{T}(v,S)|)(np^3+e_d-1)}{n^2p^4+e_q}\)<br>
\(+\frac{12|E_\mathcal{T}(v,S)|p^2}{|V(0)|}+O\left(\frac{|E_{\mathcal{T}(v,S)}|p}{|V(0)|^2}\right).\)<br>
\(\mathbb{E}'(\Delta V_S^+(i))\le-\frac{(|S|p+e_{V_S}-b^{1/3}|S|)(np^3-e_d)}{n^2p^4+e_q}+\frac{4|S|}{|V(0)|},\)<br>
\(\mathbb{E}'(\Delta V_S^-(i))\ge-\frac{(|S|p-e_{V_S}+b^{1/3}|S|)(np^3+e_d)}{n^2p^4+e_q}+\frac{4|S|}{|V(0)|},\)<br>
\(\mathbb{E}'(\Delta Z_\mathcal{A}^+(i))\le-\frac{12(|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}+e_{Z_\mathcal{A}}-b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|)(np^3-e_d)}{n^2p^4+e_q}\)<br>
\(+\frac{48|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{11}}{|V(0)|}+O\left(\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}}{n^2p^4}+\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{10}}{|V(0)|^2}\right),\)<br>
\(\mathbb{E}'(\Delta Z_\mathcal{A}^-(i))\le-\frac{12(|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}-e_{Z_\mathcal{A}}+b^{1/3}|Z_\mathcal{A}(\mathcal{T}^{-A^*})|)(np^3+e_d)}{n^2p^4+e_q}\)<br>
\(+\frac{48|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{11}}{|V(0)|}+O\left(\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{12}}{n^2p^4}+\frac{|Z_\mathcal{A}(\mathcal{T}^{-A^*})|p^{10}}{|V(0)|^2}\right),\)

Now, starting by chasing the details for \(V_S^+(i)\) we see that

\(\mathbb{E}'(\Delta V_S^+(i))\le-\frac{(|S|p+b^{1/3}|S|)(np^3-e_d)}{n^2p^4}+\frac{|S|}{n}+O\left(\frac{b|S|}{n}+\frac{e_q|S|np^4}{Q(i)^2}\right)\)<br>
\(\le-\frac{b^{1/3}|S|}{np}+\frac{e_d|S|}{n^2p^3}+O\left(\frac{b|S|}{n}+\frac{e_q|S|np^4}{Q(i)^2}+\frac{b^{1/3}|S|e_d}{n^2p^4}\right)\)

Then since we have \(p\gg b^{1/3}\mathrm{log}(n)\) and \(-\frac{b^{1/3}|S|}{np}+\frac{e_d|S|}{n^2p^3}=\Theta\left(\frac{b^{1/3}|S|}{np}\right)\le 0\), and the ‘big-O’ terms are all \(o\left(\frac{b^{1/3}|S|}{np}\right)\), we have that \(\mathbb{E}'(\Delta V_S^+(i))\le 0\), as required.

Via very similar calculations we end up deducing that

\(\mathbb{E}'(\Delta V_S^-(i))\ge\frac{b^{1/3}|S|}{np}-\frac{e_d|S|}{n^2p^3}+O\left(\frac{b|S|}{n}+\frac{e_q|S|np^4}{Q(i)^2}+\frac{b^{1/3}|S|e_d}{n^2p^4}\right)\)

and so obtain immediately also that \(\mathbb{E}'(\Delta V_S^-(i))\ge 0\).

For \(E_{v,S}^+(i)\) we find that

\(\mathbb{E}'(\Delta E_{v,S}^+(i))\le-\frac{3\big(|E_\mathcal{T}(v,S)|p^3+b^{1/3}|E_\mathcal{T}(v,S)|\big)\big(np^3-e_d\big)}{n^2p^4}+\frac{3|E_\mathcal{T}(v,S)|p^2}{n}\)<br>
\(+O\left(\frac{|E_{\mathcal{T}(v,S)}|p}{|V(0)|^2}+\frac{e_q|E_\mathcal{T}(v,S)|np^6}{Q(i)^2}+\frac{b|E_\mathcal{T}(v,S)|p^2}{n}+\frac{|E_\mathcal{T}(v,S)|}{Q(i)^2}\right)\)<br>
\(\le-\frac{3b^{1/3}|E_\mathcal{T}(v,S)|}{np}+\frac{3e_d|E_\mathcal{T}(v,S)|}{n^2p}\)<br>
\(+O\left(\frac{|E_{\mathcal{T}(v,S)}|p}{n^2}+\frac{e_q|E_\mathcal{T}(v,S)|}{n^3p^2}+\frac{b|E_\mathcal{T}(v,S)|p^2}{n}+\frac{|E_\mathcal{T}(v,S)|}{n^2p^4}+\frac{e_db^{1/3}|E_\mathcal{T}(v,S)|}{n^2p^4}\right)\)

