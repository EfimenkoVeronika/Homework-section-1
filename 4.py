from PIL import Image

class FileNotFoundException(Exception):
    ...


im = Image.open("pictures/boy.jpg")

print(im.format, im.size, im.mode)

choose = input("Что сделать с картинкой: применить эффект(1) или сохранить(2)")

if choose == '1':
    choose2 = input("Выберите эффект: черно-белое изображение(1), отражение по горизонтальной оси(2)")

    if choose2 == '1':
        for x in range(im.size[0]):
            for y in range(im.size[1]):
                pix = im.getpixel((x, y))
                avg = (pix[0] + pix[1] + pix[2]) //3
                im.putpixel((x, y), (avg, avg, avg))

    elif choose2 == '2':
        width, height = im.size
        horizontal_flip = Image.new(im.mode, (width, height))

        for x in range(width):
            for y in range(height):
                pix = im.getpixel((x, y))
                horizontal_flip.putpixel((x, height - 1 - y), pix)

        im = horizontal_flip


if choose == '2':
    while True:
        try:
            filename = input("Введите имя файла для сохранения:")

            if not 'boy.jpg' in filename:
               raise FileNotFoundException ("Некорректное имя файла, введите еще раз:")

            im.save(filename)
            print(f'Изображение сохранено как {filename}')
            break


        except FileNotFoundException as err:
           print(f'Не сработало! {err}')

im.show()




