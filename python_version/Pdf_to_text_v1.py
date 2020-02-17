#!/usr/bin/env python
# coding: utf-8

# In[ ]:



get_ipython().system('pip install pytesseract')
# !sudo apt-get install tesseract-ocr
# !pip install wand
# !pip install wand==0.4.5
# !pip install pyocr

# !pip install pillow


# In[ ]:


# !pip install PIL


# In[ ]:


# !pip install pdf2image


# In[ ]:


# !pip install pypdf


# In[ ]:


# !pip install pypdf2


# In[ ]:


# !pip install textract


# In[ ]:


# !pip install pdftotext


# In[1]:


from PIL import Image 
# import pyPdf
import PyPDF2
import textract
# import pdftotext
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import pytesseract
import argparse
import os


# In[2]:


from PIL import Image 
import pytesseract 
import sys 
from pdf2image import convert_from_path 
import os 


# In[ ]:


get_ipython().system('pip install ocrmypdf')


# In[3]:


# Read the files from your destination location
PDF_file = "scannen_rudis_uitgaand24142611_20_2018.pdf" 
PDF_file


# In[ ]:


pdfReader = PyPDF2.PdfFileReader("scannen_rudis_uitgaand24142611_20_2018.pdf", "rb")


# In[ ]:


num_pages = pdfReader.numPages
count = 0
text = ""
#The while loop will read each page
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(fileurl, method='tesseract')
#, language='eng')
 


# In[ ]:


#text


# In[4]:


pages = convert_from_path(PDF_file, 100)


# In[5]:


image_counter = 1
  
# Iterate through all the pages stored above 
for page in pages: 
  
    # Declaring filename for each page of PDF as JPG 
    # For each page, filename will be: 
    # PDF page 1 -> page_1.jpg 
    # PDF page 2 -> page_2.jpg 
    # PDF page 3 -> page_3.jpg 
    # .... 
    # PDF page n -> page_n.jpg 
    filename = "page_"+str(image_counter)+".jpg"
      
    # Save the image of the page in system 
    page.save(filename, 'JPEG') 
  
    # Increment the counter to update filename 
    image_counter = image_counter + 1
  


# In[ ]:


get_ipython().system('pip install tesseract ')


# In[6]:



''' 
Part #2 - Recognizing text from the images using OCR 
'''
    #3
# Variable to get count of total number of pages 
filelimit = image_counter-1
  
# Creating a text file to write the output 
outfile = "out_text.txt"
  
# Open the file in append mode so that  
# All contents of all images are added to the same file 
f = open(outfile, "a") 
  
# Iterate from 1 to total number of pages 
for i in range(1, filelimit + 1): 
  
    # Set filename to recognize text from 
    # Again, these files will be: 
    # page_1.jpg 
    # page_2.jpg 
    # .... 
    # page_n.jpg 
    filename = "page_"+str(i)+".jpg"
          
    # Recognize the text as string in image using pytesserct 
    text = str((pytesseract.image_to_string(Image.open(filename)))) 
  
    # The recognized text is stored in variable text 
    # Any string processing may be applied on text 
    # Here, basic formatting has been done: 
    # In many PDFs, at line ending, if a word can't 
    # be written fully, a 'hyphen' is added. 
    # The rest of the word is written in the next line 
    # Eg: This is a sample text this word here GeeksF- 
    # orGeeks is half on first line, remaining on next. 
    # To remove this, we replace every '-\n' to ''. 
   #text = text.replace('-\n', '')     
  
    # Finally, write the processed text to the file. 
    f.write(text) 
  
#Close the file after writing all the text. 
f.close() 

