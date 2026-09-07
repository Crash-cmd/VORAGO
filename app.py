import os
from customtkinter import *
from PIL import Image, ImageTk  # Ensure ImageTk is imported
import json
#import login1 ,login_2

# with open('credits.json','r') as f:
#     credit = json.load(f)

def l_d():
    if l_dswitch.get() ==1 :
        l_dswitch.configure(text="Switch to Dark Mode",button_color = "black",button_hover_color="black")

    elif l_dswitch.get()==0:
        l_dswitch.configure(text="Switch to Light Mode",button_color = "white",button_hover_color="white")

app_window = CTk()
app_window.geometry("1980x1020")

#Side Pannel-------------------------------------------
side_pannel =  CTkFrame(app_window)
side_pannel.configure(fg_color = "#2a2b2a",width=100,border_color = "#424242",border_width = 5,corner_radius=20)




logo_img = Image.open("images/logo.png")
math_d = Image.open("images/maths_dark.png")
math_l = Image.open("images/math_light.png")
phy_d = Image.open("images/phy_dark.png")
phy_l = Image.open("images/phy_light.png")
chem_d= Image.open("images/chem_dark.png")
chem_l = Image.open("images/chem_light.png")



logo = CTkLabel(side_pannel,image=CTkImage(logo_img,size=(60,60)),text="",width=60,height=60)
logo.grid(column=0,row=0)
icon = Image.open("images/icon.png")
user_account = CTkButton(side_pannel,image=CTkImage(icon,size=(40,40)),text="",width=80,height=80,border_color="white",border_width=2,corner_radius=20,fg_color="black",bg_color="transparent")
user_account.grid(column=0,row=1)
math = CTkButton(side_pannel,image=CTkImage(light_image=math_d,dark_image=math_l,size=(40,40)),width=80,height=80,text="",border_color="white",border_width=2,corner_radius=20,fg_color="black",bg_color="transparent")
math.grid(column=0,row=2)
phy = CTkButton(side_pannel,image=CTkImage(light_image=phy_d,dark_image=phy_l,size=(40,40)),text="",width=80,height=80,border_color="white",border_width=2,corner_radius=20,fg_color="black",bg_color="transparent")
phy.grid(column=0,row=3)
logo4 = CTkButton(side_pannel,image=CTkImage(light_image=chem_d,dark_image=chem_l,size=(40,40)),text="",width=80,height=80,border_color="white",border_width=2,corner_radius=20,fg_color="black",bg_color="transparent")
logo4.grid(column=0,row=4)
logo5= CTkButton(side_pannel,image=CTkImage(logo_img,size=(40,40)),text="",width=70,height=70,border_color="white",border_width=2,corner_radius=20,fg_color="black",bg_color="transparent")
logo5.grid(column=0,row=5)

side_pannel.grid_propagate(False) 
side_pannel.columnconfigure(0,weight=1)
side_pannel.rowconfigure(0,weight=1)
side_pannel.rowconfigure(1,weight=1)
side_pannel.rowconfigure(2,weight=1)
side_pannel.rowconfigure(3,weight=1)
side_pannel.rowconfigure(4,weight=1)
side_pannel.rowconfigure(5,weight=1)
side_pannel.grid(column=0,row=0,sticky="ns")


spacer = CTkFrame(app_window)
spacer.configure(fg_color = "transparent",width=20)
spacer.grid(column=1,row =0,sticky="ns")

#-------------------------------------------------------------------------------

#Main frame display ------------------------------------
main_frame = CTkFrame(app_window)

l_dswitch = CTkSwitch(main_frame,text="Switch to Light Mode",command=l_d,fg_color="black",progress_color="white")
l_dswitch.grid(row =0 ,column =0)


main_frame.configure(fg_color = "#2a2b2a",border_color = "#424242",border_width = 5,corner_radius=50)
main_frame.rowconfigure(0,weight=1)
main_frame.columnconfigure(0,weight=1)
main_frame.grid(column=2,row =0,sticky="nswe")
#--------------------------------------------------------
app_window.columnconfigure(2,weight = 2)
app_window.rowconfigure(0,weight =2)
app_window.configure(fg_color ="black")
app_window.mainloop()