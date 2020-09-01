# _*_ coding:utf-8 _*_
from time import sleep

from selenium.webdriver.common.by import By

from config import setting
from public.models.getYaml import getyaml
from public.page_obj.base import Page


testData = getyaml(setting.TEST_Element_YAML + '/' + 'login.yaml')

class login(Page):
    """
    用户登录页面
    """
    url = '/'

    # 定位器，通过元素属性定位元素对象
    # 用户名文本框
    login_userName_loc = (testData.get_find_type(0), testData.get_elementinfo(0))
    # 密码文本框
    login_password_loc = (testData.get_find_type(1), testData.get_elementinfo(1))
    # 厂区下拉框
    keeplogin_button_loc = (testData.get_find_type(2), testData.get_elementinfo(2))
    # 部门下拉框
    login_user_loc = (testData.get_find_type(3), testData.get_elementinfo(3))
    # 登陆按钮
    login_exit_loc = (testData.get_find_type(4), testData.get_elementinfo(4))

