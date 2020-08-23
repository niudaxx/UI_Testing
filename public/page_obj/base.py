# _*_ coding:utf-8 _*_
import configparser
from config import setting
from public.models.log import Log
con = configparser.ConfigParser()
con.read(setting.CONFIG_DIR,encoding='utf-8')
# --------- 读取config.ini配置文件 ---------------
login_url = con.get("WebURL","URL")
log = Log()

"""
基础类：页面对象的获取与继承
"""
class Page(object):

    def __init__(self,selenium_driver,base_url=login_url,parent=None):
        self.base

