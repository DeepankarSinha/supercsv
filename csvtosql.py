#csvtosql v1_0_0
import re
import time
import sqlite3

__sheet=[]

table_name = 'temp_table_{0}'.format(int(time.time()))
db = sqlite3.connect(':memory:')
cur=db.cursor()

def is_Integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_Real(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def create_table(header,sheet):
    global __sheet
    __sheet=sheet
    tr1=__sheet[0]
    tr2=__sheet[1]
    datatype=[]
    for i in range(len(tr1)):
        n=tr1[i]
        m=tr2[i]
        if is_Integer(n) and is_Integer(m):
            datatype.append('INTEGER')
        elif is_Real(n) and is_Real(m):
            datatype.append('REAL')
        else:
            datatype.append('TEXT')

    i=0
    sql="CREATE TEMPORARY TABLE {0}(".format(table_name)
    s=[]
    if header:
        for i in range(len(tr1)):
            s.append(header[i]+" "+datatype[i])
        sql+=", ".join(s)
    else:
        for i in range(len(tr1)):
            s.append("col_"+`i`+" "+datatype[i])
        sql+=", ".join(s)
    sql+=");"
    
    cur.execute(sql)
    db.commit()

    sql = "INSERT INTO {0} VALUES (".format(table_name)
    sql += ', '.join(('? ' * len(tr1)).split())
    sql += ');'

    for row in __sheet:
        cur.execute(sql,tuple(row))
        db.commit()

def run_query(q):
    try:
        cur.execute(q)
        db.commit();
    except Exception as e:
        print(e)
    return cur
    
    
