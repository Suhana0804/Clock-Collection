import tkinter as tk
a=tk.Tk()
a.geometry('750x300')
a.title("Stop Watch")
count=0
def begin():
    global count
    count=0
    start()
def start():
    if count==0:
        f=time["text"]
        h,m,s=map(int,f.split(":"))
        if s<60:
            s=s+1
        elif s==60:
            s=0
            if m<60:
                m=m+1
            elif m==60:
                h=h+1
                m=0
        if h<10:
            h="0"+str(h)
        if m<10:
            m="0"+str(m)
        if s<10:
            s="0"+str(s)
        time["text"]=str(h)+":"+str(m)+":"+str(s)    
        a.after(1000,start)
def hold():
    global count
    count=1
def reset():
    global count
    count=1
    time["text"]="00:00:00"
time=tk.Label(text="00:00:00",font=("Times 12 bold",25))
b=tk.Button(text="Start",bg="pink",command=begin)
c=tk.Button(text="Stop",bg="pink",command=hold)
d=tk.Button(text="Reset",bg="red",command=reset)
e=tk.Button(text="Exit",bg="red",command=a.destroy)
time.grid(row=2,column=3)
b.grid(row=3,column=1)
c.grid(row=3,column=3)
d.grid(row=3,column=5)
e.grid(row=4,column=3)
a.mainloop()
