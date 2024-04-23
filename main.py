from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p', unit='mm', format='a4')
# loading csv in a pandas data frame
df = pd.read_csv('topics.csv')
# print(df) to make sure data got loaded correctly
for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    # border= 'B' does the same thing
    pdf.cell(w=0, h=24, txt=row['Topic'], align='L', ln=1)
    # this is a painful way of adding a line you just have more control of line placement
    pdf.line(10, 28, 200, 28)



# leave blank till output is made
# just learning about the FPDF
# pdf.add_page()
# pdf.set_font(family='Times', size=12)
# pdf.cell(w=0, h=12, txt="Hello", align='L', ln=1, border=1)
# pdf.set_font(family='Times', style='B', size=12)
# pdf.cell(w=0, h=12, txt="hi there", align='L', ln=1, border=1)

pdf.output("output.pdf")