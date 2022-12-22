import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_Loginpage import DpWorkLoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_001_Login:
    dpwork_url=readConfig.getDpWorkUrl()
    logger=LogGen.loggen()
    dpwork_loginpage_SS_folder='dpWorkLoginPageSSFolder'

    def test_DpWorkLoginPage(self, setup):
        try:
            self.driver=setup
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.dplp=DpWorkLoginPage(self.driver)
            
            
            self.logger.info("**********************************************Test_001_Login***************************************************")
            self.logger.info("**********************************************DpWork Login Page Testing***************************************************")
            
            self.driver.get(self.dpwork_url)
            self.logger.info("**********************************************Request DP Work QA URL***************************************************")

            filename='.//testData//DpWorkDataParameterization.xlsx'
            sheetname='LoginPage'
            rowNum=XLUtils.getRowCount(filename, sheetname)
            colNum=XLUtils.getColCount(filename, sheetname)
            
            dataset=XLUtils.getDataIn2DList(filename,sheetname,rowNum, colNum)
            self.logger.info("**********************************************Get Data from Excel File***************************************************")
            
            location=self.dplp.createDedicatedSSFolder(self.dpwork_loginpage_SS_folder)

            self.dplp.waitForLoginPage()
            location0=location+'Login Page- SS-00.png'

            self.driver.save_screenshot(location0)

            for data in dataset:
                username=data[0]
                password=data[1]
                expectedResult=data[2]
                

                self.dplp.setDpWorkUserName(username)
                self.logger.info("**********************************************Username Entered- {}***************************************************".format(username))
                self.dplp.setDpWorkPassword(password)
                self.logger.info("**********************************************Corresponding Password Entered***************************************************")

                location1=location+str(username)+'- SS-01.png'
                self.driver.save_screenshot(location1)

                self.dplp.clickLoginButton()
                self.logger.info("**********************************************Click on login button***************************************************")

                if expectedResult=='Fail':
                    self.dplp.errorMessage()
                    self.logger.info("**********************************************Message displayed***************************************************")
                    
                    location2=location+str(username)+'-Display Message- SS-02.png'
                    self.driver.save_screenshot(location2)

                    self.dplp.closeErrorMessage()

                elif expectedResult=='Pass':
                    self.dplp.clickMenu()

                    location3=location+str(username)+'-LogOut- SS-02.png'
                    self.driver.save_screenshot(location3)

                    self.dplp.clickLogoutButton()
                    self.logger.info("**********************************************Click on Logout button***************************************************")
                    time.sleep(2)
                time.sleep(1)
            self.logger.info("**********************************************Test_001_Login- Passed***************************************************")
            assert True

        except:
            self.logger.info("**********************************************Test_001_Login- Failed***************************************************")
            assert False


    

