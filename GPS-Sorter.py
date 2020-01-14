from GPSPhoto import gpsphoto
import PIL
import tkinter as tk
from tkinter import filedialog
import shutil
import os
from PIL import Image
import re


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilenames()
print(len(file_path))
for i in range(len(file_path)):
    print(file_path[i])
    # Fetch GPS data
    Param=gpsphoto.getGPSData(file_path[i])
    # Fetch timestamp data
    Timestamp=Image.open(file_path[i])._getexif()[36867]
    # Split timestamp into year,month,day,etc
    YearTaken=re.split(':| ',Timestamp)[0]
    MonthTaken=re.split(':| ',Timestamp)[1]
    DayTaken=re.split(':| ',Timestamp)[2]
    HourTaken=re.split(':| ',Timestamp)[3]
    MinuteTaken=re.split(':| ',Timestamp)[4]
    SecondTaken=re.split(':| ',Timestamp)[5]
    # Print parameters
    Param["Altitude"]=Param["Altitude"]
    print(Param["Latitude"])
    print(Param["Longitude"])
    print(Param["Altitude"])
    # Start sloppy sorting code
    # Check if within geofence 1
    if Param["Latitude"]>27.73405420977165 and Param["Latitude"]<27.735851790228352 and Param["Longitude"]>-82.18232332511806 and Param["Longitude"]<-82.18029267488194:
        # Dump in folder1
        shutil.move(file_path[i], 'Folder1/'+MonthTaken+'_'+DayTaken+'_'+YearTaken+' '+HourTaken+'_'+MinuteTaken+'_'+SecondTaken+'.jpg')
    # Check if within geofence 2
    elif Param["Latitude"]>27.735601209771648 and Param["Latitude"]<27.73739879022835 and Param["Longitude"]>-82.19561533951676 and Param["Longitude"]<-82.19358466048322:
        # Dump in folder2
        shutil.move(file_path[i], 'Folder2/'+MonthTaken+'_'+DayTaken+'_'+YearTaken+' '+HourTaken+'_'+MinuteTaken+'_'+SecondTaken+'.jpg')
    else:
        # Dump into folder if not within geofences
        print("No Directory")
        shutil.move(file_path[i], 'Unknown/'+MonthTaken+'_'+DayTaken+'_'+YearTaken+' '+HourTaken+'_'+MinuteTaken+'_'+SecondTaken+'.jpg')
