from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random

ytLiveChatURL = "https://www.youtube.com/live_chat?v=mxTiT2igK7A"
keyword = "turkcedev"
eligibleUsers = set()

# start web browser
browser = webdriver.Firefox()


def getHTML(url):
   # get source code
    browser.get(ytLiveChatURL)
    time.sleep(1)
    page_source = browser.page_source
    return page_source


def parseHTML(html_source):
    return BeautifulSoup(html_source, 'html.parser')


def getMessages(soup):
    return soup.find_all("yt-live-chat-text-message-renderer")


def updateEligibleUsers(messages):
    for message in messages:
        content = message.find("div", {"id": "content"})
        author = content.find("span", {"id": "author-name"}).text
        message_content = content.find("span", {"id": "message"}).text
        if keyword in message_content.lower():
            eligibleUsers.add(author)


def startDrawing(eligibleUsersList):
    print("Cekilis basliyor! {totalUserCount} kisi hak kazandi.".format(
        totalUserCount=len(eligibleUsersList)))

    time.sleep(3)
    for i in range(1, 5):
        noktalar = i * "."
        print("Rasgele bir sayi cekiliyor" + noktalar)
        time.sleep(1.5)

    print("Hazir misiniz?")
    time.sleep(1.5)
    print("Son kontrolleri yapiyorum..")
    time.sleep(1.5)
    print("Bugun nasilsin?")
    time.sleep(1.5)
    print("Son son kontrolleri yapiyorum..")
    print("{totalUserCount} kisi arasindan kazanan:".format(
        totalUserCount=len(eligibleUsersList)), random.choice(eligibleUsersList))


def main():
    for i in range(0, 7):
        html_source = getHTML(ytLiveChatURL)
        soup = parseHTML(html_source)
        messages = getMessages(soup)
        updateEligibleUsers(messages)
        print("{count} kisi cekilise katilmis durumda.".format(
            count=len(eligibleUsers)))
        time.sleep(10)

    eligibleUsersList = list(eligibleUsers)
    startDrawing(eligibleUsersList)
    browser.close()


main()
