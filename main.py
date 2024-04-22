from fpdf import FPDF

pdf  = FPDF(orientation='p', unit='mm', format='a4')

pdf.add_page()
# leave blank till output is made

pdf.set_font(family='Times', size=12)
pdf.cell(w=0, h=12, txt="Hello", align='L', ln=1, border=1)
pdf.set_font(family='Times', style='B', size=12)
pdf.cell(w=0, h=12, txt="hi there", align='L', ln=1, border=1)

pdf.output("output.pdf")