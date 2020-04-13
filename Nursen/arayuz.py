from tkinter import *

pencere = Tk()
pencere.geometry("400x400+200+200")
#-----------------------------------------------
etiket = Label(pencere,text="Python'da ilk arayüz elemanım")
etiket.grid(column=0,row=0)
def tiklandi():
    etiket["text"] = "TIKLANDI"
    dugme = Button(pencere,text="TIKLA",command=tiklandi,width=50)
    dugme.grid(column=1,row=0)
#-----------------------------------------------
def tiklandi2():
    yazi = txt.get()
    etiket2.configure(text=yazi)
txt=Entry(pencere)

txt = Entry(pencere,width=40)
txt.grid(column=0,row=1)
dugme2 = Button(pencere,text="=>AKTAR=>",command=tiklandi2)
dugme2.grid(column=1,row=1)
etiket2 = Label(pencere,text="--")
etiket2.grid(column=2,row=1)
#-------------------------------------------------
pencere.mainloop()