import pymssql

conn = pymssql.connect(server='192.168.0.113:1433', user='CTTQ_Data_Import_For_TMS_Data', password='CTTQ_Data_Import_For_TMS_Data', database='CTTQ_Data_Import_For_TMS_Data',charset='GBK',as_dict=True)

cursor = conn.cursor()
cursor.execute("select * from dms_file")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()