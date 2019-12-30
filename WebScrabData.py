from bs4 import BeautifulSoup
import requests 
from PIL import Image
from io import BytesIO
import urllib
import pandas as pd
import numpy as np
import sys
import time
import os
def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata
data = pd.read_excel('Suppliers.xlsx', sheet_name="Sheet2")
#trane = data['Trane'][:349]
#data = data['York'][:312]
i = 1

header = data.columns

# Create directory
for dirName in header:
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
        data = pd.read_excel('Suppliers.xlsx', sheet_name="Sheet2")
        data = data[dirName]
        data = data.dropna()
        start_time = time.time()
        for item in data:
            try:
                soup = make_soup(item)
                for img in soup.findAll('img'):
                    temp = img.get('src')
                    print(temp)
                    filename = temp.split('/')[-1]
                    if filename.split('.')[-1]=='jpeg':
                        
                        print(filename)
                        #outFileName = os.path.join('./', filename)
                        imagefile = open(filename , 'wb')
                        imagefile.write(urllib.request.urlopen(temp).read())
                        imagefile.close()
                        print("Loop break")
                    else:
                        print("Image not found", filename)
            except:
                print("Proper URL Not found")
            print("End of URL's", i)
            print("###############################################################################")
            i = i + 1
        total_time = start_time - time.time()
        minutes = total_time / 60
        print(f"it tooks {minutes} minutes")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")
sys.exit()

