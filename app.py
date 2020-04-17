# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 19:52:41 2020

@author: KIIT
"""
import numpy 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

model = load_model('a95e25model.h5')
model.summary()


test_image=image.load_img('sample/u1.png',target_size=(50,50,3))
imgplot = plt.imshow(test_image)
plt.show()
test_image=image.img_to_array(test_image)
test_image=numpy.expand_dims(test_image,axis=0)
result = model.predict(test_image)
cell="Parsitized" if result[0][1]==1 else "Uninfected"
print(cell)
