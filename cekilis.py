from selenium import webdriver
from bs4 import BeautifulSoup
import time
import random
import colorama
from colorama import Fore, Back, Style
from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "",
    aciklama = "",
    banner   = "Cekilis Botu",
    girinti  = 1
)


taban.log_salla('KekikAkademi', 'selmankahya', 'kadirilgin1453'

)
konsol = taban.konsol
from rich.style import Style





ytLiveChatURL = input(Fore.GREEN + "Lütfen Canlı Yayın Linkinizi Giriniz >>>>>> ")
keyword = input(Fore.GREEN + "Lütfen Çekiliş İçin Seçtiğiniz Kelimeyi Giriniz >>>>>>>>>> ")
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
    print(Fore.CYAN + "Cekilis basliyor! {totalUserCount} kisi hak kazandi.".format(
        totalUserCount=len(eligibleUsersList)))

    time.sleep(3)
    for i in range(1, 5):
        noktalar = i * "."
        print(Fore.CYAN + "Rastgele Bir Sayı Çekiliyor" + noktalar)
        time.sleep(1.5)

    print(Fore.CYAN + "Hazır Mısınız?")
    time.sleep(1.5)
    print(Fore.CYAN + "Son kontrolleri yapıyorum..")
    time.sleep(1.5)
    print(Fore.CYAN + "Bugun nasılsın?")
    time.sleep(1.5)
    print(Fore.CYAN + "Son son kontrolleri yapıyorum..")
    print(Fore.CYAN + "{totalUserCount} kişi arasından kazanan:".format(
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
