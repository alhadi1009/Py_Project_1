import re
import csv
def FILE_Generate():
        

    while(True):
        Name=input("What's your Name: ").strip()
        name=r"^[A-Za-z. _-]+$"
        if re.match(name,Name):
           
            break
        
        
    while(True):
        Job=input("What's you Job title :").strip()
        job=r"^[A-Za-z _ -]+$"
        if re.match(job,Job):
            break
        
    
    while(True):
        ID=input("What's your ID :").strip()
        id=r"^[A-Za-z0-9-_ ]+$"
        if re.match(id,ID):
            break
        
    
    while(True):
        Mobile=input("Give your Mobile number :").strip()
        mobile=r"^(01[3-9][0-9]{8}|\+8801[3-9][0-9]{8})$"
        if re.match(mobile,Mobile):
            break
        
    
    while(True):
        Email=input("Give your E-mail :").strip()
        email=r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"  
        if re.match(email,Email):
            break  
        
  
    while(True):
        Address=input("Give your address: ").strip()  
        address=r"[A-Za-z0-9, ./_-]+$"
        if re.match(address,Address):
            Address=Address.replace(',','_')
            break  
          
    
    while (True):
        ImagePath = input("Give your image path: ").strip()

        imagepath = r"^[A-Za-z0-9_\-./:\\ ]+\.(jpg|jpeg|png)$"

        if re.match(imagepath, ImagePath):
            break
       
  

    with open("storeData.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([Name, Job, ID, Mobile, Email, Address, ImagePath])
def main():
    FILE_Generate()
if __name__=="__main__":
    main()    

