from time import sleep
from selenium import webdriver
def getFile(url):
    chrome=webdriver.Chrome()
    chrome.get(url)
    texts = chrome.find_elements_by_xpath("//div[@class='readAreaBox content']/div")
    for t in texts:
        a=open('小说.txt','a',encoding='utf-8')
        a.write(t.text+'\n')
        a.close()
    sleep(1)
    next_url=chrome.find_elements_by_xpath("//a[@class='nextChapter']")
    if next_url:
        next_urls=next_url[0].get_attribute("href")
        chrome.close()
        getFile(next_urls)
    else:
        chrome.close()
        return

if __name__=='__main__':
    getFile("https://www.17k.com/chapter/2849619/35312236.html")

