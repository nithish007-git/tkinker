from tkinter import *
window=Tk()
window.title("KM to miles")
window.minsize(width=200,height=100)

#label
def label_1():
    print("hi")

label=Label(text="converted into ")
label.grid(column=1,row=2,padx=10)


#entry
def miles():
   miles=float(entry1.get())
   km=miles*1.68

   entry2.config(text=f"{km}")
   #1 entry
entry1=Entry(width=10)
entry1.grid(column=2,row=1)
#entery 2
entry2=Label(width=10,text="0")
entry2.grid(column=2,row=3)
#side labels
label1=Label(text="miles ")
label1.grid(column=3,row=1,padx=10)

#km
label2=Label(text="km")
label2.grid(column=3,row=3,padx=10)

#button
cal=Button(text="calculate",command=miles)
cal.grid(column=2,row=4)


window.mainloop()
