# coding:utf-8
from selenium import webdriver
from config import setting
import configparser

def browser():
    """
    启动浏览器驱动
    :return: 返回浏览器驱动URL
    """
    try:
        # --------- 读取config.ini配置文件 ---------------
        con = configparser.ConfigParser()
        con.read(setting.CONFIG_DIR, encoding='utf-8')
        driver = webdriver.Chrome(con.get('webdriver', 'DRIVER_PATH_CHROME'))
        return driver
    except Exception as msg:
        print("selenium驱动异常---->{0}".format(msg))
