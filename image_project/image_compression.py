import numpy
import os
from PIL import Image
im=Image.open('tree.jpg')
print('the size of the image before compressing')
s1=os.stat('tree.jpg').st_size
s11=s1/1024
print(s11,' mb')
pixelmap=im.load()
img=Image.new(im.mode,im.size)
pixelnew=img.load()
for i in range(img.size[0]):
      for j in range(img.size[1]):
              for k in range(3):
                        if(pixelmap[i,j][k] >= 1 and pixelmap[i,j][k] <= 31):
                                pixelnew[i,j]=0
                        elif(pixelmap[i,j][k]>=32 and pixelmap[i,j][k]<=63):
                                pixelnew[i,j]=10	
                        elif(pixelmap[i,j][k]>=64 and pixelmap[i,j][k]<=95):
                                pixelnew[i,j]=20
                        elif(pixelmap[i,j][k]>=96 and pixelmap[i,j][k]<=127):
                                pixelnew[i,j]=30
                        elif(pixelmap[i,j][k]>=128 and pixelmap[i,j][k]<=159):
                                pixelnew[i,j]=40
                        elif(pixelmap[i,j][k]>=160 and pixelmap[i,j][k]<=191):
                                pixelnew[i,j]=50
                        elif(pixelmap[i,j][k]>=192 and pixelmap[i,j][k]<=223):
                                pixelnew[i,j]=60
                        elif(pixelmap[i,j][k]>=224 and pixelmap[i,j][k]<=225):
                                pixelnew[i,j]=70
img.save('newimage.jpg')
j=numpy.asanyarray(Image.open('newimage.jpg'))
print('the size of the image after compressing')
s2=os.stat('newimage.jpg').st_size
s22=s2/1024
print(s22,' mb')

