import tkinter
from tkinter import *

wind=Tk()
wind.title("Fibonacci Series")
wind.geometry('600x500')
wind.resizable(width=False,height=False)
ttl=Label(wind,text="Fibonacci Series",font=('arial',15,'bold','italic'),pady=10)
ttl.pack()
def fibbo():
    start=int(ent.get())
    end=int(ent1.get())
    sum=start+end
    i=0
    new=Label(wind,text=f'{start}',padx=5)
    new.pack(side='left',anchor='center')
    new2=Label(wind,text=f'{end}')
    new2.pack(side='left',anchor='center',padx=5)
    while(i<=10):
        start=end
        end=sum
        sum=start+end
        new=Label(wind,text=f'{sum}')
        new.pack(side='left',anchor='center',padx=5)
        i+=1
first=Label(wind,text='ENter First NUmber :',font=('arial',10,''))
first.place(relx=.25,rely=.2)
ent=Entry(wind,font=('arial',10,''))
ent.place(relx=.5,rely=.2)
second=Label(wind,text='ENter Second NUmber :',font=('arial',10,''))
second.place(relx=.25,rely=.3)
ent1=Entry(wind,font=('arial',10,''))
ent1.place(relx=.5,rely=.3)
btn=Button(wind,text='Start',font=('arial',10,'bold'),command=fibbo)
btn.place(relx=.38,rely=.4)
wind.mainloop()