import os
from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DpWorkLoginPage:
    text_username_Xpath='//*[@id="mat-input-0"]'
    text_password_Xpath='//*[@id="mat-input-1"]'
    button_loginButton_Xpath='//*[@class="mat-focus-indicator mat-raised-button mat-button-base mat-primary"]'
    text_errorMessage_Xpath='//*[contains(text(),"No such user found. Please check your email.")]'
    button_menu_Xpath='//*[@class="mat-focus-indicator mat-icon-button mat-button-base ng-star-inserted"]'
    button_logout_Xpath='//*[@class="mat-list-item-content"]'
    button_closeErrorMessage_Xpath='//*[@class="mat-focus-indicator mat-button mat-button-base"]'

    def __init__(self,driver):
        self.driver=driver

    def click_unitil_interactable(self,element) -> bool:
        element_is_interactable=False
        counter=1
        if element:
            while not element_is_interactable:
                try:
                    element.click()
                    element_is_interactable=True
                except(ElementClickInterceptedException,ElementNotInteractableException,StaleElementReferenceException):
                    counter=counter+1
        return element_is_interactable

    def waitForLoginPage(self):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.text_username_Xpath)))

    def setDpWorkUserName(self, username):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.text_username_Xpath)))
        self.driver.find_element(By.XPATH, self.text_username_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_Xpath).send_keys(username)
    
    def setDpWorkPassword(self, password):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.text_password_Xpath)))
        self.driver.find_element(By.XPATH, self.text_password_Xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_Xpath).send_keys(password)
        
    def clickLoginButton(self):
        #WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_loginButton_Xpath)))
        time.sleep(1)
        self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_loginButton_Xpath))

    def errorMessage(self):
        time.sleep(1)
        WebDriverWait(self.driver,100).until(EC.presence_of_element_located((By.XPATH, self.text_errorMessage_Xpath)))
        time.sleep(1)

    def closeErrorMessage(self):
        self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_closeErrorMessage_Xpath))

    def clickMenu(self):
        time.sleep(1)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_menu_Xpath)))
        self.click_unitil_interactable(self.driver.find_element(By.XPATH,self.button_menu_Xpath))

    def waitforLogoutButton(self):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_logout_Xpath)))   

    def clickLogoutButton(self):
        time.sleep(1)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH, self.button_logout_Xpath)))
        logging_out=self.driver.find_elements(By.XPATH,self.button_logout_Xpath)
        self.click_unitil_interactable(logging_out[-1])
        time.sleep(1)

    def createDedicatedSSFolder(self,foldername):
        os.chdir(".//screenshots")
        SS=foldername
        try:
            mkdir="mkdir {0}".format(SS)
            os.system(mkdir)
        except:
            pass
        location=os.getcwd()+'\\'+str(SS)+'\\'
        return location
