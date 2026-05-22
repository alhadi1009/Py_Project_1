
import sys
import time
from fpdf import FPDF
import cowsay
import datetime
import re

def PDF_Generate(Name,Course,Signeture):
    pdf=FPDF(orientation="L",unit="mm",format="A4")
    pdf.add_page()

    try:

        pdf.image("Certificate_image.png",0,0,297,210)
        pdf.set_xy(83, 70)
        pdf.set_font("Courier",style="B",size=20)

        pdf.cell(100, 30, "This is to certify that", align='R')   

       
        pdf.set_y(92)
        pdf.add_font("Allura", "BI", "Font/Allura-Regular.ttf", uni=True)
        pdf.set_font("Allura", style="BI", size=50)
        pdf.set_text_color(171, 148, 112)
        #pdf.set_text_color(212, 175, 55)
        width=pdf.get_string_width(Name)+6
        pdf.set_x((297-width)/2)
        pdf.cell(width,10,Name,align='C',fill=False)
        #explanation Portion
        text="has successfully completed"
        width=pdf.get_string_width(text)+6
       
        pdf.ln()
        pdf.ln()
        pdf.set_x((297-width)/3)
        pdf.set_text_color(0,0,0)
        pdf.set_font("Courier",style="",size=20)
        pdf.cell(175,10,"has successfully completed",align='C')
        #Course Portion
        
       # Course="Introduction to Python"
        pdf.set_y(92)
        pdf.add_font("GreatVibes", "", "Font/GreatVibes-Regular.ttf", uni=True)
        pdf.set_font("GreatVibes", style="", size=50)
        pdf.set_text_color(255,0,0)
        #pdf.set_text_color(212, 175, 55)
        width=pdf.get_string_width(Course)+6
        pdf.set_y(-80)
        pdf.set_x((297-width)/2)
        pdf.cell(width,10,Course,align='C',fill=False)
        #Time add portion 
        pdf.set_font("helvetica",style="B",size=20)
        pdf.set_text_color(128,128,128)
        pdf.set_xy(55,-50)
        Time="Date : "+str(datetime.date.today())
        pdf.cell(width,10,Time,align='L',fill=False)
        #signeture portion
       
        pdf.add_font("DancingScript", "", "Font/DancingScript-Regular.ttf", uni=True)
        pdf.set_font("DancingScript", size=20)
        pdf.set_text_color(0,0,0)
        pdf.set_xy(200, -50)
        pdf.cell(40, 10, Signeture, align='L')
        #Last Signeture portion
       
        pdf.set_xy(200,-45)
        pdf.set_font("helvetica",style="",size=12)

        pdf.cell(40,10,"_"*19,align='L')
        #Text portion
        pdf.set_font("helvetica",style="",size=12)
      
        pdf.set_xy(200,-40)
        pdf.cell(40,10,"Signeture of Author",align='L')

    except:
        print("Invalid Image path") 
    for i in range(10, 110, 10):
        sys.stdout.write(f"\rPDF Generating {i}%")
        sys.stdout.flush()
        time.sleep(0.3)       
    pdf.output("Certificate.pdf")
# Section One(1) Done