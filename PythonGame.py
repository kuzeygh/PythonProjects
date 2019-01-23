import Tkinter as tk
from itertools import count
from math import *
from random import *



border=3
c=0
i=0
List=[]
p=1
number=0
ek=0

root = tk.Tk()
root.config( bg='purple' )
root.title("Python Game")



   

def check():
    global p
    global number
    global border
    global List
    global i 
    global ek
   
   
    while i < border+ek:
           
         if List[ i ] == number%10:
           
            number=number/10
         else:
            p=0  
      
         i=i+1
    ek=i 
def start_counter(label):
    global border
    global c
    global List
    c=0

    def update_func():
        global border
        global c
        global List
        if c==border:
              label.config( text=str('Guess it !') ,bg='purple',fg='white',font=('times', 30, 'italic'))
        if c < border:
           counter = str(randrange(1,9))
           x=int( randrange(0,10) )
           List.append( int( counter ) )
           if x==0:
              label.config( text=str(counter) ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==1:
              label.config( text="\n\n\n\n\n\n\n\n                    "+str(counter)+"\n\n\n\n\n" ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==2:
              label.config( text="                            "+str(counter)+"\n\n\n" ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==3:
              label.config( text="\n\n              "+str(counter)+"\n\n" ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==4:
              label.config( text="\n\n\n\n    "+str(counter) ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==5:
              label.config( text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n"+str(counter)+"\n       " ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==6:
              label.config( text=str(counter)+"\n\n\n\n\n\n      " ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==7:
              label.config( text="                         "+str(counter)+"\n                " ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==8:
              label.config( text="\n\n "+str(counter)+"\n\n\n\n       " ,bg='purple',fg='white',font=('times', 30, 'italic'))
           if x==9:
              label.config( text="\n\n\n\n\n"+str(counter) ,bg='purple',fg='white',font=('times', 30, 'italic'))
       
           label.after(2000, update_func)  # 1000ms
           c=c+1
    update_func()

def evaluate(event):
    global number
    global ek
    global i
    global border
    number=int (entry.get()) 
    check()

    if p !=1:
 
       exit(0)
 
    if p==1:  
      
      border=border+1
      root.after(0,start_counter(label))
     
      

while True:

    label = tk.Label(root, fg="white",width=20,height=15  )

    label.pack()
    entry = tk.Entry(root)
    entry.bind("<Return>", evaluate)

    entry.pack()
    
    start_counter(label)



    button2 = tk.Button(root, text='Finish', width=30, command=quit)
    button2.pack()

    root.mainloop()
 
   





