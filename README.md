# Welcome to my demo project!
This is demo project how about python connect SQL Server.

# Let’s get started
With IDE, you can use VScode or Pycharm. **Don't forget install Python.exe**.
In this example, I need to install **pyodbc**
Let’s talk about each of the steps.

### 1. Create database in SQL Server
I' ll create a new database is **test_python**. The next, I add a new table is My_Table.


![create database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/create%20db.jpg)

### 2.  CRUD

#### 2.1. Connect to database in sql server
You can use to connect Python to SQL Server:

>conn = pyodbc.connect('Driver={SQL Server};'  
 'Server=QUANGKUN\LINHQUANG;' 
 'Database=test_python;'
  'Trusted_Connection=yes;')

Let’s review an example, where:

-   The Server Name is:  **QUANGKUN/LINHQUANG**
-   The Database Name is:  **test_python**
-   The Table Name (with a dbo schema) is:  **dbo.My_Table**

#### 2.2. Read data from data table
>print("Read")  
cursor = conn.cursor()  
cursor.execute('SELECT * FROM test_python.dbo.My_Table')  
for row in cursor:  
___print(row)

I print the result in console.

![Read database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/read.jpg)

#### 2.3. Create in data
>print("Create")  
cursor = conn.cursor()  
cursor.execute( 'insert into test_python.dbo.My_Table(Name) values(?);',  ('Dog'))  
conn.commit()  
read(conn)

![Add new database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/databse%20create.jpg)

#### 2.4. Update in data
>print("Update")  
cursor = conn.cursor()  
cursor.execute( 'update test_python.dbo.My_Table set Name = ? where ID = ?;',  ('Raichu', 1))  
conn.commit()  
read(conn)

![Update database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/database%20update.jpg)

#### 2.5. Delete in data
>print("Delete")  
cursor = conn.cursor()  
cursor.execute( 'delete from test_python.dbo.My_Table where Id = ?',  5 )  
conn.commit()  
read(conn)

![Update database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/database%20delete.jpg)

#### 2.6. Check in data
>print("Check")  
cursor = conn.cursor()  
cursor.execute('SELECT Name FROM test_python.dbo.My_Table Where Name = ?', "Raichu")  
for row in cursor:  
___print(row)

I print the result in console.

![Check database](https://github.com/LinhQuangHua/Demo-Python-connect-Sql/blob/master/doc/after%20check.jpg)

# References

https://datatofish.com/how-to-connect-python-to-sql-server-using-pyodbc/
