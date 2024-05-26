from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import asksaveasfilename
import pyautogui
import cv2
import numpy as np



def About_developer():
    root2 = Toplevel()
    root2.geometry("800x450",)
    root2.title("Omega Studio")
    root2.resizable(False,False)
    root2.wm_iconbitmap("3.ico") 

    label2=Label(root2,text='''Hi I am Namit Kumar an B.Tech CSE (Hons) AI And ML Undergraduate in First year. I made this project in my 12th class as I was an CS student in my 11th and 12th class and mastered python in 2 years. I hope you like my this software and please follow my GitHub and LinkedIn Profile to get more amazing softwares like this. Thank You''',font="Arial 11 bold")
    label2.pack()


def help():
    root3 = Toplevel()
    root3.geometry("880x450",)
    root3.title("Omega Studio")
    root3.resizable(False,False)
    root3.wm_iconbitmap("3.ico")

    label3=Label(root3,text="HOW TO USE : ",font="Algerian 20")
    label3.pack()

    label4=Label(root3,text='''Press start button to start recording your screen, then you will be asked for
the name and path of your file, you can choose multiple extensions
for your video. For example ( .mp4, .avi, etc ) just simply write the extention after the name of your file.
For example: [ FileName + (.mp4 or etc) ]. And
after filling the name and path you simply click on save button, then a small window will appear which
shows the live screen recording of your screen, then to stop recording press "q" on your keyboard and make
sure that you will press small "q".
    ''',font="Arial 10 bold")
    label4.pack()



def Start_Recording():
    resolution = (1920, 1080)
    codec = cv2.VideoWriter_fourcc(*"XVID")
    filename = asksaveasfilename(confirmoverwrite=False,defaultextension='.avi')

    fps=15.0
   
    out = cv2.VideoWriter(filename, codec, fps ,(resolution))
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Live", 480, 270)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow('Live', frame)
        
        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            tmsg.showinfo(title="Omega Studio",message="Your recording Saved Successfully")
            break
        
    out.release()


def Main_Studio(root):
    root = Tk()
    root.geometry("1200x675",)
    root.title("Omega Studio")
    root.resizable(False,False)
    root.wm_iconbitmap("3.ico")


    photo=PhotoImage(file="2.png",)
    label1=Label(root,image=photo,)
    label1.pack()

    img=PhotoImage(file="1.png")
    button1=Button(root,image=img,width=198,height=38,borderwidth=0,command=Start_Recording)
    button1.place(x=500,y=433)


    mymenu=Menu(root)
    m1=Menu(mymenu,tearoff=0)
    m1.add_command(label="About Developer",command=About_developer)
    m1.add_command(label="Help",command=help)
    root.config(menu=mymenu)
    mymenu.add_cascade(label="Settings",menu=m1)
    mymenu.add_command(label="Quit",command=quit)

    root.mainloop()