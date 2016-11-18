# supercsv
### version: v 0.4S
#####Read CSV files in the way you wanted directly from your python code.
#####Run sql query and write to a csv file without any effort.

Load any csv files exported from MS excel sheet or similar format
```python
import supercsv
supercsv.load('sample.csv')
```
If your csv include row header then pass 'True' value to load function and the code will handle the rest
```python
supercsv.load('sample.csv',True)
```
You can also import csv module and pass a csv.reader object to load_reader function to load custom csv file.

The csv file is converted into sqlite3 table with ability to maintain the datatype (Date and time datatype is not supported yet and will be treated as TEXT)
and the table is temporarily loaded into memory(till the end of the program).
If the row header is not defined column names are named as 'col_0', 'col_1', 'col_2'....
The name of the created sqlite table can be accessed using 'table' dictionary
You can run sql query on loaded csv file
```python
table_name = supercsv.table['filename_without_extension']
selection = supercsv.query("SELECT * FROM "+table_name)
```
This is not tested but you can load multiple csv file and use 'join' operation.

You can also write your query result to a file in csv format with ',' as default delimiter and '"' as default quotation 
```python
supercsv.write('file.csv', selection)
```
 
