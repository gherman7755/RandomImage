import os, subprocess
import random
from PIL import Image
import time

import configparser


config = configparser.ConfigParser()
config.read('config.ini')

COMPONENTS_PATH = config['DIRs']['COMPONENTS_PATH']
BLANK_PATH = config['DIRs']['BLANK_PATH']

forbiddenNames = [
    'Completed',
    'Components',
    'bmp',
    'main.py',
    '.gitignore',
    '.git',
    '.idea',
    'components.json',
    'config.ini',
]


BMP_PATH = __file__.replace("main.py", "bmp")
if not os.path.exists(BMP_PATH):
    os.makedirs(BMP_PATH)


def outputAnswer(choice):
    answer = input("Enter Answer: ")

    if answer.capitalize() in choice:
        print(f"Yes, it is {choice}")
    else:
        print(f"No, it is: {choice}")

    print("-" * 20)


def getRandomPhoto(files, path):
    choice = random.choice(files)

    count = 0

    while choice in forbiddenNames:
        choice = random.choice(files)
        count += 1
        if count == 100:
            print('Cannot find needed files')
            return None, None

    imagePath = path + "\\" + choice
    return imagePath, choice


def dangerousClose(path):
    files = os.listdir(path)

    for _ in range(100):
        imagePath, choice = getRandomPhoto(files, path)

        im = Image.open(imagePath)
        im.load()

        im.show()

        outputAnswer(choice)

        time.sleep(1)

        # Check if "PhotosApp.exe" is running
        proc = subprocess.run(['tasklist', '/fi', 'IMAGENAME eq PhotosApp.exe'], capture_output=True)
        if proc.stdout and b'PhotosApp.exe' in proc.stdout:
            subprocess.run(['taskkill', '/f', '/im', 'PhotosApp.exe'])

        # Check if "Microsoft.Photos.exe" is running
        proc = subprocess.run(['tasklist', '/fi', 'IMAGENAME eq Microsoft.Photos.exe'], capture_output=True)
        if proc.stdout and b'Microsoft.Photos.exe' in proc.stdout:
            subprocess.run(['taskkill', '/f', '/im', 'Microsoft.Photos.exe'])


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

        time.sleep(2)

        plt.imshow(f)
        plt.ion()  # Ion
        plt.show()

        outputAnswer(choice)

        plt.close()


def componentsAnswers(pattern, pattern_name):
    answer = input("Pattern name: ")

    if answer.capitalize() in pattern_name:
        print(f"Yes, it is {pattern_name}")
    else:
        print(f"No, it is: {pattern_name}")

    print("-" * 20)

    for variant, component in pattern.items():
        answer = input(f"What is {variant}? ")

        if answer.capitalize() in component:
            print(f"Yes, it is {component}")
        else:
            print(f"No, it is: {component}")

        print("-" * 20)


def components(path):
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
    import json

    files = os.listdir(path)

    file = open(path + '\\components.json')
    json_components = json.load(file)

    for _ in range(100):
        imagePath, choice = getRandomPhoto(files, path)

        f = Image.open(imagePath)

        bmp = choice.replace("png", "bmp")
        bmp = '.\\bmp\\' + bmp

        f.save(bmp)

        time.sleep(2)

        plt.imshow(f)
        plt.ion()  # Ion
        plt.show()

        componentsAnswers(json_components[choice], choice)

        plt.close()


if __name__ == "__main__":
    # Dangerous Close - closing image by killing PhotoApp.exe proccess
    # dangerousClose("C:\\Users\\Nick-V-PC\\Documents\\GitHub\\RandomImage\\Blank")

    # Saver Close - closing image using matplotlib, creates bmps files

    mode = int(input('Enter mode:\n'
                 '1. Pattern name\n'
                 '2. + Components\' names\n'))

    if mode == 1:
        saverClose(BLANK_PATH)

    if mode == 2:
        components(COMPONENTS_PATH)

