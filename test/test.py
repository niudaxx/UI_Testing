import pymssql

conn = pymssql.connect(server='localhost:1433', user='CTTQ_TRING', password='CTTQ_TRING', database='CTTQ_TRING',charset='GBK',as_dict=True)

cursor = conn.cursor()
cursor.execute("select * from dms_file")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()