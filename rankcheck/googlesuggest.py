import argparse
from time import sleep
from string import ascii_lowercase
from string import digits
import requests
import urllib.parse
from google import search
from retry import retry

class GoogleAutoComplete:
    @retry()
    def __init__(self, test_mode=False, recurse_mode=False):
        self.base_url = 'https://www.google.co.jp/complete/search?'\
                        'hl=ja&output=toolbar&ie=utf-8&oe=utf-8&'\
                        'client=firefox&q='
        self.test_mode = test_mode
        self.recurse_mode = recurse_mode
        if test_mode:
            self.chrs = ['あ', 'g', '1']
        else:
            self.chrs = [chr(i) for i in range(ord('ぁ'), ord('ん'))]
            self.chrs.extend(ascii_lowercase)
            self.chrs.extend(digits)

    @retry()
    def get_suggest(self, query):
        buf = requests.get(self.base_url +
                           urllib.parse.quote_plus(query)).json()
        suggests = [ph for ph in buf[1]]
        print("query: [{0}]({1})".format(query, len(suggests)))
        for ph in suggests:
            print(" ", ph)
            sleep(0.1)
        return suggests

    @retry()
    def get_suggest_with_one_char(self, query):
        # キーワードそのものの場合のサジェストワード
        ret = self.get_suggest(query)

        # キーワード＋空白の場合のサジェストワード
        ret.extend(self.get_suggest(query + ' '))

        # キーワード＋空白＋1文字の場合のサジェストワード
        for ch in self.chrs:
            ret.extend(self.get_suggest(query + ' ' + ch))
        # -rオプションがあればもう1段階
        """
        if self.recurse_mode:
            ret = self.get_uniq(ret)  # 事前に重複を除いておく
            addonelevel = []
            for ph in ret:
                addonelevel.extend(self.get_suggest(ph + ' '))
            ret.extend(addonelevel)"""

        return self.get_uniq(ret)

    # 重複を除く
    def get_uniq(self, arr):
        uniq_ret = []
        for x in arr:
            if x not in uniq_ret:
                uniq_ret.append(x)
        return uniq_ret

@retry()
def do_key2url(key,i,urls):
    i = i+1
    for url in search(key, lang="jp", pause=4.0, num=10, user_agent="Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)"):
        urls += [url]
        print(url)
        if len(urls) == 31 * i:
            break
    return urls,i

def key2url(keys):
    i=0
    urls = []
    print(keys+"の上位30件のURLを取得します。")
    urls,i = do_key2url(keys,i,urls)
    #for key in list(keys):
        #print(key+"の上位3０件のURLを取得します。")
        #urls,i = do_key2url(key,i,urls)
    return urls

def googlesuggest(phrase):
    #keys = []
    # Google Suggest キーワード取得
    #gs = GoogleAutoComplete(recurse_mode = "--recure")
    #print(phrase+"のサジェストを取得します。")
    #ret = gs.get_suggest_with_one_char(phrase)
    #for key in ret:
        #keys.append(key)
    #print(phrase+"のサジェスト取得が完了しました。")
    #print(phrase+"サジェストごとのURLを取得します。")
    #urls = key2url(keys)
    urls = key2url(phrase)
    #print(phrase+"サジェストごとのURL取得を完了しました。")
    return urls
