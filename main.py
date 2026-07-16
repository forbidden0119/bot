import os
import requests
from bs4 import BeautifulSoup

TARGET_URLS = [
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ポケモンカード&psc=0",
    "https://aeonretail.com/Form/Product/ProductList.aspx?gspsk=ワンピースカード&psc=0"
]

def main():
    for url in TARGET_URLS:
        res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # ページ全体のテキストを少しだけ表示して、サイトがちゃんと取れているか確認する
        print(f"--- サイトチェック: {url} ---")
        # ページ内の「商品」と思われる要素をできるだけ広く拾う
        items = soup.find_all(class_=lambda x: x and ('product' in x))
        print(f"検知した関連要素数: {len(items)}")
        
        # 最初の3つだけ名前を表示して、何が取れているか確認
        for i, item in enumerate(items[:3]):
            print(f"中身{i+1}: {item.text.strip()[:30]}...")

if __name__ == "__main__":
    main()
