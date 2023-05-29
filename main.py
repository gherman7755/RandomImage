import os, subprocess
import random
from PIL import Image
import time

def getRandomPhoto(files, path):
    choice = random.choice(files)
    if choice != "Completed" and choice != "bmp" and choice != "main.py" and choice != ".gitignore":
        imagePath = path + "\\" + choice
    return imagePath, choice


def dangerousClose(path):
    
    files = os.listdir(path)

    for _ in range(100):
        imagePath, choice = getRandomPhoto(files, path)

        im = Image.open(imagePath)
        im.load()   

        im.show()
        answer = input("Enter Answer: ")
        
        if answer in choice:
            print(f"Yes it is {choice}")
        else:
            print(f"It is: {choice}")
        

        time.sleep(1)
        subprocess.run(['taskkill', '/f', '/im', "PhotosApp.exe"])
            
            
def saverClose(path):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    
    files = os.listdir(path)
    
    for _ in range(100):
        imagePath, choice = getRandomPhoto(files, path)
        
        f = Image.open(imagePath)

        bmp = choice.replace("png", "bmp")

        bmp = '.\\bmp\\' + bmp
        
        f.save(bmp)
        
        time.sleep(4)
        
        plt.imshow(f)
        plt.ion() # Ion
        plt.show()
        
        answer = input("Enter Answer: ")
            
        if answer.capitalize() in choice:
            print(f"Yes it is {choice}")
        else:
            print(f"It is: {choice}")
        
        print("-"*20)
        plt.close()


if __name__ == "__main__":
    
    # Dangerous Close - closing image by killing PhotoApp.exe proccess
    # dangerousClose("C:\\Users\\Legion\\Downloads\\patterns")
    # Saver Close - closing image using matplotlib, creates bmps files
    saverClose("C:\\Users\\Magpie\\Desktop\\patterns")