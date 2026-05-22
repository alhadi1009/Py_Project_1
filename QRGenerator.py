import qrcode
import csv
def TxtFile(value):
    data=Partial()
    with open("student.txt",'w') as file:
        file.write(f"Name: {data[value][0]}\n")
        file.write(f"Job: {data[value][1]}\n")
        file.write(f"ID: {data[value][2]}\n")
        file.write(f"Mobile: {data[value][3]}\n")
        file.write(f"Email: {data[value][4]}\n")
        file.write(f"Address: {data[value][5]}\n")
    QR_Generate(value)    

def Partial():
    with open("storeData.csv", "r") as file:
         return list(csv.reader(file))

        
def QR_Generate(value):
    with open('student.txt', 'r')as file:
        data = file.read()
    qr = qrcode.QRCode(
        version=4,
        box_size=10,
        border=3,
        error_correction=qrcode.constants.ERROR_CORRECT_M
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='White')
    img = img.convert("RGB")
    img.save(f"MyImage{value}.png")
def main():
    TxtFile(0)
if __name__=="__main__":
    main()    
