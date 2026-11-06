### C.4 Matrix export and PDF generation

The following function exports the matrix to CSV and generates a PDF containing only the matrix. No graph gallery or graph images are generated.

### C.5 Input examples

The general framework is instantiated for _n_=5 and _n_=6 by changing only the input value of _n_. The following example generates the corresponding graph family, embedding matrix, matrix PDF, and _K_<sub>_n_-1</sub>-minor checks.

for n in [5, 6]: G, labels, aut = connected\_graphs(n)

Listing 1.4: Export and PDF generation for the embedding matrix.

import csv from reportlab.pdfgen import canvas from reportlab.lib.pagesizes import letter def export\_matrix(A, filename="matrix.csv"): with open(filename, "w", newline="") as f: writer = csv.writer(f) try: writer.writeows(A.rows()) except AttributeError: writer.writeows(A) def save\_matrix\_pdf(A, labels, filename): c = canvas.Canvas(filename, pagesize=letter) pw, ph = letter c.setFont("Courier", 6) x0 = 30 y = ph - 40 row\_h = 10 header = " " + " ".join( f"{label:\>5}" for label in labels ) c.drawString(x0, y, header) y -= 20 for i, row in enumerate(A): line = ( f"{labels[i]:\<5}" + " ".join(f"{x:5d}" for x in row) ) c.drawString(x0, y, line) y -= row\_h if y \< 40: c.showPage() c.setFont("Courier", 6) y = ph - 40 c.save()

Listing 1.5: Example inputs for the five- and six-vertex cases.

