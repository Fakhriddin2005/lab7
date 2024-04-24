# def t1():
#  from PIL import Image
#  a = "starwars.jpg"
#  with Image.open(a) as img:
#   img.load()
#   img.show()
#   w, h = img.size
#   format = img.format
#   mode = img.mode
#   print('Ширина: ',w)
#   print('Высота: ',h)
#   print('Формат: ', format)
#   print('Цвет: ',mode)
# t1()

# def t2():
#  from PIL import Image
#  b="starwars.jpg"
#  with Image.open(b) as img:
#   img.load()
#
#   img2 = img.resize((img.width //3, img.height //3))
#   img2.save('starwars_resize.jpg')
#
#   img3 = img2.rotate(90)
#   img3.save("starwars_rot.jpg")
#
#   img4 = img.transpose(img2.FLIP_LEFT_RIGHT)
#   img4.save("starwar_mir.jpg")
# t2()

def t3():
 from PIL import Image, ImageFilter
 for i in range(1, 6):
        i = str(i)
        img = Image.open(i + '.jpg')
        img = img.filter(ImageFilter.EMBOSS)
        # img.save("D:\питон\pics\img" + i + ".jpg")
 t3()
