#supercsv v_0_4
import csvtosql
import csv
from os import path

table={}
totalRows = 0
totalColumns = 0

def load(filename, rowHeader=False):
    """loads a csv file exported by MS excel or equivalent format"""
    if isinstance(filename, str):
        try:
            with open(filename) as csvfile:
                _reader = csv.reader(csvfile)
                __load__(filename, _reader, rowHeader)
        except Exception,e:
            print("supercsv error: ")
            print(e)
    else:
        load_reader(filename, rowHeader)

def load_reader(reader, filename, rowHeader=False):
    """loads a predefined csv.reader object"""
    if not isinstance(reader, str):
        __load__(filename, reader, rowHeader)
    else:
        load(reader, rowHeader)

def __load__(filename, _reader, rowHeader):
    global table, totalRows, totalColumns
    __rowHeader=[]
    __sheet=[]
    for row in _reader:
        totalRows+=1
        if rowHeader:
            __rowHeader=list(row)
            rowHeader=False
        else:
            __sheet.append(row)
    totalColumns=len(__sheet[0])
    table_name=__tabulate(__rowHeader, __sheet)
    table[path.splitext(path.basename(filename))[0]]=table_name
    

        
def __tabulate(__rowHeader, __sheet):
    """Create a temporary sqlite table in memory"""
    global table_name
    csvtosql.create_table(__rowHeader,__sheet)
    return csvtosql.table_name

def query(q):
    """Run a sql query"""
    cur=csvtosql.run_query(q)
    selection=[]
    for row in cur:
        selection.append(row)
    return selection

def select(tableName, columnNames='*', where=''):
    """Select operation"""
    q="SELECT "+columnNames+" FROM "+tableName
    if not where:
        q+="WHERE "+where
    return query(q)

def write(filename, table, delimiter = ",", quotation = "\""):
    """Write selected table to a file in csv format"""
    if type(table) is list:
        try:
            fo = open(filename, 'w')
            for row in table:
                line = ""
                for cell in row:
                    s = str(cell).strip()
                    if s.find(delimiter) != -1:
                        line += quotation+s+quotation+delimiter
                    else:
                        line += s+delimiter
                line = line[:len(line)-1]
                fo.write(line+"\n")
            fo.close()
        except Exception, e:
            print(e)
    else:
        print("table parameter should be a list")

##load('sample.csv')
##table=query("SELECT * FROM "+table['sample'])
##write('fruit.csv',table)
