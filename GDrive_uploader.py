'''
Python Gdrive uploader using pydrive
It will upload all files in a "Dir_Path" folder
'''
import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

Dir_Path = r"C:\Users\Admin\Desktop\Test"

for x in os.listdir(Dir_Path): 
   
    f = drive.CreateFile({'title': x}) 
    f.SetContentFile(os.path.join(Dir_Path, x)) 
    f.Upload() 
