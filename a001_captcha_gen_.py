# -*- coding: utf-8 -*-
### Generate sample captcha image

#Use ImageCaptcha
#ImageCaptcha default width=160, height=60, font and fontsize aldo can be chaged.
#To imitate real image, set (width, height, stringlength, fontsize) = (68,35,4, 20)
#Generator is easy but not similar to real captcha image, used for pre-train model


from captcha.image import ImageCaptcha
import matplotlib.pyplot as plt
import string
import random
import numpy as np
import cv2

def generate(width,height,num_char):
    characters = string.digits + string.ascii_lowercase    #ascii_letters = ascii_lowercase + ascii_uppercase
    rand_str = ''.join(random.sample(characters,num_char))
    generator = ImageCaptcha(width=width, height=height, font_sizes = [20]) #default font sizes is for (160,60), too big.
    image = generator.generate_image(rand_str)
    return (image,rand_str)


# images and labels will be in saved to save_dir folder
save_dir = 'save_dir/'
labels = []
for i in range(60):
    img, char = generate(68,35,4)    #(width, height, stringlength)
    plt.imsave(save_dir+str(char)+".jpg",np.array(img))
    labels.append(char)
with open(save_dir + 'labels.txt','w') as f:
    for lb in labels:
        f.write('%s\n' % lb)
