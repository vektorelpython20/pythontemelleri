from tkinter import *

pencere = Tk()
pencere.geometry("600x400+200+200")
#--------------------------------------------------
etiket = Label(pencere,text="Kullanıcı Adı:",width=40)
etiket.grid(column=0,row=0)
txtUser = Entry(pencere)
txtUser.grid(column=1,row=0)
etiket2 = Label(pencere,text="Şifre",width=40)
etiket2.grid(column=0,row=1)
txtPass = Entry(pencere,show="*")
txtPass.grid(column=1,row=1)
def giris():
    if txtUser.get() and txtPass.get():
        if txtUser.get() == "Ediz" and txtPass.get() == "12345":
            print("Giriş Başarılı")
        else:
            print("Giriş Başarısız")

def Temizle():
    txtUser.delete(0,END)
    txtUser.insert(0,"")
    txtPass.delete(0,END)
    txtPass.insert(0,"")    
        
dugme1 = Button(pencere,text="Giriş Yap",command=giris)
dugme1.grid(column=0,row=2)

dugme2 = Button(pencere,text="Temizle",command=Temizle)
dugme2.grid(column=1,row=2)


#--------------------------------------------------
pencere.mainloop()