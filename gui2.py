from tkinter import *
from tkinter import filedialog
import random
def open_file():
    result=filedialog.askopenfile(initialdir="/",title="Select a CSV file",filetypes=(("CSV Files","*.csv"),))
    df=[line.strip().split(',') for line in result]
    del df[0]
    for k in df:
        details[k[0]]=k[1]

def combo_finder():
    Iterations  = 20000
    j=1
    for i in range(Iterations):
        SetSize=random.randint(2,4)
        keys = random.sample(list(details), SetSize)
        Chromosome=tuple(keys)
        sum=0
        for k in keys:
            sum=sum+int(details[k])
        if sum>int(lower_limit.get()) and sum<int(upper_limit.get()):
            ResultList.add(Chromosome)

def show_comb():
    i=1
    if ResultList:
        for r in ResultList:
            l.insert(i,r)
            i+=1


root=Tk()
root.title("Combo Finder")
details={}
ResultList  = set()
upload=Button(root,text="Upload CSV File",command=open_file)
upload.grid(row=0,columnspan=2)
lower=Label(root,text="Enter Lower Limit")
upper=Label(root,text="Enter Upper Limit")
lower_limit=Entry(root)
upper_limit=Entry(root)
lower.grid(column=0,row=1)
upper.grid(column=0,row=2)
lower_limit.grid(column=1,row=1)
upper_limit.grid(column=1,row=2)
Submit=Button(root,text="Generate Combinations",command=combo_finder)
Submit.grid(column=0,row=3,columnspan=2)
l=Listbox(root)
Show=Button(root,text="Show Combinations",command=show_comb)
Show.grid(column=0,row=4,columnspan=2)
l.grid(column=0,row=5,columnspan=2)



root.geometry("320x310")
root.mainloop()
