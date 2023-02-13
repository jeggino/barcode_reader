# Importing library
import streamlit as st
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="Barcode_reader",
    page_icon="💀",
    layout="wide",
    
)

# ---FUNCTION---
# Make one method to decode the barcode
def BarcodeReader(image):

    # read the image in numpy array using cv2
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    # Decode the barcode image
    detectedBarcodes = decode(cv2_img)

    # If not detected then print the message
    if not detectedBarcodes:
        return st.write("Barcode Not Detected or your barcode is blank/corrupted!")
        
    else:
    
        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
    
            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(cv2_img, (x-10, y-10),
                        (x + w+10, y + h+10),
                        (255, 0, 0), 2)
            
            if barcode.data!="":

            # Print the barcode data
#                 st.write(f"the bar code is {barcode.data}")
                return f"{barcode.data}"




kind = st.radio('What kind of product',('Cd', 'Book'))
title = st.text_input('Movie title', 'insert a title here ...')
genre = st.multiselect("Genre?", ('Comedy', 'Drama', 'Documentary'))    
picture = st.camera_input("Take a picture")

if picture:
    df_dict = {"Kind":kind,"Title":title,"Genre":genre,"Barcode":BarcodeReader(picture)}
    df = pd.DataFrame(df_dict)
    st.dataframe(df)
    
   
    

