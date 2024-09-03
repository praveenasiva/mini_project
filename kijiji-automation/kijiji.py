from selenium import webdriver
import time
from bs4 import BeautifulSoup


browser = webdriver.Chrome('/home/praveena/Downloads/chromedriver')
file1 = open("myfile.txt","w")


browser.get('https://www.kijiji.ca/b-cars-trucks/city-of-toronto/car/sedan-honda-2010__2020-used/k0c174l1700273a138a54a68a49?no-of-doors=4&transmission=2&kilometers=60000__150000')

browser.maximize_window()
for i in range(4,6):
    browser.find_element_by_xpath("/html/body/div[3]/div[3]/div[3]/div[3]/div[3]/div[{}]/div[1]/div[2]/div/div[2]/a".format(str(i))).click()
    time.sleep(50)

    res=browser.execute_script("return document.documentElement.outerHTML")
    html_soup = BeautifulSoup(res, 'lxml')
    text = html_soup.find('h1' ,{'class' : 'title-2323565163'})
    a=text.get_text()
    file1.writelines("\n"+a+"\n")

    desc=html_soup.find('div',{'class':'descriptionContainer-3261352004'})
    b=desc.get_text()
    file1.writelines(b+"\n\n")

    browser.get('https://www.kijiji.ca/b-cars-trucks/city-of-toronto/car/sedan-honda-2010__2020-used/k0c174l1700273a138a54a68a49?no-of-doors=4&transmission=2&kilometers=60000__150000')
    time.sleep(10)
    for i in range(30):
        print("-",end="")
        file1.write("-")
file1.close()