# Automatic Number Plate Recognition (ANPR)

This is a YOLOv4-tiny model that detects License Plates and extracts the text using Easy OCR deployed onto a Flask App locally.

# Working

The YOLOv4-tiny model is trained on about 1200 images for 6100 Epochs with only 1 class named "license".

After detecting the License Plate, the image is cropped and stored locally in the name "crop4.jpg". Then OCR is run on the cropped image.

First, the OCR text is filtered to just contain Alphabets and Numbers.

Then the OCR Text is then put through a regex validation pattern that checks if it follows an Indian License Pattern or not. 

If the pattern matches, the License Plate is pushed to an SQLite DataBase.

# Features

The application allows the user to run inference on a video and store the valid plates captured into the DataBase.

The user can view all the Licence Plates stored in the database.
