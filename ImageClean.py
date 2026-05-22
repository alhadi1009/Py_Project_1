import os
def ImgClean(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        
    else:
        print("Done!")
