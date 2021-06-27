from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
import sys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.cowin.gov.in")
driver.maximize_window()


def main():
    time.sleep(5)

    search_location()
    find_doses()


def find_doses():
    #/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[7]/div/div/div/div[2]
    centers = driver.find_elements_by_xpath("/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[7]/div/div/div/div")
    print(centers)
    # for i in centers:
    #     days = i.find_elements_by_class_name("ng-star-inserted")
    #     for j in days:
    #         dose1 = i.find_element_by_xpath("//div/div/div[2]/ul/li[2]/div/div/div[1]/span[1]").text
    #         # if "1" in text:
    #         #     print("Somethig found")
    #         #     # print the hospital name
    #         #     hosp_name = i.find_element_by_class_name("center-name-title")
    #         #     print(hosp_name)
    #         print(dose1)

def search_location():
    # click on 'search by district'
    search_by_district = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div"))
        )   
    search_by_district.click()

    # select state
    select_state = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[1]/mat-form-field/div/div[1]/div/mat-select")))
    select_state.click()
    scroll_box = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div")
    for i in range(3):
        scroll_box.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    maharashtra = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[22]/span")
    maharashtra.click()

    time.sleep(2)

    # select district
    select_district = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[2]/mat-form-field/div/div[1]/div/mat-select"))
    )
    select_district.click()
    scroll_box2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div")
    for i in range(4):
        scroll_box2.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    pune = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div/mat-option[25]/span")
    pune.click()

    search = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/form/mat-tab-group/div/mat-tab-body[2]/div/div/div[3]/button")
    search.click()
    time.sleep(1)
    age_group = driver.find_element_by_xpath("/html/body/app-root/div/app-home/div[3]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/div[1]/label")
    age_group.click()


main()
