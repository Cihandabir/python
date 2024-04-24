from tkinter import *
import tkinter as tk
pencere=tk.Tk()
pencere.geometry("162x311")
pencere.config(bg = "Yellow")
imaj = PhotoImage(file = "icon.gif")
b = Button(pencere, image=imaj)
b.place(x=10, y=10)
pencere.mainloop()
import colorama

from colorama import init, Fore, Back, Style

init(convert=True)

""" Input your birthdate and month and get your Guardian Angel =int(input("1,12"))"""
month=int(input("Enter your birth month numerically="))
day=int(input("Enter your birth day numerically="))
if month==1:
    if 1<=day<=5:
        Guardian_Angel="Nemamiah"
        print(imaj)
    elif 6<=day<=10:
        Guardian_Angel="Yeialel"
    elif 11<=day<=15:
        Guardian_Angel="Harahel"
    elif 16<=day<=20:
        Guardian_Angel="Mitzrael"
    elif 21<=day<=25:
        Guardian_Angel="Umabel"
    elif 26<=day<=30:
        Guardian_Angel="Iah-Hel"
    elif day==31:
        Guardian_Angel="Anauel"
        from tkinter import *

    elif 31<day:
        print("Please enter a valid date.")
elif month==2:
    if 1<=day<=4:
        Guardian_Angel="Anauel"
    elif 5<=day<=9:
        Guardian_Angel="Mehiel"
    elif 10<=day<=14:
        Guardian_Angel="Damabiah"
    elif 15<=day<=19:
        Guardian_Angel="Manakel"
    elif 20<=day<=24:
        Guardian_Angel="Eyael"
    elif 25<=day<=29:
        Guardian_Angel="Habuhiah"
elif month==3:
    if 1<=day<=5:
        Guardian_Angel="Rochel"
    elif 6<=day<=10:
        Guardian_Angel="Yabamiah"
    elif 11<=day<=15:
        Guardian_Angel="Hayayel"
    elif 16<=day<=20:
        Guardian_Angel="Mumiah"
    elif 21<=day<=25:
        Guardian_Angel="Vehuiah"
    elif 26<=day<=30:
        Guardian_Angel="Yeliel"
    elif day==31:
        Guardian_Angel="Sitael"
elif month==4:
    if 1<=day<=4:
        Guardian_Angel="Sitael"
    elif 5<=day<=9:
        Guardian_Angel="Elemiah"
    elif 10<=day<=14:
        Guardian_Angel="Mahasiah"
    elif 15<=day<=20:
        Guardian_Angel="Lelahel"
    elif 21<=day<=25:
        Guardian_Angel="Ahaiah"
    elif 26<=day<=30:
        Guardian_Angel="Cahetel"
elif month==5:
   if 1<=day<=5:
        Guardian_Angel="Haziel"
   elif 6<=day<=10:
        Guardian_Angel="Aladiah"
   elif 11<=day<=15:
        Guardian_Angel="Lauviah"
   elif 16<=day<=20:
        Guardian_Angel="Hahaiah"
   elif 21<=day<=25:
        Guardian_Angel="Yezalel"
   elif 26<=day<=31:
        Guardian_Angel="Mebahel"
elif month==6:
   if 1<=day<=5:
        Guardian_Angel="Hariel"
   elif 6<=day<=10:
        Guardian_Angel="Hakamiah"
   elif 11<=day<=15:
        Guardian_Angel="Laviah"
   elif 16<=day<=20:
        Guardian_Angel="Caliel"
   elif 21<=day<=25:
        Guardian_Angel="Leuviah"
   elif 26<=day<=30:
        Guardian_Angel="Pahaliah"
elif month==7:
   if day==1:
       Guardian_Angel="Pahaliah"
   elif 2<=day<=6:
        Guardian_Angel="Nelahel"
   elif 7<=day<=11:
        Guardian_Angel="Yeyayel"
   elif 12<=day<=16:
        Guardian_Angel="Melahel"
   elif 17<=day<=22:
        Guardian_Angel="Haheuiah"
   elif 23<=day<=27:
        Guardian_Angel="Nithaiah"
   elif 28<=day<=31:
        Guardian_Angel="Haiiah"
elif month==8:
   if day==1:
       Guardian_Angel="Haiiah"
   elif 2<=day<=6:
        Guardian_Angel="Yeratel"
   elif 7<=day<=12:
        Guardian_Angel="Seehaiah"
   elif 13<=day<=17:
        Guardian_Angel="Reiyel"
   elif 18<=day<=22:
        Guardian_Angel="Omael"
   elif 23<=day<=28:
        Guardian_Angel="Lecabel"
   elif 29<=day<=31:
        Guardian_Angel="Vasariah"
elif month==9:
   if 1<=day<=2:
        Guardian_Angel="Vasariah"
   elif 3<=day<=7:
        Guardian_Angel="Yehuiah"
   elif 8<=day<=12:
        Guardian_Angel="Lehehaiah"
   elif 13<=day<=17:
        Guardian_Angel="Khavakiah"
   elif 18<=day<=23:
        Guardian_Angel="Menadel"
   elif 24<=day<=28:
        Guardian_Angel="Aniel"
   elif 29<=day<=30:
        Guardian_Angel="Haamiah"
elif month==10:
   if 1<=day<=3:
       Guardian_Angel="Haamiah"
   elif 4<=day<=8:
        Guardian_Angel="Reheael"
   elif 9<=day<=13:
        Guardian_Angel="Yeiazel"
   elif 14<=day<=18:
        Guardian_Angel="Hahehel"
   elif 19<=day<=23:
        Guardian_Angel="Mikael"
   elif 24<=day<=28:
        Guardian_Angel="Veuliah"
   elif 29<=day<=31:
        Guardian_Angel="Yelahiah"
elif month==11:
   if 1<=day<=2:
        Guardian_Angel="Yelahiah"
   elif 3<=day<=7:
        Guardian_Angel="Sealiah"
   elif 8<=day<=12:
        Guardian_Angel="Ariel"
   elif 13<=day<=17:
        Guardian_Angel="Asaliah"
   elif 18<=day<=22:
        Guardian_Angel="Mihael"
   elif 23<=day<=27:
        Guardian_Angel="Vehuel"
   elif 28<=day<=30:
        Guardian_Angel="Daniel"
elif month==12:
   if 1<=day<=2:
        Guardian_Angel="Daniel"
   elif 3<=day<=7:
        Guardian_Angel="Hahasiah"
   elif 8<=day<=12:
        Guardian_Angel="Imamiah"
   elif 13<=day<=16:
        Guardian_Angel="Nanael"
   elif 17<=day<=21:
        Guardian_Angel="Nitael"
   elif 22<=day<=26:
        Guardian_Angel="Mebahiah"
   elif 27<=day<=31:
        Guardian_Angel="Poyel"

print(colorama.Fore.MAGENTA + "Your Guardian Angel= "+Guardian_Angel)

input(colorama.Fore.RED + "press enter to exit.")

