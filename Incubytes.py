import mysql.connector

connection = mysql.connector.connect(host='localhost', database='incubytes', user='root', password='HF420@mysql')

mySql_distinct_country_Query = """SELECT DISTINCT Country FROM stagdata"""

cursor = connection.cursor()
cursor.execute(mySql_distinct_country_Query)
distinct_country_records = cursor.fetchall()

for i in distinct_country_records:
    country_name = i[0]
    
    mySql_Drop_Table_Query = """DROP TABLE IF EXISTS Table_""" + str(country_name)
    cursor.execute(mySql_Drop_Table_Query)
    
    mySql_Create_Table_Query = """CREATE TABLE  Table_""" + str(country_name) + """ SELECT * FROM stagdata WHERE Country = '""" + str(country_name) + """'"""
    cursor.execute(mySql_Create_Table_Query)

cursor.close()
connection.close()