import pymssql
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

conn = pymssql.connect(server='localhost:1433', user='CTTQ_TRING', password='CTTQ_TRING', database='CTTQ_TRING',charset='GBK',as_dict=True)

cursor = conn.cursor()
cursor.execute("select * from dms_file")
row = cursor.fetchone()
while row:
    print (row)
    row = cursor.fetchone()

# 下拉框选中
#driver = webdriver.Chrome()
#Select(driver.find_element(By.ID)).select_by_visible_text()