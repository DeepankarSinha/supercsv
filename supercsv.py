#supercsv_0_1
import csv


__sheet=[]
cursorx=0
cursory=0
totalRows=0
totalColumns=0

__all__ = ["load","load_reader","get_row","get_column","eac",
           "mc","show"]

def load(filename):
    """loads a csv file exported by MS excel or equivalent format"""
    global totalRows
    global totalColumns
    totalRows=totalColumns=0
    with open(filename) as csvfile:
        _reader = csv.reader(csvfile)
        for row in _reader:
            totalRows+=1
            __sheet.append(row)
        totalColumns=len(__sheet[0])

def load_reader(_reader):
    """loads a predefined csv.reader object"""
    global totalRows
    global totalColumns
    totalRows=totalColumns=0
    for row in _reader:
        totalRows+=1
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

    
