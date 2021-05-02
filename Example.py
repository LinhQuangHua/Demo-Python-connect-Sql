import pyodbc


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_python.dbo.My_Table')
    for row in cursor:
        print(row)
    print()

def create(conn):
    print("Create")
    cursor = conn.cursor()
    cursor.execute(
        'insert into test_python.dbo.My_Table(Name) values(?);',
        ('Dog'),
    )
    conn.commit()
    read(conn)

def update(conn):
    print("Update")
    cursor = conn.cursor()
    cursor.execute(
        'update test_python.dbo.My_Table set Name = ? where ID = ?;',
        ('Raichu', 1)
    )
    conn.commit()
    read(conn)

def delete(conn):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute(
        'delete from test_python.dbo.My_Table where Id = ?',
        5
    )
    conn.commit()
    read(conn)    

def check(conn):
    print("Check")
    cursor = conn.cursor()
    cursor.execute('SELECT Name FROM test_python.dbo.My_Table Where Name = ?', "Raichu")
    for row in cursor:
        print(row)

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=QUANGKUN\LINHQUANG;'
                      'Database=test_python;'
                      'Trusted_Connection=yes;')


read(conn)
check(conn)


conn.close()
