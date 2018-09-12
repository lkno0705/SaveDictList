# SaveDictList
Simple python script that allows you to save or import a List or Dictionary into/from a .txt file, just by calling some imported functions.

SaveDictList.py is the Python3 Module

SaveDictList_2_7.py is the Python2.7 Module

INSTALLATION:
1. download or clone this repository
2. unzip and open the directory
3. open up the Python Interpreter

4.Type:

  import sys
  
  print(sys.path)
5. hit return to execute
6. Open the Path that is shown in the Interpreter
7. Copy the .py File for your Python-version into this directory

USAGE:
The Module contains 4 Main functions:
1. saveList(List)
2. importList()
3. saveDict(Dict)
4. importDict()

The saveList()-Function takes exactly 1 Argument, which is the list you want to save into a .txt File, aswell as the saveDict()-Function. The saveDict()-Function needs to know the name of the Dictionary you want to save. The .txt-Files are saved in your working directory (the directory where your Python programm/script is in) and are named: Save_List_currentDate or Save_Dict_currentDate. I'll add the possibility to enter your own Path, to save the Files, later on. The importList()- and importDict()-Function return a List/Dictionary which you can use right away.
