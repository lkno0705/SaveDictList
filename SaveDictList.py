import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import time

# dd-mm-yyyy format

#list = ["a","b","c","d","e","f","g","h"]
#dict = {"red":"rot", "blau":"Blue"}

def saveList(list):
    
    File = getPath("List")
    Fobj = open(File, "w+")
    
    X = len(list)
    for i in range(X):
        Fobj.write(str(list[i])+"\n")
    
    Fobj.close()
    
    Done()
    
def importList():
    
    List = []
    Path=FileDialog()
    Fobj = open(Path, "r")
    
    for line in Fobj:
        X = line.rstrip()     
        List.append(str(X))
        
    return List
    
def saveDict(Dict):
    
    File = getPath("Dict")
    Fobj = open(File, "w+")
    
    Keys = []
    Values = []
    
    for i,j in Dict.items():
        Keys.append(i)
        Values.append(j)
    
    Y = len(Keys)
    for x in range(Y):
        Fobj.write(Keys[x]+":"+Values[x]+"\n")
        
    Fobj.close()   
    Done()
 
def importDict():
    
    Dict = {}
    
    File = FileDialog()
    Fobj = open(File, "r")
    
    for line in Fobj:
        X = line.rstrip()
        X = X.split(":")
        
        Dict[str(X[0])] = str(X[1])
        
    print(Dict)
    
    return Dict
        
        
def getPath(Type):
    Path = os.getcwd()
    File = Path+"/Saved_"+Type+"_"+time.strftime("%d-%m-%Y")+".txt"
    
    return File

def Done():
    
    MainWindow = tk.Tk()
    MainWindow.geometry("100x10")
    
    done = Label(MainWindow, text="DONE!")
    done.pack()
    
    MainWindow.mainloop()

def FileDialog():
    
    MainWindow = tk.Tk()
    MainWindow.withdraw()
    
    Path = filedialog.askopenfilename()
    
    return Path

#saveList(list)
#saveDict(dict)
#Liste1 = importList()
#print(Liste1)
#importDict()