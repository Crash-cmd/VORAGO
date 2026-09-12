import os
from customtkinter import *
from PIL import Image, ImageTk  # Ensure ImageTk is imported
import json
import time
import login1 ,login_2

with open('credits.json','r') as f:
    credit = json.load(f)

def l_d():
    if l_dswitch.get() ==1 :
        l_dswitch.configure(text="Switch to Dark Mode",button_color = "black",button_hover_color="black")
        

    elif l_dswitch.get()==0:
        l_dswitch.configure(text="Switch to Light Mode",button_color = "white",button_hover_color="white")
        # set_appearance_mode("dark")

usr = 1
pas = 1


def taskbar1():
    user.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    phy.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar2():
    maths.grid(sticky = "nswe",row=0,column=0)
    user.grid_forget()
    phy.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar3():
    phy.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    user.grid_forget()
    chem.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar4():
    chem.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    phy.grid_forget()
    user.grid_forget()
    settings.grid_forget()
    home_page.grid_forget()
def taskbar5():
    settings.grid(sticky = "nswe",row=0,column=0)
    maths.grid_forget()
    phy.grid_forget()
    chem.grid_forget()
    user.grid_forget()
    home_page.grid_forget()
def ch_usrname():
    global usr
    
    user_name.configure(state="normal")

    ch_usr.configure(text="Save")
    usr *=-1
    print(z)
    if usr == 1:
        user_name.configure(state="readonly")
        credit["username"]=user_name.get()
        user_name.insert(0,credit["username"])
        ch_usr.configure(text="Change Username")
        with open('credits.json','w') as f:
            json.dump(credit,f,indent=4)

    


def ch_password():
    global pas
    password.configure(state="normal",show="")
    ch_pass.configure(text="Save")
    pas *=-1
    if pas == 1:
        password.configure(state="readonly",show="*")
        credit["password"]=password.get()
        password.insert(0,credit["password"])
        ch_pass.configure(text="Change Password")
        with open('credits.json','w') as f:
            json.dump(credit,f,indent=4)




def font_chk():
    font_tit = tit_var.get()
    l =[info_l,badge_l,font_l]
    if font_tit =="Liberation Mono":
        for liber in l:
            f_size=liber.cget("font")[1]
            liber.configure(font=("Liberation Mono",f_size))
        info_l.update()
    elif font_tit =="Arial":
        for ari in l:
            f_size=ari.cget("font")[1]
            ari.configure(font=("Arial",f_size))
        info_l.update()
    elif font_tit =="Fira Sans Condensed":
        for fsc in l:
            f_size=fsc.cget("font")[1]
            fsc.configure(font=("Fira Sans Condensed",f_size))
        info_l.update()




if login_2.login_procces== True:
    app_window = CTk()
    app_window.geometry("1980x1020")

    #Side Pannel-------------------------------------------
    side_pannel =  CTkFrame(app_window)
    side_pannel.configure(fg_color = "#2a2b2a",corner_radius=10)




    logo_img = Image.open("images/logo.png")
    math_d = Image.open("images/maths_dark.png")
    math_l = Image.open("images/math_light.png")
    phy_d = Image.open("images/phy_dark.png")
    phy_l = Image.open("images/phy_light.png")
    chem_d= Image.open("images/chem_dark.png")
    chem_l = Image.open("images/chem_light.png")
    gear_d= Image.open("images/gear_dark.png")
    gear_l = Image.open("images/gear_light.png")
    accurate = Image.open("images/badge_accuracte.png")
    placeholder_badge = Image.open("images/place_holder.png")



    logo = CTkLabel(side_pannel,image=CTkImage(logo_img,size=(50,50)),text="VORAGO",font=("Nasalization",20),compound=LEFT)
    logo.grid(column=0,row=0)
    icon = Image.open("images/icon.png")

    user_account = CTkButton(side_pannel,image=CTkImage(icon,size=(40,40)),text="",width=40,height=40,
                            hover_color="black",bg_color="transparent",fg_color="transparent",command=taskbar1)
    user_account.grid(column=1,row=0)

    math = CTkButton(side_pannel,image=CTkImage(light_image=math_d,dark_image=math_l,size=(40,40)),width=40,height=40,text="",
                        hover_color="black",bg_color="transparent",fg_color="transparent",command=taskbar2)
    math.grid(column=2,row=0)

    phy = CTkButton(side_pannel,image=CTkImage(light_image=phy_d,dark_image=phy_l,size=(40,40)),text="",width=40,height=40,
                    hover_color="black",bg_color="transparent",fg_color="transparent",command=taskbar3)
    phy.grid(column=3,row=0)


    chem = CTkButton(side_pannel,image=CTkImage(light_image=chem_d,dark_image=chem_l,size=(40,40))
                    ,text="",width=40,height=40,hover_color="black",bg_color="transparent",fg_color="transparent",command=taskbar4)


    chem.grid(column=4,row=0)


    logo5= CTkButton(side_pannel,image=CTkImage(light_image=gear_d,dark_image=gear_l,size=(40,40))
                    ,text="",width=40,height=40,hover_color="black",bg_color="transparent",fg_color="transparent",command=taskbar5)
    logo5.grid(column=5,row=0)

    side_pannel.columnconfigure(0,weight=1)
    side_pannel.columnconfigure(1,weight=1)
    side_pannel.columnconfigure(2,weight=1)
    side_pannel.columnconfigure(3,weight=1)
    side_pannel.columnconfigure(4,weight=1)
    side_pannel.columnconfigure(5,weight=1)
    side_pannel.grid(column=0,row=0,sticky="we")


    spacer = CTkFrame(app_window)
    spacer.configure(fg_color = "transparent",width = 0,height = 15)
    spacer.grid(column=0,row =1,sticky="we")

    #-------------------------------------------------------------------------------

    #Main frame display ------------------------------------
    main_frame = CTkFrame(app_window)
    
    home_page = CTkFrame(main_frame)
    home_page.rowconfigure(0,weight=1)
    home_page.columnconfigure(0,weight=1)
    home_page.rowconfigure(1,weight=1)
    logo_label = CTkLabel(home_page,text="VORAGO \n HOME",fg_color="transparent",font=("Nasalization",70),compound=BOTTOM,height=10)
    text_l =CTkLabel(home_page,text="Click the icons above to continue",fg_color="transparent",font=("Arial",70),compound=BOTTOM)
    text_l.grid(column = 0, row= 1)
    logo_label.grid(column = 0, row= 0)
    home_page.grid(sticky="nsew")

    user = CTkFrame(main_frame)
    user.configure(fg_color = "#232423")
    user.rowconfigure(0,weight=1)
    user.rowconfigure(1,weight=1)
    user.columnconfigure(0,weight=1)
    user.columnconfigure(1,weight=1)

    stats = CTkFrame(user,fg_color="transparent",border_color="#2d2e2e",border_width=2)
    stats.grid(column=0,row=0,sticky="nswe")

    tit_var = StringVar(value="Fira Sans Condensed")
    info_user = CTkScrollableFrame(user,fg_color="transparent",border_color="#2d2e2e",border_width=2)
    info_user.rowconfigure(0,weight=1)
    info_user.rowconfigure(1,weight=1)
    info_user.columnconfigure(0,weight=1)
    user_name = CTkEntry(info_user,state='normal')
    info_l =  CTkLabel(info_user, text="USER INFORMATION",font=(tit_var.get(),30),anchor="center",text_color="White")
    info_l.grid(row=0,column=0)

    user_name.insert(0,credit["username"])
    user_name.configure(state="readonly")
    ch_usr = CTkButton(info_user,text="Change Username",command=ch_usrname)
    ch_usr.grid(row=1,column=1)
    user_name.grid(column =0,row=1,sticky="we",pady=10)

    password = CTkEntry(info_user,state='normal',show="*")
    password.insert(0,credit["password"])
    password.configure(state="readonly")
    ch_pass = CTkButton(info_user,text="Change password",command=ch_password)
    ch_pass.grid(row=2,column=1)
    password.grid(column =0,row=2,sticky="we",pady=10)


    info_user.grid(column=1,row=0,sticky="nswe")

    badge = CTkFrame(user,fg_color="transparent",border_color="#2d2e2e",border_width=2)
    badge_l = CTkLabel(badge,text="BADGES",font=("Fira Sans Condensed",30))
    badge_l.grid(column=0,row=0)

    spacer_row = CTkLabel(badge,text="")
    spacer_row.grid(column=0,row=1)
    accurate_label = CTkLabel(badge,image=CTkImage(accurate,size=(80,80)),text="Accurate",compound=TOP,font=("Nasalization",20),
                              fg_color="#706e6e",corner_radius=10,border_color="#474747",border_width=2)
    accurate_label.grid(column=0,row=2)
    placeholder1 = CTkLabel(badge,image=CTkImage(placeholder_badge,size=(80,80)),text="LOCKED",compound=TOP,font=("Nasalization",20),
                              fg_color="#706e6e",corner_radius=10,border_color="#474747",border_width=2)
    placeholder1.grid(column=1,row=2)
    placeholder2 = CTkLabel(badge,image=CTkImage(placeholder_badge,size=(80,80)),text="LOCKED",compound=TOP,font=("Nasalization",20),
                              fg_color="#706e6e",corner_radius=10,border_color="#474747",border_width=2)
    placeholder2.grid(column=2,row=2)
    placeholder3 = CTkLabel(badge,image=CTkImage(placeholder_badge,size=(80,80)),text="LOCKED",compound=TOP,font=("Nasalization",20),
                              fg_color="#706e6e",corner_radius=10,border_color="#474747",border_width=2)
    placeholder3.grid(column=3,row=2)
    placeholder4 = CTkLabel(badge,image=CTkImage(placeholder_badge,size=(80,80)),text="LOCKED",compound=TOP,font=("Nasalization",20),
                              fg_color="#706e6e",corner_radius=10,border_color="#474747",border_width=2)
    placeholder4.grid(column=4,row=2)
    for i in range(0,11):
        badge.columnconfigure(i,weight=1)
    badge.grid(column=0,row=1,sticky="nswe")

    user.grid_forget()
    maths= CTkFrame(main_frame)
    label1 = CTkLabel(maths,text="TAB 1")
    label1.grid(row=0,column=0)
    maths.rowconfigure(0,weight=1)
    maths.columnconfigure(0,weight=1)
    maths.configure(fg_color = "black",border_color = "#424242",border_width = 5,corner_radius=50)
    maths.grid_forget()

    phy = CTkFrame(main_frame)
    label2 = CTkLabel(phy,text="TAB 2")
    label2.grid(row=0,column=0)
    phy.rowconfigure(0,weight=1)
    phy.columnconfigure(0,weight=1)
    phy.configure(fg_color = "black",border_color = "#424242",border_width = 5,corner_radius=50)
    phy.grid_forget()

    chem = CTkFrame(main_frame)
    label3 = CTkLabel(chem,text="TAB 3")
    label3.grid(row=0,column=0)
    chem.rowconfigure(0,weight=1)
    chem.columnconfigure(0,weight=1)
    chem.configure(fg_color = "black",border_color = "#424242",border_width = 5,corner_radius=50)
    chem.grid_forget()

    settings = CTkFrame(main_frame,fg_color="#232423")
    l_dswitch = CTkSwitch(settings,text="Switch to Light Mode",command=l_d,corner_radius=0,font=("Fira Sans Condensed",20))
    l_dswitch.grid(column=0,row=0,sticky="w")
    tit_var = StringVar(value="Fira Sans Condensed")
    con_var = StringVar(value="Fira Sans Condensed")

    font_frame = CTkFrame(settings)
    font_l = CTkLabel(font_frame,text="FONTs",font=("Fira Sans Condensed",40))
    font_l.grid(column=0,row=0,sticky="w",pady=10)
    title_font = CTkLabel(font_frame,text="Title",font=("Fira Sans Condensed",30))
    title_font.grid(column=0,row=1,sticky='w')
    Arial_f = CTkRadioButton(font_frame,variable=tit_var,value="Arial",text="Arial",font=("Arial",20),command=font_chk)
    Arial_f.grid(column = 0,row=2)
    lib_mono = CTkRadioButton(font_frame,variable=tit_var,value="Liberation Mono",text="Liberation Mono",font=("Liberation Mono",20),command=font_chk)
    lib_mono.grid(column=1,row=2)
    Fsc_f = CTkRadioButton(font_frame,variable=tit_var,value="Fira Sans Condensed",text="Fira Sans",font=("Fira Sans Condensed",20),command=font_chk)
    Fsc_f.grid(column=2,row=2,pady=5)
    
    content = CTkLabel(font_frame,text="Content",font=("Fira Sans Condensed",30))
    content.grid(column=0,row=3,sticky='w')
    Arial_f = CTkRadioButton(font_frame,variable=con_var,value="Arial",text="Arial",font=("Arial",20))
    Arial_f.grid(column = 0,row=4)
    lib_mono = CTkRadioButton(font_frame,variable=con_var,value="Liberation Mono",text="Liberation Mono",font=("Liberation Mono",20))
    lib_mono.grid(column=1,row=4)
    Fsc_f = CTkRadioButton(font_frame,variable=con_var,value="Fira Sans Condensed",text="Fira Sans",font=("Fira Sans Condensed",20))
    Fsc_f.grid(column=2,row=4)

        



    font_frame.grid(column=0,row=1,sticky="ew",pady=10)


    pan_var = IntVar(value=1)
    pannel_mode = CTkFrame(settings)
    pannel_text= CTkLabel(pannel_mode,text="Pannel Orientation",font=("Fira Sans Condensed",40))
    pannel_text.grid(column=0,row=0,sticky="w")
    pannel_normal = CTkRadioButton(pannel_mode,text="Horizontal(Default)",font=("Fira Sans Condensed",20),variable=pan_var,value=1)
    pannel_normal.grid(column=0,row=1)
    pannel_ver = CTkRadioButton(pannel_mode,text="Vertical Pannel",font=("Fira Sans Condensed",20),variable=pan_var,value=2)
    pannel_ver.grid(column=1,row=1)
    pannel_mode.grid(column = 0,row=2,sticky = "ew",pady= 10)

    settings.columnconfigure(0,weight=1)
    for k in range(4):
        settings.rowconfigure(k+1,weight=1)
        font_frame.rowconfigure(k,weight=1)
        font_frame.columnconfigure(k,weight=1)
        pannel_mode.rowconfigure(k,weight=1)
        pannel_mode.columnconfigure(k,weight=1)
    settings.grid_forget()




    main_frame.rowconfigure(0,weight=1)
    main_frame.columnconfigure(0,weight=1)
    main_frame.grid(sticky="nswe")
    #--------------------------------------------------------
    app_window.columnconfigure(0,weight = 2)
    app_window.rowconfigure(2,weight =2)
    app_window.configure(fg_color ="black")
    app_window.mainloop()