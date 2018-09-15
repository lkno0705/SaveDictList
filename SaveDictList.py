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
    
    Done(File)
    
def importList():
    
    List = []
    Path=FileDialog("")
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
    Done(File)
 
def importDict():
    
    Dict = {}
    
    File = FileDialog("")
    Fobj = open(File, "r")
    
    for line in Fobj:
        X = line.rstrip()
        X = X.split(":")
        
        Dict[str(X[0])] = str(X[1])
    
    return Dict
        
        
def getPath(Type):
    Path = FileDialog("dir")
    File = Path+"/Saved_"+Type+"_"+time.strftime("%d-%m-%Y")+".txt"
    
    return File

def Done(Path):

    MainWindow = tk.Tk()
    MainWindow.title("Save complete!")
    MainWindow.geometry("500x20")
    
    done = Label(MainWindow, text="DONE! Path: "+str(Path))
    done.pack()
    
    MainWindow.mainloop()

def FileDialog(Type):
    
    MainWindow = tk.Tk()
    MainWindow.withdraw()
    
    if Type == "dir":
        MainWindow.update()
        Path = filedialog.askdirectory(
            title = "Select directory")
        MainWindow.destroy()
    else:
        MainWindow.update()
        Path = filedialog.askopenfilename(
            defaultextension = ".txt"
            title = "Select your Dict/List Save File")
    
    return Path

#Liste1 = importList()
#print(Liste1)
#saveList(list)
#saveDict(dict)
#importDict()
