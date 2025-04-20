

from time import sleep
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import Select
from xlrd import open_workbook



def wait_for_element(func):
    def wrapper(*args,**kwargs):
        instance=args[0]
        locator=args[1]
        # print(f"waiting for element {locator}")
        _wait=WebDriverWait(instance.driver,10)
        v=visibility_of_element_located(locator)
        _wait.until(v)
        n=func(*args,**kwargs)
        return n
    return wrapper
class SeleniumWrapper:
    def __init__(self,driver):
        self.driver=driver

    @wait_for_element
    def enter_text(self,locator, /, *, value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait_for_element
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @wait_for_element
    def select_item(self,locator, /, *, item):
        webelement = self.driver.find_element(*locator)
        # select_item(("id","cars"),item="Mercedes")
        # s=select(webelement)
        s =Select(webelement)
        s.select_by_visible_text(item)
    @wait_for_element
    def find_elements(self,locator):
        m=self.driver.find_elements(*locator)
        for i in m:
            print(i.text)
        return len(m)
    @wait_for_element
    def is_displayedp(self,locator):
        return self.driver.find_element(*locator).isdisplayed

    def save_scr(self):
        d=datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
        print(d)
        print("screeshot saved")
        self.driver.save_screenshot(rf"C:\Users\DELL\Pictures\Screenshots/{d}.png")
    # def read_data_from_xls(self,filepath,sheetname):
    #     wb=open_workbook(rf"{filepath}")
    #     ws=wb.sheet_by_name(sheetname)
    #     rowcount=ws.nrows
    #     data=[]
    #     for index in range(1,rowcount):
    #         row=ws.row_values(index)
    #         data.append((row[0],row[1]))
    #     return data
   def test1(self):
        print("test merge")
    def testsdet(self):
        print("test sdet")


