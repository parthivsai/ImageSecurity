# encrypted and decrypted png's will be created for your selected image in your directory.
# inputs required for encryption are path of the image,key.
# inputs required for decryption is just the key since 'encrypted.png' is already taken as input for image in decryption code.
# execute encryption and decryption chunks of code seperately.

#ENCRYPTION

import numpy as np
from PIL import Image
path = input("enter the image location")
key = int(input("enter the encryption key"))

def encrypt(xx,key):
    y=[]
    for x in xx:
        step1=key^x
        a='00000000'
        s=bin(step1)[2:]
        plain=a[:-len(s)]+s
        cipher=plain[4:]+plain[:4]
        y.append(int(cipher,2))
    return y

#read image
image=Image.open(path)

#length*width
m,n=image.size[1],image.size[0]

#converting image into list of pixel arrays
inmatrix=list(np.array(image))

endata=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(encrypt(inmatrix[i][j],key))
    endata.append(row)

#creating image from manuplated pixel array 
enimg=Image.fromarray(np.array(endata,dtype=np.uint8))
enimg.save('encryptedimage.png')



#DECRYPTION

import numpy as np
from PIL import Image
import cv2
key = int(input("enter the decryption key"))

def decrypt(xx,key):
    y=[]
    for x in xx:
        a='00000000'
        b=bin(x)[2:]
        b=a[:-len(b)]+b
        b=b[4:]+b[:4]
        b=int(b,2)^key
        y.append(b)
    return y
#read encrypted image
image=Image.open("encryptedimage.png")

#length*width
m,n=image.size[1],image.size[0]

#converting the image into pixel matrix
dedata=list(np.array(image))

outdata=[]
for i in range(m):
    sa=[]
    for j in range(n):
        sa.append(tuple(decrypt(dedata[i][j],key)))
    outdata.append(sa)

#creating image from pixel array
outimg=Image.fromarray(np.array(outdata,dtype=np.uint8))
outimg.save('decryptedimage.png')

