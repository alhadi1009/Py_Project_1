from PIL import Image,ImageOps
from QRGenerator import Partial
def ImageResize(value):
    path = Partial()  
    path=path[value][6]

    try:

        with Image.open(path) as im:
            im = ImageOps.contain(im, (100, 100))
            im.save(f"resize{value}.png")
    except :
        print("hi")        
  


def main():
    ImageResize(0)
   
if __name__=="__main__":
    main()