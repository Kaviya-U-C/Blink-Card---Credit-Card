#!/usr/bin/env python
# coding: utf-8

# In[12]:


import easyocr
import cv2






def easyocr_input(imagepath):
    image = cv2.imread(imagepath)
    gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray_img,(200,200), interpolation = cv2.INTER_AREA)
    clahe=cv2.createCLAHE(clipLimit=1,tileGridSize=(12,8))
    clahe_img=clahe.apply(resized)
    reader=easyocr.Reader(['en'])
    obj=reader.readtext(clahe_img,detail=0,decoder='beamsearch',
                    allowlist='0123456789',text_threshold=0.65,link_threshold=0.01,mag_ratio=1.6)
    max_len = -1
    for x in obj:
        if len(x) > max_len:
            max_len = len(x)
            cno = x
    #cno = cno[0:4]+" "+cno[4:8]+" "+cno[8:12]+" "+cno[12:16]
    return cno
   







