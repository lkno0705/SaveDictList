# SaveDictList
Simple python script that allows you to save or import a List or Dictionary into/from a .txt file, just by calling some imported functions.

SaveDictList.py is the Python3 Module<br/>

SaveDictList_2_7.py is the Python2.7 Module<br/>

INSTALLATION:<br/>
1. download or clone this repository<br/>
2. unzip and open the directory<br/>
3. open up the Python Interpreter<br/>
4.Type:<br/>
  import sys<br/>
  print(sys.path)<br/>
5. hit return to execute<br/>
6. Open the Path that is shown in the Interpreter<br/>
7. Copy the .py File for your Python-version into this directory<br/>

USAGE:<br/>
The Module contains 4 Main functions:<br/>
1. saveList(List)<br/>
2. importList()<br/>
3. saveDict(Dict)<br/>
4. importDict()<br/>

The saveList()-Function takes exactly 1 Argument, which is the list you want to save into a .txt File, aswell as the saveDict()-Function. The saveDict()-Function needs to know the name of the Dictionary you want to save. The .txt-Files are saved in your chosen directory and are named: Save_List_currentDate or Save_Dict_currentDate. The importList()- and importDict()-Function return a List/Dictionary which you can use right away.
