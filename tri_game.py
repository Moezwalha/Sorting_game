import sys
import os
import tkinter as tk
from tkinter.messagebox import *

#verifier la saisie de l'utilisateur
def verif(ch):
    for i in range(len(ch)):
        if ch[i]<'z' and ch[i]>'a':
            showwarning('Résultat','erreur de saisir')
            return False
    return True

def lancer_tri():
    T1=[]
    for i in range(len(T)):
        if verif(str(T[i].get())):
            if i==len(T)-1:
                for i in range(len(T)):
                    if (str(T[i].get())!=''):
                        T1.append(int(T[i].get()))

                #algorithme de tri
                for i in range(len(T1)):
                    min= i
                    for j in range(i+1,len(T1)):
                        if T1[min] > T1[j]:
                            min = j
                
                    tmp = T1[i]
                    T1[i] = T1[min]
                    T1[min] = tmp
                for i in range(len(T1)):
                    e=tk.IntVar()
                    e.set(T1[i])
                    entryresult=tk.Entry(textvariable=e,width=5)
                    entryresult.place(x=(i+1)*50,y=150)
                    
        else:
            break


T=[]
def next_entry(p,n,i):
    def changer_cursor(event):
        if (i!=int(n)):
            next_entry(p,n,i)
    button.destroy()
    label.destroy()
    entry.destroy()  
    i+=1
    entry1=tk.Entry(window,width=5)
    entry1.place(x=p,y=50)
    entry1.focus()
    p+=50
    T.append(entry1)
    entry1.bind("<Return>",changer_cursor)
    if (i!=int(n)):
        next_entry(p,n,i)

#rechoisir le nbre de case à trier
def restart_program():
    python = sys.executable
    os.execl(python,python,* sys.argv) 
    
#construire les cases
def nbre_case():
    i=tk.IntVar()
    n=tk.IntVar()
    p=tk.IntVar()
    n=entry.get()
    T1=[]
    i=0
    p=50
    next_entry(p,n,i)
    #tri boutton
    button = tk.Button(text="Tri",bg="blue",fg="yellow",width=10,height=2,command=lancer_tri,)
    button.place(x=200,y=100)
    #restart boutton
    restart = tk.Button(text="restart",bg="blue",fg="yellow",width=10,height=2,command=restart_program,)
    restart.place(x=300,y=100)
def keyPress(event):
    if not event.char.isdigit():
        return 'break'
        
   
#ouverture fenetre 
window =tk.Tk()
window.geometry('600x400')
window.title(" Sorting Algorithm")
#frame
frame2 = tk.Frame(window, bg="grey")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#label
label=tk.Label(window,text="choisir le nbre de case à trier")
label.place(x=0,y=0)
#entry(nbre de case à saisir)
entry=tk.Entry(window,width=5)
entry.place(x=200,y=0)
entry.focus()
entry.bind('<KeyPress>', keyPress)
#button Click
button = tk.Button(window,
    text="Click",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=nbre_case,)
button.place(x=100,y=100)

window.mainloop()
