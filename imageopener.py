from tkinter import *
from PIL import Image,ImageTk
root=Tk()
imagenumber=1
imagelist=['sample images/pic ('+str(i)+').jpg' for i in range (1,6)]
handler=ImageTk.PhotoImage(Image.open("sample images/pic (1).jpg"))
l=Label(image=handler)
l.grid(row=2,column=0,columnspan=3,pady=10)
def nextimage():
    global imagenumber
    global l
    global handler
    bc=Button(root,text="<<",command=previmage)
    bc.grid(row=1,column=2)
    l.grid_forget()
    handler=ImageTk.PhotoImage(Image.open(str(imagelist[imagenumber])))
    l=Label(image=handler)
    l.grid(row=2,column=0,columnspan=3,pady=10)
    imagenumber+=1
    fw=Button(root,text=">>",command=nextimage)
    fw.grid(row=1,column=0)
    status_bar=Label(root,text="image"+str(imagenumber)+"of"+str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)
    status_bar.grid(row=3,column=0,columnspan=3,sticky=W+E)
    if imagenumber==len(imagelist):
        fw=Button(root,text=">>",command=lambda: nextimage(imagenumber),state=DISABLED)
        fw.grid(row=1,column=0)
    
def previmage():
    global imagenumber
    global l
    global handler
    l.grid_forget()
    handler=ImageTk.PhotoImage(Image.open(str(imagelist[imagenumber-2])))
    l=Label(image=handler)
    l.grid(row=2,column=0,columnspan=3,pady=10)
    imagenumber-=1
    bc=Button(root,text="<<",command=previmage)
    bc.grid(row=1,column=2)
    status_bar=Label(root,text="image"+str(imagenumber)+"of"+str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)
    status_bar.grid(row=3,column=0,columnspan=3,sticky=W+E)
    if imagenumber==1:
        bc=Button(root,text="<<",command= previmage,state=DISABLED)
        bc.grid(row=1,column=2)
    fw=Button(root,text=">>",command=nextimage)
    fw.grid(row=1,column=0)


fw=Button(root,text=">>",command=nextimage)
fw.grid(row=1,column=0)
bc=Button(root,text="<<",command=previmage,state=DISABLED)
bc.grid(row=1,column=2)
qt=Button(root,text="EXIT",fg='red',command=root.quit)
qt.grid(row=0,column=1)
status_bar=Label(root,text="image"+str(imagenumber)+"of"+str(len(imagelist)),bd=1,relief=SUNKEN,anchor=E)
status_bar.grid(row=3,column=0,columnspan=3,sticky=W+E)
root.mainloop()