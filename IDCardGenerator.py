from fpdf import FPDF
from datetime import date
from ImageResize import ImageResize
from QRGenerator import Partial


class PDF(FPDF):

    def __init__(self):
        super().__init__(format=(50, 85))
        self.set_auto_page_break(auto=False)

    def fit_text(self, text, font="Courier", style="B", size=16, limit=46):

        self.set_font(font, style=style, size=size)

        width = self.get_string_width(text)

        while width > limit and size > 4:
            size -= 1
            self.set_font(font, style=style, size=size)
            width = self.get_string_width(text)

        return width

    def center_text(self, y, h, text):

        width = self.get_string_width(text)
        x = (50 - width) / 2

        self.set_xy(x, y)
        self.cell(width, h, text)

    def FirstPage(self, value):

        self.add_page()

        # Background
        self.image('IDimg1.png', 0, 0, 50, 85)

        # User image
        ImageResize(value)
        try:
            self.image(f'resize{value}.png', 10, 10, 30, 30)

        except:
            self.image(f'default.png', 10, 10, 30, 30)

       

        # Border
        self.set_draw_color(128, 128, 128)
        self.set_line_width(.5)

        self.rect(10, 10, 30, 30)

        Text = Partial()

        # ================= NAME =================
        text = Text[value][0]

        self.set_text_color(0, 0, 0)

        self.fit_text(text, size=16)

        self.center_text(40, 6, text)

        # ================= DESIGNATION =================
        text = Text[value][1]

        self.fit_text(text, style="", size=11)

        self.center_text(43.7, 5, text)

        # ================= ID =================
        text = "ID :" + Text[value][2]

        self.fit_text(text, size=9)

        self.center_text(50, 5, text)

        # ================= LINE =================
        self.set_xy(10, 52)

        self.cell(30, 3, '-' * 18, align='C')

        # ================= VALID DATE =================
        now = date.today()

        future = now.replace(year=now.year + 7)

        text = "Valid Till :" + str(future)

        self.fit_text(text, size=10, limit=35)

        self.center_text(51, 10, text)
        # add QR code
        try:
            self.image(f'MyImage{value}.png', 20, 60, 10, 10)

        except:
            self.image(f'default.png', 20, 60, 10, 10)
        
        self.set_draw_color(128, 128, 128)
        self.set_line_width(.5)

        self.rect(20, 60, 10, 10)

        #logo set
        
        self.image('Logo.png', 1,1, 5, 5)
        # institute name
        company="Mawlana Bhashani Science and Technology University"
        self.set_xy(6,4)
        
        self.fit_text(company,size=16,limit=28)
       
        self.cell(0, 0, company)
        



    def SecondPage(self,value):

        self.add_page()

        self.image('IDimg2.png', 0, 0, 50, 85)
        text=" 1. This card is not Transferable.\n 2. If found ,Please return to Institute.\n 3. Misuse of this card is Panishable offence.\n 4. Card must be carried at all time."
        self.set_xy(10,20)
        self.set_font("Helvetica",style="",size=5)
        self.set_text_color(255,0,0)
        self.multi_cell(40,5,text) 
        #Names
        self.set_xy(25,-23)
        Text = Partial()
        Text=Text[value][0].split(' ')
        self.set_text_color(0,0,0)
        self.add_font("GreatVibes", "", "Font/GreatVibes-Regular.ttf", uni=True)

        self.set_font("GreatVibes", size=5)
        self.cell(0,0,Text[0])



#names
        self.set_xy(25,-22)
        sign="-"*23
        self.set_text_color(0,0,0)
        self.fit_text(sign,style="",limit=20)
        self.cell(0,0,sign)

        self.set_xy(25,-21)
        sign="Signeture"
        self.set_text_color(0,0,0)
        self.fit_text(sign,style="",limit=8)
        self.cell(0,0,sign)
       
       


def main():

    pdf = PDF()

    pdf.FirstPage(0)

    pdf.SecondPage(0)

    pdf.output("hi.pdf")


if __name__ == "__main__":
    main()