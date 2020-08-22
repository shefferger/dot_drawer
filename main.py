from PIL import Image, ImageDraw
import os

image = Image.new("RGBA", (640, 480), (0, 0, 0, 0))


def draw(x, y, img):
    p = ImageDraw.Draw(img)
    p.ellipse((x + 319, y + 239, x + 321, y + 241), fill="black", outline=None)


def read(filename):
    global image
    if not os.path.exists(filename):
        return
    with open(filename, "r") as f:
        text = f.read().split("\n")
        for i in text:
            x, y = int(i.split(',')[0]), int(i.split(',')[1])
            print(x, y)
            draw(x, y, image)
    image.show(title="Координаты")


def openF():
    fname = input("Введите название файла (с расширением): ")
    if not os.path.exists(fname):
        print("\nТакого файла не существует!")
        openF()
    else:
        read(fname)


openF()
