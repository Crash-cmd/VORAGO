import os
from customtkinter import *
from PIL import Image, ImageTk  # Ensure ImageTk is imported
import json
import login1 ,login_2

with open('credits.json','r') as f:
    credit = json.load(f)

if  login_2.login_procces == True:
    print('YOU ARE HERE')
    app_window = CTk()
    app_window.geometry("1000x1000")
    app_window.mainloop()