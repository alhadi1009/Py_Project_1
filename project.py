import sys
import time
from fpdf import FPDF
import cowsay
import datetime
import re
from PDFGenerator import PDF_Generate
from FileGenerator import FILE_Generate
from QRGenerator import TxtFile
from IDCardGenerator import PDF
from CSVClean import clncsv
from ImageClean import ImgClean


def PDFGeneratorHelper(Name,Course,Author):
    PDF_Generate(Name,Course,Author)


def main():
    print("Welcome to the Animated Smart PDF System")
    for i in range(10, 110, 10):
        sys.stdout.write(f"\rApplication Opening {i}%")
        sys.stdout.flush()
        time.sleep(0.3)
    print("\nFeatures: ")
    print(" 1.PDF Generate\n 2.Poster\n 3.ID Card Generate \n 4.EXIT")
    
    x=1
    while (x):
        try:
            Checker = int(input("Take option (like 1/2/3/4): "))
            if Checker == 1:
                while(True):

                     Name_patern=r"[A-Za-z ]+$"
                     Name=input("You Full Name: ")
                     if  re.match(Name_patern,Name):
                         break
                while(True):
                    try:
                        Course=input("Course Name: ").strip()
                        break
                    except ValueError:
                        print("Please enter a valid name.")
                while(True):

                     Author_patern=r"[A-Za-z. ]+$"
                     Author=input("Author name: ")
                     if  re.match(Author_patern,Author):
                         break        
                     
                PDFGeneratorHelper(Name,Course,Author)
                cowsay.cow(">>> THANK YOU <<< PDF GENERATED SUCCESSFULLY")
            elif Checker == 2:
                pass
            elif Checker == 3:
                NumberOfStudent=int(input("How much Students ID's want you generate :"))
                for _ in range(NumberOfStudent):
                    print(f"Give {_+1} Student Info :")
                    FILE_Generate()
                    TxtFile(_)
                    IDCARD=PDF()
                for _ in range(NumberOfStudent):
                    IDCARD.FirstPage(_)
                    IDCARD.SecondPage(_)
                IDCARD.output("ID Card's.pdf") 
                clncsv()
                for _ in range(NumberOfStudent):
                    ImgClean(f"resize{_}.png")
                    ImgClean(f"MyImage{_}.png")
                   

                pass
            elif Checker == 4:
                cowsay.cow("Thank you, come again later")
                sys.exit(0)
            else:
                print("Invalid Input")
        except ValueError:
            print("Type Correct Value")
        x=x-1 

        
    return 0


if __name__ == "__main__":
    main()
