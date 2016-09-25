#supercsv_0_1
import csv


__sheet=[]
__rowHeader=[]
hasHeader=False
cursorx=0
cursory=0
totalRows=0
totalColumns=0

__all__ = ["load","load_reaortder","get_row","get_column","get_column_number","eac",
           "mc","show","select"]

def load(filename, rowHeader=False):
    """loads a csv file exported by MS excel or equivalent format"""
    global totalRows
    global totalColumns, hasHeader, __sheet, __rowHeader
    del __sheet[:]
    hasHeader=rowHeader
    totalRows=totalColumns=0
    with open(filename) as csvfile:
        _reader = csv.reader(csvfile)
        for row in _reader:
            totalRows+=1
            if rowHeader:
                __rowHeader=list(row)
                rowHeader=False
            else:
                __sheet.append(row)
        totalColumns=len(__sheet[0])

def load_reader(_reader, rowHeader=False):
    """loads a predefined csv.reader object"""
    global totalRows
    global totalColumns, hasHeader, __sheet, __rowHeader
    del __sheet[:]
    totalRows=totalColumns=0
    for row in _reader:
        totalRows+=1
        if rowHeader:
            __rowHeader=list(row)
            rowHeader=False
        else:
            __sheet.append(row)
    totalColumns=len(__sheet[0])

def get_row(rowNumber):
    """returns a row as a list"""
    row=__sheet[rowNumber]
    return row

def get_column(columnNumber):
    """returns a column as a list"""
    entry=[]
    for row in __sheet:
        entry.append(row[columnNumber])
    return entry

def get_column_number(columnName):
    """returns index of a column"""
    for i,x in enumerate(__rowHeader):
        if x == columnName:
            return i

def eac():
    """eac stands for Entry At Cursor"""
    row=__sheet[cursorx]
    return row[cursory]

def mc(x=0, y=0):
    """mc stands for Move Cursor
       Moves the cursor by x and y values
    """
    global cursorx, cursory
    if cursorx+x >= 0 and cursorx+x < totalRows:
        if cursory+y >= 0 and cursory+y < totalColumns:
            cursorx=cursorx+x
            cursory=cursory+y
        else:
            print('The cursor could not be moved. Error moving cursor by y values')
    else:
        print('The cursor could not be moved. Error moving cursor by x values')
 
def show(i=None, j=None):
    """print the csv file
       i- ith row
       j- jth column
    """
    if i is None and j is None:
           for row in __sheet:
               print(', '.join(row))
    elif i is not None and j is None:
           row=__sheet[i]
           print(', '.join(row))
    elif i is None and j is not None:
           row=__sheet[j]
           print(', '.join(row))
    else:
           row=__sheet[i]
           print(row[j])

################################################################

__selection=[]

def select(*clist):
    """selects column and return the selection list"""
    global __selection,totalColumns
    del __selection[:]
    if not clist:
        __selection=__sheet
    elif hasHeader:
        flag=False
        for data in clist:
            if data not in __rowHeader:
                flag=True
                break
        if flag:
            print('Column not found')
        else:
            for data in clist:
                __selection.append(get_column(get_column_number(data)))
    else:
        for i in clist:
            if i >= 0 and i < totalColumns:
                __selection.append(get_column(i))
            else:
                print('Operation failed. Index out of bound')
                del __selection[:]
    return __selection
        
           
    
    
