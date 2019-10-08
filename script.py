#!/usr/bin/env python3
from bs4 import BeautifulSoup
from csv import writer
from selenium import webdriver
import time
import random

url  = "https://www.instagram.com/accounts/login/"
url_follower = "url_page_to_follow"

def open_browser():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path='/snap/bin/chromium.chromedriver',options=options) # change the executable_path
    try:
        browser.get(url)
        print("Ouverture du site...")
    except Exception as e:
        print("erreur de connection a instagram")
        browser.close()
    return browser


def connection(brows,user,password):
    print("connection...")
    for k in range(5):
        time.sleep(1)
        print(k)
    try:
        brow.find_element_by_name("username").send_keys(user)
        brow.find_element_by_name("password").send_keys(password)
        brow.find_element_by_class_name("sqdOP.L3NKy").click()
    except Exception as e:
        print("erreur de la connection du compte instagram")

def follow(brows,url_compte):

    compte = 0
    i =0
    try:

        #ouverture de la page
        brows.get(url_compte)
        time.sleep(2)
        print("click des followers")
        #affichage des followers
        fol = brows.find_element_by_xpath("//a[@class='-nal3 ']")

        fol.click()

        time.sleep(2)

        brows.execute_script("var list = document.getElementsByClassName('isgrP'); list[0].scrollTo(0,600);")

        while(1):

            time.sleep(2)
            blocs = brows.find_elements_by_xpath("//button[@class='sqdOP  L3NKy       ']")
            blocs_a =brow.find_elements_by_class_name("L3NKy")

            for rang in range(i,len(blocs)):
                print("taille du bloc = " , len(blocs),rang)
                try:
                    blocs[rang].click()
                    compte+=1
                    print(compte , " compte ")
                    for k in range(int(random.uniform(25,30))):
                        time.sleep(1)
                        print(k)
                except Exception as e:
                    print("erreur d'abonnement")



            js = "var list = document.getElementsByClassName('isgrP'); list[0].scrollTo(0,"+str(len(blocs_a)*50)+");"
            brows.execute_script(js)
            if(compte%100==0):
                time.sleep(60*20)


    except Exception as e:
        print("erreur de louverture de la page")
        print(e)




brow = open_browser()
connection(brow, "username_instagram", "password_instagram")
time.sleep(2)
follow(brow, url_follower)
