from PIL import Image

projuct = Image.open('E:\\PT-Plugin-Plus-UserData (3).png','r')

box1=(0,0,650,2403)
box2=(0,2403,650,4806)
region=projuct.crop(box1)
region.save("e:\\part1.png")
region=projuct.crop(box2)
region.save("e:\\part2.png")
