from ImageOptions import *
from makeFilters import *
from xyPoints import *
from numpy import polyfit, polyval


def load_picture() -> Image:
    file = choose_file()
    image = load_image(file)

    new_image = copy(image)
    show(new_image)

    return new_image


def statement() -> str:
    print("\nL)oad image S)ave-as \n3)-tone X)treme contrast T)int sepia P)osterize \nE)dge detect D)raw curve V)ertical flip H)orizontal flip \nQ)uit")
    word = input("\nPlease enter your command: ")
    word = word.upper()
    return word


imagesuccess = False
userinterface = True
while userinterface == True:
    word = statement()
    if word == 'L':
        new_image = load_picture()
        imagesuccess = True
    elif imagesuccess == False:
        print('No image loaded')
    elif word == '3':
        col_lst = ['black', 'white', 'red', 'lime', 'blue', 'yellow', 'cyan', 'magenta', 'grey']
        print("Here are your colours: black, white, red, lime, blue, yellow, cyan, magenta, grey")
        cc1 = str(input("Choose your first colour: "))
        while cc1 not in col_lst:
            cc1 = str(input("Illegal input, please choose your first colour again: "))
        cc2 = str(input("Choose your second colour: "))
        while cc2 not in col_lst:
            cc2 = str(input("Illegal input, please choose your second colour again: "))
        cc3 = str(input("Choose your third colour: "))
        while cc3 not in col_lst:
            cc3 = str(input("Illegal input, please choose your third colour again: "))
        new_image = three_tone(new_image, cc1, cc2, cc3)
        show(new_image)
    elif word == 'X':
        new_image = extreme_contrast(new_image)
        show(new_image)
    elif word == 'T':
        new_image = sepia(new_image)
        show(new_image)
    elif word == 'P':
        new_image = posterize(new_image)
        show(new_image)
    elif word == 'E':
        threshold = int(input("Please enter your threshold: "))
        new_image = detect_edges(new_image, threshold)
        show(new_image)
    elif word == 'D':
        new_image, borders = draw_curve(new_image, "cyan", [(145, 28), (189, 70), (4, 20)])
        show(new_image)
    elif word == 'V':
        new_image = vertical_flip(new_image)
        show(new_image)
    elif word == 'H':
        new_image = flip_horizontal(new_image)
        show(new_image)
    elif word == 'S':
        save_as(new_image)
    elif word == 'Q':
        print("Thank you for using our application, have a nice day!")
        userinterface = False

    else:
        print('No such command')
