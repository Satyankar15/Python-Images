# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 15:05:53 2020

@author: satya
"""

from PIL import Image
img=Image.open("C:\\Users\satya\Desktop\deadcells.jpg")
savepath="Experiment.jpg"
img.save(savepath)
print("Saved")
img=Image.open(savepath)
img=img.rotate(90)
img.save(savepath)