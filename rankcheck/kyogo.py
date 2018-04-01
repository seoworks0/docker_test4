import urllib.request, urllib.error
from urllib.request import Request, urlopen
from urllib.error import URLError
import sys
from .googlesuggest import googlesuggest
from bs4 import BeautifulSoup
import pandas as pd
from retry import retry
import ssl


ssl._create_default_https_context = ssl._create_unverified_context


def url2text(urls):
    text = []
    text2 = []
    list4 = []
    list6 = ""
    j = 0
    for i,url in enumerate(urls):
        if j ==0:
            j = 1
        else:
            print(url+"の内容を取得しています。")
            html = url_req(url)
            text_title,text_h1 = soup(html)
            list5 = [i,url,text_title,text_h1]
            list4 += [list5]
    return list4

@retry()
def url_req(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    req.add_header('Host', req.host.encode('idna'))
    html = urllib.request.urlopen(req)
    return html

def soup(html):
    soup = BeautifulSoup(html, "html.parser")
    soup_title = soup.find_all("title")
    soup_h1 = soup.find_all("h1")

    maped_list_h1 = map(str, soup_h1)
    soup1_h1 = ', '.join(maped_list_h1)
    soup2_h1 = BeautifulSoup(soup1_h1, "html.parser")
    text_h1 = soup2_h1.get_text()
    maped_list_title = map(str, soup_title)
    soup1_title = ', '.join(maped_list_title)
    soup2_title = BeautifulSoup(soup1_title, "html.parser")
    text_title = soup2_title.get_text()
    text_h1 = text_h1.replace(" ","")
    text_h1 = text_h1.replace("　","")
    text_h1 = text_h1.replace('\n',"")
    text_title = text_title.replace(" ","")
    text_title = text_title.replace("　","")
    text_title = text_title.replace('\n',"")
    return text_title,text_h1

#def makelist


def main(phrase):
    urls = googlesuggest(phrase)
    list4 = url2text(urls)
    df = pd.DataFrame(list4,columns=["順位","URL","タイトル","h1"])
    df.to_csv("file/sample.csv",encoding="UTF-8")
    return list4
