from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome('/chromedriver.exe')

driver.implicitly_wait(3)

keyword = "카지노"
domainUrl = "https://torrentsome82.com"
url = "{0}/search/index?keywords={1}&search_type=0&order=time".format(domainUrl, keyword)

driver.get(url)

html = driver.page_source

soup = BeautifulSoup(html, "html.parser")

contentsBox =  soup.find("div", class_= "grid grid-cols-1 pb-2" )

contents = contentsBox.find_all("div", class_="py-4 flex flex-row border-b topic-item")

for content in contents:
    title = content.select_one("div.flex-auto.px-2.truncate > a")
    contentPath = domainUrl + title['href']
    title.find('span').decompose()
    
    volume = content.select_one("div.flex-none.w-16.text-center").text.strip()
    date = content.select_one("div.flex-none.w-16.text-center.hidden").text.strip()

    print(title.text.strip())
    print(contentPath)
    print(volume)
    print(date)