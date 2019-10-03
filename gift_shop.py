from pprint import pprint
from selenium import webdriver
from bs4 import BeautifulSoup
browser = webdriver.Chrome("/home/kapil/Desktop/express/chromedriver")
url='https://www.justdial.com/Delhi/Gift-Stores/nct-10231352/page-1'
browser.get(url)


from selenium.webdriver.common.keys import Keys
import time
elm=browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(5)
elm.send_keys(Keys.HOME)

response = browser.execute_script('return document.documentElement.outerHTML')
soup=BeautifulSoup(response,'html.parser')
main_div=soup.find('ul',class_="rsl col-md-12 padding0")
li=main_div.find_all("li",class_="cntanr")
all_data=[]
for i in li:
    dic={}
    # for name 
    name=i.find("div",class_=" col-sm-5 col-xs-8 store-details sp-detail paddingR0").h2.span.a.text
    dic["name"]=name
    # for contact number
    try:
        contact_span=i.find("p",class_="contact-info ").a.find_all('span')
        contact_no=""
        dic_contact={'icon-dc':'+','icon-fe':'(','icon-hg':')','icon-ba':'-','icon-acb':'0','icon-yz':'1','icon-wx':'2','icon-vu':'3','icon-ts':'4','icon-rq':'5','icon-po':'6','icon-nm':'7','icon-lk':'8','icon-ji':'9'}
        for j in contact_span:
            b=dic_contact[(j)['class'][1]]
            contact_no+=b
    except AttributeError:
        contact_no=""
        pass
    dic["contact"]=contact_no

    # for rating
    rating=i.find("p",class_="newrtings ").find("span","green-box").text
    dic["rating"]=rating

    # for address
    add_div=i.find('p',class_='address-info tme_adrssec').a.text.split()
    add_div.remove('more..')
    address=""
    for w in add_div:
        address+=(w+" ")
    dic["address"]=address

    # for image link
    image_div=i.find('div',class_="thumb_img").a['href']
    dic["image"]=image_div

    all_data.append(dic.copy())
pprint(all_data)
user=str(input("close page or not--y/n"))
browser.quit()
print ("closed")