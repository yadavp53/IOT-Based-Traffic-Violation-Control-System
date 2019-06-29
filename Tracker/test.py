import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("gui")
root.geometry('400x200')

tab=ttk.Notebook(root)
page1=ttk.Frame(tab)
tab.add(page1,text="home")
tab.pack()

name_Label=ttk.Label(page1,text="name")
name_Label.grid(row=0,column=0,sticky=tk.W)
city_Label=ttk.Label(page1,text="city")
city_Label.grid(row=0,column=1,sticky=tk.W )

name_var=tk.StringVar()
city_var=tk.StringVar()

name_entry=ttk.Entry(page1,width=15,textvariable=name_var)
name_entry.grid(row=1,column=0)
city_entry=ttk.Entry(page1,width=15,textvariable=age_var)
city_entry.grid(row=1,column=1)

def action2():
    n=name_var.get()
    c=city_var.get()
    with open(r"D:\python\city.txt","a")as f:
        f.write(f"\n name is {n}\n,city is {c}")
    name_entry.delete(0,tk.END)
    city_entry.delete(0,tk.END)

submit=ttk.Button(root,text="submit",command=action2)
submit.grid(row=2,column=0)

root.mainloop()