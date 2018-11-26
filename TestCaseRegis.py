__author__ = 'jasmine'

from selenium import webdriver
import unittest
import os
import HTMLTestRunner
import time
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class TestCaseFFRegisInvalidFormat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome('/var/www/html/TestingTurnamenFF/Driver/chromedriver')
        self.driver.get('https://turnamen.ff.garena.co.id/invitational/registration/')

    def testInValidFormat(self):
        try:
            
            driver = self.driver
            # driver.execute_script("$('#login img').find('img[src$='assets/img/icon_web/icon_bigwhitefb.png'].click()")
            # driver.execute_script("//*[@id='login']/img[@src='assets/img/icon_web/icon_bigwhitefb.png'")
            driver.find_element_by_xpath("//*[@id='login']/img").click()

            userfb = driver.find_element_by_id('email')
            userfb.send_keys('webdevgarena@gmail.com')

            passfb = driver.find_element_by_id('pass')
            passfb.send_keys('garenawebdev')

            btnfb = driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

            time.sleep(5)

            nama = driver.find_element_by_name('team_name')
            nama.send_keys('testingdev')

            guild_id = driver.find_element_by_name('guild_id')
            guild_id.send_keys('869685038')

            nama_guild = driver.find_element_by_name('guild_name')
            nama_guild.send_keys('testerdevweb')

            nama_kapten = driver.find_element_by_name('nama_lengkap_1')
            nama_kapten.send_keys('developertester')

            no_identitas_kapten = driver.find_element_by_name('no_id_1')
            no_identitas_kapten.send_keys('3216054910980010')

            telp = driver.find_element_by_name('no_telp')
            telp.send_keys('087887123010')

            email = driver.find_element_by_name('email')
            email.send_keys('webdevgarena@gmail.com')

            discord_id = driver.find_element_by_name('discord_username')
            discord_id.send_keys('acc_1234')

            domisili = driver.find_element_by_name('domisili_1')
            domisili.send_keys('jakarta')

            anggota1 = driver.find_element_by_name('nama_lengkap_2')
            anggota1.send_keys('testersatu')

            no_identitas_anggota1 = driver.find_element_by_name('no_id_2')
            no_identitas_anggota1.send_keys('3217098709760098')

            domisili_anggota1 = driver.find_element_by_name('domisili_2')
            domisili_anggota1.send_keys('bekasi')

            no_id_anggota1 = driver.find_element_by_name('account_id_2')
            no_id_anggota1.send_keys('123489796')

            validate_anggota1 = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[2]/div[3]/div/div/div[4]/div/div/div/button').click()
            time.sleep(1)
            popup = driver.find_element_by_xpath('//*[@id="errorModal"]/div/div/div/button/img').click()
            time.sleep(1)

            anggota2 = driver.find_element_by_name('nama_lengkap_3')
            if anggota2 is None:
                print("eror")
            else:
                anggota2.send_keys('hahaetestng')
            
            no_identitas_anggota2 = driver.find_element_by_name("no_id_3")
            no_identitas_anggota2.send_keys('3216785938754097')
            time.sleep(5)

            domisili_anggota2 = driver.find_element_by_name("domisili_3").send_keys("Lampung Selatan")
            time.sleep(5)

            no_id_anggota2 = driver.find_element_by_name('account_id_3')
            no_id_anggota2.send_keys("04043745922")

            validate_anggota2 = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[2]/div[4]/div/div/div[4]/div/div/div/button').click()
            time.sleep(5)
            pop2 = driver.find_element_by_xpath('//*[@id="errorModal"]/div/div/div/button/img').click()
            time.sleep(5)

            anggota3 = driver.find_element_by_name('nama_lengkap_4')
            anggota3.send_keys('testingtigaa')

            no_identitas_anggota3 = driver.find_element_by_name('no_id_4')
            no_identitas_anggota3.send_keys('321806576196643')

            domisili_anggota3 = driver.find_element_by_name("domisili_4").send_keys("Banjarmasin")
            time.sleep(1)

            no_id_anggota3 = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[2]/div[5]/div/div/div[4]/div/div/input')
            no_id_anggota3.send_keys('097869608')
            time.sleep(10)
            
            validate_anggota3 = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[2]/div[5]/div/div/div[4]/div/div/div/button').click()
            time.sleep(5)

            pop3 = driver.find_element_by_xpath('//*[@id="errorModal"]/div/div/div/button/img').click()
            time.sleep(1)

            cadangan = driver.find_element_by_name('nama_lengkap_5')
            cadangan.send_keys('testerkeempat')
            time.sleep(1)

            no_identitas_cadangan = driver.find_element_by_name('no_id_5')
            no_identitas_cadangan.send_keys('34856993')
            time.sleep(1)

            domisili_cadangan = driver.find_element_by_name('domisili_5')
            domisili_cadangan.send_keys('banten')
            time.sleep(1)

            no_id_cadangan = driver.find_element_by_name('account_id_5')
            no_id_cadangan.send_keys('3740573027')
            time.sleep(1)

            validate_cadangan = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[2]/div[6]/div/div/div[4]/div/div/div/button').click()
            time.sleep(1)

            popcad = driver.find_element_by_xpath('//*[@id="errorModal"]/div/div/div/button/img').click()
            time.sleep(1)

            checkboxes = driver.find_element_by_xpath('//*[@id="understanding"]').click()
            time.sleep(5)
            btnKirim = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[4]/div[2]/button').click()
            time.sleep(2)
            pop4 = driver.find_element_by_xpath('//*[@id="errorModal"]/div/div/div/button/img').click()
            time.sleep(3)

            logout = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[1]/div/div/a').click()
            time.sleep(5)

            def is_element_present(self, how, what):

                try: self.driver.find_element(by=how, value=what)
                except NoSuchElementException as e: return False
                return True
    
            def is_alert_present(self):
                try: self.driver.switch_to_alert()
                except NoAlertPresentException as e: return False
                return True
    
            def close_alert_and_get_its_text(self):

                try:

                    alert = self.driver.switch_to_alert()
                    alert_text = alert.text
                    if self.accept_next_alert:
                        alert.accept()
                    else:
                        alert.dismiss()
                    return alert_text
        
                finally: self.accept_next_alert = True
        
        except AssertionError as error :
            logging.log_exception(error)
        
        finally:
            self.driver.quit()
    
    def testbtnregulasi(self):
        try:
            driver = self.driver

            driver.find_element_by_xpath("//*[@id='login']/img").click()

            userfb = driver.find_element_by_id('email')
            userfb.send_keys('webdevgarena@gmail.com')

            passfb = driver.find_element_by_id('pass')
            passfb.send_keys('garenawebdev')

            btnfb = driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

            time.sleep(5)
            btnRegulasi = driver.find_element_by_xpath('//*[@id="daftar"]/form/div[4]/div[1]/a').click()
            time.sleep(5)

        except AssertionError as error:
            logging.log_exception(error)

        finally:
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()








