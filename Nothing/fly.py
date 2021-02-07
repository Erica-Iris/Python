from PIL import Image
import pylab
img = Image.open('a.png')
img = img.convert('L')
fig,ax = pylab.subplots()
ax.contour(img,origin='image',level=[100])
pylab.show()