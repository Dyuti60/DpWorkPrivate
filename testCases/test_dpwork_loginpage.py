import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.dpwork_Loginpage import DpWorkLoginPage
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from utilities import docsUtil
from utilities import emailUtil
import time

class Test_001_Login:
    dpwork_url=readConfig.getDpWorkUrl()
    logger=LogGen.loggen()
    dpwork_loginpage_SS_folder='dpWorkLoginPageSSFolder'
    dpwork_loginpage_documentation_filename='dpWorkLoginPageTestingDocumentation'

    sender=readConfig.getEmailSender()
    receivers=readConfig.getEmailReceivers()
    attachment1='automation.log'
    attachment2='dpWorkLoginPageTestingDocumentation.docx'
    attachment3='DPWorkLoginPageTestReport.html' 

    
    def test_DpWorkLoginPage(self, setup):
        try:
            self.driver=setup
            self.driver.implicitly_wait(10)
            self.driver.maximize_window()
            self.dplp=DpWorkLoginPage(self.driver)
            document=docsUtil.createDocxFile()
            count=1
            docsUtil.addMainHeading(document,"DP Work Login Functionality Testing Documentation")
            
            self.logger.info("**********************************************Test_001_DP Worker Login***************************************************")
            self.logger.info("**********************************************DP Work Login Page Testing***************************************************")
            
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

            ss0_location=self.dplp.takeAndSaveScreenshotUnique(location,'DP Work Login Page','00')
            docsUtil.addMediumHeading(document,"DP Work Login Page:")
            docsUtil.insertImageInDocx(document,ss0_location)

            for data in (dataset):
                username=data[0]
                password=data[1]
                expectedResult=data[2]
                

                self.dplp.setDpWorkUserName(username)
                self.logger.info("**********************************************Username Entered- {}***************************************************".format(username))
                self.dplp.setDpWorkPassword(password)
                self.logger.info("**********************************************Corresponding Password Entered***************************************************")

                self.dplp.takeAndSaveScreenshotCommon(location,username,'01')

                self.dplp.clickLoginButton()
                self.logger.info("**********************************************Click on login button***************************************************")

                if expectedResult=='Fail':
                    self.dplp.errorMessage()
                    self.logger.info("**********************************************Message displayed***************************************************")
                    
                    self.dplp.takeAndSaveScreenshotCommon(location,username,'02')

                    self.dplp.closeErrorMessage()

                elif expectedResult=='Pass':
                    self.dplp.clickMenu()
                    time.sleep(1)
                    self.dplp.takeAndSaveScreenshotCommon(location,username,'02')

                    self.dplp.clickLogoutButton()
                    self.logger.info("**********************************************Click on Logout button***************************************************")
                    time.sleep(2)

                #documentation:
                userloginevidences=self.dplp.collectScreenshot(self.dpwork_loginpage_SS_folder,username)
                docsUtil.addMediumHeading(document,"Scenario")
                docsUtil.appendContent(document,"DP worker username - {}".format(username))
                docsUtil.appendContent(document,"DP worker password - {}".format(password))
                docsUtil.appendContent(document,"Scenario expected result - {}".format(expectedResult))
                docsUtil.addMediumHeading(document,"User login into DpWork Portal")
                docsUtil.insertImageInDocx(document,userloginevidences[0])
                docsUtil.addMediumHeading(document,"User clicks on the login button")
                docsUtil.appendContent(document,"Scenario actual result:")
                docsUtil.insertImageInDocx(document,userloginevidences[1])
                self.dplp.deleteScreenshots(self.dpwork_loginpage_SS_folder,username)
                self.dplp.deleteScreenshots(self.dpwork_loginpage_SS_folder,"DP Work Login Page")
                time.sleep(1)
            docsUtil.saveDocument(document,self.dpwork_loginpage_documentation_filename)
            
            emailUtil.sendEmail(self.sender,self.receivers,self.attachment1, self.attachment2, self.attachment3)
            
            self.logger.info("**********************************************Test_001_Login- Passed***************************************************")
            assert True

        except:
            self.logger.info("**********************************************Test_001_Login- Failed***************************************************")
            assert False


    

