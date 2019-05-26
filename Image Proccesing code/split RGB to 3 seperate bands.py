import numpy as np
from PIL import Image

image=Image.open("C:\\Users\\Borealis\\Desktop\\NSCR\\crop_project\\test\\1.jpg")

#print(image.size) #size is inverted i.e columns first rows second eg: 500,250

#convert to array
li_r=list(image.getdata(band=0))
arr_r=np.array(li_r,dtype="uint8")
li_g=list(image.getdata(band=1))
arr_g=np.array(li_g,dtype="uint8")
li_b=list(image.getdata(band=2))
arr_b=np.array(li_b,dtype="uint8")

# reshape 
reshaper=arr_r.reshape(227,227) #size flipped so it reshapes correctly
reshapeb=arr_b.reshape(227,227)
reshapeg=arr_g.reshape(227,227)

imr=Image.fromarray(reshaper,mode=None) # mode I
imb=Image.fromarray(reshapeb,mode=None)
img=Image.fromarray(reshapeg,mode=None)

imr.save('R__.jpg')

img.save('_G_.jpg')

imb.save('__B.jpg')

#merge
#merged=Image.merge("RGB",(imr,img,imb))
#merged.show()

#img.save('myimg.jpeg')

#img.show()